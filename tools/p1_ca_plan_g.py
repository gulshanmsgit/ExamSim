"""Paper 1 · Current Affairs · planner topics P1-CA-10 Important Tourist Places and Peaks and P1-CA-11 Industries and Ores
(2 topics × 2 sub-topics × 20), with detailed notes (NOTES).
Sources: Karnataka Tourism, Survey of India / NCERT Geography (classes 9–11), KTBS Social Science, Indian Bureau of Mines (Indian
Minerals Yearbook), Ministry of Steel and SAIL, Karnataka Industrial Policy 2020-25. REAL previous-year questions come from PSI 2023,
VAO 2024, Legislative Council 2024 Paper-1, GTTC 2024 GK (official KEA key), KRIES entrance tests, GFGC 2021 GK, the KEA 2026 GK
papers and a UPSC-coaching entrance test; answers without an official key were worked out by ExamSim and say so. Questions whose
printed facts were doubtful (e.g. ghats wrongly paired, falls on the wrong rivers) were left out."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

PEAKS = [
    ("Mullayanagiri Hills are located in the ____ ranges of Western Ghats.",
     ["Aravalli", "Chandra Dhrona", "Anaimudi", "Vindhya"], 1,
     "Mullayanagiri (about 1,930 m, Chikkamagaluru) – Karnataka's highest peak – is in the Baba Budan / Chandra Drona range." + NOTE, "PSI 2023 General Paper · Q73"),
    ("Which one of the following is the correct sequence of the given mountain peaks in increasing order of their altitude?",
     ["Mullayyanagiri – Kuduremukh – Tadiandamol – Biligiriranga Hills", "Biligiriranga Hills – Tadiyandamol – Kuduremukh – Mullayyanagiri",
      "Kuduremukh – Biligiriranga Hills – Mullayyanagiri – Tadiyandamol", "Tadiandamol – Mullayyanagiri – Biligiriranga Hills – Kuduremukh"], 1,
     "BR Hills (lowest) < Tadiandamol (~1,748 m) < Kudremukh (~1,894 m) < Mullayanagiri (~1,930 m)." + NOTE,
     "Legislative Council 2024 Asst/Computer Operator P1 · Q18"),
    ("Consider the following peaks in Karnataka.\n(a) Tadiandamol\n(b) Baba Budangiri\n(c) Kudremukha\n(d) Kumara Parvatha\nWhich is the correct sequence from highest to lowest?",
     ["(c), (b), (d) and (a)", "(b), (c), (a) and (d)", "(b), (c), (d) and (a)", "(c), (b), (a) and (d)"], 1,
     "Baba Budangiri (~1,895 m) is marginally higher than Kudremukh (~1,894 m); Tadiandamol (~1,748 m) is above Kumara Parvatha (~1,712 m)." + NOTE,
     "KEA 2026 GK-3 (NHK, 10 May 2026) · Q36"),
    ("____ is the highest peak in India.",
     ["Mullayanagiri", "Anaimudi", "Mount Everest", "Mount Godwin Austen"], 3,
     "India's official answer is K2 (Godwin Austen, 8,611 m) in Gilgit-Baltistan (PoK); Kanchenjunga (8,586 m) is the highest under Indian administration; Everest is in Nepal." + NOTE,
     "KRIES 2024 entrance · Q82"),
    ("____ is the highest peak in the Aravalli Range.",
     ["Nilagiri Hills", "Gurushikara", "Mount Everest", "Kanchenjunga"], 1,
     "Guru Shikhar (about 1,722 m) is near Mount Abu, Rajasthan." + NOTE, "KRIES 2025 entrance · Q91"),
    ("Which is the highest peak in the Western Ghats?",
     ["Agasthyamalai", "Pushpagiri", "Kudremukh", "Anamudi"], 3,
     "Anamudi (2,695 m, Kerala) is the highest peak of the Western Ghats and of India south of the Himalayas." + NOTE, "UPSC coaching entrance 2026 (HK) · Q12"),
    ("Name the hill station situated in Nilgiri hills where, Western Ghats and Eastern Ghats meet.",
     ["Shimla", "Manali", "Kodaikanal", "Udhagamandalam"], 3,
     "Ooty (Udhagamandalam), the 'Queen of hill stations', is in the Nilgiris, the junction of the two ghats; Doddabetta (2,637 m) is nearby." + NOTE,
     "KRIES 2026 entrance · Q91"),
    ("Match the following\nState – Mountain passes\na. Jammu and Kashmir  i) Lipulekh\nb. Himachal Pradesh  ii) Zoji La\nc. Sikkim  iii) Shipki La\nd. Uttarakhand  iv) Jelep La",
     ["a – ii, b – iii, c – iv, d – i", "a – i, b – ii, c – iii, d – iv", "a – iii, b – iv, c – ii, d – i", "a – iv, b – i, c – ii, d – iii"], 0,
     "Zoji La links Srinagar and Ladakh; Shipki La (HP) and Lipulekh (Uttarakhand) lead to Tibet; Jelep La and Nathu La are in Sikkim." + NOTE,
     "Legislative Council 2024 Data Entry P1 · Q19"),
    ("Match the following:\na) Padubidri Beach  i. Gokarna\nb) Half moon Beach  ii. Udupi\nc) Devbagh Beach  iii. Mangaluru\nd) Tannirbhavi Beach  iv. Karwar",
     ["a – i, b – ii, c – iii, d – iv", "a – i, b – ii, c – iv, d – iii", "a – ii, b – i, c – iv, d – iii", "a – ii, b – iv, c – iii, d – i"], 2,
     "Padubidri (Udupi) is a Blue Flag beach; Half Moon beach is at Gokarna; Devbagh near Karwar; Tannirbhavi in Mangaluru." + NOTE, "VAO 2024 Paper-1 · Q49"),
    ("The highest peak located entirely within India's own territory (not on a border) is:",
     ["Nanda Devi", "Kanchenjunga", "K2", "Saramati"], 0, PYQ + "Nanda Devi (7,816 m, Uttarakhand). Kanchenjunga lies on the India–Nepal border."),
    ("The highest peak of the Eastern Ghats is:",
     ["Arma Konda (Jindhagada) in Andhra Pradesh", "Doddabetta", "Mahendragiri in Karnataka", "Anamudi"], 0, "It is about 1,680 m high."),
    ("The highest peak in Kodagu district is:",
     ["Tadiandamol", "Kudremukh", "Mullayanagiri", "Kodachadri"], 0, PYQ + "Pushpagiri and Brahmagiri are other Kodagu peaks."),
    ("Jog Falls, one of India's highest plunge waterfalls, is formed by the river:",
     ["Sharavathi", "Kaveri", "Aghanashini", "Kali"], 0, "Its four streams are Raja, Rani, Roarer and Rocket (about 253 m)."),
    ("Gaganachukki and Bharachukki falls at Shivanasamudra are on the river:",
     ["Kaveri", "Tungabhadra", "Krishna", "Netravati"], 0, PYQ + "The Shivanasamudra hydroelectric station (1902) was one of the first in Asia; it powered the Kolar Gold Fields."),
    ("Gokak Falls in Belagavi district is on the river:",
     ["Ghataprabha", "Malaprabha", "Bhima", "Tunga"], 0, "It is called the 'Niagara of Karnataka'."),
    ("Agumbe in Shivamogga district is known as:",
     ["The 'Cherrapunji of the South' and a rainforest research centre", "The silk city", "The sugar city", "The hottest place in Karnataka"], 0,
     PYQ + "It is famous for king cobras and sunsets."),
    ("Kodagu (Coorg) is popularly called:",
     ["The Scotland of India", "The Switzerland of the South", "The Venice of the East", "The Manchester of the South"], 0, "Madikeri is its headquarters; Abbey Falls is nearby."),
    ("Consider the statements:\nI. Kasarkod and Padubidri in Karnataka have 'Blue Flag' certification.\nII. St Mary's Islands off Malpe are known for columnar basalt rocks.",
     I_II, 2, "Both statements are correct."),
    ("Assertion (A): Anamudi is the highest peak in South India.\nReason (R): Anamudi is in the Nilgiri hills of Tamil Nadu.",
     AR, 2, "Anamudi is in the Anaimalai hills of Kerala; the highest Nilgiri peak is Doddabetta."),
    ("Match:\na. Ooty  b. Darjeeling  c. Kodaikanal  d. Munnar\n1. Tamil Nadu (Nilgiris)  2. West Bengal  3. Tamil Nadu (Palani hills)  4. Kerala",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Hill-station matching is common."),
]

PLACES = [
    ("Karnataka Tourism's slogan is:",
     ["One State, Many Worlds", "God's Own Country", "Incredible India", "Enchanting Tamil Nadu"], 0, PYQ + "'God's Own Country' is Kerala's slogan."),
    ("The Group of Monuments at Hampi lies on the banks of the river:",
     ["Tungabhadra", "Kaveri", "Krishna", "Sharavathi"], 0, "It was the Vijayanagara capital and became a World Heritage Site in 1986."),
    ("The 'Cradle of Indian temple architecture', with about 120 early Chalukya temples, is:",
     ["Aihole", "Belur", "Halebidu", "Hampi"], 0, PYQ + "Aihole, Badami and Pattadakal together show early Chalukya architecture."),
    ("Badami (Vatapi), famous for rock-cut cave temples, was the capital of the:",
     ["Chalukyas of Badami", "Hoysalas", "Rashtrakutas", "Kadambas"], 0, "Pulakeshi II ruled from here."),
    ("Murudeshwar in Uttara Kannada is famous for:",
     ["One of the tallest Shiva statues in the world, by the Arabian Sea", "Gol Gumbaz", "Silk weaving", "Toy making"], 0, PYQ + "Netrani island nearby is a scuba-diving spot."),
    ("Channapatna is famous for:",
     ["Lacquered wooden toys (GI tag)", "Sandalwood carving", "Silk saris", "Bidriware"], 0, "Bidriware comes from Bidar; Ilkal saris from Bagalkot."),
    ("Bidar's Bidriware is made by inlaying silver on an alloy of mainly:",
     ["Zinc and copper", "Iron and nickel", "Gold and silver", "Aluminium and tin"], 0, PYQ + "It has a GI tag."),
    ("Nandi Hills near Chikkaballapur was a summer retreat of:",
     ["Tipu Sultan", "Krishnadevaraya", "Kempegowda", "Shivaji"], 0, "Tipu's Drop is a cliff there; the Arkavathi and Pennar rise nearby."),
    ("The coffee-growing region where Baba Budan is believed to have planted India's first coffee seeds is:",
     ["Chikkamagaluru", "Mandya", "Kalaburagi", "Ballari"], 0, PYQ + "Mullayanagiri and Kemmangundi are nearby."),
    ("Dandeli in Uttara Kannada is popular for:",
     ["White-water rafting on the Kali river and wildlife", "Desert safaris", "Snow skiing", "Salt pans"], 0, "It is part of the Kali Tiger Reserve."),
    ("Gokarna is a pilgrimage and beach town famous for the temple of:",
     ["Mahabaleshwara (Atmalinga)", "Virupaksha", "Chamundeshwari", "Mookambika"], 0, PYQ + "Kollur has the Mookambika temple."),
    ("Srirangapatna, the island capital of Tipu Sultan, is formed by the river:",
     ["Kaveri", "Tunga", "Hemavati", "Lakshmana Tirtha"], 0, "The Daria Daulat Bagh summer palace is there."),
    ("Dudhsagar falls, on the Mandovi river, is on the border of Goa and:",
     ["Karnataka", "Kerala", "Tamil Nadu", "Telangana"], 0, PYQ + "Its name means 'sea of milk'."),
    ("Athirappilly falls, called the 'Niagara of India', is in:",
     ["Kerala", "Karnataka", "Odisha", "Meghalaya"], 0, "It is on the Chalakudy river."),
    ("Nohkalikai falls, one of India's tallest plunge waterfalls, is in:",
     ["Meghalaya", "Sikkim", "Assam", "Arunachal Pradesh"], 0, PYQ + "Cherrapunji and Mawsynram nearby are among the wettest places on Earth."),
    ("The ghat road that connects Chikkamagaluru (Mudigere) with Dakshina Kannada (Ujire) is:",
     ["Charmadi ghat", "Agumbe ghat", "Shiradi ghat", "Sampaje ghat"], 0, "Shiradi links Sakleshpur and Mangaluru; Sampaje links Madikeri and Mangaluru; Agumbe links Shivamogga and Udupi."),
    ("Consider the statements:\nI. Belur and Halebidu are in Hassan district.\nII. Somanathapura is in Mandya district.",
     I_II, 0, "Somanathapura is in Mysuru district (T. Narasipura taluk)."),
    ("Assertion (A): Shravanabelagola is an important Jain pilgrimage centre.\nReason (R): It has the monolithic statue of Gommateshwara (Bahubali).",
     AR, 0, "Chavundaraya installed it in 983 CE."),
    ("Assertion (A): Jog Falls is on the Kaveri river.\nReason (R): Jog Falls is in Shivamogga district.",
     AR, 3, "Jog is on the Sharavathi; R is true (on the Shivamogga – Uttara Kannada border)."),
    ("Match the Karnataka place with what it is known for:\na. Mandya  b. Ramanagara  c. Davanagere  d. Ilkal\n1. Sugar city  2. Silk city  3. 'Manchester of Karnataka' (cotton textiles)  4. Saris",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Nickname matching is common."),
]

ORES = [
    ("Match the metals in List-I with their nature in List-II.\nList-I\n(a) Gold (Au)\n(b) Copper (Cu)\n(c) Magnesium (Mg)\n(d) Lead (Pb)\nList-II\n(i) Never found in free state in nature\n(ii) Chalcocite is its ore\n(iii) Found in earth crust as oxides, sulphides and carbonates\n(iv) Found in free state in nature",
     ["a – iv, b – ii, c – i, d – iii", "a – iv, b – ii, c – iii, d – i", "a – iv, b – iii, c – i, d – ii", "a – iv, b – i, c – iii, d – ii"], 0,
     "Gold is found native; chalcocite (Cu₂S) is a copper ore; magnesium is too reactive to occur free; lead occurs as galena (sulphide), cerussite (carbonate) and oxides." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q7"),
    ("Recently in Mandya, reserves of the following mineral were found:",
     ["Magnesium", "Lithium", "Uranium", "Thorium"], 1,
     "The Atomic Minerals Directorate found lithium at Marlagalla, Mandya (2021); larger reserves were reported in Reasi, J&K, in 2023." + NOTE, "GFGC 2021 GK · Q43"),
    ("Which of the following is a ferrous mineral ?",
     ["Manganese", "Bauxite", "Mica", "Copper"], 0,
     "Ferrous minerals (iron ore, manganese, chromite, nickel) are used in iron and steel; bauxite and copper are non-ferrous; mica is non-metallic." + NOTE,
     "PSI 2023 General Paper · Q90"),
    ("'Kimberly process' recently was in news, which is related to:",
     ["To regulate coal trade", "To regulate the gold trade", "To regulate the diamond trade", "To regulate the milk products"], 2,
     "The Kimberley Process Certification Scheme (2003) stops trade in 'conflict diamonds'; India chaired it in 2019." + KEY, "GTTC 2024 Asst Gr-II GK · Q72"),
    ("India's leading state in the production of iron ore is:",
     ["Odisha", "Kerala", "Punjab", "Bihar"], 0, PYQ + "Chhattisgarh, Karnataka (Ballari–Hosapete–Sandur) and Jharkhand follow."),
    ("Hutti Gold Mines, India's main working gold mine, is in:",
     ["Raichur district, Karnataka", "Kolar district, Karnataka", "Anantapur, Andhra Pradesh", "Singhbhum, Jharkhand"], 0,
     "Kolar Gold Fields, once among the deepest mines in the world, closed in 2001."),
    ("Kudremukh Iron Ore Company Ltd (KIOCL) mined iron ore in:",
     ["Chikkamagaluru district", "Ballari district", "Kalaburagi district", "Bidar district"], 0, PYQ + "Mining stopped in 2005 to protect the Kudremukh National Park."),
    ("The 'mica capital of India' is:",
     ["Koderma (Jharkhand)", "Khetri (Rajasthan)", "Jharia (Jharkhand)", "Talcher (Odisha)"], 0, "Andhra Pradesh (Nellore) and Rajasthan also produce mica."),
    ("Bauxite is the ore of:",
     ["Aluminium", "Iron", "Copper", "Zinc"], 0, PYQ + "Odisha leads in bauxite; NALCO's alumina refinery is at Damanjodi."),
    ("Khetri in Rajasthan and Malanjkhand in Madhya Pradesh are known for:",
     ["Copper", "Gold", "Coal", "Mica"], 0, "Singhbhum in Jharkhand also has copper."),
    ("Jharia coalfield, India's main source of coking coal, is in:",
     ["Jharkhand", "West Bengal", "Odisha", "Chhattisgarh"], 0, PYQ + "Raniganj (West Bengal) was India's first coalfield (1774)."),
    ("Neyveli in Tamil Nadu is known for:",
     ["Lignite (brown coal)", "Gold", "Uranium", "Diamonds"], 0, "NLC India Ltd runs lignite mines and power plants there."),
    ("India's only operating diamond mine is at:",
     ["Panna, Madhya Pradesh", "Kolar, Karnataka", "Golconda, Telangana", "Jaduguda, Jharkhand"], 0, PYQ + "Jaduguda in Jharkhand is known for uranium."),
    ("Hematite and magnetite are ores of:",
     ["Iron", "Aluminium", "Copper", "Lead"], 0, "Hematite is the most widely mined iron ore in India."),
    ("Limestone, the main raw material of cement, is quarried widely in Karnataka around:",
     ["Kalaburagi (Shahabad, Wadi)", "Kodagu", "Udupi", "Chikkaballapur"], 0, PYQ + "Kalaburagi is a major cement belt."),
    ("Consider the statements:\nI. Manganese is used in making steel.\nII. Mica is a good conductor of electricity.",
     I_II, 0, "Mica is an excellent insulator, used in electrical equipment."),
    ("Assertion (A): Lithium is called 'white gold'.\nReason (R): Lithium is in high demand for rechargeable batteries of electric vehicles.",
     AR, 0, "In older texts cotton was also called 'white gold'."),
    ("Assertion (A): Gold occurs only as compounds and is never found in the free state.\nReason (R): Gold is a very unreactive (noble) metal.",
     AR, 3, "Because it is unreactive, gold is found in the native (free) state."),
    ("Match the mineral with a major producing area:\na. Iron ore  b. Bauxite  c. Mica  d. Copper\n1. Ballari–Hosapete  2. Odisha (Koraput)  3. Koderma  4. Khetri",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Mineral–place matching is common."),
    ("India's National Critical Mineral Mission (2025) aims mainly at:",
     ["Securing supplies of minerals such as lithium, cobalt and rare earths", "Exporting all coal", "Closing all mines", "Importing iron ore only"], 0,
     "Critical minerals are needed for batteries, electronics and clean energy."),
]

INDUSTRIES = [
    ("In the beginning, iron & steel industries were coal-based in India, the only exception was",
     ["Kulti", "Jamshedpur", "Bhadravathi", "Burnpur"], 2,
     "The Mysore Iron Works at Bhadravati (1923, now Visvesvaraya Iron and Steel Plant) used charcoal from the nearby forests." + NOTE, "VAO 2024 Paper-1 · Q46"),
    ("The Index of Industrial Production (IIP) is compiled and published every month by whom?",
     ["NSSO", "CSO", "RBI", "Ministry of Industry and Commerce"], 1,
     "The Central Statistics Office (now the National Statistics Office, MoSPI) releases the IIP; its base year is 2011-12." + NOTE, "Legislative Council 2024 Data Entry P1 · Q17"),
    ("India's first large integrated steel plant in the private sector, TISCO, was set up in 1907 at:",
     ["Jamshedpur", "Bhilai", "Rourkela", "Durgapur"], 0, PYQ + "It was founded by Jamsetji Tata's company."),
    ("Match the public-sector steel plant with the country that helped set it up:\na. Bhilai  b. Rourkela  c. Durgapur\n1. Soviet Union  2. West Germany  3. United Kingdom",
     ["a-1, b-2, c-3", "a-2, b-1, c-3", "a-3, b-2, c-1", "a-1, b-3, c-2"], 0, "Bokaro was also built with Soviet help."),
    ("JSW Steel's Vijayanagar works, one of India's largest single-location steel plants, is at:",
     ["Toranagallu, Ballari district", "Bhadravati", "Hubballi", "Raichur"], 0, PYQ + "It uses the iron ore of the Ballari–Sandur region."),
    ("Hindustan Aeronautics Limited (HAL), headquartered in Bengaluru, was founded in 1940 by:",
     ["Walchand Hirachand", "M. Visvesvaraya", "J. R. D. Tata", "G. D. Birla"], 0, "It became a public-sector company after independence."),
    ("Mysore Sandal Soap, made by Karnataka Soaps and Detergents Ltd, was first produced in:",
     ["1916", "1956", "1947", "1980"], 0, PYQ + "It was started during Krishnaraja Wadiyar IV's reign under Visvesvaraya."),
    ("Mandya is called the 'Sugar city' because of:",
     ["Its sugarcane cultivation and the Mysore Sugar Company (1933)", "Its silk farms", "Its iron mines", "Its IT parks"], 0, "Krishnaraja Sagar irrigation made sugarcane possible."),
    ("Ramanagara is known as the 'Silk city' because it has:",
     ["One of Asia's largest cocoon markets", "Iron and steel plants", "Gold mines", "Car factories"], 0, PYQ + "Karnataka is India's largest producer of mulberry silk."),
    ("Peenya Industrial Area, one of the largest industrial estates in Asia, is in:",
     ["Bengaluru", "Hubballi", "Mysuru", "Belagavi"], 0, "It is mostly made up of small and medium enterprises."),
    ("The first modern cotton textile mill in India was set up in 1854 at:",
     ["Bombay (Mumbai)", "Ahmedabad", "Kanpur", "Coimbatore"], 0, PYQ + "Ahmedabad later became the 'Manchester of India'."),
    ("India's first jute mill was set up in 1855 at:",
     ["Rishra, near Kolkata", "Mumbai", "Chennai", "Kanpur"], 0, "The jute industry is concentrated along the Hooghly river."),
    ("Bengaluru is often called:",
     ["The Silicon Valley of India", "The Detroit of India", "The Manchester of India", "The Pittsburgh of India"], 0, PYQ + "Chennai is the 'Detroit of India' (automobiles); Jamshedpur the 'Pittsburgh of India'."),
    ("The eight core industries of India include:",
     ["Coal, crude oil, natural gas, refinery products, fertilisers, steel, cement and electricity", "Textiles, sugar, paper and jute only", "IT, banking, tourism and retail", "Gold, diamonds, silver and copper"], 0,
     "They make up about 40% of the weight in the IIP."),
    ("Bharat Earth Movers Ltd (BEML), a defence and mining equipment PSU, has its main plant at:",
     ["Kolar Gold Fields", "Raichur", "Hassan", "Udupi"], 0, PYQ + "BEML is headquartered in Bengaluru."),
    ("Consider the statements:\nI. Karnataka's Industrial Policy 2020-25 promotes Tier-II and Tier-III cities as growth engines.\nII. It aims to discourage the MSME sector.",
     I_II, 0, "The policy focuses on MSMEs, sustainable and inclusive growth, and industrial clusters beyond Bengaluru."),
    ("Assertion (A): Iron and steel plants are usually located near sources of raw materials.\nReason (R): Iron ore and coal are heavy, weight-losing raw materials.",
     AR, 0, "That is why plants cluster in the Chota Nagpur plateau region."),
    ("Assertion (A): The sugar industry is moving towards South India.\nReason (R): South India has a lower sucrose content in sugarcane than North India.",
     AR, 2, "Peninsular cane has higher sucrose content and a longer crushing season – that is part of why the industry is shifting south."),
    ("Match the Karnataka industry with its place:\na. Mysore Paper Mills  b. ITI (telephone equipment)  c. Visvesvaraya Iron & Steel  d. Cement\n1. Bhadravati (paper)  2. Bengaluru  3. Bhadravati (steel)  4. Wadi",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Bhadravati has both a paper mill and a steel plant."),
    ("The Kolar Gold Fields are in which district of Karnataka?",
     ["Kolar", "Chikkaballapur", "Tumakuru", "Ramanagara"], 0, "KGF received electricity from the Shivanasamudra power station in 1902 for its mines."),
]

TOPICS = {
    "Important Tourist Places and Peaks": [("1 · Mountain Peaks, Passes, Hill Stations and Waterfalls", PEAKS),
                                           ("2 · Tourist and Heritage Places of Karnataka and India", PLACES)],
    "Industries and Ores": [("1 · Minerals, Ores and Mining Regions", ORES),
                            ("2 · Major Industries of India and Karnataka", INDUSTRIES)],
}

NOTES = {
    "Important Tourist Places and Peaks": [{"title": "Peaks, passes, falls and tourist places – detailed notes", "md": """# Important tourist places and peaks

