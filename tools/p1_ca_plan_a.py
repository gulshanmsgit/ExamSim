"""Paper 1 · Current Affairs · planner topics P1-CA-01 Current International Affairs, P1-CA-02 Current National Affairs and
P1-CA-03 Movies (2 sub-topics × 20 each), with detailed notes for each topic (NOTES, imported into the topic's Notes).
Sources: PIB, MEA, ISRO, Nobel Prize and Booker Prize websites, Directorate of Film Festivals (National Film Awards), news reports
up to mid-2026. Each set mixes REAL previous-year questions from the KEA 2025–26 GK papers, GTTC 2024 GK (official KEA key), VAO and
PSI 2024 and UPSC-coaching entrance tests (answers worked out by ExamSim unless marked official) with new questions. Only facts
that could be checked are used; events that were still unfolding are left out."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

# ---------------------------------------------------------------- CA-01 International
INTL_ORGS = [
    ("Which are the member-countries of Quadrilateral Security Dialogue (QUAD)?\na) India\nb) Japan\nc) USA\nd) Australia\nSelect the correct answer using the codes given below:",
     ["a and c only", "a and b only", "a, b and c only", "a, b, c and d"], 3,
     "The Quad has four members: India, Japan, the USA and Australia." + NOTE, "VAO 2024 Paper-1 · Q11"),
    ("Which of the following pair/pairs of Secretary Generals of UNO and their nations is/are correctly matched?\na) Trygve Lie – Norway\nb) U Thant – Myanmar\nc) Javier Perez de Cuellar – Portugal\nd) Antonio Guterres – Peru",
     ["a only", "a and b only", "a and c only", "a, b, c and d"], 1,
     "Pérez de Cuéllar was from Peru and Guterres is from Portugal – the last two are swapped." + NOTE, "VAO 2024 Paper-1 · Q12"),
    ("Which of the following countries are members of both QUAD as well as Middle East QUAD (I2U2)?\na) India\nb) Australia\nc) USA\nd) UAE",
     ["a and d", "a and c", "c and d", "b and c"], 1,
     "I2U2 = India, Israel, the USA and the UAE; the Quad = India, Japan, the USA and Australia." + NOTE, "PSI 2024 General Paper · Q69"),
    ("On July 4, 2024, which of the following country joined the 'Shanghai Cooperation Organization' (SCO) as a permanent member?",
     ["India", "Belarus", "Iran", "Pakistan"], 1,
     "Belarus became the 10th member at the Astana summit; Iran joined in 2023, India and Pakistan in 2017." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q94"),
    ("Which of the following statements is/are INCORRECT with respect to UN Peace Building Commission (PBC)?\n(a) India has been re-elected to the UN PBC for the 2025-2026 term\n(b) The UN Peace Building Commission was established in 1945\n(c) India is not the founding member of UN PBC\n(d) The PBC serves as a vital link between the UN General Assembly and the Security Council",
     ["a only", "b only", "b and c only", "a and d only"], 2,
     "The PBC was set up in 2005 and India is one of its founding members." + KEY, "GTTC 2024 Asst Gr-II GK · Q97"),
    ("The 14th World Trade Organization's Ministerial Conference (MC14) was held in ____ in March 2026.",
     ["Abu Dhabi, UAE", "Geneva, Switzerland", "Yaounde, Cameroon", "Mumbai, India"], 2,
     "MC13 was held at Abu Dhabi (2024); MC14 was hosted by Cameroon." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q85"),
    ("Which of the following agreement is labelled as \"Mother of All Deals\"? It was concluded on 27th January 2026.",
     ["India-UK CETA", "India-EU Free Trade Agreement", "India-Mauritius CECPA", "India-UAE CEPA"], 1,
     "The India–EU FTA negotiations were concluded at the India–EU summit in New Delhi." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q87"),
    ("Which Pacific island nation has signed the historic Falepili Union Treaty in 2023 with Australia, becoming the first country in the world to plan the relocation of its entire population due to rising sea levels caused by climate change?",
     ["Kiribati", "Tuvalu", "Vanuatu", "Solomon Islands"], 1,
     "Australia offers Tuvalu's citizens a special migration pathway under the treaty." + NOTE, "UPSC coaching entrance 2026 (HK) · Q67"),
    ("Anura Kumara Dissanayake, the current President of Sri Lanka, belongs to which of the following political parties?",
     ["Janatha Vimukthi Peramuna", "United National Party", "Ceylon Workers' Congress", "Democratic People's Front"], 0,
     "He leads the JVP and its alliance, the National People's Power (NPP); he became President in September 2024." + NOTE, "VAO 2024 Paper-1 · Q35"),
    ("Match the following correctly:\nRegions in news recently: a) Kursk  b) Tigray  c) St Martin Island  d) Kachin  e) Nagorno-Karabakh\nCountries related: i. Myanmar  ii. Russia  iii. Azerbaijan  iv. Ethiopia  v. Bangladesh",
     ["a - ii, b - i, c - iii, d - iv, e - v", "a - ii, b - iii, c - v, d - i, e - iv", "a - ii, b - iv, c - v, d - i, e - iii", "a - v, b - iv, c - i, d - ii, e - iii"], 2,
     "Kursk (Russia), Tigray (Ethiopia), St Martin's Island (Bangladesh), Kachin (Myanmar), Nagorno-Karabakh (Azerbaijan)." + NOTE, "PSI 2024 General Paper · Q63"),
    # --- new questions ---
    ("The G20 Leaders' Summit of November 2025, the first held on the African continent, took place in:",
     ["Johannesburg, South Africa", "Rio de Janeiro, Brazil", "New Delhi, India", "Washington, USA"], 0,
     PYQ + "India hosted in 2023 (New Delhi), Brazil in 2024 (Rio); the USA holds the presidency in 2026."),
    ("The 17th BRICS summit (July 2025) was hosted by:",
     ["Brazil, at Rio de Janeiro", "Russia, at Kazan", "South Africa, at Johannesburg", "China, at Xiamen"], 0,
     PYQ + "Indonesia became a full BRICS member in January 2025; India chairs BRICS in 2026."),
    ("COP30, the UN Climate Change Conference of November 2025, was held at:",
     ["Belém, Brazil", "Baku, Azerbaijan", "Dubai, UAE", "Glasgow, UK"], 0,
     PYQ + "COP29 was at Baku (2024) and COP28 at Dubai (2023)."),
    ("The SCO Heads of State summit of 2025 was held at:",
     ["Tianjin, China", "Astana, Kazakhstan", "New Delhi, India", "Moscow, Russia"], 0,
     "The 2024 summit at Astana admitted Belarus as the 10th member."),
    ("The President of the 80th session of the UN General Assembly (2025–26) is:",
     ["Annalena Baerbock of Germany", "Philemon Yang of Cameroon", "Dennis Francis of Trinidad and Tobago", "Csaba Kőrösi of Hungary"], 0,
     "She is the fifth woman to hold the post."),
    ("In May 2025, Cardinal Robert Francis Prevost was elected Pope and took the name:",
     ["Leo XIV", "Francis II", "Benedict XVII", "John Paul III"], 0,
     PYQ + "He is the first Pope from the United States."),
    ("Match the leader with the country (2025):\na. Mark Carney  b. Friedrich Merz  c. Sanae Takaichi  d. Lee Jae-myung\n1. South Korea (President)  2. Japan (first woman Prime Minister)  3. Germany (Chancellor)  4. Canada (Prime Minister)",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "New heads of government are a favourite current-affairs question."),
    ("The India–UK Comprehensive Economic and Trade Agreement (CETA) was signed in:",
     ["July 2025", "January 2024", "March 2026", "December 2022"], 0,
     "The India–EFTA TEPA came into force on 1 October 2025."),
    ("Consider the statements:\nI. The World Health Assembly adopted a Pandemic Agreement in May 2025.\nII. India is a member of the I2U2 grouping.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): The G20 summit of 2025 was historic for Africa.\nReason (R): It was the first G20 summit hosted on the African continent.",
     AR, 0, "South Africa held the G20 presidency in 2025; the African Union became a permanent member in 2023 at New Delhi."),
]

INTL_EVENTS = [
    ("Who got the Nobel Prize in 2023 for developing effective mRNA vaccine for COVID-19 in the field of medicine and physiology?",
     ["Kariko and Weissman", "H. G. Khorana", "Watson and Crick", "Geoffrey E. Hinton"], 0,
     "Katalin Karikó and Drew Weissman; Hinton shared the 2024 Physics prize." + NOTE, "VAO 2024 Paper-1 · Q22"),
    ("Consider the Nobel Prize for Physiology or Medicine, 2025.\n(a) This was awarded by the Nobel Assembly at Pasteur Institute\n(b) The award was given to a group of 3 Scientists\n(c) Contribution was discovery of Peripheral immune tolerance and identification of Regulatory T Cells and FOXP3 genes\n(d) The contribution will help in treating diseases like Cardiac arrest and Obesity.\nHow many of the above statements is/are correct?",
     ["All of them", "Only three of them", "Only two of them", "Only one of them"], 2,
     "(b) and (c) are correct (Mary Brunkow, Fred Ramsdell, Shimon Sakaguchi). The medicine prize is awarded by the Nobel Assembly at the Karolinska Institutet, and the work matters for autoimmune diseases, cancer and transplants." + NOTE,
     "KEA 2025 GK (HK, 21 Dec 2025) · Q58"),
    ("Which female writer won the prestigious Booker Prize for literature in 2024 and from which country does she hail?",
     ["Samantha Harvey - U.K.", "Arundhati Roy - India", "Rachel Kushner - U.S.", "Margaret Atwood - Canada"], 0,
     "She won for the novel 'Orbital'." + KEY, "GTTC 2024 Asst Gr-II GK · Q93"),
    ("Gobekli Tepe which was in the news recently is a place related to:",
     ["Archaeological site in Turkey", "Conflict zone in Ukraine", "Dark oxygen was discovered in Pacific Ocean", "Missile testing site in Iran"], 0,
     "It is a Neolithic site about 11,000 years old and a UNESCO World Heritage Site." + NOTE, "PSI 2024 General Paper · Q66"),
    ("WHO declares Monkeypox (Mpox) outbreak a public health emergency of international concern. In this regard which of the following statements are correct?\na) Monkeypox virus belongs to the same family of viruses as smallpox virus\nb) This disease spreads through direct skin-to-skin contact\nc) It is a zoonotic disease also\nd) Monkeypox variants are called as clades",
     ["Only a and c are correct", "Only a, b and c are correct", "Only a, c and d are correct", "a, b, c and d are correct"], 3,
     "Mpox is an orthopoxvirus (like smallpox), zoonotic, spread by close contact, and its variants are called clades (Ib caused the 2024 emergency)." + NOTE,
     "PSI 2024 General Paper · Q61"),
    ("Against whom did Carlos Alcaraz win 2024 Men's singles Wimbledon Tennis Title and belongs to which country?",
     ["Novak Djokovic - Spain", "Rafael Nadal - Spain", "Roger Federer - Switzerland", "Novak Djokovic - Serbia"], 0,
     "Alcaraz (Spain) beat Novak Djokovic in the 2024 final." + NOTE, "PSI 2024 General Paper · Q90"),
    ("Who among the following carried Indian flag during the closing ceremony of Paris Olympics-2024?",
     ["Manu Bhaker & P.R. Sreejesh", "Neeraj Chopra & P.R. Sreejesh", "Manu Bhaker & Vinesh Phogat", "Swapnil Kusale & Aman Sehrawat"], 0,
     "Manu Bhaker won two bronze medals; Sreejesh retired after the hockey bronze." + NOTE, "VAO 2024 Paper-1 · Q26"),
    ("Consider the following statements with respect to Paralympics - 2024.\na) Paralympics games were held in Paris, the capital of France.\nb) Paralympics games are held once in 5 years.\nc) For the first time Indian sportspersons have secured more medals in Paralympics - 2024.\nd) China, Britain and USA respectively are the three countries which have won the highest number of medals.",
     ["a, c and d are correct", "b, c and d are correct", "a, b and d are correct", "a and c are correct"], 0,
     "The Paralympics are held every 4 years; India won a record 29 medals (7 gold) at Paris 2024." + NOTE, "VAO 2024 Paper-1 · Q28"),
    # --- new questions ---
    ("The Nobel Peace Prize 2025 was awarded to:",
     ["María Corina Machado of Venezuela", "Nihon Hidankyo of Japan", "Narges Mohammadi of Iran", "The World Food Programme"], 0,
     PYQ + "Nihon Hidankyo won in 2024, Narges Mohammadi in 2023."),
    ("The Nobel Prize in Literature 2025 was awarded to the Hungarian writer:",
     ["László Krasznahorkai", "Han Kang", "Jon Fosse", "Annie Ernaux"], 0,
     "Han Kang (South Korea) won in 2024."),
    ("The Nobel Prize in Chemistry 2025 (Kitagawa, Robson and Yaghi) recognised the development of:",
     ["Metal–organic frameworks (MOFs)", "Protein structure prediction", "CRISPR gene editing", "Quantum dots"], 0,
     "Physics 2025 went to Clarke, Devoret and Martinis for macroscopic quantum tunnelling in electric circuits."),
    ("The International Booker Prize 2025 was won by 'Heart Lamp', a collection of short stories originally written in Kannada by:",
     ["Banu Mushtaq (translated by Deepa Bhasthi)", "Vivek Shanbhag", "S. L. Bhyrappa", "Geetanjali Shree"], 0,
     PYQ + "It was the first Kannada book to win; Geetanjali Shree's 'Tomb of Sand' (Hindi) won in 2022."),
    ("The Booker Prize 2025 was won by the Hungarian-British author David Szalay for the novel:",
     ["Flesh", "Orbital", "Prophet Song", "The Seven Moons of Maali Almeida"], 0,
     "Orbital won in 2024 (Samantha Harvey)."),
    ("In December 2024, D. Gukesh became the youngest undisputed World Chess Champion by defeating:",
     ["Ding Liren of China", "Magnus Carlsen of Norway", "Ian Nepomniachtchi", "Fabiano Caruana"], 0,
     PYQ + "In July 2025, Divya Deshmukh won the FIDE Women's World Cup, beating Koneru Humpy in the final."),
    ("The ICC World Test Championship final of June 2025 at Lord's was won by:",
     ["South Africa", "Australia", "India", "New Zealand"], 0,
     "India won the ICC Champions Trophy in March 2025 (final at Dubai)."),
    ("India won its first ICC Women's ODI World Cup in November 2025 by defeating in the final:",
     ["South Africa", "Australia", "England", "New Zealand"], 0,
     "The final was played at Navi Mumbai."),
    ("Wimbledon 2025 singles champions were:",
     ["Jannik Sinner (men) and Iga Świątek (women)", "Carlos Alcaraz and Barbora Krejčíková", "Novak Djokovic and Aryna Sabalenka", "Daniil Medvedev and Coco Gauff"], 0,
     "Alcaraz won Wimbledon in 2023 and 2024."),
    ("Assertion (A): The 2025 International Booker Prize was a landmark for Kannada literature.\nReason (R): Banu Mushtaq's 'Heart Lamp' was the first Kannada work to win it.",
     AR, 0, "The prize is shared equally by author and translator."),
    ("Consider the statements:\nI. The 2024 Summer Olympics and Paralympics were held in Paris.\nII. The 2028 Summer Olympics will be held in Los Angeles.\nWhich is/are correct?",
     I_II, 2, "Brisbane will host the 2032 Games."),
    ("Match the 2025 Nobel Prize with its subject:\na. Physics  b. Chemistry  c. Medicine  d. Economics\n1. Innovation-driven economic growth (Mokyr, Aghion, Howitt)  2. Peripheral immune tolerance  3. Metal–organic frameworks  4. Macroscopic quantum tunnelling",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Nobel matching appears in almost every GK paper."),
]

# ---------------------------------------------------------------- CA-02 National
NAT_GOV = [
    ("Pradhana Mantri Suraksha Bima Yojana (PMSBY) is a",
     ["Government backed accident insurance scheme", "Only scheme for rural landless households", "Government health insurance programme", "The scheme meant for child life insurance"], 0,
     "PMSBY gives accident cover of ₹2 lakh for a small yearly premium; PMJJBY is the life-insurance scheme." + KEY, "GTTC 2024 Asst Gr-II GK · Q94"),
    ("The three categories of loans under MUDRA scheme are",
     ["Shishu, Kishor, Uttam", "Suvid, Uttam, Kishor", "Shishu, Kishor, Tarun", "Uttam, Tarun, Suvid"], 2,
     "Shishu (up to ₹50,000), Kishor and Tarun; Tarun Plus (up to ₹20 lakh) was added in 2024." + NOTE, "VAO 2024 Paper-1 · Q92"),
    ("AMRUT - Expand.",
     ["Atal Mission for Rehabilitation and Urban Transformation", "Atal Mission for Rejuvenation and Urban Transportation", "Atal Mission for Rejuvenation and Urban Transformation", "Atal Mission for Regeneration and Urban Transportation"], 2,
     "AMRUT was launched in 2015; AMRUT 2.0 in 2021." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q26"),
    ("India's LVM3 launch vehicle has successfully launched the CMS-03 satellite on November 02, 2025. CMS-03 is a ____ satellite.",
     ["Navigation", "Communication", "Remote sensing", "Astronomical"], 1,
     "CMS-03, a multi-band communication satellite of about 4,400 kg, was the heaviest launched from India." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q95"),
    ("Which of the Indian states was in news recently for declaring as the first 'Indian state free of extreme poverty'?",
     ["Tamil Nadu", "Kerala", "Karnataka", "Tripura"], 1,
     "Kerala made the declaration on 1 November 2025 (Kerala Piravi)." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q73"),
    ("As of December 2025, who is the Union Minister of Cooperation for Government of India?",
     ["Shri Shivaraj Singh Chouhan", "Shri Amit Shah", "Shri Arjun Ram Meghwal", "Shri V. Somanna"], 1,
     "The Ministry of Cooperation was created in 2021; Amit Shah also holds Home Affairs." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q34"),
    ("The Bhojshala complex, which was recently in the news regarding a High Court directive for an ASI survey, is located in which State?",
     ["Uttar Pradesh", "Madhya Pradesh", "Chhattisgarh", "Rajasthan"], 1,
     "It is at Dhar in Madhya Pradesh." + NOTE, "UPSC coaching entrance 2026 (HK) · Q49"),
    ("Who among the following were the Chief Guests of India's 77th Republic Day celebrations held on 26.01.2026?\n(a) Prabowo Subianto\n(b) Emmanuel Macron\n(c) Antonio Luis Santos da Costa\n(d) Ursula von der Leyen",
     ["(c) and (d)", "(a) and (b)", "(a) and (c)", "(a) and (d)"], 0,
     "The two EU leaders – European Council President António Costa and Commission President von der Leyen – were the chief guests; Prabowo (2025) and Macron (2024) came earlier." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q86"),
    # --- new questions ---
    ("'Operation Sindoor' (May 2025) was:",
     ["India's precision strikes on terror infrastructure in Pakistan and PoK after the Pahalgam attack", "A rescue of Indians from Sudan", "A flood-relief operation in Kerala", "A naval exercise with Japan"], 0,
     PYQ + "Operation Kaveri (2023) evacuated Indians from Sudan; Operation Ajay (2023) from Israel."),
    ("Group Captain Shubhanshu Shukla became the first Indian to visit the International Space Station in June 2025 on the mission:",
     ["Axiom Mission 4 (Ax-4)", "Gaganyaan G1", "Artemis II", "Chandrayaan-4"], 0,
     PYQ + "Rakesh Sharma (1984) was the first Indian in space."),
    ("NISAR, launched on GSLV-F16 in July 2025, is an Earth-observation satellite built jointly by:",
     ["NASA and ISRO", "ESA and ISRO", "JAXA and ISRO", "Roscosmos and ISRO"], 0,
     "It uses dual-frequency (L- and S-band) synthetic aperture radar."),
    ("In September 2025, C. P. Radhakrishnan was elected as India's:",
     ["15th Vice-President", "16th President", "Chief Justice", "Chief Election Commissioner"], 0,
     "The election followed Jagdeep Dhankhar's resignation in July 2025."),
    ("Justice Surya Kant took office in November 2025 as the:",
     ["53rd Chief Justice of India", "52nd Chief Justice of India", "Chairperson of the NHRC", "Lokpal"], 0,
     "Justice B. R. Gavai was the 52nd CJI (May–November 2025)."),
    ("Under the 'next-generation' GST reform effective 22 September 2025, the main GST slabs became:",
     ["5% and 18% (with a special 40% rate on a few items)", "0%, 12% and 28% only", "A single 15% rate", "10% and 20%"], 0,
     PYQ + "The 12% and 28% slabs were largely merged."),
    ("Match the person with the post (2025):\na. Sanjay Malhotra  b. Gyanesh Kumar  c. Surya Kant  d. C. P. Radhakrishnan\n1. Vice-President of India  2. Chief Justice of India  3. Chief Election Commissioner  4. RBI Governor",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Who's who questions are very common."),
    ("The Maha Kumbh Mela of 2025 was held at:",
     ["Prayagraj, from 13 January to 26 February 2025", "Haridwar", "Nashik", "Ujjain"], 0,
     "The Kumbh Mela is on UNESCO's Intangible Cultural Heritage list (2017)."),
    ("Consider the statements:\nI. The Waqf (Amendment) Act was passed in 2025.\nII. The next Census will also count castes.\nWhich is/are correct?",
     I_II, 2, "Both are correct; the Census reference date is 1 March 2027 (1 October 2026 for snow-bound areas)."),
    ("Assertion (A): CMS-03 was launched by LVM3 rather than PSLV.\nReason (R): LVM3 is ISRO's heaviest launch vehicle, able to place about 4 tonnes in geosynchronous transfer orbit.",
     AR, 0, "Heavy communication satellites need LVM3."),
    ("Which mission launched in 2023 placed India's first space-based solar observatory at the L1 point?",
     ["Aditya-L1", "Chandrayaan-3", "XPoSat", "NISAR"], 0,
     "Chandrayaan-3 landed near the Moon's south pole on 23 August 2023 – now National Space Day."),
    ("PM-JANMAN (2023) is a mission for the development of:",
     ["Particularly Vulnerable Tribal Groups (PVTGs)", "Urban street vendors", "Small industries", "Coastal fishermen"], 0,
     "India has 75 PVTGs, including the Koraga and Jenu Kuruba of Karnataka."),
]

NAT_PEOPLE = [
    ("Who is the Asia's first female Loco Pilot who retired recently?",
     ["Shanthi Swarooparani", "Surekha Yadav", "Shashikala Malhotra", "Rekha Bai"], 1,
     "Surekha Yadav of Central Railway retired in September 2025 after 36 years of service." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q19"),
    ("In which of the following sports, Aditi Swami and Ojas Deotale had won India's first ever individual gold medals at the World Championship-2023?",
     ["Archery", "Badminton", "Shooting", "Table Tennis"], 0,
     "They won the compound archery world titles in Berlin (2023)." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q20"),
    ("Name the Kannada writer who has won the Kendra Sahitya Akademi Award-2024 for the book 'Nudigala Alivu'?",
     ["Lakshmisha Tolpadi", "K.V. Narayana", "K.G. Nagarajappa", "H.S. Venkateshamurthy"], 1,
     "K. V. Narayana won for his collection of essays 'Nudigala Alivu'." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q93"),
    ("India defeated Pakistan to win the trophy in the Asia Cup final match held on September 28, 2025. The venue of this match was:",
     ["Dubai", "Abu Dhabi", "Colombo", "Dhaka"], 0,
     "The final was at the Dubai International Cricket Stadium." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q67"),
    ("Sri Siddaramaiah, the Chief Minister of Karnataka, on January 6, 2026 equalled the record as the longest serving Chief Minister of Karnataka. The Chief Minister was ____ and days were ____",
     ["D. Devaraj Urs, 2775", "B.S. Yediyurappa, 2792", "D. Devaraj Urs, 2792", "B.S. Yediyurappa, 2775"], 2,
     "D. Devaraj Urs served 2,792 days as Chief Minister." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q89"),
    ("M.S. Swaminathan, who is regarded as the \"Father of India's Green Revolution\", has recently passed away. Which of the following award/awards he has received?\n(a) Ramon Magsaysay Award  (b) Bharat Ratna\n(c) Albert Einstein Award  (d) Padmashree",
     ["b only", "a, b, c and d", "c only", "a only"], 1,
     "He received the Padma Shri (1967), Magsaysay (1971), Albert Einstein World Science Award (1986) and the Bharat Ratna (2024, posthumously)." + KEY,
     "GTTC 2024 Asst Gr-II GK · Q64"),
    # --- new questions ---
    ("The Bharat Ratna for 2024 was conferred on:",
     ["Karpoori Thakur, L. K. Advani, P. V. Narasimha Rao, Chaudhary Charan Singh and M. S. Swaminathan", "Only L. K. Advani", "Ratan Tata and Lata Mangeshkar", "Pranab Mukherjee and Nanaji Deshmukh"], 0,
     PYQ + "Five awards in one year – the highest ever."),
    ("The 2023 Dadasaheb Phalke Award, announced in 2025, went to:",
     ["Mohanlal", "Mithun Chakraborty", "Waheeda Rehman", "Asha Parekh"], 0,
     "Mithun Chakraborty received the 2022 award (presented in 2024)."),
    ("The 'Swachh Survekshan' cleanliness rankings, in which Indore has repeatedly been the cleanest city, are released by the:",
     ["Ministry of Housing and Urban Affairs", "Ministry of Health", "NITI Aayog", "Ministry of Tourism"], 0,
     "Swachh Bharat Mission was launched on 2 October 2014."),
    ("In the 2025 Bihar Assembly election, the alliance that won a majority was the:",
     ["NDA, with Nitish Kumar continuing as Chief Minister", "Mahagathbandhan", "A third front", "No alliance – President's Rule"], 0,
     "Results were declared in November 2025."),
    ("Who became the first Indian woman to win the FIDE Women's World Cup (July 2025)?",
     ["Divya Deshmukh", "Koneru Humpy", "R. Vaishali", "Harika Dronavalli"], 0,
     "She also earned the Grandmaster title with the win."),
    ("Neeraj Chopra won ____ at the Paris Olympics 2024 in javelin throw.",
     ["Silver", "Gold", "Bronze", "No medal"], 0,
     "He won gold at Tokyo 2020; Arshad Nadeem of Pakistan won gold in Paris."),
    ("India's tally at the Paris 2024 Olympics was:",
     ["6 medals – 1 silver and 5 bronze", "7 medals including 1 gold", "4 medals – 2 silver, 2 bronze", "10 medals"], 0,
     "Tokyo 2020 remains India's best (7 medals, 1 gold)."),
    ("The 2025 'Khelo India' events help mainly to:",
     ["Identify and develop young sporting talent across India", "Regulate cricket boards", "Build airports", "Conduct board exams"], 0,
     "Khelo India Youth, University, Para, Winter and Beach Games are held."),
    ("Match the person with the field:\na. Surekha Yadav  b. K. V. Narayana  c. Divya Deshmukh  d. Shubhanshu Shukla\n1. Space – Axiom-4 mission  2. Chess  3. Kannada literature (Sahitya Akademi)  4. Railways – Asia's first woman loco pilot",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Persons-in-news matching."),
    ("Consider the statements:\nI. D. Devaraj Urs holds the record for the longest tenure as Karnataka Chief Minister (equalled in January 2026).\nII. K. V. Narayana won the Kendra Sahitya Akademi award 2024 for Kannada.\nWhich is/are correct?",
     I_II, 2, "Both are from the KEA 2026 papers."),
    ("Assertion (A): M. S. Swaminathan is called the Father of India's Green Revolution.\nReason (R): He led the introduction of high-yielding wheat and rice varieties in the 1960s.",
     AR, 0, "He received the Bharat Ratna in 2024."),
    ("Which state's 'Gruha Lakshmi' and 'Shakti' schemes are among its five guarantee schemes launched in 2023?",
     ["Karnataka", "Kerala", "Telangana", "Tamil Nadu"], 0,
     "The five are Gruha Jyothi, Gruha Lakshmi, Anna Bhagya, Shakti (free bus travel for women) and Yuva Nidhi."),
    ("The 2025 International Booker winner Banu Mushtaq hails from:",
     ["Hassan, Karnataka", "Mysuru, Karnataka", "Kochi, Kerala", "Hyderabad, Telangana"], 0,
     "She is a lawyer, activist and Kannada writer of the Bandaya movement."),
    ("India's first indigenous aircraft carrier, commissioned in 2022, is:",
     ["INS Vikrant", "INS Vikramaditya", "INS Arihant", "INS Vishal"], 0,
     "It was built by Cochin Shipyard."),
]

# ---------------------------------------------------------------- CA-03 Movies
FILM_AWARDS = [
    ("Based on 71st National Film Awards, match the following:\nList-I (Winner): (a) Rani Mukherji  (b) Vikrant Massey  (c) Shah Rukh Khan  (d) Sudipto Sen\nList-II (Film): (i) The Kerala Story  (ii) 12th Fail  (iii) Jawan  (iv) Mrs. Chatterjee Vs. Norway  (v) Parking",
     ["a-iv, b-ii, c-iii, d-i", "a-iv, b-v, c-iii, d-i", "a-v, b-ii, c-iv, d-iii", "a-iii, b-iv, c-ii, d-i"], 0,
     "Best Actress – Rani Mukerji; Best Actor shared by Vikrant Massey (12th Fail) and Shah Rukh Khan (Jawan); Best Director – Sudipto Sen (The Kerala Story)." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q100"),
    ("Which of the following statements about Kannada movie \"Kandeelu\" are incorrect?\na. The movie was directed by Yashoda Prakash.\nb. It was awarded with National Film Award in the category of Best Feature Film in Kannada during 70th National Film Awards Ceremony.\nc. The movie was directed by Girish Kasaravalli.",
     ["a, b and c", "b and c", "a and b", "a and c"], 1,
     "Kandeelu, directed by Yashoda Prakash, won Best Kannada Film at the 71st (not 70th) awards; KGF Chapter 2 won at the 70th." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q81"),
    ("The first Kannada cinema artist who received the prestigious 'Dadasaheb Phalke' Award is:",
     ["Vishnuvardhan", "Ambareesh", "K.S. Ashwath", "Dr. Rajkumar"], 3,
     "Dr Rajkumar received it for 1995; Puttanna Kanagal never received it." + NOTE, "KRIES 2024 entrance · Q90"),
    # --- new questions ---
    ("The National Film Awards are presented by the President and conducted by the:",
     ["Ministry of Information and Broadcasting (through the National Film Development Corporation)", "Ministry of Culture", "Film Federation of India", "Central Board of Film Certification"], 0,
     PYQ + "Winners of the top awards receive the Swarna Kamal or Rajat Kamal."),
    ("The Best Feature Film at the 71st National Film Awards (announced August 2025) was:",
     ["12th Fail", "Jawan", "Aattam", "Kantara"], 0,
     "Rocky Aur Rani Kii Prem Kahaani won Best Popular Film providing wholesome entertainment."),
    ("At the 70th National Film Awards (August 2024), Rishab Shetty won Best Actor for:",
     ["Kantara", "777 Charlie", "KGF Chapter 2", "Sapta Sagaradaache Ello"], 0,
     PYQ + "KGF Chapter 2 won Best Kannada Film; Kantara won Best Popular Film."),
    ("The Best Feature Film at the 70th National Film Awards was the Malayalam film:",
     ["Aattam", "Manjummel Boys", "2018", "Premalu"], 0,
     "Nithya Menen and Manasi Parekh shared Best Actress."),
    ("The Dadasaheb Phalke Award is India's highest award in cinema. It was instituted in:",
     ["1969, and first given to Devika Rani", "1913", "1954, to Satyajit Ray", "1980, to Raj Kapoor"], 0,
     PYQ + "Dadasaheb Phalke made Raja Harishchandra (1913), India's first full-length feature film."),
    ("The first Kannada talkie film (1934) was:",
     ["Sati Sulochana", "Bhakta Dhruva", "Bedara Kannappa", "Samskara"], 0,
     PYQ + "Bedara Kannappa (1954) was Dr Rajkumar's first film as a hero."),
    ("India's first sound film (talkie), released in 1931, was:",
     ["Alam Ara", "Raja Harishchandra", "Kisan Kanya", "Mother India"], 0,
     "It was directed by Ardeshir Irani. Kisan Kanya (1937) was the first Indian colour film."),
    ("The Kannada film 'Samskara' (1970), which won the President's Gold Medal, was based on the novel by:",
     ["U. R. Ananthamurthy", "S. L. Bhyrappa", "Shivaram Karanth", "Kuvempu"], 0,
     "It is regarded as a landmark of the Kannada new-wave cinema."),
    ("Match the Kannada film-maker with a famous film:\na. Puttanna Kanagal  b. Girish Kasaravalli  c. Shankar Nag  d. Rishab Shetty\n1. Kantara  2. Ondanondu Kaladalli  3. Ghatashraddha  4. Nagarahavu",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Girish Kasaravalli has won the most National Awards for Best Feature Film among directors."),
    ("Consider the statements:\nI. Dr Rajkumar was the first Kannada artist to receive the Dadasaheb Phalke Award.\nII. Dr Rajkumar also won the National Award for Best Male Playback Singer.\nWhich is/are correct?",
     I_II, 2, "He won the playback award for 'Naadamaya' (Jeevana Chaitra, 1992)."),
    ("Assertion (A): Shah Rukh Khan received his first National Film Award in 2025.\nReason (R): He shared the Best Actor award at the 71st National Film Awards for 'Jawan'.",
     AR, 0, "He shared it with Vikrant Massey."),
    ("The Kannada actor known as 'Power Star', who died in 2021 and was posthumously given the Karnataka Ratna, was:",
     ["Puneeth Rajkumar", "Shiva Rajkumar", "Darshan", "Sudeep"], 0,
     "He was the youngest son of Dr Rajkumar."),
    ("The Karnataka State Film Awards are presented by the:",
     ["Government of Karnataka (Department of Information and Public Relations)", "Ministry of I&B", "Karnataka Film Chamber of Commerce only", "Sahitya Akademi"], 0,
     "The Bengaluru International Film Festival (BIFFes) is organised by the Karnataka Chalanachitra Academy."),
    ("Which of these is India's oldest international film festival, held each November in Goa?",
     ["IFFI (International Film Festival of India)", "BIFFes", "MAMI Mumbai", "Kolkata International Film Festival"], 0,
     PYQ + "IFFI began in 1952; Goa has been its permanent venue since 2004."),
    ("Puttanna Kanagal's 'Nagarahavu' (1972) made a star of:",
     ["Vishnuvardhan", "Ambareesh", "Anant Nag", "Ravichandran"], 0,
     "It was based on T. R. Subbanna's novels."),
    ("Which statement about the 70th and 71st National Film Awards is correct?",
     ["KGF Chapter 2 won Best Kannada Film at the 70th; Kandeelu at the 71st", "Kandeelu won Best Feature Film at the 70th", "Kantara won Best Feature Film at the 71st", "12th Fail won Best Kannada Film"], 0,
     "Compare the two ceremonies carefully – a favourite trap."),
    ("The Best Popular Film Providing Wholesome Entertainment at the 71st National Film Awards was:",
     ["Rocky Aur Rani Kii Prem Kahaani", "Kantara", "Jawan", "12th Fail"], 0,
     "Kantara won this award at the 70th National Film Awards."),
]

FILM_WORLD = [
    ("The Academy Awards (Oscars) are given by the:",
     ["Academy of Motion Picture Arts and Sciences, USA", "British Academy (BAFTA)", "Cannes Film Festival jury", "UNESCO"], 0,
     PYQ + "The first ceremony was held in 1929."),
    ("'Naatu Naatu' from RRR won the Oscar in 2023 for:",
     ["Best Original Song (M. M. Keeravani and Chandrabose)", "Best Picture", "Best Documentary", "Best Visual Effects"], 0,
     PYQ + "'The Elephant Whisperers' won Best Documentary Short the same year."),
    ("'The Elephant Whisperers', which won the 2023 Oscar for Best Documentary Short, was directed by:",
     ["Kartiki Gonsalves", "Payal Kapadia", "Zoya Akhtar", "Shaunak Sen"], 0,
     "It is set in the Mudumalai Tiger Reserve, Tamil Nadu."),
    ("At the 97th Academy Awards (March 2025), Best Picture went to:",
     ["Anora", "Oppenheimer", "The Brutalist", "Emilia Pérez"], 0,
     "Sean Baker won Best Director; Mikey Madison Best Actress; Adrien Brody Best Actor."),
    ("Payal Kapadia's 'All We Imagine as Light' won which award at Cannes 2024?",
     ["Grand Prix (second-highest award)", "Palme d'Or", "Best Actor", "Caméra d'Or"], 0,
     PYQ + "It was the first Indian film in the main competition in 30 years."),
    ("The Palme d'Or at the Cannes Film Festival 2025 was won by Jafar Panahi's:",
     ["It Was Just an Accident", "Anora", "Anatomy of a Fall", "Triangle of Sadness"], 0,
     "Anora won the Palme d'Or in 2024."),
    ("Anasuya Sengupta became the first Indian to win Best Actress in the Un Certain Regard section at Cannes 2024 for:",
     ["The Shameless", "Santosh", "Girls Will Be Girls", "All We Imagine as Light"], 0,
     "Un Certain Regard is a parallel competitive section of Cannes."),
    ("The first Indian to win an Academy Award was:",
     ["Bhanu Athaiya, for costume design in Gandhi (1983)", "Satyajit Ray", "A. R. Rahman", "Resul Pookutty"], 0,
     PYQ + "Satyajit Ray received an honorary Oscar in 1992; A. R. Rahman won two Oscars for Slumdog Millionaire (2009)."),
    ("The Golden Bear is the top prize of the:",
     ["Berlin International Film Festival", "Venice Film Festival", "Cannes Film Festival", "Toronto Film Festival"], 0,
     "Venice gives the Golden Lion; Cannes the Palme d'Or."),
    ("Match the film award with the country where it is given:\na. Oscar  b. BAFTA  c. Golden Lion  d. Palme d'Or\n1. France  2. Italy  3. United Kingdom  4. USA",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Award–country matching."),
    ("India's official entry for the Oscars is chosen by the:",
     ["Film Federation of India", "Ministry of I&B", "CBFC", "Prasar Bharati"], 0,
     "Laapataa Ladies was India's entry for the 2025 Oscars."),
    ("The Central Board of Film Certification (CBFC) certifies films under the:",
     ["Cinematograph Act, 1952", "Copyright Act, 1957", "Information Technology Act, 2000", "Press Council Act, 1978"], 0,
     "The 2023 amendment added UA 7+, UA 13+ and UA 16+ categories."),
    ("The 2025 Kannada film 'Kantara: Chapter 1' is a prequel directed by and starring:",
     ["Rishab Shetty", "Raj B. Shetty", "Rakshit Shetty", "Yash"], 0,
     "It is set in the coastal Tulu Nadu tradition of daiva worship."),
    ("The National Film Archive of India is located at:",
     ["Pune", "Mumbai", "Chennai", "Kolkata"], 0,
     "The Film and Television Institute of India (FTII) is also in Pune."),
    ("Consider the statements:\nI. 'Naatu Naatu' was the first song from an Indian film to win the Oscar for Best Original Song.\nII. 'Jai Ho' (Slumdog Millionaire) also won the Best Original Song Oscar.\nWhich is/are correct?",
     I_II, 2, "Both are true: Jai Ho won in 2009 for the British film Slumdog Millionaire, so Naatu Naatu was the first winner from an Indian production."),
    ("Assertion (A): Payal Kapadia's film won the Grand Prix at Cannes 2024.\nReason (R): The Grand Prix is the highest award at Cannes.",
     AR, 2, "The highest award is the Palme d'Or; the Grand Prix is second, so R is false."),
    ("Who received the Dadasaheb Phalke Award for the year 2021?",
     ["Waheeda Rehman", "Asha Parekh", "Rajinikanth", "Amitabh Bachchan"], 0,
     "Asha Parekh (2020), Waheeda Rehman (2021), Mithun Chakraborty (2022), Mohanlal (2023)."),
    ("The famous dialogue-free Kannada film 'Pushpaka Vimana' (1987) starred:",
     ["Kamal Haasan", "Dr Rajkumar", "Vishnuvardhan", "Shankar Nag"], 0,
     "It was directed by Singeetham Srinivasa Rao."),
    ("Which award did 'The Elephant Whisperers' and 'Naatu Naatu' bring India in 2023?",
     ["Two Oscars in one night", "Two Golden Globes", "Two Palme d'Ors", "Two BAFTAs"], 0,
     "Naatu Naatu also won the Golden Globe for Best Original Song."),
    ("A biopic on 'Super 30' founder Anand Kumar, and '12th Fail' on IPS officer Manoj Kumar Sharma, are examples of films based on:",
     ["Real-life stories of educators and officers", "Mythology", "Science fiction", "Historical kings"], 0,
     "12th Fail was directed by Vidhu Vinod Chopra."),
]

TOPICS = {
    "Current International Affairs": [("1 · Organisations, Summits and Diplomacy", INTL_ORGS),
                                      ("2 · World Events, Awards and Sports", INTL_EVENTS)],
    "Current National Affairs": [("1 · Governance, Schemes, Science and Defence", NAT_GOV),
                                 ("2 · Persons, Awards, Karnataka and Sports", NAT_PEOPLE)],
    "Movies": [("1 · National Film Awards and Kannada Cinema", FILM_AWARDS),
               ("2 · Oscars, Festivals and World Cinema", FILM_WORLD)],
}

NOTES = {
    "Current International Affairs": [{"title": "International affairs 2024–26 – revision notes", "md": """# Current international affairs (2024 – mid-2026)

