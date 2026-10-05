"""Paper 1 · Current Affairs · planner topic P1-CA-08 Initiatives in Education in India (2 sub-topics × 20), with detailed notes (NOTES).
Sources: NEP 2020 document (MoE), Ministry of Education and PIB releases on Samagra Shiksha, NIPUN Bharat, PM SHRI, PM POSHAN, DIKSHA,
SWAYAM, PARAKH and APAAR; RTE Act 2009; NCERT, NCTE, UGC and AICTE websites; Karnataka School Education department. REAL previous-year
questions come from KEA 2026 GK, GFGC 2021 Education, KSET 2023–25 Education and General papers, GTTC 2024 GK (official KEA key) and
VAO 2024; answers without an official key were worked out by ExamSim and say so."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / TET). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

POLICY = [
    ("The three-language formula for language learning was recommended by",
     ["Mudhaliar Commission", "Radhakrishnan Commission", "Adiseshiah Review Committee", "Kothari Education Commission"], 3,
     "The formula was evolved by CABE (1956–61), recommended in modified form by the Kothari Commission (1964–66) and adopted in NPE 1968; NEP 2020 keeps it with more flexibility." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q96"),
    ("Secondary education as an important link in education is identified by",
     ["University Education Commission", "Mudaliar Commission", "Education Commission", "National policy of Education"], 1,
     "The Secondary Education Commission (1952–53), chaired by Dr A. Lakshmanaswami Mudaliar, dealt with secondary education." + NOTE, "GFGC 2021 Education · Q16"),
    ("What are the guidelines specified in the National Curriculum Framework (NCF) – 2005 ?\nI. Connecting knowledge to life outside school.\nII. School curriculum should include more content.\nIII. Ensuring that students do not just learn mechanical without thinking.\nIV. Ensuring that students are familiar with text books and other learning resources used in teaching.",
     ["I and II only", "II and III only", "III and IV only", "I and III only"], 3,
     "NCF 2005 asked for connecting knowledge to life outside school and moving away from rote learning; it wanted less curriculum load, not more content." + NOTE,
     "GFGC 2021 Education · Q57"),
    ("Match the following and choose the correct answer.\nList-I (Commission)\na) University Education Commission\nb) Secondary Education Commission\nc) National Education Policy\nd) Kothari Education Commission\nList-II (Years)\ni. 1952-53\nii. 1968, 1986\niii. 1964-66\niv. 1948-49",
     ["a-i, b-ii, c-iii, d-iv", "a-iii, b-ii, c-iv, d-i", "a-ii, b-iii, c-i, d-iv", "a-iv, b-i, c-ii, d-iii"], 3,
     "Radhakrishnan (University) Commission 1948–49; Mudaliar (Secondary) 1952–53; Kothari Commission 1964–66; national policies 1968 and 1986." + NOTE,
     "KSET 2025 Education · Q16"),
    ("The provision of earning credits from optional and elective courses was introduced in Higher Education by which of the following?",
     ["Academic Bank of Credits", "MOOCs on SWAYAM portal", "Choice-based Credit System", "B.Voc courses"], 2,
     "UGC introduced the Choice-Based Credit System (CBCS) in 2015, letting students pick core, elective and skill courses." + NOTE, "KSET 2024 General Paper · Q5"),
    ("The National Education Policy 2020 was approved by the Union Cabinet on 29 July 2020. The committee that drafted it was chaired by:",
     ["Dr K. Kasturirangan", "Dr D. S. Kothari", "T. S. R. Subramanian", "Prof. Yash Pal"], 0,
     PYQ + "T. S. R. Subramanian's committee (2016) gave inputs earlier; NEP 2020 replaced the 1986 policy."),
    ("NEP 2020 replaces the 10+2 school structure with:",
     ["5+3+3+4 (ages 3–8, 8–11, 11–14, 14–18)", "4+4+4+4", "6+3+3", "5+5+2"], 0,
     "Foundational (3 years pre-school + classes 1–2), preparatory (3–5), middle (6–8), secondary (9–12)."),
    ("NEP 2020 aims to raise the Gross Enrolment Ratio in higher education to ____ by 2035.",
     ["50%", "100%", "26%", "75%"], 0, PYQ + "It also aims for 100% GER in school education by 2030."),
    ("According to NEP 2020, the medium of instruction should preferably be the home language / mother tongue at least up to:",
     ["Class 5 (preferably till class 8 and beyond)", "Class 1", "Class 12", "Graduation"], 0, "It is not compulsory; states decide."),
    ("The Right of Children to Free and Compulsory Education Act, 2009 covers children of the age group:",
     ["6 to 14 years", "3 to 6 years", "6 to 18 years", "5 to 15 years"], 0, PYQ + "It came into force on 1 April 2010 under Article 21A (86th Amendment, 2002)."),
    ("Under Section 12(1)(c) of the RTE Act, private unaided schools must reserve ____ of entry-level seats for children of weaker sections.",
     ["25%", "10%", "15%", "50%"], 0, "The State reimburses the schools."),
    ("Which Article of the Constitution makes elementary education a Fundamental Right?",
     ["Article 21A", "Article 45", "Article 51A(k)", "Article 30"], 0,
     PYQ + "Article 45 (DPSP) now covers early childhood care up to 6 years; Article 51A(k) makes it a parent's duty to educate a child aged 6–14."),
    ("Wood's Despatch (1854), called the 'Magna Carta of English education in India', recommended:",
     ["A graded system of schools and universities at Calcutta, Bombay and Madras", "Abolition of English", "Only Sanskrit education", "Free higher education for all"], 0,
     "The three universities were founded in 1857."),
    ("The 'Learning without Burden' report (1993) was prepared by a committee chaired by:",
     ["Prof. Yash Pal", "Acharya Ramamurti", "D. S. Kothari", "Sam Pitroda"], 0, PYQ + "It led to reducing curriculum load and inspired NCF 2005."),
    ("The National Policy on Education 1986 was revised and its Programme of Action (POA) brought out in:",
     ["1992", "1990", "2000", "2005"], 0, "The Acharya Ramamurti Committee (1990) had reviewed NPE 1986."),
    ("Consider the statements:\nI. NEP 2020 proposes that the four-year undergraduate programme have multiple entry and exit options.\nII. NEP 2020 proposes spending 6% of GDP on education.",
     I_II, 2, "Both are NEP 2020 goals; certificates, diplomas or degrees are given at different exit points."),
    ("Assertion (A): The Kothari Commission is known as the first commission to examine all aspects of education.\nReason (R): It reviewed education from the primary to the university level.",
     AR, 0, "Its report was 'Education and National Development' (1966)."),
    ("Assertion (A): The RTE Act applies to children of 3–18 years.\nReason (R): The RTE Act provides free and compulsory education to children of 6–14 years.",
     AR, 3, "A is false – the Act covers 6–14 years."),
    ("Arrange in chronological order:\n1. Hunter Commission\n2. Sargent Plan\n3. Radhakrishnan Commission\n4. Kothari Commission",
     ["1, 2, 3, 4", "2, 1, 3, 4", "1, 3, 2, 4", "3, 1, 2, 4"], 0, PYQ + "1882, 1944, 1948–49, 1964–66."),
    ("National Curriculum Framework for Foundational Stage (NCF-FS) and for School Education (NCF-SE) were released in:",
     ["2022 and 2023", "2005 and 2009", "2015 and 2016", "2020 and 2021"], 0, "Both were prepared by the steering committee headed by Dr K. Kasturirangan."),
]

SCHEMES = [
    ("'SWAYAM' stands for:",
     ["Study Website for Young Actual Learning", "Study Webs for Action Learning of Young Attentive Minds", "Study Websites for Automated Young Active Minds",
      "Study Webs of Active Learning for Young Aspiring Minds"], 3,
     "SWAYAM (2017) is India's MOOC platform, from class 9 to post-graduation." + NOTE, "KSET 2024 Education · Q61"),
    ("SWAYAM is:",
     ["It offers free online courses in various subjects ranging from basic to advanced levels.", "It offers free offline courses in various subjects.",
      "It offers paid online courses in various subjects ranging from basic to advanced levels.", "It offers free online courses in various subjects, only basic level."], 0,
     "Courses are free; a fee is charged only for the optional certification exam." + NOTE, "KSET 2023 Education · Q52"),
    ("'SWAYAM' an initiative of the Government of India aims at",
     ["Promoting the SHG's in rural areas", "Providing affordable and quality education to the citizens for free", "Providing public health facilities",
      "Providing technical assistance to entrepreneurs"], 1,
     "It aims at access, equity and quality in education through free online courses." + KEY, "GTTC 2024 Asst Gr-II GK · Q58"),
    ("Which initiative of the Government of India provides 24x7 DTH satellite TV channels?",
     ["Shodhganga", "SWAYAM", "Swayam Prabha", "Shodh Sindhu"], 2,
     "Swayam Prabha broadcasts educational TV channels; Shodhganga is the repository of Indian theses and Shodh Sindhu an e-journal consortium." + NOTE,
     "KSET 2024 General Paper · Q38"),
    ("e-Pathshala has been developed by :",
     ["NCERT", "NCTE", "NIEPA", "UGC"], 0,
     "e-Pathshala (2015) gives NCERT textbooks and resources online; e-PG Pathshala is UGC's post-graduate content platform." + NOTE, "KSET 2023 Education · Q19"),
    ("Which of the following organisation is associated with accreditation of preservice teacher education programmes?",
     ["UGC", "NCERT", "SCERT", "NCTE"], 3,
     "The National Council for Teacher Education (statutory since 1993) recognises and regulates teacher-education programmes." + NOTE, "GFGC 2021 Education · Q40"),
    ("The board which is responsible for assessing and accrediting technical programs to ensure quality standards is",
     ["AICTE", "NITs", "NBA", "UGC"], 2,
     "The National Board of Accreditation (1994) accredits programmes; NAAC (Bengaluru) accredits higher-education institutions." + NOTE, "KSET 2025 General Paper · Q49"),
    ("Match the following educational schemes with their objectives:\na) National Means-cum-Merit Scholarship scheme\nb) Vidyanjali\nc) Unnat Bharat Abhiyan\nd) Pragati\ni. Scholarship for girls in technical education\nii. Connecting higher education institutions with society & villages\niii. Award scholarship to meritorious students of economically weaker sections\niv. Remedial classes & training programmes for students through voluntarism.",
     ["a – iii, b – iv, c – ii, d – i", "a – i, b – ii, c – iv, d – iii", "a – ii, b – iii, c – i, d – iv", "a – iii, b – i, c – iv, d – ii"], 0,
     "NMMSS – merit scholarships for poorer students; Vidyanjali – school volunteers; Unnat Bharat Abhiyan – HEIs adopt villages; Pragati – AICTE scholarship for girls." + NOTE,
     "VAO 2024 Paper-1 · Q44"),
    ("Grama Panchayat libraries in Karnataka was renamed as",
     ["Arivu Kendra", "Kalike Kendra", "Shikshana Kendra", "Jnana Kendra"], 0,
     "Karnataka renamed its Grama Panchayat libraries 'Arivu Kendras' (knowledge centres) and upgraded them with digital resources." + KEY, "GTTC 2024 Asst Gr-II GK · Q66"),
    ("The scheme that merged Sarva Shiksha Abhiyan, Rashtriya Madhyamik Shiksha Abhiyan and Teacher Education in 2018 is:",
     ["Samagra Shiksha", "PM SHRI", "NIPUN Bharat", "PM POSHAN"], 0, PYQ + "It covers school education from pre-school to class 12."),
    ("NIPUN Bharat (launched 5 July 2021) aims at:",
     ["Foundational literacy and numeracy for every child by the end of class 3", "Free laptops for college students", "Vocational training for adults", "Teacher recruitment"], 0,
     "NIPUN = National Initiative for Proficiency in reading with Understanding and Numeracy."),
    ("The PM POSHAN scheme (2021) is the new name of the:",
     ["Mid-day meal scheme", "Integrated Child Development Services", "Beti Bachao Beti Padhao", "Kasturba Gandhi Balika Vidyalaya scheme"], 0,
     PYQ + "The national mid-day meal programme began in 1995; Karnataka calls it Akshara Dasoha."),
    ("PM SHRI schools (2022) are meant to:",
     ["Develop over 14,500 existing schools into model schools showcasing NEP 2020", "Build new private schools", "Train only teachers", "Run only online classes"], 0,
     "PM SHRI = PM Schools for Rising India."),
    ("DIKSHA, the national digital platform for school education, stands for:",
     ["Digital Infrastructure for Knowledge Sharing", "Digital Initiative for Knowledge and Skill Acquisition", "Direct Information for Kids and School Administration", "Distance Education for Higher Achievers"], 0,
     PYQ + "It is the 'One Nation, One Digital Platform' of PM eVIDYA (2020)."),
    ("NISHTHA is a national programme for:",
     ["Integrated in-service training of school teachers and heads", "Girls' hostels", "School buildings", "Student scholarships"], 0,
     "NISHTHA = National Initiative for School Heads' and Teachers' Holistic Advancement (2019)."),
    ("PARAKH, set up under NCERT in 2023, is India's:",
     ["National Assessment Centre for standard-setting in student assessment", "Teacher-recruitment board", "Textbook printing press", "Scholarship portal"], 0,
     PYQ + "It conducted the PARAKH Rashtriya Sarvekshan (earlier National Achievement Survey) in December 2024."),
    ("APAAR ID, introduced under NEP 2020, is:",
     ["A lifelong 12-digit academic ID for every student ('One Nation, One Student ID')", "A teacher's salary code", "A school's land record", "An exam roll number"], 0,
     "It links with the Academic Bank of Credits and DigiLocker."),
    ("'Nali-Kali', the activity-based joyful learning method for lower primary classes, began in 1995 in:",
     ["H. D. Kote taluk, Mysuru district, Karnataka", "Kerala", "Delhi", "Tamil Nadu"], 0, PYQ + "It was supported by UNICEF and later spread across Karnataka."),
    ("Kasturba Gandhi Balika Vidyalayas (2004) are:",
     ["Residential upper-primary (now up to class 12) schools for girls from disadvantaged groups", "Day schools for boys", "Colleges for women", "Teacher-training institutes"], 0,
     "They target educationally backward blocks."),
    ("Match:\na. NCERT  b. NCTE  c. NAAC  d. NIOS\n1. School curriculum and textbooks  2. Teacher-education standards  3. Accreditation of higher-education institutions  4. Open schooling",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "NAAC is headquartered in Bengaluru; NCERT was set up in 1961."),
]

TOPICS = {
    "Initiatives in Education in India": [("1 · Education Policies, Commissions, NEP 2020 and RTE", POLICY),
                                          ("2 · Schemes, Digital Initiatives and Education Bodies", SCHEMES)],
}

NOTES = {
    "Initiatives in Education in India": [{"title": "Education initiatives in India – detailed notes", "md": """# Initiatives in education in India