## 1. Peaks of India
| Peak | Height (approx.) | Facts |
|---|---|---|
| **K2 / Godwin Austen** | 8,611 m | **Highest in India** (official) – Gilgit-Baltistan, Karakoram |
| **Kanchenjunga** | 8,586 m | Highest under Indian administration – Sikkim–Nepal border |
| **Nanda Devi** | 7,816 m | Highest **entirely within** India – Uttarakhand |
| Mount Everest (Sagarmatha) | 8,849 m | In **Nepal** (Nepal–China border), not India |
| **Anamudi** | 2,695 m | Highest in **South India / Western Ghats** – Anaimalai hills, **Kerala** |
| **Doddabetta** | 2,637 m | Highest in the **Nilgiris** (Tamil Nadu) |
| Arma Konda (Jindhagada) | ~1,680 m | Highest in the **Eastern Ghats** (Andhra Pradesh) |
| **Guru Shikhar** | 1,722 m | Highest in the **Aravallis** (Mount Abu, Rajasthan) |
| Dhupgarh | 1,350 m | Highest in the Satpuras (Pachmarhi) |
| Saramati | 3,826 m | Highest in Nagaland |

## 2. Peaks of Karnataka (highest first)
**Mullayanagiri (~1,930 m, Chikkamagaluru – Baba Budan / Chandra Drona range)** > Baba Budangiri (~1,895 m) > **Kudremukh (~1,894 m)** > **Tadiandamol (~1,748 m, highest in Kodagu)** > Kumara Parvatha / Pushpagiri (~1,712 m) > Nandi Hills (~1,478 m) > Kodachadri (~1,343 m). BR Hills and Savandurga (a large monolith) are lower.

