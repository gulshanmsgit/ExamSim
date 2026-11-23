"""Most important GPSTR topics, subject-wise, from ALL real previous-year questions in the bank (owner, 23 Nov 2026: "prepare
the most important topics for Paper 1 and Paper 2 … subject-wise").

Every real question (one with a `source`, "<paper> · Q<n>") is counted ONCE – keyed by its source, so a bilingual KEA paper's
English and Kannada copies count once – under a GPSTR subject and syllabus topic, taken from (first that applies):
  1. a GPSTR topic pack (the topic it was filed under);
  2. a KRIES Paper 1 pack (KEA GK questions in Kannada) – mapped by topic_priority_kw.KRIES;
  3. the previous-year papers sorted by subject/unit (pyq-by-subject.json, KEA GK/KEC paper sections) – topic by keyword
     rules topic_priority_kw.KW; a question no rule matches is NOT counted (the by-unit files also hold PGCET MCA
     aptitude/English/GK items filed under a unit only as a fallback).
Questions not on the GPSTR syllabus (PGCET MCA maths/reasoning, KSET Education philosophy/sociology/research, KRIES
reasoning/arithmetic …) are not counted.
Within a subject, topics are ranked by real questions: "must" = the top topics holding about half of the subject's sorted
questions (≥ 3 each, at most 4), "important" = the next ones up to about 80 % (≥ 2 each, at most 5), the rest "revise".
Writes packs/topic-priority.json (read by the app's Subjects tab). Usage: python tools/topic_priority.py
"""
import collections
import datetime
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_subject_mocks as bsm  # noqa: E402
import mock3_pyq as m3  # noqa: E402
import mock_pyq_more as mm  # noqa: E402
from topic_priority_kw import KW, KRIES  # noqa: E402

MONTHS = "Monthly current affairs (Jan–Oct 2026)"
MIXED = "Previous-year questions (mixed topics)"
OUT = ROOT / "packs" / "topic-priority.json"


def skey(q):
    return re.sub(r"\s+", " ", q["source"]).strip()


def load(f):
    return json.loads((ROOT / "packs" / f).read_text(encoding="utf-8"))


