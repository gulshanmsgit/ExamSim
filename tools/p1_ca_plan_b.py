"""Paper 1 · Current Affairs · planner topics P1-CA-04 Currency and Capitals of Countries, P1-CA-05 Important Days and Slogans and
P1-CA-06 Festivals, Folk Dances, Tribes of the Country (2 sub-topics × 20 each), with detailed notes (NOTES).
Sources: UN observances list, PIB, Ministry of Culture / Sangeet Natak Akademi, UNESCO Intangible Cultural Heritage lists, Census
2011, Karnataka Kannada & Culture department. Real previous-year questions come from GTTC 2024 GK (official KEA key), VAO and PSI
2023–24, KRIES entrance tests and KEA 2025–26 GK papers (answers worked out by ExamSim unless marked official). No real question
on currencies and capitals was found in the downloaded papers, so CA-04 uses "PYQ pattern" questions."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

# ---------------------------------------------------------------- CA-04 Currency and capitals
ASIA = [
    ("The currency of Bhutan is:",
     ["Ngultrum", "Taka", "Kyat", "Rufiyaa"], 0, PYQ + "Taka – Bangladesh; Kyat – Myanmar; Rufiyaa – Maldives."),
    ("The capital of Myanmar is:",
     ["Naypyidaw", "Yangon", "Mandalay", "Bagan"], 0, PYQ + "The capital moved from Yangon (Rangoon) to Naypyidaw in 2005–06."),
    ("The administrative capital of Sri Lanka is ____ while ____ is its commercial capital.",
     ["Sri Jayawardenepura Kotte; Colombo", "Colombo; Kandy", "Jaffna; Colombo", "Kandy; Galle"], 0, PYQ + "The currency is the Sri Lankan rupee."),
    ("Which country uses the 'Rufiyaa' as its currency?",
     ["Maldives", "Mauritius", "Seychelles", "Sri Lanka"], 0, "Its capital is Malé. Mauritius and Seychelles use rupees."),
    ("The currency of Indonesia is the ____ and of Malaysia the ____.",
     ["Rupiah; Ringgit", "Ringgit; Rupiah", "Baht; Dong", "Peso; Riel"], 0, "Indonesia is moving its capital from Jakarta to Nusantara (Borneo)."),
    ("Match the country with its currency:\na. Thailand  b. Vietnam  c. South Korea  d. Japan\n1. Yen  2. Won  3. Dong  4. Baht",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Currency matching is very common."),
    ("The capital of Kazakhstan, which hosted the SCO summit of 2024, is:",
     ["Astana", "Almaty", "Tashkent", "Bishkek"], 0, "Almaty was the capital until 1997; Tashkent – Uzbekistan; Bishkek – Kyrgyzstan."),
    ("The capital and currency of the United Arab Emirates are:",
     ["Abu Dhabi; Dirham", "Dubai; Riyal", "Abu Dhabi; Dinar", "Doha; Dirham"], 0, "Doha is the capital of Qatar (Qatari riyal)."),
    ("Which country's currency, the dinar, is generally the highest-valued currency unit in the world?",
     ["Kuwait", "Bahrain", "Iraq", "Jordan"], 0, PYQ + "Kuwait City is the capital."),
    ("The capital of Australia is:",
     ["Canberra", "Sydney", "Melbourne", "Perth"], 0, PYQ + "Wellington is the capital of New Zealand."),
    ("The currency of China is the:",
     ["Renminbi (Yuan)", "Yen", "Won", "Ringgit"], 0, "Its capital is Beijing."),
    ("Which pair is correctly matched (country – capital)?",
     ["Afghanistan – Kabul", "Pakistan – Karachi", "Turkey – Istanbul", "Vietnam – Ho Chi Minh City"], 0, "Pakistan – Islamabad; Turkey – Ankara; Vietnam – Hanoi."),
    ("The currency of Nepal and its capital are:",
     ["Nepalese rupee; Kathmandu", "Ngultrum; Thimphu", "Taka; Pokhara", "Kyat; Lalitpur"], 0, "Nepal pegs its rupee to the Indian rupee."),
    ("The capital of Iran is ____ and its currency is the ____.",
     ["Tehran; Rial", "Baghdad; Dinar", "Riyadh; Riyal", "Tehran; Dinar"], 0, "Baghdad – Iraq (dinar); Riyadh – Saudi Arabia (riyal)."),
    ("The Philippines uses the ____ as its currency.",
     ["Peso", "Baht", "Ringgit", "Kip"], 0, "Its capital is Manila. Kip – Laos."),
    ("The capital of Mongolia is:",
     ["Ulaanbaatar", "Astana", "Lhasa", "Bishkek"], 0, "Its currency is the tugrik."),
    ("Consider the statements:\nI. The taka is the currency of Bangladesh.\nII. Dhaka is the capital of Bangladesh.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Sri Lanka has two capitals.\nReason (R): Sri Jayawardenepura Kotte is the legislative capital and Colombo the executive and commercial capital.",
     AR, 0, "Parliament sits at Kotte."),
    ("Which of these countries does NOT use a currency called 'rupee'?",
     ["Bhutan", "Nepal", "Pakistan", "Mauritius"], 0, "Bhutan uses the ngultrum (pegged to the Indian rupee)."),
    ("The capital of Cambodia is:",
     ["Phnom Penh", "Vientiane", "Hanoi", "Bangkok"], 0, "Its currency is the riel. Vientiane – Laos."),
]

WORLD = [
    ("The currency of Switzerland is the:",
     ["Swiss franc", "Euro", "Krone", "Pound"], 0, PYQ + "Switzerland is not in the European Union; its capital is Bern."),
    ("Match the country with its currency:\na. Russia  b. Poland  c. Sweden  d. Ukraine\n1. Hryvnia  2. Krona  3. Złoty  4. Ruble",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Kyiv is the capital of Ukraine."),
    ("South Africa has three capitals. Its executive (administrative) capital is:",
     ["Pretoria", "Cape Town", "Bloemfontein", "Johannesburg"], 0, PYQ + "Cape Town is the legislative and Bloemfontein the judicial capital; the currency is the rand."),
    ("The capital of Nigeria is:",
     ["Abuja", "Lagos", "Accra", "Nairobi"], 0, PYQ + "Its currency is the naira. Accra – Ghana; Nairobi – Kenya."),
    ("The currency of Brazil is the ____ and its capital is ____.",
     ["Real; Brasília", "Peso; Rio de Janeiro", "Real; São Paulo", "Sol; Brasília"], 0, "Belém, Brazil hosted COP30 (2025)."),
    ("The capital of Canada is:",
     ["Ottawa", "Toronto", "Montreal", "Vancouver"], 0, PYQ + "The currency is the Canadian dollar."),
    ("The currency of Ethiopia, whose capital Addis Ababa hosts the African Union headquarters, is the:",
     ["Birr", "Shilling", "Cedi", "Naira"], 0, "Cedi – Ghana; shilling – Kenya, Tanzania, Uganda."),
    ("Which of these countries uses the euro?",
     ["Croatia", "Denmark", "Sweden", "Poland"], 0, "Croatia joined the euro area in 2023 and Bulgaria in January 2026; Denmark, Sweden and Poland keep their own currencies."),
    ("The capital of Egypt is ____ and its currency is the ____.",
     ["Cairo; Egyptian pound", "Alexandria; Dinar", "Cairo; Dirham", "Giza; Pound"], 0, "Morocco uses the dirham (capital Rabat)."),
    ("Peru's capital and currency are:",
     ["Lima; Sol", "Quito; Dollar", "Santiago; Peso", "La Paz; Boliviano"], 0, "Quito – Ecuador; Santiago – Chile; La Paz – Bolivia (seat of government)."),
    ("The capital of Venezuela is:",
     ["Caracas", "Bogotá", "Havana", "Lima"], 0, "Its currency is the bolívar. Bogotá – Colombia; Havana – Cuba."),
    ("The Netherlands' constitutional capital is Amsterdam, but its seat of government is:",
     ["The Hague", "Rotterdam", "Brussels", "Utrecht"], 0, "The International Court of Justice is also at The Hague."),
    ("The capital of Tanzania is:",
     ["Dodoma", "Dar es Salaam", "Kampala", "Kigali"], 0, "Dar es Salaam is the largest city. Kampala – Uganda; Kigali – Rwanda."),
    ("Which country's currency is the forint?",
     ["Hungary", "Czech Republic", "Romania", "Austria"], 0, "Budapest is its capital. Czech koruna – Czechia."),
    ("The capital of Argentina is ____ and its currency is the ____.",
     ["Buenos Aires; Peso", "Santiago; Peso", "Montevideo; Real", "Buenos Aires; Real"], 0, "Montevideo – Uruguay."),
    ("Which pair is NOT correctly matched (country – capital)?",
     ["Turkey – Istanbul", "Germany – Berlin", "Norway – Oslo", "Portugal – Lisbon"], 0, "Turkey's capital is Ankara."),
    ("The currency of the United Kingdom is the:",
     ["Pound sterling", "Euro", "Franc", "Krone"], 0, "The UK left the EU in 2020 and never used the euro."),
    ("Cameroon, which hosted the WTO's 14th Ministerial Conference (MC14) in 2026, has its capital at:",
     ["Yaoundé", "Douala", "Abuja", "Dakar"], 0, "Its currency is the Central African CFA franc."),
    ("Consider the statements:\nI. Bolivia has a constitutional capital, Sucre, and a seat of government, La Paz.\nII. The currency of Mexico is the peso.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Countries such as France, Germany and Italy have a common currency.\nReason (R): They are members of the euro area of the European Union.",
     AR, 0, "The euro was introduced in 1999 (notes and coins in 2002)."),
]

# ---------------------------------------------------------------- CA-05 Important days and slogans
DAYS = [
    ("Consider the following statements.\nIndia observed 'Pravasi Bharatiya Divas' on 9th January to mark\n(a) Return of Dr. B.R. Ambedkar from England\n(b) Return of Mahatma Gandhi from South Africa\n(c) Return of Swami Vivekananda from Chicago, USA.\nSelect the correct answer using the codes given below.",
     ["a only", "b only", "a and b", "b and c"], 1,
     "Gandhiji returned to India on 9 January 1915; the day has been observed since 2003." + KEY, "GTTC 2024 Asst Gr-II GK · Q20"),
    ("Which of the following tablets is administered to children and adolescents on National Deworming Day?",
     ["Albendazole tablet", "Paracetamol tablet", "Vitamin-A tablet", "Calcium tablet"], 0,
     "National Deworming Day is held on 10 February (and 10 August); children aged 1–19 get albendazole." + KEY, "GTTC 2024 Asst Gr-II GK · Q30"),
    ("Which day was declared as the \"Day of 8 Billion\" (with respect to population) by the United Nations?",
     ["July 11, 2022", "July 11, 2023", "November 15, 2023", "November 15, 2022"], 3,
     "The UN marked 15 November 2022 as the day world population reached 8 billion; 11 July is World Population Day." + NOTE, "PSI 2023 General Paper · Q87"),
    ("India celebrated its first National Space Day on which day?",
     ["August 22, 2024", "August 23, 2024", "August 25, 2024", "August 27, 2024"], 1,
     "It marks Chandrayaan-3's landing on 23 August 2023." + NOTE, "VAO 2024 Paper-1 · Q29"),
    ("'Vigilance Awareness Week' is observed every year in the month of",
     ["December", "October", "January", "May"], 1,
     "The CVC holds it in the week that includes 31 October, Sardar Patel's birth anniversary." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q2"),
    # --- new questions ---
    ("National Youth Day (12 January) marks the birth anniversary of:",
     ["Swami Vivekananda", "Subhas Chandra Bose", "Bhagat Singh", "Rabindranath Tagore"], 0, PYQ + "Netaji's birthday (23 January) is Parakram Diwas."),
    ("National Science Day is celebrated on 28 February to mark:",
     ["C. V. Raman's announcement of the Raman effect (1928)", "The launch of Aryabhata", "Pokhran-II", "Homi Bhabha's birthday"], 0, PYQ + "National Technology Day (11 May) marks Pokhran-II (1998)."),
    ("National Sports Day, 29 August, is the birth anniversary of:",
     ["Major Dhyan Chand", "Milkha Singh", "P. T. Usha", "Sachin Tendulkar"], 0, PYQ + "The Khel Ratna award is named after Dhyan Chand."),
    ("Engineers' Day in India (15 September) honours:",
     ["Sir M. Visvesvaraya", "A. P. J. Abdul Kalam", "Satish Dhawan", "Vikram Sarabhai"], 0, PYQ + "He was Diwan of Mysore and built the Krishna Raja Sagara dam."),
    ("Constitution Day (Samvidhan Divas) is observed on:",
     ["26 November", "26 January", "15 August", "2 October"], 0, PYQ + "The Constituent Assembly adopted the Constitution on 26 November 1949; observed as Constitution Day since 2015."),
    ("National Education Day (11 November) commemorates the birth anniversary of:",
     ["Maulana Abul Kalam Azad", "Savitribai Phule", "Dr S. Radhakrishnan", "Jyotiba Phule"], 0, "Teachers' Day (5 September) is Dr Radhakrishnan's birthday."),
    ("Janjatiya Gaurav Divas, observed on 15 November, honours:",
     ["Birsa Munda", "Alluri Sitarama Raju", "Rani Gaidinliu", "Tantya Bhil"], 0, PYQ + "15 November is also Jharkhand's foundation day."),
    ("National Voters' Day, first observed in 2011, is on:",
     ["25 January – the Election Commission's foundation day", "26 January", "15 March", "2 October"], 0, "The Election Commission of India was set up on 25 January 1950."),
    ("Match the day with its date:\na. World Environment Day  b. International Yoga Day  c. World Health Day  d. World Population Day\n1. 11 July  2. 7 April  3. 21 June  4. 5 June",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Date matching appears in almost every GK paper."),
    ("Navy Day (4 December) commemorates:",
     ["Operation Trident – the attack on Karachi harbour in 1971", "The commissioning of INS Vikrant", "The Kargil victory", "The formation of the Navy in 1950"], 0, "Army Day – 15 January; Air Force Day – 8 October."),
    ("National Unity Day (Rashtriya Ekta Diwas), 31 October, marks the birth anniversary of:",
     ["Sardar Vallabhbhai Patel", "Indira Gandhi", "Lal Bahadur Shastri", "B. R. Ambedkar"], 0, "The Statue of Unity (Gujarat) is the world's tallest statue."),
    ("Kannada Rajyotsava is celebrated on 1 November because on that day in 1956:",
     ["The Kannada-speaking regions were united to form Mysore State", "Karnataka got its present name", "Kannada got classical status", "Bengaluru became the capital"], 0, PYQ + "The name 'Karnataka' was adopted on 1 November 1973."),
    ("Consider the statements:\nI. Good Governance Day (25 December) marks Atal Bihari Vajpayee's birth anniversary.\nII. Kisan Diwas (23 December) marks Chaudhary Charan Singh's birth anniversary.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): National Space Day is observed on 23 August.\nReason (R): Chandrayaan-3's lander Vikram touched down near the Moon's south pole on 23 August 2023.",
     AR, 0, "The landing point was named Shiv Shakti point."),
    ("National Technology Day (11 May) commemorates:",
     ["The Pokhran-II nuclear tests of 1998", "The launch of Aryabhata (1975)", "The first Indian computer", "The founding of ISRO"], 0,
     "Pokhran-I (Smiling Buddha) was in 1974."),
]

SLOGANS = [
    ("Which one of the following slogans of Tourism Department of Karnataka State is correct?",
     ["One State Many Worlds", "One State Many Countries", "One World Many States", "One Country Many Worlds"], 0,
     "Karnataka Tourism's tagline is 'One State, Many Worlds'." + NOTE, "VAO 2024 Paper-1 · Q98"),
    # --- new questions ---
    ("The theme of World Environment Day 2025, hosted by the Republic of Korea, was:",
     ["Ending plastic pollution (#BeatPlasticPollution)", "Land restoration (#GenerationRestoration)", "Only One Earth", "Ecosystem Restoration"], 0,
     PYQ + "2024: land restoration, desertification and drought resilience (host Saudi Arabia)."),
    ("The theme of the 11th International Day of Yoga (21 June 2025), with the main event at Visakhapatnam, was:",
     ["Yoga for One Earth, One Health", "Yoga for Self and Society", "Yoga for Humanity", "Yoga for Vasudhaiva Kutumbakam"], 0,
     PYQ + "2024 (Srinagar): Yoga for Self and Society."),
    ("World Health Day 2025's campaign 'Healthy beginnings, hopeful futures' focused on:",
     ["Maternal and newborn health", "Mental health at work", "Air pollution", "Antimicrobial resistance"], 0,
     "2024's theme was 'My health, my right'."),
    ("The slogan 'Jai Jawan Jai Kisan' was given by:",
     ["Lal Bahadur Shastri (1965)", "Jawaharlal Nehru", "Indira Gandhi", "Atal Bihari Vajpayee"], 0,
     PYQ + "Vajpayee added 'Jai Vigyan' (1998) and Narendra Modi 'Jai Anusandhan' (2019)."),
    ("Match the slogan with its originator:\na. Inquilab Zindabad  b. Swaraj is my birthright  c. Do or Die  d. Dilli Chalo\n1. Subhas Chandra Bose  2. Mahatma Gandhi  3. Bal Gangadhar Tilak  4. Maulana Hasrat Mohani",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0,
     PYQ + "Bhagat Singh popularised 'Inquilab Zindabad'."),
    ("'Vande Mataram', which completed 150 years in 2025, was written by Bankim Chandra Chattopadhyay and appears in his novel:",
     ["Anandamath", "Gitanjali", "Devdas", "Durgeshnandini"], 0, "It was adopted as the national song."),
    ("The national motto 'Satyameva Jayate' is taken from the:",
     ["Mundaka Upanishad", "Rigveda", "Bhagavad Gita", "Arthashastra"], 0, PYQ + "It is inscribed below the Lion Capital of Sarnath."),
    ("The motto of the Indian Air Force, 'Nabha Sparsham Deeptam', is taken from the:",
     ["Bhagavad Gita", "Rigveda", "Ramayana", "Kathopanishad"], 0, "Army: 'Service Before Self'; Navy: 'Sham No Varunah'."),
    ("The motto of the Supreme Court of India is:",
     ["Yato Dharmastato Jayah", "Satyameva Jayate", "Yogakshemam Vahamyaham", "Satyam Shivam Sundaram"], 0,
     "'Yogakshemam Vahamyaham' is LIC's motto; 'Satyam Shivam Sundaram' Doordarshan's."),
    ("The Olympic motto, expanded in 2021, is:",
     ["Citius, Altius, Fortius – Communiter (Faster, Higher, Stronger – Together)", "Peace through Sport", "One World, One Dream", "Unity in Diversity"], 0, "'Communiter' was added by the IOC in 2021."),
    ("The slogan 'Garibi Hatao' was associated with:",
     ["Indira Gandhi (1971)", "Rajiv Gandhi", "Morarji Desai", "V. P. Singh"], 0, "It was the theme of the 1971 general election."),
    ("The theme of International Women's Day 2025 (campaign by IWD) was:",
     ["Accelerate Action", "Inspire Inclusion", "Embrace Equity", "Break the Bias"], 0, "2024: Inspire Inclusion; 2023: Embrace Equity."),
    ("The theme of World Water Day 2025 was:",
     ["Glacier preservation", "Water for peace", "Accelerating change", "Groundwater – making the invisible visible"], 0, "2024: Water for peace."),
    ("The theme of National Voters' Day 2025 was:",
     ["Nothing Like Voting, I Vote for Sure", "Every vote counts", "Making our elections inclusive", "Electoral literacy for stronger democracy"], 0,
     "National Voters' Day is on 25 January."),
    ("'Saare Jahan Se Achha' was written by:",
     ["Muhammad Iqbal", "Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Sarojini Naidu"], 0, PYQ + "Tagore wrote 'Jana Gana Mana', the national anthem."),
    ("'Ek Kadam Swachhata Ki Or' is the tagline of:",
     ["Swachh Bharat Mission", "Make in India", "Digital India", "Beti Bachao Beti Padhao"], 0, "The mission was launched on 2 October 2014."),
    ("Consider the statements:\nI. 'Jai Anusandhan' was added to 'Jai Jawan, Jai Kisan, Jai Vigyan' by Prime Minister Modi in 2019.\nII. 'Jai Vigyan' was added by Atal Bihari Vajpayee after Pokhran-II.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): 'One State, Many Worlds' is the tagline of Karnataka Tourism.\nReason (R): Karnataka offers very diverse attractions – coast, hills, forests and heritage.",
     AR, 0, "Kerala's tagline is 'God's Own Country'."),
    ("Kerala Tourism's famous tagline is:",
     ["God's Own Country", "Incredible India", "The Heart of Incredible India", "Awesome Assam"], 0, "'The Heart of Incredible India' is Madhya Pradesh."),
]

# ---------------------------------------------------------------- CA-06 Festivals, folk dances and tribes
FESTIVALS = [
    ("Which Indian festival has been inscribed on UNESCO's list of 'Intangible Cultural Heritage of Humanity' during 20th UNESCO Intergovernmental Committee session at New Delhi's Red Fort held in December 2025?",
     ["Deepavali", "Dussehra", "Ganesh Chaturthi", "Holi"], 0,
     "Deepavali became India's 16th element on the list; Garba of Gujarat was added in 2023 and Durga Puja in 2021." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q83"),
    # --- new questions ---
    ("The Hornbill Festival, called the 'festival of festivals', is held every December in:",
     ["Nagaland", "Assam", "Mizoram", "Sikkim"], 0, PYQ + "It is held at Kisama Heritage Village near Kohima, 1–10 December."),
    ("Bihu is the main festival of:",
     ["Assam", "Odisha", "West Bengal", "Manipur"], 0, PYQ + "Rongali (Bohag) Bihu marks the Assamese new year in April."),
    ("Onam is celebrated in Kerala to welcome the legendary king:",
     ["Mahabali", "Ravana", "Bhagiratha", "Harishchandra"], 0, "Vallam Kali (snake-boat races) and pookalam are part of it."),
    ("Mysuru Dasara, the 'Nada Habba' of Karnataka, ends with the Jamboo Savari procession in which the idol of ____ is carried on an elephant.",
     ["Goddess Chamundeshwari", "Lord Ganesha", "Lord Rama", "Goddess Saraswati"], 0, PYQ + "Dasara was revived on a grand scale by the Wodeyars from the Vijayanagara tradition."),
    ("The Bengaluru Karaga festival, centred on the Dharmaraya Swamy temple, is celebrated mainly by the:",
     ["Thigala community", "Kodava community", "Siddi community", "Lambani community"], 0, "The Karaga bearer carries a decorated pot on his head through the night."),
    ("Kambala, the traditional buffalo race in slushy paddy fields, is held in:",
     ["Coastal Karnataka (Dakshina Kannada and Udupi)", "North Karnataka", "Kodagu only", "Bengaluru"], 0, PYQ + "A 2017 law allowed it to continue after the jallikattu debate."),
    ("Match the festival with the state:\na. Hornbill  b. Pongal  c. Chhath  d. Losar\n1. Ladakh / Sikkim  2. Bihar  3. Tamil Nadu  4. Nagaland",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Festival–state matching is very common."),
    ("Which of the following is on UNESCO's Intangible Cultural Heritage list for India?",
     ["Kumbh Mela (2017)", "Mysuru Dasara", "Hornbill Festival", "Pushkar Fair"], 0,
     "Others include Yoga (2016), Durga Puja in Kolkata (2021), Garba (2023) and Deepavali (2025)."),
    ("Ugadi, the new-year festival, is celebrated mainly in:",
     ["Karnataka, Andhra Pradesh and Telangana", "Punjab and Haryana", "Assam and Bengal", "Gujarat and Rajasthan"], 0, "Bevu-bella (neem and jaggery) symbolises life's bitter and sweet experiences."),
    ("The Pushkar camel fair is held in:",
     ["Rajasthan", "Gujarat", "Haryana", "Uttar Pradesh"], 0, "It takes place around Kartik Purnima."),
    ("The Hampi Utsav (Vijaya Utsav) celebrates the heritage of:",
     ["The Vijayanagara empire", "The Hoysalas", "The Wodeyars", "The Kadambas"], 0, "It is organised by the Karnataka government at Hampi."),
    ("Bathukamma, a floral festival celebrated by women, is associated with:",
     ["Telangana", "Kerala", "Odisha", "Goa"], 0, "Bonalu is another festival of Telangana."),
    ("Nuakhai, the harvest festival of eating new rice, is celebrated in:",
     ["Western Odisha", "Punjab", "Kerala", "Manipur"], 0, "Wangala is the harvest festival of the Garos of Meghalaya."),
    ("The Hemis festival, celebrating Guru Padmasambhava with masked Cham dances, is held in:",
     ["Ladakh", "Sikkim", "Arunachal Pradesh", "Himachal Pradesh"], 0, "Hemis is the largest monastery in Ladakh."),
    ("The Sangai festival, named after the brow-antlered deer, is held in:",
     ["Manipur", "Mizoram", "Tripura", "Meghalaya"], 0, "The sangai lives in Keibul Lamjao, the only floating national park."),
    ("Consider the statements:\nI. Garba of Gujarat was added to UNESCO's Intangible Cultural Heritage list in 2023.\nII. Durga Puja in Kolkata was added in 2021.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Deepavali is now an element of UNESCO's Intangible Cultural Heritage list.\nReason (R): It was inscribed at the 20th session of the UNESCO committee held at the Red Fort, New Delhi, in December 2025.",
     AR, 0, "India hosted the committee session for the first time."),
    ("Bhoota Kola, a ritual performance worshipping local spirits (daivas), is associated with:",
     ["Tulu Nadu (coastal Karnataka)", "Kodagu", "Hyderabad-Karnataka", "Old Mysore"], 0, "The film 'Kantara' brought it wide attention."),
    ("Puthari (Huttari), the harvest festival with new paddy, is the main festival of:",
     ["Kodagu (the Kodavas)", "Udupi", "Bidar", "Chikkamagaluru"], 0, "Kailpodh (festival of arms) is another Kodava festival."),
]

DANCES_TRIBES = [
    ("Madhvi Mudgal is a renowned exponent of which of the following dance forms?",
     ["Odissi", "Bharatanatyam", "Kuchipudi", "Kathakali"], 0, "Odissi is the classical dance of Odisha." + NOTE, "PSI 2023 General Paper · Q93"),
    ("Bharatanatyam, one of the dance forms, is the major dance art of which state?",
     ["Karnataka", "Kerala", "Tamil Nadu", "Andhra Pradesh"], 2, "Bharatanatyam developed in the temples of Tamil Nadu." + NOTE, "KRIES 2025 entrance · Q84"),
    ("The district in which the Jenu Kuruba tribals live is:",
     ["Kodagu", "Dakshina Kannada", "Kalaburagi", "Belagavi"], 0,
     "Jenu Kurubas ('honey gatherers', a PVTG) live in the forests of Kodagu, Mysuru and Chamarajanagar." + NOTE, "KRIES 2024 entrance · Q85"),
    ("The 'Bhil' tribes are found in these four states of India.",
     ["Rajasthan, Haryana, Odisha, West Bengal", "Rajasthan, Madhya Pradesh, Himachal Pradesh, Punjab", "Rajasthan, Haryana, Madhya Pradesh, Odisha", "Rajasthan, Gujarat, Maharashtra, Madhya Pradesh"], 3,
     "The Bhils, India's largest tribal group, live mainly in these western and central states." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q5"),
    ("Which one of the following tribes is not correctly matched?",
     ["Birhor - Chhattisgarh", "Apatani - Arunachal Pradesh", "Kadar - Tamil Nadu", "Jaunsari - Maharashtra"], 3,
     "The Jaunsari live in the Jaunsar-Bawar region of Uttarakhand." + NOTE, "PSI 2024 General Paper · Q32"),
    # --- new questions ---
    ("How many classical dance forms are recognised by the Sangeet Natak Akademi?",
     ["Eight", "Six", "Ten", "Twelve"], 0, PYQ + "Bharatanatyam, Kathak, Kathakali, Kuchipudi, Odissi, Manipuri, Sattriya and Mohiniyattam (the Ministry of Culture also lists Chhau)."),
    ("Match the classical dance with its state:\na. Kathakali  b. Kuchipudi  c. Sattriya  d. Kathak\n1. Uttar Pradesh  2. Assam  3. Andhra Pradesh  4. Kerala",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Mohiniyattam is also from Kerala."),
    ("Yakshagana, combining dance, music, dialogue and elaborate costumes, is a traditional theatre form mainly of:",
     ["Coastal and Malnad Karnataka", "North-east India", "Punjab", "Gujarat"], 0, PYQ + "It has Tenkutittu (southern) and Badagutittu (northern) styles."),
    ("Dollu Kunitha, performed with large drums, is a folk dance of Karnataka associated mainly with the:",
     ["Kuruba community", "Siddi community", "Kodava community", "Lambani community"], 0, PYQ + "It is linked to the worship of Beereshwara."),
    ("Match the Karnataka folk art with its description:\na. Veeragase  b. Kamsale  c. Togalu Gombeyata  d. Huli Vesha\n1. Tiger dance of Udupi during Navaratri  2. Leather-puppet shadow play  3. Cymbal dance by devotees of Male Mahadeshwara  4. Vigorous dance on the legend of Veerabhadra",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Karnataka's folk arts are a favourite topic in KEA papers."),
    ("Match the folk dance with its state:\na. Bihu  b. Lavani  c. Ghoomar  d. Garba\n1. Gujarat  2. Rajasthan  3. Maharashtra  4. Assam",
     ["a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1", "a-4, b-2, c-3, d-1", "a-4, b-3, c-1, d-2"], 0, PYQ + "Bhangra and Giddha are from Punjab."),
    ("Cheraw, the bamboo dance, belongs to:",
     ["Mizoram", "Tripura", "Kerala", "Goa"], 0, "Hojagiri is a dance of the Reang tribe of Tripura."),
    ("The Siddi community of Karnataka, of African descent, lives mainly in the district of:",
     ["Uttara Kannada", "Kolar", "Bidar", "Mandya"], 0, PYQ + "Many live around Yellapur, Haliyal and Ankola."),
    ("The Soliga tribe, who won forest rights inside a tiger reserve, live mainly in the:",
     ["Biligiri Rangana (BR) Hills, Chamarajanagar", "Western Ghats of Uttara Kannada", "Bidar plateau", "Kolar gold fields"], 0, "BRT Tiger Reserve is in Chamarajanagar district."),
    ("The Koraga tribe, a PVTG of Karnataka, live mainly in:",
     ["Udupi and Dakshina Kannada", "Kalaburagi and Bidar", "Kodagu and Hassan", "Ballari and Raichur"], 0, "Karnataka's PVTGs are the Koraga and the Jenu Kuruba."),
    ("The Toda tribe, known for their pastoral life and barrel-vaulted huts, live in the:",
     ["Nilgiri hills of Tamil Nadu", "Aravalli hills", "Khasi hills", "Satpura range"], 0, PYQ + "They are a PVTG."),
    ("The Jarawa, Onge, Sentinelese and Great Andamanese are tribes of:",
     ["The Andaman and Nicobar Islands", "Lakshadweep", "Kerala", "Assam"], 0, "All four are PVTGs; the Sentinelese avoid contact with outsiders."),
    ("According to Census 2011, Scheduled Tribes form about ____ of India's population.",
     ["8.6%", "16.6%", "2.5%", "25%"], 0, PYQ + "The Bhils are the largest tribe, followed by the Gonds."),
    ("The Santhal tribe is found mainly in:",
     ["Jharkhand, West Bengal and Odisha", "Kerala and Tamil Nadu", "Punjab and Haryana", "Goa and Maharashtra"], 0, "Their language Santali is in the Eighth Schedule (Ol Chiki script)."),
    ("Consider the statements:\nI. Chhau is a masked dance of Jharkhand, Odisha and West Bengal on UNESCO's list.\nII. Yakshagana is a classical dance recognised by the Sangeet Natak Akademi.\nWhich is/are correct?",
     I_II, 0, "Yakshagana is a folk theatre form, not one of the classical dances."),
]

TOPICS = {
    "Currency and Capitals of Countries": [("1 · Asia and Oceania", ASIA),
                                           ("2 · Europe, Africa and the Americas", WORLD)],
    "Important Days and Slogans": [("1 · National and International Days", DAYS),
                                   ("2 · Themes, Slogans and Mottos", SLOGANS)],
    "Festivals, Folk Dances, Tribes of the Country": [("1 · Festivals and Fairs", FESTIVALS),
                                                      ("2 · Classical and Folk Dances, and Tribes", DANCES_TRIBES)],
}

NOTES = {
    "Currency and Capitals of Countries": [{"title": "Countries – capitals – currencies (flash list)", "md": """# Countries, capitals and currencies

