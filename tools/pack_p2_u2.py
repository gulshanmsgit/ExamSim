"""Pack: Paper 2 · Unit 2 – Discrete Structures & Optimization, complete (all topics and sub-topics × 30)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from packlib import build_pack
import p2u2_a, p2u2_b, p2u2_c, p2u2_d, p2u2_e

SUBJECT = "P2 · Unit 2 – Discrete Structures & Optimization"
ALL = {**p2u2_a.TOPICS, **p2u2_b.TOPICS, **p2u2_c.TOPICS, **p2u2_d.TOPICS, **p2u2_e.TOPICS}

# Topic names must match the planner topics in the structure pack exactly, so questions land in the right topics
structure = json.loads((Path(__file__).parent.parent / "packs" / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
planned = [t["name"] for s in structure["subjects"] if s["name"] == SUBJECT for t in s["topics"]]
missing = [t for t in ALL if t not in planned]
assert not missing, f"topics not in planner: {missing}"

topics = []
for t in planned:
    if t not in ALL:
        continue
    sets = []
    for name, qs in ALL[t]:
        assert len(qs) == 30, f"{t} / {name}: {len(qs)} questions"
        sets.append({"name": name, "tag": name.split(" · ", 1)[1], "questions": qs})
    topics.append({"name": t, "sets": sets})
assert len(topics) == len(planned), "every Unit 2 planner topic must be covered"

build_pack(sys.argv[1], "P2 · Unit 2 — Discrete Structures & Optimization (complete)",
           "All 9 topics of Unit 2 split into 30 syllabus sub-topics, 30 questions each: propositional and predicate logic, inference, sets, relations, "
           "counting, induction, probability, Bayes, graph theory, planarity, colouring, trees, prefix codes, traversals, spanning trees, Boolean algebra. Many worked numericals.",
           [{"name": SUBJECT, "icon": "🔢", "topics": topics}])
