"""Paper 1 · General Knowledge · P1-GK-11 Geography – Festivals, Population and Literacy and P1-GK-12 Geography – Natural Regions,
Natural Resources, Food Crops (2 topics × 2 sets × 20), with detailed revision NOTES. Shared by GPSTR and KRIES (Paper 1 item C),
so English like the other GK topics. References: Census of India 2011, NCERT Geography (classes 9–12: Contemporary India, India –
People and Economy), KTBS Social Science, Karnataka Census 2011 tables. REAL previous-year questions come from the KEA 2025–26 GK
papers, Legislative Council 2024 Data Entry Paper-1, GTTC 2024 GK (Q79 lies beyond the parsed key) and VAO 2024; answers worked out
by ExamSim (the parsed Data Entry key disagrees with the paper on Q66, so it is not used). Skipped as unclear: KEA 2026 GK-2 (NHK) Q76,
Q80; GK-3 (NHK) Q33, Q86; Legislative Council Asst P1 Q9, Q93; Data Entry P1 Q61."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

POPULATION = [
    ("Consider the following statements with respect to Census of India, 2027.\nStatement I: Houselisting and housing census will be conducted between April to September, 2026.\n"
     "Statement II: It will be the second census by digital means in the country.",
     ["Statement I is correct but, Statement II is incorrect", "Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect",
      "Statement I is incorrect but, Statement II is correct"], 0,
     "Census 2027 is India's FIRST digital census (mobile apps) and also enumerates caste; the population count's reference date is 1 March 2027." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q92"),
    ("Assertion (A): Zero Population Growth (ZPG) is a demographic balance when the number of people in population does not increase or decrease.\n"
     "Reason (R): A country is said to attain ZPG when the total number of births and the number of immigrants into a country is equal to the total number of deaths plus the number of people who emigrate out of the country.",
     ["Both (A) and (R) are correct and (R) is the correct explanation for (A)", "Both (A) and (R) are correct but (R) is not the correct explanation for (A)",
      "(A) is correct but (R) is incorrect", "(A) is incorrect but (R) is correct"], 0,
     "Births + immigrants = deaths + emigrants means the population neither grows nor shrinks." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q78"),
    ("According to the Census Commission of India (2011), Class-I city means",
     ["The city with population of 10000 to 19999", "The city with population of 20000 to 49999", "The city with population of 50000 to 99999",
      "The city with population of more than 1 Lakh (100000)"], 3,
     "Class I – 1 lakh and above; a million-plus city has 10 lakh or more; megacity – over 1 crore (10 million)." + NOTE, "Legislative Council 2024 Data Entry P1 · Q18"),
    ("Match the following on the basis of population census of 2011.\nList-I: a. Kerala  b. Arunachal Pradesh  c. Uttar Pradesh  d. Bihar\n"
     "List-II: i) Highest population  ii) Highest population density  iii) Highest literacy  iv) Lowest population density",
     ["a – iii, b – iv, c – i, d – ii", "a – ii, b – iii, c – iv, d – i", "a – iv, b – iii, c – ii, d – i", "a – i, b – ii, c – iv, d – iii"], 0,
     "Kerala literacy ≈ 94%; Arunachal 17 per sq km; UP ≈ 20 crore; Bihar 1,106 per sq km." + NOTE, "Legislative Council 2024 Data Entry P1 · Q64"),
    ("According to Census 2011, India's population was about:",
     ["121 crore", "102 crore", "135 crore", "110 crore"], 0, PYQ + "1,210.9 million (17.7% of the world); decadal growth 2001–11: 17.7%."),
    ("Census 2011 sex ratio of India (females per 1,000 males) was:",
     ["943", "933", "914", "1,020"], 0, "Kerala had the highest (1,084) and Haryana the lowest (879); the child sex ratio (0–6 years) was 919."),
    ("India's literacy rate in Census 2011 was:",
     ["74.04%", "64.8%", "82.1%", "69.3%"], 0, PYQ + "Male 82.1%, female 65.5%; highest Kerala (94%), lowest Bihar (61.8%)."),
    ("India's population density in 2011 was:",
     ["382 persons per sq km", "325 persons per sq km", "455 persons per sq km", "1,106 persons per sq km"], 0, "1,106 was Bihar's density, the highest among states."),
    ("Karnataka's population, sex ratio and literacy as per Census 2011 were about:",
     ["6.11 crore, 973, 75.4%", "5.28 crore, 965, 66.6%", "7.20 crore, 996, 82.3%", "6.11 crore, 943, 74.0%"], 0,
     PYQ + "Karnataka's density is 319 per sq km; urban share 38.7%."),
    ("In Karnataka (Census 2011), the district with the highest literacy rate and the one with the lowest are:",
     ["Dakshina Kannada and Yadgir", "Bengaluru Urban and Raichur", "Udupi and Kalaburagi", "Kodagu and Chamarajanagar"], 0,
     "Dakshina Kannada ≈ 88.6%, Yadgir ≈ 51.8%. Bengaluru Urban is the most populous district and Kodagu the least."),
    ("Which census year is called the 'Year of the Great Divide' in India's demographic history?",
     ["1921", "1951", "1911", "1961"], 0, PYQ + "After 1921 India's population grew every decade; 1961–81 was the phase of population explosion."),
    ("The first synchronous (complete) census of India was held in 1881 under:",
     ["Lord Ripon", "Lord Mayo", "Lord Curzon", "Lord Dalhousie"], 0, "The first (non-synchronous) census was in 1872 under Lord Mayo."),
    ("Census 2027 will also count castes. When was caste last enumerated fully in a census of India?",
     ["1931", "1951", "1901", "2011"], 0, PYQ + "The 2011 Socio-Economic and Caste Census (SECC) was a separate exercise."),
    ("The Census in India is conducted under the Census Act, 1948 by the:",
     ["Registrar General and Census Commissioner (Ministry of Home Affairs)", "Election Commission", "NITI Aayog", "National Statistical Office"], 0,
     "Census is in the Union List (entry 69)."),
    ("According to UN estimates, India became the world's most populous country in:",
     ["2023", "2011", "2019", "2027"], 0, PYQ + "UN World Population Prospects; World Population Day is 11 July."),
    ("In the census, a person is counted as 'literate' if he or she is:",
     ["Aged 7 or above and can read and write with understanding in any language", "Aged 6 or above and has passed class 1",
      "Aged 10 or above and can sign their name", "Any person who has attended school"], 0, "Children of 0–6 years are treated as non-literate by definition."),
    ("Consider the statements:\nI. Sex ratio in India is measured as the number of females per 1,000 males.\nII. The child sex ratio refers to the 0–6 years age group.",
     I_II, 2, "Both are correct. Karnataka's sex ratio (2011) was 973; child sex ratio 948."),
    ("Assertion (A): Kerala has the highest literacy among Indian states.\nReason (R): Kerala has the lowest population density in India.",
     AR, 2, "R is false: Kerala is densely populated (859 per sq km); Arunachal Pradesh has the lowest density."),
    ("The urban share of Karnataka's population in 2011 was about:",
     ["38.7%", "21.4%", "52.3%", "31.2%"], 0, "India's urbanisation in 2011 was 31.2%; the 74th Amendment (1992) gave urban local bodies constitutional status."),
    ("The demographic stage in which both birth and death rates are low and population growth is slow is the:",
     ["Fourth (late) stage of demographic transition", "First stage", "Second stage (population explosion)", "Stage of high fluctuation"], 0,
     PYQ + "Stage 1: high birth and death rates; stage 2: death rate falls fast; stage 3: birth rate falls; stage 4: both low."),
]

PEOPLE = [
    ("Which one of the Tribes is NOT settled in Nilgiris of Tamil Nadu?",
     ["Badagas", "Kotas", "Kurumbas", "Lambadas"], 3,
     "Todas, Kotas, Badagas, Kurumbas and Irulas live in the Nilgiris; Lambanis (Banjaras) are spread over the Deccan." + NOTE, "GTTC 2024 Asst Gr-II GK · Q79"),
    ("Which of the following regions is the original habitat of the 'Toda Tribe'?",
     ["Kumaon Hills", "Nilgiri Hills", "Khasi Hills", "Garhwal Hills"], 1,
     "Todas are pastoral buffalo-herders living in barrel-vaulted huts called 'munds'." + NOTE, "VAO 2024 Paper-1 · Q47"),
    ("Match the festivals with their states:\na. Onam  b. Bihu  c. Pongal  d. Hornbill festival\n1. Kerala  2. Assam  3. Tamil Nadu  4. Nagaland",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4"], 0,
     PYQ + "Hornbill festival (1–10 December, Kisama) – 'festival of festivals'; Assam has three Bihus (Bohag, Kati, Magh)."),
    ("The Kumbh Mela rotates among four places. Which of these is NOT one of them?",
     ["Varanasi", "Prayagraj", "Haridwar", "Nashik"], 0, "The fourth is Ujjain; the Maha Kumbh at Prayagraj was held in January–February 2025. UNESCO intangible heritage (2017)."),
    ("Chhath Puja, dedicated to the Sun God, is mainly celebrated in:",
     ["Bihar", "Gujarat", "Punjab", "Kerala"], 0, PYQ + "Also in eastern Uttar Pradesh and Jharkhand."),
    ("Match the Karnataka festivals with their regions:\na. Karaga  b. Kambala  c. Huttari (Puttari)  d. Hampi Utsav\n"
     "1. Bengaluru (Dharmaraya temple)  2. Dakshina Kannada and Udupi (buffalo race)  3. Kodagu (harvest)  4. Vijayanagara district",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0,
     "Karaga is performed by the Thigala community; Kambala is held in slush tracks of paddy fields."),
    ("Ugadi, the New Year festival of Karnataka, falls in the month of:",
     ["Chaitra (March–April)", "Kartika", "Shravana", "Magha"], 0, PYQ + "Bevu-bella (neem and jaggery) symbolises life's mix of joy and sorrow."),
    ("The Pushkar fair, famous for its camel trade, is held in:",
     ["Rajasthan", "Gujarat", "Madhya Pradesh", "Haryana"], 0, "It is held in the month of Kartika near Ajmer."),
    ("'Hemis festival' is celebrated in:",
     ["Ladakh", "Sikkim", "Arunachal Pradesh", "Himachal Pradesh"], 0, PYQ + "It honours Guru Padmasambhava with masked Cham dances at Hemis monastery."),
    ("'Losar' is the New Year festival of:",
     ["Tibetan Buddhist communities (Ladakh, Sikkim, Arunachal)", "Parsis", "Sikhs of Punjab", "Tribes of Jharkhand"], 0, "The Parsi New Year is Navroz."),
    ("'Nuakhai', a festival of eating the new rice crop, is celebrated in:",
     ["Odisha", "Kerala", "Goa", "Uttarakhand"], 0, PYQ + "Mainly western Odisha (Sambalpur region)."),
    ("Makara Sankranti is marked in Karnataka by exchanging:",
     ["Ellu-bella (sesame, jaggery and coconut)", "Bevu-bella", "Kadubu", "Holige only"], 0, "It marks the Sun's entry into Capricorn (around 14 January)."),
    ("Which festival is associated with Mysuru and has the Jamboo Savari procession?",
     ["Dasara (Nadahabba)", "Deepavali", "Ganesha Chaturthi", "Karaga"], 0, PYQ + "Started at Srirangapatna in 1610 by Raja Wodeyar; Karnataka's state festival."),
    ("'Bathukamma', a floral festival celebrated by women, belongs to:",
     ["Telangana", "Goa", "Punjab", "Manipur"], 0, "Bonalu is another Telangana festival; Gangaur is celebrated in Rajasthan."),
    ("Gangaur, a festival in honour of Goddess Gauri (Parvati), is mainly celebrated in:",
     ["Rajasthan", "Kerala", "Assam", "Tamil Nadu"], 0, PYQ + "Teej is another Rajasthani festival of married women."),
    ("According to Census 2011, the most populous Scheduled Tribe in India is the:",
     ["Bhil", "Gond", "Santhal", "Oraon"], 0, "Gonds are the second largest; Santhals are known for the 1855 Hul rebellion."),
    ("The Soliga tribe, the first tribal community to win forest rights inside a tiger reserve, lives mainly in:",
     ["Biligirirangana (BR) Hills, Chamarajanagar", "Nagarahole, Kodagu", "Dandeli, Uttara Kannada", "Kudremukh, Chikkamagaluru"], 0,
     PYQ + "BRT Tiger Reserve lies where the Western and Eastern Ghats meet."),
    ("The Siddis of Karnataka, who live mainly in Uttara Kannada, are of:",
     ["African origin", "Central Asian origin", "Tibetan origin", "Arab origin"], 0, "They were brought by Portuguese and Arab traders; Siddis are also found in Gujarat and Hyderabad."),
    ("Consider the statements about tribes of Karnataka:\nI. The Jenu Kurubas are traditionally honey-gatherers of the Nagarahole–H.D. Kote forests.\n"
     "II. The Hakki Pikkis are traditionally bird-catchers.", I_II, 2, PYQ + "Both are correct; other Karnataka tribes include the Kadu Kuruba, Koraga, Gowdalu and Yerava."),
    ("Assertion (A): Kambala is a traditional buffalo race of coastal Karnataka.\nReason (R): Kambala is run on dry, rocky ground after the harvest.",
     AR, 2, "R is false: Kambala tracks are slushy paddy fields; it is held from November to March."),
]

LAND_RESOURCES = [
    ("Which of the following statements about Bhangar soil is incorrect?",
     ["Bhangar is an older alluvial soil.", "It is found in higher areas away from river beds", "It has a fine texture with high moisture retention",
      "Bhangar often contains Kankar (lime nodules)"], 2,
     "Fine texture and fertility describe Khadar, the new alluvium renewed by floods every year." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q77"),
    ("Match the following:\nList – I (Coal mining centre): (a) Raniganj (b) Jariya (c) Tattapani (d) Talcher\nList – II (State): (i) Odisha (ii) West Bengal (iii) Jharkhand (iv) Chattisgarh",
     ["a – iii, b – ii, c – i, d – iv", "a – ii, b – i, c – iii, d – iv", "a – ii, b – iii, c – i, d – iv", "a – ii, b – iii, c – iv, d – i"], 3,
     "Raniganj – West Bengal; Jharia – Jharkhand (largest coking coal field); Tattapani – Chhattisgarh; Talcher – Odisha." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q84"),
    ("Match List I with List II and choose the answer from the codes given below:\nList I: a. Sundargarh  b. Neyveli  c. Balaghat  d. Chand Mari\nList II: i. Copper  ii. Manganese  iii. Iron ore  iv. Lignite",
     ["a-iii, b-iv, c-ii, d-i", "a-ii, b-iv, c-i, d-iii", "a-iv, b-iii, c-ii, d-i", "a-iii, b-ii, c-iv, d-i"], 0,
     "Sundargarh (Odisha) – iron ore; Neyveli (Tamil Nadu) – lignite; Balaghat (MP) – manganese; Chandmari (Rajasthan, Khetri belt) – copper." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q74"),
    ("Choose the correct sequence of the given rivers in length.",
     ["Nile - Amazon - Mississippi Missouri - Yangtze Kiang", "Nile - Amazon - Yangtze Kiang - Mississippi Missouri",
      "Nile - Yangtze Kiang - Amazon - Mississippi Missouri", "Nile - Mississippi Missouri - Amazon - Yangtze Kiang"], 1,
     "Nile ≈ 6,650 km, Amazon ≈ 6,400 km, Yangtze ≈ 6,300 km, Mississippi–Missouri ≈ 6,275 km." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q72"),
    ("As per the criteria of rivers joining their main rivers, which of the following is correct?",
     ["Jhelum - Chenab - Sutlej - Indus", "Jhelum - Sutlej - Chenab - Indus", "Chenab - Jhelum - Sutlej - Indus", "Chenab - Sutlej - Jhelum - Indus"], 0,
     "The Jhelum joins the Chenab, the Chenab (with the Ravi) joins the Sutlej (with the Beas) as the Panjnad, which joins the Indus at Mithankot." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q52"),
    ("In India, which type of soils are more found in Western Ghats and North-Eastern States?",
     ["Alluvial soils", "Red soils", "Laterite soils", "Black soils"], 2,
     "Laterite forms by leaching under heavy rain and high temperature; good for cashew, tea, coffee and rubber." + NOTE, "Legislative Council 2024 Data Entry P1 · Q65"),
    ("India's major physiographic divisions are:",
     ["Himalayas, Northern Plains, Peninsular Plateau, Indian Desert, Coastal Plains and Islands", "Himalayas, Deccan and Islands only",
      "Northern Plains and Southern Plateau only", "Western Ghats, Eastern Ghats and Thar only"], 0, PYQ + "The Peninsular Plateau is the oldest landmass, part of Gondwana."),
    ("Black soil (regur), ideal for cotton, is formed from:",
     ["Weathering of Deccan trap (basalt) lava rocks", "River deposits", "Leaching under heavy rainfall", "Wind-blown sand"], 0,
     "It retains moisture and develops deep cracks in summer ('self-ploughing'); found in north Karnataka, Maharashtra and Gujarat."),
    ("Red soil gets its colour from the presence of:",
     ["Iron oxide", "Humus", "Calcium carbonate", "Aluminium"], 0, PYQ + "It looks yellow when hydrated; it covers much of south Karnataka and Tamil Nadu."),
    ("The Sandur region of Karnataka (Ballari) is known for deposits of:",
     ["Iron ore and manganese", "Coal and lignite", "Bauxite and mica", "Petroleum"], 0,
     "Kudremukh's magnetite mines closed in 2006; Odisha is India's largest producer of iron ore."),
    ("India's largest producer of bauxite, the ore of aluminium, is:",
     ["Odisha", "Karnataka", "Gujarat", "Kerala"], 0, PYQ + "Panchpatmali (Koraput) hosts NALCO's mine."),
    ("Mumbai High, India's largest oil field, is:",
     ["An offshore field in the Arabian Sea", "In the Brahmaputra valley", "In the Gulf of Mannar", "In the Thar desert"], 0,
     "Digboi (Assam) is the oldest oil field; Barmer (Rajasthan) is a major onshore field."),
    ("Tropical evergreen forests in India are found where annual rainfall exceeds:",
     ["200 cm (Western Ghats, North-East, Andamans)", "50 cm", "100 cm only in the Deccan", "25 cm"], 0,
     PYQ + "Tropical deciduous (monsoon) forests – 70 to 200 cm; thorn forests – below 70 cm."),
    ("The world's largest mangrove forest, home to the Royal Bengal tiger, is the:",
     ["Sundarbans", "Bhitarkanika", "Pichavaram", "Coringa"], 0, "Named after the Sundari tree; shared by India and Bangladesh."),
    ("The wettest place in India (highest average annual rainfall) is:",
     ["Mawsynram, Meghalaya", "Agumbe, Karnataka", "Cherrapunji, Assam", "Mahabaleshwar, Maharashtra"], 0,
     PYQ + "Agumbe is called the 'Cherrapunji of the South'; Cherrapunji (Sohra) is also in Meghalaya."),
    ("The highest peak in South India and the highest peak in Karnataka are respectively:",
     ["Anamudi and Mullayanagiri", "Doddabetta and Kudremukh", "Mullayanagiri and Anamudi", "Anamudi and Kodachadri"], 0,
     "Anamudi (2,695 m, Kerala); Mullayanagiri (1,925 m, Chikkamagaluru)."),
    ("Consider the statements:\nI. India's oldest landmass is the Peninsular Plateau.\nII. The Himalayas are fold mountains formed by the collision of the Indian and Eurasian plates.",
     I_II, 2, PYQ + "Both are correct; the Himalayas are young fold mountains."),
    ("Assertion (A): The western slopes of the Western Ghats receive very heavy rainfall during the south-west monsoon.\n"
     "Reason (R): The Ghats force moisture-laden winds to rise and cool, causing orographic rainfall.",
     AR, 0, "The eastern side lies in the rain-shadow – which is why north Karnataka's plateau is dry."),
    ("Which of these is NOT a separate biosphere reserve of India?",
     ["Bandipur", "Nilgiri", "Sundarbans", "Gulf of Mannar"], 0,
     "Bandipur is part of the Nilgiri Biosphere Reserve (India's first, 1986), not a separate reserve."),
    ("Which mineral is mined at Hutti (Raichur) and Kolar in Karnataka's history?",
     ["Gold", "Copper", "Coal", "Uranium"], 0, PYQ + "Karnataka produces most of India's primary gold (Hutti Gold Mines)."),
]

CROPS = [
    ("TKM(R)12, MTU 1001, Poosa RH10, AGRO 6201, these are the varieties of",
     ["Commonly used varieties of wheat in India", "Commonly used varieties of paddy in India", "Commonly used varieties of cotton in India",
      "Commonly used varieties of sugarcane in India"], 1, "MTU 1001 (Maruteru) and Pusa RH-10 (a basmati hybrid) are rice varieties." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q85"),
    ("Choose the correctly matched option:",
     ["Kharif-Paddy, Rabi-Wheat, Zaid-Vegetable", "Kharif-Barli, Rabi-Maize, Zaid-Vegetable", "Kharif-Paddy, Rabi-Vegetable, Zaid-Groundnut",
      "Kharif-Groundnut, Rabi-Barli, Zaid-Vegetable"], 0,
     "Kharif – sown with the monsoon (June–July); Rabi – winter (October–November); Zaid – short summer season (watermelon, cucumber, vegetables)." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q72"),
    ("Which of the following is called as 'white gold'?",
     ["Diamond", "Cotton", "Sugar", "Lithium"], 1,
     "Cotton is traditionally called 'white gold' (lithium is sometimes nicknamed so today, but the standard GK answer is cotton)." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q33"),
    ("Red rot of sugarcane is caused by",
     ["Bacteria", "Virus", "Algae", "Fungi"], 3, "Red rot is a fungal disease (Colletotrichum falcatum)." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q15"),
    ("India's largest rice-producing state is:",
     ["West Bengal", "Punjab", "Karnataka", "Tamil Nadu"], 0, PYQ + "Rice needs over 100 cm of rain, high temperature (above 25 °C) and clayey soil."),
    ("India's largest producer of wheat and of sugarcane is:",
     ["Uttar Pradesh", "Maharashtra", "Bihar", "Gujarat"], 0, "Wheat needs a cool growing season and 50–75 cm of rain."),
    ("India's largest tea-producing state is:",
     ["Assam", "Kerala", "West Bengal", "Karnataka"], 0, PYQ + "Darjeeling tea (West Bengal) was India's first GI product (2004)."),
    ("Which state is India's largest producer of coffee?",
     ["Karnataka", "Kerala", "Tamil Nadu", "Andhra Pradesh"], 0, "Karnataka grows about 70%; coffee was first planted at Baba Budangiri, Chikkamagaluru."),
    ("Raw jute production in India is concentrated in:",
     ["West Bengal", "Punjab", "Rajasthan", "Karnataka"], 0, PYQ + "Jute needs high temperature, heavy rain and the fertile delta soil of the Ganga–Brahmaputra."),
    ("Match the revolutions with their sectors:\na. Yellow revolution  b. Blue revolution  c. White revolution  d. Silver revolution\n1. Oilseeds  2. Fisheries  3. Milk  4. Eggs (poultry)",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0,
     "Green revolution – food grains (wheat, rice); Golden – horticulture and honey."),
    ("The Green Revolution in India in the 1960s is associated with:",
     ["High-yielding wheat varieties, M.S. Swaminathan and Norman Borlaug", "Operation Flood and Verghese Kurien", "The Bhoodan movement", "Organic farming"], 0,
     PYQ + "It mainly helped Punjab, Haryana and western UP; Operation Flood is the White Revolution."),
    ("The minimum support price (MSP) for crops is announced by the central government on the recommendation of the:",
     ["Commission for Agricultural Costs and Prices (CACP)", "NABARD", "Food Corporation of India", "NITI Aayog"], 0,
     "FCI procures, stores and distributes grain; NABARD finances rural credit."),
    ("Which of these is a Zaid crop?",
     ["Watermelon", "Wheat", "Paddy (kharif)", "Mustard"], 0, PYQ + "Mustard and wheat are rabi; paddy is mainly kharif."),
    ("The UN declared 2023 the International Year of Millets on India's proposal. Millets in India are also called:",
     ["Shree Anna", "Anna Bhagya", "Krishi Ratna", "Bhoochetana"], 0, "Ragi, jowar, bajra and the small millets; Karnataka leads in ragi."),
    ("India is the world's largest producer of:",
     ["Milk", "Wheat", "Coffee", "Rubber"], 0, PYQ + "India is also the largest producer of pulses and second in rice and wheat."),
    ("The state that leads India in cotton production in recent years is:",
     ["Gujarat", "Punjab", "Kerala", "West Bengal"], 0, "Cotton grows in black soil with 50–100 cm rain and 210 frost-free days."),
    ("Consider the statements about Karnataka agriculture:\nI. Kalaburagi district is known as the 'tur (red gram) bowl' of Karnataka.\nII. Coffee is mainly grown in the plains of north Karnataka.",
     I_II, 0, "Only I: coffee grows on the hill slopes of Kodagu, Chikkamagaluru and Hassan."),
    ("Ragi in Karnataka is mainly grown in the:",
     ["Kharif season, under rainfed conditions in the southern districts", "Rabi season in the coastal belt", "Zaid season in the Malnad", "Winter under irrigation only"], 0,
     PYQ + "Tumakuru, Hassan, Mandya and Ramanagara are leading ragi districts."),
    ("Which of the following crops is a plantation crop grown on hill slopes?",
     ["Tea", "Wheat", "Gram", "Bajra"], 0, "Tea, coffee, rubber and cardamom are plantation crops; Karnataka's cardamom hills are in Kodagu and Hassan."),
    ("Assertion (A): Rice is the main crop of the coastal plains of Karnataka.\nReason (R): The coast receives very little rainfall.",
     AR, 2, "R is false: the coast gets over 300 cm of rain, which is why rice dominates there."),
]

TOPICS = {
    "Geography – Festivals, Population and Literacy": [
        ("1 · Population, Census and Literacy", POPULATION),
        ("2 · Festivals, Fairs and Tribes", PEOPLE),
    ],
    "Geography – Natural Regions, Natural Resources, Food Crops": [
        ("1 · Natural Regions, Soils and Mineral Resources", LAND_RESOURCES),
        ("2 · Agriculture and Food Crops", CROPS),
    ],
}

NOTES = {
    "Geography – Festivals, Population and Literacy": [
        {"title": "Population, census, festivals and tribes – revision notes", "md": """## 1. Census facts (2011)
