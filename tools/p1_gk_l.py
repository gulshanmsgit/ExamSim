"""Paper 1 · General Knowledge · P1-GK-18 Basics of Computers (2 sub-topics × 20), with detailed notes (NOTES).
Coverage (planner): basic computer knowledge.
References: NCERT/DSERT ICT texts; P. K. Sinha, Computer Fundamentals; TIFR and C-DAC history pages. REAL previous-year questions come
from the KEA 2025–26 Kannada-English-Computer papers, the GTTC 2024 KEC paper, VAO 2024 Paper 2, PGCET 2023 MCA and the Legislative
Council 2024 Data Entry Operator Paper 2 (no key matching the booklets; answers worked out by ExamSim and marked so). The Computer
Literacy subject (P1-CL) covers each unit in depth; this topic is the GK-paper view."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA GK / computer awareness). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

HISTORY_HW = [
    ("Expand ENIAC",
     ["Electronic Numerical Integrator and Computer", "Electrical Numerical Integrator and Computer", "Electrical Numbered Integrator and Computer", "Electronic Numerical Integrator and Concepts."], 0,
     "ENIAC (1946, University of Pennsylvania) was the first general-purpose electronic digital computer, built with about 18,000 vacuum tubes." + NOTE,
     "Legislative Council 2024 Data Entry Operator P2 · Q80"),
    ("Expand EDVAC :",
     ["Electronic Discrete Variable Automatic Computer", "Electronic Discrete Volatile Automatic Computer", "Electronic Duplex Variable Automatic Computer", "Electronic Duplex Volatile Arithmetic Computer"], 0,
     "EDVAC used von Neumann's stored-program idea." + NOTE, "VAO 2024 Paper-2 · Q74"),
    ("TIFRAC stands for",
     ["Tata Institute of Fundamental Research Advanced Computer", "Tata Institute of Fundamental Research Advanced Calculator",
      "Tata Institute of Fundamental Research Automatic Computer", "Tata Institute of Fundamental Research Automatic Calculator"], 3,
     "TIFRAC (commissioned 1960, Mumbai) was India's first indigenously built electronic digital computer." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q97"),
    ("SMPS stands for",
     ["Switched Mode Power Supply", "Simple Mode Power Supply", "Switched Mode Power Source", "Storage Mode Power Supply"], 0,
     "The SMPS converts mains AC to the low DC voltages a computer needs." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q75"),
    ("Expand RAID related to disk organization technique.",
     ["Related Array of Independent Disks", "Redundant Array of Independent Disks", "Removable Array of Independent Disks", "Remote Array of Independent Disks"], 1,
     "RAID combines several disks for speed (RAID 0) or safety (RAID 1 mirroring, RAID 5 parity)." + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q89"),
    ("MSD stands for :",
     ["Many Significant Digit", "More Significant Digit", "Most Significant Digit", "Multi Significant Digit"], 2,
     "The MSD is the left-most digit, with the highest place value; LSD is the right-most." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q95"),
    ("Expand FLOPS",
     ["Filtering Point Operations Per Second", "Floating Point Operations Per Second", "Flex Point Operations Per Second", "Floating Point Operations Per System"], 1,
     "FLOPS measure the speed of supercomputers (e.g. India's PARAM series by C-DAC)." + NOTE, "KEA 2026 KEC (NHK, 11 Jan 2026) · Q91"),
    ("Truth table is a way of expressing which of the following functions?",
     ["Boolean functions", "Prime functions", "Illogical functions", "Trigonometric functions"], 0,
     "A truth table lists the output of a Boolean (logic) function for every combination of inputs." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q83"),
    ("Charles Babbage, called the 'father of the computer', designed the:",
     ["Analytical Engine", "ENIAC", "Abacus", "Pascaline"], 0, PYQ + "Ada Lovelace wrote the first algorithm for it and is called the first programmer."),
    ("First-generation computers used:",
     ["Vacuum tubes", "Transistors", "Integrated circuits", "Microprocessors"], 0, "2nd – transistors; 3rd – ICs; 4th – microprocessors (VLSI); 5th – AI."),
    ("The 'brain' of the computer is the:",
     ["CPU (Central Processing Unit)", "Monitor", "Keyboard", "Printer"], 0, PYQ + "It contains the ALU, the control unit and registers."),
    ("Which of the following is volatile memory?",
     ["RAM", "ROM", "Hard disk", "Pen drive"], 0, "RAM loses its contents when the power is switched off."),
    ("1 kilobyte (KB) is equal to:",
     ["1024 bytes", "1000 bits", "100 bytes", "8 bytes"], 0, PYQ + "1 byte = 8 bits; 1 MB = 1024 KB; 1 GB = 1024 MB."),
    ("Which of the following is an input device?",
     ["Scanner", "Printer", "Monitor", "Speaker"], 0, "Keyboard, mouse, microphone and webcam are also input devices."),
    ("India's first supercomputer, PARAM 8000 (1991), was developed by:",
     ["C-DAC, Pune", "ISRO", "IIT Bombay", "Infosys"], 0, PYQ + "Vijay Bhatkar led the project."),
    ("The binary number system uses the digits:",
     ["0 and 1", "0 to 7", "0 to 9", "0 to 9 and A to F"], 0, "Octal uses 0–7; hexadecimal uses 0–9 and A–F."),
    ("Consider the statements:\nI. ROM is non-volatile memory.\nII. Cache memory is slower than the hard disk.",
     I_II, 0, "Cache is the fastest memory after registers."),
    ("Assertion (A): Fourth-generation computers are smaller and faster than first-generation computers.\nReason (R): Fourth-generation computers use microprocessors built with VLSI technology.",
     AR, 0, "The Intel 4004 (1971) was the first microprocessor."),
    ("Match:\na. Vacuum tubes  b. Transistors  c. Integrated circuits  d. Microprocessors\n1. First generation  2. Second generation  3. Third generation  4. Fourth generation",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Generations of computers."),
    ("The decimal number 10 written in binary is:",
     ["1010", "1100", "1001", "0110"], 0, "8 + 2 = 10."),
]

SOFTWARE_NET = [
    ("Which of the following is the full form of DDL?",
     ["Detailed Data Language", "Dynamic Data Language", "Data Derivation Language", "Data Definition Language"], 3,
     "DDL commands (CREATE, ALTER, DROP) define database structures; DML commands (INSERT, UPDATE) change the data." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q75"),
    ("ISDN stands for",
     ["Infrastructure Services Digital Network", "Integrated Services Digital Network", "Internal Signal Digital Network", "Integrated Signal Digital Network"], 1,
     "ISDN carries voice and data digitally over telephone lines." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q97"),
    ("What does the acronym ISP stand for ?",
     ["Internet Service Provider", "Internal Service Provider", "Internet Service Providing", "Internet Service Provision"], 0,
     "BSNL, Airtel and Jio are ISPs." + NOTE, "PGCET 2023 MCA · Q27"),
    ("The Primary functions of utility software is/are:\n(a) Disk cleanup.\n(b) System restore and disk compression.\n(c) Protection from virus.\n(d) Managing Database.",
     ["a and b only", "c only", "a, b and c only", "a, b, c and d"], 2,
     "Utility programs maintain and protect the system; managing a database is the job of a DBMS (application software)." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q74"),
    ("State whether the following statements are True or False with respect to MS Word features:\na. Using Hyperlinks is allowed in MS Word.\nb. Digital signature is allowed in MS Word.",
     ["a true, b true", "a true, b false", "a false, b true", "a false, b false"], 0,
     "Word supports hyperlinks (Insert → Link) and digital signatures (File → Info → Protect Document)." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q84"),
    ("Select the correct statement/statements :\na. Microsoft Edge, Safari, Adobe Flash, Google Chrome are examples of browsers.\nb. Mbps stands for Mega bytes per second and MBps stands for Mega bits per second.\nc. 2 GB = 1024 MB\nd. Ubuntu, Red Hat Enterprise Linux, and Windows XP are examples of Operating Systems.",
     ["a only", "b and d only", "a and c only", "d only"], 3,
     "Adobe Flash is a plug-in, not a browser; Mbps = megabits and MBps = megabytes; 2 GB = 2048 MB; only d is correct." + NOTE, "VAO 2024 Paper-2 · Q89"),
    ("An operating system is:",
     ["System software that manages hardware and provides services to programs", "An application for typing letters", "A computer virus", "An input device"], 0, PYQ + "Windows, Linux, macOS and Android are operating systems."),
    ("Which of the following is application software?",
     ["MS Excel", "Windows 11", "BIOS", "Device driver"], 0, "System software runs the computer; application software does user tasks."),
    ("Open-source software is software whose:",
     ["Source code is freely available to view, modify and share", "Code is secret", "Use is illegal", "Licence must always be bought"], 0, PYQ + "Linux, LibreOffice and Firefox are open source."),
    ("The World Wide Web (WWW) was invented in 1989 by:",
     ["Tim Berners-Lee", "Bill Gates", "Vint Cerf", "Steve Jobs"], 0, "Vint Cerf and Bob Kahn designed TCP/IP – the 'fathers of the internet'."),
    ("HTTP stands for:",
     ["HyperText Transfer Protocol", "High Transfer Text Protocol", "HyperText Transmission Program", "Home Text Transfer Protocol"], 0, PYQ + "HTTPS is the secure version."),
    ("A URL is:",
     ["The address of a resource on the internet", "A type of virus", "A programming language", "An input device"], 0, "URL = Uniform Resource Locator."),
    ("Which of the following is a search engine?",
     ["Google", "Windows", "MS Word", "Linux"], 0, PYQ + "Bing and DuckDuckGo are also search engines."),
    ("The shortcut key to copy selected text in Windows is:",
     ["Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + Z"], 0, "Ctrl + V – paste; Ctrl + X – cut; Ctrl + Z – undo."),
    ("E-mail attachments are files that are:",
     ["Sent along with an e-mail message", "Deleted automatically", "Only images", "Only printed"], 0, PYQ + "Never open attachments from unknown senders."),
    ("A LAN is a network that covers:",
     ["A small area such as a building or campus", "A whole country", "The whole world", "Only satellites"], 0, "MAN – city; WAN – country or world (the internet is the largest WAN)."),
    ("Consider the statements:\nI. A web browser is used to view web pages.\nII. A search engine and a web browser are the same thing.",
     I_II, 0, "Chrome is a browser; Google Search is a search engine."),
    ("Assertion (A): Antivirus software is utility software.\nReason (R): Utility software helps maintain, protect and optimise the computer.",
     AR, 0, "Disk cleanup and backup tools are other utilities."),
    ("Match:\na. Ctrl + C  b. Ctrl + V  c. Ctrl + Z  d. Ctrl + S\n1. Copy  2. Paste  3. Undo  4. Save",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Shortcut keys."),
    ("The extension '.xlsx' belongs to files created in:",
     ["MS Excel", "MS Word", "MS PowerPoint", "Notepad"], 0, ".docx – Word; .pptx – PowerPoint; .txt – Notepad."),
]

TOPICS = {
    "Basics of Computers": [("1 · History, Generations, Hardware and Number Systems", HISTORY_HW),
                            ("2 · Software, Internet and Common Computer Abbreviations", SOFTWARE_NET)],
}

NOTES = {
    "Basics of Computers": [{"title": "Basics of computers – detailed notes", "md": """# Basics of computers

