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
    "p2-u5": {"subject": "P2 · Unit 5 – Database Management Systems", "modules": ["p2u5_b", "p2u5_c", "p2u5_d", "p2u5_e", "p2u5_f"]},
    "p2-u6": {"subject": "P2 · Unit 6 – System Software & Operating Systems", "modules": ["p2u6_a", "p2u6_b", "p2u6_c", "p2u6_d", "p2u6_e", "p2u6_f", "p2u6_g", "p2u6_h", "p2u6_i"]},
    "p2-u9": {"subject": "P2 · Unit 9 – Data Communication & Networks", "modules": ["p2u9_a", "p2u9_b", "p2u9_c", "p2u9_d", "p2u9_e", "p2u9_f"]},
    "p2-u3": {"subject": "P2 · Unit 3 – Computer System Architecture", "modules": ["p2u3_a", "p2u3_b", "p2u3_c", "p2u3_d", "p2u3_e"]},
    "p2-u7": {"subject": "P2 · Unit 7 – Software Engineering", "modules": ["p2u7_a", "p2u7_b"]},
    "p2-u10": {"subject": "P2 · Unit 10 – Artificial Intelligence", "modules": ["p2u10_a", "p2u10_b"]},
    "p2-u8": {"subject": "P2 · Unit 8 – Data Structures & Algorithms", "modules": ["p2u8_a", "p2u8_b", "p2u8_c", "p2u8_d", "p2u8_e", "p2u8_f"]},
    "p1-psy": {"subject": "P1 · Educational Psychology", "modules": ["p1_psy_a", "p1_psy_b", "p1_psy_c", "p1_psy_d", "p1_psy_e", "p1_psy_f", "p1_psy_g", "p1_psy_h", "p1_psy_i", "p1_psy_j", "p1_psy_k", "p1_psy_l", "p1_psy_m", "p1_psy_n", "p1_psy_o", "p1_psy_p", "p1_psy_q"]},
    "p1-gk": {"subject": "P1 · General Knowledge", "modules": ["p1_gk_a", "p1_gk_b", "p1_gk_c", "p1_gk_d", "p1_gk_e", "p1_gk_f", "p1_gk_g", "p1_gk_pyq", "p1_gk_notes", "p1_gk_h", "p1_gk_i", "p1_gk_j", "p1_gk_k"]},
    "p1-cl": {"subject": "P1 · Computer Literacy", "modules": ["p1_cl_a", "p1_cl_b", "p1_cl_c", "p1_cl_d", "p1_cl_e", "p1_cl_f", "p1_cl_g", "p1_cl_h", "p1_cl_i", "p1_cl_j", "p1_cl_k", "p1_cl_l", "p1_cl_m"]},
    "p1-eng": {"subject": "P1 · General English", "modules": ["p1_eng_a", "p1_eng_b", "p1_eng_c", "p1_eng_d", "p1_eng_e", "p1_eng_f", "p1_eng_g", "p1_eng_h", "p1_eng_i", "p1_eng_j", "p1_eng_k", "p1_eng_l"]},
    "p1-he": {"subject": "P1 · Health Education", "modules": ["p1_he_a", "p1_he_b", "p1_he_c", "p1_he_d", "p1_he_e", "p1_he_f", "p1_he_g", "p1_he_h", "p1_he_i"]},
    "p1-ve": {"subject": "P1 · Value Education", "modules": ["p1_ve_a", "p1_ve_b", "p1_ve_c", "p1_ve_d", "p1_ve_e", "p1_ve_f", "p1_ve_g"]},
    "p1-ca": {"subject": "P1 · Current Affairs", "modules": ["p1_ca_plan_a", "p1_ca_plan_b", "p1_ca_plan_c", "p1_ca_plan_d", "p1_ca_plan_e", "p1_ca_plan_f", "p1_ca_2026", "p1_ca_2026_b", "p1_ca_2026_c", "p1_ca_2026_d", "p1_ca_2026_e", "p1_ca_plan_g", "p1_ca_plan_h", "p1_ca_plan_i"]},
    # KRIES Paper 1 topics that are not in the GPSTR syllabus (tools/make_kries_plan.py); questions in Kannada, KEA style
    "p2-kries": {"subject": "P2 · KRIES – Additional Topics", "modules": ["p2_kr_a"]},
    # KRIES Computer Teacher syllabus 'Computer Fundamentals and C Programming' – one topic per heading (owner's request, 13 Oct 2026)
    "p2-kries-ds": {"subject": "P2 · KRIES – Data Structures", "modules": ["p2_krd_a", "p2_krd_b", "p2_krd_c", "p2_krd_d"]},
    "p2-kries-c": {"subject": "P2 · KRIES – C Programming", "modules": ["p2_krc_a", "p2_krc_b", "p2_krc_c", "p2_krc_d", "p2_krc_e", "p2_krc_f", "p2_krc_g"]},
    "p1-kries": {"subject": "P1 · KRIES – Karnataka & General Studies", "modules": ["p1_kr_a", "p1_kr_b", "p1_kr_c", "p1_kr_d", "p1_kr_e"]},
}