## India's neighbours
| Country | Capital | Currency |
|---|---|---|
| Pakistan | Islamabad | Pakistani rupee |
| Nepal | Kathmandu | Nepalese rupee |
| Bhutan | Thimphu | **Ngultrum** |
| Bangladesh | Dhaka | **Taka** |
| Sri Lanka | **Sri Jayawardenepura Kotte** (legislative) / Colombo (commercial) | Sri Lankan rupee |
| Maldives | Malé | **Rufiyaa** |
| Myanmar | **Naypyidaw** (since 2005–06; earlier Yangon) | **Kyat** |
| China | Beijing | Renminbi (Yuan) |
| Afghanistan | Kabul | Afghani |

## Rest of Asia and Oceania
| Country | Capital | Currency |
|---|---|---|
| Japan | Tokyo | Yen |
| South Korea / North Korea | Seoul / Pyongyang | Won |
| Thailand | Bangkok | **Baht** |
| Vietnam | **Hanoi** | **Dong** |
| Indonesia | Jakarta (→ **Nusantara**) | **Rupiah** |
| Malaysia | Kuala Lumpur (admin. Putrajaya) | **Ringgit** |
| Philippines | Manila | Peso |
| Cambodia / Laos | Phnom Penh / Vientiane | Riel / Kip |
| Mongolia | Ulaanbaatar | Tugrik |
| Kazakhstan | **Astana** | Tenge |
| Iran / Iraq | Tehran / Baghdad | Rial / Dinar |
| Saudi Arabia | Riyadh | Riyal |
| UAE | **Abu Dhabi** | **Dirham** |
| Qatar / Oman | Doha / Muscat | Riyal / Rial |
| **Kuwait** | Kuwait City | **Dinar – highest-valued currency unit** |
| Türkiye | **Ankara** | Lira |
| Israel | Jerusalem (proclaimed) | Shekel |
| Australia / New Zealand | **Canberra** / Wellington | Dollar |

