"""Download the previous-year papers listed in tools/pyq_manifest.tsv into sources/pyq/ (git-ignored).

The manifest records every paper's group (p1/p2), year, exam, paper and KEA URL. Local file name = local_name(row).
Files already present are skipped. Usage: python tools/pyq_fetch.py
"""
import csv, re, sys, time, urllib.request
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
DEST = TOOLS.parent / "sources" / "pyq"
# the first 12 papers were downloaded under short names before the manifest existed
LEGACY = {"QP_26_08_2026_GFGC_2021_2022_COMPUTER_SCIENCE_01092026": "gfgc2021_cs",
          "K_SET_2023_05_07_26_CS&A_13072026": "kset2023_csa",
          "COMPUTER_SCIENCE_&_APPLICATION": "kset2024_csa",
          "K_SET_2025_05_07_26_COMP_SCIE_&_APL_13072026": "kset2025_csa",
          "COMPETITIVE_EXAM__04_05_JULY_26_P2_CS_RPC_05_07_26_13072026": "kea2026_cs_p2",
          "CS": "gttc2024_lecturer_cs",
          "jr_prg_n_sr_prg_paper2": "klc2024_programmer_p2",
          "RU_COMPUTER_SCIENCE_&_APPLICATION": "ru2024_asstprof_csa",
          "NHK_GK_P1_11_01_26_18062026": "kea2026_gk_nhk_1101",
          "HK_GK_GROUP_C_22_02_26_18062026": "kea2026_gk_hk_2202",
          "NHK_KEC_P2_25_01_26_18062026": "kea2026_kec_nhk_2501",
          "K_SET_2025_05_07_26_GN_SDU_13072026": "kset2025_general"}


def rows():
    with open(TOOLS / "pyq_manifest.tsv", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def local_name(r):
    base = r["url"].rsplit("/", 1)[-1].removesuffix("kannada.pdf").removesuffix(".pdf")
    if base in LEGACY:
        return LEGACY[base]
    return f"{r['group']}_{r['year']}_" + re.sub(r"[^a-z0-9]+", "_", base.lower()).strip("_")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    got = 0
    for r in rows():
        out = DEST / f"{local_name(r)}.pdf"
        if out.exists():
            continue
        url = r["url"].replace("&", "%26")
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url, timeout=120) as resp:
                    out.write_bytes(resp.read())
                print(f"ok  {out.name}  {out.stat().st_size / 1048576:.1f} MB", flush=True)
                got += 1
                break
            except Exception as e:  # network hiccups: retry, then report
                if attempt == 2:
                    print(f"FAIL {out.name}: {e}", flush=True)
                time.sleep(3)
    print(f"{got} downloaded")


if __name__ == "__main__":
    sys.exit(main())