## History
| Year | Event |
|---|---|
| 1830s | **Charles Babbage** – Analytical Engine ("father of the computer"); **Ada Lovelace** – first programmer |
| 1946 | **ENIAC** – Electronic Numerical Integrator and Computer (vacuum tubes) |
| 1949 | **EDVAC** – Electronic Discrete Variable Automatic Computer (stored program, von Neumann) |
| 1960 | **TIFRAC** – TIFR **Automatic Calculator**, India's first indigenous computer |
| 1971 | Intel 4004 – first microprocessor |
| 1989 | **Tim Berners-Lee** – World Wide Web |
| 1991 | **PARAM 8000** – India's first supercomputer, C-DAC Pune (Vijay Bhatkar) |

**Generations:** 1 vacuum tubes · 2 transistors · 3 ICs · 4 microprocessors (VLSI) · 5 AI.

## Hardware
- **CPU** = ALU + Control Unit + registers. Speed in GHz; supercomputers in **FLOPS** (Floating Point Operations Per Second).
- Memory: registers → cache → **RAM (volatile)** → ROM (non-volatile) → secondary storage (HDD, SSD, pen drive).
- **SMPS** – Switched Mode Power Supply. **RAID** – Redundant Array of Independent Disks. **UPS** – Uninterruptible Power Supply.
- Units: 1 byte = 8 bits; 1 KB = 1024 B; 1 MB = 1024 KB; 1 GB = 1024 MB (so 2 GB = 2048 MB). **Mbps** = megabits/s; **MBps** = megabytes/s.
- Number systems: binary (0–1), octal (0–7), decimal, hexadecimal (0–9, A–F). **MSD** – Most Significant Digit; LSD – least.
- **Truth table** – shows every output of a **Boolean** function.

