"""Mock Set 3 – a full mock made only of real previous-year questions (owner, 13 Nov 2026).

Questions come from packs/pyq-by-subject.json (and the Kannada parts of packs/pyq-p1.json), copied as asked:
option order, answer, explanation and source are kept. Half of each section (rounded up) is drawn from KEA/KSET papers
when the pool has them, the rest from the other papers. Nothing already used in Mock Sets 1–2 is picked again.
Value Education has only one previous-year question in the bank, so its other 9 marks go to Educational Psychology;
Unit 1 has only 8 clean CS-paper questions, so its other 2 marks go to Unit 2.
"""
import json, random, unicodedata, re
from pathlib import Path

ROOT = Path(__file__).parent.parent

# (section shown in results, source topic(s), count)
P1_PLAN = [("General Knowledge", ["General Knowledge", "KRIES – Karnataka & General Studies"], 15),
           ("Current Affairs", ["Current Affairs"], 15),
           ("General Kannada", ["@kannada"], 10),
           ("General English", ["General English"], 10),
           ("Educational Psychology", ["Educational Psychology"], 24),
           ("Computer Literacy", ["Computer Literacy"], 15),
           ("Health Education", ["Health Education"], 10),
           ("Value Education", ["Value Education"], 1)]
P2_PLAN = [("Unit 1 – Fundamentals", 1, 8), ("Unit 2 – Discrete Structures", 2, 10), ("Unit 3 – Computer Architecture", 3, 10),
           ("Unit 4 – Programming & Web", 4, 12), ("Unit 5 – DBMS", 5, 12), ("Unit 6 – OS & System Software", 6, 12),
           ("Unit 7 – Software Engineering", 7, 8), ("Unit 8 – Data Structures & Algorithms", 8, 11),
           ("Unit 9 – Networks", 9, 12), ("Unit 10 – Artificial Intelligence", 10, 5)]

# which papers a section may draw from (the by-subject index files some aptitude/maths/English items under CS units)
GENERAL = r"GK|General Paper|VAO|PSI|UPSC|KRIES|Paper-1|P1"
ALLOW = {"General Knowledge": GENERAL, "Current Affairs": GENERAL, "General English": r"KEC|General Paper|P2|VAO|KSET",
         "Computer Literacy": r"KEC|P2|VAO|UPSC", "Educational Psychology": r"Education|General Paper",
         "Health Education": r".", "Value Education": r".", "General Kannada": r"."}
CS = r"CS|Programmer|Computer Operator|Console|Data Entry"
# misfiled in the index (topic belongs to another section) or not answerable without a figure/other question
EXCLUDE = {"GFGC 2021 CS · Q74", "GTTC 2024 Technician Gr-III CS (C1) · Q38", "GTTC 2024 Technician Gr-III CS (C1) · Q36",
           "Legislative Council 2024 Sr/Jr Programmer P2 · Q35", "GTTC 2024 Technician Gr-III CS (C1) · Q20",
           "GFGC 2021 CS · Q68", "GFGC 2021 CS · Q98",
           "GTTC 2024 Lecturer CS · Q59", "Legislative Council 2024 Data Entry Operator P2 · Q99", "PGCET 2024 M.Tech CS · Q54",
           "PGCET 2026 CS · Q54", "PGCET 2024 M.Tech CS · Q87",
           "KSET 2025 Education · Q30"}  # last: keeps the paper from having three assertion–reason items all keyed A
