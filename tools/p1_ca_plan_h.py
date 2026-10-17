"""Paper 1 · Current Affairs · planner topic P1-CA-12 Three Wings of the Army (2 sub-topics × 20), with detailed notes (NOTES).
Sources: Ministry of Defence annual reports and PIB, websites of the Indian Army, Navy and Air Force, DRDO, NCERT / KTBS civics.
REAL previous-year questions come from PSI 2023, GTTC 2024 GK, a KEA 2026 GK paper and a UPSC-coaching entrance test; KEA's key for
GTTC Q76–100 could not be parsed, so all answers here were worked out by ExamSim and say so. Names of serving chiefs change, so
they are given only in the notes ('as of 2025') and kept out of the questions."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

STRUCTURE = [
    ("The Supreme Commander of the Indian Armed Forces is:",
     ["The President of India", "The Prime Minister", "The Defence Minister", "The Chief of Defence Staff"], 0, PYQ + "Article 53(2) vests the supreme command in the President."),
    ("The post of Chief of Defence Staff (CDS), who heads the Department of Military Affairs, was created in:",
     ["2019 (first CDS General Bipin Rawat took office on 1 January 2020)", "1947", "1999", "2014"], 0, "It followed the Kargil Review Committee's recommendations."),
    ("Indian Army Day is observed on 15 January because on that day in 1949:",
     ["General K. M. Cariappa became the first Indian Commander-in-Chief", "India won the Kargil war", "The Army was founded", "The Constitution came into force"], 0, PYQ + "Navy Day is 4 December; Air Force Day is 8 October."),
    ("The Indian Navy celebrates its Navy Day on 4 December to remember:",
     ["Operation Trident – the attack on Karachi harbour in the 1971 war", "The founding of the Navy", "INS Vikrant's commissioning", "The liberation of Goa"], 0, "Vijay Diwas, 16 December, marks the 1971 victory."),
    ("Which rank in the Navy is equal to a General in the Army?",
     ["Admiral", "Vice Admiral", "Commodore", "Captain"], 0, PYQ + "The Air Force equivalent is Air Chief Marshal."),
    ("A Brigadier in the Army is equivalent to which rank in the Air Force?",
     ["Air Commodore", "Group Captain", "Wing Commander", "Air Vice Marshal"], 0, "Navy equivalent: Commodore."),
    ("Who were the two Field Marshals of the Indian Army?",
     ["Sam Manekshaw and K. M. Cariappa", "Bipin Rawat and V. K. Singh", "Arjan Singh and Cariappa", "Manekshaw and Thimayya"], 0, PYQ + "Arjan Singh was the only Marshal of the Indian Air Force."),
    ("Field Marshal K. M. Cariappa belonged to:",
     ["Kodagu (Coorg), Karnataka", "Punjab", "Kerala", "Maharashtra"], 0, "General K. S. Thimayya was also from Kodagu."),
    ("The National Defence Academy (NDA), which trains cadets of all three services together, is at:",
     ["Khadakwasla, Pune", "Dehradun", "Ezhimala", "Dundigal"], 0, PYQ + "IMA – Dehradun; Indian Naval Academy – Ezhimala (Kerala); Air Force Academy – Dundigal (Hyderabad)."),
    ("The Indian Air Force's Training Command has its headquarters at:",
     ["Bengaluru", "Shillong", "Nagpur", "Gandhinagar"], 0, "Maintenance Command – Nagpur; Eastern Air Command – Shillong."),
    ("The Western and Eastern Naval Commands are headquartered at:",
     ["Mumbai and Visakhapatnam", "Kochi and Chennai", "Goa and Kolkata", "Karwar and Port Blair"], 0, PYQ + "Southern Naval Command (training) is at Kochi."),
    ("INS Kadamba, developed under Project Seabird, is a major naval base at:",
     ["Karwar, Karnataka", "Mangaluru", "Kochi", "Goa"], 0, "It is planned to be one of the largest naval bases east of the Suez."),
    ("The Agnipath scheme (2022) recruits 'Agniveers' into the armed forces for a period of:",
     ["4 years, with up to 25% retained for regular service", "10 years", "2 years", "Lifetime"], 0, PYQ + "Recruits are aged 17½ to 21 (relaxed in the first year)."),
    ("The highest wartime gallantry award in India is the:",
     ["Param Vir Chakra", "Ashoka Chakra", "Kirti Chakra", "Bharat Ratna"], 0, "The Ashoka Chakra is the highest peacetime gallantry award."),
    ("The first recipient of the Param Vir Chakra was:",
     ["Major Somnath Sharma (1947, Kashmir)", "Captain Vikram Batra", "Major Shaitan Singh", "Abdul Hamid"], 0, PYQ + "He was awarded posthumously for the defence of Srinagar airport (Battle of Badgam)."),
    ("The oldest paramilitary force of India, raised in 1835, is the:",
     ["Assam Rifles", "BSF", "CRPF", "ITBP"], 0, "It is under the administrative control of the Ministry of Home Affairs but officered by the Army."),
    ("The Indian Coast Guard was set up in 1977 under the:",
     ["Ministry of Defence", "Ministry of Home Affairs", "Ministry of Shipping", "Ministry of External Affairs"], 0, PYQ + "BSF, CRPF, CISF, ITBP and SSB (CAPFs) are under the Home Ministry."),
    ("Consider the statements:\nI. NCC (National Cadet Corps) was formed in 1948.\nII. NCC is a combat force of the Army deployed on borders.",
     I_II, 0, "NCC is a youth organisation that trains school and college students."),
    ("Assertion (A): Kargil Vijay Diwas is observed on 26 July.\nReason (R): On 26 July 1999, India announced the successful end of Operation Vijay in Kargil.",
     AR, 0, "Operation Vijay is also the name of the 1961 liberation of Goa."),
    ("Match the rank equivalents:\na. Lieutenant General  b. Colonel  c. Major  d. Lieutenant (Army)\n1. Vice Admiral / Air Marshal  2. Captain (Navy) / Group Captain  3. Lieutenant Commander / Squadron Leader  4. Sub Lieutenant / Flying Officer",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Rank equivalents are often asked."),
]

EQUIP_OPS = [
    ("DRDO successfully Flight-tested the following Ballistic Missile in June 2023:",
     ["Agni-IV", "Agni-V", "Agni Prime", "Agni-VI"], 2,
     "Agni Prime (Agni-P), a new-generation canisterised missile, had its first pre-induction night launch from Abdul Kalam Island in June 2023." + NOTE, "PSI 2023 General Paper · Q24"),
    ("'Agni warrior 2024' military exercise was held between which of the following countries?",
     ["India and Sri lanka", "India and Russia", "India and Singapore", "India and Israel"], 2,
     "Agni Warrior is a bilateral artillery exercise of the Indian Army and the Singapore Army." + NOTE, "GTTC 2024 Asst Gr-II GK · Q99"),
    ("Consider the Joint Military/Navy Exercises conducted by India with foreign countries :\nName of the Exercise – Name of the Country\na. Varuna  i. Russia\nb. Cyclone  ii. France\nc. Indra  iii. Egypt\nd. Dharma Guardian  iv. Nepal\ne. Surya Kiran  v. Japan\nChoose the correct answer from the options given below:",
     ["a-iii, b-i, c-ii, d-v, e-iv", "a-ii, b-iii, c-i, d-v, e-iv", "a-iii, b-v, c-ii, d-iv, e-i", "a-iii, b-v, c-i, d-ii, e-iv"], 1,
     "Varuna – France (navy); Cyclone – Egypt; Indra – Russia; Dharma Guardian – Japan; Surya Kiran – Nepal." + NOTE, "UPSC coaching entrance 2025 (19 Jul) · Q12"),
    ("Match the following operations in List-I with their purpose in List-II.\nList-I (Operation)\n(a) Operation Sindoor\n(b) Operation Brahma\n(c) Operation Ajay\n(d) Operation Black Forest\nList-II (Purpose)\n(i) Anti-Naxal operations\n(ii) Evacuation of Indian nationals during West Asia conflict\n(iii) In response to the Pahalgam terror attack\n(iv) Humanitarian assistance to Myanmar after a devastating earthquake",
     ["a-iii, b-ii, c-i, d-iv", "a-i, b-iii, c-iv, d-ii", "a-iii, b-iv, c-ii, d-i", "a-i, b-ii, c-iv, d-iii"], 2,
     "Sindoor (May 2025) – strikes after the Pahalgam attack; Brahma (March 2025) – Myanmar quake relief; Ajay (2023) – evacuation from Israel; Black Forest (2025) – anti-Naxal operation in the Karregutta hills." + NOTE,
     "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q98"),
    ("INS Vikrant, India's first indigenously built aircraft carrier, was commissioned in 2022 and built at:",
     ["Cochin Shipyard", "Mazagon Dock, Mumbai", "Garden Reach, Kolkata", "Hindustan Shipyard, Visakhapatnam"], 0, PYQ + "INS Vikramaditya is a carrier bought from Russia."),
    ("The Light Combat Aircraft 'Tejas' is built by:",
     ["Hindustan Aeronautics Limited (HAL), Bengaluru", "Dassault, France", "Boeing, USA", "Sukhoi, Russia"], 0, "The Rafale is from Dassault (France); the Su-30MKI is built in India under licence."),
    ("BrahMos, the supersonic cruise missile, is a joint venture of India and:",
     ["Russia", "Israel", "France", "USA"], 0, PYQ + "The name combines the Brahmaputra and the Moskva rivers."),
    ("INS Arihant is India's first indigenous:",
     ["Nuclear-powered ballistic missile submarine", "Aircraft carrier", "Stealth frigate", "Hospital ship"], 0, "It gives India the sea leg of the nuclear triad."),
    ("Operation Meghdoot (1984) was launched to secure:",
     ["The Siachen Glacier", "Goa", "Kargil heights", "Bangladesh"], 0, PYQ + "Siachen is the world's highest battlefield."),
    ("Operation Ganga (2022) and Operation Kaveri (2023) were operations to:",
     ["Evacuate Indian nationals from Ukraine and Sudan", "Clean rivers", "Fight floods", "Arrest smugglers"], 0, "Operation Sindhu (2025) evacuated Indians from Iran and Israel."),
    ("The Malabar naval exercise involves the navies of:",
     ["India, the USA, Japan and Australia", "India and France only", "India and Russia only", "India and China"], 0, PYQ + "It began as an India–US exercise in 1992."),
    ("Exercise Yudh Abhyas is held between the armies of India and:",
     ["The USA", "Nepal", "Japan", "Egypt"], 0, "Garuda is India–France (air); Shakti is India–France (army); Mitra Shakti is India–Sri Lanka."),
    ("The Defence Research and Development Organisation (DRDO) was set up in:",
     ["1958", "1947", "1969", "1983"], 0, PYQ + "The Integrated Guided Missile Development Programme (1983) was led by Dr A. P. J. Abdul Kalam."),
    ("Prithvi, Agni, Akash, Nag and Trishul were the missiles of the:",
     ["Integrated Guided Missile Development Programme", "Chandrayaan programme", "Gaganyaan mission", "Make in India campaign only"], 0, "Agni is a long-range ballistic missile; Akash a surface-to-air missile; Nag an anti-tank missile."),
    ("'Prachand', inducted in 2022, is India's:",
     ["Light Combat Helicopter", "Main battle tank", "Aircraft carrier", "Submarine"], 0, PYQ + "Arjun is India's main battle tank."),
    ("Consider the statements:\nI. The Rafale fighter jets were bought from France.\nII. Tejas is an indigenous light combat aircraft.",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Operation Sindoor was launched in May 2025.\nReason (R): It was India's military response to the Pahalgam terror attack of April 2025.",
     AR, 0, "Terror infrastructure across the border was targeted."),
    ("Assertion (A): The Ashoka Chakra is India's highest wartime gallantry award.\nReason (R): The Param Vir Chakra is awarded for the highest bravery in the presence of the enemy.",
     AR, 3, "The Ashoka Chakra is the highest peacetime award; the PVC is the wartime award."),
    ("Match the defence academy with its place:\na. National Defence Academy  b. Indian Military Academy  c. Indian Naval Academy  d. Air Force Academy\n1. Khadakwasla  2. Dehradun  3. Ezhimala  4. Dundigal",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Academy matching is common."),
    ("India's Sainik Schools in Karnataka are at:",
     ["Kodagu (Kudige) and Vijayapura", "Mysuru and Hubballi", "Mangaluru and Udupi", "Ballari and Raichur"], 0, "Sainik Schools prepare students for the NDA."),
]

TOPICS = {
    "Three Wings of the Army": [("1 · Organisation, Ranks, Days, Training and Awards", STRUCTURE),
                                ("2 · Weapons, Ships, Missiles, Exercises and Operations", EQUIP_OPS)],
}

NOTES = {
    "Three Wings of the Army": [{"title": "Indian Army, Navy and Air Force – detailed notes", "md": """# Three wings of the armed forces

