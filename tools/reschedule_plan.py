"""Reschedule the GPSTR CST 2026 study plan (owner's request, 10 Oct 2026): restart it on 10 Oct and finish on 30 Nov,
with the exam date set to 30 Nov.

The 42 learning days (26 Sep – 6 Nov) move forward exactly two weeks (10 Oct – 20 Nov), so weekdays stay weekdays and the heavy
Saturday/Sunday days stay on weekends. The 21 buffer, revision, mock and final-revision days (7 – 27 Nov) are packed into the last
10 days (21 – 30 Nov): the two buffer days are dropped, pairs of unit-revision days are merged, and all three mocks are kept.

Updates, in place:
  packs/gpstr-cst-2026-plan.json      calendar dates, weekday labels, hours, row start/target dates, examDate, and a dateMap
                                      {old date: new date} that the app uses to move 'day done' ticks
  packs/gpstr-cst-2026-00-structure.json   each topic's plan.start / plan.end
Run once after tools/make_plan.py; running it again does nothing (it checks the first calendar date).
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN, STRUCT = ROOT / "packs" / "gpstr-cst-2026-plan.json", ROOT / "packs" / "gpstr-cst-2026-00-structure.json"
OLD_START, NEW_START, EXAM = "2026-09-26", "2026-10-10", "2026-11-30"
LEARNING_DAYS, SHIFT = 42, 14

D = dt.date.fromisoformat
fmt = lambda d: d.isoformat()

pack = json.loads(PLAN.read_text(encoding="utf-8"))
sp = pack["studyPlan"]
cal = sp["calendar"]
if cal[0]["date"] != OLD_START:
    raise SystemExit(f"Plan already rescheduled (starts {cal[0]['date']}); nothing to do.")
assert len(cal) == 63 and all(c["phase"] == "Learning" for c in cal[:LEARNING_DAYS]), "unexpected calendar layout"

# Old day numbers (1-based) of the tail, merged into the last 10 days: (old days, phase, hours)
TAIL = [((50,), "MOCK TEST", 6.5),            # Sat 21 Nov – Full mock 1
        ((51,), "Revision", 6.5),             # Sun 22 Nov – Mock 1 analysis + weak topics
        ((45, 46), "Revision", 3.5),          # Mon – Units 1 + 4
        ((47, 48), "Revision", 3.5),          # Tue – Units 8 + 5
        ((49, 52), "Revision", 3.5),          # Wed – Units 6 + 9
        ((53, 54), "Revision", 3.5),          # Thu – Units 3 + 2
        ((55, 56), "Revision", 3.5),          # Fri – Units 7 + 10
        ((57,), "MOCK TEST", 6.5),            # Sat 28 Nov – Full mock 2
        ((58,), "MOCK TEST", 6.5),            # Sun 29 Nov – Full mock 3 + analysis
        ((59, 60, 61, 62, 63), "Final Revision", 3.0)]  # Mon 30 Nov – final revision + last look (exam day)
DROPPED = (43, 44)                            # buffer / catch-up days

new_cal, date_map = [], {}
for i, c in enumerate(cal[:LEARNING_DAYS]):
    nd = D(c["date"]) + dt.timedelta(days=SHIFT)
    date_map[c["date"]] = fmt(nd)
    new_cal.append({**c, "date": fmt(nd), "day": nd.strftime("%a")})
first_tail = D(new_cal[-1]["date"]) + dt.timedelta(days=1)
for k, (olds, phase, hours) in enumerate(TAIL):
    nd = first_tail + dt.timedelta(days=k)
    src = [cal[o - 1] for o in olds]
    for c in src:
        date_map[c["date"]] = fmt(nd)
    new_cal.append({"date": fmt(nd), "day": nd.strftime("%a"), "phase": phase, "hours": hours,
                    "p2": list(dict.fromkeys(t for c in src for t in c["p2"])), "p1": list(dict.fromkeys(t for c in src for t in c["p1"])),
                    "habit": src[0].get("habit", ""), "done": False})
for o in DROPPED:  # buffer days point to the first revision day after them
    date_map[cal[o - 1]["date"]] = new_cal[LEARNING_DAYS + 2]["date"]
assert new_cal[-1]["date"] == EXAM and len(new_cal) == 52 and len(date_map) == 63

remap = lambda d: date_map.get(d, d) if d else d
for sheet in sp["sheets"].values():
    for g in sheet["groups"]:
        for r in g["rows"]:
            r["start"], r["target"] = remap(r["start"]), remap(r["target"])
            if r.get("start"):
                r["day"] = D(r["start"]).strftime("%a")
sp["calendar"], sp["examDate"], sp["dateMap"] = new_cal, EXAM, date_map
sp["rescheduled"] = "Rescheduled on 10 Oct 2026: 10 Oct – 30 Nov (was 26 Sep – 27 Nov); learning days moved two weeks, revision and mocks packed into 21–30 Nov."
PLAN.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

st = json.loads(STRUCT.read_text(encoding="utf-8"))
n = 0
for s in st["subjects"]:
    for t in s["topics"]:
        p = t.get("plan")
        if p:
            p["start"], p["end"] = remap(p.get("start")), remap(p.get("end"))
            n += 1
STRUCT.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"calendar {new_cal[0]['date']} – {new_cal[-1]['date']} ({len(new_cal)} days), exam {EXAM}; {n} topic dates moved")