| Indicator | India | Karnataka |
|---|---|---|
| Population | 121.09 crore | 6.11 crore |
| Density | 382 / sq km | 319 |
| Sex ratio | 943 | 973 |
| Child sex ratio (0–6) | 919 | 948 |
| Literacy | 74.04% | 75.36% |
| Urban share | 31.2% | 38.7% |
- Highest: population UP; density Bihar (1,106); literacy Kerala (94%); sex ratio Kerala (1,084)
- Lowest: density Arunachal (17); literacy Bihar (61.8%); sex ratio Haryana (879)
- Karnataka districts: literacy highest Dakshina Kannada, lowest Yadgir; most populous Bengaluru Urban; least Kodagu
- Least density in Karnataka: Kodagu, Uttara Kannada

## 2. Census history
| Year | Fact |
|---|---|
| 1872 | first census (Lord Mayo) |
| 1881 | first synchronous census (Lord Ripon) |
| 1921 | 'Year of the Great Divide' |
| 1931 | last full caste census |
| 1948 | Census Act |
| 2027 | **first digital census**, caste enumerated; houselisting Apr–Sep 2026; reference date 1 Mar 2027 (snow-bound areas 1 Oct 2026) |
- Class I city ≥ 1 lakh; million-plus ≥ 10 lakh; megacity > 1 crore
- Literate = 7+ years, reads and writes with understanding
- Zero population growth: births + immigrants = deaths + emigrants
- India most populous country since 2023; World Population Day 11 July

