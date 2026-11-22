"""Build packs/gpstr-subject-mocks.json – subject-wise GPSTR mock tests (owner, 21 Nov 2026: "mock subject wise for GPSTR").

One topic per GPSTR syllabus subject (Paper 1's eight subjects, Paper 2's ten units), each with 3 mock tests of 25 questions,
at exam level:
  1. real previous-year questions first – hardest papers first (tiers in tools/mock_pyq_more.py) – up to 15 per test;
  2. then the subject's previous-year-PATTERN questions (KEA style, explanation starts "PYQ pattern"), spread round-robin
     over the subject's syllabus topics so each test covers the whole subject;
  3. then other questions of the subject's topics if a pool runs short.
No question repeats inside a subject's three tests. Every question keeps its options, key and explanation as stored; its
`subject` is the syllabus topic it came from, so the result screen names the weak topics inside the subject.
The subject is called "GPSTR Subject Mock Tests" – GPSTR-only in the app (KRIES mode hides it). Strict exam settings.
Usage: python tools/build_subject_mocks.py   (then make_index.py, check_packs.py)
"""
import json
import random
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import mock3_pyq as m3  # noqa: E402
import mock_pyq_more as mm  # noqa: E402
import packlib  # noqa: E402

SUBJECT = "GPSTR Subject Mock Tests"
REV = 2  # rev 2 (21 Nov 2026): GK questions of one Paper-1 paper no longer leak into English / Computer / Unit 1
N_TESTS, SIZE, MAX_REAL = 3, 25, 15
SETTINGS = {"minPerQ": 1.2, "correct": 1, "wrong": "1/4", "blank": "1/4", "shuffleQ": False, "shuffleO": False}

# (topic shown in the app, library subject, pack files, previous-year pool key in mock_pyq_more.pools())
P1 = [("Paper 1 · General Knowledge", "P1 · General Knowledge", ["p1-gk.json"], "General Knowledge"),
      ("Paper 1 · Current Affairs", "P1 · Current Affairs", ["p1-ca.json"], "Current Affairs"),
      ("Paper 1 · General Kannada", "P1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ)", ["p1-kannada-complete.json"], "General Kannada"),
      ("Paper 1 · General English", "P1 · General English", ["p1-eng.json"], "General English"),
      ("Paper 1 · Educational Psychology", "P1 · Educational Psychology", ["p1-psy.json"], "Educational Psychology"),
      ("Paper 1 · Computer Literacy", "P1 · Computer Literacy", ["p1-cl.json"], "Computer Literacy"),
      ("Paper 1 · Health Education", "P1 · Health Education", ["p1-he.json"], "Health Education"),
      ("Paper 1 · Value Education", "P1 · Value Education", ["p1-ve.json"], "Value Education")]
P2_FILES = {1: ["p2-u1-complete.json"], 2: ["p2-u2-complete.json"], 3: ["p2-u3.json"], 4: ["p2-u4.json"],
            5: ["p2-u5-01-dbms-concepts.json", "p2-u5.json"], 6: ["p2-u6.json"], 7: ["p2-u7.json"], 8: ["p2-u8.json"],
            9: ["p2-u9.json"], 10: ["p2-u10.json"]}
P2_NAMES = {1: "Fundamentals of Computers", 2: "Discrete Structures & Optimization", 3: "Computer System Architecture",
            4: "Programming Languages & Web", 5: "Database Management Systems", 6: "System Software & Operating Systems",
            7: "Software Engineering", 8: "Data Structures & Algorithms", 9: "Data Communication & Networks",
            10: "Artificial Intelligence"}
P2 = [(f"Paper 2 · Unit {u} – {n}", f"P2 · Unit {u} – {n}", P2_FILES[u], u) for u, n in P2_NAMES.items()]
TOPICS = [t for t, *_ in P1 + P2]
KEEP = ("question", "options", "answer", "explanation", "source")


def topic_questions(lib_subject, files):
    """[(syllabus topic, question)] of one library subject across its packs (plan topics and monthly CA alike)."""
    out = []
    for f in files:
        pack = json.loads((ROOT / "packs" / f).read_text(encoding="utf-8"))
        for s in pack["subjects"]:
            if s["name"] != lib_subject:
                continue
            for t in s["topics"]:
                out += [(t["name"], q) for st in t["sets"] for q in st["questions"]]
    return out


def round_robin(by_topic, n, rng, used):
    """n questions spread over the topics in turn (random inside a topic), skipping used keys."""
    names = list(by_topic)
    rng.shuffle(names)
    queues = {k: [q for q in by_topic[k]] for k in names}
    for k in names:
        rng.shuffle(queues[k])
    got = []
    while len(got) < n and any(queues.values()):
        for k in names:
            while queues[k] and m3._key(queues[k][0][1]) in used:
                queues[k].pop(0)
            if queues[k] and len(got) < n:
                item = queues[k].pop(0)
                used.add(m3._key(item[1]))
                got.append(item)
    return got


