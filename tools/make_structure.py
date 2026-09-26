"""Build the ExamSim structure pack (subjects, topics, plan dates, mock presets)
from the CST 2026 study planner. Current affairs are excluded (dynamic content)."""
import json, re, sys, warnings
from pathlib import Path
import openpyxl

warnings.filterwarnings("ignore")
SRC = Path(r"C:\Users\DELL\Downloads\CST_2026_Study_Planner.xlsx")
OUT = Path(sys.argv[1])

P1_NAMES = {
    "General Knowledge": ("P1 · General Knowledge", "🌍"),
    "General Kannada": ("P1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ)", "ಕ"),
    "General English": ("P1 · General English", "📝"),
    "Educational Psychology": ("P1 · Educational Psychology", "🧠"),
    "Computer Literacy": ("P1 · Computer Literacy", "💻"),
    "Health Education": ("P1 · Health Education", "🩺"),
    "Value Education": ("P1 · Value Education", "🌱"),
}
UNIT_ICONS = {1: "🖥️", 2: "🔢", 3: "🔌", 4: "⌨️", 5: "🗄️", 6: "⚙️", 7: "🛠️", 8: "🌳", 9: "🌐", 10: "🤖"}
# Current-affairs rows are dynamic, so they are left out of the question bank
SKIP_IDS = {"P1-GK-16", "P1-GK-17"}

wb = openpyxl.load_workbook(SRC, data_only=True)
subjects = {}  # name -> {name, icon, topics: []}


def day(v):
    return v.strftime("%Y-%m-%d") if hasattr(v, "strftime") else (str(v)[:10] if v else None)


for sheet in ("Paper 1 Plan", "Paper 2 Plan"):
    ws = wb[sheet]
    for row in ws.iter_rows(min_row=1, values_only=True):
        rid = row[0]
        if not isinstance(rid, str) or not re.match(r"P[12]-[A-Z0-9]+-\d+$", rid):
            continue
        if "-CA-" in rid or "-REV-" in rid or rid in SKIP_IDS:
            continue
        subj, topic, coverage, priority = row[1], row[2], row[3], row[4]
        start, end, tip = day(row[6]), day(row[7]), row[13]
        if rid.startswith("P1"):
            name, icon = P1_NAMES[subj]
        else:
            unit = int(re.match(r"Unit (\d+)", subj).group(1))
            name, icon = "P2 · " + subj, UNIT_ICONS[unit]
        s = subjects.setdefault(name, {"name": name, "icon": icon, "topics": []})
        plan = {"id": rid, "start": start, "end": end, "priority": priority}
        if tip:
            plan["tip"] = str(tip)
        if coverage:
            plan["coverage"] = str(coverage)
        s["topics"].append({"name": str(topic).strip(), "plan": plan})

p1 = lambda k: P1_NAMES[k][0]
units = {int(re.match(r"P2 · Unit (\d+)", n).group(1)): n for n in subjects if n.startswith("P2")}
pack = {
    "examsimPack": 1,
    "name": "GPSTR / CST 2026 — Syllabus & study plan",
    "description": "All Paper 1 and Paper 2 subjects and topics from the official syllabus, with your study-planner dates. "
                   "Current affairs are left out. Import this first, then the question packs.",
    "subjects": list(subjects.values()),
    "mocks": [
        {"name": "Paper 1 full mock (85 Q, without current affairs)", "mode": "count", "prefer": "unseen",
         "sources": [{"subject": p1("General Knowledge"), "weight": 15}, {"subject": p1("General Kannada"), "weight": 10},
                     {"subject": p1("General English"), "weight": 10}, {"subject": p1("Educational Psychology"), "weight": 15},
                     {"subject": p1("Computer Literacy"), "weight": 15}, {"subject": p1("Health Education"), "weight": 10},
                     {"subject": p1("Value Education"), "weight": 10}]},
        {"name": "Paper 2 full mock (100 Q, computer science)", "mode": "count", "prefer": "unseen",
         "sources": [{"subject": units[u], "weight": w} for u, w in
                     [(1, 10), (2, 8), (3, 10), (4, 12), (5, 12), (6, 12), (7, 8), (8, 11), (9, 12), (10, 5)]]},
    ],
}
OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(pack["subjects"]), "subjects,", sum(len(s["topics"]) for s in pack["subjects"]), "topics")
for s in pack["subjects"]:
    print(f"  {s['name']}: {len(s['topics'])}")
