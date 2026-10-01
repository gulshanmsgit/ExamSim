"""Parse KEA's official FINAL key PDFs (text-based) in sources/pyq/keys/final_*.pdf into sources/pyq/keys/<name>.json:
{"A1": {"1": "3", ...}, "B1": {...}, ...}. Answers are KEA option numbers 1-4 (or text such as 'GRACE' / '1 or 3').
Usage: python tools/pyq_keys.py"""
import json, re, subprocess
from pathlib import Path

KEYS = Path(__file__).resolve().parent.parent / "sources" / "pyq" / "keys"


def parse(pdf):
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, encoding="utf-8").stdout
    versions = ["A1", "B1", "C1", "D1"]
    out = {v: {} for v in versions}
    if re.search(r"A1\s+ANS\s+B1\s+ANS", text):  # GTTC layout: a (question, answer) column pair per version
        pair = re.compile(r"(\d+)\s+(\d(?:\s*(?:or|,|&)\s*\d)*|[A-Z]+)(?=\s|$)")
        for line in text.splitlines():
            pairs = pair.findall(line.strip())
            if len(pairs) == 4:
                for (q, ans), v in zip(pairs, versions):
                    out[v][q] = " ".join(ans.split())
        return out
    for line in text.splitlines():
        # one or two blocks per line: Q a b c d
        toks = re.findall(r"\S+(?: or \S+)*", line)
        i = 0
        while i + 4 < len(toks) + 0 and toks[i].isdigit() and len(toks) - i >= 5:
            q, ans = toks[i], toks[i + 1:i + 5]
            for v, a in zip(versions, ans):
                out[v][q] = a
            i += 5
    return out


if __name__ == "__main__":
    for pdf in sorted(KEYS.glob("final_*.pdf")):
        k = parse(pdf)
        (KEYS / (pdf.stem + ".json")).write_text(json.dumps(k, indent=0), encoding="utf-8")
        print(pdf.stem, {v: len(x) for v, x in k.items()})
