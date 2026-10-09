"""Check every question pack against QUESTION_STANDARD.md. Run before every commit that touches packs.

ERROR = must fix before committing.  WARN = review (older packs may carry a few).
Checks: pack files are listed in packs/index.json; subject/topic names match the planner (structure pack);
set sizes (P2 30, P1 20); sets match tools/syllabus_map.json; Paper 2 is English only; every question has
4 distinct options, an answer and an explanation; A–D spread per set; assertion–reason answers vary;
no duplicate questions across the whole bank (compared the way the app does: spacing and case ignored,
options in any order).
Usage: python tools/check_packs.py
"""
import json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).parent.parent
PACKS = ROOT / "packs"
LEGACY = {"gpstr-cst-2026-01-days01-02.json"}  # older 10-per-topic sample, exempt from set-size and map rules
MOCK_TOPICS = {"Mock tests", "ಮಾದರಿ ಪರೀಕ್ಷೆಗಳು (Mock tests)"}
KANNADA = re.compile(r"[ಀ-೿]")

structure = json.loads((PACKS / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
planned = {s["name"]: {t["name"] for t in s["topics"]} for s in structure["subjects"]}
sys.path.insert(0, str(ROOT / "tools"))
from build_subject import EXTRA_SUBJECTS  # non-planner subjects such as monthly current affairs
for _n, _x in EXTRA_SUBJECTS.items():
    planned[_n] = set(_x["topics"])
from build_pyq import PYQ_SUBJECTS  # real previous-year papers: printed option order and length, not planner topics
PYQ_SUBJECTS = set(PYQ_SUBJECTS) | {"P1 · Previous-Year Questions · General Paper", "P2 · Previous-Year Questions · Computer Science"}  # tools/build_pyq_subjects.py
smap = json.loads((ROOT / "tools" / "syllabus_map.json").read_text(encoding="utf-8"))
index = json.loads((PACKS / "index.json").read_text(encoding="utf-8"))
listed = {p["file"] for p in index["packs"]}



def key_text(t):  # same as keyText() in index.html: collapse spacing, lower-case, NFKC
    return unicodedata.normalize("NFKC", re.sub(r"\s+", " ", str(t)).strip().lower())


def app_key(question, options):  # the app's question identity (qKey v2): used for history, de-duplication and flashcards
    return key_text(question) + "|" + "|".join(sorted(key_text(o) for o in options))


errors, warns, seen = [], [], {}
err = lambda m: errors.append(m)
warn = lambda m: warns.append(m)

for f in sorted(PACKS.glob("*.json")):
    if f.name not in ("index.json", "syllabus.json") and f.name not in listed:  # syllabus.json is app data, not a pack
        err(f"{f.name}: not listed in packs/index.json")

for f in sorted(listed):
    pack = json.loads((PACKS / f).read_text(encoding="utf-8"))
    legacy = f in LEGACY
    for s in pack.get("subjects", []):
        sname = s["name"]
        if sname in PYQ_SUBJECTS:
            for t in s.get("topics", []):
                for st in t.get("sets", []):
                    for i, q in enumerate(st.get("questions", []), 1):
                        where = f"{f}: {t['name']} / {st['name']} Q{i}"
                        vals = [q.get("options", {}).get(k, "") for k in "ABCD"]
                        if len(set(vals)) != 4 or not all(v.strip() for v in vals):
                            err(f"{where}: needs 4 distinct non-empty options")
                        if q.get("answer") not in "ABCD" or not q.get("answer"):
                            err(f"{where}: bad answer")
                        if not q.get("source"):
                            err(f"{where}: previous-year question without a source")
                        k = app_key(q["question"], vals)
                        if f == "pyq-by-subject.json":  # collects real questions that also sit in topic sets – repeats are by design
                            continue
                        if k in seen:
                            warn(f"{where}: same as {seen[k]}")
                        else:
                            seen[k] = where
            continue
        if sname not in planned:
            err(f"{f}: subject '{sname}' is not a planner subject")
            continue
        paper2 = sname.startswith("P2")
        for t in s.get("topics", []):
            tname, sets = t["name"], t.get("sets", [])
            if not sets:
                continue
            mock = tname in MOCK_TOPICS
            if tname not in planned[sname] and not mock:
                err(f"{f}: topic '{tname}' not in planner subject '{sname}' (names must match exactly)")
            if not legacy and not mock:
                want = smap.get(sname, {}).get(tname)
                have = [st["name"].split(" · ", 1)[-1] for st in sets]
                if not want:
                    warn(f"{f}: '{tname}' has no sub-topic list in tools/syllabus_map.json")
                elif have != want:
                    err(f"{f}: '{tname}' sets {have} differ from syllabus_map {want}")
            for st in sets:
                where = f"{f}: {tname} / {st['name']}"
                qs = st.get("questions", [])
                size = EXTRA_SUBJECTS[sname]["sizes"].get(st["name"].split(" · ", 1)[-1], EXTRA_SUBJECTS[sname].get("size", 20)) if sname in EXTRA_SUBJECTS else 30 if paper2 else 20
                real = "Previous-Year Questions" in st["name"]  # real questions only: any size, printed answer letters
                if not legacy and not real and len(qs) != size:
                    err(f"{where}: {len(qs)} questions, expected {size}")
                letters, ar = Counter(), Counter()
                for i, q in enumerate(qs, 1):
                    opts = q.get("options", {})
                    vals = [opts.get(k, "") for k in "ABCD"]
                    if len(set(vals)) != 4 or not all(v.strip() for v in vals):
                        err(f"{where} Q{i}: needs 4 distinct non-empty options")
                    if q.get("answer") not in "ABCD" or not q.get("answer"):
                        err(f"{where} Q{i}: bad answer")
                    if not (q.get("explanation") or "").strip():
                        err(f"{where} Q{i}: missing explanation")
                    if paper2 and KANNADA.search(q["question"] + " ".join(vals)):
                        err(f"{where} Q{i}: Paper 2 must be English only")
                    letters[q.get("answer")] += 1
                    if "Assertion (A)" in q["question"]:
                        ar[q.get("answer")] += 1
                    k = app_key(q["question"], vals)
                    if k in seen:
                        err(f"{where} Q{i}: duplicate of {seen[k]}")
                    else:
                        seen[k] = f"{where} Q{i}"
                if qs:
                    top, n = letters.most_common(1)[0]
                    if n / len(qs) > 0.5 and not legacy and not real:
                        err(f"{where}: answer {top} is {n}/{len(qs)} — spread answers across A–D")
                    elif n / len(qs) > 0.4:
                        warn(f"{where}: answer {top} is {n}/{len(qs)}")
                if sum(ar.values()) >= 3 and len(ar) == 1:
                    err(f"{where}: all {sum(ar.values())} assertion–reason answers are {next(iter(ar))} — vary them")

for m in warns:
    print("WARN ", m)
for m in errors:
    print("ERROR", m)
print(f"\n{len(seen)} questions checked · {len(errors)} errors · {len(warns)} warnings")
sys.exit(1 if errors else 0)