## Europe
| Country | Capital | Currency |
|---|---|---|
| UK | London | **Pound sterling** |
| France / Germany / Italy / Spain | Paris / Berlin / Rome / Madrid | Euro |
| Netherlands | Amsterdam (govt. **The Hague**) | Euro |
| Switzerland | **Bern** | **Swiss franc** |
| Russia | Moscow | Ruble |
| Ukraine | Kyiv | **Hryvnia** |
| Poland | Warsaw | **Złoty** |
| Hungary | Budapest | **Forint** |
| Czechia | Prague | Koruna |
| Sweden / Norway / Denmark | Stockholm / Oslo / Copenhagen | Krona / Krone / Krone |
| Croatia (euro 2023), **Bulgaria (euro Jan 2026)** | Zagreb / Sofia | Euro |

## Africa
| Country | Capital | Currency |
|---|---|---|
| South Africa | **Pretoria** (exec.), Cape Town (leg.), Bloemfontein (jud.) | **Rand** |
| Egypt | Cairo | Egyptian pound |
| Nigeria | **Abuja** | **Naira** |
| Kenya | Nairobi | Shilling |
| Ethiopia | Addis Ababa (AU HQ) | **Birr** |
| Ghana | Accra | **Cedi** |
| Tanzania | **Dodoma** | Shilling |
| Morocco | Rabat | Dirham |
| Cameroon | **Yaoundé** (WTO MC14, 2026) | CFA franc |