## 1. Command and heads
- **Supreme Commander:** the **President** (Art. 53). **Defence Minister** heads the Ministry of Defence.
- **Chief of Defence Staff (CDS):** post created 2019; heads the **Department of Military Affairs**; first CDS **Gen Bipin Rawat** (1 Jan 2020, died Dec 2021); then **Gen Anil Chauhan** (from Sept 2022).
- Service chiefs as of 2025: Army – **Gen Upendra Dwivedi**; Navy – **Adm Dinesh K. Tripathi**; Air Force – **ACM A. P. Singh** (check for changes).
- All three service headquarters are in **New Delhi**.

## 2. Days
| Day | Date | Why |
|---|---|---|
| **Army Day** | **15 Jan** | Gen **K. M. Cariappa** became first Indian C-in-C (1949) |
| **Air Force Day** | **8 Oct** | IAF founded 1932 |
| **Navy Day** | **4 Dec** | **Operation Trident** (Karachi, 1971) |
| Armed Forces Flag Day | 7 Dec | |
| **Kargil Vijay Diwas** | **26 Jul** | Op Vijay 1999 |
| **Vijay Diwas** | **16 Dec** | 1971 victory, Bangladesh |
| Territorial Army Day | 9 Oct | |

## 3. Rank equivalents
| Army | Navy | Air Force |
|---|---|---|
| General | Admiral | Air Chief Marshal |
| Lieutenant General | Vice Admiral | Air Marshal |
| Major General | Rear Admiral | Air Vice Marshal |
| Brigadier | Commodore | Air Commodore |
| Colonel | Captain | Group Captain |
| Lieutenant Colonel | Commander | Wing Commander |
| Major | Lieutenant Commander | Squadron Leader |
| Captain | Lieutenant | Flight Lieutenant |
| Lieutenant | Sub Lieutenant | Flying Officer |
**Five-star ranks:** Field Marshal **Sam Manekshaw** (1973) and **K. M. Cariappa** (1986, from **Kodagu**); Marshal of the IAF **Arjan Singh** (2002).

