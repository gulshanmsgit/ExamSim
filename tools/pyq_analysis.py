"""Previous-year question (PYQ) analysis notes – owner's request (19 Oct 2026): "complete the remaining PYQ analysis".

For every topic in the topic packs it adds a note "Previous-year analysis – <topic>": how many REAL previous-year questions
(questions with a `source`, copied word for word from KEA/KSET/PGCET papers) the topic holds, from which papers and exam
families, its rank inside its subject, a priority label, the unit's share of all real papers, and sample questions with
their answers. For every unit/subject topic of packs/pyq-by-subject.json it adds a whole-unit overview.

Notes are written straight into the pack JSON (replaced by title, so re-running is safe). build_subject.py rebuilds a pack
without them, so run `python tools/pyq_analysis.py` after building packs (then make_index.py)."""
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
SKIP = {"index.json", "syllabus.json", "pyq-p1.json", "pyq-p2.json", "pyq-by-subject.json"}
TITLE = "Previous-year analysis – "


def family(paper):
    p = paper.lower()
    if p.startswith("kset"):
        return "KSET (lecturer eligibility)"
    if p.startswith("pgcet"):
        return "PGCET (KEA entrance)"
    if p.startswith("gfgc"):
        return "GFGC Asst Professor (KEA)"
    return "KEA recruitment exams (GTTC, Legislative Council, KEA)"


def paper_of(source):
    return source.rsplit(" · Q", 1)[0]


def official(q):
    return "official answer" in (q.get("explanation") or "").lower()


def load(path):
    raw = path.read_text(encoding="utf-8")
    return raw, json.loads(raw)