## Americas
| Country | Capital | Currency |
|---|---|---|
| USA | Washington, D.C. | US dollar |
| Canada | **Ottawa** | Canadian dollar |
| Mexico | Mexico City | Peso |
| Brazil | **Brasília** | **Real** |
| Argentina | Buenos Aires | Peso |
| Peru | Lima | **Sol** |
| Chile / Colombia | Santiago / Bogotá | Peso |
| Venezuela | Caracas | Bolívar |
| Cuba | Havana | Peso |
| Bolivia | Sucre (const.) / La Paz (govt.) | Boliviano |

**Traps:** Turkey – Ankara (not Istanbul) · Australia – Canberra (not Sydney) · Brazil – Brasília (not Rio) · Nigeria – Abuja (not Lagos) · Vietnam – Hanoi · Myanmar – Naypyidaw · Bhutan uses the ngultrum, not the rupee.
"""}],
    "Important Days and Slogans": [{"title": "Important days, themes and slogans – month-wise list", "md": """# Important days (month-wise)

| Date | Day | Why / remember |
|---|---|---|
| 9 Jan | **Pravasi Bharatiya Divas** | Gandhiji returned from South Africa, **9 Jan 1915** |
| 12 Jan | National Youth Day | Swami Vivekananda |
| 15 Jan | Army Day | Gen. K. M. Cariappa became first Indian C-in-C (1949) |
| 23 Jan | Parakram Diwas | Netaji Subhas Chandra Bose |
| 24 Jan | National Girl Child Day | |
| 25 Jan | **National Voters' Day** (since 2011) | ECI founded 25 Jan 1950 · 2025 theme *"Nothing Like Voting, I Vote for Sure"* |
| 30 Jan | Martyrs' Day | Gandhiji's death |
| 10 Feb (+10 Aug) | **National Deworming Day** | **Albendazole** for children 1–19 |
| 28 Feb | **National Science Day** | C. V. Raman's Raman effect (1928) |
| 8 Mar | International Women's Day | 2025 IWD theme *"Accelerate Action"* |
| 22 Mar | World Water Day | 2025: *Glacier preservation* |
| 7 Apr | World Health Day | 2025: *Healthy beginnings, hopeful futures* · 2024: *My health, my right* |
| 22 Apr | Earth Day | |
| 11 May | National Technology Day | Pokhran-II (1998) |
| 31 May | World No Tobacco Day | |
| 5 Jun | **World Environment Day** | 2025 host **Republic of Korea** – *Ending plastic pollution* · 2024 host Saudi Arabia – land restoration |
| 21 Jun | **International Day of Yoga** | 2025 (11th): *Yoga for One Earth, One Health*, Visakhapatnam · 2024: *Yoga for Self and Society*, Srinagar |
| 11 Jul | World Population Day | ("Day of 8 Billion" = **15 Nov 2022**) |
| 7 Aug | National Handloom Day | Swadeshi Movement launched 7 Aug 1905 |
| 23 Aug | **National Space Day** (first 2024) | Chandrayaan-3 landing, 2023 |
| 29 Aug | National Sports Day | Major Dhyan Chand |
| 5 Sep | Teachers' Day | Dr S. Radhakrishnan |
| 8 Sep | International Literacy Day | |
| 14 Sep | Hindi Diwas | |
| 15 Sep | **Engineers' Day** | **Sir M. Visvesvaraya** |
| 2 Oct | Gandhi Jayanti / Intl. Day of Non-Violence | |
| 8 Oct | Air Force Day | |
| 10 Oct | World Mental Health Day | |
| last week Oct | **Vigilance Awareness Week** | includes **31 Oct** |
| 31 Oct | National Unity Day | Sardar Patel |
| 1 Nov | **Kannada Rajyotsava** | Mysore State formed 1956; renamed Karnataka 1973 |
| 11 Nov | National Education Day | Maulana Azad |
| 14 Nov | Children's Day | Nehru |
| 15 Nov | **Janjatiya Gaurav Divas** | Birsa Munda |
| 26 Nov | **Constitution Day** (since 2015) | Constitution adopted 1949 |
| 1 Dec | World AIDS Day | |
| 4 Dec | Navy Day | Operation Trident, 1971 |
| 10 Dec | Human Rights Day | |
| 23 Dec | Kisan Diwas | Chaudhary Charan Singh |
| 25 Dec | Good Governance Day | Atal Bihari Vajpayee |

