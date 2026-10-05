"""Refresh packs/index.json from the pack files themselves.

Keeps each entry's hand-written fields (group, name, description, order) and recomputes what the app
needs to show packs inside subjects, topics and study-plan days:
  questions, topics, subjects (subject names), planIds (study-plan topic IDs covered).
A pack listed in index.json but missing on disk fails loudly. The study-plan pack is added if missing.
Usage: python tools/make_index.py
"""
import hashlib, json, re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
PACKS = Path(__file__).parent.parent / "packs"
idx_path = PACKS / "index.json"
idx = json.loads(idx_path.read_text(encoding="utf-8"))
structure = json.loads((PACKS / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))


def key(s):  # same normalisation idea as nameKey() in the app
    s = re.sub(r"^p[12]\s*·\s*", "", s.strip().lower())
    s = re.sub(r"\(.*?\)", " ", s.replace("&", " and ").replace("+", " plus ").replace("#", " sharp "))
    return re.sub(r"[^\w]+", " ", s).strip()


plan_ids = {(key(s["name"]), key(t["name"])): t["plan"]["id"] for s in structure["subjects"] for t in s["topics"]}

if not any(p["file"] == "gpstr-cst-2026-plan.json" for p in idx["packs"]) and (PACKS / "gpstr-cst-2026-plan.json").exists():
    idx["packs"].insert(1, {"group": "① Start here", "file": "gpstr-cst-2026-plan.json",
                            "name": "Study plan (your Excel planner)",
                            "description": "All 245 planner rows, the tracker and the 63-day calendar. Opens in 📅 Study plan in the bottom bar; your status updates sync to all devices."})

for entry in idx["packs"]:
    raw = (PACKS / entry["file"]).read_text(encoding="utf-8")
    pack = json.loads(raw)
    subjects, ids, questions, topics = [], [], 0, 0
    for s in pack.get("subjects", []):
        subjects.append(s["name"])
        for t in s.get("topics", []):
            n = sum(len(st.get("questions", [])) for st in t.get("sets", []))
            topics += 1
            questions += n
            pid = (t.get("plan") or {}).get("id") or plan_ids.get((key(s["name"]), key(t["name"])))
            if pid and n:
                ids.append(pid)
    entry["questions"] = questions
    entry["topics"] = topics
    entry["subjects"] = subjects
    entry["planIds"] = sorted(set(ids))
    # content version: the app offers "Update" when a pack it imported earlier has changed since
    entry["v"] = hashlib.md5(raw.encode("utf-8")).hexdigest()[:10]
    if pack.get("studyPlan"):
        entry["studyPlan"] = True
    print(f"{entry['file']:40} {questions:5d} Q {topics:4d} topics  plan IDs: {len(entry['planIds'])}")

idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