def save(path, raw, pack):
    path.write_text(json.dumps(pack, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")


def put_note(topic, title, md):
    topic["notes"] = [n for n in topic.get("notes", []) if not n["title"].startswith(TITLE)] + [{"title": title, "md": md}]


def priority(n):
    if n >= 15:
        return "**High** – asked often; master it"
    if n >= 6:
        return "**Medium** – asked regularly; know the main facts"
    if n >= 1:
        return "**Low** – asked occasionally; revise the basics"
    return "**Not seen** in the papers collected so far – syllabus topic, learn the essentials"


def short(text, n=150):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1] + "…"


def unit_overview():
    """Shares per unit/subject from pyq-by-subject.json → {subject name key: (count, total, rank, n_units, by family)}."""
    _, pack = load(PACKS / "pyq-by-subject.json")
    out = {}
    for subj in pack["subjects"]:
        rows = []
        for t in subj["topics"]:
            qs = [q for s in t["sets"] for q in s["questions"]]
            fam = collections.Counter(family(paper_of(q["source"])) for q in qs if q.get("source"))
            rows.append((t["name"], len(qs), fam))
        total = sum(r[1] for r in rows)
        ranked = sorted(rows, key=lambda r: -r[1])
        for name, n, fam in rows:
            out[name] = (n, total, [r[0] for r in ranked].index(name) + 1, len(rows), fam, subj["name"], ranked)
    return out


def unit_key(subject_name, overview):
    """Match a topic pack's subject ('P2 · Unit 6 – …', 'P1 · General Knowledge') to a pyq-by-subject topic name."""
    s = re.sub(r"^P[12] · ", "", subject_name)
    for k in overview:
        if s.startswith(k) or k.startswith(s) or s.split(" (")[0] == k.split(" (")[0]:
            return k
    return None


def topic_note(subject_name, topic, overview, rank, n_topics):
    qs = [q for s in topic["sets"] for q in s["questions"]]
    seen, real = set(), []
    for q in qs:
        src = q.get("source")
        if src and src not in seen:
            seen.add(src)
            real.append(q)
    pattern = sum(1 for q in qs if "PYQ pattern" in (q.get("explanation") or ""))
    papers = collections.Counter(paper_of(q["source"]) for q in real)
    fams = collections.Counter(family(p) for p in paper_of_list(real))
    n_off = sum(1 for q in real if official(q))
    md = [f"**Real previous-year questions in this topic: {len(real)}**"
          + (f" from {len(papers)} paper{'s' if len(papers) != 1 else ''}" if real else "")
          + (f" ({n_off} with KEA's official key)" if n_off else "")
          + f" · PYQ-pattern practice questions: {pattern} · all questions: {len(qs)}",
          "",
          f"- Priority: {priority(len(real))}",
          f"- Rank in this subject by real questions: **{rank} of {n_topics}** topics"]
    k = unit_key(subject_name, overview)
    if k:
        n, total, urank, nunits, _, sname, _ = overview[k]
        md.append(f"- Whole subject/unit in the collected papers: **{n} of {total}** real questions ({n / total * 100:.1f}%) – rank {urank} of {nunits} in “{sname.split(' · ')[-1]}”")
    if real:
        md += ["", "| Exam family | Questions |", "|---|---|"]
        md += [f"| {f} | {c} |" for f, c in fams.most_common()]
        md += ["", "**Papers that asked it:** " + "; ".join(f"{p} ({c})" for p, c in papers.most_common())]
        picks = sorted(real, key=lambda q: (not official(q), len(q["question"])))[:6]
        md += ["", "**What they asked (samples, word for word):**"]
        for q in picks:
            ans = q["options"].get(q["answer"], "")
            md.append(f"- {short(q['question'])} → **{short(str(ans), 80)}** _({q['source']})_")
    md += ["", "_How to use: start revision with High-priority topics; for Low/Not-seen topics learn definitions and one-line facts. "
           "Counts come from the papers collected in ExamSim (KEA recruitment papers 2024–26, KSET 2023–25, PGCET 2023–26, GFGC 2021)._"]
    return "\n".join(md), len(real)


def paper_of_list(real):
    return [paper_of(q["source"]) for q in real]


def overview_note(name, overview):
    n, total, urank, nunits, fam, sname, ranked = overview[name]
    md = [f"**{name}: {n} of {total} real questions ({n / total * 100:.1f}%) – rank {urank} of {nunits}** in {sname}", "",
          "| Rank | Unit / subject | Real questions | Share |", "|---|---|---|---|"]
    md += [f"| {i} | {r[0]}{' ←' if r[0] == name else ''} | {r[1]} | {r[1] / total * 100:.1f}% |" for i, r in enumerate(ranked, 1)]
    md += ["", "| Exam family | Questions from this unit |", "|---|---|"] + [f"| {f} | {c} |" for f, c in fam.most_common()]
    md += ["", "_Shares show where the collected papers put their weight – use them with the syllabus weightage to plan revision._"]
    return "\n".join(md)


def main():
    overview = unit_overview()
    summary = []
    for path in sorted(PACKS.glob("*.json")):
        if path.name in SKIP or "plan" in path.name or "structure" in path.name:
            continue
        raw, pack = load(path)
        changed = False
        for subj in pack.get("subjects", []):
            topics = subj.get("topics", [])
            counts = []
            for t in topics:
                srcs = {q["source"] for s in t.get("sets", []) for q in s["questions"] if q.get("source")}
                counts.append(len(srcs))
            order = sorted(range(len(topics)), key=lambda i: -counts[i])
            for i, t in enumerate(topics):
                if not t.get("sets"):
                    continue
                md, n = topic_note(subj["name"], t, overview, order.index(i) + 1, len(topics))
                put_note(t, TITLE + t["name"], md)
                summary.append((path.name, t["name"], n))
                changed = True
        if changed:
            save(path, raw, pack)
    raw, pack = load(PACKS / "pyq-by-subject.json")
    for subj in pack["subjects"]:
        for t in subj["topics"]:
            if t["name"] in overview:
                put_note(t, TITLE + t["name"] + " (whole unit)", overview_note(t["name"], overview))
    save(PACKS / "pyq-by-subject.json", raw, pack)
    print(f"{len(summary)} topic notes; topics with real PYQs: {sum(1 for s in summary if s[2])}")
    return summary


if __name__ == "__main__":
    main()
