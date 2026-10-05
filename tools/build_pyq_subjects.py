"""Build packs/pyq-by-subject.json: two Library subjects that collect every REAL previous-year question by syllabus subject.

  P1 · Previous-Year Questions · General Paper  – one topic per Paper 1 subject (GK, English, Ed. Psychology, Computer Literacy, …)
  P2 · Previous-Year Questions · Computer Science  – one topic per Paper 2 unit (Unit 1 … Unit 10)

Sources: every question with a `source` in the topic packs (they were mixed into topic sets word for word), plus the
transcribed full CS papers in packs/pyq-p2.json, which are sorted into units by keyword rules (UNIT_RULES) with manual
corrections in OVERRIDE. Inside a topic, questions are grouped into one set per paper (papers with fewer than MIN_SET questions
are pooled into 'Other papers'). Questions keep their printed option order and official / unofficial answer notes.
Run after building the topic packs:  python tools/build_pyq_subjects.py  then  python tools/make_index.py"""
import json, re, sys
from collections import OrderedDict, defaultdict
from pathlib import Path
from packlib import build_pack

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
MIN_SET = 4

P1_PACKS = OrderedDict([("p1-gk.json", "General Knowledge"), ("p1-ca.json", "Current Affairs"), ("p1-eng.json", "General English"),
                        ("p1-psy.json", "Educational Psychology"), ("p1-cl.json", "Computer Literacy"),
                        ("p1-he.json", "Health Education"), ("p1-ve.json", "Value Education")])
UNITS = ["Unit 1 – Fundamentals of Computers", "Unit 2 – Discrete Structures & Optimization", "Unit 3 – Computer System Architecture",
         "Unit 4 – Programming Languages & Web", "Unit 5 – Database Management Systems", "Unit 6 – System Software & Operating Systems",
         "Unit 7 – Software Engineering", "Unit 8 – Data Structures & Algorithms", "Unit 9 – Data Communication & Networks",
         "Unit 10 – Artificial Intelligence"]
P2_PACK_UNIT = {"p2-u1-complete.json": 1, "p2-u2-complete.json": 2, "p2-u4.json": 4, "p2-u5-01-dbms-concepts.json": 5, "p2-u5.json": 5,
                "p2-u6.json": 6, "p2-u8.json": 8}

