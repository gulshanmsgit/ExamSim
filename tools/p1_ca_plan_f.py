"""Paper 1 · Current Affairs (planner topic) · P1-CA-13 Indian Constitution – amendments, recent constitutional developments,
important articles, parts and schedules (2 × 20) with detailed NOTES. GK-15 covers rights, legislature, executive and judiciary;
this topic covers the 'in the news' side. References: M. Laxmikanth – Indian Polity, PRS Legislative Research, PIB.
REAL previous-year questions come from the KEA 2026 general-knowledge papers (no published key – answers worked out by ExamSim)."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

AMENDMENTS = [
    ("According to Article 368 of Indian Constitution, changes in which of the following is not considered as an Amendment to Indian Constitution?",
     ["Election process of President of India", "Provisions related to Supreme Court and High Court", "Any of the lists in the Seventh Schedule", "Any entry in the Second Schedule"], 3,
     "Changes to the Second Schedule (salaries, allowances) are made by a simple law and are 'not deemed an amendment for the purposes of Art. 368'. "
     "The President's election, the judiciary and the Seventh Schedule lists need a special majority plus ratification by half the states." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q67"),
    ("Identify the Article and Part, with reference to Amendment of the Constitution:",
     ["Article 366 and Part XI", "Article 367 and Part XI", "Article 368 and Part XX", "Article 368 and Part XXI"], 2,
     "Part XX has only one Article – 368. Part XXI deals with temporary, transitional and special provisions." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q5"),
    ("Consider the following statements regarding 101st Constitutional Amendment of the Constitution of India:\na. It was passed by the Parliament in 2015.\n"
     "b. It paved the way for GST.\nc. It provided for the establishment of the GST Council.\nWhich of the above statements is/are incorrect?",
     ["Only a", "Only a and b", "a, b and c", "Only b and c"], 0,
     "The 101st Amendment was passed in 2016 (assent 8 Sep 2016); GST began on 1 July 2017; GST Council – Art. 279A." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q9"),
    ("The Constitution (71st Amendment) Act, 1992 amends Eighth Schedule to the Constitution to include which of the following languages?\n(a) Konkani\n(b) Manipuri\n(c) Nepali\n(d) Tulu",
     ["(a), (b) and (c)", "(a), (b) and (d)", "(a), (c) and (d)", "(b), (c) and (d)"], 0,
     "Tulu is not yet in the Eighth Schedule. 21st Amdt (1967) added Sindhi; 92nd (2003) Bodo, Dogri, Maithili, Santhali – total 22." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q46"),
    ("The 97th Constitutional Amendment deals with",
     ["Nari Vandana Bill", "Co-operative Societies", "Goods and Services Tax", "Official Languages"], 1,
     "97th Amendment (2011): right to form co-operatives in Art. 19(1)(c), Art. 43B and Part IXB." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q78"),
    ("Which of the following statements is/are INCORRECT with respect to Special Intensive Revision (SIR)?\n(a) Every year Election Commission of India conducts this exercise.\n"
     "(b) The names of new voters who are aged 18+ are being included in the voters list.\n(c) It also intends to remove the names of illegal foreign immigrants.\n"
     "(d) Election Commission of India can conduct SIR exercise if the concerned states give consent.",
     ["(a) and (b)", "(b) and (c)", "(c) and (d)", "(a) and (d)"], 3,
     "SIR is a special, not annual, revision (summary revision is yearly); the EC conducts it under Art. 324 and the RP Act, 1950 without needing state consent." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q99"),
    ("The 103rd Constitutional Amendment (2019) provided:",
     ["Up to 10% reservation for economically weaker sections (EWS) in education and public jobs", "Women's reservation in legislatures",
      "Constitutional status to the NCBC", "Abolition of Anglo-Indian nomination"], 0,
     PYQ + "Upheld by the Supreme Court in Janhit Abhiyan (2022). It added Arts 15(6) and 16(6)."),
    ("Which amendment extended SC/ST reservation in the Lok Sabha and Assemblies by ten years and ended nomination of Anglo-Indians?",
     ["104th Amendment, 2020", "95th Amendment, 2010", "102nd Amendment, 2018", "105th Amendment, 2021"], 0, "Reservation now runs until January 2030."),
    ("The 105th Amendment (2021) is about:",
     ["Restoring states' power to prepare their own lists of socially and educationally backward classes", "GST compensation",
      "Lowering the voting age", "Creating the National Judicial Appointments Commission"], 0, PYQ + "It reversed the effect of the Maratha reservation judgment (2021)."),
    ("The Constitution (106th Amendment) Act, 2023 – 'Nari Shakti Vandan Adhiniyam' – provides:",
     ["One-third of seats for women in the Lok Sabha, state Assemblies and the Delhi Assembly, after the next census and delimitation",
      "50% reservation for women in panchayats", "Reservation for women in the Rajya Sabha", "Women's reservation in central government jobs"], 0,
     "The reservation will last 15 years and includes seats for SC/ST women; it does not cover the Rajya Sabha or Legislative Councils."),
    ("Article 370 relating to Jammu and Kashmir was made inoperative in August 2019. The Supreme Court upheld the decision in:",
     ["December 2023", "August 2020", "January 2022", "March 2024"], 0, PYQ + "J&K and Ladakh became Union territories on 31 October 2019."),
    ("The 44th Amendment (1978) made which change to emergency provisions?",
     ["Replaced 'internal disturbance' with 'armed rebellion' as a ground for national emergency", "Introduced financial emergency",
      "Allowed suspension of Article 21 during emergency", "Abolished President's Rule"], 0,
     "It also said Arts 20 and 21 cannot be suspended and required the Cabinet's written advice for an emergency."),
    ("The Anti-Defection Law (Tenth Schedule) was added by the:",
     ["52nd Amendment, 1985", "61st Amendment, 1988", "73rd Amendment, 1992", "91st Amendment, 2003"], 0,
     PYQ + "The 91st Amendment (2003) removed the 'split' exception; mergers need two-thirds of the legislature party."),
    ("The voting age was reduced from 21 to 18 years by the:",
     ["61st Amendment, 1988", "42nd Amendment, 1976", "52nd Amendment, 1985", "73rd Amendment, 1992"], 0, "It came into force in 1989; Art. 326 – adult suffrage."),
    ("The 73rd and 74th Amendments (1992) added respectively:",
     ["Part IX and the Eleventh Schedule (panchayats); Part IXA and the Twelfth Schedule (municipalities)", "Part IVA and Part XIVA",
      "The Tenth and Ninth Schedules", "Part XX and Part XXI"], 0, "The 11th Schedule lists 29 subjects; the 12th lists 18."),
    ("The 99th Amendment (2014) creating the National Judicial Appointments Commission (NJAC) was:",
     ["Struck down by the Supreme Court in 2015 (Fourth Judges case)", "Ratified and is in force", "Withdrawn by Parliament in 2018",
      "Replaced by the 102nd Amendment"], 0, PYQ + "The collegium system therefore continues."),
    ("The National Commission for Backward Classes got constitutional status (Article 338B) through the:",
     ["102nd Amendment, 2018", "89th Amendment, 2003", "65th Amendment, 1990", "93rd Amendment, 2005"], 0,
     "89th Amdt – separate NCST (338A); 65th – National Commission for SCs and STs; 93rd – reservation in private educational institutions (15(5))."),
    ("Constitution Day (Samvidhan Divas) is observed every year on:",
     ["26 November", "26 January", "15 August", "25 June"], 0,
     PYQ + "The Constitution was adopted on 26 Nov 1949; observed as Constitution Day since 2015. 25 June is 'Samvidhan Hatya Diwas' (from 2024)."),
    ("Consider the statements about 'One Nation, One Election':\nI. A high-level committee on simultaneous elections was chaired by former President Ram Nath Kovind.\n"
     "II. The Constitution (129th Amendment) Bill on simultaneous elections was introduced in the Lok Sabha in December 2024 and sent to a Joint Parliamentary Committee.",
     I_II, 2, "Both are correct. The Bill proposes Art. 82A for simultaneous Lok Sabha and Assembly elections."),
    ("Assertion (A): The 42nd Amendment (1976) is called the 'Mini-Constitution'.\nReason (R): It made the largest number of changes to the Constitution, including the Preamble, DPSP and Fundamental Duties.",
     AR, 0, "It was based on the Swaran Singh Committee; many changes were reversed by the 43rd and 44th Amendments."),
]

ARTICLES = [
    ("Match List-I with List-II and select the correct answer using the codes given below:\nList-I (Provision)\n(a) Residuary Power of Legislation\n(b) Interstate Council\n"
     "(c) All India Services\n(d) Consolidated Fund of India\nList-II (Article)\n(i) Article 263\n(ii) Article 266\n(iii) Article 312\n(iv) Article 248",
     ["a - iv, b - ii, c - iii, d - i", "a - iii, b - i, c - iv, d - ii", "a - iv, b - i, c - iii, d - ii", "a - iii, b - ii, c - iv, d - i"], 2,
     "Residuary powers – 248 (with the Union); Inter-State Council – 263; All India Services – 312; Consolidated Fund – 266." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q26"),
    ("The constitutional provisions for the 'Census' is mentioned in",
     ["Seventh Schedule, Article 246, Union list", "Seventh Schedule, Article 246, State list", "Sixth Schedule, Article 247, Union list", "Sixth Schedule, Article 247, State list"], 0,
     "Census is entry 69 of the Union List; the next census (2027) is the first digital census and includes caste enumeration." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q48"),
    ("How many Schedules does the Constitution of India have now?",
     ["12", "8", "10", "14"], 0, PYQ + "Originally 8; 9th (1951), 10th (1985), 11th and 12th (1992) were added."),
    ("How many languages are now in the Eighth Schedule?",
     ["22", "18", "14", "24"], 0, "The 92nd Amendment (2003) added Bodo, Dogri, Maithili and Santhali."),
    ("'Education' was shifted from the State List to the Concurrent List by the:",
     ["42nd Amendment", "44th Amendment", "86th Amendment", "7th Amendment"], 0,
     PYQ + "Forests, weights and measures, protection of wild animals and administration of justice were also moved in 1976."),
    ("Match the Parts with their subjects:\na. Part III  b. Part IV  c. Part IVA  d. Part IX\n1. Fundamental Rights  2. Directive Principles  3. Fundamental Duties  4. Panchayats",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Part IXA – municipalities; IXB – co-operative societies."),
    ("Which emergency provision of the Constitution has never been used so far?",
     ["Financial Emergency (Article 360)", "National Emergency (Article 352)", "President's Rule (Article 356)", "Suspension of rights under Article 359"], 0,
     PYQ + "National emergency was declared in 1962, 1971 and 1975."),
    ("The right to privacy was declared a Fundamental Right (part of Article 21) in:",
     ["Justice K.S. Puttaswamy case, 2017", "Maneka Gandhi case, 1978", "Kesavananda Bharati case, 1973", "Minerva Mills case, 1980"], 0,
     "Maneka Gandhi widened 'procedure established by law' to mean fair, just and reasonable procedure."),
    ("'Equality before the law' and 'equal protection of the laws' in Article 14 are borrowed respectively from:",
     ["Britain and the USA", "The USA and Britain", "Ireland and Canada", "France and Australia"], 0, PYQ + "Equality before law is a negative concept; equal protection a positive one."),
    ("Article 1 of the Constitution says:",
     ["India, that is Bharat, shall be a Union of States", "India is a sovereign socialist secular democratic republic", "India shall be a federation of states",
      "Hindi shall be the national language"], 0, "The words 'Union of States' show that states have no right to secede."),
    ("Under Article 3, a new state can be formed by:",
     ["Parliament by a simple-majority law, on the President's recommendation", "A constitutional amendment with ratification by half the states",
      "The President's order alone", "A referendum in the region"], 0, PYQ + "The President refers the bill to the affected state legislature for its views, which are not binding."),
    ("Which Fundamental Duty asks citizens to develop the scientific temper, humanism and the spirit of inquiry and reform?",
     ["Article 51A(h)", "Article 51A(a)", "Article 51A(g)", "Article 51A(k)"], 0, "51A(g) – protect the environment; 51A(k) – education of children 6–14."),
    ("Under Article 343, the official language of the Union is:",
     ["Hindi in Devanagari script (with international numerals)", "English", "Hindi and English equally", "All Eighth Schedule languages"], 0,
     PYQ + "The Official Languages Act, 1963 allows English to continue for official purposes."),
    ("The pardoning power of the President and of the Governor are under:",
     ["Articles 72 and 161", "Articles 74 and 163", "Articles 123 and 213", "Articles 52 and 153"], 0,
     "Only the President can pardon a death sentence and sentences by court-martial."),
    ("Special provisions for the National Capital Territory of Delhi are in:",
     ["Article 239AA", "Article 370", "Article 371J", "Article 244"], 0, PYQ + "Added by the 69th Amendment (1991)."),
    ("Article 371J, giving special provisions for the Hyderabad-Karnataka (Kalyana Karnataka) region, was inserted by the:",
     ["98th Amendment, 2012", "73rd Amendment, 1992", "86th Amendment, 2002", "101st Amendment, 2016"], 0,
     "It led to the Kalyana Karnataka Region Development Board and local reservation in jobs and education for the region."),
    ("Which Article provides for State Election Commissions to conduct panchayat elections?",
     ["Article 243K", "Article 243I", "Article 324", "Article 280"], 0, PYQ + "243I – State Finance Commission; 243D – reservation in panchayats."),
    ("Consider the statements:\nI. Part XX of the Constitution has only one Article.\nII. A constitutional amendment bill can be introduced only in the Lok Sabha.",
     I_II, 0, "II is wrong: an amendment bill can be introduced in either House, by a minister or a private member, and needs no prior permission of the President."),
    ("Assertion (A): The Rajya Sabha is called the Council of States.\nReason (R): Its members are elected by the elected members of state Legislative Assemblies.",
     AR, 0, "Indirect election by MLAs makes it represent the states."),
    ("Match the constitutional posts with their Articles:\na. Election Commission  b. CAG  c. UPSC  d. Attorney General\n1. 324  2. 148  3. 315  4. 76",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Finance Commission – 280; Advocate General – 165."),
]

TOPICS = {
    "Indian Constitution": [
        ("1 · Constitutional Amendments and Recent Developments", AMENDMENTS),
        ("2 · Important Articles, Parts and Schedules", ARTICLES),
    ],
}

NOTES = {
    "Indian Constitution": [
        {"title": "Constitution – amendments, articles and schedules (in the news)", "md": """## 1. Key amendments
