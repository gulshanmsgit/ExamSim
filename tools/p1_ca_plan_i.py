"""Paper 1 · Current Affairs · planner topics P1-GK-16 Current International Affairs – India's Foreign Relations and P1-CA-14
Highways, Railways and Airport Names (2 sub-topics × 20 each), with detailed notes (NOTES). P1-GK-16 is a General Knowledge row of
the planner that the structure pack leaves out (current affairs), so it lives in this subject with its plan ID.
Sources: Ministry of External Affairs annual reports and joint statements, PIB, MoRTH / NHAI, Ministry of Railways and Ministry of
Civil Aviation / AAI data, Ministry of Ports, Shipping and Waterways. REAL previous-year questions come from the Legislative Council
2024 Programmer Paper 1 (official KEA key), PSI 2024, VAO 2024, PGCET 2023 MCA, a KEA 2026 GK paper and UPSC-coaching entrance tests
(answers worked out by ExamSim and marked so)."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
KLC = " (Official answer: KEA final key, Legislative Council Secretariat exam 2024.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

PRINCIPLES = [
    ("India is a member of which of the following?\na) G20  b) G7\nc) Shanghai Cooperation Organisation (SCO)  d) New Development Bank (NDB)\nSelect the correct answer using the codes given below:",
     ["a only", "a, c and d only", "a, b and c only", "a, b, c and d"], 1,
     "India is in the G20, the SCO (full member since 2017) and the BRICS New Development Bank; it attends G7 summits only as an invited guest." + KLC,
     "Legislative Council 2024 Programmer P1 · Q18"),
    ("Name the leaders who introduced Non-Alignment Movement.",
     ["Jawaharlal Nehru, Nasser, Tito", "Sukarno, Tito, Nasser", "Tito, Zhou Enlai, Jawaharlal Nehru", "Zhou Enlai, Nasser, Jawaharlal Nehru"], 0,
     "Nehru, Nasser (Egypt) and Tito (Yugoslavia) launched the idea at Brioni (1956); with Sukarno and Nkrumah they founded NAM at Belgrade in 1961. Zhou Enlai (China) was never a NAM founder." + NOTE,
     "UPSC coaching entrance 2026 (HK) · Q6"),
    ("Which of following statement with regard to G20 Summit is wrong?",
     ["The 2023 G20 New Delhi Summit was the first ever G20 Summit to be held in India as well as in South Asia.", "In 2024, G20 Summit is scheduled to be held in Rio de Janeiro.",
      "In 2022, G20 Summit was held in Rome.", "The first G20 Summit was held in 2008 in Washington, D.C."], 2,
     "The 2022 summit was held in Bali, Indonesia; Rome hosted it in 2021." + NOTE, "PGCET 2023 MCA · Q79"),
    ("Consider the following statements with reference to International Solar Alliance (ISA).\na) It is a global initiative launched by India and France in 2015 at the COP 21 Summit held in Paris\nb) Its objective is to promote solar energy as a sustainable solution for energy access and climate change\nc) Headquarters of ISA is in Bangalore\nd) STAR-C Initiative and Green Hydrogen Innovation Centre are few of the initiatives launched by ISA\nHow many of the above statements is/are correct?",
     ["All the four are correct", "Only three statements are correct", "Only two statements are correct", "Only one statement is correct"], 1,
     "ISA's headquarters is in Gurugram (Haryana), so c is wrong; a, b and d are correct." + KLC, "Legislative Council 2024 Programmer P1 · Q64"),
    ("Recently CARICOM was in the news. Consider the following statements:\na. CARICOM refers to Caribbean Community and Common Market.\nb. The organization was founded on August 1, 1973, with the Treaty of Chaguramas.\nc. CARICOM has 15 members and 6 associate member countries.\nd. Recently the second India-CARICOM Summit was organised in Guyana.\nWhich of the above statement(s) is/are correct?",
     ["All of the above", "a, c and d only", "a and d only", "d only"], 0,
     "All four are correct; PM Modi attended the 2nd India–CARICOM Summit at Georgetown, Guyana, in November 2024." + NOTE, "UPSC coaching entrance 2025 (19 Jul) · Q2"),
    ("The 'Panchsheel' (five principles of peaceful coexistence) was signed in 1954 between India and:",
     ["China", "Pakistan", "Nepal", "USSR"], 0, PYQ + "It was part of the agreement on trade with the Tibet region."),
    ("India's 'Neighbourhood First' policy gives priority to relations with:",
     ["Its South Asian neighbours", "Only Western countries", "Only African countries", "Only the Gulf"], 0, "SAGAR (Security and Growth for All in the Region) covers the Indian Ocean."),
    ("The 'Look East' policy of 1991 was upgraded to the 'Act East' policy in:",
     ["2014", "2004", "1999", "2020"], 0, PYQ + "It focuses on ASEAN and the Indo-Pacific."),
    ("The Simla Agreement (1972) was signed between:",
     ["Indira Gandhi and Zulfikar Ali Bhutto", "Nehru and Liaquat Ali Khan", "Shastri and Ayub Khan", "Vajpayee and Nawaz Sharif"], 0, "The Tashkent Declaration (1966) was signed by Shastri and Ayub Khan."),
    ("The Indus Waters Treaty (1960) between India and Pakistan was brokered by the:",
     ["World Bank", "United Nations", "USA", "Commonwealth"], 0, PYQ + "India put the treaty 'in abeyance' after the Pahalgam attack of April 2025."),
    ("The 'Quad' (Quadrilateral Security Dialogue) consists of India and:",
     ["The USA, Japan and Australia", "Russia, China and Brazil", "France, UK and Germany", "Japan, South Korea and China"], 0, "India hosts a Quad Leaders' Summit as chair."),
    ("The India–Middle East–Europe Economic Corridor (IMEC) was announced at the:",
     ["G20 New Delhi Summit, 2023", "BRICS Summit, 2024", "SCO Summit, 2022", "Quad Summit, 2021"], 0, PYQ + "It links India by sea and rail to the Gulf and Europe."),
    ("The Chabahar port, developed with Indian help, is in:",
     ["Iran", "Pakistan", "Oman", "Afghanistan"], 0, "India signed a 10-year operating agreement for it in 2024."),
    ("India's first civil nuclear agreement with the USA (the '123 Agreement') was concluded in:",
     ["2008", "1998", "1974", "2015"], 0, PYQ + "The NSG waiver came the same year."),
    ("Maitri Setu (2021), built by India across the Feni river, connects Tripura with:",
     ["Bangladesh", "Myanmar", "Nepal", "Bhutan"], 0, "Maitri Setu (2021) connects Sabroom (Tripura) with Ramgarh (Bangladesh)."),
    ("Consider the statements:\nI. India is a founder member of the Non-Aligned Movement.\nII. India is a permanent member of the UN Security Council.",
     I_II, 0, "India is seeking a permanent seat; it has served as a non-permanent member eight times."),
    ("Assertion (A): India attends G7 summits.\nReason (R): India is a full member of the G7.",
     AR, 2, "India attends as an invited outreach partner; R is false."),
    ("Assertion (A): India's Act East policy focuses on South-East Asia and the Indo-Pacific.\nReason (R): ASEAN is one of India's largest trading partners.",
     AR, 1, "Both are true, but trade is not the whole reason for the policy."),
    ("Match the agreement with the year:\na. Panchsheel  b. Indus Waters Treaty  c. Simla Agreement  d. India–US nuclear deal\n1. 1954  2. 1960  3. 1972  4. 2008",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Treaty dates are common."),
    ("India's foreign policy principle of 'Vasudhaiva Kutumbakam' (the world is one family) was the theme of:",
     ["India's G20 presidency (2023) – 'One Earth, One Family, One Future'", "The 1961 NAM summit", "The Simla Agreement", "SAARC's founding"], 0, "It comes from the Maha Upanishad."),
]

BILATERAL = [
    ("The 'Vaccine Maitri' initiative of 2021 was India's programme to:",
     ["Supply COVID-19 vaccines to other countries", "Import vaccines from the USA", "Ban vaccine exports", "Fund WHO only"], 0, PYQ + "Neighbours received the first supplies."),
    ("Operation Sindhu (June 2025) evacuated Indian nationals from:",
     ["Iran and Israel", "Ukraine", "Sudan", "Afghanistan"], 0, "Operation Ganga (2022) – Ukraine; Operation Kaveri (2023) – Sudan."),
    ("The Comprehensive Economic Partnership Agreement (CEPA) of 2022 was signed by India with the:",
     ["United Arab Emirates", "China", "Pakistan", "Russia"], 0, PYQ + "An Economic Cooperation and Trade Agreement (ECTA) was signed with Australia the same year."),
    ("India and the United Kingdom signed a Comprehensive Economic and Trade Agreement (free trade agreement) in:",
     ["July 2025", "2010", "2016", "2020"], 0, "It was signed during PM Modi's visit to London."),
    ("India and the European Free Trade Association (EFTA) signed the TEPA in 2024. EFTA does NOT include:",
     ["France", "Switzerland", "Norway", "Iceland"], 0, PYQ + "EFTA = Switzerland, Norway, Iceland and Liechtenstein."),
    ("The Kartarpur Corridor (2019) connects Dera Baba Nanak in Punjab with Gurdwara Darbar Sahib in:",
     ["Pakistan", "Nepal", "Bangladesh", "Afghanistan"], 0, "It allows visa-free visits for Indian pilgrims."),
    ("India's longest land border is with:",
     ["Bangladesh", "China", "Pakistan", "Nepal"], 0, PYQ + "About 4,096 km."),
    ("The Galwan Valley clash of June 2020 took place on India's border with:",
     ["China", "Pakistan", "Nepal", "Bhutan"], 0, "It is in eastern Ladakh along the Line of Actual Control (LAC)."),
    ("India's largest hydropower partnership in its neighbourhood, including the Mangdechhu and Punatsangchhu projects, is with:",
     ["Bhutan", "Bangladesh", "Sri Lanka", "Maldives"], 0, PYQ + "Bhutan sells surplus hydropower to India."),
    ("Katchatheevu island, a recurring issue in India–Sri Lanka relations, was ceded to Sri Lanka in:",
     ["1974", "1947", "1983", "2009"], 0, "It lies in the Palk Strait."),
    ("The Indian Peace Keeping Force (IPKF) was sent to Sri Lanka in:",
     ["1987", "1971", "1999", "2005"], 0, PYQ + "It followed the Rajiv Gandhi–Jayewardene accord."),
    ("The India–Russia 'Special and Privileged Strategic Partnership' includes cooperation on:",
     ["Defence (S-400, BrahMos), nuclear energy (Kudankulam) and space", "Only tourism", "Only cricket", "Only films"], 0, "Annual summits are held between the two leaders."),
    ("The 2+2 ministerial dialogue involves the:",
     ["Foreign and defence ministers of both countries", "Prime ministers and presidents", "Finance and trade ministers", "Two army chiefs"], 0, PYQ + "India holds 2+2 dialogues with the USA, Japan, Australia and others."),
    ("Which neighbour of India adopted a 'India Out' campaign, followed by a reset of ties in 2024–25?",
     ["Maldives", "Bhutan", "Nepal", "Myanmar"], 0, "PM Modi was guest of honour at the Maldives' 60th independence day in July 2025."),
    ("The 'Lipulekh–Kalapani' territorial issue concerns India and:",
     ["Nepal", "China only", "Bhutan", "Bangladesh"], 0, PYQ + "Nepal published a new map in 2020."),
    ("Consider the statements:\nI. India and Bangladesh settled their land boundary through the Land Boundary Agreement of 2015.\nII. Enclaves (chhitmahals) were exchanged under it.",
     I_II, 2, "About 162 enclaves were exchanged."),
    ("Assertion (A): India put the Indus Waters Treaty in abeyance in 2025.\nReason (R): The decision was taken after the Pahalgam terror attack.",
     AR, 0, "It was announced in April 2025."),
    ("Assertion (A): Chabahar port helps India reach Afghanistan and Central Asia.\nReason (R): Chabahar is in Pakistan.",
     AR, 2, "Chabahar is in Iran; it bypasses Pakistan."),
    ("Match the operation with the country it evacuated Indians from:\na. Ganga  b. Kaveri  c. Ajay  d. Devi Shakti\n1. Ukraine  2. Sudan  3. Israel  4. Afghanistan",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Evacuation operations."),
    ("India's 'Global South' outreach includes the 'Voice of the Global South Summit', first hosted virtually in:",
     ["January 2023", "January 2015", "June 2019", "March 2010"], 0, "It was held during India's G20 presidency."),
]

ROADS_RAIL = [
    ("Match the following initiatives related to transportation infrastructure with their aims:\na) Gati Shakti Plan  i. Efficient logistics network\nb) Bharatmala Pariyojana  ii. Development of ropeways\nc) Parvatmala Pariyojana  iii. Online processing of land acquisition to accelerate highway infrastructure\nd) Bhoomi Rashi  iv. Connect, improve and decongest highways and road network in India",
     ["a - ii, b - iv, c - iii, d - i", "a - i, b - iv, c - ii, d - iii", "a - iii, b - ii, c - i, d - iv", "a - i, b - ii, c - iii, d - iv"], 1,
     "PM Gati Shakti (2021) – integrated logistics; Bharatmala – highways; Parvatmala (2022) – ropeways; Bhoomi Rashi – online land acquisition for NHs." + NOTE,
     "PSI 2024 General Paper · Q82"),
    ("Which of the following statements is not correct about railways in Karnataka?",
     ["South-Western Railway was created by merging the Hubli division with the Bangalore and Mysore divisions", "In Konkan Railway the first passenger train ran between Mangalore and Karwar in 1993",
      "The Bangalore City Railway Station was renamed as \"Kranthiveera Sangolli Rayanna Railway Station\" in 2016", "The first railway line in the state was from Bengaluru to Madras and it was opened in 1864."], 1,
     "The first Konkan Railway passenger train (20 March 1993) ran between Mangaluru and Udupi, not Karwar." + NOTE, "VAO 2024 Paper-1 · Q97"),
    ("The first Vande Bharat Express train which was inaugurated on February 18, 2019 runs between which of the following cities?",
     ["Mumbai-Sainagar Shirdi", "Puri-Howrah", "Varanasi-New Delhi", "Bengaluru-Dharwad"], 2,
     "The first Vande Bharat (Train 18) ran between New Delhi and Varanasi; it was flagged off on 15 February 2019 and began regular service soon after." + NOTE, "PGCET 2023 MCA · Q49"),
    ("The longest National Highway of India, running from Srinagar to Kanyakumari, is:",
     ["NH-44", "NH-48", "NH-27", "NH-66"], 0, PYQ + "It is about 4,100 km long and passes through Bengaluru."),
    ("The Golden Quadrilateral connects:",
     ["Delhi, Mumbai, Chennai and Kolkata", "Delhi, Bengaluru, Hyderabad and Kolkata", "Mumbai, Pune, Nagpur and Delhi", "Chennai, Kochi, Bengaluru and Mumbai"], 0,
     "It was part of the National Highways Development Project (from 2001)."),
    ("The North–South corridor connects Srinagar with Kanyakumari, and the East–West corridor connects Silchar with:",
     ["Porbandar", "Mumbai", "Kandla", "Dwarka"], 0, PYQ + "The two corridors cross at Jhansi."),
    ("The Bengaluru–Mysuru access-controlled expressway, opened in 2023, is part of:",
     ["NH-275", "NH-44", "NH-48", "NH-75"], 0, "It cut the travel time to about 75 minutes."),
    ("The headquarters of the South Western Railway zone is at:",
     ["Hubballi", "Bengaluru", "Mysuru", "Mangaluru"], 0, PYQ + "It was formed in 2003; its divisions are Hubballi, Bengaluru and Mysuru."),
    ("India's first passenger train ran on 16 April 1853 between:",
     ["Bori Bunder (Bombay) and Thane", "Howrah and Hooghly", "Madras and Arcot", "Delhi and Agra"], 0, "It covered 34 km."),
    ("The Konkan Railway runs between Roha (Maharashtra) and Thokur near:",
     ["Mangaluru", "Karwar", "Goa", "Kochi"], 0, PYQ + "It is about 741 km long; E. Sreedharan led its construction."),
    ("The Mumbai–Ahmedabad High Speed Rail (bullet train) project uses technology from:",
     ["Japan (Shinkansen)", "France", "China", "Germany"], 0, "It is being built by the National High Speed Rail Corporation (NHSRCL)."),
    ("The Chenab rail bridge, the world's highest railway arch bridge, is in:",
     ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim"], 0, PYQ + "It is part of the Udhampur–Srinagar–Baramulla line opened in 2025."),
    ("The New Pamban Bridge (2025), India's first vertical-lift sea bridge, links the mainland with:",
     ["Rameswaram", "Diu", "Port Blair", "Kavaratti"], 0, "It replaced the 1914 cantilever bridge in Tamil Nadu."),
    ("Indian Railways is divided into how many zones (excluding Kolkata Metro and the new South Coast Railway)?",
     ["17", "9", "12", "25"], 0, PYQ + "The South Coast Railway zone (Visakhapatnam) is being set up as the 18th."),
    ("The 'Atal Tunnel', one of the world's longest highway tunnels above 10,000 ft, is at:",
     ["Rohtang, Himachal Pradesh", "Zojila, Ladakh", "Banihal, J&K", "Nathu La, Sikkim"], 0, "It opened in 2020 on the Manali–Leh road."),
    ("Consider the statements:\nI. The Bharatmala Pariyojana is a highway development programme.\nII. The Sagarmala programme aims at port-led development.",
     I_II, 2, "Both are correct."),
    ("Assertion (A): The FASTag system speeds up toll collection on national highways.\nReason (R): FASTag uses RFID to deduct tolls electronically without stopping.",
     AR, 0, "It became mandatory in 2021."),
    ("Assertion (A): The Konkan Railway is run directly by a zonal railway of Indian Railways.\nReason (R): Konkan Railway Corporation Ltd is a separate public-sector company.",
     AR, 3, "It is a separate corporation; A is false."),
    ("Match:\na. NH-44  b. Golden Quadrilateral  c. Konkan Railway  d. South Western Railway\n1. Srinagar–Kanyakumari  2. Four metros  3. Roha–Thokur  4. Hubballi",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Transport matching."),
    ("The Delhi–Mumbai Expressway, India's longest expressway under construction, is being built under:",
     ["Bharatmala Pariyojana", "Sagarmala", "UDAN", "Smart Cities Mission"], 0, "It is about 1,350 km long."),
]

AIR_PORTS = [
    ("Arrange the following major ports of India from north to south direction.\na) Haldia\nb) Kolkata\nc) Vishakapatnam\nd) Paradeep",
     ["a, c, b, d", "b, a, d, c", "c, b, a, d", "d, c, b, a"], 1,
     "Kolkata (≈22.6° N) → Haldia (≈22.0° N) → Paradip (≈20.3° N) → Visakhapatnam (≈17.7° N)." + KLC, "Legislative Council 2024 Programmer P1 · Q25"),
    ("Name the collaborative system developed jointly by Airports Authority of India and Indian Space Research Organization to improve the accuracy and reliability of GPS signals.",
     ["Sugamya Bharat Abhiyan", "Krishi UDAN 2.0", "Digi Yatra", "GAGAN"], 3,
     "GAGAN (GPS Aided GEO Augmented Navigation) is India's satellite-based augmentation system." + NOTE, "VAO 2024 Paper-1 · Q33"),
    ("The newly formed Bengaluru Metropolitan Land Transport Authority (BMLTA) in Karnataka will be chaired by",
     ["The Home Minister", "The Transport Minister", "The Chief Minister", "The Bengaluru Development Minister"], 2,
     "Under the BMLTA Act, the Chief Minister heads the authority that plans all modes of transport in the Bengaluru region." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q88"),
    ("Bengaluru's international airport is named after:",
     ["Kempegowda", "Sir M. Visvesvaraya", "Basavanna", "Tipu Sultan"], 0, PYQ + "Kempegowda International Airport, Devanahalli, opened in 2008."),
    ("Chhatrapati Shivaji Maharaj International Airport is in:",
     ["Mumbai", "Pune", "Nagpur", "Aurangabad"], 0, "Nagpur's airport is named after Dr Babasaheb Ambedkar."),
    ("Netaji Subhas Chandra Bose International Airport is in:",
     ["Kolkata", "Bhubaneswar", "Patna", "Guwahati"], 0, PYQ + "Bhubaneswar – Biju Patnaik; Patna – Jay Prakash Narayan; Guwahati – Lokpriya Gopinath Bordoloi."),
    ("Rajiv Gandhi International Airport serves:",
     ["Hyderabad", "Chennai", "Delhi", "Thiruvananthapuram"], 0, "Delhi – Indira Gandhi International Airport."),
    ("Sardar Vallabhbhai Patel International Airport is in:",
     ["Ahmedabad", "Surat", "Vadodara", "Rajkot"], 0, PYQ + "Indore – Devi Ahilyabai Holkar; Bhopal – Raja Bhoj."),
    ("The world's first fully solar-powered airport is:",
     ["Cochin International Airport", "Kempegowda International Airport", "Chennai Airport", "Goa Airport"], 0, "It achieved this in 2015; it is also India's first airport built under PPP."),
    ("The new airport at Shivamogga (2023) is named after:",
     ["Kuvempu (Rashtrakavi Kuvempu Airport)", "Kempegowda", "Jayachamarajendra Wadiyar", "Sangolli Rayanna"], 0, PYQ + "Belagavi airport is at Sambra; Mangaluru airport is at Bajpe."),
    ("Ayodhya's airport, opened in December 2023, is named:",
     ["Maharishi Valmiki International Airport", "Shri Ram International Airport", "Tulsidas Airport", "Kabir Airport"], 0, "Ayodhya Dham railway station was redeveloped at the same time."),
    ("Goa's second airport at Mopa (2022) is named after:",
     ["Manohar Parrikar", "Dayanand Bandodkar", "Francis Xavier", "Pratapsingh Rane"], 0, PYQ + "The older Goa airport is at Dabolim."),
    ("The UDAN scheme (2016) of the Ministry of Civil Aviation aims to:",
     ["Make regional air travel affordable – 'Ude Desh ka Aam Nagrik'", "Build only metro lines", "Privatise railways", "Build highways"], 0, "Krishi UDAN helps air transport of farm produce."),
    ("Karnataka's only major port is:",
     ["New Mangalore Port (Panambur)", "Karwar", "Belekeri", "Malpe"], 0, PYQ + "Karwar is a minor (state) port."),
    ("Kandla port has been renamed as:",
     ["Deendayal Port", "Syama Prasad Mookerjee Port", "V. O. Chidambaranar Port", "Kamarajar Port"], 0, "Kolkata – Syama Prasad Mookerjee; Tuticorin – V. O. Chidambaranar; Ennore – Kamarajar."),
    ("India's first deep-water container transshipment port, commissioned in 2025, is:",
     ["Vizhinjam (Kerala)", "Vadhavan (Maharashtra)", "Paradip", "Haldia"], 0, PYQ + "Vadhavan near Mumbai is being built as a new mega port."),
    ("Consider the statements:\nI. Digi Yatra enables paperless, face-recognition-based entry at airports.\nII. GAGAN is a satellite-based navigation augmentation system.",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Kempegowda International Airport is at Devanahalli.\nReason (R): It is named after the founder of Bengaluru.",
     AR, 1, "Both are true, but the name does not explain the location."),
    ("Assertion (A): New Mangalore Port is a major port.\nReason (R): Major ports are administered by the Union Government under the Major Port Authorities Act, 2021.",
     AR, 0, "Minor ports are under state maritime boards."),
    ("Match the airport with its city:\na. Biju Patnaik  b. Lokpriya Gopinath Bordoloi  c. Jay Prakash Narayan  d. Sri Guru Ram Dass Jee\n1. Bhubaneswar  2. Guwahati  3. Patna  4. Amritsar",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Airport names are frequently asked."),
]

TOPICS = {
    "Current International Affairs – India's Foreign Relations": [("1 · Principles, Groupings, Treaties and Global Role", PRINCIPLES),
                                                                  ("2 · India and Its Neighbours and Partners", BILATERAL)],
    "Highways, Railways and Airport Names": [("1 · National Highways, Expressways and Railways", ROADS_RAIL),
                                             ("2 · Airports and Ports of India and Karnataka", AIR_PORTS)],
}

NOTES = {
    "Current International Affairs – India's Foreign Relations": [{"title": "India's foreign relations – detailed notes", "md": """# India's foreign relations