## 1. Commissions and policies (in order)
| Year | Commission / policy | Remember |
|---|---|---|
| 1835 | **Macaulay's Minute** | English education |
| **1854** | **Wood's Despatch** | 'Magna Carta of English education'; universities at Calcutta, Bombay, Madras (**1857**) |
| 1882 | **Hunter Commission** | Primary and secondary education |
| 1917–19 | Sadler (Calcutta University) Commission | |
| 1929 | Hartog Committee | Wastage and stagnation |
| 1937 | **Wardha scheme** (Gandhiji's **Nai Talim** / basic education) | Zakir Hussain committee |
| 1944 | **Sargent Plan** | Post-war educational development |
| **1948–49** | **University Education Commission** – Dr **S. Radhakrishnan** | Led to UGC |
| **1952–53** | **Secondary Education Commission** – Dr **A. L. Mudaliar** | Secondary education as a link |
| **1964–66** | **Education Commission** – Dr **D. S. Kothari** | 'Education and National Development'; common school system; 10+2+3; 6% of GDP; **three-language formula** |
| **1968** | **First National Policy on Education** (Indira Gandhi) | Three-language formula adopted |
| **1986** | **NPE 1986** (Rajiv Gandhi) | Operation Blackboard (1987), Navodaya Vidyalayas, DIETs |
| 1990 | Acharya **Ramamurti** Committee | Review of NPE |
| **1992** | Revised NPE + **Programme of Action** | |
| 1993 | **Yash Pal** – 'Learning without Burden' | |
| 2005 | **NCF 2005** | Connect knowledge to life outside school; no rote learning; reduce load |
| **2009** | **RTE Act** | In force 1 April 2010 |
| **2020** | **NEP 2020** – Dr **K. Kasturirangan** | Approved **29 July 2020** |
| 2022 / 2023 | **NCF-FS / NCF-SE** | Under NEP 2020 |

## 2. NEP 2020 – key points
- **5+3+3+4** structure: foundational (age 3–8), preparatory (8–11), middle (11–14), secondary (14–18).
- **Foundational literacy and numeracy** by class 3 → **NIPUN Bharat**.
- Mother tongue / home language as medium at least till **class 5** (preferably 8).
- Flexible three-language formula; no language imposed.
- Vocational education and internships from **class 6**; coding from the middle stage.
- Board exams made 'easier', twice a year option; **PARAKH** as the national assessment centre.
- Higher education: **GER 50% by 2035**; 4-year UG with **multiple entry and exit**; **Academic Bank of Credits**; **APAAR ID**; Higher Education Commission of India (proposed); **National Research Foundation** (Act 2023).
- Public spending on education target: **6% of GDP**.
- Teacher education: 4-year integrated **B.Ed.** as the minimum by 2030.

## 3. Constitution and RTE
- **Article 21A** (86th Amendment, 2002) – free and compulsory education for **6–14 years** (Fundamental Right).
- **Article 45** – early childhood care and education up to 6 years (DPSP).
- **Article 51A(k)** – parent's duty to provide education to a child of 6–14.
- **RTE Act 2009**: no capitation fee, no screening; **25% seats** in private unaided schools for disadvantaged children (Sec 12(1)(c)); pupil–teacher ratio 30:1 (primary), 35:1 (upper primary); School Management Committees.

## 4. School-education schemes
| Scheme | Year | Purpose |
|---|---|---|
| **Operation Blackboard** | 1987 | Minimum facilities in primary schools |
| DPEP | 1994 | District Primary Education Programme |
| Mid-day meal → **PM POSHAN** | 1995 → 2021 | Hot cooked meal; Karnataka: **Akshara Dasoha**, Ksheera Bhagya (milk, 2013) |
| **Sarva Shiksha Abhiyan** | 2001 | Universal elementary education |
| **Kasturba Gandhi Balika Vidyalaya** | 2004 | Residential schools for girls of disadvantaged groups |
| **RMSA** | 2009 | Secondary education |
| **Beti Bachao Beti Padhao** | 22 Jan 2015 (Panipat) | Girl child |
| **Samagra Shiksha** | 2018 | SSA + RMSA + Teacher Education merged |
| **NISHTHA** | 2019 | Teacher training |
| **PM eVIDYA** | 2020 | Digital / on-air education (DIKSHA, Swayam Prabha TV) |
| **NIPUN Bharat** | 5 July 2021 | Foundational literacy and numeracy by class 3 |
| **Vidyanjali** | 2021 | Volunteers and donors help schools |
| **Vidya Pravesh** | 2021 | 3-month play-based school-readiness module for class 1 |
| **PM SHRI** | Sept 2022 | 14,500+ model schools |
| National Means-cum-Merit Scholarship | 2008 | Class 9–12 scholarships for meritorious poor students |

## 5. Higher education and digital initiatives
| Initiative | Facts |
|---|---|
| **SWAYAM** (2017) | **Study Webs of Active-Learning for Young Aspiring Minds** – free MOOCs (fee only for certification) |
| **Swayam Prabha** | **24×7 DTH** educational TV channels |
| **DIKSHA** (2017) | **Digital Infrastructure for Knowledge Sharing** – 'One Nation, One Digital Platform' |
| **e-Pathshala** | **NCERT** e-books; **e-PG Pathshala** – UGC (PG content) |
| Shodhganga / Shodh Sindhu | Theses repository / e-journal consortium (INFLIBNET) |
| **CBCS** (2015, UGC) | Choice-Based Credit System – electives earn credits |
| Academic Bank of Credits (2021), **APAAR ID** | Stored credits; lifelong student ID |
| NIRF (2015) | National Institutional Ranking Framework |
| **Unnat Bharat Abhiyan** (2014) | HEIs adopt villages |
| **Pragati** / Saksham (AICTE) | Scholarships for girls / specially-abled in technical education |
| PM Vidyalaxmi (2024) | Collateral-free education loans |

## 6. Bodies
| Body | Role / facts |
|---|---|
| **NCERT** (1961) | School curriculum, textbooks; PARAKH (2023) |
| **NCTE** (statutory 1993) | Teacher education – recognises programmes |
| **UGC** (1953; Act 1956) | Funds and regulates universities |
| **AICTE** (1945; statutory 1987) | Technical education |
| **NAAC** (1994, **Bengaluru**) | Accredits higher-education **institutions** |
| **NBA** (1994) | Accredits technical **programmes** |
| **NIOS** (1989) | Open schooling |
| NIEPA | Educational planning and administration |
| Kendriya Vidyalaya Sangathan (1963), Navodaya Vidyalaya Samiti (1986) | Central schools |

## 7. Karnataka initiatives
- **Nali-Kali** (1995, H. D. Kote, Mysuru – UNICEF): activity-based learning for classes 1–3.
- **Chinnara Angala** (bridge course for out-of-school children), **Kalika Chetarike** (2022 learning-recovery programme), **Vidyagama** (2020, COVID-time learning).
- **Arivu Kendras** – renamed Grama Panchayat libraries.
- Karnataka Public Schools (KPS) – classes LKG–12 on one campus; State Education Policy commission headed by Prof. **Sukhadeo Thorat** (2023).

## 8. Traps
- Three-language formula: evolved by CABE, **recommended by the Kothari Commission**, adopted in **NPE 1968**.
- **Radhakrishnan** = university education (1948–49); **Mudaliar** = secondary (1952–53).
- **NAAC** accredits institutions; **NBA** accredits programmes; **NCTE** accredits teacher education.
- SWAYAM courses are **free**; Swayam **Prabha** is the TV channel service.
- RTE age group is **6–14**, not 3–18.
"""}],
}