## Slogans
| Slogan | Given by |
|---|---|
| Jai Jawan Jai Kisan (1965) | Lal Bahadur Shastri → **Jai Vigyan** (Vajpayee, 1998) → **Jai Anusandhan** (Modi, 2019) |
| Swaraj is my birthright | Bal Gangadhar Tilak |
| Do or Die (1942) | Mahatma Gandhi |
| Inquilab Zindabad | Maulana Hasrat Mohani (popularised by Bhagat Singh) |
| Dilli Chalo / Jai Hind / Give me blood… | Subhas Chandra Bose |
| Simon Go Back | protest of 1928 (Lala Lajpat Rai) |
| Vande Mataram (**150 years in 2025**) | Bankim Chandra – *Anandamath* |
| Saare Jahan Se Achha | Muhammad Iqbal |
| Garibi Hatao (1971) | Indira Gandhi |

## Mottos and taglines
Satyameva Jayate – **Mundaka Upanishad** · Supreme Court – *Yato Dharmastato Jayah* · Army – *Service Before Self* · Navy – *Sham No Varunah* · Air Force – *Nabha Sparsham Deeptam* (Gita) · LIC – *Yogakshemam Vahamyaham* · Doordarshan – *Satyam Shivam Sundaram* · Olympics – *Citius, Altius, Fortius – Communiter* · **Karnataka Tourism – "One State, Many Worlds"** · Kerala – "God's Own Country" · MP – "The Heart of Incredible India" · Swachh Bharat – *Ek Kadam Swachhata Ki Or*.
"""}],
    "Festivals, Folk Dances, Tribes of the Country": [{"title": "Festivals, folk dances and tribes – revision notes", "md": """# Festivals, folk dances and tribes

