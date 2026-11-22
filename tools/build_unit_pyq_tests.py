"""Build packs/gpstr-unit-pyq-tests.json – unit-wise GPSTR mock tests made ONLY of real previous-year questions
(owner, 22 Nov 2026: "start mock for each unit from previous year").

For every Paper 2 unit, all its clean real previous-year questions (the same pool the subject tests draw on: questions with a
`source` in the unit's topic packs, KEA/KSET/PGCET papers filed under the unit, and – Unit 1 – the KEA papers' computer
sections) are split into tests of about 25 questions, each question used once. Hard and easy papers are dealt out evenly,
so every test has a similar level. Questions keep the paper's wording, printed option order, key and explanation; `subject`
is the syllabus topic when known. Subject "GPSTR Unit Tests (Previous-Year)" – GPSTR-only; strict exam settings.
Usage: python tools/build_unit_pyq_tests.py   (then make_index.py, check_packs.py)
"""
import json
import random
import sys
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_subject_mocks as bsm  # noqa: E402
import mock3_pyq as m3  # noqa: E402
import mock_pyq_more as mm  # noqa: E402

SUBJECT = "GPSTR Unit Tests (Previous-Year)"
FILE = "gpstr-unit-pyq-tests.json"
TARGET = 25          # questions per test (tests in a unit differ by at most one question)
MAX_TESTS = 8        # big units: at most 8 tests (≤ 200 questions)
UNITS = [(f"Unit {u} – {n}", f"P2 · Unit {u} – {n}", bsm.P2_FILES[u], u) for u, n in bsm.P2_NAMES.items()]
TOPICS = [t for t, *_ in UNITS]


def n_tests(n):
    return max(1, min(MAX_TESTS, round(n / TARGET)))


def unit_tests(lib, files, u, pools, rng):
    real = list(bsm.real_questions(lib, files, u, pools).values())
    rng.shuffle(real)
    real.sort(key=lambda it: mm.tier(it[1]))           # hardest first …
    k = n_tests(len(real))
    use = real[:k * TARGET + k] if len(real) > MAX_TESTS * TARGET else real  # big units: keep the hardest ≈ 8 × 25
    tests = [[] for _ in range(k)]
    # … dealt in rounds of k (every test gets the same mix of hard and easy papers); inside a round each question goes to
    # the test with the fewest answers on its letter so far, so no test is lopsided on A, B, C or D (printed keys unchanged)
    for r in range(0, len(use), k):
        free = list(range(k))
        for it in use[r:r + k]:
            letter = it[1]["answer"]
            best = min(free, key=lambda j: (sum(1 for _, q in tests[j] if q["answer"] == letter), j))
            tests[best].append(it); free.remove(best)
    out = []
    for t in tests:
        t.sort(key=lambda it: (mm.tier(it[1]), it[1]["source"]))
        out.append([{key: q[key] for key in bsm.KEEP if key in q} | {"subject": tn} for tn, q in t])
    return out, len(real)


def main():
    pools, rng = mm.pools(), random.Random("gpstr-unit-pyq-tests")
    topics, report = [], []
    for topic, lib, files, u in UNITS:
        tests, n_real = unit_tests(lib, files, u, pools, rng)
        topics.append({"name": topic, "sets": [{"name": f"{i} · PYQ Test {i}", "questions": qs} for i, qs in enumerate(tests, 1)]})
        report.append(f"{topic}: {n_real} real → {len(tests)} tests {[len(t) for t in tests]}")
    desc = ("Unit-wise GPSTR mock tests made only of real previous-year questions (KEA, KSET, GTTC, PGCET …): every Paper 2 unit "
            "split into tests of about 25 questions, each question used once, hard and easy papers spread evenly. Original wording, "
            "option order and keys. Strict timing: 30 minutes per 25 questions, −¼ for a wrong or blank answer. GPSTR mode only.")
    pack = {"examsimPack": 1, "name": SUBJECT, "description": desc,
            "subjects": [{"name": SUBJECT, "icon": "📚", "settings": bsm.SETTINGS, "topics": topics}]}
    (ROOT / "packs" / FILE).write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == FILE), None)
    if not entry:
        pos = next((i + 1 for i, p in enumerate(idx["packs"]) if p["file"] == "gpstr-subject-mocks.json"), len(idx["packs"]))
        entry = {"file": FILE}
        idx["packs"].insert(pos, entry)
    entry.update({"group": "④ Full mock papers", "name": SUBJECT, "description": desc})
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    smap_path = TOOLS / "syllabus_map.json"
    smap = json.loads(smap_path.read_text(encoding="utf-8"))
    smap[SUBJECT] = {t["name"]: [st["name"].split(" · ", 1)[1] for st in t["sets"]] for t in topics}
    smap_path.write_text(json.dumps(smap, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
