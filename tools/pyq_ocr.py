"""OCR the scanned previous-year papers in sources/pyq/*.pdf (KEA publishes image-only PDFs).

For each paper writes
  sources/pyq/ocr/<paper>.txt   – OCR text, one line per text row, with '=== page N ===' markers (a first draft only:
                                  symbols such as overbars, ¬, ↔ and roman numerals need checking against the page image)
  sources/pyq/img/<paper>/pNN.png – page images (110 dpi) for visual checking while transcribing.
Usage: python tools/pyq_ocr.py [paper-stem ...]    (default: every PDF not yet OCR'd)
Needs: pip install pymupdf rapidocr_onnxruntime"""
import sys
from pathlib import Path
import pymupdf
from rapidocr_onnxruntime import RapidOCR

SRC = Path(__file__).resolve().parent.parent / "sources" / "pyq"


def rows(result):
    """Group OCR boxes into text rows (top-to-bottom, left-to-right)."""
    items = sorted(((b[0][1], b[0][0], t) for b, t, _ in result or []), key=lambda x: (x[0], x[1]))
    out, cur, y0 = [], [], None
    for y, x, t in items:
        if y0 is not None and y - y0 > 18:
            out.append("   ".join(s for _, s in sorted(cur)))
            cur = []
        if not cur:
            y0 = y
        cur.append((x, t))
    if cur:
        out.append("   ".join(s for _, s in sorted(cur)))
    return out


def main():
    stems = sys.argv[1:] or [p.stem for p in sorted(SRC.glob("*.pdf")) if not (SRC / "ocr" / f"{p.stem}.txt").exists()]
    ocr = RapidOCR()
    (SRC / "ocr").mkdir(exist_ok=True)
    for stem in stems:
        doc = pymupdf.open(SRC / f"{stem}.pdf")
        img_dir = SRC / "img" / stem
        img_dir.mkdir(parents=True, exist_ok=True)
        lines = []
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=110).save(img_dir / f"p{i:02d}.png")
            tmp = img_dir / "_ocr.png"
            page.get_pixmap(dpi=200).save(tmp)
            res, _ = ocr(str(tmp))
            lines.append(f"=== page {i} ===")
            lines.extend(rows(res))
        (img_dir / "_ocr.png").unlink(missing_ok=True)
        (SRC / "ocr" / f"{stem}.txt").write_text("\n".join(lines), encoding="utf-8")
        print(f"{stem}: {doc.page_count} pages", flush=True)


if __name__ == "__main__":
    main()