> How to use: read once, then revise the tables. KEA asks *who / where / which country / which edition*. Facts are as reported up to mid-2026; check the newspaper for anything newer.

## 1. Groupings and summits
| Grouping | Members / key facts | Recent summit (host) |
|---|---|---|
| **G20** | 19 countries + EU + **African Union** (permanent member since New Delhi summit, Sept 2023) | 2023 New Delhi (India) · 2024 Rio de Janeiro (Brazil) · **2025 Johannesburg (South Africa) – first in Africa** · 2026 USA |
| **BRICS** | Brazil, Russia, India, China, South Africa + Egypt, Ethiopia, Iran, UAE (2024) + **Indonesia (Jan 2025)** | 2024 Kazan (Russia) · **2025 Rio de Janeiro (Brazil)** · **2026 – India chairs** |
| **SCO** | 10 members: China, Russia, India, Pakistan, Kazakhstan, Kyrgyzstan, Tajikistan, Uzbekistan, Iran (2023), **Belarus (4 July 2024, Astana)** | 2024 Astana · **2025 Tianjin (China)** |
| **Quad** | India, Japan, USA, Australia | — |
| **I2U2** ("West Asian Quad") | India, Israel, USA, UAE | Common with Quad: **India & USA** |
| **UN Peacebuilding Commission** | Set up **2005**; India a **founding member**; re-elected for 2025–26 | Link between UNGA and UNSC |
| **WTO Ministerial** | MC13 Abu Dhabi (2024) · **MC14 Yaoundé, Cameroon (March 2026)** | |
| **UN Climate (COP)** | COP28 Dubai (2023) · COP29 Baku (2024) · **COP30 Belém, Brazil (Nov 2025)** | |