## 1. Principles
- **Panchsheel** (1954, India–China): mutual respect for territory and sovereignty, non-aggression, non-interference, equality and mutual benefit, peaceful coexistence.
- **Non-Alignment:** Nehru, **Nasser** (Egypt), **Tito** (Yugoslavia) at **Brioni (1956)**; NAM founded at **Belgrade (1961)** with **Sukarno** (Indonesia) and **Nkrumah** (Ghana).
- **Neighbourhood First** · **SAGAR** (2015, Indian Ocean) · **Look East (1991) → Act East (2014)** · **Vasudhaiva Kutumbakam** – G20 theme "One Earth, One Family, One Future".
- **Strategic autonomy**: India deals with the USA, Russia and others at the same time.

## 2. Groupings (India's status)
| Grouping | India |
|---|---|
| G20 | Member; **New Delhi summit, Sept 2023** (African Union admitted) |
| G7 | **Invited guest only** |
| BRICS / **NDB** | Founder; BRICS expanded 2024–25 |
| **SCO** | Full member since **2017**; chair 2023 |
| Quad | India, USA, Japan, Australia |
| SAARC (1985) / BIMSTEC (1997) | Founder |
| **ISA** | Launched by India & France at **COP21 Paris, 2015**; HQ **Gurugram** |
| CARICOM | Caribbean grouping; **2nd India–CARICOM Summit, Georgetown (Guyana), Nov 2024** |
| UN Security Council | Non-permanent member 8 times; seeks a permanent seat |

