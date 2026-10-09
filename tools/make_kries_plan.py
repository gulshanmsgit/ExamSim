"""KRIES Computer Teacher 2026 study plan (owner's request, 10 Oct 2026) – a second exam mode next to GPSTR.

KRIES (Karnataka Residential Educational Institutions Society) recruitment is conducted by KEA: Paper 1 on 26 Oct 2026 and
Paper 2 on 27 Oct 2026. The Paper 2 syllabus for the Computer Teacher post (C Programming, Data Structures, Operating System, plus
C++, DBMS, Software Engineering, System Software, Internet Technology, Java and UNIX, Computer Graphics, Computer Networks) is mapped
onto the GPSTR topics we already have (same plan IDs, so questions, notes and progress are shared). Only two areas are not in the
GPSTR syllabus; they become topics of the extra subject 'P2 · KRIES – Additional Topics' (P2-KR-01 Java, P2-KR-02 Computer Graphics).
Paper 1 (owner's request, 10 Oct 2026, from the KRIES notification: 100 questions, 100 marks, 2 hours) is KEA's general paper
(items A–O: current affairs, general science, geography, social science, Indian society, history of India and Karnataka,
Constitution and public administration, practical knowledge and mental ability at SSLC level, Karnataka's social and cultural
history, land reforms, economy, rural development / Panchayat Raj / co-operatives, science and technology in administration,
environment). It reuses the GPSTR GK and current-affairs topics; the Karnataka items, mental ability and SSLC social science become
topics of 'P1 · KRIES – Karnataka & General Studies' (P1-KR-01…09). New KRIES Paper 1 questions are written in Kannada, KEA style.
In KRIES mode the app shows only the subjects and topics in this plan.

Writes packs/kries-2026-plan.json and adds it to packs/index.json (group '① Start here'). Run tools/make_index.py afterwards.
Usage: python tools/make_kries_plan.py
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "packs" / "kries-2026-plan.json"
START = dt.date(2026, 10, 10)
EXTRA_SUBJECT = "P2 · KRIES – Additional Topics"
P1_SUBJECT = "P1 · KRIES – Karnataka & General Studies"

# (group, [(plan id, topic, KRIES syllabus coverage, priority, hours)])
P2_GROUPS = [
    ("C Programming", "KRIES core area · Unit 4 topics", [
        ("P2-U4-03", "Programming in C – Part 1", "History and structure of a C program, character set, constants, variables, keywords; type declaration, arithmetic "
         "instructions, integer/float conversion, operators and their hierarchy; formatted and unformatted I/O; if/else, logical, relational and conditional "
         "operators; while, do-while, for, break, continue, switch, goto; 1-D and 2-D arrays, bubble sort; strings and library functions; structures, unions, "
         "typedef, enum, bit fields", "High", 3.0),
        ("P2-U4-04", "Programming in C – Part 2", "Functions – definition, prototypes, types, arguments, recursion, passing arrays; storage classes (auto, register, "
         "extern, static); pointers – notation, pointers and arrays, arrays of pointers, call by value / reference, pointer to pointer; bitwise operators "
         "(AND, OR, XOR, complement, shifts); preprocessor – macros, file inclusion; files – modes, text and binary files, high- and low-level I/O, "
         "command-line arguments", "High", 3.0),
    ]),
    ("Data Structures", "KRIES core area · Unit 8 topics", [
        ("P2-U8-06", "Performance Analysis & Recurrences", "Introduction to time and space complexity", "Medium", 0.75),
        ("P2-U8-01", "Linear Data Structures", "Definition, classification and operations; primitive data structures and strings using pointers; 1-D and 2-D array "
         "storage, insertion and deletion; linked lists (singly, circular, doubly) with dynamic memory allocation; stacks – sequential and linked, Tower of "
         "Hanoi, infix to postfix, postfix evaluation; queues – circular, priority, deque", "High", 2.0),
        ("P2-U8-02", "Trees", "Binary trees, sequential and linked representation, insertion and deletion, traversals", "High", 1.0),
        ("P2-U8-03", "Sets & Graph Representation", "Graph concepts, sequential and linked representation, BFS and DFS", "Medium", 1.0),
        ("P2-U8-04", "Sorting and Searching", "Linear and binary search; selection, insertion, quick and merge sort (bubble sort with C arrays)", "High", 1.25),
    ]),
    ("Operating System", "KRIES core area · Unit 6 topics", [
        ("P2-U6-02", "OS Basics", "History; batch, multiprogrammed, time-sharing, personal, distributed and real-time systems; OS structures – command interpreter, "
         "services, system calls, system programs", "High", 1.0),
        ("P2-U6-03", "Process Management & IPC", "Process concept, process control block, process scheduling", "Medium", 0.75),
        ("P2-U6-06", "CPU Scheduling", "Basic concepts; FIFO, RR, SJF, multilevel and multilevel feedback queue scheduling", "High", 1.0),
        ("P2-U6-08", "Memory Management", "Logical and physical address space, swapping, contiguous allocation, paging, segmentation", "High", 1.0),
        ("P2-U6-09", "Virtual Memory", "Demand paging, page replacement and its algorithms, allocation of frames, thrashing, demand segmentation", "High", 1.0),
        ("P2-U6-11", "File Systems", "File concept, access methods, directory structure, protection, file-system structure, allocation methods, free-space management", "Medium", 1.0),
        ("P2-U6-10", "Storage Management", "Secondary storage – disk structure, disk scheduling", "Medium", 0.75),
        ("P2-U6-12", "I/O Systems", "Overview of I/O systems and I/O interfaces", "Low", 0.5),
    ]),
    ("Other areas in the syllabus", "Listed by name only in the KRIES syllabus – revise the basics", [
        ("P2-U4-05", "Object Oriented Programming", "OOPS using C++ – classes, objects, inheritance, polymorphism", "Medium", 0.75),
        ("P2-U4-06", "Programming in C++ – Part 1", "OOPS using C++ – tokens, functions, classes, constructors and destructors", "Medium", 1.0),
        ("P2-U4-07", "Programming in C++ – Part 2", "OOPS using C++ – overloading, virtual functions, inheritance, templates, exceptions, files", "Medium", 1.0),
        ("P2-U5-01", "DBMS Concepts and Architecture", "Database Management System – concepts and architecture", "Medium", 0.75),
        ("P2-U5-02", "ER Model & Relational Model", "Database Management System – ER and relational model", "Medium", 0.75),
        ("P2-U5-04", "SQL – Part 1", "Database Management System – SQL", "Medium", 0.75),
        ("P2-U5-06", "Normalization", "Database Management System – normalization", "Medium", 0.75),
        ("P2-U7-01", "Software Process Models", "Software Engineering – process models", "Medium", 0.75),
        ("P2-U7-03", "Software Requirements", "Software Engineering – requirements", "Low", 0.5),
        ("P2-U7-04", "Software Design", "Software Engineering – design", "Low", 0.5),
        ("P2-U7-05", "Software Testing", "Software Engineering – testing", "Medium", 0.75),
        ("P2-U6-01", "System Software", "System Software – assemblers, loaders, linkers, compilers, interpreters", "Medium", 0.75),
        ("P2-U4-08", "Web Programming – HTML, DHTML, CSS", "Internet Technology / Internet Lab – HTML, CSS", "Medium", 0.75),
        ("P2-U4-09", "Web Programming – XML, Scripting, JavaScript", "Internet Technology – XML, JavaScript", "Medium", 0.75),
        ("P2-U9-10", "World Wide Web & Applications", "Internet Technology – URL, DNS, e-mail, FTP, TELNET", "Medium", 0.75),
        ("P2-KR-01", "Basic Java Programming", "Basic Java – features, JVM and bytecode, data types, operators, control statements, classes and objects, "
         "constructors, inheritance, interfaces, packages, exception handling, strings, applets", "Medium", 1.0),
        ("P2-U6-14", "Linux Operating System", "UNIX programming – commands, file system, permissions, shell", "Medium", 0.75),
        ("P2-KR-02", "Computer Graphics", "Computer Graphics – display devices, line and circle drawing (DDA, Bresenham), 2-D transformations, "
         "windowing and clipping, colour models", "Medium", 1.0),
        ("P2-U9-01", "Data Communication – Part 1", "Computer Networks – data communication basics", "Low", 0.5),
        ("P2-U9-03", "Computer Networks & Topologies", "Computer Networks – topologies, LAN, MAN, WAN", "Medium", 0.5),
        ("P2-U9-04", "Network Models", "Computer Networks – OSI and TCP/IP models", "High", 0.75),
        ("P2-U9-05", "Data Link Layer", "Computer Networks – error detection, flow control", "Low", 0.5),
        ("P2-U9-06", "Multiple Access, Devices & VLANs", "Computer Networks – CSMA/CD, network devices", "Medium", 0.5),
        ("P2-U9-07", "IPv4 Addressing", "Computer Networks – IP addressing", "Medium", 0.5),
        ("P2-U9-09", "Transport Layer", "Computer Networks – TCP and UDP", "Medium", 0.5),
    ]),
]

# Paper 1: (group, meta, [(plan id, KRIES syllabus coverage, priority, hours)]); topic names come from the structure pack,
# the current-affairs subject (P1-CA-xx) or P1_NEW (the KRIES-only topics)
P1_NEW = {
    "P1-KR-01": "Land Reforms and Social Change in Karnataka",
    "P1-KR-02": "Karnataka Economy – Strengths, Weaknesses and Current Status",
    "P1-KR-03": "Rural Development, Panchayat Raj and Rural Co-operatives",
    "P1-KR-04": "Science and Technology in Karnataka Administration",
    "P1-KR-05": "Environment and Development of Karnataka",
    "P1-KR-06": "Mental Ability – Reasoning",
    "P1-KR-07": "Practical Knowledge – SSLC Arithmetic",
    "P1-KR-08": "Social Science – SSLC Basics",
    "P1-KR-09": "Social and Cultural History of Karnataka",
}
CA_NAMES = {"P1-CA-01": "Current International Affairs", "P1-CA-02": "Current National Affairs", "P1-CA-05": "Important Days and Slogans",
            "P1-CA-09": "Monuments and National Forests", "P1-CA-13": "Indian Constitution"}
P1_GROUPS = [
    ("Karnataka (items I–N)", "KRIES Paper 1 · Karnataka-specific items – heavily asked in KEA general papers", [
        ("P1-KR-09", "(I) Social and cultural history of Karnataka – religious and social reform (Basavanna, Dasas), Wodeyars and Dewans, "
         "armed rebellions, freedom movement, unification, literature and culture", "High", 1.5),
        ("P1-KR-01", "(J) Land reforms in Karnataka after independence and social change – 1961 and 1974 Acts, land tribunals, "
         "Devaraj Urs, backward-class commissions, debt relief and bonded labour", "High", 1.5),
        ("P1-KR-02", "(K) Karnataka's economy – strengths and weaknesses, current status (economic survey, budget, GSDP, sectors, schemes)", "High", 1.5),
        ("P1-KR-03", "(L) Rural development, Panchayat Raj institutions and rural co-operatives", "High", 1.5),
        ("P1-KR-04", "(M) Role of science and technology in effective administration in Karnataka (e-governance)", "Medium", 1.0),
        ("P1-KR-05", "(N) Environmental problems and development of Karnataka", "Medium", 1.0),
    ]),
    ("History, society and culture (items E, F)", "GPSTR GK topics", [
        ("P1-GK-05", "(F) History of Karnataka – dynasties, culture, art and architecture", "High", 1.0),
        ("P1-GK-06", "(E, F) Indian society and its history – ancient India", "Medium", 1.0),
        ("P1-GK-07", "(E, F) Medieval India", "Medium", 1.0),
        ("P1-GK-08", "(E, F) Modern India and the freedom struggle", "High", 1.0),
    ]),
    ("Constitution and public administration (item G)", "GPSTR GK and current-affairs topics", [
        ("P1-GK-15", "(G) Indian Constitution – fundamental rights, legislature, executive, judiciary; public administration", "High", 2.0),
        ("P1-CA-13", "(G) Constitution – amendments, articles and bodies in the news", "Medium", 1.0),
    ]),
    ("Science, geography and social science (items B, C, D)", "GPSTR GK topics + SSLC social science", [
        ("P1-GK-02", "(B) Inventions and discoveries", "Medium", 0.5),
        ("P1-GK-03", "(B) General science – physics, chemistry, biology (SSLC level)", "High", 1.0),
        ("P1-GK-04", "(B) Health and hygiene", "Low", 0.5),
        ("P1-GK-10", "(C) Geography – basic concepts, land and people", "Medium", 0.75),
        ("P1-GK-11", "(C) Geography – population, literacy, festivals", "Medium", 0.75),
        ("P1-GK-12", "(C) Geography – natural regions, resources, crops", "Medium", 0.75),
        ("P1-CA-09", "(C) Monuments and national parks", "Low", 0.5),
        ("P1-KR-08", "(D) Social science at SSLC level – civics, economics, sociology, business studies", "Medium", 1.0),
        ("P1-GK-13", "(D) Indian economy – industries, projects, public undertakings", "Medium", 0.75),
    ]),
    ("Practical knowledge and mental ability (items H, O)", "SSLC-level reasoning and arithmetic", [
        ("P1-KR-06", "(H, O) Mental ability – series, analogy, coding–decoding, blood relations, directions, ranking, calendar, clocks, "
         "statements and conclusions", "High", 1.5),
        ("P1-KR-07", "(H) Practical knowledge – percentages, ratio, averages, profit and loss, interest, time and work, speed, mensuration", "High", 1.5),
    ]),
    ("Current affairs (item A)", "Planner CA topics + monthly current affairs (P1 · Current Affairs)", [
        ("P1-CA-01", "(A) International affairs", "High", 0.75),
        ("P1-CA-02", "(A) National affairs", "High", 0.75),
        ("P1-GK-14", "(A) Awards, honours and prizes", "Medium", 0.75),
        ("P1-CA-05", "(A) Important days and slogans", "Medium", 0.5),
    ]),
]

# Calendar: (Paper 2 plan IDs, extra Paper 2 text, Paper 1 plan IDs, extra Paper 1 text, phase)
DAYS = [
    (["P2-U4-03"], "", ["P1-GK-05", "P1-KR-01"], "", "Learning"),                                           # Sat 10
    (["P2-U4-04", "P2-U8-06"], "", ["P1-GK-06", "P1-GK-07", "P1-KR-09"], "", "Learning"),                   # Sun 11
    (["P2-U8-01"], "", ["P1-GK-08"], "", "Learning"),                                                       # Mon 12
    (["P2-U8-02", "P2-U8-03", "P2-U8-04"], "", ["P1-GK-15"], "", "Learning"),                               # Tue 13
    (["P2-U6-02", "P2-U6-03", "P2-U6-06"], "", ["P1-CA-13"], "Constitution revision – public administration", "Learning"),  # Wed 14
    (["P2-U6-08", "P2-U6-09"], "", ["P1-KR-03"], "", "Learning"),                                           # Thu 15
    (["P2-U6-11", "P2-U6-10", "P2-U6-12"], "", ["P1-KR-02", "P1-GK-13"], "", "Learning"),                   # Fri 16
    (["P2-U4-05", "P2-U4-06", "P2-U4-07"], "", ["P1-GK-10", "P1-GK-11", "P1-GK-12"], "", "Learning"),       # Sat 17
    (["P2-U5-01", "P2-U5-02", "P2-U5-04", "P2-U5-06"], "", ["P1-KR-05", "P1-CA-09"], "", "Learning"),       # Sun 18
    (["P2-U7-01", "P2-U7-03", "P2-U7-04", "P2-U7-05"], "", ["P1-GK-02", "P1-GK-03", "P1-GK-04"], "", "Learning"),  # Mon 19
    (["P2-U6-01", "P2-U4-08", "P2-U4-09", "P2-U9-10"], "", ["P1-KR-04"], "", "Learning"),                   # Tue 20
    (["P2-KR-01"], "", ["P1-KR-06"], "", "Learning"),                                                       # Wed 21
    (["P2-U6-14", "P2-KR-02"], "", ["P1-KR-07", "P1-KR-08"], "", "Learning"),                               # Thu 22
    (["P2-U9-01", "P2-U9-03", "P2-U9-04", "P2-U9-05"], "", ["P1-CA-01", "P1-CA-02"],
     "Monthly current affairs January – June 2026 (P1 · Current Affairs)", "Learning"),                     # Fri 23
    (["P2-U9-06", "P2-U9-07", "P2-U9-09"], "Full mock test – Paper 2 (evening) + analysis", ["P1-GK-14", "P1-CA-05"],
     "Monthly current affairs July – October 2026 (P1 · Current Affairs)", "Learning"),                     # Sat 24
    ([], "Light revision – C output and pointer questions, Data Structures and OS short notes",
     [], "Full mock test – Paper 1 (KEA general paper, 100 questions, 2 hours) + analysis; Karnataka notes", "MOCK TEST"),  # Sun 25
    ([], "Evening: Paper 2 weak topics from the mock (light)", [], "PAPER 1 EXAM – General paper (KRIES)", "Exam"),   # Mon 26
    ([], "PAPER 2 EXAM – Computer Teacher (KRIES)", [], "", "Exam"),                                        # Tue 27
]


def p1_names():
    st = json.loads((ROOT / "packs" / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
    names = {t["plan"]["id"]: t["name"] for s in st["subjects"] for t in s["topics"] if t.get("plan", {}).get("id", "").startswith("P1-")}
    return {**names, **CA_NAMES, **P1_NEW}


def sheet_groups(groups, when):
    out = []
    for g, meta, rs in groups:
        rows = []
        for pid, topic, cov, pri, hrs in rs:
            ds = when[pid]
            rows.append({"id": pid, "subject": g, "topic": topic, "coverage": cov, "priority": pri, "hours": hrs, "start": ds[0], "target": ds[-1],
                         "day": dt.date.fromisoformat(ds[0]).strftime("%a"), "status": "Not Started", "rev1": "No", "rev2": "No",
                         "confidence": None, "tip": "", "notes": ""})
        out.append({"name": g, "meta": [meta, f"{len(rows)} topics"], "rows": rows})
    return out


def main():
    names = p1_names()
    p1_groups = [(g, meta, [(pid, names[pid], cov, pri, hrs) for pid, cov, pri, hrs in rs]) for g, meta, rs in P1_GROUPS]
    rows = {r[0]: r for _, _, rs in P2_GROUPS + p1_groups for r in rs}
    cal, when = [], {}
    for i, (ids2, extra2, ids1, extra1, phase) in enumerate(DAYS):
        d = START + dt.timedelta(days=i)
        for pid in ids2 + ids1:
            when.setdefault(pid, []).append(d.isoformat())
        weekend = d.weekday() >= 5
        cal.append({"date": d.isoformat(), "day": d.strftime("%a"), "phase": phase, "hours": 8.0 if weekend else 4.5,
                    "p2": [f"{pid} {rows[pid][1]}" for pid in ids2] + ([extra2] if extra2 else []),
                    "p1": [f"{pid} {rows[pid][1]}" for pid in ids1] + ([extra1] if extra1 else []),
                    "habit": "10 C output questions + 15 min Karnataka current affairs", "done": False})
    missing = set(rows) - set(when)
    assert not missing, f"plan rows not on the calendar: {missing}"
    groups2, groups1 = sheet_groups(P2_GROUPS, when), sheet_groups(p1_groups, when)
    new_topics = lambda pre: [{"name": topic, "plan": {"id": pid, "start": when[pid][0], "end": when[pid][-1], "priority": pri, "tip": "", "coverage": cov}}
                              for _, _, rs in P2_GROUPS + p1_groups for pid, topic, cov, pri, _ in rs if pid.startswith(pre)]
    extra_topics, p1_topics = new_topics("P2-KR-"), sorted(new_topics("P1-KR-"), key=lambda t: t["plan"]["id"])
    pack = {
        "examsimPack": 1,
        "name": "Study plan · KRIES Computer Teacher 2026",
        "description": "Exam mode for KRIES Computer Teacher recruitment (KEA): Paper 1 (general paper) on 26 Oct and Paper 2 (Computer Teacher) on "
                       "27 Oct 2026. An 18-day plan from 10 Oct mapped onto the topics you already have, plus KRIES-only topics (Paper 1: Karnataka "
                       "land reforms, economy, Panchayat Raj, e-governance, environment, social and cultural history, mental ability, SSLC "
                       "arithmetic and social science – in Kannada; Paper 2: Java, Computer Graphics). Importing it switches the app to KRIES "
                       "mode; switch back to GPSTR any time in Profile → Exam mode.",
        "subjects": [{"name": P1_SUBJECT, "icon": "🏛", "topics": p1_topics}, {"name": EXTRA_SUBJECT, "icon": "🖥", "topics": extra_topics}],
        "studyPlan": {
            "key": "kries", "title": "KRIES Computer Teacher 2026 study plan", "examDate": "2026-10-26",
            "exams": [{"paper": "Paper 1", "date": "2026-10-26"}, {"paper": "Paper 2", "date": "2026-10-27"}], "papers": ["p1", "p2"],
            "marks": {}, "notes": ["KRIES Paper 1 (100 questions, 100 marks, 2 hours): KEA's general paper – current affairs, general science, "
                                   "geography, social science, history of India and Karnataka, Constitution and public administration, mental "
                                   "ability (SSLC level) and Karnataka's history, land reforms, economy, Panchayat Raj, administration and environment.",
                                   "KRIES Paper 2 (Computer Teacher) syllabus: C Programming, Data Structures and Operating System in detail; OOPS using C++, "
                                   "DBMS, Software Engineering, System Software, Internet Technology, Basic Java and UNIX, Computer Graphics and Computer "
                                   "Networks by name.", "KRIES mode shows only the topics in this plan."],
            "statuses": ["Not Started", "In Progress", "Completed", "Review Required"],
            "sheets": {"p1": {"title": "PAPER 1 (GENERAL) — KRIES 2026", "source": "KRIES notification §10, Paper 1 items A–O",
                              "howTo": "GK and current-affairs topics are shared with GPSTR; Karnataka items and mental ability are KRIES topics (in Kannada).",
                              "groups": groups1},
                       "p2": {"title": "PAPER 2 (COMPUTER TEACHER) — KRIES 2026", "source": "KRIES Computer Teacher syllabus (Paper 2)",
                              "howTo": "Topics reuse the GPSTR question bank; progress is shared between the two exams.", "groups": groups2}},
            "calendar": cal},
    }
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == OUT.name), None)
    if not entry:
        at = max(i for i, p in enumerate(idx["packs"]) if "①" in p.get("group", "")) + 1
        entry = {"group": "① Start here", "file": OUT.name}
        idx["packs"].insert(at, entry)
    entry.update({"name": pack["name"], "description": pack["description"]})
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n1, n2 = (sum(len(g["rows"]) for g in gs) for gs in (groups1, groups2))
    print(f"KRIES plan: {len(cal)} days {cal[0]['date']} – {cal[-1]['date']}, {n1} Paper 1 topics ({len(p1_topics)} new), "
          f"{n2} Paper 2 topics ({len(extra_topics)} new)")


if __name__ == "__main__":
    main()
