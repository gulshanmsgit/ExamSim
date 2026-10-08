"""Paper 1 · Current Affairs · planner topic P1-CA-09 Monuments and National Forests (2 sub-topics × 20), with detailed notes (NOTES).
Sources: UNESCO World Heritage list, ASI, MoEFCC / NTCA (tiger reserves), Ramsar Convention site list, Karnataka Forest Department,
NCERT / KTBS history texts. Most questions are REAL previous-year questions from the KEA 2026 GK papers, VAO 2024, PSI 2023–24,
Legislative Council 2024 Paper-1, GTTC 2024 GK (official KEA key), KRIES entrance tests and a UPSC-coaching entrance test (answers
worked out by ExamSim unless marked official). Counts that change often (Ramsar sites, tiger reserves) are given 'as of 2025' in the
notes and kept out of the questions."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

MONUMENTS = [
    ("Among the following monuments, which is not built by Ibrahim Adil Shah II?",
     ["Ibrahim Roza", "Mehtar Mahal", "Navarasapura", "Jami Masjid at Vijayapur"], 3,
     "The Jami Masjid of Vijayapura was begun by Ali Adil Shah I (c. 1576); Ibrahim Roza, Mehtar Mahal and the town of Navaraspur belong to Ibrahim Adil Shah II." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q5"),
    ("Consider the following statements regarding Kailasanatha temple of Ellora.\nStatements:\n(a) A cave temple built by huge monolith\n(b) It is in Ahamadnagar district of Maharashtra\n(c) It was built by the king Krishna-I\nChoose the correct answer from the options given below.",
     ["Statements (a) and (b) are true", "Statements (a) and (c) are true", "Statements (b) and (c) are true", "Statements (a), (b) and (c) are true"], 1,
     "Cave 16 at Ellora was carved from one rock by the Rashtrakuta king Krishna I (8th century); Ellora is in Chhatrapati Sambhajinagar (Aurangabad) district." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q23"),
    ("Where is Chand Minar?",
     ["Delhi", "Doulatabad", "Ghaziabad", "Hyderabad"], 1,
     "Chand Minar (1435) at Daulatabad fort was built by Alauddin Bahman Shah of the Bahmani kingdom." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q27"),
    ("Kutub Minar is located in",
     ["Delhi", "Mumbai", "Kolkata", "Chennai"], 0,
     "Begun by Qutbuddin Aibak and completed by Iltutmish; it is a UNESCO World Heritage Site (1993)." + NOTE, "KRIES 2026 entrance · Q89"),
    ("Consider the following statements about the Virupaksha Temple at Pattadakallu:\na. This temple is also known as Trilokeshwara Temple.\nb. It was built to commemorate the victory of Vikramaditya II over Kanchi.\nc. The architects of the temple were Sarvasiddhi Achari and Gunda.\nd. The temple was built by Triloka Mahadevi.\nHow many of the above statement(s) is/are correct?",
     ["Only one statement is correct", "Only two statements are correct", "Only three statements are correct", "All four statements are correct"], 1,
     "Queen Lokamahadevi built the Virupaksha (Lokeshwara) temple to mark Vikramaditya II's victory over the Pallavas of Kanchi; her sister Trailokyamahadevi built the Mallikarjuna (Trailokeshwara) temple. Inscriptions name Gunda (Sarvasiddhi Achari) as architect – so b and c are correct." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q29"),
    ("Match the following:\nList-I\na. Ekakuta temple\nb. Dwikuta temple\nc. Trikuta temple\nd. Chaturkuta temple\nList-II\ni. Kesava temple of Somanathapura\nii. Lakshmidevi temple of Doddagaddavalli\niii. Chennakeshava temple of Belur\niv. Hoysaleshwara temple of Halebidu\nChoose the answer from the following codes :",
     ["a – iii, b – iv, c – ii, d – i", "a – iv, b – i, c – iii, d – ii", "a – ii, b – iv, c – i, d – iii", "a – iii, b – iv, c – i, d – ii"], 3,
     "Belur – single shrine; Halebidu – twin shrines; Somanathapura – three shrines; Doddagaddavalli – four shrines." + NOTE, "UPSC coaching entrance 2026 (HK) · Q84"),
    ("The Gol Gumbaz at Vijayapura, famous for its whispering gallery, is the tomb of:",
     ["Mohammed Adil Shah", "Ibrahim Adil Shah II", "Yusuf Adil Shah", "Ali Adil Shah I"], 0, PYQ + "It was completed in 1656 and has one of the largest domes in the world."),
    ("The Charminar at Hyderabad was built in 1591 by:",
     ["Muhammad Quli Qutb Shah", "Aurangzeb", "Mahmud Gawan", "Alauddin Khalji"], 0, "Mahmud Gawan built the madrasa at Bidar."),
    ("The 57-foot monolithic statue of Gommateshwara (Bahubali) at Shravanabelagola was installed in 983 CE by:",
     ["Chavundaraya, minister of the Western Gangas", "Vishnuvardhana", "Krishnadevaraya", "Pulakeshi II"], 0, PYQ + "The Mahamastakabhisheka is held about every 12 years (last in 2018)."),
    ("The Hoysala temples of Belur, Halebidu and Somanathapura were inscribed together as a UNESCO World Heritage Site in:",
     ["2023", "1986", "2012", "2004"], 0, "Hampi (1986) and Pattadakal (1987) are Karnataka's other cultural World Heritage Sites."),
    ("The Sun Temple at Konark was built by:",
     ["Narasimhadeva I of the Eastern Ganga dynasty", "Rajaraja Chola I", "Ashoka", "Harsha"], 0, PYQ + "It is designed as a huge chariot with 24 wheels."),
    ("The Brihadeeswara temple at Thanjavur was built by:",
     ["Rajaraja Chola I", "Narasimhavarman I", "Krishnadevaraya", "Pulakeshi II"], 0, "It is part of the 'Great Living Chola Temples' World Heritage Site."),
    ("The Buland Darwaza at Fatehpur Sikri was built by Akbar to commemorate his victory over:",
     ["Gujarat", "Bengal", "Kashmir", "Ahmednagar"], 0, PYQ + "Fatehpur Sikri was Akbar's capital for about 14 years."),
    ("Which was the most recent Indian site to be added to the UNESCO World Heritage list (July 2025)?",
     ["Maratha Military Landscapes of India", "Moidams of Assam", "Santiniketan", "Hoysala temples"], 0, "The 12 forts include Raigad, Shivneri and Gingee; Moidams were added in 2024."),
    ("Mysuru Palace in its present form (completed 1912) was designed by the British architect:",
     ["Henry Irwin", "Edwin Lutyens", "George Wittet", "Robert Chisholm"], 0, PYQ + "Lutyens designed much of New Delhi; Wittet designed the Gateway of India."),
    ("Consider the statements:\nI. Hampi was the capital of the Vijayanagara empire.\nII. The stone chariot at Hampi is in the Vittala temple complex.",
     I_II, 2, "Both are correct; the stone chariot is a Garuda shrine."),
    ("Assertion (A): Humayun's Tomb is regarded as a forerunner of the Taj Mahal.\nReason (R): It was the first garden-tomb on the Indian subcontinent built on a large scale.",
     AR, 0, "It was commissioned by his widow Hamida Banu (Bega) Begum in 1565."),
    ("Assertion (A): The Vidhana Soudha in Bengaluru was built during the Wodeyar rule.\nReason (R): The Vidhana Soudha houses the Karnataka legislature.",
     AR, 3, "It was built in 1956 under Chief Minister Kengal Hanumanthaiah."),
    ("Match:\na. Ibrahim Roza  b. Charminar  c. Buland Darwaza  d. Red Fort (Delhi)\n1. Vijayapura  2. Hyderabad  3. Fatehpur Sikri  4. Shah Jahan",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Monument matching is very common."),
    ("The Sanchi Stupa, a UNESCO World Heritage Site, is in the state of:",
     ["Madhya Pradesh", "Bihar", "Uttar Pradesh", "Odisha"], 0, "It was built by Ashoka and enlarged under the Shungas; the gateways (toranas) date from the Satavahana period."),
]

FORESTS = [
    ("Kumbhalgarh Wildlife Sanctuary which has been declared as Eco-Sensitive Zone by MoEFCC recently is located in the state of",
     ["Tamil Nadu", "Telangana", "Odisha", "Rajasthan"], 3,
     "It lies in the Aravalli hills around Kumbhalgarh fort (a World Heritage hill fort)." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q85"),
    ("Which wildlife sanctuary has recently become a natural home for Asiatic Lions through dispersal?",
     ["Barda Wildlife Sanctuary", "Gandhi Sagar Sanctuary", "Banni Grasslands", "Kuno National Park"], 0,
     "Lions from Gir moved naturally into Barda (Porbandar–Devbhumi Dwarka, Gujarat) in 2023–25; it is being developed as a second home for them." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q89"),
    ("Bonal Bird Sanctuary is located in which of the following districts?",
     ["Kalburgi", "Bidar", "Yadgir", "Raichur"], 2,
     "Bonal tank near Shorapur (Surpur) in Yadgir district is one of Karnataka's largest bird sanctuaries." + NOTE, "PSI 2023 General Paper · Q36"),
    ("Match List-I with List-II and select the correct answer using the codes given below:\nList-I (Tiger Reserve)\na) Dudhwa\nb) Bandipur\nc) Periyar\nd) Sariska\nList-II (State)\ni. Kerala\nii. Rajasthan\niii. Karnataka\niv. Uttar Pradesh",
     ["a – iii, b – iv, c – ii, d – i", "a – iv, b – iii, c – ii, d – i", "a – iv, b – iii, c – i, d – ii", "a – iii, b – iv, c – i, d – ii"], 2,
     "Dudhwa – UP; Bandipur – Karnataka; Periyar – Kerala; Sariska – Rajasthan." + KEY, "GTTC 2024 Asst Gr-II GK · Q70"),
    ("Consider the following statements about National Parks of Karnataka and choose the correct options given below:\na) The Moyar river passes through the southern part of Bandipur National Park.\nb) Bannerghatta National Park is a part of wildlife corridor for elephants which connects the B.R. Hills and Sathyamangalam forests.\nc) The Kudremukh National Park is spread over Dakshina Kannada, Udupi and Chikkamagaluru districts of Karnataka.\nd) The unique feature of Nagarahole National Park is that it is the only habitat in Asia where 'Black Panther' is found.",
     ["a, b and c are correct", "b, c and d are correct", "a, b and d are correct", "only a and b are correct"], 0,
     "Black panthers (melanistic leopards) are seen in Nagarahole–Kabini but also in Dandeli and other forests of Asia, so (d) is wrong." + NOTE,
     "PSI 2024 General Paper · Q33"),
    ("Which of the following places from Karnataka are already declared as Ramsar sites?\na) Magadi Kere Conservation Reserve\nb) Ankasamudra Bird Conservation Reserve\nc) Aghanashini Estuary\nd) Ranganathittu Bird Sanctuary\nOptions:",
     ["All of them", "a, b and c only", "a, b and d only", "b, c and d only"], 0,
     "Ranganathittu became Karnataka's first Ramsar site in 2022; Magadi Kere (Gadag), Ankasamudra (Vijayanagara) and Aghanashini (Uttara Kannada) followed in August 2024." + NOTE,
     "Legislative Council 2024 Asst/Computer Operator P1 · Q26"),
    ("Which of the following Ramsar sites were recently added on the eve of Independence Day 2024?\na) Nanjarayan Bird Sanctuary\nb) Kazhuveli Bird Sanctuary\nc) Sharavathi Kandla Mangrove\nd) Tawa Reservoir\nChoose the correct answer from the options given below:",
     ["Only a and b", "Only a, b and c", "Only a, b and d", "a, b, c and d"], 2,
     "Nanjarayan and Kazhuveli (Tamil Nadu) and Tawa Reservoir (Madhya Pradesh) were added on 13–14 August 2024; 'Sharavathi Kandla mangrove' is not a Ramsar site." + NOTE,
     "VAO 2024 Paper-1 · Q32"),
    ("Which of the following pairs are correct regarding tiger reserve forests of India?\n(i) Kaval - Telangana\n(ii) Bore - Maharashtra\n(iii) Pench - Madhya Pradesh\n(iv) Kanha - Uttar Pradesh\nCodes:",
     ["(i), (ii) and (iii) correct", "(ii), (iii) and (iv) correct", "(i), (ii) and (iv) correct", "(ii) and (iii) correct"], 0,
     "Kanha is in Madhya Pradesh, not Uttar Pradesh. Pench has reserves in both MP and Maharashtra." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q40"),
    ("What was the movement started by Panduranga Hegde in Karnataka to prevent deforestation in Western Ghats which has rich biodiversity?",
     ["Chipko Movement", "The Jungle Bachao Movement", "Appiko Movement", "Gokak Movement"], 2,
     "Appiko ('hug') began in 1983 at Salkani, Uttara Kannada, inspired by Chipko." + NOTE, "KRIES 2025 entrance · Q87"),
    ("India's first national park, set up in 1936 as Hailey National Park, is now called:",
     ["Jim Corbett National Park", "Kaziranga National Park", "Gir National Park", "Bandipur National Park"], 0, PYQ + "It is in Uttarakhand and is where Project Tiger was launched in 1973."),
    ("Project Tiger was launched in:",
     ["1973", "1972", "1992", "2006"], 0, "The Wildlife (Protection) Act came in 1972; Project Elephant in 1992; NTCA was set up in 2006."),
    ("Kaziranga National Park, famous for the one-horned rhinoceros, is in:",
     ["Assam", "West Bengal", "Odisha", "Kerala"], 0, PYQ + "It is a UNESCO natural World Heritage Site (1985)."),
    ("The only natural habitat of the Asiatic lion in the wild (apart from its recent dispersal areas) is:",
     ["Gir, Gujarat", "Sundarbans", "Ranthambore", "Nagarahole"], 0, "Cheetahs were reintroduced at Kuno National Park, MP, in 2022."),
    ("The national park in Karnataka created close to Bengaluru city, with a butterfly park and safari, is:",
     ["Bannerghatta National Park", "Kudremukh National Park", "Anshi National Park", "Nagarahole National Park"], 0, PYQ + "It was declared a national park in 1974."),
    ("Which tiger reserve of Karnataka lies in the Biligirirangana hills of Chamarajanagar district?",
     ["BRT (Biligiri Ranganathaswamy Temple) Tiger Reserve", "Bhadra Tiger Reserve", "Kali Tiger Reserve", "Nagarahole Tiger Reserve"], 0, "Karnataka's five tiger reserves: Bandipur, Nagarahole, Bhadra, Kali (Dandeli–Anshi) and BRT."),
    ("Ranganathittu Bird Sanctuary, on islets of the Kaveri river, is in:",
     ["Mandya district (near Srirangapatna)", "Shivamogga district", "Yadgir district", "Uttara Kannada district"], 0, PYQ + "Salim Ali persuaded the Mysore ruler to protect it in 1940."),
    ("Consider the statements:\nI. The Sundarbans is the largest mangrove forest in the world and has Royal Bengal tigers.\nII. The Western Ghats is a natural UNESCO World Heritage Site.",
     I_II, 2, "Both are correct; the Western Ghats were inscribed in 2012."),
    ("Assertion (A): Biosphere reserves conserve more species than a zoo or botanical garden.\nReason (R): Biosphere reserves protect whole ecosystems in their natural state, with core, buffer and transition zones.",
     AR, 0, "The Nilgiri Biosphere Reserve (1986) was India's first."),
    ("Assertion (A): The Ramsar Convention deals with the protection of tigers.\nReason (R): The Ramsar Convention (1971) is an international treaty for the conservation of wetlands.",
     AR, 3, "Ramsar is about wetlands; tigers come under Project Tiger and NTCA."),
    ("Match:\na. Kaziranga  b. Gir  c. Keoladeo  d. Periyar\n1. One-horned rhinoceros  2. Asiatic lion  3. Birds (Bharatpur)  4. Elephants and tigers, Kerala",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Park–species matching is common."),
]

TOPICS = {
    "Monuments and National Forests": [("1 · Monuments and World Heritage Sites", MONUMENTS),
                                       ("2 · National Parks, Sanctuaries, Tiger Reserves and Wetlands", FORESTS)],
}

NOTES = {
    "Monuments and National Forests": [{"title": "Monuments, national parks and forests – detailed notes", "md": """# Monuments and national forests