## 2. United Nations
- **Secretary-General:** António Guterres (Portugal), 9th SG, since 2017. Earlier: Trygve Lie (Norway, 1st), U Thant (Myanmar), Kurt Waldheim (Austria), **Javier Pérez de Cuéllar (Peru)**, Boutros Boutros-Ghali (Egypt), Kofi Annan (Ghana), Ban Ki-moon (South Korea).
- **President, 80th UNGA (2025–26):** Annalena Baerbock (Germany).
- WHO: **Pandemic Agreement** adopted by the World Health Assembly, **May 2025**. Mpox declared a public-health emergency of international concern in **Aug 2024** (clade Ib).

## 3. Leaders in the news
| Country | Leader (post, from) |
|---|---|
| USA | Donald Trump – 47th President (20 Jan 2025) |
| Vatican | **Pope Leo XIV** (Robert Prevost, elected 8 May 2025 – first American Pope) |
| Sri Lanka | Anura Kumara Dissanayake – President (Sept 2024), **JVP / NPP** |
| Canada | Mark Carney – PM (March 2025) |
| Germany | Friedrich Merz – Chancellor (May 2025) |
| Japan | **Sanae Takaichi** – first woman PM (Oct 2025) |
| South Korea | Lee Jae-myung – President (June 2025) |
| UK | Keir Starmer – PM (July 2024) |