## 1. India on UNESCO's Intangible Cultural Heritage list (16 elements)
Vedic chanting · Ramlila · Kutiyattam · Ramman (Garhwal) · Mudiyettu (Kerala) · Kalbelia (Rajasthan) · **Chhau** · Buddhist chanting of Ladakh · Sankirtana (Manipur) · Thatheras of Jandiala Guru (brass work) · **Yoga (2016)** · Nowruz (2016) · **Kumbh Mela (2017)** · **Durga Puja in Kolkata (2021)** · **Garba of Gujarat (2023)** · **Deepavali (Dec 2025 – 20th session at the Red Fort, New Delhi)**.

## 2. Festivals and fairs
| Festival | State / notes |
|---|---|
| **Hornbill** – "festival of festivals" | Nagaland, 1–10 Dec, Kisama near Kohima |
| Bihu | Assam (Rongali/Bohag Bihu in April) |
| Pongal | Tamil Nadu |
| Onam | Kerala – King **Mahabali**; Vallam Kali boat races |
| Chhath | Bihar |
| Losar | Ladakh, Sikkim (Tibetan new year) |
| Hemis | Ladakh (masked Cham dance) |
| Sangai | Manipur |
| Wangala | Meghalaya (Garo harvest) |
| Nuakhai | Western Odisha |
| Bathukamma, Bonalu | Telangana |
| Pushkar fair | Rajasthan |
| Ugadi | Karnataka, Andhra, Telangana (bevu-bella) |

