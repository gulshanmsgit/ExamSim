"""Paper 1 · Current Affairs · planner topic P1-CA-15 Abbreviations (2 sub-topics × 20), with detailed notes (NOTES).
Sources: PIB scheme pages, Union and Karnataka budget documents, ministry websites. REAL previous-year questions come from GTTC 2024 GK
and the Legislative Council 2024 Programmer Paper 1 (official KEA keys), and from the KEA 2025–26 GK papers, PSI 2023/2024, VAO 2024,
KSET 2024, KRIES 2025, PGCET 2023, the Legislative Council 2024 Asst/Computer Operator and Data Entry Paper 1 and UPSC-coaching tests
(answers worked out by ExamSim and marked so). Computer abbreviations are in P1-GK-18 Basics of Computers."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
KLC = " (Official answer: KEA final key, Legislative Council Secretariat exam 2024.)"
GTTC = " (Official answer: KEA final key, GTTC recruitment 2024.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

SCHEMES_BODIES = [
    ("Expand VB-G RAM G",
     ["Viksit Bharat - Gram Rozgar Ajeevika Mission (Guarantee)", "Viksit Bharat - Gramin Rozgar Ajeevika Mission (Guarantee)",
      "Viksit Bharat - Guarantee for Rozgar and Ajeevika Mission (Gramin)", "Viksit Bharat - Guarantee for Rural Ajeevika Mission (Gramin)"], 2,
     "The VB-G RAM G Act (December 2025) replaced MGNREGA and raised the work guarantee to 125 days." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q39"),
    ("Expand SMILE",
     ["Support for Medium Industries for Livelihood and Enterprise", "Smart Management of Intelligence and Leadership Efforts",
      "Support for Marginalized Individuals for Livelihood and Enterprise", "Support for Marginalized Individuals for Livelihood and Employment"], 2,
     "SMILE (2022, Ministry of Social Justice) supports transgender persons and people engaged in begging." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q13"),
    ("Expand HRIDAY",
     ["Harbour City Development and Approved Yojana", "Heritage City Development and Augmentation Yojana", "Heritage City Development and Assurance Yojana", "Huge Canal Development and Augmentation Yojana"], 1,
     "HRIDAY (2015) developed heritage cities; Badami was among its first 12 cities." + NOTE, "PSI 2023 General Paper · Q69"),
    ("The Union Budget, 2025 introduced SWAMIH 2.0. Expand SWAMIH.",
     ["Special Window for Affordable and Mid-Income Housing", "Second Window for Affordable and Mid-Income Housing", "Second World Affordable and Mid-Income Homes", "Special Window for Aged and Mid-Income Housing"], 0,
     "SWAMIH funds stalled housing projects; SWAMIH 2.0 aims to complete about one lakh more homes." + NOTE, "Legislative Council 2024 Asst/Computer Operator P1 · Q85"),
    ("Expand SAPCC",
     ["State Authority Policy on Climate Change", "State Action Plans on Climate Change", "Security Action Plans on Chemical Change", "State Administration Plans on Climate Change"], 1,
     "States prepare SAPCCs in line with the National Action Plan on Climate Change (NAPCC, 2008)." + NOTE, "Legislative Council 2024 Data Entry P1 · Q41"),
    ("Expand MUDRA",
     ["Micro Units Development and Rural Agency", "Micro Units Development and Refinance Agency", "Micro Units Development and Regional Agency", "Micro Units Development and Record Agency"], 1,
     "PM Mudra Yojana (2015) gives Shishu, Kishore, Tarun and Tarun Plus loans." + NOTE, "Legislative Council 2024 Data Entry P1 · Q46"),
    ("Expand KSHIP",
     ["Karnataka State Hospital Improvement Plan", "Karnataka State Highways Improvement Plan", "Karnataka State Human Improvement Programme", "Karnataka State Horticulture Improvement Programme"], 1,
     "KSHIP upgrades state highways with World Bank / ADB help." + GTTC, "GTTC 2024 Asst Gr-II GK · Q57"),
    ("Saumitra Kumar Haldar is the chairman of CWMA. Expand CWMA.",
     ["Canal Water Management Authority", "Cauvery Water Management Authority", "Central Water-Management Authority", "Cauvery Water Maintenance Authority"], 1,
     "The Cauvery Water Management Authority (2018) implements the Supreme Court's Cauvery award; CWRC is its regulation committee." + NOTE, "PSI 2024 General Paper · Q79"),
    ("Recently the Election Commission of India has initiated the delisting of 345 RUPPs. Expand RUPPs.",
     ["Registered Unrecognised Political Parties", "Registered Unauthorised Political Parties", "Registered Unrecognised People's Parties", "Registered Unauthorised People's Parties"], 0,
     "RUPPs that had not contested any election for six years were removed from the list in 2025." + NOTE, "UPSC coaching entrance 2025 (19 Jul) · Q18"),
    ("Expand DILRMP.",
     ["Digital India Labour Records Modernisation Programme", "Digital India Land Records Modernisation Programme", "Digital India Land Reforms Modernisation Programme", "Digital India Land Records Monetary Programme"], 1,
     "DILRMP computerises land records; Karnataka's Bhoomi was a pioneer." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q67"),
    ("Expand NWDPRA:",
     ["National Watershed Development Procedure for Rainfed Areas", "National Watershed Development Programme for Rainfed Areas", "National Watershed Development Project for Rainfed Areas", "Natural Watershed Development Project for Rainfed Areas"], 2,
     "NWDPRA was launched in 1990–91 by the Ministry of Agriculture for rainfed farming areas." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q73"),
    ("Expand PM-SVANidhi",
     ["Prime Minister Street Vendor's Atma Nirbhar Nidhi", "Prime Minister Sainik Vikas Atma Nirbhar Nidhi", "Prime Minister Suraksha Vidhi Atma Nirbhar Nidhi", "Prime Minister Skill Vikas Atma Nirbhar Nidhi"], 0,
     "It gives collateral-free working-capital loans to street vendors (2020)." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q95"),
    ("In India, PCRA advises people to save fuels. The full form of PCRA refers to",
     ["Petroleum Conservation Research Association", "Power Conservation Research Association", "Petroleum Consumption Research Association", "Power Consumption Research Association"], 0,
     "PCRA (1977) works under the Ministry of Petroleum and Natural Gas; it runs the 'Saksham' campaign." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q11"),
    ("NITI in NITI Aayog stands for:",
     ["National Institution for Transforming India", "National Institute for Technology and Innovation", "New India Transformation Initiative", "National Integration and Trade Institute"], 0,
     PYQ + "It replaced the Planning Commission on 1 January 2015."),
    ("PMAY stands for:",
     ["Pradhan Mantri Awas Yojana", "Pradhan Mantri Arogya Yojana", "Pradhan Mantri Anna Yojana", "Prime Minister's Agriculture Yojana"], 0, "It provides housing for all."),
    ("NABARD stands for:",
     ["National Bank for Agriculture and Rural Development", "National Board for Agricultural Research and Development", "National Bank for Agro-Rural Districts", "New Agricultural Bank for Rural Development"], 0,
     PYQ + "It was set up in 1982 on the recommendation of the Shivaraman Committee."),
    ("ISRO stands for:",
     ["Indian Space Research Organisation", "International Space Research Organisation", "Indian Science Research Office", "Indian Satellite Research Organisation"], 0, "Its headquarters is in Bengaluru."),
    ("Consider the statements:\nI. KSRTC stands for Karnataka State Road Transport Corporation.\nII. BMRCL stands for Bangalore Metro Rail Corporation Limited.",
     I_II, 2, "Both are correct."),
    ("Assertion (A): MGNREGA was replaced by the VB-G RAM G Act.\nReason (R): The new law raises the guaranteed days of wage employment in rural areas.",
     AR, 0, "It guarantees 125 days instead of 100."),
    ("Match:\na. NABARD  b. SEBI  c. CAG  d. UPSC\n1. Agriculture and rural credit  2. Securities market regulator  3. Audits government accounts  4. Recruits for all-India services",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Abbreviations with functions."),
]

SCI_ECON = [
    ("'MCB' in an electric circuit stands for",
     ["Master Circuit Breaker", "Miniature Circuit Breaker", "Main Circuit Breaker", "Master Current Breaker"], 1,
     "An MCB automatically switches off the circuit on overload or short circuit." + KLC, "Legislative Council 2024 Programmer P1 · Q53"),
    ("'SONAR' stands for",
     ["Solar navigation and reflection", "Sound over navigation and ranging", "Sound navigation and ranging", "Solar navigation and ranging"], 2,
     "SONAR uses ultrasonic waves to find objects under water." + NOTE, "Legislative Council 2024 Asst/Computer Operator P1 · Q50"),
    ("Expand QR Code:",
     ["Quick Reply code", "Quick Response Code", "Quick Retrace Code", "Quick Reaction Code"], 1, "It was invented by Denso Wave (Japan) in 1994." + NOTE, "KSET 2024 General Paper · Q31"),
    ("Soft drinks beverages are usually stored in PET bottles. Expand PET.",
     ["Poly ethylene terephthalate", "Poly ethyl tolyene", "Propyl ethyl terephthalate", "Phenyl ethanyl terephthalate"], 0,
     "PET is a recyclable polyester (resin code 1)." + NOTE, "PSI 2024 General Paper · Q39"),
    ("Expand HSRP.",
     ["High Speed Registration Place", "High Security Registration Plate", "Heavy Security Registration Place", "High Space Registration Plate"], 1,
     "HSRP number plates are mandatory for vehicles; Karnataka set deadlines for older vehicles in 2024–25." + NOTE, "VAO 2024 Paper-1 · Q38"),
    ("Expand LPG.",
     ["Liquefied Petroleum Gas", "Liquid Petroleum Gas", "Liquid Paraffin Gas", "Liquefied Paraffin Gas"], 0, "It is mainly propane and butane." + NOTE, "KRIES 2025 entrance · Q76"),
    ("With reference to animal breeding, expand MoET",
     ["Multiple Ovary Embryo Transfer technology", "Multiple Ovulation Embryo Transfer technology", "Multiple Ovules Embryo Transfer technology", "Multiple Oogonia Embryo Transfer technology"], 1,
     "MOET is used to multiply high-yielding cattle breeds quickly." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q41"),
    ("What is the full form of ISD which is related to GST?",
     ["Input Service Distributor", "Indian Standard Data", "Income Sales Distributor", "Inter State Delivery"], 0,
     "An ISD distributes input tax credit for common services among its branches." + NOTE, "UPSC coaching entrance 2026 (HK) · Q72"),
    ("Expand 'UPI'.",
     ["United Payment India", "Unified Payment Interface", "Unique Payment Information", "Unified Payment Information"], 1, "UPI was launched by NPCI in 2016." + NOTE, "PGCET 2023 MCA · Q52"),
    ("GDP stands for:",
     ["Gross Domestic Product", "General Domestic Price", "Gross Development Plan", "Government Debt Position"], 0, PYQ + "GNP adds net factor income from abroad."),
    ("GST stands for:",
     ["Goods and Services Tax", "General Sales Tax", "Government Service Tax", "Gross Sales Turnover"], 0, "It came into force on 1 July 2017 (101st Amendment)."),
    ("RBI's 'CRR' stands for:",
     ["Cash Reserve Ratio", "Credit Rate Ratio", "Current Reserve Rate", "Capital Reserve Requirement"], 0, PYQ + "SLR – Statutory Liquidity Ratio."),
    ("LASER stands for:",
     ["Light Amplification by Stimulated Emission of Radiation", "Light Amplified by Simple Emission of Rays", "Laser Action by Stimulated Electron Radiation", "Light Absorption by Stimulated Energy Release"], 0,
     "The first laser was built by Theodore Maiman in 1960."),
    ("RADAR stands for:",
     ["Radio Detection and Ranging", "Radio Distance and Range", "Radiated Detection and Response", "Rapid Detection and Ranging"], 0, PYQ + "It uses radio waves; SONAR uses sound."),
    ("DNA stands for:",
     ["Deoxyribonucleic acid", "Dinitrogen acid", "Deoxyribose nitric acid", "Dual nucleic acid"], 0, "Its double-helix structure was described by Watson and Crick (1953)."),
    ("AIDS stands for:",
     ["Acquired Immuno Deficiency Syndrome", "Acute Immune Disorder Syndrome", "Acquired Infection Disease Syndrome", "Anti Immune Deficiency System"], 0, PYQ + "It is caused by HIV."),
    ("CNG stands for:",
     ["Compressed Natural Gas", "Carbon Natural Gas", "Condensed Nitrogen Gas", "Compressed Nitrogen Gas"], 0, "It is mainly methane."),
    ("Consider the statements:\nI. SONAR uses sound waves.\nII. RADAR uses sound waves.",
     I_II, 0, "RADAR uses radio waves."),
    ("Assertion (A): An MCB protects household wiring.\nReason (R): An MCB trips automatically when excess current flows.",
     AR, 0, "It replaces old rewireable fuses."),
    ("Match:\na. LASER  b. RADAR  c. SONAR  d. LPG\n1. Stimulated emission of radiation  2. Radio detection and ranging  3. Sound navigation and ranging  4. Liquefied petroleum gas",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Science abbreviations."),
]

TOPICS = {
    "Abbreviations": [("1 · Government Schemes, Programmes and Bodies", SCHEMES_BODIES),
                      ("2 · Science, Technology and Economy", SCI_ECON)],
}

NOTES = {
    "Abbreviations": [{"title": "Common abbreviations – detailed notes", "md": """# Abbreviations