| No. | Year | Change |
|---|---|---|
| 1st | 1951 | 9th Schedule (land reforms) |
| 7th | 1956 | states reorganised |
| 42nd | 1976 | 'Mini-Constitution' – socialist, secular, integrity; Fundamental Duties; tribunals; education to Concurrent List |
| 44th | 1978 | property → 300A; 'armed rebellion'; Arts 20, 21 never suspended |
| 52nd | 1985 | Anti-defection (10th Schedule) |
| 61st | 1988 | voting age 21 → 18 |
| 71st | 1992 | Konkani, Manipuri, Nepali in 8th Schedule |
| 73rd / 74th | 1992 | Panchayats (Part IX, 11th Sch) / Municipalities (IXA, 12th Sch) |
| 86th | 2002 | Art. 21A RTE; 11th Fundamental Duty |
| 89th | 2003 | separate NCST (338A) |
| 91st | 2003 | ministers ≤ 15%; split exception removed |
| 92nd | 2003 | Bodo, Dogri, Maithili, Santhali (22 languages) |
| 97th | 2011 | Co-operative societies (19(1)(c), 43B, Part IXB) |
| 98th | 2012 | Art. 371J – Hyderabad-Karnataka |
| 99th | 2014 | NJAC – struck down 2015 |
| 101st | **2016** | GST; GST Council 279A (GST from 1 Jul 2017) |
| 102nd | 2018 | NCBC – 338B |
| 103rd | 2019 | 10% EWS |
| 104th | 2020 | SC/ST reservation +10 yrs; Anglo-Indian nomination ended |
| 105th | 2021 | states' SEBC lists restored |
| 106th | 2023 | Nari Shakti Vandan – 1/3 women in LS & Assemblies (after census + delimitation, 15 yrs) |