# Subjects that are not in the planner. Current affairs: one topic per month ("January 2026", …) with a
# Karnataka set (30 Q) and a National set (10 Q) – the owner's 75% Karnataka / 25% national rule.
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# The planner's own current-affairs topics (P1-CA-01 … 15) are not in the structure pack; they live in this subject too
CA_PLAN = {"Current International Affairs": "P1-CA-01", "Current National Affairs": "P1-CA-02", "Movies": "P1-CA-03",
           "Currency and Capitals of Countries": "P1-CA-04", "Important Days and Slogans": "P1-CA-05",
           "Festivals, Folk Dances, Tribes of the Country": "P1-CA-06", "United Nations Organizations and Headquarters": "P1-CA-07",
           "Initiatives in Education in India": "P1-CA-08", "Monuments and National Forests": "P1-CA-09",
           "Important Tourist Places and Peaks": "P1-CA-10", "Industries and Ores": "P1-CA-11", "Three Wings of the Army": "P1-CA-12",
           "Indian Constitution": "P1-CA-13", "Highways, Railways and Airport Names": "P1-CA-14", "Abbreviations": "P1-CA-15",
           # planner General Knowledge rows on current affairs, left out of the structure pack (tools/make_structure.py SKIP_IDS)
           "Current International Affairs – India's Foreign Relations": "P1-GK-16", "Current State and National Affairs": "P1-GK-17"}
EXTRA_SUBJECTS = {"P1 · Current Affairs": {"icon": "📰", "topics": list(CA_PLAN) + [f"{m} {y}" for y in (2026, 2027) for m in MONTHS],
                                          "plan": CA_PLAN, "sizes": {"Karnataka": 30, "National": 10},
                                          "group": "③ Current affairs (planner topics + monthly · 75% Karnataka, 25% national)"},
                  # KRIES Computer Teacher topics that are not in the GPSTR syllabus (tools/make_kries_plan.py); Paper 2 sets of 30
                  "P2 · KRIES – Additional Topics": {"icon": "🖥", "topics": ["Basic Java Programming", "Computer Graphics"],
                                                     "plan": {"Basic Java Programming": "P2-KR-01", "Computer Graphics": "P2-KR-02"}, "sizes": {}, "size": 30,
                                                     "group": "② Paper 2 · Computer Science (30 questions per sub-topic)"},
                  # KRIES 'Computer Fundamentals and C Programming' syllabus headings (P2-KRC-01…10, tools/make_kries_plan.py); reuses GPSTR Unit 4 C questions
                  "P2 · KRIES – C Programming": {"icon": "©", "topics": ["Introduction to C Programming", "C Instructions", "Control Structures", "Arrays", "Functions", "Pointers", "Structures and Unions", "Bitwise Operators", "C Preprocessor", "Files"],
                                                 "plan": {"Introduction to C Programming": "P2-KRC-01", "C Instructions": "P2-KRC-02", "Control Structures": "P2-KRC-03", "Arrays": "P2-KRC-04", "Functions": "P2-KRC-05", "Pointers": "P2-KRC-06", "Structures and Unions": "P2-KRC-07", "Bitwise Operators": "P2-KRC-08", "C Preprocessor": "P2-KRC-09", "Files": "P2-KRC-10"}, "sizes": {}, "size": 30,
                                                 "group": "② Paper 2 · Computer Science (30 questions per sub-topic)"},
                  # KRIES 'Data Structures' syllabus headings (P2-KRD-01…09, tools/make_kries_plan.py); reuses GPSTR Unit 8 questions
                  "P2 · KRIES – Data Structures": {"icon": "🌳", "topics": ["Introduction to Data Structures", "Primitive Data Structures", "Arrays in Data Structures", "Linked Lists", "Stacks", "Queues", "Trees – Binary Trees", "Graphs", "Searching and Sorting"],
                                                   "plan": {"Introduction to Data Structures": "P2-KRD-01", "Primitive Data Structures": "P2-KRD-02", "Arrays in Data Structures": "P2-KRD-03", "Linked Lists": "P2-KRD-04", "Stacks": "P2-KRD-05", "Queues": "P2-KRD-06", "Trees – Binary Trees": "P2-KRD-07", "Graphs": "P2-KRD-08", "Searching and Sorting": "P2-KRD-09"}, "sizes": {}, "size": 30,
                                                   "group": "② Paper 2 · Computer Science (30 questions per sub-topic)"},
                  # KRIES Paper 1 topics that are not in the GPSTR syllabus (P1-KR-01…09, tools/make_kries_plan.py); sets of 20, in Kannada
                  "P1 · KRIES – Karnataka & General Studies": {"icon": "🏛", "topics": [
                      "Land Reforms and Social Change in Karnataka", "Karnataka Economy – Strengths, Weaknesses and Current Status",
                      "Rural Development, Panchayat Raj and Rural Co-operatives", "Science and Technology in Karnataka Administration",
                      "Environment and Development of Karnataka", "Mental Ability – Reasoning", "Practical Knowledge – SSLC Arithmetic",
                      "Social Science – SSLC Basics", "Social and Cultural History of Karnataka"],
                      "plan": {"Land Reforms and Social Change in Karnataka": "P1-KR-01", "Karnataka Economy – Strengths, Weaknesses and Current Status": "P1-KR-02",
                               "Rural Development, Panchayat Raj and Rural Co-operatives": "P1-KR-03", "Science and Technology in Karnataka Administration": "P1-KR-04",
                               "Environment and Development of Karnataka": "P1-KR-05", "Mental Ability – Reasoning": "P1-KR-06",
                               "Practical Knowledge – SSLC Arithmetic": "P1-KR-07", "Social Science – SSLC Basics": "P1-KR-08",
                               "Social and Cultural History of Karnataka": "P1-KR-09"},
                      "sizes": {}, "size": 20, "group": "② Paper 1 · General (20 questions per set)"}}


