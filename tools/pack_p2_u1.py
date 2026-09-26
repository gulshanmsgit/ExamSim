"""Pack: Paper 2 · Unit 1 – Fundamentals of Computers, complete (all topics and sub-topics × 30)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from packlib import build_pack
import p2u1_a, p2u1_b, p2u1_c, p2u1_d

ORDER = ["Introduction & Functional Components", "Evolution, Generations, Classification, Applications",
         "Input, Output and Memory Devices", "Software Concepts & Problem Solving Methodology",
         "Word Processing, Spreadsheets, PowerPoint", "Computer Configuration & Motherboard", "Memory, Power Supply & Assembling"]
ALL = {**p2u1_a.TOPICS, **p2u1_b.TOPICS, **p2u1_c.TOPICS, **p2u1_d.TOPICS}
assert list(ALL) == ORDER or set(ALL) == set(ORDER), set(ALL) ^ set(ORDER)
topics = []
for t in ORDER:
    sets = []
    for name, qs in ALL[t]:
        assert len(qs) == 30, f"{t} / {name}: {len(qs)} questions"
        sets.append({"name": name, "tag": name.split(" · ", 1)[1], "questions": qs})
    topics.append({"name": t, "sets": sets})

build_pack(sys.argv[1], "P2 · Unit 1 — Fundamentals of Computers (complete)",
           "All 7 topics of Unit 1 split into 20 syllabus sub-topics, 30 questions each: introduction, functional units, evolution, generations, "
           "classification, applications, I/O and memory devices, software, problem solving, Word, Excel, PowerPoint, configuration, motherboard, memory, power supply, assembling.",
           [{"name": "P2 · Unit 1 – Fundamentals of Computers", "icon": "🖥️", "topics": topics}])