## Schemes and programmes
| Short | Full form | Note |
|---|---|---|
| **VB-G RAM G** | Viksit Bharat – **Guarantee for Rozgar and Ajeevika Mission (Gramin)** | Replaced MGNREGA (Dec 2025), 125 days |
| MGNREGA | Mahatma Gandhi National Rural Employment Guarantee Act | 2005 |
| **SMILE** | Support for **Marginalized Individuals** for Livelihood and **Enterprise** | Transgender persons, beggary |
| **HRIDAY** | Heritage City Development and **Augmentation** Yojana | 2015 |
| **SWAMIH** | **Special Window** for Affordable and Mid-Income Housing | SWAMIH 2.0 – Budget 2025 |
| **MUDRA** | Micro Units Development and **Refinance** Agency | 2015 |
| **PM-SVANidhi** | PM **Street Vendor's** AtmaNirbhar Nidhi | 2020 |
| **DILRMP** | Digital India **Land Records** Modernisation Programme | |
| **NWDPRA** | National Watershed Development **Project** for Rainfed Areas | 1990–91 |
| **SAPCC** | State **Action Plans** on Climate Change | NAPCC 2008 |
| PMAY / PMJDY / PMKSY | PM Awas / Jan Dhan / Krishi Sinchayee Yojana | |
| AMRUT | Atal Mission for Rejuvenation and Urban Transformation | |
| UDAN | Ude Desh ka Aam Nagrik | Regional air travel |
| SAGAR | Security and Growth for All in the Region | Indian Ocean |
| **KSHIP** | Karnataka State **Highways** Improvement Project | |

