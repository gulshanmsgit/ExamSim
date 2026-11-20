"""Mock Sets 4 and 5 – more full mocks made only of real previous-year questions (owner, 20 Nov 2026: "prepare mock test
using previous year questions only").

Same marks split and section tags as Mock Set 3 (tools/mock3_pyq.py). Pools: packs/pyq-by-subject.json plus the full
papers in packs/pyq-p1.json (GK papers → General Knowledge; KEC papers: Q1–35 Kannada, Q36–70 English, Q71–100 computer).
No question used in an earlier Mock Set is picked again, except in the three education sections: the bank holds very few
previous-year questions on Educational Psychology (≈ 35), Health Education (≈ 11) and Value Education (1), so after the
unused ones run out these sections repeat questions from Mock Set 3 (said in the set description). Paper 2 Unit 1 has no
unused CS-paper questions left, so it draws on the computer sections of the KEA papers (fundamentals level).
Option order, keys, explanations and sources are kept as in the papers; packlib balances A–D only by reordering questions.
"""
import json
import random
import re
from pathlib import Path

import mock3_pyq as m3

ROOT = Path(__file__).parent.parent
EDU = ("Educational Psychology", "Health Education", "Value Education")


def qnum(source):
    mt = re.search(r"· Q(\d+)$", source or "")
    return int(mt.group(1)) if mt else 0


def pools():
    """{section tag or unit number: [question, …]} from both previous-year packs."""
    topics = m3._load()
    p = {tag: [q for s in src for q in topics[s]] for tag, src, _ in m3.P1_PLAN}
    p.update({u: list(topics[u]) for _, u, _ in m3.P2_PLAN})
    p["@computer"] = list(topics["Computer Literacy"])
    p1 = json.loads((ROOT / "packs" / "pyq-p1.json").read_text(encoding="utf-8"))
    for s in p1["subjects"]:
        for t in s["topics"]:
            qs = [q for st in t["sets"] for q in st["questions"]]
            if re.search(r"English|Computer|KEC", t["name"]):
                p["General English"] += [q for q in qs if 36 <= qnum(q["source"]) <= 70]
                p["Computer Literacy"] += [q for q in qs if qnum(q["source"]) >= 71]
                p["@computer"] += [q for q in qs if qnum(q["source"]) >= 71]
            elif re.search(r"General Knowledge|GK|General Studies", t["name"]):
                p["General Knowledge"] += qs
    return p


def clean(pool, taken, allow, unit=None):
    out = {}
    for q in pool:
        k = m3._key(q)
        if (q.get("source") and k not in taken and q["source"] not in m3.EXCLUDE and re.search(allow, q["source"])
                and not any(b in q["question"].lower() for b in m3.BAD)
                and (unit is None or re.search(m3.UNIT_KW[unit], q["question"], re.I))):
            out.setdefault(k, q)
    return list(out.values())


def pick(cands, n, rng, repeats=(), now=None):
    """Half (rounded up) from KEA/KSET papers when possible; top up from `repeats` (education sections only)."""
    cands = list(cands)
    rng.shuffle(cands)
    first = [q for q in cands if re.match(r"(KEA|KSET)", q["source"])]
    want = (n + 1) // 2
    got = first[:want]
    got += [q for q in cands if q not in got][:n - len(got)]
    if len(got) < n:
        extra = [q for q in repeats if m3._key(q) not in {m3._key(g) for g in got} | (now or set())]
        rng.shuffle(extra)
        got += extra[:n - len(got)]
    assert len(got) == n, (n, len(got))
    got.sort(key=lambda q: q["source"])
    return got


def build(set_no, taken, set3_questions):
    """Return (paper1, paper2) for Mock Set `set_no`; `taken` holds keys of every earlier set and is updated."""
    p, rng = pools(), random.Random(f"mock{set_no}-pyq")
    repeat = {tag: [q for q in set3_questions if q.get("subject") == tag] for tag in EDU}
    paper1, paper2, now = [], [], set()  # `now`: keys already in this set (repeats must not clash across sections)
    for tag, _, n in m3.P1_PLAN:
        cands = clean(p[tag], taken, m3.ALLOW.get(tag, m3.CS))
        if tag == "General English":  # KEC English sections count even though the source names say P2
            cands = clean(p[tag], taken, r".")
        if tag == "Computer Literacy":
            cands = clean(p[tag], taken, r".")
        got = pick(cands, n, rng, repeat.get(tag, ()), now)
        for q in got:
            taken.add(m3._key(q))
            now.add(m3._key(q))
        paper1 += [{k: q[k] for k in ("question", "options", "answer", "explanation", "source") if k in q} | {"subject": tag} for q in got]
    for tag, u, n in m3.P2_PLAN:
        cands = clean(p[u], taken, m3.CS, u)
        if len(cands) < n and u == 1:
            cands += clean(p["@computer"], taken, r".")  # Unit 1 covers basics and office tools too
        got = pick(cands, n, rng)
        for q in got:
            taken.add(m3._key(q))
        paper2 += [{k: q[k] for k in ("question", "options", "answer", "explanation", "source") if k in q} | {"subject": tag} for q in got]
    return paper1, paper2


if __name__ == "__main__":  # quick capacity report
    pk = json.loads((ROOT / "packs" / "mock-papers.json").read_text(encoding="utf-8"))
    taken = {m3._key(q) for s in pk["subjects"] for t in s["topics"] for st in t["sets"] for q in st["questions"]}
    p = pools()
    for tag, _, n in m3.P1_PLAN:
        print("P1", tag, n, len(clean(p[tag], taken, r"." if tag in ("General English", "Computer Literacy") else m3.ALLOW.get(tag, m3.CS))))
    for tag, u, n in m3.P2_PLAN:
        print("P2", tag, n, len(clean(p[u], taken, m3.CS, u)), "+computer" if u == 1 else "", len(clean(p["@computer"], taken, r".", 1)) if u == 1 else "")
