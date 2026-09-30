"""Make print files of the previous-year papers in Desktop\\pyq: two pages per side, in reading order.

Each A4 landscape page holds two original pages side by side: sheet 1 front = pages 1-2, back = pages 3-4, and so on.
Every question paper is padded with blank pages to a multiple of 4, so the next paper always starts on the front of a new
sheet and the papers can be separated after printing. Print double-sided (manual duplex on the HP M126nw).
Output: Desktop\\pyq\\Print (2 pages per side)\\<subject> - print.pdf, plus <subject> - contents.txt (sheet ranges per paper)
Usage: python tools/pyq_booklet.py
"""
import os
import shutil
from pathlib import Path
import pymupdf

ROOT = Path(os.path.expanduser("~")) / "Desktop" / "pyq"
OUT = ROOT / "Print (2 pages per side)"
SUBJECTS = ["Computer Science", "General Knowledge"]
W, H = pymupdf.paper_size("a4-l")  # 842 x 595 pt
LEFT, RIGHT = pymupdf.Rect(8, 8, W / 2 - 8, H - 8), pymupdf.Rect(W / 2 + 8, 8, W - 8, H - 8)


def add_two_up(out, src: Path):
    doc = pymupdf.open(src)
    n = doc.page_count
    padded = (n + 3) // 4 * 4
    for p in range(0, padded, 2):
        page = out.new_page(width=W, height=H)
        for num, rect in ((p, LEFT), (p + 1, RIGHT)):
            if num < n:
                page.show_pdf_page(rect, doc, num)
    return n, padded // 4


def main():
    for old in (ROOT / "Booklets (print)", OUT):
        if old.exists():
            shutil.rmtree(old)
    OUT.mkdir(parents=True)
    for subject in SUBJECTS:
        out, sheets, rows = pymupdf.open(), 0, []
        for src in sorted((ROOT / subject).glob("*.pdf")):
            n, s = add_two_up(out, src)
            rows.append(f"sheets {sheets + 1}-{sheets + s}: {src.stem} ({n} pages)")
            sheets += s
        out.save(OUT / f"{subject} - print.pdf", garbage=3, deflate=True)
        (OUT / f"{subject} - contents.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")
        if subject == SUBJECTS[0]:
            test = pymupdf.open()
            test.insert_pdf(out, from_page=0, to_page=3)
            test.save(OUT / "TEST PRINT - 2 sheets.pdf")
        print(f"{subject}: {len(rows)} papers, {sheets} sheets", flush=True)


if __name__ == "__main__":
    main()
