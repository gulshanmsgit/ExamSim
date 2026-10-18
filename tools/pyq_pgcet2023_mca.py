"""Previous-year paper · Karnataka PGCET 2023 (24 Sep 2023) · MCA entrance · version A1 · 80 Q (Part A Q1–60 one mark, Part B
Q61–80 two marks), 100 marks – mathematics, computer awareness, reasoning, general knowledge and English, as printed.
Source: KEA question-paper archive (p2_2023_mca_2023_18062026.pdf, URL in tools/pyq_manifest.tsv; scanned, transcribed from the
page images). Options (A)–(D) as printed. Current-affairs answers are as of 2023, when the paper was set.
No key for this paper was found on KEA's site, so every answer was worked out by ExamSim and is NOT the official key.
Skipped as flawed or ambiguous: Q1 (the 31st term is 1/123 – not an option), Q10 (three options satisfy X + Y = 1), Q44 (figure
count), Q45 (rule unclear), Q53 (GST rates have changed since), Q71 (option misprinted as bps), Q73 (the missing term 400 is not
an option), Q76 (the answer, West, is not an option)."""

SRC = "PGCET 2023 MCA · Q{}"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

Q = {

2: ('If A = [cos α  sin α; −sin α  cos α], then the value of AA′ is :', ['0', 'I', '2I', '3I'], 1, 'A rotation matrix is orthogonal.'),
3: ('How many three-digit odd numbers can be formed from the digits 5, 6, 7, 8, 9 if the digits can be repeated ?', ['25', '50', '75', '100'], 2, 'Units digit 5, 7 or 9: 5 × 5 × 3 = 75.'),
4: ('The coefficient of y in the expansion of (y² + c/y)⁵ is :', ['4 c²', '10 c²', '5 c³', '10 c³'], 3, 'Power of y = 10 − 3k = 1 → k = 3: ⁵C₃ c³ = 10c³.'),
5: ('The co-ordinates of a point dividing the line segment joining (1, 2) and (4, 5) internally in the ratio 2 : 1 are :', ['(3, 4)', '(4, 3)', '(5, 4)', '(5, 3)'], 0, '((2·4 + 1)/3, (2·5 + 2)/3).'),
6: ('The centre and radius of the circle with equation x² + y² − 4x − 10y + 4 = 0 are :', ['(−2, −5), 3', '(−2, −5), 5', '(2, 5), 3', '(2, 5), 5'], 3, 'r = √(4 + 25 − 4) = 5.'),
7: ('The coordinates of the foci of the ellipse 9x² + 4y² = 36 are :', ['(0, √5), (0, −√5)', '(0, 5), (0, − 5)', '(√5, 0), (−√5, 0)', '(5, 0), (− 5, 0)'], 0, 'x²/4 + y²/9 = 1: major axis along y, c = √(9 − 4).'),
8: ('The number of vertices and foci of a hyperbola respectively are :', ['two, one', 'one, one', 'two, two', 'one, two'], 2, 'Two of each.'),
9: ('If A, B, C are three matrices such that all the matrices are conformable for the product matrices, then :', ['(AB)C = (BA)C', '(AB)C = A(BC)', '(AB)C = C(AB)', '(AB)C = B(AC)'], 1, 'Associativity.'),
11: ('In Boolean algebra, the value of (X + Y)(X + Ȳ) is :', ['X', 'Y', 'X̄', 'Ȳ'], 0, 'X + YȲ = X.'),
12: ('If A = [1 0; 0 2], B = [1 1; 1 1], then the value of |AB| is :', ['1', '−1', '0', '2'], 2, '|B| = 0.'),
13: ('The value of cos (π/4 + x) + cos (π/4 − x) is :', ['√2 sin x', '√2 cos x', '2 sin x', '2 cos x'], 1, '2 cos(π/4) cos x.'),
14: ('The principal value of cot⁻¹ (−1/√3) is :', ['π/2', 'π/3', '2π/3', 'π'], 2, 'Range (0, π): π − π/3.'),
15: ('The value of sin⁻¹ (sin 3π/5) is :', ['π/5', '2π/5', '3π/5', '−3π/5'], 1, 'sin(3π/5) = sin(2π/5), and 2π/5 is in [−π/2, π/2].'),
16: ('The value of 3 sin (π/6) sec (π/3) − 4 sin (5π/6) cot (π/4) is :', ['0', '1', '−1', '1/2'], 1, '3 × ½ × 2 − 4 × ½ × 1 = 1.'),
17: ('One card is drawn from a well-shuffled deck of 52 cards. If each outcome is equally likely, the probability that the card is a diamond is :', ['1/2', '1/3', '1/4', '1/5'], 2, '13/52.'),
18: ('If σ is the standard deviation for a set of values in an x-series, the coefficient of variation is :', ['(σ/x̄) × 100', '√(σ/x̄) × 100', '(σ/x) × 100', '√(σ/x) × 100'], 0, 'CV = σ/mean × 100.'),
19: ('Which of the following values of the correlation coefficient r are valid ?', ['− 2', '− 1·5', '0·5', '1·5'], 2, '−1 ≤ r ≤ 1.'),
20: ('If the regression line of y on x is y = ax + b and regression line of x on y is x = cy + d, then which of the following is true ?', ['ac ≤ 1, r = ± √ac', 'ac < 1, r = ac', 'ac > 1, r = ± √ac', 'ac > 1, r = ac'], 0, 'r² = product of the regression coefficients ≤ 1.'),
21: ('Pratyush is the ____ fastest supercomputer in the world.', ['first', 'second', 'third', 'fourth'], 3, "At its 2018 launch Pratyush was called the world's fourth fastest supercomputer for weather and climate research."),
22: ('The main purpose of time sharing techniques used in computers is to make the best use of :', ['Central Processing Unit', 'Peripherals', 'Secondary storage', 'Floppy disks'], 0, 'CPU time is shared.'),
23: ('A joystick is primarily used to/for :', ['Control sound', 'Computer gaming', 'Draw pictures', 'Enter text'], 1, 'Gaming.'),
24: ('Which of the following is the largest unit of storage ?', ['TB', 'MB', 'KB', 'GB'], 0, 'Terabyte.'),
25: ("The use of combination of 1's and 0's is the feature of which of the following type of computer language ?", ['High Level Language', 'PASCAL', 'Machine language', 'COBOL'], 2, 'Binary.'),
26: ('The two categories of software are :', ['Word processing and Spreadsheet', 'Transaction and Application', 'Windows and MacOS', 'System and Application'], 3, 'System and application software.'),
27: ('What does the acronym ISP stand for ?', ['Internet Service Provider', 'Internal Service Provider', 'Internet Service Providing', 'Internet Service Provision'], 0, 'BSNL, Airtel and Jio are ISPs.'),
28: ("The one's complement of binary number 101010 is :", ['010110', '010101', '110111', '101011'], 1, 'Invert every bit: 101010 → 010101.'),
29: ('Which of the following uses the spawn mechanism to duplicate itself ?', ['Trojan Horse', 'Worm', 'Keystroke Logger', 'Logic Bomb'], 1, 'A worm spawns copies of itself and spreads through networks without needing a host program (Silberschatz).'),
30: ('To move to the bottom of a document while working on MS Word, which key is used ?', ['Home key', 'End key', 'Insert key', 'Ctrl key + End key'], 3, 'End alone goes to the end of the line.'),
31: ('Integrated Circuit (IC) chips used in computers are made with :', ['Copper', 'Aluminium', 'Silicon', 'Silver'], 2, 'Silicon.'),
32: ('Binary system is also called :', ['Base one system', 'Base two system', 'Base system', 'None of the above'], 1, 'Base 2.'),
33: ('What is Backup ?', ["Connecting the user's network to more components", 'Copying of files to save data from original source to another destination', 'Filtering on old data from new data', 'Accessing data from tape'], 1, 'A copy kept elsewhere.'),
34: ('Error in a program is called :', ['Bug', 'Debug', 'Virus', 'Noise'], 0, 'Bug.'),
35: ('Windows XP was released in the year :', ['2000', '1998', '1999', '2001'], 3, 'Windows XP came out in October 2001 and introduced fast user switching for home users.'),
36: ("If in a certain code language 'CROWNED' is written as 'PSDVEFO', which word will be coded as 'STREAMS' ?", ['QSRDTNB', 'SUTDTNB', 'TUSDTNB', 'SUTDBNT'], 1, 'First three letters +1 and reversed (CRO → DSP → PSD), middle letter −1, last three +1 and reversed: STR → SUT, E → D, AMS → TNB.'),
37: ('Nithish leaves his house. He walks 20 m in North-West direction and then 40 m in South-West direction. Next he moves 40 m in South-East direction. Finally he turns towards his house. In which direction is Nithish going ?', ['North-West', 'South-East', 'North-East', 'South-West'], 2, 'He ends up south-west of his house, so he walks north-east.'),
38: ("'M' is the daughter of 'N'. 'N' is married to 'Y'. 'G' is the mother of both 'Y' and 'Q'. 'Q' is the only son of 'X'. 'X' is the brother of 'H'. How is 'M' related to 'Q' ?", ['Son-in-law', 'Daughter', 'Niece', 'Grand-daughter'], 2, "Q is Y's brother, and M is Y's daughter."),
39: ('What comes in the place of question mark (?) in the following number series ?\n330, 80, 280, 120, 250, ?', ['160', '180', '110', '140'], 0, 'Two series: 330, 280, 250 and 80, 120, 160 (+40).'),
40: ('Find the odd one.', ['321', '876', '987', '345'], 3, 'The others have consecutive digits in descending order.'),
41: ('Given the following three-digit numbers :\n684, 512, 437, 385, 296\nWhat will be the resultant number if the second digit of the second lowest number is divided by the third digit of the highest number ?', ['3', '0', '2', '1'], 2, '385 → 8; 684 → 4; 8 ÷ 4 = 2.'),
42: ('Which one of the following interchange of signs would make the given equation correct ?\n5 + 3 × 8 − 12 ÷ 4 = 3', ['+ and +', '+ and ×', '− and ×', '− and ÷'], 3, '5 + 3 × 8 ÷ 12 − 4 = 5 + 2 − 4 = 3.'),
43: ('Find the missing letter and number in the following :\n[Figure: a hexagon divided into triangles; around it the numbers 4, 9, 16, 25, ?, 49 and the letters A, C, F, J, O, ?]', ['Y and 40', 'X and 81', 'W and 64', 'U and 36'], 3, 'Squares 2²…7² → 36; letters +2, +3, +4, +5, +6 → U.'),
46: ('Which of the following programme/scheme is not run by Government of India under National Health Mission ?', ['Mission Indradhanush', 'Janani Suraksha Yojana', 'Rashtriya Bal Swasthya Karyakram', 'Prasuti Araike'], 3, 'Prasuti Araike is a Karnataka state scheme.'),
47: ('Who is the architect of the recently inaugurated New Parliament House which is situated in New Delhi ?', ['Bimal Patel', 'Bijoy Jain', 'B.V. Doshi', 'Rahul Mehrotra'], 0, "HCP Design's Bimal Patel."),
48: ('Which of the following statements is/are correct with regard to Chandrayaan-3 ?\nI. It was launched on 15th July, 2023.\nII. It was launched from Satish Dhawan Space Centre.\nIII. Dr. P. Veeramuthuvel is the Mission Director.\nIV. The rocket which was used for the launch is LVM3-M4.', ['All the above', 'Only II and IV', 'Only II', 'Only III'], 1, 'Launched 14 July 2023; Veeramuthuvel was the Project Director (S. Mohana Kumar was Mission Director).'),
49: ('The first Vande Bharat Express train which was inaugurated on February 18, 2019 runs between which of the following cities?', ['Mumbai-Sainagar Shirdi', 'Puri-Howrah', 'Varanasi-New Delhi', 'Bengaluru-Dharwad'], 2, 'The first Vande Bharat (Train 18) ran between New Delhi and Varanasi; it was flagged off on 15 February 2019 and began regular service soon after.'),
50: ('At present who is the Comptroller and Auditor General of India ?', ['Girish Chandra Murmu', 'V. Narahari Rao', 'Shashikant Sharma', 'M.K. Jain'], 0, 'Correct in 2023, when the paper was set; K. Sanjay Murthy became CAG in November 2024.'),
51: ('The National Green Hydrogen Mission aims to enable India to be energy independent by which year ?', ['2030', '2035', '2042', '2047'], 3, 'Energy independence by 2047 (net zero by 2070).'),
52: ("Expand 'UPI'.", ['United Payment India', 'Unified Payment Interface', 'Unique Payment Information', 'Unified Payment Information'], 1, 'UPI was launched by NPCI in 2016.'),
54: ('Which of the following pairs is wrongly matched ?\nName of the Jnanpith Awardee – Language', ['Damodar Mauzo – Konkani', 'Krishna Sobti – Hindi', 'Pratibha Ray – Odia', 'Kedarnath Singh – Punjabi'], 3, 'Kedarnath Singh wrote in Hindi.'),
55: ('Which of the following pairs is wrongly matched ?\nAcquirer Bank – Merger Bank', ['Indian Bank – Vijaya Bank', 'Canara Bank – Syndicate Bank', 'Union Bank of India – Andhra Bank', 'Punjab National Bank – United Bank of India'], 0, 'Vijaya Bank merged into Bank of Baroda; Indian Bank took Allahabad Bank.'),
56: ("The synonym of 'Circumscribe' is :", ['Din', 'Mention', 'Restrict', 'Alliance'], 2, 'To limit.'),
57: ("The antonym of 'Philanthropist' is :", ['Disphilanthropist', 'Unphilanthropist', 'Disanthropist', 'Misanthropist'], 3, 'One who dislikes people.'),
58: ('Choose the correct meaning of the underlined phrase.\nMr. Jacob pulled through his illness.', ['recover', 'leave', 'give up', 'suppress'], 0, 'Pull through = recover from a serious illness or difficulty.'),
59: ("Identify the correct meaning of the idiomatic expression 'uphill task'.", ['Simple work', 'Hard work', 'Discontinuous work', 'Continuous work'], 1, 'An uphill task is a difficult one.'),
60: ('I saw four ____ in the forest.', ['deer', 'deers', 'deering', 'deered'], 0, 'Deer has the same plural.'),
61: ('The factorization of 4(x + y)² − 28(x² − y²) + 49(x − y)² is :', ['(5x + 9y)²', '(9y − 5x)²', '(5y + 9x)²', '(5y − 9x)²'], 1, '[2(x + y) − 7(x − y)]² = (9y − 5x)².'),
62: ('The solution of 2x² − 8y² = 18, 3x + 4y = 7 is :', ['(x, y) = (3, −1) or (5, −1)', '(x, y) = (3, 1) or (5, 2)', '(x, y) = (3·4, −0·8) or (5, −2)', '(x, y) = (3·4, 0·8) or (5, 2)'], 2, 'Both pairs satisfy x² − 4y² = 9 and 3x + 4y = 7.'),
63: ('The distance of the point (3, − 5) from the line 3x − 4y − 26 = 0 is :', ['1/5', '2/5', '3/5', '4/5'], 2, '|9 + 20 − 26| / 5.'),
64: ('The equation of the parabola which is symmetric about the y-axis and passes through the point (2, − 3) is :', ['4x² = − 3y', '3x² = − 4y', '2x² = − 3y', '3x² = − 2y'], 1, 'x² = ky: 4 = −3k.'),
65: ('Which of the following sets A, B, C, D, E are equal ?\nA = {0}\nB = {x : x > 15 and x < 5}\nC = {x : x − 5 = 0}\nD = {x : x² = 25}\nE = {x : x is an integral positive root of the equation x² − 2x − 15 = 0}', ['C, D, E', 'D, E', 'C, E', 'C, D'], 2, 'C = E = {5}; D = {5, −5}.'),
66: ('If A ∪ B = A ∩ B, then', ['A = B', 'A = B̄', 'Ā = B', 'Ā = B̄'], 0, 'Union equals intersection only when the sets are equal.'),
67: ('If cot x = − 5/12 and x lies in the 2nd quadrant, then the value of sin x is :', ['13/12', '13/14', '12/13', '14/13'], 2, '5-12-13 triangle; sine is positive in Q2.'),
68: ('In binary addition,\n0111 + 0001 = ____.', ['111', '1000', '1001', '1110'], 1, '7 + 1 = 8.'),
69: ('Who among the following invented the computer language COBOL ?', ['Grace Murray Hopper', 'John McCarthy', 'Guido van Rossum', 'Brendan Eich'], 0, "COBOL grew from Hopper's FLOW-MATIC."),
70: ('What is a website ?', ['A place from where we can get information in documents and files', 'A site that is owned by any particular company', 'A location on world wide web', 'A place from where we can access the Internet'], 2, 'A set of pages at one location on the Web.'),
72: ('Multiprogramming systems ____.', ['are easier to develop than single programming systems', 'execute each job faster', 'execute more jobs in the same time period', 'are used only on one large mainframe computer'], 2, 'Higher throughput, not faster jobs.'),
74: ('A watch which gains uniformly, is 3 minutes slow at 12 noon on Sunday and is 5 minutes 36 seconds fast at 4 pm on the next Sunday. At what time was it correct ?', ['12 pm on Monday', '12 am on Tuesday', '12 am on Wednesday', '12 am on the same day'], 2, 'It gains 8.6 min in 172 h; 3 min takes 60 h: Sunday noon + 60 h = midnight between Tuesday and Wednesday.'),
75: ('If 27th March, 1995 was a Monday, then what day of the week was 1st November, 1994 ?', ['Wednesday', 'Tuesday', 'Sunday', 'Monday'], 1, '146 days earlier; 146 = 20 weeks + 6 days.'),
77: ('In a hotel, 60% had vegetarian lunch while 30% had non-vegetarian lunch and 15% had both types of lunches. If 96 people were present, then how many did not eat either type of lunch ?', ['26', '20', '28', '24'], 3, '60 + 30 − 15 = 75%; 25% of 96 = 24.'),
78: ('Which of the following is/are wrongly matched ?\nIndustrial City – Industry\nI. Korba – Aluminium\nII. Vapi – Ship-building\nIII. Hissar – Steel\nIV. Dhanbad – Copper', ['Only I', 'Only II and IV', 'All of the above', 'None of the above'], 1, 'Vapi is a chemicals hub; Dhanbad is known for coal.'),
79: ('Which of following statement with regard to G20 Summit is wrong?', ['The 2023 G20 New Delhi Summit was the first ever G20 Summit to be held in India as well as in South Asia.', 'In 2024, G20 Summit is scheduled to be held in Rio de Janeiro.', 'In 2022, G20 Summit was held in Rome.', 'The first G20 Summit was held in 2008 in Washington, D.C.'], 2, 'The 2022 summit was held in Bali, Indonesia; Rome hosted it in 2021.'),
80: ('Which of the following cannot be a subordinate clause ?', ['Prepositional clause', 'Noun clause', 'Adjective clause', 'Adverb clause'], 0, 'Subordinate clauses are noun, adjective or adverb clauses.'),
}


def sets():
    out = []
    for lo in (1, 26, 51, 76):
        qs = [(q, o, a, e + NOTE, SRC.format(n)) for n in sorted(Q) if lo <= n <= lo + 24 for q, o, a, e in [Q[n]]]
        out.append({"name": f"Q{lo}–{lo + 24}", "questions": qs, "keep_order": True})
    return out


TOPIC = "PGCET 2023 – MCA entrance"