## 1. UNESCO World Heritage Sites in India
India has **44** sites (as of July 2025): 35 cultural, 7 natural, 1 mixed + the latest addition.
| Recent additions | Year |
|---|---|
| **Maratha Military Landscapes of India** (12 forts – Raigad, Shivneri, Pratapgad, Gingee …) | **2025** |
| **Moidams** – Ahom mound burials, Charaideo (Assam) | 2024 |
| **Santiniketan** (West Bengal) | 2023 |
| **Sacred Ensembles of the Hoysalas** – Belur, Halebidu, Somanathapura | **2023** |
| Dholavira; Ramappa temple (Telangana) | 2021 |
**Karnataka:** **Hampi** (1986), **Pattadakal** (1987), **Hoysala temples** (2023), **Western Ghats** (natural, 2012, shared).
**Natural sites:** Kaziranga, Manas, Keoladeo (Bharatpur), Sundarbans, Nanda Devi & Valley of Flowers, Western Ghats, Great Himalayan NP. **Mixed:** Khangchendzonga (Sikkim).

## 2. Monuments and their builders
| Monument | Place | Built by / facts |
|---|---|---|
| **Sanchi Stupa** | Madhya Pradesh | **Ashoka**; enlarged under Shungas; toranas – Satavahana period |
| **Kailasanatha (Cave 16), Ellora** | Chhatrapati Sambhajinagar dist., Maharashtra | **Krishna I** (Rashtrakuta) – carved from one rock |
| **Virupaksha, Pattadakal** | Bagalkot | Queen **Lokamahadevi** – Vikramaditya II's victory over Kanchi; architect **Gunda** (Sarvasiddhi Achari). Mallikarjuna (Trailokeshwara) – Queen Trailokyamahadevi |
| **Gommateshwara** | Shravanabelagola | **Chavundaraya** (983 CE), 57 ft monolith |
| **Brihadeeswara** | Thanjavur | **Rajaraja Chola I** (1010) |
| **Konark Sun Temple** | Odisha | **Narasimhadeva I** (Eastern Ganga), 13th c. |
| **Chennakeshava, Belur** | Hassan | **Vishnuvardhana** (1117) – **ekakuta** (single shrine) |
| **Hoysaleshwara, Halebidu** | Hassan | **dvikuta** (twin shrines) |
| **Kesava, Somanathapura** | Mysuru | Somanatha (general of Narasimha III), 1268 – **trikuta** |
| Lakshmidevi, Doddagaddavalli | Hassan | **chatushkuta** (four shrines) |
| **Qutub Minar** | Delhi | **Qutbuddin Aibak**, completed by **Iltutmish** |
| **Chand Minar** | **Daulatabad** | Alauddin Bahman Shah (1435) |
| Mahmud Gawan's Madrasa | Bidar | Mahmud Gawan (1472) |
| **Jami Masjid, Vijayapura** | Vijayapura | **Ali Adil Shah I** |
| **Ibrahim Roza**, Mehtar Mahal, Navaraspur | Vijayapura | **Ibrahim Adil Shah II** |
| **Gol Gumbaz** | Vijayapura | **Mohammed Adil Shah** (1656) – whispering gallery |
| **Charminar** | Hyderabad | **Muhammad Quli Qutb Shah** (1591) |
| **Humayun's Tomb** | Delhi | Hamida Banu (Bega) Begum (1565) – forerunner of the Taj |
| **Fatehpur Sikri, Buland Darwaza** | UP | **Akbar** – Buland Darwaza for the Gujarat victory |
| **Taj Mahal, Red Fort, Jama Masjid (Delhi)** | Agra / Delhi | **Shah Jahan** |
| **Gateway of India** | Mumbai | George Wittet (1924) |
| **Mysuru Palace** | Mysuru | Henry Irwin (1912) |
| **Vidhana Soudha** | Bengaluru | Kengal Hanumanthaiah (1956) |