## Software
- System software (OS, drivers, BIOS) · **utility** software (antivirus, disk cleanup, backup, compression) · application software (Word, Excel, browsers, **DBMS**).
- OS: Windows, Linux (Ubuntu, Red Hat), macOS, Android. Open source: Linux, LibreOffice, Firefox.
- **DDL** – Data Definition Language (CREATE, ALTER, DROP); DML – Data Manipulation Language.
- MS Word supports hyperlinks and digital signatures. Extensions: .docx, .xlsx, .pptx, .pdf, .txt.

## Internet
| Short | Full form |
|---|---|
| WWW | World Wide Web |
| HTTP / HTTPS | HyperText Transfer Protocol (Secure) |
| URL | Uniform Resource Locator |
| **ISP** | **Internet Service Provider** |
| **ISDN** | **Integrated Services Digital Network** |
| LAN / MAN / WAN | Local / Metropolitan / Wide Area Network |
| IP / TCP | Internet Protocol / Transmission Control Protocol |
| HTML | HyperText Markup Language |
| Wi-Fi | Wireless Fidelity |

Browsers: Chrome, Edge, Firefox, Safari, Opera (**Adobe Flash is not a browser**). Search engines: Google, Bing, DuckDuckGo.

## Shortcut keys
Ctrl+C copy · Ctrl+X cut · Ctrl+V paste · Ctrl+Z undo · Ctrl+Y redo · Ctrl+S save · Ctrl+P print · Ctrl+A select all · F1 help · F2 rename · F5 refresh.
"""}],
}