## 4. Trade deals
- **India–UK CETA** signed **24 July 2025**.
- **India–EFTA TEPA** in force **1 Oct 2025** (Switzerland, Norway, Iceland, Liechtenstein).
- **India–EU FTA** – called the **"mother of all deals"**, concluded **27 Jan 2026**; the EU leaders **António Costa** and **Ursula von der Leyen** were chief guests on Republic Day 2026.

## 5. Nobel Prizes
| Year | Peace | Literature | Medicine | Physics | Chemistry | Economics |
|---|---|---|---|---|---|---|
| 2023 | Narges Mohammadi (Iran) | Jon Fosse | **Karikó & Weissman (mRNA vaccines)** | Agostini, Krausz, L'Huillier (attosecond) | Bawendi, Brus, Ekimov (quantum dots) | Claudia Goldin |
| 2024 | Nihon Hidankyo (Japan) | Han Kang (S. Korea) | Ambros & Ruvkun (microRNA) | Hopfield & **Hinton** (AI) | Baker, Hassabis, Jumper (proteins) | Acemoglu, Johnson, Robinson |
| 2025 | **María Corina Machado** (Venezuela) | **László Krasznahorkai** (Hungary) | **Brunkow, Ramsdell, Sakaguchi** – peripheral immune tolerance, regulatory T cells, FOXP3 (awarded by the Nobel Assembly at **Karolinska Institutet**) | Clarke, Devoret, Martinis (macroscopic quantum tunnelling) | Kitagawa, Robson, Yaghi (**MOFs**) | Mokyr, Aghion, Howitt (innovation-led growth) |