G20 venues: 2008 Washington · 2021 Rome · **2022 Bali** · 2023 New Delhi · 2024 Rio de Janeiro · 2025 Johannesburg.

## 3. Treaties and agreements
| Year | Agreement |
|---|---|
| 1954 | Panchsheel (China) |
| 1960 | **Indus Waters Treaty** (World Bank) – **in abeyance from April 2025** |
| 1966 | Tashkent Declaration (Shastri–Ayub) |
| 1971 | Indo-Soviet Treaty of Friendship |
| 1972 | **Simla Agreement** (Indira–Bhutto) |
| 1987 | India–Sri Lanka Accord (IPKF) |
| 2008 | India–US civil nuclear (123) agreement |
| 2015 | India–Bangladesh Land Boundary Agreement (enclaves) |
| 2022 | **CEPA with UAE**; ECTA with Australia |
| 2024 | **TEPA with EFTA** (Switzerland, Norway, Iceland, Liechtenstein); Chabahar 10-year deal |
| 2025 | **India–UK trade agreement** (July) |

## 4. Neighbours
- **Pakistan:** wars 1947, 1965, 1971, 1999 (Kargil); Kartarpur Corridor 2019; **Operation Sindoor** May 2025.
- **China:** 1962 war; LAC; **Galwan** clash June 2020; disengagement agreement Oct 2024.
- **Bangladesh:** longest border (~4,096 km); Maitri Setu (Tripura).
- **Nepal:** Kalapani–Lipulekh dispute; open border. **Bhutan:** hydropower. **Sri Lanka:** Katchatheevu (1974); IPKF (1987).
- **Maldives:** 'India Out' campaign, then a reset in 2024–25. **Myanmar:** Kaladan project; **Operation Brahma** (2025 quake).