## 4. Commands
- **Army (7):** Northern (Udhampur), Western (Chandimandir), South Western (Jaipur), Southern (Pune), Central (Lucknow), Eastern (Kolkata), Army Training Command (Shimla).
- **Navy (3):** **Western – Mumbai**, **Eastern – Visakhapatnam**, Southern – Kochi (training). Andaman & Nicobar Command (Port Blair) is tri-service.
- **Air Force (7):** Western (New Delhi), Eastern (Shillong), Central (Prayagraj), South Western (Gandhinagar), Southern (Thiruvananthapuram), **Training – Bengaluru**, Maintenance – Nagpur.

## 5. Training and recruitment
NDA **Khadakwasla (Pune)** · IMA **Dehradun** · Indian Naval Academy **Ezhimala** (Kerala) · Air Force Academy **Dundigal** (Hyderabad) · OTA Chennai and Gaya · Sainik Schools (Karnataka: **Kodagu – Kudige**, **Vijayapura**). **Agnipath** (2022): Agniveers serve **4 years**, up to **25%** retained. **NCC** – 1948.

## 6. Gallantry awards
Wartime: **Param Vir Chakra** > Maha Vir Chakra > Vir Chakra. Peacetime: **Ashoka Chakra** > Kirti Chakra > Shaurya Chakra. First PVC: **Major Somnath Sharma** (1947).

