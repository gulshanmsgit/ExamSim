"""One-off edit: vary the answers of assertion–reason and I/II statement questions in Unit 1
(previously almost all were A / 'Only I'). Replaces whole question tuples in the source files."""
import re
from pathlib import Path

HERE = Path(__file__).parent
# (file, prefix of existing question source text, new question source text, new answer index, new explanation)
CHANGES = [
    ("p2u1_a.py", r"Assertion (A): A computer can produce wrong results even when its hardware works perfectly.",
     r"Assertion (A): A computer can produce wrong results even when its hardware works perfectly.\nReason (R): Computers can work continuously for long hours without fatigue.", 1,
     "Both statements are true, but diligence does not explain wrong results; the real reason is GIGO (wrong input or program)."),
    ("p2u1_a.py", r"Assertion (A): Punched cards played an important role in early data processing.",
     r"Assertion (A): Punched cards played an important role in early data processing.\nReason (R): Charles Babbage introduced punched cards for processing the 1890 US census.", 2,
     "A is true. R is false: Herman Hollerith used punched cards for the 1890 census (Jacquard had used them for looms in 1804)."),
    ("p2u1_a.py", r"Assertion (A): Supercomputers are used for weather forecasting.",
     r"Assertion (A): Analog computers are generally more accurate than digital computers.\nReason (R): Digital computers process data in discrete (binary) form.", 3,
     "A is false: digital computers are more accurate, since analog results depend on the precision of physical measurements. R is true."),
    ("p2u1_a.py", r"Assertion (A): Computers are widely used in banks.",
     r"Assertion (A): Computers are widely used in banks.\nReason (R): MICR characters on cheques are printed with magnetic ink.", 1,
     "Both are true, but R does not explain A; banks use computers because they must process huge numbers of transactions quickly and accurately."),
    ("p2u1_a.py", r"Consider the statements:\nI. A computer can work only on the instructions given to it.",
     r"Consider the statements:\nI. A computer can take decisions without being given any program.\nII. A computer never needs input data to produce useful output.\nWhich is/are correct?", 3,
     "Both are false: a computer follows programs and needs input data to process."),
    ("p2u1_a.py", r"Consider the statements:\nI. Ada Lovelace worked on programs for Babbage's Analytical Engine.",
     r"Consider the statements:\nI. The Analytical Engine was fully built and used during Babbage's lifetime.\nII. Ada Lovelace wrote an algorithm intended for the Analytical Engine.\nWhich is/are correct?", 1,
     "The Analytical Engine was never completed in Babbage's lifetime; Lovelace's notes (1843) contain an algorithm for computing Bernoulli numbers."),
    ("p2u1_a.py", r"Consider the statements:\nI. Transistor-based computers consumed less power than vacuum-tube computers.",
     r"Consider the statements:\nI. Transistor-based computers consumed less power than vacuum-tube computers.\nII. Third-generation computers used integrated circuits.\nWhich is/are correct?", 2,
     "Both are correct."),
    ("p2u1_b.py", r"Assertion (A): Hard disks are used as secondary storage rather than main memory.",
     r"Assertion (A): Hard disks are used as secondary storage rather than main memory.\nReason (R): Hard disks are volatile and lose data when power is switched off.", 2,
     "A is true, but R is false: hard disks are non-volatile. They are secondary storage because they are much slower than RAM."),
    ("p2u1_b.py", r"Assertion (A): Testing a program with sample inputs whose outputs are known helps detect logical errors.",
     r"Assertion (A): Logical errors are always detected and reported by the compiler.\nReason (R): Syntax errors are detected during compilation.", 3,
     "A is false: logical errors produce wrong results without error messages. R is true."),
    ("p2u1_b.py", r"Consider the statements:\nI. DRAM is denser and cheaper than SRAM.",
     r"Consider the statements:\nI. SRAM needs to be refreshed periodically.\nII. DRAM is denser and cheaper per bit than SRAM.\nWhich is/are correct?", 1,
     "DRAM needs refreshing; SRAM does not. Statement II is correct."),
    ("p2u1_c.py", r"Assertion (A): A formula using $B$1 keeps referring to B1 when copied anywhere.",
     r"Assertion (A): A formula using $B$1 keeps referring to B1 when copied anywhere.\nReason (R): The dollar sign makes a cell reference relative.", 2,
     "A is true, but R is false: the dollar sign makes the column/row absolute."),
    ("p2u1_c.py", r"Assertion (A): Changing the font in the Slide Master changes it on all slides using that master.",
     r"Assertion (A): Changing the font in the Slide Master changes it on all slides using that master.\nReason (R): PowerPoint presentations are saved with the .pptx extension by default.", 1,
     "Both are true, but R is unrelated; the real reason is that slide layouts inherit formatting from the Slide Master."),
    ("p2u1_c.py", r"Consider the statements:\nI. A document can have different headers in different sections.",
     r"Consider the statements:\nI. In MS Word, footnotes appear at the end of the whole document.\nII. A Word document can have only one page orientation.\nWhich is/are correct?", 3,
     "Both are false: footnotes appear at the bottom of the page (endnotes at the end), and section breaks allow mixed orientations."),
    ("p2u1_d.py", r"Assertion (A): Choosing the right motherboard is important when building a PC.",
     r"Assertion (A): Any Intel desktop processor fits any motherboard that has an LGA socket.\nReason (R): The socket type and chipset determine which processors a motherboard supports.", 3,
     "A is false: LGA sockets differ (e.g. LGA1200 and LGA1700 are incompatible). R is true."),
    ("p2u1_d.py", r"Assertion (A): SRAM is used for cache memory.",
     r"Assertion (A): SRAM is used for cache memory.\nReason (R): SRAM is cheaper and denser than DRAM.", 2,
     "A is true, but R is false: SRAM is costlier and less dense. It is used for cache because it is faster and needs no refresh."),
    ("p2u1_d.py", r"Assertion (A): Installing the CPU and RAM before fixing the motherboard in the case is recommended.",
     r"Assertion (A): Installing the CPU and RAM before fixing the motherboard in the case is recommended.\nReason (R): Motherboards are made as multi-layer printed circuit boards.", 1,
     "Both are true, but R does not explain A; the reason is that an open board gives more working space and less risk of damage."),
    ("p2u1_d.py", r"Consider the statements:\nI. ATX motherboards have I/O ports built onto the rear edge, covered by an I/O shield.",
     r"Consider the statements:\nI. AT motherboards supported soft power control through a PS_ON signal.\nII. ATX motherboards have I/O ports built onto the rear edge, covered by an I/O shield.\nWhich is/are correct?", 1,
     "Soft power control was introduced with ATX; statement II is correct."),
    ("p2u1_d.py", r"Consider the statements:\nI. A UPS provides backup power during outages.",
     r"Consider the statements:\nI. A voltage stabiliser provides backup power during outages.\nII. A surge protector provides backup power during outages.\nWhich is/are correct?", 3,
     "Neither provides backup power; only a UPS (with a battery) does."),
]

files = {}
for fn, prefix, newq, ans, expl in CHANGES:
    s = files.get(fn) or (HERE / fn).read_text(encoding="utf-8")
    pat = re.compile(r'\("' + re.escape(prefix) + r'[^"]*",\s*\n\s*(AR|I_II), \d, "[^"]*"\),')
    found = list(pat.finditer(s))
    assert len(found) == 1, (fn, prefix, len(found))
    m = found[0]
    s = s[:m.start()] + f'("{newq}",\n     {m.group(1)}, {ans}, "{expl}"),' + s[m.end():]
    files[fn] = s
for fn, s in files.items():
    (HERE / fn).write_text(s, encoding="utf-8")
print("updated", len(CHANGES), "questions in", len(files), "files")