## Bodies
| Short | Full form |
|---|---|
| NITI | National Institution for Transforming India |
| NABARD | National Bank for Agriculture and Rural Development (1982) |
| SEBI / CAG / UPSC | Securities and Exchange Board of India / Comptroller and Auditor General / Union Public Service Commission |
| **CWMA** | **Cauvery** Water Management Authority (2018) |
| **PCRA** | **Petroleum Conservation Research** Association |
| **RUPP** | Registered **Unrecognised** Political Party |
| NPCI | National Payments Corporation of India |
| ISRO / DRDO / HAL | Indian Space Research Organisation / Defence Research and Development Organisation / Hindustan Aeronautics Ltd |
| KSRTC / BMRCL / BESCOM | Karnataka State Road Transport Corpn / Bangalore Metro Rail Corpn Ltd / Bangalore Electricity Supply Company |
| KEA / KPSC / DSERT | Karnataka Examinations Authority / Karnataka Public Service Commission / Dept of State Educational Research and Training |

## Science and technology
| Short | Full form |
|---|---|
| LASER | Light Amplification by Stimulated Emission of Radiation |
| RADAR / **SONAR** | Radio Detection and Ranging / **Sound Navigation and Ranging** |
| **MCB** | **Miniature** Circuit Breaker |
| **LPG** / CNG | **Liquefied** Petroleum Gas / Compressed Natural Gas |
| **PET** | **Polyethylene terephthalate** |
| **MOET** | Multiple **Ovulation** Embryo Transfer |
| DNA / RNA | Deoxyribonucleic / Ribonucleic acid |
| AIDS / HIV | Acquired Immuno Deficiency Syndrome / Human Immunodeficiency Virus |
| **QR** | Quick **Response** |
| **HSRP** | High **Security** Registration Plate |
| GPS / GAGAN | Global Positioning System / GPS Aided GEO Augmented Navigation |

## Economy and banking
| Short | Full form |
|---|---|
| GDP / GNP | Gross Domestic / National Product |
| GST / **ISD** | Goods and Services Tax / **Input Service Distributor** |
| CRR / SLR / MSF | Cash Reserve Ratio / Statutory Liquidity Ratio / Marginal Standing Facility |
| **UPI** | **Unified Payments Interface** (NPCI, 2016) |
| NEFT / RTGS / IMPS | National Electronic Funds Transfer / Real Time Gross Settlement / Immediate Payment Service |
| IFSC / KYC | Indian Financial System Code / Know Your Customer |

## Traps
- MUDRA – **Refinance**, not Rural. SWAMIH – **Special** Window. QR – **Response**. HSRP – **Security** Plate.
- VB-G RAM G – "**Guarantee for Rozgar and Ajeevika Mission (Gramin)**".
- SONAR = sound; RADAR = radio.
"""}],
}