## 6. Books
- **Booker 2024:** Samantha Harvey (UK) – *Orbital*. **Booker 2025:** David Szalay – *Flesh*.
- **International Booker 2025:** **Banu Mushtaq – *Heart Lamp*** (Kannada short stories, tr. Deepa Bhasthi) – first Kannada winner. (2022: Geetanjali Shree – *Tomb of Sand*.)

## 7. Sports
- **Paris 2024 Olympics:** India 6 medals (1 silver – Neeraj Chopra; 5 bronze incl. **Manu Bhaker ×2**). Closing-ceremony flag-bearers: **Manu Bhaker & P. R. Sreejesh**. Next: LA 2028, Brisbane 2032.
- **Paris 2024 Paralympics:** India's best ever – **29 medals (7 gold)**; top three: China, Great Britain, USA. Paralympics are every **4** years.
- **Cricket:** India won the **Champions Trophy (Mar 2025, Dubai)**, **Asia Cup (28 Sept 2025, Dubai)** and the **Women's ODI World Cup (Nov 2025, beat South Africa, Navi Mumbai)**. **WTC final 2025** – South Africa beat Australia (Lord's).
- **Chess:** D. Gukesh – youngest undisputed world champion (Dec 2024, beat Ding Liren). **Divya Deshmukh** – FIDE Women's World Cup 2025.
- **Tennis:** Wimbledon 2024 – Alcaraz (Spain) beat Djokovic; Wimbledon 2025 – Jannik Sinner & Iga Świątek.