## 3. Protected areas – basics
- **Wildlife (Protection) Act 1972**; **Project Tiger 1973** (launched at Jim Corbett); **Project Elephant 1992**; **NTCA 2006**.
- India has about **106 national parks**, **570+ wildlife sanctuaries** and **58 tiger reserves** (2025; Madhav, MP – 58th).
- First national park: **Hailey NP (1936) → Jim Corbett**, Uttarakhand.
- **Biosphere reserves** (UNESCO MAB): core, buffer, transition zones; first – **Nilgiri (1986)**, spanning Karnataka, Kerala and Tamil Nadu.
- **Ramsar Convention (1971, Iran)** – wetlands; India's count crossed **90** in 2025. First Indian sites: Chilika and Keoladeo (1981).

## 4. Famous parks and their species
| Park | State | Known for |
|---|---|---|
| **Kaziranga** | Assam | **One-horned rhino** (World Heritage) |
| **Gir** | Gujarat | **Asiatic lion** (natural dispersal to **Barda WLS**, Porbandar) |
| **Kuno** | Madhya Pradesh | **Cheetah reintroduction (2022)** |
| **Keoladeo (Bharatpur)** | Rajasthan | Birds (Siberian crane) |
| **Sundarbans** | West Bengal | Mangroves, Royal Bengal tiger |
| **Periyar** | Kerala | Elephants, tigers |
| Dudhwa / Sariska / Ranthambore | UP / Rajasthan / Rajasthan | Tigers |
| Kanha, Pench, Bandhavgarh | Madhya Pradesh | Tigers (Kanha – barasingha) |
| Kaval / Bor | Telangana / Maharashtra | Tiger reserves |
| **Kumbhalgarh WLS** | Rajasthan | Eco-sensitive zone, Aravallis |