def build(key):
    cfg = PACKS[key]
    subject = cfg["subject"]
    structure = json.loads((ROOT / "packs" / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
    smap = json.loads((TOOLS / "syllabus_map.json").read_text(encoding="utf-8"))
    extra = EXTRA_SUBJECTS.get(subject)
    ssub = {"icon": extra["icon"], "topics": [{"name": t} for t in extra["topics"]]} if extra else next(s for s in structure["subjects"] if s["name"] == subject)
    planned = [t["name"] for t in ssub["topics"]]
    size = 30 if subject.startswith("P2") else 20
    content, notes = {}, {}
    for m in cfg["modules"]:
        mod = importlib.import_module(m)
        for k, v in mod.TOPICS.items():  # a later module may add sets to a topic (e.g. a "Previous-Year Questions" set)
            content.setdefault(k, []).extend(v)
        notes.update(getattr(mod, "NOTES", {}))  # optional ready-made notes per topic: [{"title", "md"}]
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
            want_n = extra["sizes"].get(sub, size) if extra else size
            if sub.startswith("Previous-Year Questions"):  # real questions only – as many as the papers give
                assert len(qs) >= 4, f"{t} / {name}: only {len(qs)} questions"
            else:
                assert len(qs) == want_n, f"{t} / {name}: {len(qs)} questions, expected {want_n}"
            sets.append({"name": name, "tag": sub, "questions": qs})
        want = smap.get(subject, {}).get(t)
        assert want == [s["tag"] for s in sets], f"{t}: sets {[s['tag'] for s in sets]} differ from syllabus_map {want}"
        pid = (extra or {}).get("plan", {}).get(t)
        topics.append({"name": t, "sets": sets, **({"plan": {"id": pid}} if pid else {}), **({"notes": notes[t]} if t in notes else {})})
    n_sets = sum(len(t["sets"]) for t in topics)
    title = subject.replace(" – ", " — ", 1)
    covered = "all topics" if len(topics) == len(planned) else f"{len(topics)} of {len(planned)} topics"
    desc = (f"{covered.capitalize()} so far ({n_sets} sets × {size} questions): " + "; ".join(t["name"] for t in topics)
            + ". More topics are added to this pack as the plan goes on; re-importing only adds the new sets.")
    if extra and subject == "P1 · Current Affairs":
        plan_t = [t["name"] for t in topics if t.get("plan")]
        months = [t["name"] for t in topics if not t.get("plan")]
        desc = ("The planner's current-affairs topics (with detailed notes and real KEA questions)" + (": " + "; ".join(plan_t) if plan_t else "")
                + ". Plus month-by-month current affairs from January 2026 (75% Karnataka, 25% national), facts checked against news "
                "sources named in the explanations. Months so far: " + ", ".join(months) + ".")
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
