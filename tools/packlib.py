"""Shared builder for ExamSim study packs.

A pack script defines questions as (question, [4 options], correct_index, explanation)
and calls build_pack(). Options are shuffled deterministically (seeded by the question
text) so correct answers spread across A–D, except option sets whose order carries
meaning (Only I / Both…, assertion–reason, a-1 b-2 matchings, arrows/sequences).
The build fails on any structural problem: wrong option count, duplicate options,
bad answer index or duplicate questions (within the pack).
"""
import hashlib, json, random, re, sys
from pathlib import Path

AR = ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false", "A is false, but R is true"]
I_II = ["Only I", "Only II", "Both I and II", "Neither I nor II"]

_ORDERED = re.compile(r"^(Only|Both|Neither|A is|a-\d|All of|None of)|→")


def _keep_order(q, opts):
    return "Assertion (A)" in q or any(_ORDERED.search(o) for o in opts)


def build_pack(out_path, name, description, subjects):
    """subjects: [{name, icon, topics: [{name, sets: [{name, questions: [(q, opts, ans, expl)], tag?}]}]}]"""
    problems, counts, seen = [], {"A": 0, "B": 0, "C": 0, "D": 0}, {}
    out_subjects = []
    for s in subjects:
        out_topics = []
        for t in s["topics"]:
            out_sets = []
            for st in t["sets"]:
                qs = []
                for i, (q, opts, ans, expl) in enumerate(st["questions"]):
                    where = f"{t['name']} / {st['name']} Q{i + 1}"
                    if len(opts) != 4 or len(set(opts)) != 4:
                        problems.append(f"{where}: needs 4 distinct options")
                    if not 0 <= ans < 4:
                        problems.append(f"{where}: bad answer index")
                    key = re.sub(r"\s+", " ", q.strip().lower())
                    if key in seen:
                        problems.append(f"{where}: duplicate of {seen[key]}")
                    seen[key] = where
                    order = list(range(4))
                    if not _keep_order(q, opts):
                        random.Random(hashlib.md5(q.encode()).hexdigest()).shuffle(order)
                    letter = "ABCD"[order.index(ans)] if 0 <= ans < 4 else "A"
                    counts[letter] += 1
                    qs.append({"question": q, "options": dict(zip("ABCD", [opts[k] for k in order])),
                               "answer": letter, "subject": st.get("tag", st["name"]), "explanation": expl})
                out_sets.append({"name": st["name"], "questions": qs})
            out_topics.append({"name": t["name"], "sets": out_sets})
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