## 3. Festivals
| Festival | State | Festival | State |
|---|---|---|---|
| Onam | Kerala | Bihu (3) | Assam |
| Pongal | Tamil Nadu | Hornbill (1–10 Dec) | Nagaland |
| Chhath | Bihar | Hemis | Ladakh |
| Losar | Tibetan Buddhists | Nuakhai | Odisha |
| Pushkar fair | Rajasthan | Kumbh | Prayagraj, Haridwar, Ujjain, Nashik |
| Karaga | Bengaluru | Kambala | Dakshina Kannada, Udupi |
| Huttari | Kodagu | Dasara | Mysuru (1610, Raja Wodeyar) |
| Ugadi | Chaitra – bevu-bella | Sankranti | ellu-bella |

## 4. Tribes
- Largest ST: **Bhil**, then Gond; Santhal – Hul 1855
- Nilgiris: Toda, Kota, Badaga, Kurumba, Irula (not Lambani)
- Karnataka: Soliga (BR Hills), Jenu Kuruba (honey), Kadu Kuruba, Hakki Pikki (bird-catchers), Siddi (African origin, Uttara Kannada), Koraga (coast), Lambani

## ⚠ Traps
- Census 2027 is the FIRST digital census
- Kerala: high literacy and HIGH density (lowest density = Arunachal)
- Bandipur and Nagarahole are in the Nilgiri Biosphere Reserve
"""}],
    "Geography – Natural Regions, Natural Resources, Food Crops": [
        {"title": "Natural regions, resources and crops – revision notes", "md": """## 1. Physiography and soils