## 5. Other partners
USA – 2+2 dialogue, iCET, Quad · Russia – S-400, Kudankulam, BrahMos · Japan – bullet train · France – Rafale, ISA · Iran – **Chabahar** · Gulf – IMEC (G20 2023).

## 6. Evacuations
Rahat (Yemen 2015) · Devi Shakti (Afghanistan 2021) · Ganga (Ukraine 2022) · Kaveri (Sudan 2023) · Ajay (Israel 2023) · **Sindhu** (Iran/Israel 2025).

## 7. Traps
- India is **not** a G7 member. ISA HQ is in **Gurugram**, not Bengaluru.
- Zhou Enlai was at **Bandung (1955)**, not a NAM founder.
"""}],
    "Highways, Railways and Airport Names": [{"title": "Highways, railways, airports and ports – detailed notes", "md": """# Highways, railways and airports

## 1. Roads
- **NH-44** – longest NH, **Srinagar → Kanyakumari** (~4,100 km), via Bengaluru. NH-48 Delhi–Mumbai–Bengaluru–Chennai. NH-66 – west coast (Panvel–Kanyakumari, through coastal Karnataka).
- **Golden Quadrilateral** – Delhi, Mumbai, Chennai, Kolkata. **North–South** (Srinagar–Kanyakumari) and **East–West** (**Silchar–Porbandar**) corridors cross at **Jhansi**.
- Programmes: **Bharatmala** (highways), **Sagarmala** (ports), **Parvatmala** (ropeways), **PM Gati Shakti** (2021, integrated logistics), **Bhoomi Rashi** (online land acquisition), FASTag (RFID tolls).
- Expressways: Delhi–Mumbai (~1,350 km); Mumbai–Nagpur Samruddhi; **Bengaluru–Mysuru (NH-275, 2023)**; Bengaluru–Chennai.
- Tunnels: **Atal Tunnel**, Rohtang (2020); Zojila tunnel (under construction).

