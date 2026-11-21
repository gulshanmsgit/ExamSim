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
# Paper 2 in the syllabus (planner) unit weights – Unit 1 back to 10 and Unit 2 to 8 (Set 3 had to swap 2 marks).
# Paper 1 follows the official marks except Value Education: the bank has 1 real Value Education question, so its other
# 9 marks stay with Educational Psychology (as in Set 3) – m3.P1_PLAN.
P2_PLAN = [(tag, u, {1: 10, 2: 8}.get(u, n)) for tag, u, n in m3.P2_PLAN]


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
            # GK papers first: "Assistant / Computer Operator Paper-1 (General Knowledge)" must not count as a computer paper
            if re.search(r"General Knowledge|GK|General Studies", t["name"]):
                p["General Knowledge"] += qs
            elif re.search(r"English & Computer|KEC", t["name"]):
                p["General English"] += [q for q in qs if 36 <= qnum(q["source"]) <= 70]
                p["Computer Literacy"] += [q for q in qs if qnum(q["source"]) >= 71]
                p["@computer"] += [q for q in qs if qnum(q["source"]) >= 71]
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


# Harder papers first (owner, 21 Nov 2026: "the exam is difficult – make the paper stricter"): tier 1 = lecturer/PG-level and
# the KEA 2025–26 general papers, tier 2 = programmer/technician/MCA and other recruitment GK papers, tier 3 = clerk-level KEC.
TIER1 = r"KSET|M\.Tech|PGCET 2026 CS|GTTC 2024 Lecturer|KEA 2026 CS|Raichur|GFGC|KEA 202[56] GK|UPSC|PSI"
TIER2 = r"MCA|Programmer|Technician|GTTC 2024 Asst Gr-II GK|Legislative Council 2024 .*P1|KRIES|VAO"


def tier(q):
    return 0 if re.search(TIER1, q["source"]) else 1 if re.search(TIER2, q["source"]) else 2


def pick(cands, n, rng, repeats=(), now=None, used=None):
    """Hardest papers first (tier 1, then 2, then 3, random inside a tier); top up from `repeats` (education sections only)."""
    cands = list(cands)
    rng.shuffle(cands)
    cands.sort(key=tier)  # stable: random order kept inside each tier
    got = cands[:n]
    if len(got) < n:
        extra = [q for q in repeats if m3._key(q) not in {m3._key(g) for g in got} | (now or set())]
        rng.shuffle(extra)
        extra.sort(key=lambda q: (used or {}).get(m3._key(q), 0))  # least-used earlier questions first (stable sort)
        got += extra[:n - len(got)]
    assert len(got) == n, (n, len(got))
    got.sort(key=lambda q: q["source"])
    return got


def build(set_no, taken, earlier_papers):
    """Return (paper1, paper2) for Mock Set `set_no`; `taken` holds keys of every earlier set and is updated.
    `earlier_papers`: the Paper 1 question lists of the earlier previous-year sets (3, 4 …) – the education sections may
    repeat from them, least-used first."""
    p, rng = pools(), random.Random(f"mock{set_no}-pyq")
    used, repeat = {}, {tag: [] for tag in EDU}
    for paper in earlier_papers:
        for q in paper:
            k = m3._key(q)
            if k not in used and q.get("subject") in repeat:
                repeat[q["subject"]].append(q)
            used[k] = used.get(k, 0) + 1
    paper1, paper2, now = [], [], set()  # `now`: keys already in this set (repeats must not clash across sections)
    for tag, _, n in m3.P1_PLAN:
        cands = clean(p[tag], taken, m3.ALLOW.get(tag, m3.CS))
        if tag == "General English":  # KEC English sections count even though the source names say P2
            cands = clean(p[tag], taken, r".")
        if tag == "Computer Literacy":
            cands = clean(p[tag], taken, r".")
        got = pick(cands, n, rng, repeat.get(tag, ()), now, used)
        for q in got:
            taken.add(m3._key(q))
            now.add(m3._key(q))
        paper1 += [{k: q[k] for k in ("question", "options", "answer", "explanation", "source") if k in q} | {"subject": tag} for q in got]
    for tag, u, n in P2_PLAN:
        cands = clean(p[u], taken, m3.CS, u)
        if u == 1:
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
