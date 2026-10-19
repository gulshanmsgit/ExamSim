"""P2 · Unit 1 – Fundamentals of Computers · revision NOTES for all seven topics (no new questions).
Owner's request (19 Oct 2026): notes for the remaining KRIES Paper 2 areas. The Unit 1 pack is built by pack_p2_u1.py followed by
fix_u1_balance.py (which reshuffles options), so these notes are added straight into packs/p2-u1-complete.json by
add_u1_notes() below instead of rebuilding the pack."""
import json
from pathlib import Path

NOTES = {
    "Introduction & Functional Components": [{"title": "Computer basics and functional units – revision sheet", "md": """## What a computer is
An electronic device that accepts **input**, **processes** it under the control of a stored program, **stores** data and gives **output** (IPO cycle). Characteristics: speed, accuracy (GIGO – garbage in, garbage out), diligence, versatility, storage, automation; no IQ or feelings.
- Data (raw facts) → processing → information (meaningful); hardware vs software vs firmware; liveware (users)
- **Charles Babbage** – father of the computer (Difference Engine, **Analytical Engine** 1837 – had mill, store, punched-card input); **Ada Lovelace** – first programmer

## Von Neumann (stored-program) architecture
Program and data share one memory; instructions run one after another (fetch–decode–execute); bottleneck = the single bus between CPU and memory. **Harvard** architecture keeps separate instruction and data memories (DSPs, microcontrollers).

## Functional units
| Unit | Job |
|---|---|
| **Input unit** | accepts data, converts it to binary (keyboard, mouse, scanner) |
| **CPU** = ALU + CU (+ registers) | the "brain" |
| **ALU** | arithmetic (+ − × ÷) and logical (AND, OR, NOT, comparisons) operations |
| **Control unit** | fetches and decodes instructions, sends control signals – "central nervous system"; does **not** process data |
| **Memory unit** | primary (RAM/ROM/cache) and secondary storage |
| **Output unit** | converts binary to human form (monitor, printer) |

## Registers
| Register | Holds |
|---|---|
| **PC** (program counter) | address of the **next** instruction |
| **IR** (instruction register) | the instruction being executed |
| **MAR** | memory address to read/write |
| **MDR / MBR** | data read from / to be written to memory |
| Accumulator (AC) | ALU results |
| Status/flag register | carry, zero, sign, overflow flags |
| Stack pointer | top of the stack |

## Instruction cycle
**Fetch** (PC → MAR, memory → MDR → IR, PC + 1) → **decode** (CU) → **execute** (ALU) → (store) → repeat; interrupts are checked after each cycle
- Clock speed in Hz (GHz); MIPS/FLOPS measure performance
- **Buses**: **address bus** (unidirectional, CPU → memory; n lines → 2ⁿ addresses: 32 lines → 4 GB), **data bus** (bidirectional; width = word size), **control bus** (read/write/interrupt signals)

## Units of storage
bit → nibble (4 bits) → **byte (8 bits)** → KB (2¹⁰ = 1024 bytes) → MB (2²⁰) → GB (2³⁰) → TB → PB → EB → ZB → YB
- Word = the unit a CPU processes at once (32/64 bits)

## Traps
- PC holds the address of the **next** instruction, not the current one
- CU directs; ALU computes
- 1 KB = 1024 bytes (binary); disk makers use 1000 (decimal)"""}],

    "Evolution, Generations, Classification, Applications": [{"title": "Evolution, generations and classification – revision sheet", "md": """## Evolution (timeline)
| Device | Who / when | Note |
|---|---|---|
| Abacus | China/Babylon | first counting device |
| Napier's bones | John Napier, 1617 | logarithms, multiplication |
| Slide rule | Oughtred, 1620s | |
| **Pascaline** | Blaise Pascal, 1642 | first mechanical adding machine |
| Stepped reckoner | Leibniz, 1673 | could multiply |
| Jacquard loom | 1801 | **punched cards** |
| Difference / **Analytical Engine** | Charles Babbage, 1822 / 1837 | first general-purpose design |
| Tabulating machine | **Herman Hollerith**, 1890 US census | punched cards → founded the company that became IBM |
| Mark I | Howard Aiken, 1944 | electromechanical |
| **ENIAC** | Eckert & Mauchly, 1946 | first general-purpose electronic digital computer, ~18,000 vacuum tubes |
| EDVAC / EDSAC | von Neumann / Wilkes, 1949 | stored-program (EDSAC first practical) |
| **UNIVAC I** | 1951 | first commercial computer |
- India: **TIFRAC** (first Indian computer, 1960), **PARAM 8000** (first Indian supercomputer, C-DAC 1991, Vijay Bhatkar)

## Generations
| Gen | Years | Technology | Language | Examples |
|---|---|---|---|---|
| 1st | 1940–56 | **vacuum tubes** | machine language | ENIAC, UNIVAC, EDVAC |
| 2nd | 1956–63 | **transistors** (Bell Labs 1947) | assembly, early FORTRAN/COBOL | IBM 1401, IBM 7094 |
| 3rd | 1964–71 | **integrated circuits** (Jack Kilby) | high-level, OS, multiprogramming | IBM 360 |
| 4th | 1971–now | **microprocessors (VLSI)** – Intel 4004 (1971) | C, GUI, networks | PCs |
| 5th | now/future | **AI**, ULSI, parallel processing, quantum | Prolog, natural language | robots, expert systems |

## Classification
- **By data**: analog (continuous – speedometer, thermometer), **digital** (discrete), **hybrid** (both – ICU patient monitor, petrol pump)
- **By size/power**: **supercomputer** (fastest – weather, nuclear; Frontier, El Capitan; India: PARAM, Pratyush, Mihir; measured in FLOPS) > **mainframe** (large organisations, many users – banks, railways; IBM z) > minicomputer (mid-range) > **microcomputer** (PC – desktop, laptop, tablet, smartphone) ; embedded computers inside devices
- **By purpose**: general-purpose vs special-purpose
- Workstation = powerful single-user computer; server = serves clients

## Applications
Education (e-learning, smart classes), banking (ATM, core banking, UPI), railways (PRS), healthcare (CT/MRI, telemedicine), governance (e-governance – Bhoomi, Kaveri, Seva Sindhu in Karnataka), business, science, defence, entertainment, communication, weather forecasting

## Traps
- First **electronic general-purpose** computer = ENIAC; first **commercial** = UNIVAC I
- Transistor (2nd gen) ≠ IC (3rd gen) ≠ microprocessor (4th gen)
- Hollerith (punched-card tabulator), not Babbage, founded the company that became IBM"""}],

    "Input, Output and Memory Devices": [{"title": "Input, output and memory devices – revision sheet", "md": """## Input devices
Keyboard (QWERTY, function keys F1–F12, toggle keys Caps/Num/Scroll Lock), mouse (mechanical, optical; click, drag), trackball, touchpad, **light pen**, joystick (games, CAD), touch screen, **scanner** (flatbed, handheld), digital camera, webcam, microphone, graphics tablet/digitiser
- **MICR** – magnetic ink characters on **cheques** (banks)
- **OCR** – reads printed text into editable text
- **OMR** – detects marks on answer sheets (exams like the KEA's)
- **Barcode reader** (retail, library), **QR code** scanner, RFID reader, biometric (fingerprint, iris – Aadhaar)

## Output devices
- **Monitors**: CRT (old), **LCD**, **LED**, OLED, plasma; resolution (1920 × 1080), pixel, refresh rate (Hz), dot pitch, screen size measured **diagonally**
- **Printers**:
| Impact | Non-impact |
|---|---|
| **Dot-matrix** (carbon copies, noisy; speed in cps), daisy wheel, line printer (lines per minute) | **Laser** (toner, drum, fast, ppm), **inkjet** (ink cartridges, cheap colour), thermal (bills, ATM slips), 3-D printer |
- **Plotter** – large drawings (engineering, maps); projector, speakers, headphones
- Both input and output: touch screen, modem, headset, network card

## Memory hierarchy (fast/costly/small → slow/cheap/large)
**Registers → cache (L1, L2, L3) → main memory (RAM) → secondary (SSD, HDD) → tertiary (tape, optical)**

## Primary memory
| RAM (volatile, read/write) | ROM (non-volatile, read-only) |
|---|---|
| **SRAM** – flip-flops, fast, costly → **cache** | **PROM** – programmed once |
| **DRAM** – capacitors, needs **refreshing**, cheap → main memory (SDRAM, DDR4, DDR5) | **EPROM** – erased by **UV light** |
| | **EEPROM** – erased electrically (byte by byte); **flash** = block-erasable EEPROM |
- BIOS/firmware lives in ROM/flash; cache memory is SRAM between CPU and RAM
- **Virtual memory** = disk space used as extra RAM

## Secondary storage
| Device | Note |
|---|---|
| Hard disk (HDD) | magnetic platters, tracks/sectors/cylinders, rpm (5400/7200), **direct access** |
| **SSD** | flash, no moving parts, fast, costlier |
| Magnetic tape | **sequential access**, backups |
| CD (700 MB), **DVD (4.7 GB single layer)**, **Blu-ray (25 GB)** | optical, laser |
| Pen drive / memory card | flash |
| Cloud storage | online (Google Drive, DigiLocker) |

## Traps
- MICR → cheques; OMR → answer sheets; OCR → text
- DRAM needs refresh, SRAM doesn't
- Cache is faster than RAM; registers are the fastest of all
- Tape is sequential access; disk is direct (random) access"""}],

    "Software Concepts & Problem Solving Methodology": [{"title": "Software concepts and problem solving – revision sheet", "md": """## Software types
| Type | Examples |
|---|---|
| **System software** | operating systems (Windows, Linux, Android), device drivers, language translators (compiler, interpreter, assembler), linker, loader |
| **Utility software** | antivirus, disk cleanup, defragmenter, backup, compression (WinZip), file managers |
| **Application software** | general-purpose (MS Office, browsers) and specific (Tally, railway reservation, payroll) |
- Licensing: proprietary (Windows, MS Office), **open source** (Linux, LibreOffice, Firefox – source available, GPL), freeware (free, closed source), shareware (try before you buy), public domain
- Translators: **compiler** (whole program, faster run), **interpreter** (line by line), **assembler** (assembly → machine)
- Language generations: 1GL machine, 2GL assembly, 3GL high-level (C, Java), 4GL (SQL), 5GL (Prolog)

## Problem-solving steps
1. **Understand / define** the problem (input, output, constraints)
2. **Analyse** – find the method
3. **Design the algorithm** (flowchart / pseudocode)
4. **Code** in a language
5. **Test and debug** (syntax, logical, run-time errors)
6. Document and maintain

## Algorithms
- Properties: **finiteness, definiteness, input (0 or more), output (1 or more), effectiveness**
- Represented as step lists, **pseudocode** (structured English), **flowcharts**, decision tables
- Example – largest of three numbers: read A, B, C; if A > B and A > C print A, else if B > C print B, else print C
- Example – sum of 1 to N: S = 0; for i = 1 to N: S = S + i; print S (or S = N(N + 1)/2)

## Flowchart symbols
| Symbol | Meaning |
|---|---|
| Oval (terminal) | start / stop |
| Parallelogram | input / output |
| **Rectangle** | process (calculation, assignment) |
| **Diamond** | decision (yes/no) |
| Arrow | flow of control |
| Small circle | connector (same page); pentagon – off-page connector |
| Rectangle with double side lines | predefined process (subroutine) |
- Flowcharts are good for small programs, hard to modify for large ones

## Programming constructs (structured programming – Böhm & Jacopini)
**Sequence, selection (decision), iteration (repetition)** – enough for any algorithm; avoid goto
- Top-down design (stepwise refinement), modular programming, bottom-up design

## Errors
Syntax errors (compiler finds them), **logical** errors (wrong output – hardest to find), run-time errors (divide by zero, file not found)

## Traps
- A flowchart decision box is a **diamond**; input/output is a **parallelogram**
- An algorithm must terminate (finiteness)
- Antivirus is utility software, not system software in the strict sense (it is often grouped under system software in Indian textbooks – read the options)"""}],

    "Word Processing, Spreadsheets, PowerPoint": [{"title": "Office tools – Word, Excel, PowerPoint – revision sheet", "md": """## Word processing (MS Word, LibreOffice Writer, Google Docs)
- File extensions: **.docx** (.doc older), .dotx (template), .rtf, .odt; .pdf via Save As
- Shortcuts: **Ctrl+B** bold, **Ctrl+I** italic, **Ctrl+U** underline, Ctrl+E centre, Ctrl+L left, Ctrl+R right, **Ctrl+J** justify, Ctrl+Z undo, **Ctrl+Y** redo, Ctrl+F find, **Ctrl+H** replace, Ctrl+K hyperlink, Ctrl+Enter page break, Ctrl+P print, **F7** spelling & grammar, **Shift+F3** change case, Ctrl+A select all, Ctrl+] / Ctrl+[ font size up/down, F12 Save As
- Features: **mail merge** (main document + data source → personalised letters), styles, headers/footers, page numbers, footnotes/endnotes, table of contents, track changes, macros, watermark, columns, drop cap, word count, thesaurus (Shift+F7)
- Margins, orientation (portrait/landscape), page size (A4 = 21 × 29.7 cm); default MS Word font Calibri 11 (Aptos in newer versions)

## Spreadsheets (MS Excel, LibreOffice Calc, Google Sheets)
- File **.xlsx**; workbook → worksheets → cells (column letter + row number: **B3**); 16,384 columns (A … **XFD**) × **1,048,576 rows** in Excel 2007+
- Formulas start with **=**; references: **relative A1**, **absolute $A$1**, mixed $A1 / A$1 (**F4** cycles them)
- Functions: SUM, AVERAGE, COUNT (numbers), **COUNTA** (non-empty), COUNTIF, MAX, MIN, **IF(cond, yes, no)**, ROUND, **VLOOKUP(value, table, col, FALSE)**, HLOOKUP, XLOOKUP, CONCAT, LEN, TODAY(), NOW(), SUMIF, RANK
- Worked: A1 = 10, A2 = 20, A3 = "x", A4 empty → COUNT(A1:A4) = **2**, COUNTA = **3**, AVERAGE = **15**
- Copying `=A1+$B$1` from C1 to C2 gives `=A2+$B$1`
- Errors: **#DIV/0!**, **#VALUE!** (wrong type), **#REF!** (invalid reference), **#NAME?** (unknown function name), **#N/A** (lookup not found), **####** (column too narrow), #NUM!
- Tools: sort, filter, **conditional formatting**, charts (column, bar, line, pie, scatter), **pivot tables**, data validation, freeze panes, what-if analysis (Goal Seek), protect sheet
- Shortcuts: F2 edit cell, Ctrl+; today's date, Alt+= AutoSum, Ctrl+Shift+L filter, Ctrl+Arrow jump to edge

## Presentations (MS PowerPoint, Impress, Google Slides)
- File **.pptx**; show file .ppsx; template .potx
- **F5** start from the beginning, **Shift+F5** from the current slide, Esc end, Ctrl+M new slide, B/W black/white screen during a show
- Views: **Normal**, Outline, **Slide Sorter** (rearrange), Notes Page, Reading view, Slide Show; **Slide Master** controls the look of all slides
- **Transitions** = effects between slides; **animations** = effects on objects within a slide (entrance, emphasis, exit, motion paths)
- Layouts, themes, design ideas, SmartArt, speaker notes, rehearse timings, hyperlinks and action buttons, insert audio/video, export as PDF/video

## Traps
- Transition (between slides) vs animation (objects on a slide)
- $A$1 stays fixed when copied; A1 changes
- COUNT counts numbers only; COUNTA counts anything non-empty
- F7 = spelling in Word; F5 = slide show in PowerPoint (and Go To in Word)"""}],

    "Computer Configuration & Motherboard": [{"title": "Configuration and motherboard – revision sheet", "md": """## Reading a configuration
"Intel Core i5-13400, 2.5 GHz, 16 GB DDR5 RAM, 512 GB NVMe SSD, 24-inch FHD monitor, Windows 11"
- Processor: maker/family/generation, **clock speed (GHz)**, cores/threads, cache (L2/L3 MB)
- RAM: size (GB), type (DDR4/DDR5), speed (MHz/MT/s)
- Storage: HDD (rpm) or SSD (SATA or NVMe), capacity
- Graphics (integrated or dedicated GPU, VRAM), display (size, resolution), ports (USB, HDMI), network (Wi-Fi, Ethernet), OS
- 64-bit OS needed to use more than 4 GB RAM

## Motherboard
The main circuit board (system board, mainboard) that connects all components.
- **Form factors**: AT (old), **ATX** (standard, 12 × 9.6 in), Micro-ATX, Mini-ITX (small), BTX
- Types by integration: integrated (on-board sound, graphics, LAN) vs non-integrated

## Components on the motherboard
| Component | Purpose |
|---|---|
| **CPU socket** | holds the processor (Intel LGA, AMD AM5) |
| **Chipset** | traffic controller: **northbridge** (CPU–RAM–graphics, now inside the CPU) and **southbridge** (I/O, USB, SATA) – today one PCH |
| **RAM slots (DIMM)** | memory modules (SO-DIMM in laptops) |
| **Expansion slots** | **PCIe** (x1, x16 for graphics), older **PCI**, **AGP** (old graphics) |
| **SATA** ports | hard disks, SSDs, optical drives (older IDE/PATA ribbon cables) |
| **M.2** slot | NVMe SSDs, Wi-Fi cards |
| **BIOS/UEFI** chip | firmware, POST, boot settings |
| **CMOS** battery (CR2032) | keeps the clock and BIOS settings when power is off |
| Power connectors | 24-pin ATX, 4/8-pin CPU |
| I/O panel / back ports | USB, HDMI, DisplayPort, audio jacks, Ethernet (RJ-45), PS/2 (old) |
| Jumpers, front-panel headers, fan headers, VRM, clock generator | |

## Ports and connectors
USB (1.1, 2.0 480 Mbps, 3.x, **Type-C**), HDMI (audio + video), VGA (analog video, 15-pin), DVI, DisplayPort, Ethernet RJ-45, audio 3.5 mm, serial (COM, 9-pin) and parallel (LPT, 25-pin – old printers), Thunderbolt

## Booting basics
Power on → SMPS gives **Power Good** signal → BIOS/UEFI runs **POST** (beep codes on errors) → finds a boot device (boot order) → loads the OS boot loader

## Traps
- CMOS battery dead → date/time and BIOS settings reset
- PCIe x16 is for graphics cards; AGP is obsolete
- The chipset, not the CPU socket, manages I/O traffic
- HDMI carries audio and video; VGA carries analog video only"""}],

    "Memory, Power Supply & Assembling": [{"title": "Memory, power supply and assembling – revision sheet", "md": """## Memory modules
- **SIMM** (old, 32-bit) → **DIMM** (64-bit, desktops) → **SO-DIMM** (laptops); RIMM (Rambus, old)
- SDRAM → **DDR** (data on both clock edges) → DDR2 → DDR3 → **DDR4** → **DDR5**; each has a different notch – not interchangeable
- Dual/quad channel: install matched modules in paired slots for more bandwidth
- ECC memory (servers) corrects single-bit errors; parity memory detects
- Cache: L1 (inside each core, smallest/fastest), L2, L3 (shared)
- Memory speed in MHz / MT/s; latency CL; capacity per module 4 – 64 GB

## Power supply
- **SMPS** (Switch Mode Power Supply) converts **AC mains (230 V in India) to low DC**: **+3.3 V, +5 V, +12 V** (also −12 V); rated in **watts** (450 W, 650 W); efficiency ratings **80 PLUS** (Bronze, Gold, Platinum)
- Connectors: **24-pin ATX** main, 4/8-pin EPS (CPU), PCIe 6/8-pin (graphics), **SATA power** (15-pin), Molex (4-pin, older drives)
- Power Good signal tells the motherboard the voltages are stable
- **UPS** keeps the computer running on battery during a power cut: **offline/standby**, **line-interactive**, **online** (double conversion – best, continuous); rated in **VA**
- Surge protector / spike buster, voltage stabiliser (AVR); proper earthing
- Power problems: surge/spike, sag/brownout, blackout, noise

## Assembling a computer – order of steps
1. Prepare an anti-static workspace (**wrist strap**, ESD mat); gather tools (screwdriver, thermal paste)
2. Install the **CPU** in the socket (match the triangle/notch, no force), apply **thermal paste**, fix the **heat sink and fan**
3. Insert **RAM** modules (align the notch, press until the clips lock)
4. Fit the **motherboard** in the cabinet on standoffs with the I/O shield
5. Mount the **SMPS**; connect the 24-pin and CPU power connectors
6. Install storage (SSD/HDD/M.2) and connect SATA data + power cables
7. Insert expansion cards (graphics card in PCIe x16)
8. Connect front-panel connectors (power switch, reset, LEDs, USB, audio) and fans
9. Check cables, close the case, connect monitor, keyboard, mouse, power
10. Power on → enter **BIOS/UEFI** (Del/F2) → check detection, set boot order → install the OS → install **drivers** → updates, antivirus

## Troubleshooting basics
- No power: check cable, switch, SMPS; beeps during POST point to RAM/graphics faults; overheating → clean fans, reapply thermal paste
- Preventive maintenance: dust cleaning, cable management, disk cleanup, updates, backups

## Traps
- SMPS output is DC; mains input is AC
- UPS capacity in VA; SMPS capacity in watts
- Thermal paste goes between the CPU and the heat sink
- Always discharge static before touching components"""}],
}


def add_u1_notes():
    """Put the notes into packs/p2-u1-complete.json without touching the questions (re-run safe: replaces these titles)."""
    path = Path(__file__).resolve().parent.parent / "packs" / "p2-u1-complete.json"
    raw = path.read_text(encoding="utf-8")
    pack = json.loads(raw)
    for t in pack["subjects"][0]["topics"]:
        if t["name"] in NOTES:
            mine = {n["title"] for n in NOTES[t["name"]]}
            t["notes"] = [n for n in t.get("notes", []) if n["title"] not in mine] + NOTES[t["name"]]
    path.write_text(json.dumps(pack, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")


if __name__ == "__main__":
    add_u1_notes()