## 7. Equipment
| Item | Facts |
|---|---|
| **INS Vikrant** | First indigenous aircraft carrier, **Cochin Shipyard**, commissioned **2 Sep 2022** |
| INS Vikramaditya | Carrier bought from Russia |
| **INS Arihant** | First indigenous nuclear ballistic-missile submarine |
| **INS Kadamba, Karwar** | Project Seabird naval base (Karnataka) |
| **Tejas** | Light Combat Aircraft – **HAL Bengaluru** |
| Rafale | France (Dassault) |
| **Prachand** | Light Combat Helicopter (2022) |
| Arjun | Main battle tank |
| **BrahMos** | Supersonic cruise missile – **India + Russia** |
| Agni / Agni Prime | Ballistic missiles; Agni-V ~5,000 km; **Agni Prime** tested June 2023 |
| Prithvi, Akash, Nag, Trishul | IGMDP (1983, Dr Kalam); **DRDO** founded **1958** |

## 8. Paramilitary and others
- **CAPFs (Home Ministry):** CRPF (largest), BSF (1965), CISF, ITBP, SSB; **Assam Rifles** – oldest (1835).
- **Indian Coast Guard** – 1977, **Ministry of Defence**.

## 9. Operations
| Operation | What |
|---|---|
| Vijay | Goa 1961; Kargil 1999 |
| Trident | Karachi harbour 1971 |
| **Meghdoot** | Siachen 1984 |
| Blue Star | Golden Temple 1984 |
| Ganga / Kaveri / Ajay | Evacuations: Ukraine 2022 / Sudan 2023 / Israel 2023 |
| **Brahma** | Myanmar earthquake relief, March 2025 |
| **Sindoor** | Strikes after the **Pahalgam attack**, May 2025 |
| Sindhu | Evacuation from Iran and Israel, June 2025 |
| Black Forest | Anti-Naxal operation, 2025 |

## 10. Joint exercises
| Exercise | With |
|---|---|
| **Varuna** | France (navy) |
| Garuda / Shakti | France (air / army) |
| **Malabar** | USA, Japan, Australia (navies) |
| **Yudh Abhyas** | USA (army) |
| **Indra** | Russia |
| **Dharma Guardian** | Japan (army) |
| JIMEX | Japan (navy) |
| **Surya Kiran** | Nepal |
| **Mitra Shakti** | Sri Lanka |
| **Agni Warrior** | Singapore (artillery) |
| SIMBEX | Singapore (navy) |
| **Cyclone** | Egypt |
| Nomadic Elephant | Mongolia |
| AUSINDEX | Australia (navy) |
| Tarang Shakti | IAF multinational (2024) |

## 11. Traps
- Army Day 15 Jan, Navy Day 4 Dec, **Air Force Day 8 Oct** – don't mix them up.
- Ashoka Chakra = **peacetime**; PVC = **wartime**.
- Coast Guard is under **Defence**, CAPFs under **Home**.
- Varuna = France, Indra = Russia, Surya Kiran = Nepal, Cyclone = Egypt.
"""}],
}