## 8. Places in the news
Kursk – Russia · Tigray – Ethiopia · St Martin's Island – Bangladesh · Kachin – Myanmar · Nagorno-Karabakh – Azerbaijan · **Göbekli Tepe – Neolithic site, Türkiye** · **Tuvalu – Falepili Union treaty with Australia (2023), first planned relocation of a whole nation due to sea-level rise**.
"""}],
    "Current National Affairs": [{"title": "National affairs 2024–26 – revision notes", "md": """# Current national affairs (2024 – mid-2026)

## 1. Constitutional and key posts (as of early 2026)
| Post | Holder |
|---|---|
| President | Droupadi Murmu (15th, July 2022) |
| Vice-President | **C. P. Radhakrishnan** (15th, Sept 2025 – after Jagdeep Dhankhar resigned in July 2025) |
| Prime Minister | Narendra Modi (third term, June 2024) |
| Chief Justice of India | **Surya Kant** (53rd, 24 Nov 2025); before him B. R. Gavai (52nd) |
| Chief Election Commissioner | Gyanesh Kumar (Feb 2025) |
| RBI Governor | Sanjay Malhotra (Dec 2024) |
| Union Minister of Cooperation | **Amit Shah** (also Home) – ministry created 2021 |
| Karnataka CM | Siddaramaiah – equalled **D. Devaraj Urs's record of 2,792 days** on 6 Jan 2026 |