# a P2 question must also mention its own unit's material (the index files maths/aptitude/English under CS units)
UNIT_KW = {
    1: r"binary|decimal|octal|hexadecimal|number system|complement|bits?|bytes?|ASCII|unicode|memory|storage|ROM|RAM|input device|output device|printer|generation of computer|hardware|software|compiler|interpreter|assembler",
    2: r"sets?|relation|function|group|graph|lattice|proposition|tautology|permutation|combination|probabilit|matrix|eigen|recurrence|automat|DFA|NFA|PDA|grammar|language|Turing|linear programming|optimi|simplex|pigeonhole|induction",
    3: r"gate|flip-?flop|adder|multiplexer|decoder|register|cache|pipelin|instruction|addressing|interrupt|bus|8085|8086|microprocessor|ALU|memory|SoP|PoS|Boolean|K-map|DMA|control word|locality",
    4: r"#include|printf|int main|Java|C\+\+|class|object|inheritance|pointer|HTML|XML|CSS|JavaScript|PHP|servlet|ASP|web|graphics|clipping|rotation|z-buffer|aspect ratio|Python|operator|array|in C|C code|syntax",
    5: r"SQL|relation|normal form|NF|transaction|database|DBMS|key|query|B\+ ?tree|index|NoSQL|warehous|mining|K-means|entity|tuple|join|lock|schema|DML|DDL",
    6: r"process|thread|schedul|deadlock|Banker|pages?|paging|semaphore|kernel|operating system|file system|disk|compiler|pars(er|ing)|LR|LL\(|lexical|assembler|loader|linker|boot|BIOS|hypervisor|activation record|syntax directed|grammar|share|protection",
    7: r"software|SDLC|model|testing|test|COCOMO|UML|use case|requirement|risk|cohesion|coupling|agile|waterfall|spiral|Gantt|time-?line chart|maintenance|version control|architectural design",
    8: r"stack|queue|tree|graph|sort|search|complexity|O\(|hash|heap|algorithm|dynamic programming|greedy|divide and conquer|spanning|shortest path|linked list|AVL|backtracking",
    9: r"network|protocol|TCP|UDP|IP|OSI|layer|router|bridge|switch|Ethernet|port|bandwidth|encoding|CRC|cyclic|frame|MAC|ARP|DNS|HTTP|SMTP|POP|FTP|topology|modulat|cryptograph|encrypt|firewall|wireless|channel|signal|duplex|hyperlink",
    10: r"AI|artificial intelligence|agent|heuristic|neural|fuzzy|learning|knowledge|Prolog|NLP|reinforcement|expert system|Turing|perceptron|genetic|propositional|semantic web|RDF|backpropagation",
}
BAD = ("as in q", "shown below", "figure", "diagram", "given graph", "the image")


def _key(q):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", q["question"])).strip().lower()


def _load():
    by = json.loads((ROOT / "packs" / "pyq-by-subject.json").read_text(encoding="utf-8"))
    topics = {t["name"]: [q for st in t["sets"] for q in st["questions"]] for s in by["subjects"] for t in s["topics"]}
    p1 = json.loads((ROOT / "packs" / "pyq-p1.json").read_text(encoding="utf-8"))
    topics["@kannada"] = [q for s in p1["subjects"] for t in s["topics"] for st in t["sets"] if "Kannada" in st["name"]
                          for q in st["questions"]]
    for i in range(1, 11):
        topics[i] = next(v for k, v in topics.items() if isinstance(k, str) and k.startswith(f"Unit {i} "))
    return topics


def _used_before():
    f = ROOT / "packs" / "mock-papers.json"
    if not f.exists():
        return set()
    pack = json.loads(f.read_text(encoding="utf-8"))
    return {_key(q) for s in pack["subjects"] for t in s["topics"] for st in t["sets"]
            if not st["name"].startswith("3 ·") for q in st["questions"]}


def _pick(pool, n, rng, taken, allow, unit=None):
    pool = [q for q in pool if q.get("source") and _key(q) not in taken and q["source"] not in EXCLUDE
            and re.search(allow, q["source"]) and not any(b in q["question"].lower() for b in BAD)
            and (unit is None or re.search(UNIT_KW[unit], q["question"], re.I))]
    uniq = {}
    for q in pool:
        uniq.setdefault(_key(q), q)
    pool = list(uniq.values())
    rng.shuffle(pool)
    first = [q for q in pool if re.match(r"(KEA|KSET)", q["source"])]
    rest = [q for q in pool if q not in first]
    want = (n + 1) // 2
    got = first[:want]
    got += [q for q in rest + first[want:] if q not in got][:n - len(got)]
    assert len(got) == n, (n, len(got))
    got.sort(key=lambda q: q["source"])
    for q in got:
        taken.add(_key(q))
    return got


def build(seed="mock3-pyq"):
    topics, rng, taken = _load(), random.Random(seed), _used_before()
    out = []
    for plan in (P1_PLAN, P2_PLAN):
        qs = []
        for tag, src, n in plan:
            pool = [q for s in (src if isinstance(src, list) else [src]) for q in topics[s]]
            for q in _pick(pool, n, rng, taken, ALLOW.get(tag, CS), None if isinstance(src, list) else src):
                qs.append({k: q[k] for k in ("question", "options", "answer", "explanation", "source") if k in q} | {"subject": tag})
        out.append(qs)
    return out