# Keyword rules for the transcribed full papers: first match wins (order matters)
UNIT_RULES = [
    (5, r"\bSQL\b|database|relation(al)? (schema|algebra|calculus|model)|normal form|BCNF|\bNF\b|functional dependenc|tuple|transaction|serializ|"
        r"two.phase|2PL|candidate key|primary key|foreign key|superkey|DBMS|RDBMS|index(ed)? (file|structure)|B\+ ?tree|data warehouse|OLAP|data mining|"
        r"ER (model|diagram)|entity|NoSQL|Hadoop|query"),
    (10, r"artificial intelligence|\bAI\b|machine learning|neural|perceptron|fuzzy|genetic algorithm|heuristic|A\* |minimax|alpha.beta|"
         r"expert system|Turing test|natural language|NLP|reinforcement learning|K.means|cluster|classification|regression|supervised|"
         r"knowledge representation|predicate logic|resolution|Bayes|deep learning|chatbot|agent"),
    (7, r"software (engineering|process|testing|maintenance|requirement|quality|reliability|metric|project)|SDLC|waterfall|spiral|agile|scrum|"
        r"prototype model|cohesion|coupling|cyclomatic|COCOMO|function point|black.box|white.box|unit testing|integration testing|"
        r"regression testing|UML|use.case|CMM|risk management|verification and validation|V.model|DevOps"),
    (9, r"network|TCP|UDP|\bIP\b|IPv[46]|OSI|router|routing|switch(ing)?\b|ethernet|LAN|WAN|MAN\b|protocol|HTTP|FTP|SMTP|DNS|DHCP|"
        r"subnet|bandwidth|modulation|multiplex|Nyquist|Shannon|CRC|Hamming|error (detection|correction)|sliding window|ARQ|CSMA|ALOHA|"
        r"topology|wireless|Wi.?Fi|Bluetooth|cryptograph|encryption|RSA|firewall|SSL|TLS|VPN|baud|fibre|fiber|coaxial|channel|MPLS|ATM\b|"
        r"Fast Ethernet|100 ?Base|IoT|cloud|blockchain|cyber|malware|virus|phishing|DES\b|AES\b|digital signature|hash"),
    (6, r"operating system|\bOS\b|process|thread|schedul|semaphore|mutex|deadlock|banker|paging|page fault|page replacement|segmentation|"
        r"virtual memory|thrashing|working set|belady|critical section|monitor|file system|inode|disk scheduling|SCAN|LOOK|"
        r"kernel|system call|fork|context switch|compiler|lexical|token|pars(er|ing)|grammar.*(LL|LR)|LL\(|LR\(|SLR|LALR|syntax.directed|"
        r"three.address|code optimization|symbol table|assembler|loader|linker|macro|interpreter|Linux|Unix|Windows|shell"),
    (3, r"flip.?flop|register|cache|pipeline|instruction|microprocessor|8085|8086|ALU|control unit|addressing mode|RISC|CISC|"
        r"interrupt|DMA|I/O|bus\b|Boolean|K.?map|logic gate|NAND|NOR|XOR|adder|multiplexer|decoder|encoder|counter|"
        r"two'?s complement|floating.point|IEEE 754|binary|octal|hexadecimal|BCD|gray code|memory (hierarchy|organi)|RAM|ROM|"
        r"associative mapping|direct mapping|hit ratio|clock|CPU"),
    (4, r"\bC\+\+|\bC\b (program|language)|printf|scanf|#include|int main|Java|Python|class\b|object|inheritance|polymorphism|"
        r"constructor|destructor|overload|virtual function|exception|HTML|CSS|JavaScript|XML|PHP|JSP|ASP|servlet|applet|DOM|"
        r"web|URL|browser|pointer|function|array of|struct|union|recursion|compile.time|run.time|operator"),
    (8, r"stack|queue|linked list|tree|graph|BFS|DFS|sort|search|hash(ing)? table|heap|AVL|binary search|time complexity|"
        r"O\(|asymptotic|recurrence|dynamic programming|greedy|divide and conquer|Dijkstra|Kruskal|Prim|spanning tree|"
        r"knapsack|Huffman|NP|algorithm|matrix chain|job scheduling|Floyd|Bellman"),
    (2, r"proposition|tautology|predicate|quantifier|set\b|relation|function|lattice|poset|group|ring|field|graph theory|"
        r"planar|Euler|Hamilton|chromatic|combinat|permutation|combination|pigeonhole|probability|recurrence relation|"
        r"linear programming|LPP|simplex|transportation|assignment problem|game theory|automat|DFA|NFA|regular (expression|language)|"
        r"context.free|Turing machine|pushdown|grammar|language|matrix|eigen|determinant|mathematical induction|inference|"
        r"correlation|regression line"),
    (1, r"computer|software|hardware|memory|input|output|storage|generation|MS (Word|Excel|PowerPoint)|spreadsheet|printer|keyboard|"
        r"monitor|disk|motherboard|BIOS|byte|bit\b"),
]
# KSET CS&A papers follow the UGC-NET unit order in blocks of 10 questions. Block → GPSTR unit; "toc" = theory of computation
# and compilers, split by keyword (compiler topics → Unit 6, automata/languages → Unit 2).
BLOCKS = {"KSET 2023 CS&A": [4, 5, 6, 7, 8, "toc", 9, 10, 2, 3],
          "KSET 2024 CS&A": [2, 3, 4, 5, 6, 7, 8, "toc", 9, 10],
          "KSET 2025 CS&A": [2, 3, 4, 5, 6, 7, 8, "toc", 9, 10]}
COMPILER = r"compil|pars(er|ing)|lexical|token|syntax.directed|three.address|code (optimi|generat)|symbol table|activation record|" \
           r"data flow|basic block|LR|LL|SLR|LALR|attribute|peephole|jump"
# The KEA 2026 CS paper is also sectioned, but with uneven blocks: (first Q, last Q, unit)
RANGES = {"KEA 2026 CS Paper-2": [(1, 12, 8), (13, 20, 2), (21, 32, 3), (33, 34, 2), (35, 42, 6), (43, 51, 6), (52, 62, 5),
                                  (63, 72, 9), (73, 85, 4), (86, 100, 2)]}
# Manual corrections after reviewing the sorting: {source: unit}
OVERRIDE = {"KSET 2023 CS&A · Q58": 3}


def load(name):
    return json.loads((PACKS / name).read_text(encoding="utf-8"))


def as_tuple(q):
    opts = [q["options"][k] for k in "ABCD"]
    return (q["question"], opts, "ABCD".index(q["answer"]), q.get("explanation", ""), q["source"])


def paper_of(source):
    return source.rsplit(" · Q", 1)[0]


def qnum(source):
    m = re.search(r"· Q(\d+)$", source)
    return int(m.group(1)) if m else 0