## 2. Railways
- First train **16 April 1853**, **Bori Bunder–Thane** (34 km). In Karnataka: **Bengaluru–Jolarpettai (towards Madras), 1864**.
- **17 zones** (+ South Coast Railway, Visakhapatnam, being set up). **South Western Railway – HQ Hubballi** (2003; Hubballi, Bengaluru, Mysuru divisions).
- **Konkan Railway**: Roha–Thokur (Mangaluru), ~741 km; separate corporation (HQ Navi Mumbai); first passenger train **Mangaluru–Udupi, 1993**; E. Sreedharan.
- Bengaluru City station renamed **Krantiveera Sangolli Rayanna (KSR)** station in 2016.
- **Vande Bharat** – first train **New Delhi–Varanasi (Feb 2019)**, built at ICF Chennai. Vande Bharat sleeper trains are next.
- **Bullet train**: Mumbai–Ahmedabad, Japanese Shinkansen, NHSRCL.
- **Chenab bridge** (world's highest rail arch) and **Anji Khad** cable bridge – USBRL, opened 2025. **New Pamban bridge** (vertical lift), Rameswaram, 2025.

## 3. Airports
| Airport | City |
|---|---|
| Indira Gandhi | Delhi (busiest) |
| Chhatrapati Shivaji Maharaj | Mumbai |
| Netaji Subhas Chandra Bose | Kolkata |
| **Kempegowda** | Bengaluru (Devanahalli) |
| Rajiv Gandhi | Hyderabad |
| Chennai (Anna / Kamaraj terminals) | Chennai |
| Sardar Vallabhbhai Patel | Ahmedabad |
| Biju Patnaik | Bhubaneswar |
| Lokpriya Gopinath Bordoloi | Guwahati |
| Jay Prakash Narayan | Patna |
| Sri Guru Ram Dass Jee | Amritsar |
| Chaudhary Charan Singh | Lucknow |
| Devi Ahilyabai Holkar / Raja Bhoj | Indore / Bhopal |
| Dr Babasaheb Ambedkar | Nagpur |
| **Manohar International (Mopa)** / Dabolim | Goa |
| **Maharishi Valmiki** | Ayodhya (2023) |
| Cochin | **First fully solar-powered airport** (2015) |
| Navi Mumbai International (D. B. Patil) / Noida (Jewar) | New airports, 2025– |

**Karnataka:** Bengaluru (Kempegowda; HAL old airport), Mangaluru (**Bajpe**), Mysuru (Mandakalli), Hubballi, Belagavi (**Sambra**), Kalaburagi, Bidar, **Shivamogga – Rashtrakavi Kuvempu (2023)**, Vijayapura, Ballari (Jindal Vidyanagar).
Schemes: **UDAN** (2016, "Ude Desh ka Aam Nagrik"), **Krishi UDAN**, **Digi Yatra** (face-recognition boarding), **GAGAN** (AAI + ISRO, GPS augmentation).

## 4. Ports
12 major ports (+ **Vadhavan**, Maharashtra, coming). Renamed: Kandla → **Deendayal**; Kolkata → **Syama Prasad Mookerjee**; Tuticorin → **V. O. Chidambaranar**; Ennore → **Kamarajar**; JNPT → **Jawaharlal Nehru Port**. Karnataka's only major port – **New Mangalore (Panambur)**; Karwar is a minor port; **INS Kadamba** naval base at Karwar. **Vizhinjam** (Kerala) – first deep-water transshipment port, 2025.
North → south on the east coast: **Kolkata → Haldia → Paradip → Visakhapatnam → Kamarajar (Ennore) → Chennai → V. O. Chidambaranar (Tuticorin)**.

## 5. Traps
- First Konkan passenger train: Mangaluru–**Udupi**, not Karwar.
- First Vande Bharat: **Delhi–Varanasi**.
- Kandla = Deendayal; ISA HQ Gurugram (not a port!).
"""}],
}