- Six divisions: Himalayas, Northern Plains, Peninsular Plateau (oldest), Indian Desert, Coastal Plains, Islands
- Highest peaks: Anamudi 2,695 m (South India); Mullayanagiri 1,925 m (Karnataka)
| Soil | Feature | Crops |
|---|---|---|
| Alluvial – **Khadar** (new, fine) / **Bhangar** (old, kankar, higher) | plains | rice, wheat, sugarcane |
| Black (regur) | Deccan trap, self-ploughing | cotton |
| Red | iron oxide | ragi, groundnut |
| Laterite | leaching, heavy rain – Western Ghats, NE | cashew, tea, coffee, rubber |

## 2. Rivers
- Indus system: Jhelum → Chenab → Sutlej (Panjnad) → Indus
- World: Nile > Amazon > Yangtze > Mississippi–Missouri

## 3. Minerals and energy
| Resource | Leading area |
|---|---|
| Coal | Jharia (Jharkhand), Raniganj (WB), Talcher (Odisha), Tattapani (Chhattisgarh) |
| Lignite | Neyveli (TN) |
| Iron ore | Odisha (Sundargarh), Ballari–Sandur, Kudremukh (closed 2006) |
| Manganese | Balaghat (MP), Odisha, Sandur |
| Bauxite | Odisha (Panchpatmali) |
| Copper | Khetri–Chandmari (Rajasthan), Malanjkhand (MP) |
| Gold | Hutti (Karnataka); KGF closed 2001 |
| Oil | Mumbai High (offshore), Digboi (oldest), Barmer |

