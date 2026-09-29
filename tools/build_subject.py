"""Build one pack per subject / unit from its content modules, then list it in the Question bank.

Usage:  python tools/build_subject.py <key> [<key> …]      e.g.  python tools/build_subject.py p2-u4 p1-psy
        python tools/build_subject.py all

Each content module (tools/<module>.py) exports TOPICS = {"<planner topic>": [("1 · <Sub-topic>", QUESTIONS), …]}.
A pack grows topic by topic: add a module (or topics to one) and rebuild. The builder checks
topic names against the planner (structure pack), set names against tools/syllabus_map.json and
set sizes (Paper 2: 30, Paper 1: 20), writes packs/<key>.json, adds/updates its packs/index.json
entry and refreshes the index. Run tools/check_packs.py afterwards.
"""
import importlib, json, subprocess, sys
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
from packlib import build_pack

P1_GROUP = "② Paper 1 · General (20 questions per set)"
P2_GROUP = "② Paper 2 · Computer Science (30 questions per sub-topic)"

# key: subject (exact planner name) and its content modules, in planner order
PACKS = {
    "p2-u4": {"subject": "P2 · Unit 4 – Programming Languages & Web", "modules": ["p2u4_a", "p2u4_b", "p2u4_c", "p2u4_d", "p2u4_e"]},
    "p2-u8": {"subject": "P2 · Unit 8 – Data Structures & Algorithms", "modules": ["p2u8_a", "p2u8_b", "p2u8_c"]},
    "p1-psy": {"subject": "P1 · Educational Psychology", "modules": ["p1_psy_a", "p1_psy_b", "p1_psy_c"]},
    "p1-gk": {"subject": "P1 · General Knowledge", "modules": ["p1_gk_a", "p1_gk_b"]},
    "p1-cl": {"subject": "P1 · Computer Literacy", "modules": ["p1_cl_a", "p1_cl_b", "p1_cl_c"]},
    "p1-eng": {"subject": "P1 · General English", "modules": ["p1_eng_a", "p1_eng_b", "p1_eng_c"]},
    "p1-he": {"subject": "P1 · Health Education", "modules": ["p1_he_a", "p1_he_b"]},
    "p1-ve": {"subject": "P1 · Value Education", "modules": ["p1_ve_a", "p1_ve_b"]},
    "p1-ca": {"subject": "P1 · Current Affairs", "modules": ["p1_ca_2026"]},
}

# Subjects that are not in the planner. Current affairs: one topic per month ("January 2026", …) with a
# Karnataka set (30 Q) and a National set (10 Q) – the owner's 75% Karnataka / 25% national rule.
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
EXTRA_SUBJECTS = {"P1 · Current Affairs": {"icon": "📰", "topics": [f"{m} {y}" for y in (2026, 2027) for m in MONTHS],
                                          "sizes": {"Karnataka": 30, "National": 10}, "group": "③ Current affairs (monthly · 75% Karnataka, 25% national)"}}


def build(key):
    cfg = PACKS[key]
    subject = cfg["subject"]
    structure = json.loads((ROOT / "packs" / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
    smap = json.loads((TOOLS / "syllabus_map.json").read_text(encoding="utf-8"))
    extra = EXTRA_SUBJECTS.get(subject)
    ssub = {"icon": extra["icon"], "topics": [{"name": t} for t in extra["topics"]]} if extra else next(s for s in structure["subjects"] if s["name"] == subject)
    planned = [t["name"] for t in ssub["topics"]]
    size = 30 if subject.startswith("P2") else 20
    content = {}
    for m in cfg["modules"]:
        content.update(importlib.import_module(m).TOPICS)
    missing = [t for t in content if t not in planned]
    assert not missing, f"topics not in the planner for {subject}: {missing}"
    topics = []
    for t in planned:  # planner order
        if t not in content:
            continue
        sets = []
        for i, (name, qs) in enumerate(content[t], 1):
            num, sub = name.split(" · ", 1)
            assert num == str(i), f"{t} / {name}: sets must be numbered 1, 2, 3…"
            want_n = extra["sizes"][sub] if extra else size
            assert len(qs) == want_n, f"{t} / {name}: {len(qs)} questions, expected {want_n}"
            sets.append({"name": name, "tag": sub, "questions": qs})
        want = smap.get(subject, {}).get(t)
        assert want == [s["tag"] for s in sets], f"{t}: sets {[s['tag'] for s in sets]} differ from syllabus_map {want}"
        topics.append({"name": t, "sets": sets})
    n_sets = sum(len(t["sets"]) for t in topics)
    title = subject.replace(" – ", " — ", 1)
    covered = "all topics" if len(topics) == len(planned) else f"{len(topics)} of {len(planned)} topics"
    desc = (f"{covered.capitalize()} so far ({n_sets} sets × {size} questions): " + "; ".join(t["name"] for t in topics)
            + ". More topics are added to this pack as the plan goes on; re-importing only adds the new sets.")
    if extra:
        desc = ("Month-by-month current affairs from January 2026: 75% Karnataka and 25% national, including important schemes. "
                "Facts checked against news sources, which are named in the explanations. Months so far: " + ", ".join(t["name"] for t in topics) + ".")
    out = ROOT / "packs" / f"{key}.json"
    build_pack(out, title, desc, [{"name": subject, "icon": ssub.get("icon", ""), "topics": topics}])

    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == out.name), None)
    if not entry:
        entry = {"file": out.name}
        idx["packs"].append(entry)
    entry.update({"group": extra["group"] if extra else P2_GROUP if subject.startswith("P2") else P1_GROUP, "name": title, "description": desc})
    # keep groups together in the Question bank: start, Paper 1, Paper 2, daily practice
    order = lambda p: ("①" not in p["group"], "Paper 2" in p["group"], "③" in p["group"])
    idx["packs"].sort(key=order)
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    keys = list(PACKS) if sys.argv[1:] == ["all"] else sys.argv[1:]
    if not keys or any(k not in PACKS for k in keys):
        sys.exit(f"usage: build_subject.py <key>… | all   (keys: {', '.join(PACKS)})")
    for k in keys:
        print(f"== {k}")
        build(k)
    subprocess.run([sys.executable, str(TOOLS / "make_index.py")], check=True)
    subprocess.run([sys.executable, str(TOOLS / "make_syllabus.py")], check=True, stdout=subprocess.DEVNULL)  # sub-topics shown in the app
