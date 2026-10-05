"""Shared builder for ExamSim study packs.

A pack script defines questions as (question, [4 options], correct_index, explanation)
and calls build_pack(). Options are shuffled deterministically and balanced per set
(each correct answer goes to the least-used letter so far) so answers spread evenly across A–D, except option sets whose order carries
meaning (Only I / Both…, assertion–reason, a-1 b-2 matchings, arrows/sequences).
The build fails on any structural problem: wrong option count, duplicate options,
bad answer index or duplicate questions (within the pack).
"""
import hashlib, json, random, re, sys
from collections import Counter
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

AR = ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false", "A is false, but R is true"]
I_II = ["Only I", "Only II", "Both I and II", "Neither I nor II"]

# Only option sets whose order carries meaning stay fixed; sequences and matchings are self-contained, so they shuffle.
_ORDERED = re.compile(r"^(Only|Both|Neither|A is|All of|None of)")


def _keep_order(q, opts):
    return "Assertion (A)" in q or any(_ORDERED.search(o) for o in opts)


# Match-the-following: stem ends with a line "1. …  2. …  3. …  4. …" and options are codes like "a-4, b-3, c-2, d-1".
# The numbered column is reordered (seeded by the question text) and every code is rewritten to match, so the
# correct code differs from question to question instead of following one habit such as "a-4, b-3, c-2, d-1".
_MATCH_OPT = re.compile(r"^[a-e]-\d(, [a-e]-\d)+$")


def _renumber_match(q, opts):
    if not all(_MATCH_OPT.match(o) for o in opts):
        return q, opts
    head, _, last = q.rpartition("\n")
    parts = re.split(r"(?:^|\s{2,})(\d)\.\s", last)
    nums, items = parts[1::2], parts[2::2]
    if parts[0].strip() or nums != [str(i) for i in range(1, len(nums) + 1)]:
        return q, opts
    perm = list(range(len(items)))
    random.Random("match" + hashlib.md5(q.encode()).hexdigest()).shuffle(perm)  # old item k becomes number perm[k] + 1
    new_items = [None] * len(items)
    for k, it in enumerate(items):
        new_items[perm[k]] = it.strip()
    recode = lambda o: re.sub(r"([a-e])-(\d)", lambda m: f"{m.group(1)}-{perm[int(m.group(2)) - 1] + 1}", o)
    # One item per line (the app keeps line breaks): stem, then a. b. c. d., a blank line, then 1. 2. 3. 4.
    stem, _, left = head.rpartition("\n")
    lparts = re.split(r"(?:^|\s{2,})([a-e])\.\s", left)
    if not lparts[0].strip() and lparts[1::2] == list("abcde"[:len(lparts[1::2])]) and len(lparts) > 1:
        head = stem + "\n" + "\n".join(f"{lab}. {txt.strip()}" for lab, txt in zip(lparts[1::2], lparts[2::2]))
    return head + "\n\n" + "\n".join(f"{i + 1}. {t}" for i, t in enumerate(new_items)), [recode(o) for o in opts]


def build_pack(out_path, name, description, subjects):
    """subjects: [{name, icon, topics: [{name, sets: [{name, questions: [(q, opts, ans, expl[, source])], tag?, keep_order?}]}]}]
    A 5th tuple item names a real previous-year paper ("KSET 2024 · CS&A · Q17") and is stored as `source`.
    keep_order=True keeps every option where the paper printed it (for previous-year papers)."""
    problems, counts, seen = [], {"A": 0, "B": 0, "C": 0, "D": 0}, {}
    out_subjects = []
    for s in subjects:
        out_topics = []
        for t in s["topics"]:
            out_sets = []
            for st in t["sets"]:
                qs = []
                # Balance A–D inside the set: fixed-order questions keep their letter; every other question puts its
                # correct answer on the least-used letter so far (ties and distractor order decided by a hash of the text).
                # real previous-year questions (5th item = source) keep the paper's printed option order
                fixed = lambda q, o, src=None: st.get("keep_order") or bool(src) or _keep_order(q, o)
                used = Counter("ABCD"[it[2]] for it in st["questions"] if fixed(it[0], it[1], it[4] if len(it) > 4 else None) and 0 <= it[2] < 4)
                for i, item in enumerate(st["questions"]):
                    q, opts, ans, expl = item[:4]
                    source = item[4] if len(item) > 4 else None
                    if not st.get("keep_order") and not source:
                        q, opts = _renumber_match(q, opts)
                    where = f"{t['name']} / {st['name']} Q{i + 1}"
                    if len(opts) != 4 or len(set(opts)) != 4:
                        problems.append(f"{where}: needs 4 distinct options")
                    if not 0 <= ans < 4:
                        problems.append(f"{where}: bad answer index")
                    key = re.sub(r"\s+", " ", q.strip().lower())
                    if st.get("keep_order") or source:  # real papers reuse stems such as "Which statement is FALSE?"
                        key += "|" + "|".join(opts)
                    if key in seen:
                        problems.append(f"{where}: duplicate of {seen[key]}")
                    seen[key] = where
                    order = list(range(4))
                    if not fixed(q, opts, source) and 0 <= ans < 4:
                        rng = random.Random(hashlib.md5(q.encode()).hexdigest())
                        others = [k for k in order if k != ans]
                        rng.shuffle(others)
                        slots = sorted(range(4), key=lambda k: (used["ABCD"[k]], rng.random()))
                        order = others[:slots[0]] + [ans] + others[slots[0]:]
                        used["ABCD"[slots[0]]] += 1
                    letter = "ABCD"[order.index(ans)] if 0 <= ans < 4 else "A"
                    counts[letter] += 1
                    qs.append({"question": q, "options": dict(zip("ABCD", [opts[k] for k in order])),
                               "answer": letter, "subject": st.get("tag", st["name"]), "explanation": expl,
                               **({"source": source} if source else {})})
                out_sets.append({"name": st["name"], "questions": qs})
            out_topics.append({"name": t["name"], **({"plan": t["plan"]} if t.get("plan") else {}), "sets": out_sets,
                               **({"notes": t["notes"]} if t.get("notes") else {})})
        out_subjects.append({"name": s["name"], "icon": s.get("icon", ""), "topics": out_topics})
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    pack = {"examsimPack": 1, "name": name, "description": description, "subjects": out_subjects}
    Path(out_path).write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
    total = sum(counts.values())
    per_set = [(st["name"], len(st["questions"])) for s in out_subjects for t in s["topics"] for st in t["sets"]]
    print(f"{total} questions, answer spread {counts}")
    for n, c in per_set:
        print(f"  {c:3d}  {n}")
    return total
