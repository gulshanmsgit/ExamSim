"""KRIES Computer Teacher 2026 study plan (owner's request, 10 Oct 2026) – a second exam mode next to GPSTR.

KRIES (Karnataka Residential Educational Institutions Society) recruitment is conducted by KEA: Paper 1 on 26 Oct 2026 and
Paper 2 on 27 Oct 2026. The Paper 2 syllabus for the Computer Teacher post (C Programming, Data Structures, Operating System, plus
C++, DBMS, Software Engineering, System Software, Internet Technology, Java and UNIX, Computer Graphics, Computer Networks) is mapped
onto the GPSTR topics we already have (same plan IDs, so questions, notes and progress are shared). Only two areas are not in the
GPSTR syllabus; they become topics of the extra subject 'P2 · KRIES – Additional Topics' (P2-KR-01 Java, P2-KR-02 Computer Graphics).
The owner wants KRIES mode to cover Paper 2 only, so the plan has no Paper 1 sheet rows or tasks, and in KRIES mode the app shows
only the subjects and topics in this plan.

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

# (group, [(plan id, topic, KRIES syllabus coverage, priority, hours)])
GROUPS = [
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

# Calendar: (Paper 2 plan IDs, extra Paper 2 text, Paper 1 text, phase)
P1_NOTE = ""  # KRIES mode covers Paper 2 only (owner's choice, 10 Oct 2026)
DAYS = [
    (["P2-U4-03"], "", P1_NOTE, "Learning"),                                            # Sat 10
    (["P2-U4-04", "P2-U8-06"], "", P1_NOTE, "Learning"),                                # Sun 11
    (["P2-U8-01"], "", P1_NOTE, "Learning"),                                            # Mon 12
    (["P2-U8-02", "P2-U8-03", "P2-U8-04"], "", P1_NOTE, "Learning"),                    # Tue 13
    (["P2-U6-02", "P2-U6-03", "P2-U6-06"], "", P1_NOTE, "Learning"),                    # Wed 14
    (["P2-U6-08", "P2-U6-09"], "", P1_NOTE, "Learning"),                                # Thu 15
    (["P2-U6-11", "P2-U6-10", "P2-U6-12"], "", P1_NOTE, "Learning"),                    # Fri 16
    (["P2-U4-05", "P2-U4-06", "P2-U4-07"], "", P1_NOTE, "Learning"),                    # Sat 17
    (["P2-U5-01", "P2-U5-02", "P2-U5-04", "P2-U5-06"], "", P1_NOTE, "Learning"),        # Sun 18
    (["P2-U7-01", "P2-U7-03", "P2-U7-04", "P2-U7-05"], "", P1_NOTE, "Learning"),        # Mon 19
    (["P2-U6-01", "P2-U4-08", "P2-U4-09", "P2-U9-10"], "", P1_NOTE, "Learning"),        # Tue 20
    (["P2-KR-01"], "", P1_NOTE, "Learning"),                                            # Wed 21
    (["P2-U6-14", "P2-KR-02"], "", P1_NOTE, "Learning"),                                # Thu 22
    (["P2-U9-01", "P2-U9-03", "P2-U9-04", "P2-U9-05"], "", P1_NOTE, "Learning"),        # Fri 23
    (["P2-U9-06", "P2-U9-07", "P2-U9-09"], "Revision – C Programming (output and pointer questions)", P1_NOTE, "Learning"),  # Sat 24
    ([], "Full mock test – Paper 2 (C, Data Structures, OS) + analysis", "", "MOCK TEST"),  # Sun 25
    ([], "Final revision – C, Data Structures and OS short notes; weak topics from the mock", "", "Final Revision"),  # Mon 26
    ([], "PAPER 2 EXAM – Computer Teacher (KRIES)", "", "Exam"),                    # Tue 27
]


def main():
    rows = {r[0]: (g, r) for g, _, rs in GROUPS for r in rs}
    cal, when = [], {}
    for i, (ids, extra, p1, phase) in enumerate(DAYS):
        d = START + dt.timedelta(days=i)
        for pid in ids:
            when.setdefault(pid, []).append(d.isoformat())
        weekend = d.weekday() >= 5
        cal.append({"date": d.isoformat(), "day": d.strftime("%a"), "phase": phase, "hours": 6.5 if weekend else 3.0,
                    "p2": [f"{pid} {rows[pid][1][1]}" for pid in ids] + ([extra] if extra else []),
                    "p1": [p1] if p1 else [], "habit": "Solve 10 C output-prediction questions", "done": False})
    missing = set(rows) - set(when)
    assert not missing, f"plan rows not on the calendar: {missing}"
    groups = []
    for g, meta, rs in GROUPS:
        out = []
        for pid, topic, cov, pri, hrs in rs:
            ds = when[pid]
            out.append({"id": pid, "subject": g, "topic": topic, "coverage": cov, "priority": pri, "hours": hrs, "start": ds[0], "target": ds[-1],
                        "day": dt.date.fromisoformat(ds[0]).strftime("%a"), "status": "Not Started", "rev1": "No", "rev2": "No",
                        "confidence": None, "tip": "", "notes": ""})
        groups.append({"name": g, "meta": [meta, f"{len(out)} topics"], "rows": out})
    extra_topics = [{"name": topic, "plan": {"id": pid, "start": when[pid][0], "end": when[pid][-1], "priority": pri, "tip": "", "coverage": cov}}
                    for _, _, rs in GROUPS for pid, topic, cov, pri, _ in rs if pid.startswith("P2-KR-")]
    pack = {
        "examsimPack": 1,
        "name": "Study plan · KRIES Computer Teacher 2026",
        "description": "Exam mode for KRIES Computer Teacher recruitment (KEA), Paper 2 (Computer Teacher) on 27 Oct 2026. An 18-day plan from 10 Oct mapped "
                       "onto the topics you already have, plus two KRIES-only topics (Java, Computer Graphics). Importing it switches the app to KRIES mode; "
                       "switch back to GPSTR any time in Profile → Exam mode.",
        "subjects": [{"name": EXTRA_SUBJECT, "icon": "🖥", "topics": extra_topics}],
        "studyPlan": {
            "key": "kries", "title": "KRIES Computer Teacher 2026 study plan", "examDate": "2026-10-27",
            "exams": [{"paper": "Paper 2", "date": "2026-10-27"}], "papers": ["p2"],
            "marks": {}, "notes": ["KRIES Paper 2 (Computer Teacher) syllabus: C Programming, Data Structures and Operating System in detail; OOPS using C++, "
                                   "DBMS, Software Engineering, System Software, Internet Technology, Basic Java and UNIX, Computer Graphics and Computer "
                                   "Networks by name.", "KRIES mode shows only the Paper 2 (Computer Teacher) syllabus."],
            "statuses": ["Not Started", "In Progress", "Completed", "Review Required"],
            "sheets": {"p1": {"title": "PAPER 1 — KRIES 2026", "source": "Syllabus to be added", "howTo": "", "groups": []},
                       "p2": {"title": "PAPER 2 (COMPUTER TEACHER) — KRIES 2026", "source": "KRIES Computer Teacher syllabus (Paper 2)",
                              "howTo": "Topics reuse the GPSTR question bank; progress is shared between the two exams.", "groups": groups}},
            "calendar": cal},
    }
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    if not any(p["file"] == OUT.name for p in idx["packs"]):
        at = max(i for i, p in enumerate(idx["packs"]) if "①" in p.get("group", "")) + 1
        idx["packs"].insert(at, {"group": "① Start here", "file": OUT.name, "name": pack["name"], "description": pack["description"]})
        idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n = sum(len(g["rows"]) for g in groups)
    print(f"KRIES plan: {len(cal)} days {cal[0]['date']} – {cal[-1]['date']}, {n} Paper 2 topics ({len(extra_topics)} new)")


if __name__ == "__main__":
    main()
