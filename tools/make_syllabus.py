"""Build packs/syllabus.json: the official syllabus text of every subject (from the GPT_P1 / GPT_P2 PDFs, extracted to
tools/syllabus_src/*.txt with `pdftotext -layout`), joined with the planner topics (plan ID, dates, coverage) and the
sub-topics of each topic (tools/syllabus_map.json). The app's Today tab and subject pages show it.
Kannada-script parts of the PDFs use a legacy font that does not extract, so General Kannada shows the planner topics only.
Usage: python tools/make_syllabus.py
"""
import json, re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
TOOLS = Path(__file__).parent
ROOT = TOOLS.parent
SRC = TOOLS / "syllabus_src"


def clean(t):
    t = t.replace("�", "–")
    t = re.sub(r"\s*Page \d+ of \d+\s*", " ", t)
    return re.sub(r"\s+", " ", t).strip(" ,")


def between(text, start, end):
    a = text.index(start) + len(start)
    b = text.index(end, a) if end else len(text)
    return text[a:b]


def headed_sections(block):
    """'Heading: text. Heading: text.' → [{title, text}] (a block without headings becomes one section)."""
    body = clean(block)
    parts = re.split(r"(?:(?<=[.;,])|^)\s*([A-Z][A-Za-z0-9 ,&/()'+\-]{2,70}?)\s?:\s", body)
    if len(parts) < 3:
        return [{"title": "Syllabus", "text": body}]
    out = [{"title": "Syllabus", "text": parts[0].strip()}] if parts[0].strip() else []
    for i in range(1, len(parts) - 1, 2):
        out.append({"title": parts[i].strip(), "text": parts[i + 1].strip(" .;,") + "."})
    return out


def short_title(x):
    return re.split(r"\s*:\s|\s+[-–]\s+", x, 1)[0].strip(" .")


def numbered_items(block, pat=r"(?:^|\s)(\d{1,2})\.\s+"):
    items = [clean(x) for x in re.split(pat, block)[2::2]]
    return [{"title": short_title(x), "text": x} for x in items if x]


p2 = (SRC / "p2.txt").read_text(encoding="utf-8")
p1 = (SRC / "p1.txt").read_text(encoding="utf-8")
official = {}

# Paper 2: one block per unit
units = re.split(r"\n\s*Unit\s*[-–� ]*\s*(\d+)\s*:", p2)
for i in range(1, len(units) - 1, 2):
    n, block = int(units[i]), units[i + 1]
    block = block.split("References:")[0]
    title, _, rest = block.partition("\n")
    official[f"P2 · Unit {n}"] = {"heading": clean(title), "sections": headed_sections(rest)}

# Paper 1 (English-script sections only)
gk = between(p1, "SYLLABUS FOR GENERAL KNOWLEDGE", "REFERANCE BOOKS")
official["P1 · General Knowledge"] = {"heading": "General Knowledge", "sections": numbered_items(gk),
                                      "note": "Current affairs topics (12, 13) are part of the syllabus but have no question packs here."}
eng = between(p1, "GENERAL ENGLISH SYLLABUS", "Suggested Reference Book:")
eng_items = [clean(x).replace(" o ", " · ") for x in re.split(r"[•�]", eng) if clean(x)]
official["P1 · General English"] = {"heading": "General English", "sections": [{"title": short_title(x), "text": x} for x in eng_items]}
psy = between(p1, "EDUCATIONAL PSYCHOLOGY\n", "SCIENCE AND ITS BRANCHES")
psy_items = [clean(x) for x in re.split(r"\n(?=[A-Z][A-Za-z ]+[-–]| ?[A-Z][a-z]+ [a-z]+ of|Transfer|Learning|Domains|Theories|Trial|Personality|Cognitive|Mental)", psy) if clean(x)]
official["P1 · Educational Psychology"] = {"heading": "Educational Psychology", "sections": [{"title": re.split(r"\s*[-–:]\s*", x, 1)[0], "text": x} for x in psy_items]}
cl = between(p1, "SYLLABUS FOR COMPUTER LITERACY", "*****")
cl_items = [clean(x) for x in re.split(r"\n(?=Unit\s*-?\s*\d)", cl) if clean(x)]
official["P1 · Computer Literacy"] = {"heading": "Computer Literacy", "sections": [{"title": re.sub(r"^Unit\s*-?\s*(\d+)\s*:\s*", r"Unit \1: ", x).split(":")[0] + ": " + x.split(":")[1].strip() if x.count(":") >= 2 else x.split(":")[0], "text": x.split(":", 2)[-1].strip() if x.count(":") >= 2 else x} for x in cl_items]}
he = between(p1, "Health Education\n", "Reference Books")
official["P1 · Health Education"] = {"heading": "Health Education", "sections": numbered_items(he)}
ve = between(p1, "Value Education\n", "Reference Books")
official["P1 · Value Education"] = {"heading": "Value Education", "sections": numbered_items(ve)}

structure = json.loads((ROOT / "packs" / "gpstr-cst-2026-00-structure.json").read_text(encoding="utf-8"))
smap = json.loads((TOOLS / "syllabus_map.json").read_text(encoding="utf-8"))
out = {"title": "GPSTR / CST 2026 syllabus", "subjects": {}}
for s in structure["subjects"]:
    m = re.match(r"(P2 · Unit \d+)", s["name"])
    off = official.get(m.group(1) if m else s["name"])
    out["subjects"][s["name"]] = {
        "official": off,
        "topics": [{"id": t["plan"]["id"], "name": t["name"], "start": t["plan"].get("start"), "end": t["plan"].get("end"),
                    "priority": t["plan"].get("priority"), "coverage": t["plan"].get("coverage", ""),
                    "subs": smap.get(s["name"], {}).get(t["name"], [])} for t in s["topics"]],
    }
(ROOT / "packs" / "syllabus.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for name, v in out["subjects"].items():
    o = v["official"]
    print(f"{name:55} official sections: {len(o['sections']) if o else '—':>3}   topics: {len(v['topics'])}")