## 3. Mountain passes
| Pass | State / UT | Links |
|---|---|---|
| **Zoji La** | J&K – Ladakh | Srinagar – Leh |
| Khardung La | Ladakh | Leh – Nubra |
| **Shipki La** | Himachal Pradesh | India – Tibet (Sutlej) |
| Rohtang (Atal Tunnel) | Himachal Pradesh | Kullu – Lahaul |
| **Lipulekh** | Uttarakhand | Kailash–Mansarovar route |
| **Nathu La, Jelep La** | Sikkim | Sikkim – Tibet |
| Bomdi La | Arunachal Pradesh | |
**Karnataka ghat roads:** **Charmadi** (Mudigere – Ujire/Mangaluru), **Shiradi** (Sakleshpur – Mangaluru), **Sampaje** (Madikeri – Mangaluru), **Agumbe** (Shivamogga – Udupi), Hulikal (Shivamogga – Kundapura).

## 4. Waterfalls
| Falls | River | Place |
|---|---|---|
| **Jog (Gerusoppa)** – Raja, Rani, Roarer, Rocket | **Sharavathi** | Shivamogga – Uttara Kannada border |
| **Gaganachukki, Bharachukki** | **Kaveri** | Shivanasamudra (hydro-power 1902) |
| **Gokak** ('Niagara of Karnataka') | **Ghataprabha** | Belagavi |
| Unchalli (Lushington) | Aghanashini | Uttara Kannada |
| Magod | Bedti (Gangavali) | Uttara Kannada |
| Abbey, Iruppu | Kodagu streams / Lakshmana Tirtha | Kodagu |
| Dudhsagar | Mandovi | Goa – Karnataka border |
| Athirappilly ('Niagara of India') | Chalakudy | Kerala |
| Hogenakkal | Kaveri | Tamil Nadu |
| Nohkalikai | – | Meghalaya |

