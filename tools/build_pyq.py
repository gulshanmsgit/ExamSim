"""Build the previous-year-paper packs from the transcribed papers (tools/pyq_*.py).

Each paper module defines TOPIC (the paper's name), sets() → [{name, questions: [(q, opts, ans, expl, source)], keep_order}]
and a docstring naming the source PDF. Options stay in the printed order and every question carries `source`
("KSET 2024 CS&A · Q17"), which the app shows as a PYQ badge. Each paper also gets a full-paper mock preset.
Usage: python tools/build_pyq.py
"""
import importlib, json, subprocess, sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
from packlib import build_pack

GROUP = "③ Previous-year papers · KEA / KSET (real questions, source shown on each)"
PYQ_PACKS = {
    "pyq-p2": {"subject": "P2 · Previous-Year Papers (KEA/KSET)", "icon": "📜",
               "papers": ["pyq_kset2023_csa", "pyq_kset2024_csa"],
               "name": "P2 · Previous-year papers — Computer Science (KEA / KSET)"},
}
PYQ_SUBJECTS = {c["subject"] for c in PYQ_PACKS.values()}


def build(key):
    cfg = PYQ_PACKS[key]
    topics, mocks = [], []
    for m in cfg["papers"]:
        mod = importlib.import_module(m)
        sets = mod.sets()
        topics.append({"name": mod.TOPIC, "sets": sets})
        n = sum(len(s["questions"]) for s in sets)
        mocks.append({"name": f"{mod.TOPIC} · full paper", "mode": "count",
                      "sources": [{"subject": cfg["subject"], "topic": mod.TOPIC, "weight": n}]})
    n_q = sum(len(s["questions"]) for t in topics for s in t["sets"])
    desc = (f"Real questions from past KEA / KSET papers ({n_q} so far): " + "; ".join(t["name"] for t in topics)
            + ". Typed from KEA's scanned question papers with the options in the printed order; each question shows its "
              "paper and number. Where KEA publishes no full key, the answer was worked out by ExamSim and says so. "
              "Each paper also comes as a full-paper mock test.")
    out = ROOT / "packs" / f"{key}.json"
    build_pack(out, cfg["name"], desc, [{"name": cfg["subject"], "icon": cfg["icon"], "topics": topics}])
    pack = json.loads(out.read_text(encoding="utf-8"))
    pack["mocks"] = mocks
    out.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")

    idx_path = ROOT / "packs" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    entry = next((p for p in idx["packs"] if p["file"] == out.name), None)
    if not entry:
        entry = {"file": out.name}
        idx["packs"].append(entry)
    entry.update({"group": GROUP, "name": cfg["name"], "description": desc})
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for k in PYQ_PACKS:
        print(f"== {k}")
        build(k)
    subprocess.run([sys.executable, str(TOOLS / "make_index.py")], check=True)