## 5. Karnataka
- **National parks (5):** **Bandipur**, **Nagarahole (Rajiv Gandhi)**, **Bannerghatta** (1974), **Kudremukh** (DK, Udupi, Chikkamagaluru), **Anshi** (now part of Kali TR).
- **Tiger reserves (5):** Bandipur, Nagarahole, **Bhadra**, **Kali (Dandeli–Anshi)**, **BRT (Biligiri Ranganathaswamy Temple)**.
- **Moyar river** – southern boundary of Bandipur; Bannerghatta – elephant corridor towards BR Hills / Sathyamangalam.
- **Bird sanctuaries:** **Ranganathittu** (Mandya), Kokkare Bellur (Mandya), Gudavi (Shivamogga), **Bonal** (Yadgir), Attiveri (Uttara Kannada), Mandagadde (Shivamogga).
- **Ramsar sites (4):** **Ranganathittu (2022)**, **Magadi Kere** (Gadag), **Ankasamudra** (Vijayanagara), **Aghanashini estuary** (Uttara Kannada) – Aug 2024.
- **Appiko movement** (1983, Salkani, Uttara Kannada) – **Panduranga Hegde**; inspired by **Chipko** (Sunderlal Bahuguna, Uttarakhand).
- 'Vriksha Mate' **Saalumarada Thimmakka**; **Tulsi Gowda** – 'Encyclopedia of the Forest' (Padma Shri 2020).

## 6. Traps
- Kanha is in **MP**, not UP; Pench is in both MP and Maharashtra.
- **Chand Minar** – Daulatabad; **Charminar** – Hyderabad; **Qutub Minar** – Delhi.
- Gol Gumbaz – **Mohammed** Adil Shah; Ibrahim Roza – **Ibrahim** Adil Shah II; Jami Masjid (Vijayapura) – **Ali** Adil Shah I.
- Ellora is in **Chhatrapati Sambhajinagar (Aurangabad)** district, not Ahmednagar.
- Ramsar = **wetlands**, not tigers.
"""}],
}