## 2. Republic Day chief guests
2024 – Emmanuel Macron (France) · 2025 – Prabowo Subianto (Indonesia) · **2026 (77th) – António Costa & Ursula von der Leyen (EU)**.

## 3. Defence and security
- **Operation Sindoor** (7 May 2025): strikes on terror camps in Pakistan & PoK after the **Pahalgam attack** (22 Apr 2025).
- Evacuation operations: Ganga (Ukraine 2022), Kaveri (Sudan 2023), Ajay (Israel 2023), Indravati (Haiti 2024).
- INS Vikrant – first indigenous aircraft carrier (2022).

## 4. Space
| Mission | Fact |
|---|---|
| Chandrayaan-3 | Landed near lunar south pole **23 Aug 2023** → **National Space Day (first observed 23 Aug 2024)** |
| Aditya-L1 | Solar observatory at L1 (launched Sept 2023) |
| **Axiom-4** | **Shubhanshu Shukla** – first Indian on the ISS (June 2025) |
| **NISAR** | NASA–ISRO radar satellite, GSLV-F16, **30 July 2025** |
| **CMS-03** | **Communication** satellite (~4,400 kg) by **LVM3-M5, 2 Nov 2025** – heaviest launched from India |

## 5. Economy, laws and schemes
- **GST 2.0** (22 Sept 2025): two main slabs **5% and 18%** (+40% on luxury / sin goods).
- **Four Labour Codes** in force from **21 Nov 2025**.
- **Waqf (Amendment) Act, 2025**. Next **Census with caste enumeration** (reference date 1 March 2027).
- **Kerala** – first state declared **free of extreme poverty** (1 Nov 2025).
- **PMSBY** – accident insurance (₹2 lakh) · **PMJJBY** – life insurance · **MUDRA** – Shishu / Kishor / Tarun (+ Tarun Plus up to ₹20 lakh) · **AMRUT** – Atal Mission for **Rejuvenation** and Urban **Transformation** (2015) · **PM-JANMAN** (2023) – PVTGs.
- **Maha Kumbh 2025** – Prayagraj, 13 Jan – 26 Feb 2025.
- Karnataka's **five guarantees** (2023): Gruha Jyothi (free power up to 200 units), Gruha Lakshmi (₹2,000/month to women heads), Anna Bhagya (rice), **Shakti (free bus travel for women)**, Yuva Nidhi (unemployment allowance).

