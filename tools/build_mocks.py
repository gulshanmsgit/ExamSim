"""Build packs/mock-papers.json – full-length GPSTR/CST mock papers (owner, 12 Nov 2026).

Mock Set 2: same format; current affairs from July–August 2026 (tools/mock2_p1.py, tools/mock2_p2.py).
Mock Set 1:
  Paper 1 – 100 Q in the official marks split (tools/mock1_p1.py, 85 new) + 15 current-affairs questions taken from the web-checked
            monthly pack packs/p1-ca.json (September–October 2026: 11 Karnataka + 4 national).
  Paper 2 – 100 new Computer Science Q in the planner's unit weights (tools/mock1_p2.py).
Every question carries its section in `subject`, so the result screen's subject-wise breakdown shows the weak subjects.
Each section is balanced A–D by packlib (built separately, then joined in syllabus order).
Usage: python tools/build_mocks.py
"""
import json, random, sys, tempfile
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
from packlib import build_pack
import mock1_p1, mock1_p2, mock2_p1, mock2_p2

SUBJECT = "Full Mock Papers"
P1_TOPIC, P2_TOPIC = "Paper 1 – Full Mock Tests", "Paper 2 – Full Mock Tests"


def section_questions(tag, qs):
    """Run one section through packlib (checks + A–D balance) and return its question dicts."""
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "s.json"
        build_pack(out, "tmp", "", [{"name": "S", "topics": [{"name": "T", "sets": [{"name": tag, "tag": tag, "questions": qs}]}]}])
        return json.loads(out.read_text(encoding="utf-8"))["subjects"][0]["topics"][0]["sets"][0]["questions"]


def current_affairs(months, seed, n_ka=11, n_nat=4):
    ca = json.loads((ROOT / "packs" / "p1-ca.json").read_text(encoding="utf-8"))
    by_name = {t["name"]: t for s in ca["subjects"] for t in s["topics"]}
    pool = {"Karnataka": [], "National": []}
    for m in months:
        for st in by_name[m]["sets"]:
            kind = st["name"].split(" · ", 1)[-1]
            pool[kind] += [dict(q, explanation=q["explanation"] + f" ({m})") for q in st["questions"]]
    rng = random.Random(seed)
    picked = rng.sample(pool["Karnataka"], n_ka) + rng.sample(pool["National"], n_nat)
    for q in picked:
        q["subject"] = "Current Affairs"
    return picked


def paper(sections, extra_after=None):
    qs = []
    for tag, items in sections:
        qs += section_questions(tag, items)
        if extra_after and tag == extra_after[0]:
            qs += extra_after[1]
    return qs


SETS = [(1, mock1_p1, mock1_p2, ("September 2026", "October 2026")), (2, mock2_p1, mock2_p2, ("July 2026", "August 2026"))]
built = []
for n, m1, m2, months in SETS:
    p1 = paper(m1.SECTIONS, extra_after=("General Knowledge", current_affairs(months, f"mock{n}-ca")))
    p2 = paper(m2.SECTIONS)
    assert len(p1) == 100 and len(p2) == 100, (n, len(p1), len(p2))
    built.append((n, p1, p2))

pack = {"examsimPack": 1, "name": "Full Mock Papers",
        "description": "Full-length GPSTR/CST mock papers at KEA level. Mock Sets 1 and 2, each with Paper 1 (100 Q, official marks split incl. 15 current affairs) "
                       "and Paper 2 (100 Q, unit weights). After the test, the result's subject-wise breakdown shows your weak subjects.",
        "subjects": [{"name": SUBJECT, "icon": "📝", "topics": [
            {"name": P1_TOPIC, "sets": [{"name": f"{n} · Mock Set {n} – Paper 1 (General)", "questions": p1} for n, p1, _ in built]},
            {"name": P2_TOPIC, "sets": [{"name": f"{n} · Mock Set {n} – Paper 2 (Computer Science)", "questions": p2} for n, _, p2 in built]}]}]}
(ROOT / "packs" / "mock-papers.json").write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
for name, qs in [(f"Set {n} Paper {k}", q) for n, a, b in built for k, q in ((1, a), (2, b))]:
    spread = {L: sum(q["answer"] == L for q in qs) for L in "ABCD"}
    print(f"{name}: {len(qs)} Q, answers {spread}")