def main():
    plan = load("gpstr-cst-2026-plan.json")
    marks = {}

    def find(o):
        if isinstance(o, dict):
            for k, v in o.items():
                marks.update(v) if k == "marks" else find(v)
        elif isinstance(o, list):
            for x in o:
                find(x)
    find(plan)

    subjects = collections.OrderedDict()  # subject name → {paper, library, key, marks, est, topics: [names], tmap}
    for paper, rows in (("P1", bsm.P1), ("P2", bsm.P2)):
        for show, lib, files, key in rows:
            name = show.split(" · ", 1)[1]
            mk = marks[name] if paper == "P1" else next(v for k, v in marks.items() if k.startswith(name.split(" – ")[0] + " "))
            names, tmap = [], {}
            for f in files:
                for s in load(f)["subjects"]:
                    if s["name"] == lib:
                        for t in s["topics"]:
                            nm = t["name"] if (t.get("plan") or name != "Current Affairs") else MONTHS
                            tmap[t["name"]] = nm
                            if nm not in names:
                                names.append(nm)
            subjects[name] = {"paper": paper, "library": lib, "files": files, "key": key, "marks": mk, "est": paper == "P2",
                              "names": names, "tmap": tmap}
    by_key = {v["key"]: k for k, v in subjects.items()}

    assigned = {}  # source → (subject, topic or None, paper of source)

    def put(q, subj, topic):
        if not q.get("source") or q["source"] in m3.EXCLUDE:
            return
        k = skey(q)
        old = assigned.get(k)
        if old is None or (old[1] is None and topic is not None):
            assigned[k] = (subj, topic, q["source"].rsplit(" · Q", 1)[0])

    def classify(subj, q):
        rules = KW.get(subj) or KW.get(subjects[subj]["key"]) or []
        text = q["question"] + " " + " ".join((q.get("options") or {}).values())
        return next((t for t, rx in rules if re.search(rx, text, re.I)), None)

    # 1. GPSTR topic packs
    for subj, d in subjects.items():
        for f in d["files"]:
            for s in load(f)["subjects"]:
                if s["name"] != d["library"]:
                    continue
                for t in s["topics"]:
                    for st in t["sets"]:
                        for q in st["questions"]:
                            put(q, subj, d["tmap"][t["name"]])
    # 2. KRIES Paper 1 packs (KEA GK questions)
    for f in sorted((ROOT / "packs").glob("p1-kries*.json")):
        for s in json.loads(f.read_text(encoding="utf-8"))["subjects"]:
            for t in s["topics"]:
                rule = next((r for r in KRIES if re.search(r[0], s["name"]) and re.search(r[1], t["name"])), None)
                tgt = rule[2] if rule else None
                if tgt is None:
                    continue
                for st in t["sets"]:
                    for q in st["questions"]:
                        if tgt == "KW":
                            top = classify("General Knowledge", q)
                            if top:
                                put(q, "General Knowledge", top)
                        else:
                            put(q, *tgt)
    # 3. papers sorted by subject / unit, and the KEA GK / KEC paper sections
    by = load("pyq-by-subject.json")
    for s in by["subjects"]:
        for t in s["topics"]:
            m = re.match(r"Unit (\d+)", t["name"])
            subj = by_key.get(int(m.group(1))) if m else (t["name"] if t["name"] in subjects else
                                                         "General Knowledge" if "KRIES" in t["name"] else None)
            if not subj:
                continue
            for st in t["sets"]:
                for q in st["questions"]:
                    put(q, subj, classify(subj, q))
    pools = mm.pools()
    for subj, d in subjects.items():
        if isinstance(d["key"], str):
            for q in pools.get(d["key"], []):
                put(q, subj, classify(subj, q))
    for q in pools.get("@computer", []):
        put(q, "Computer Literacy", classify("Computer Literacy", q))

    # every real question in the bank, for the "not counted" line
    bank = {}
    for f in (ROOT / "packs").glob("*.json"):
        if f.name in {"index.json", "syllabus.json", OUT.name, "mock-papers.json", "gpstr-subject-mocks.json",
                      "gpstr-unit-pyq-tests.json"} or "plan" in f.name or "structure" in f.name:
            continue
        for s in json.loads(f.read_text(encoding="utf-8")).get("subjects", []):
            for t in s.get("topics", []):
                for st in t.get("sets", []):
                    for q in st["questions"]:
                        if q.get("source"):
                            bank[skey(q)] = q["source"].rsplit(" · Q", 1)[0]

    out_subjects = []
    for subj, d in subjects.items():
        rows = [v for v in assigned.values() if v[0] == subj and v[1] is not None]
        cnt, papers = collections.Counter(), collections.defaultdict(set)
        for _, top, pap in rows:
            if top is not None:
                assert top in d["names"], (subj, top)
                cnt[top] += 1
                papers[top].add(pap)
        sorted_n = sum(cnt.values())
        n_topics = len(d["names"])
        mk = d["marks"] * (150 if d["est"] else 1)
        order = sorted(d["names"], key=lambda t: (-cnt[t], -len(papers[t]), d["names"].index(t)))
        topics, cum, n_must, n_imp = [], 0, 0, 0
        for t in order:
            n = cnt[t]
            share_before = cum / sorted_n if sorted_n else 1
            if n >= 3 and n_must < 4 and (n_must == 0 or share_before < 0.5):
                tier = "must"; n_must += 1
            elif n >= 2 and n_imp < 5 and share_before < 0.8:
                tier = "important"; n_imp += 1
            else:
                tier = "revise"
            cum += n
            topics.append({"name": t, "real": n, "papers": len(papers[t]), "tier": tier,
                           "exp": round(mk * (n + 1) / (sorted_n + n_topics), 1)})
        out_subjects.append({"paper": d["paper"], "subject": subj, "library": d["library"], "marks": round(mk, 1), "est": d["est"],
                             "real": sorted_n, "few": sorted_n < 15, "topics": topics})

    counted = {k for k, v in assigned.items() if v[1] is not None}
    data = {"updated": datetime.date.today().isoformat(), "bank": len(bank), "counted": len(counted),
            "papers": len({v[2] for v in assigned.values() if v[1] is not None}),
            "subjects": out_subjects}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    rest = collections.Counter(p for k, p in bank.items() if k not in counted)
    print(f"real questions in the bank: {len(bank)} · counted for GPSTR: {len(counted)} from {data['papers']} papers")
    print("not counted (off the GPSTR syllabus), by paper:", ", ".join(f"{p} {n}" for p, n in rest.most_common(12)))
    for s in out_subjects:
        print(f"{s['paper']} {s['subject']} [{s['marks']} marks, {s['real']} real]")
        for t in s["topics"]:
            if t["tier"] != "revise":
                print(f"   {t['tier']:9s} {t['real']:3d} Q {t['papers']:2d} papers  {t['name']}")


if __name__ == "__main__":
    main()
