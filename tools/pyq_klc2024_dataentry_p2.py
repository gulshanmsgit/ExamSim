"""Previous-year paper · Karnataka Legislative Council Secretariat recruitment 2024 (exam 2025) · Data Entry Operator · Paper-2 ·
version A1 · 100 Q (Kannada Q1–35, English Q36–70, Computer Q71–100), 100 marks.
Source: KEA question-paper archive (p2_2024_data_entry_assistant_kec.pdf, URL in tools/pyq_manifest.tsv; bilingual booklet,
transcribed from the page images). Only the COMPUTER section (Q71–100) is in this CS pack; the Kannada and English sections
belong to Paper 1 subjects. Options (1)–(4) are A–D in the printed order. Q77's ER symbols are described in words.
Answers: the parsed key file for this paper (final_klc_dataentry_p2) does not reliably match the booklet (it gives (2) for Q80,
ENIAC), so every answer here was worked out by ExamSim and is marked as not KEA's official key."""

SRC = "Legislative Council 2024 Data Entry Operator P2 · Q{}"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

Q = {
71: ("What is the default subnet mask of a class B, IP value in address?", ["255.0.0.0", "255.255.0.0", "255.255.255.255", "255.255.255.0"], 1, "Class B = /16."),
72: ("Which of the following is a linear data structure?", ["Tree", "Graph", "Stack", "Hash table"], 2, "Stacks, queues, arrays and lists are linear."),
73: ("The OS environment which permits many processors active at the same time is ____.", ["Multiprogramming", "Time-sharing", "Multiprocessing", "Multitasking"], 2,
     "Multiprocessing = several CPUs."),
74: ("Which one among the following is not a basic function of operating system?", ["Virus protection", "File management", "Device management", "Process management"], 0,
     "Antivirus is a utility."),
75: ("The symbol 'E' represents ____ decimal value in Hexadecimal number system.", ["13", "14", "5", "8"], 1, "A = 10 … E = 14."),
76: ("In RDBMS, a data record is known as ____", ["Column", "Table", "Database", "Tuple"], 3, "A row = tuple."),
77: ("Match the following\nEntity Type\na) Attribute\nb) Relationship\nc) Entity\nd) Cardinality Ratio\nER Representation\n(i) an ellipse\n(ii) a diamond\n(iii) a rectangle\n(iv) two rectangles joined through a diamond, the lines labelled 1 and N",
     ["a – i, b – ii, c – iii, d – iv", "a – ii, b – iii, c – i, d – iv", "a – iv, b – iii, c – ii, d – i", "a – iii, b – iv, c – ii, d – i"], 0, "Chen notation."),
78: ("= SUM (A1 : E1) formula in MS Excel performs which of the following task?",
     ["calculates the sum of all the values in cells from A1 to E1", "calculates the sum of values in cells, A1 and E1 only", "calculates the sum of the values in cells A1 to A10", "calculates the sum of values in cells E1 to E10"], 0,
     "A colon means a range; SUM(A1,E1) would add only two cells."),
79: ("The software available for free, but source code may not be available, such softwares are called",
     ["Proprietary software", "Application software", "Freeware", "System software"], 2, "Freeware is free of cost but usually closed source."),
80: ("Expand ENIAC", ["Electronic Numerical Integrator and Computer", "Electrical Numerical Integrator and Computer", "Electrical Numbered Integrator and Computer", "Electronic Numerical Integrator and Concepts."], 0,
     "ENIAC (1946): Electronic Numerical Integrator and Computer."),
81: ("____ is not a scheduling algorithm in OS", ["First come first serve", "Shortest job first", "Round Robin", "Banker's Algorithm"], 3, "Banker's algorithm avoids deadlock."),
82: ("____ command is used to change the attributes of a file", ["COPY", "REN", "ATTRIB", "TYPE"], 2, "DOS ATTRIB +R/+H etc."),
83: ("____ tab is used to enable 'Ruler' option in MS Word.", ["Design", "Page layout", "Review", "View"], 3, "View → Ruler."),
84: ("The main goal of machine learning is", ["To completely automate manual tasks", "To make computers intelligent like human beings", "To create self aware machines", "To enable computers to learn from data"], 3,
     "Learning from data without explicit programming."),
85: ("The 2's complement of 101000 is", ["011000", "010101", "010111", "000111"], 0, "1's complement 010111, plus 1 = 011000."),
86: ("The smallest unit that can be written to or read from the disk is a", ["Track", "Head", "Byte", "Sector"], 3, "Disks transfer whole sectors."),
87: ("Primary key in DBMS should be", ["Unique", "Not null", "Unique and not null", "Null"], 2, "Entity integrity."),
88: ("Data transmission used in walkie-talkie is", ["Simplex", "Duplex", "Half-duplex", "Complex"], 2, "Both ways, one at a time."),
89: ("A set of programs that controls the resources of a system and provides it to the users with an interface that is easier to use is called",
     ["Utility programs", "Application software", "Operating system", "Firmware"], 2, "Definition of an OS."),
90: ("Simplex communication system can transmit data", ["In one direction", "In both directions", "Switch direction each time the direction of data transfer reverses", "None of the above"], 0,
     "e.g. TV broadcast."),
91: ("CPU Registers are used for\na) Storing data\nb) Storing instructions\nc) Storing intermediate results",
     ["Only a is correct", "Only b is correct", "Both a and c are correct", "a, b and c are correct"], 3, "IR holds instructions; others hold data and results."),
92: ("MAN stands for", ["Metropolitan Area Network", "Main Area Network", "Modified Area Network", "Middle Area Network"], 0, "City-wide network."),
93: ("The ____ network is owned by multiple organizations.", ["LAN", "WAN", "MAN", "PAN"], 1, "WAN links belong to several carriers and organisations."),
94: ("A system that prevents unauthorised access to a private computer network is", ["IDS", "FireWall", "Nmap", "Malware"], 1, "An IDS detects; a firewall blocks."),
95: ("____ is used in a symmetric encryption", ["Public key", "Private key", "Candidate key", "Secret key"], 3, "One shared secret key."),
96: ("The shortcut keys for slide show in MS PowerPoint are", ["Shift + F5", "Shift + F7", "Ctrl + F2", "Ctrl + F5"], 0,
     "Shift + F5 starts the show from the current slide (F5 alone from the beginning)."),
97: ("A 4 bit word is called as", ["Noble", "Nibble", "Byte", "Bit"], 1, "4 bits = nibble."),
98: ("In MS-EXCEL, the full form of 'PV' is", ["Past Value", "Present Value", "Post Value", "Pet Value"], 1, "PV() = present value."),
99: ("The shortcut keys in MS Word used to find a text and automatically replace it with something different are", ["Ctrl + R", "Ctrl + U", "Ctrl + H", "Ctrl + Z"], 2,
     "Ctrl + H opens Replace."),
100: ("____ is an example for a written communication", ["Making a phone call", "Attending a meeting", "Sending a text message", "Having a conversation"], 2, "Text is written."),
}


def sets():
    qs = [(q, o, a, e + NOTE, SRC.format(n)) for n in sorted(Q) for q, o, a, e in [Q[n]]]
    return [{"name": "Q71–100 · Computer section", "questions": qs, "keep_order": True}]


TOPIC = "Legislative Council 2024 – Data Entry Operator Paper-2 (Computer section)"