## 4. Vegetation and climate
- Evergreen > 200 cm; deciduous 70–200 cm; thorn < 70 cm; mangroves – Sundarbans
- Wettest: Mawsynram; Agumbe – 'Cherrapunji of the South'
- Western Ghats: orographic rain on the west, rain-shadow on the east

## 5. Crops
| Crop | Top state |
|---|---|
| Rice | West Bengal |
| Wheat, sugarcane | Uttar Pradesh |
| Cotton | Gujarat |
| Tea | Assam |
| Coffee | Karnataka (~70%) |
| Jute | West Bengal |
| Ragi | Karnataka |
- Kharif – paddy, ragi, cotton, tur; Rabi – wheat, mustard, gram; Zaid – watermelon, vegetables
- Varieties: MTU 1001, Pusa RH-10 = rice; red rot of sugarcane = fungus; cotton = 'white gold'
- Revolutions: Green – grains; White – milk; Yellow – oilseeds; Blue – fish; Silver – eggs; Golden – horticulture/honey
- MSP – CACP; India – largest milk producer; IYM 2023 – 'Shree Anna'

## ⚠ Traps
- Fine texture = Khadar, not Bhangar
- Jharia (coking coal) is in Jharkhand; Raniganj in West Bengal
- Cherrapunji and Mawsynram are both in Meghalaya
"""}],
}
