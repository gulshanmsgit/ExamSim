"""Make print-ready booklet PDFs (saddle-stitch) of every paper in Desktop\\pyq.

Each A4 landscape page holds two original pages side by side, ordered so that when the output is printed double-sided
(flip on SHORT edge), stacked and folded in the middle, the pages read 1, 2, 3 … in order. One printed sheet = 4 pages.
Blank pages pad the paper to a multiple of 4. Output: Desktop\\pyq\\Booklets (print)\\<subject>\\<paper> - booklet.pdf
Usage: python tools/pyq_booklet.py
"""
import os
from pathlib import Path
import pymupdf

ROOT = Path(os.path.expanduser("~")) / "Desktop" / "pyq"
OUT = ROOT / "Booklets (print)"
W, H = pymupdf.paper_size("a4-l")  # 842 x 595 pt


def booklet(src: Path, dst: Path):
    doc = pymupdf.open(src)
    n = doc.page_count
    total = (n + 3) // 4 * 4
    out = pymupdf.open()
    left, right = pymupdf.Rect(0, 0, W / 2, H), pymupdf.Rect(W / 2, 0, W, H)
    for s in range(total // 4):
        # 1-based page numbers on each side of sheet s
        for l, r in ((total - 2 * s, 2 * s + 1), (2 * s + 2, total - 2 * s - 1)):
            page = out.new_page(width=W, height=H)
            for num, rect in ((l, left), (r, right)):
                if num <= n:
                    page.show_pdf_page(rect + (8, 8, -8, -8), doc, num - 1)  # 8 pt margin, aspect kept
    dst.parent.mkdir(parents=True, exist_ok=True)
    out.save(dst, garbage=3, deflate=True)
    return n, total // 4


def main():
    """One print file per subject: each paper is its own booklet (fold and staple separately), papers in year order."""
    import shutil, tempfile
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    tmp = Path(tempfile.mkdtemp())
    for subject in sorted(p for p in ROOT.iterdir() if p.is_dir() and p != OUT and "Answer Keys" not in p.name):
        merged, sheets, rows = pymupdf.open(), 0, []
        for src in sorted(subject.glob("*.pdf")):
            part = tmp / f"{src.stem}.pdf"
            n, s = booklet(src, part)
            start = sheets + 1
            merged.insert_pdf(pymupdf.open(part))
            sheets += s
            rows.append(f"   sheets {start}-{sheets}: {src.stem} ({n} pages)")
        merged.save(OUT / f"{subject.name} - booklets.pdf", garbage=3, deflate=True)
        (OUT / f"{subject.name} - contents.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")
        print(f"{subject.name}: {len(rows)} papers, {sheets} sheets", flush=True)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