## 2. In the news
- Art. 370 inoperative Aug 2019; SC upheld Dec 2023; J&K, Ladakh UTs from 31 Oct 2019
- One Nation One Election – Kovind committee; 129th Amendment Bill (Dec 2024) → JPC
- Special Intensive Revision (SIR) of electoral rolls by ECI – not annual, no state consent needed
- Census 2027 – first digital census, with caste enumeration; census = Union List entry 69
- Constitution Day 26 Nov (since 2015); Samvidhan Hatya Diwas 25 June (from 2024)

## 3. Important Articles
| Art. | Subject | Art. | Subject |
|---|---|---|---|
| 1 | Union of States | 3 | new states |
| 14 | equality | 21 | life, liberty (privacy – Puttaswamy 2017) |
| 32 | constitutional remedies | 40 | village panchayats |
| 44 | UCC | 51A | duties (h – scientific temper) |
| 72 / 161 | pardon | 76 / 165 | AG / Advocate General |
| 110 | Money Bill | 123 / 213 | ordinances |
| 148 | CAG | 239AA | Delhi |
| 243D / I / K | reservation / SFC / SEC | 248 | residuary powers |
| 263 | Inter-State Council | 266 | Consolidated Fund |
| 280 | Finance Commission | 279A | GST Council |
| 312 | All India Services | 315 | PSCs |
| 324 | Election Commission | 343 | Hindi official language |
| 352/356/360 | emergencies | 368 | amendment (Part XX) |
| 371J | Kalyana Karnataka | | |

## 4. Parts and schedules
- 12 Schedules; Part III FR, IV DPSP, IVA duties, IX panchayats, IXA municipalities, IXB co-operatives, XIVA tribunals, XX amendment
- Second Schedule (salaries) changes are not 'amendments' under Art. 368

## ⚠ Traps
- 101st Amendment passed in 2016, not 2015
- Tulu is NOT in the 8th Schedule (demand pending)
- Financial emergency (360) has never been used
"""}],
}