def real_questions(lib_subject, files, pool_key, pools, items=None):
    """{key: (syllabus topic, question)} – every clean real previous-year question of a subject/unit."""
    items = topic_questions(lib_subject, files) if items is None else items
    real_t = {}   # real previous-year questions with their syllabus topic
    for tn, q in items:
        if q.get("source") and not any(b in q["question"].lower() for b in m3.BAD) and q["source"] not in m3.EXCLUDE:
            real_t.setdefault(m3._key(q), (tn, q))
    extra = pools.get("@computer", []) if pool_key == 1 else []  # Unit 1 also takes the KEA papers' computer sections
    for q in pools.get(pool_key, []) + extra:  # previous-year questions filed under this subject without a topic
        if q.get("source") and not any(b in q["question"].lower() for b in m3.BAD) and q["source"] not in m3.EXCLUDE \
                and (not isinstance(pool_key, int) or q in extra or re.search(m3.UNIT_KW[pool_key], q["question"], re.I)):
            real_t.setdefault(m3._key(q), ("Previous-year questions (mixed topics)", q))
    return real_t


def subject_tests(topic, lib_subject, files, pool_key, pools, rng):
    items = topic_questions(lib_subject, files)
    real_t = real_questions(lib_subject, files, pool_key, pools, items)
    real = list(real_t.values())
    rng.shuffle(real)
    real.sort(key=lambda it: mm.tier(it[1]))  # hardest papers first
    pattern, other = {}, {}
    for tn, q in items:
        if m3._key(q) in real_t:
            continue
        (pattern if "PYQ pattern" in (q.get("explanation") or "") else other).setdefault(tn, []).append((tn, q))
    used, tests = set(), []
    per_test = min(MAX_REAL, len(real) // N_TESTS) if len(real) >= N_TESTS else 0
    extra_real = len(real) - per_test * N_TESTS if per_test < MAX_REAL else 0
    for i in range(N_TESTS):
        n_real = per_test + (1 if i < extra_real and per_test < MAX_REAL else 0)
        got = []
        for it in real:
            if len(got) == n_real:
                break
            if m3._key(it[1]) not in used:
                used.add(m3._key(it[1]))
                got.append(it)
        got += round_robin(pattern, SIZE - len(got), rng, used)
        got += round_robin(other, SIZE - len(got), rng, used)
        assert len(got) == SIZE, (topic, i, len(got))
        rng.shuffle(got)
        got.sort(key=lambda it: mm.tier(it[1]) if it[1].get("source") else 3)  # real (hardest first), then pattern
        tests.append(balance([{k: q[k] for k in KEEP if k in q} | {"subject": tn} for tn, q in got]))
    return tests, len(real)


LETTER_REF = re.compile(r"\(([A-D])\)|\b(option|answer|choice)s? \(?[A-D]\b|\b[A-D] and [A-D]\b", re.I)


def balance(qs):
    """Spread the answers over A–D: real previous-year questions and questions whose options or explanation depend on the
    printed order keep their letter; every other question moves its correct option to the least-used letter so far."""
    def movable(q):
        opts = [q["options"][L] for L in "ABCD"]
        return not q.get("source") and not packlib._keep_order(q["question"], opts) and not LETTER_REF.search(q.get("explanation") or "")
    used = {L: 0 for L in "ABCD"}
    for q in qs:
        if not movable(q):
            used[q["answer"]] += 1
    out = []
    for q in qs:
        if movable(q):
            to = min("ABCD", key=lambda L: (used[L], L != q["answer"]))  # stay put on a tie
            if to != q["answer"]:
                o = dict(q["options"])
                o[q["answer"]], o[to] = o[to], o[q["answer"]]
                q = q | {"options": {L: o[L] for L in "ABCD"}, "answer": to}
            used[to] += 1
        out.append(q)
    return out


def main():
    pools, rng = mm.pools(), random.Random("gpstr-subject-mocks")
    topics, report = [], []
    for topic, lib, files, key in P1 + P2:
        tests, n_real = subject_tests(topic, lib, files, key, pools, rng)
        topics.append({"name": topic, "sets": [{"name": f"{i} · Mock {i}", "questions": qs, "rev": REV} for i, qs in enumerate(tests, 1)]})
        reals = [sum(1 for q in qs if q.get("source")) for qs in tests]
        report.append(f"{topic}: real previous-year {n_real} in pool → per test {reals}")
    desc = ("Subject-wise GPSTR mock tests: 3 tests of 25 questions for each Paper 1 subject and each Paper 2 unit, at exam level – "
            "real previous-year questions first (hardest papers first, up to 15 per test), then KEA-pattern questions spread over "
            "the subject's syllabus topics. Strict timing: 30 minutes per test, −¼ for a wrong or blank answer. The result shows your "
            "weak topics inside the subject. GPSTR mode only.")
    pack = {"examsimPack": 1, "name": SUBJECT, "description": desc,
            "subjects": [{"name": SUBJECT, "icon": "🎯", "settings": SETTINGS, "topics": topics}]}
    (ROOT / "packs" / "gpstr-subject-mocks.json").write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == "gpstr-subject-mocks.json"), None)
    if not entry:
        pos = next((i + 1 for i, p in enumerate(idx["packs"]) if p["file"] == "mock-papers.json"), len(idx["packs"]))
        entry = {"file": "gpstr-subject-mocks.json"}
        idx["packs"].insert(pos, entry)
    entry.update({"group": "④ Full mock papers", "name": SUBJECT, "description": desc})
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