## 6. Awards and people
- **Bharat Ratna 2024:** Karpoori Thakur, L. K. Advani, P. V. Narasimha Rao, Charan Singh, **M. S. Swaminathan** (also Padma Shri 1967, Magsaysay 1971, Albert Einstein World Science Award 1986).
- **Kendra Sahitya Akademi 2024 (Kannada):** **K. V. Narayana – *Nudigala Alivu***.
- **Surekha Yadav** – Asia's first woman loco pilot, retired Sept 2025.
- **Aditi Swami & Ojas Deotale** – India's first individual world titles in compound **archery** (2023).

## 7. Sports (national angle)
Paris 2024: 6 medals · Asia Cup 2025 – India beat Pakistan in Dubai (28 Sept 2025) · Women's ODI World Cup 2025 – India champions · Divya Deshmukh – FIDE Women's World Cup 2025.
"""}],
    "Movies": [{"title": "Movies and film awards – revision notes", "md": """# Movies and film awards

## 1. National Film Awards (by the Ministry of I&B / NFDC; presented by the President)
| | **70th** (for 2022 films, announced Aug 2024) | **71st** (for 2023 films, announced 1 Aug 2025) |
|---|---|---|
| Best Feature Film | *Aattam* (Malayalam) | ***12th Fail*** |
| Best Actor | **Rishab Shetty – *Kantara*** | **Shah Rukh Khan – *Jawan*** & **Vikrant Massey – *12th Fail*** |
| Best Actress | Nithya Menen & Manasi Parekh | **Rani Mukerji – *Mrs Chatterjee vs Norway*** |
| Best Director | Sooraj Barjatya | **Sudipto Sen – *The Kerala Story*** |
| Best Popular Film | *Kantara* | *Rocky Aur Rani Kii Prem Kahaani* |
| **Best Kannada Film** | ***KGF Chapter 2*** | ***Kandeelu – The Ray of Hope*** (dir. **Yashoda Prakash**) |

## 2. Dadasaheb Phalke Award (highest Indian film honour, instituted **1969**; first: **Devika Rani**)
| Award year | Recipient |
|---|---|
| 1995 | **Dr Rajkumar** – first and only Kannada artist so far |
| 2020 | Asha Parekh |
| 2021 | Waheeda Rehman |
| 2022 | Mithun Chakraborty (given Oct 2024) |
| **2023** | **Mohanlal** (announced Sept 2025) |

## 3. Firsts in Indian and Kannada cinema
- *Raja Harishchandra* (1913, Dadasaheb Phalke) – first full-length Indian feature.
- *Alam Ara* (1931, Ardeshir Irani) – first Indian talkie. *Kisan Kanya* (1937) – first colour film.
- ***Sati Sulochana* (1934)** – first Kannada talkie. *Bedara Kannappa* (1954) – Dr Rajkumar's debut as hero.
- *Samskara* (1970, from **U. R. Ananthamurthy**'s novel) – Kannada new wave; *Ghatashraddha* (Girish Kasaravalli); *Nagarahavu* (Puttanna Kanagal, launched Vishnuvardhan); *Ondanondu Kaladalli* (Shankar Nag); *Pushpaka Vimana* (1987, silent film with Kamal Haasan); *Kantara* (2022) & *Kantara: Chapter 1* (2025) – Rishab Shetty.
- Puneeth Rajkumar – "Power Star", posthumous **Karnataka Ratna** (2021).

## 4. Oscars and world festivals
- **Oscars** (Academy of Motion Picture Arts & Sciences, USA; first 1929). Bhanu Athaiya – first Indian winner (costume, *Gandhi*, 1983); Satyajit Ray – honorary (1992); A. R. Rahman – 2 (2009).
- **2023:** ***Naatu Naatu*** (*RRR*, M. M. Keeravani & Chandrabose) – Best Original Song; ***The Elephant Whisperers*** (Kartiki Gonsalves) – Documentary Short.
- **2025 (97th):** *Anora* – Best Picture; Sean Baker – Director; Adrien Brody & Mikey Madison – acting.
- **Cannes (France) – Palme d'Or:** 2024 *Anora*; 2025 *It Was Just an Accident* (Jafar Panahi). **2024 Grand Prix:** Payal Kapadia – *All We Imagine as Light*. Anasuya Sengupta – Best Actress, Un Certain Regard (*The Shameless*).
- Berlin – **Golden Bear**; Venice – **Golden Lion**; UK – **BAFTA**.
- **IFFI** – Goa (permanent venue since 2004), began 1952. **BIFFes** – Bengaluru (Karnataka Chalanachitra Academy).
- India's Oscar entry is chosen by the **Film Federation of India**. Films are certified by the **CBFC** under the **Cinematograph Act, 1952**.
"""}],
}