### Karnataka
**Mysuru Dasara** (Nada Habba; Jamboo Savari with Goddess **Chamundeshwari**) · **Bengaluru Karaga** (Thigala community, Dharmaraya Swamy temple) · **Kambala** (buffalo race, coastal Karnataka) · **Hampi Utsav / Vijaya Utsav** · **Bhoota Kola** (Tulu Nadu daiva worship) · **Huttari (Puthari)** & Kailpodh (Kodagu) · Karnataka Bird Festival.

## 3. Classical dances (Sangeet Natak Akademi – 8)
Bharatanatyam – **Tamil Nadu** · Kathak – Uttar Pradesh · Kathakali – Kerala · Mohiniyattam – Kerala · Kuchipudi – Andhra Pradesh · **Odissi – Odisha (Madhavi Mudgal, Kelucharan Mohapatra)** · Manipuri – Manipur · Sattriya – Assam. (Chhau is also listed by the Ministry of Culture.)

## 4. Folk dances
| Dance | State |
|---|---|
| Bihu | Assam |
| Garba, Dandiya | Gujarat |
| Bhangra, Giddha | Punjab |
| Lavani | Maharashtra |
| Ghoomar, Kalbelia | Rajasthan |
| Chhau | Jharkhand, Odisha, West Bengal |
| Theyyam | Kerala |
| Karakattam | Tamil Nadu |
| Cheraw (bamboo) | Mizoram |
| Hojagiri | Tripura (Reang) |