def classify(q):
    text = q["question"] + " " + " ".join(q["options"].values())
    for lo, hi, unit in RANGES.get(paper_of(q["source"]), []):
        if lo <= qnum(q["source"]) <= hi:
            return unit
    blocks = BLOCKS.get(paper_of(q["source"]))
    if blocks:
        b = blocks[min(9, (qnum(q["source"]) - 1) // 10)]
        return (6 if re.search(COMPILER, text) else 2) if b == "toc" else b
    for unit, pat in UNIT_RULES:
        if re.search(pat, text, re.I):
            return unit
    return 1


def sets_for(questions):
    """One set per paper; small papers pooled. Each item: (name, tag, [tuples])."""
    by_paper = defaultdict(list)
    for q in questions:
        by_paper[paper_of(q["source"])].append(q)
    big = sorted((p for p in by_paper if len(by_paper[p]) >= MIN_SET), key=lambda p: (-len(by_paper[p]), p))
    small = [q for p in by_paper if len(by_paper[p]) < MIN_SET for q in by_paper[p]]
    out = []
    for p in big:
        out.append((p, sorted(by_paper[p], key=lambda q: qnum(q["source"]))))
    if small:
        out.append(("Other papers", sorted(small, key=lambda q: (paper_of(q["source"]), qnum(q["source"])))))
    return [{"name": f"{i} · {name}", "tag": name, "questions": [as_tuple(q) for q in qs]} for i, (name, qs) in enumerate(out, 1)]


def collect(pack_names):
    seen, items = set(), []
    for name in pack_names:
        if not (PACKS / name).exists():
            continue
        for s in load(name)["subjects"]:
            for t in s["topics"]:
                for st in t["sets"]:
                    for q in st["questions"]:
                        if q.get("source") and q["source"] not in seen:
                            seen.add(q["source"]); items.append((name, q))
    return items, seen


def main(report=False):
    # ---- Paper 1
    p1_topics = []
    p1_items, _ = collect(P1_PACKS)
    for pack, topic in P1_PACKS.items():
        qs = [q for n, q in p1_items if n == pack]
        if qs:
            p1_topics.append({"name": topic, "sets": sets_for(qs)})
    # ---- Paper 2: topic packs (unit known) + transcribed full papers (unit by keyword)
    by_unit = defaultdict(list)
    p2_items, seen = collect(P2_PACK_UNIT)
    for n, q in p2_items:
        by_unit[P2_PACK_UNIT[n]].append(q)
    for s in load("pyq-p2.json")["subjects"]:
        for t in s["topics"]:
            for st in t["sets"]:
                for q in st["questions"]:
                    src = q.get("source")
                    if not src or src in seen:
                        continue
                    seen.add(src)
                    u = OVERRIDE.get(src) or classify(q)
                    by_unit[u].append(q)
                    if report:
                        print(f"U{u:<2} {src:28} {' '.join(q['question'].split())[:95]}")
    p2_topics = [{"name": UNITS[u - 1], "sets": sets_for(by_unit[u])} for u in range(1, 11) if by_unit[u]]
    if report:
        return
    n1 = sum(len(s["questions"]) for t in p1_topics for s in t["sets"])
    n2 = sum(len(s["questions"]) for t in p2_topics for s in t["sets"])
    desc = (f"Every real KEA / KSET / KPSC-style previous-year question collected so far, sorted by syllabus subject – Paper 1: {n1}, "
            f"Paper 2: {n2}. Each set is one exam paper (small papers are pooled); the source and whether the answer is KEA's official "
            "key are shown with every question. Grows as more papers and topics are added; re-importing adds only new sets.")
    build_pack(PACKS / "pyq-by-subject.json", "Previous-year questions by subject (P1 + P2)", desc,
               [{"name": "P1 · Previous-Year Questions · General Paper", "icon": "📜", "topics": p1_topics},
                {"name": "P2 · Previous-Year Questions · Computer Science", "icon": "📜", "topics": p2_topics}])
    idx_path = PACKS / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == "pyq-by-subject.json"), None)
    if not entry:
        pos = next((i for i, p in enumerate(idx["packs"]) if p["file"] == "pyq-p2.json"), len(idx["packs"]) - 1) + 1
        entry = {"file": "pyq-by-subject.json"}
        idx["packs"].insert(pos, entry)
    entry.update({"group": "③ Previous-year papers · KEA / KSET (real questions, source shown on each)",
                  "name": "Previous-year questions by subject (P1 + P2)", "description": desc})
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(report="--report" in sys.argv)