## 5. Hill stations
Ooty / Udhagamandalam (Nilgiris, **where Western and Eastern Ghats meet**, 'Queen of hill stations') · Kodaikanal (Palani hills) · Munnar (Kerala) · Darjeeling (WB, 'Queen of the hills') · Shimla, Manali (HP) · Mussoorie, Nainital (Uttarakhand) · Mount Abu (Rajasthan's only hill station) · Karnataka: Madikeri (Coorg – 'Scotland of India'), Kemmangundi, Nandi Hills, BR Hills, Agumbe ('Cherrapunji of the South').

## 6. Karnataka tourist places
- **Slogan:** 'One State, Many Worlds'.
- **Heritage:** Hampi (Tungabhadra), Badami, Aihole ('cradle of temple architecture'), Pattadakal, Belur–Halebidu (Hassan), Somanathapura (**Mysuru dist.**), Shravanabelagola, Gol Gumbaz (Vijayapura), Bidar fort, Srirangapatna (Kaveri island), Mysuru Palace, Chitradurga fort.
- **Coast:** Gokarna (Mahabaleshwara, Om and Half Moon beaches), Murudeshwar (giant Shiva statue, Netrani island), Udupi (Krishna temple, Malpe, **St Mary's Islands** – columnar basalt), Kollur (Mookambika), Karwar (Devbagh), Mangaluru (Tannirbhavi, Panambur). **Blue Flag beaches:** **Kasarkod** (Honnavar) and **Padubidri** (Udupi).
- **Nature:** Dandeli (rafting on the Kali), Kabini, Bandipur, Nagarahole, Chikkamagaluru (coffee – Baba Budan), Coorg.
- **Crafts and nicknames:** Channapatna toys, Bidriware (Bidar), Ilkal saris, Mysuru silk; Mandya – sugar city; Ramanagara – silk city; Davanagere – 'Manchester of Karnataka'.

## 7. Traps
- Highest peak in India (official) = **K2**, not Everest. Highest in South India = **Anamudi**, not Doddabetta.
- Jog is on the **Sharavathi**; Gokak on the **Ghataprabha**.
- Somanathapura is in **Mysuru** district, not Mandya.
- Charmadi ghat goes to **Ujire / Mangaluru**, not Bhatkal; Shiradi starts at **Sakleshpur**, not Kumta.
"""}],
    "Industries and Ores": [{"title": "Minerals and industries – detailed notes", "md": """# Industries and ores

## 1. Minerals – where they are found
| Mineral | Type | Leading areas |
|---|---|---|
| **Iron ore** (hematite, magnetite) | Ferrous | **Odisha** (largest), Chhattisgarh (Bailadila), **Karnataka (Ballari–Hosapete–Sandur)**, Jharkhand; Kudremukh (KIOCL, closed 2005) |
| **Manganese** | **Ferrous** (used in steel) | Odisha, MP, Maharashtra, Karnataka (Sandur, Shivamogga) |
| **Bauxite** (aluminium ore) | Non-ferrous | **Odisha** (Koraput – NALCO Damanjodi), Jharkhand, Gujarat |
| **Copper** | Non-ferrous | **Khetri** (Rajasthan), **Malanjkhand** (MP), Singhbhum (Jharkhand) |
| **Mica** | Non-metallic, insulator | **Koderma** (Jharkhand – 'mica capital'), Nellore (AP), Rajasthan |
| **Gold** | Precious | **Karnataka – Hutti (Raichur)**; Kolar Gold Fields closed 2001 |
| **Diamond** | Precious | **Panna** (MP) – India's only working diamond mine |
| **Coal** | Fuel | **Jharia** (Jharkhand – coking coal), **Raniganj** (WB – first, 1774), **Talcher** (Odisha), Tattapani (Chhattisgarh), Singrauli |
| **Lignite** | Fuel | **Neyveli** (Tamil Nadu) |
| **Uranium** | Atomic | **Jaduguda** (Jharkhand), Tummalapalle (AP) |
| **Lithium** | Critical | **Marlagalla, Mandya** (2021), Reasi, J&K (2023) – 'white gold' |
| Limestone | Cement | Kalaburagi (Shahabad, Wadi), MP, Rajasthan |
- Metals in nature: **gold** occurs native (free); **copper** as chalcocite and chalcopyrite; **lead** as galena; reactive metals like **magnesium** never occur free.
- **Kimberley Process** (2003) – certification to stop trade in **conflict diamonds**.
- **National Critical Mineral Mission** (2025) – lithium, cobalt, rare earths.

## 2. Iron and steel
| Plant | Year / helper | Facts |
|---|---|---|
| Porto Novo (TN) | 1830 | First attempt |
| **Kulti** (Bengal Iron Works) | 1870 | |
| **TISCO, Jamshedpur** | **1907** | First large integrated private plant |
| **Mysore Iron Works, Bhadravati** (now VISL) | **1923** | **Charcoal-based** – the only early non-coal plant |
| IISCO Burnpur / Hirapur | 1918–19 | |
| **Bhilai** (Chhattisgarh) | **USSR** | SAIL |
| **Rourkela** (Odisha) | **West Germany** | SAIL |
| **Durgapur** (WB) | **UK** | SAIL |
| **Bokaro** (Jharkhand) | USSR | SAIL |
| Visakhapatnam (RINL) | 1992 | Shore-based |
| **JSW Vijayanagar, Toranagallu (Ballari)** | private | One of India's largest single-site plants |

## 3. Other industries
- **Cotton textiles:** first mill **Bombay 1854**; **Ahmedabad – 'Manchester of India'**; Davanagere – 'Manchester of Karnataka'. Karnataka's cotton mills lag due to old machinery, power and raw-cotton problems.
- **Jute:** first mill **Rishra 1855**; Hooghly belt.
- **Sugar:** shifting **south** (higher sucrose, longer season); **Mandya** – Mysore Sugar Co. (1933).
- **Silk:** Karnataka is India's largest mulberry-silk producer; **Ramanagara** – Asia's large cocoon market; Mysore Silk (KSIC, 1912).
- **Nicknames:** Bengaluru – Silicon Valley of India; Chennai – Detroit of India; Jamshedpur – Pittsburgh of India; Kanpur – Manchester of the North.

## 4. Karnataka public-sector and landmark industries
| Unit | Place / year |
|---|---|
| **HAL** | Bengaluru, **1940 – Walchand Hirachand** |
| ITI (telephones) | Bengaluru, 1948 |
| HMT (machine tools, watches) | Bengaluru, 1953 |
| BEL | Bengaluru, 1954 |
| **BEML** | KGF / Bengaluru, 1964 |
| Mysore Sandal Soap (KSDL) | **1916** |
| Mysore Paper Mills, VISL | Bhadravati |
| Cement | Wadi, Shahabad (Kalaburagi) |
| **Peenya Industrial Area** | Bengaluru – one of Asia's largest industrial estates |
- **Karnataka Industrial Policy 2020-25:** sustainable and inclusive growth, MSMEs, Tier-II/III cities as growth engines.

## 5. Measuring industry
- **IIP (Index of Industrial Production):** monthly, by **NSO (earlier CSO), MoSPI**; base year 2011-12.
- **Eight core industries** (≈40% of IIP): coal, crude oil, natural gas, refinery products, fertilisers, steel, cement, electricity.

## 6. Traps
- **Manganese is ferrous**; bauxite, copper are non-ferrous; mica is an insulator.
- **Bhadravati** = charcoal-based, not coal-based.
- **Hutti** is the working gold mine; KGF is closed.
- 'White gold' today usually means **lithium** (older texts: cotton).
"""}],
}