### Karnataka folk arts
**Yakshagana** (coast & Malnad – Tenkutittu/Badagutittu) · **Dollu Kunitha** (Kuruba community, big drums) · **Veeragase** (Veerabhadra legend) · **Kamsale** (Male Mahadeshwara devotees, cymbals) · Pooja Kunitha · Kolata · **Huli Vesha** (tiger dance, Udupi) · **Togalu Gombeyata** (leather puppetry) · Gaarudi Gombe · Somana Kunitha · Suggi Kunitha · Lambani dance.

## 5. Tribes
- **ST population (Census 2011): 8.6%.** Largest: **Bhil** (Rajasthan, Gujarat, Maharashtra, MP), then **Gond**.
- **PVTGs: 75** – mission **PM-JANMAN** (2023). **Janjatiya Gaurav Divas** – 15 Nov (Birsa Munda).

| Tribe | Region |
|---|---|
| Santhal | Jharkhand, WB, Odisha (Santali – Ol Chiki) |
| Munda, Oraon, Ho | Jharkhand |
| Toda, Kurumba, Irula | Nilgiris (TN) |
| Jarawa, Onge, Sentinelese, Great Andamanese, Shompen | Andaman & Nicobar |
| Khasi, Garo, Jaintia | Meghalaya |
| **Apatani** | Arunachal (Ziro valley) |
| Bodo | Assam |
| Baiga | Madhya Pradesh |
| Chenchu | Andhra / Telangana |
| **Jaunsari** | **Uttarakhand** (Jaunsar-Bawar) |
| Birhor | Jharkhand, Chhattisgarh |
| Kadar | Kerala, Tamil Nadu |

### Karnataka
**Jenu Kuruba** (PVTG; Kodagu, Mysuru, Chamarajanagar) · Kadu Kuruba · **Soliga** (BR Hills, Chamarajanagar) · **Siddi** (African descent; Uttara Kannada – Yellapur, Haliyal) · **Koraga** (PVTG; Udupi, Dakshina Kannada) · Hakki Pikki · Lambani (Banjara).
"""}],
}
