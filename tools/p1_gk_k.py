"""Paper 1 · General Knowledge · P1-GK-14 Awards, Honours and Prizes (2 sets × 20), with detailed revision NOTES. Shared by GPSTR and
KRIES (Paper 1 item A), so English like the other GK topics. References: Ministry of Home Affairs (Padma / Bharat Ratna lists),
Bharatiya Jnanpith, Directorate of Film Festivals, nobelprize.org, thebookerprizes.com, Karnataka Kannada and Culture Department.
Only settled facts up to mid-2026 are used; the 2026 Nobel and Booker results are not included. REAL previous-year questions come from
the KEA 2025–26 GK papers; answers worked out by ExamSim. Skipped as unclear: KEA 2026 GK-1 (HK) Q87 (Rajyotsava 2025 fields);
GK-2 (NHK) Q97; GK-3 (HK) Q69, Q74, Q77 (2025–26 facts that could not be checked)."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

INDIAN_AWARDS = [
    ("Consider the following statements related to Rashtriya Vigyan Puraskar Awards.\n(a) They are the National Awards in the field of Science, "
     "Technology and Innovation\n(b) The awards are given in four categories viz. Vigyan Ratna, Vigyan Shri, Vigyan Yuva-Shanti Swarup Bhatnagar and "
     "Vigyan Team\n(c) The awards are given in 13 domains\n(d) The Award Ceremony for all categories of awards will be held on 28th February "
     "(National Science Day) every year\nHow many of the above statements is/are correct?",
     ["All of them", "Only three", "Only two", "Only one"], 1,
     "(a), (b), (c) are correct. The awards are announced on 11 May (National Technology Day) and presented on 23 August (National Space Day), "
     "not 28 February. They replaced about 300 older science awards, including the Shanti Swarup Bhatnagar Prize, from 2024." + NOTE,
     "KEA 2025 GK (HK, 21 Dec 2025) · Q51"),
    ("Which of the following statements regarding Kumari Kamala, a renowned Bharatanatyam artist, is incorrect?",
     ["She was trained under Vazhuvoor Ramaiah Pillai", "She was awarded with Padma Vibhushan award in 1970",
      "She was the recipient of US National Heritage Fellowship", "She also acted in almost 100 Tamil, Hindi, Telugu and Kannada films"], 1,
     "Kamala received the Padma BHUSHAN in 1970, not the Padma Vibhushan. She trained in the Vazhuvoor style and later taught in the USA, "
     "where she received the National Heritage Fellowship (2010)." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q62"),
    ("Dr. Subhash C. Kashyap, an expert on the Indian Constitution, passed away on 4 June 2026. Identify the incorrect statement/s about him.\n"
     "(a) He was the Secretary-General of the 7th, 8th and 9th Lok Sabha.\n(b) He was honoured with the Padma Bhushan award.\n"
     "(c) He was the Chairman of the high-level committee on 'One Nation, One Election'.",
     ["(a) and (b)", "Only (a)", "Only (c)", "Only (b)"], 2,
     "(a) and (b) are true (Lok Sabha Secretary-General 1984–90; Padma Bhushan 2015). The One Nation, One Election committee (2023–24) was chaired "
     "by former President Ram Nath Kovind." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q72"),
    ("In which year were the Bharat Ratna and the Padma awards instituted?",
     ["1954", "1950", "1947", "1961"], 0,
     PYQ + "Both were instituted on 2 January 1954. The order of precedence is Bharat Ratna > Padma Vibhushan > Padma Bhushan > Padma Shri."),
    ("Who were the first recipients of the Bharat Ratna in 1954?",
     ["C. Rajagopalachari, S. Radhakrishnan and C. V. Raman", "Jawaharlal Nehru, Rajendra Prasad and Sardar Patel",
      "M. Visvesvaraya, Govind Ballabh Pant and Zakir Husain", "B. R. Ambedkar, Abul Kalam Azad and Mahatma Gandhi"], 0,
     PYQ + "M. Visvesvaraya of Karnataka received it in 1955. Lal Bahadur Shastri (1966) was the first posthumous recipient; Indira Gandhi (1971) the first woman."),
    ("Which of the following persons connected with Karnataka has NOT received the Bharat Ratna?",
     ["Kuvempu", "M. Visvesvaraya", "C. N. R. Rao", "Bhimsen Joshi"], 0,
     "Visvesvaraya – 1955; Bhimsen Joshi (born in Gadag) – 2009; C. N. R. Rao (Bengaluru) – 2014. Kuvempu received the Padma Vibhushan, Jnanpith and Karnataka Ratna."),
    ("Who were among the five persons awarded the Bharat Ratna in 2024?",
     ["Karpoori Thakur, L. K. Advani, P. V. Narasimha Rao, Chaudhary Charan Singh and M. S. Swaminathan",
      "Pranab Mukherjee, Nanaji Deshmukh, Bhupen Hazarika, Atal Bihari Vajpayee and Madan Mohan Malaviya",
      "Sachin Tendulkar, C. N. R. Rao, Lata Mangeshkar, Bhimsen Joshi and Amartya Sen",
      "Ratan Tata, Manmohan Singh, Mulayam Singh Yadav, Zakir Hussain and Sharad Yadav"], 0,
     "2024 was the first year with five awards (the usual limit is three a year); four were posthumous – Advani was the only living recipient."),
    ("Who is the only sportsperson to have received the Bharat Ratna (2014)?",
     ["Sachin Tendulkar", "Dhyan Chand", "Milkha Singh", "Viswanathan Anand"], 0,
     PYQ + "He is also its youngest recipient (aged 40). The Khel Ratna was renamed the Major Dhyan Chand Khel Ratna in 2021."),
    ("Which foreign nationals have received the Bharat Ratna?",
     ["Khan Abdul Ghaffar Khan and Nelson Mandela", "Nelson Mandela and Barack Obama", "Dalai Lama and Aung San Suu Kyi", "Mother Teresa and Martin Luther King Jr."], 0,
     "Khan Abdul Ghaffar Khan ('Frontier Gandhi') – 1987; Nelson Mandela – 1990. Mother Teresa (1980) was a naturalised Indian citizen."),
    ("The highest wartime and peacetime gallantry awards of India are respectively:",
     ["Param Vir Chakra and Ashoka Chakra", "Ashoka Chakra and Param Vir Chakra", "Maha Vir Chakra and Kirti Chakra", "Vir Chakra and Shaurya Chakra"], 0,
     PYQ + "Wartime: Param Vir > Maha Vir > Vir Chakra. Peacetime: Ashoka > Kirti > Shaurya Chakra. Major Somnath Sharma received the first Param Vir Chakra (1947)."),
    ("The first Jnanpith Award (1965) was given to:",
     ["G. Sankara Kurup (Malayalam) for 'Odakkuzhal'", "Kuvempu (Kannada) for 'Sri Ramayana Darshanam'", "Tarashankar Bandyopadhyay (Bengali)", "Sumitranandan Pant (Hindi)"], 0,
     PYQ + "The award was set up in 1961 by the Bharatiya Jnanpith trust. Kuvempu (1967) was the first Kannada winner."),
    ("Match the Kannada Jnanpith winners with the year of the award:\na. D. R. Bendre  b. Shivaram Karanth  c. U. R. Ananthamurthy  d. Chandrashekhar Kambar\n"
     "1. 1973  2. 1977  3. 1994  4. 2010",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-2, c-4, d-3", "a-3, b-2, c-1, d-4"], 0,
     PYQ + "Kannada's eight: Kuvempu 1967, Bendre 1973, Karanth 1977, Masti 1983, V. K. Gokak 1990, Ananthamurthy 1994, Girish Karnad 1998, Kambar 2010."),
    ("Which language has received the most Jnanpith Awards?",
     ["Hindi", "Kannada", "Bengali", "Malayalam"], 0,
     "Hindi leads, followed by Kannada with 8. The 59th award (2024) went to Vinod Kumar Shukla (Hindi); the 58th (2023) to Gulzar and Jagadguru Rambhadracharya."),
    ("The Dadasaheb Phalke Award is India's highest award in the field of:",
     ["Cinema", "Literature", "Classical music", "Journalism"], 0,
     PYQ + "Instituted in 1969; first recipient Devika Rani. Dr. Rajkumar (1995) is the Kannada recipient. Mohanlal received the award for 2023 (announced 2025)."),
    ("Consider the statements:\nI. The Dronacharya Award is given to outstanding sports coaches.\nII. The Arjuna Award is given for lifetime achievement in coaching.\nWhich is/are correct?",
     I_II, 0, "Only I. Arjuna Award (1961) – for consistent outstanding performance by sportspersons; Dronacharya (1985) – coaches; Dhyan Chand Award – lifetime achievement."),
    ("The Gandhi Peace Prize is awarded by:",
     ["The Government of India", "The United Nations", "The Gandhi Smarak Nidhi only", "The Nobel Committee"], 0,
     "Instituted in 1995 on Gandhi's 125th birth anniversary; it carries ₹1 crore. Gita Press, Gorakhpur received it for 2021."),
    ("National Teachers' Awards are presented every year on:",
     ["5 September", "14 November", "11 November", "15 September"], 0,
     PYQ + "Teachers' Day – birthday of Dr. S. Radhakrishnan. 14 November – Children's Day; 11 November – National Education Day (Maulana Azad); 15 September – Engineers' Day (Visvesvaraya)."),
    ("The Sahitya Akademi Award is given for literature in how many languages?",
     ["24", "22", "18", "28"], 0,
     "The 22 Eighth Schedule languages plus English and Rajasthani. The Akademi was founded in 1954; the Bhasha Samman honours other languages."),
    ("Which award is given to Indian writers for outstanding contribution to Indian literature and is India's highest literary award?",
     ["Jnanpith Award", "Saraswati Samman", "Vyas Samman", "Sahitya Akademi Fellowship"], 0,
     PYQ + "The Saraswati Samman (K. K. Birla Foundation, 1991) is given for a single work published in the previous 10 years."),
    ("Assertion (A): Padma awards are announced on the eve of Republic Day.\nReason (R): The Padma awards are conferred by the President of India.",
     AR, 1, "Both are true, but R does not explain A – the timing is a convention; investiture ceremonies are held at Rashtrapati Bhavan in March–April."),
]

WORLD_KARNATAKA_AWARDS = [
    ("Which of the following statement/statements is/are correct with respect to the prestigious Booker Prize 2025?\n(a) David Szalay, Hungarian-British author, "
     "has won the Booker Prize 2025 for his novel 'Flesh'.\n(b) Indian author Kiran Desai's 'The Loneliness of Sonia and Sunny' was shortlisted for the final round.\n"
     "(c) Samantha Harvey's 'Orbital' novel won the Booker Prize 2025.\n(d) Banu Mushtaq's 'Heart Lamp' won the Booker Prize 2025.",
     ["(a), (b) and (c)", "(a), (c) and (d)", "(b) and (d)", "(a) and (b)"], 3,
     "'Orbital' won the 2024 Booker; 'Heart Lamp' won the 2025 INTERNATIONAL Booker (for translated fiction), a different prize." + NOTE,
     "KEA 2026 GK-3 (NHK, 10 May 2026) · Q87"),
    ("Banu Mushtaq's 'Heart Lamp', winner of the International Booker Prize 2025, was translated from which language, and by whom?",
     ["Kannada – Deepa Bhasthi", "Urdu – Daisy Rockwell", "Malayalam – Deepa Bhasthi", "Kannada – Daisy Rockwell"], 0,
     PYQ + "First Kannada book and first short-story collection to win; Banu Mushtaq is from Hassan. Geetanjali Shree's 'Tomb of Sand' (Hindi, translated by Daisy Rockwell) won in 2022."),
    ("Who won the Nobel Peace Prize 2025?",
     ["María Corina Machado", "Nihon Hidankyo", "Narges Mohammadi", "Ales Bialiatski"], 0,
     "Venezuelan opposition leader, for her struggle for democracy. Nihon Hidankyo – 2024; Narges Mohammadi – 2023."),
    ("The Nobel Prize in Literature 2025 was awarded to:",
     ["László Krasznahorkai", "Han Kang", "Jon Fosse", "Annie Ernaux"], 0,
     "Hungarian novelist. Han Kang (South Korea) – 2024; Jon Fosse (Norway) – 2023; Annie Ernaux (France) – 2022."),
    ("The Nobel Prize in Chemistry 2025 (Kitagawa, Robson and Yaghi) was awarded for the development of:",
     ["Metal–organic frameworks (MOFs)", "Lithium-ion batteries", "CRISPR gene editing", "Quantum dots"], 0,
     "MOFs are porous crystals that can capture CO₂ or harvest water from air. Lithium-ion batteries – 2019; CRISPR – 2020; quantum dots – 2023."),
    ("The Nobel Prize in Economic Sciences 2025 was shared by Joel Mokyr, Philippe Aghion and Peter Howitt for explaining:",
     ["Innovation-driven economic growth", "The role of institutions in prosperity", "Poverty alleviation through experiments", "Behavioural economics"], 0,
     "Aghion and Howitt – 'creative destruction' model. Institutions and prosperity – Acemoglu, Johnson, Robinson (2024); experiments on poverty – Banerjee, Duflo, Kremer (2019)."),
    ("Which statement about the Nobel Prizes is NOT correct?",
     ["All Nobel Prizes are presented in Stockholm", "They were first awarded in 1901", "The Economics prize was added in 1968 by Sweden's central bank",
      "They are presented on 10 December, Alfred Nobel's death anniversary"], 0,
     PYQ + "The Peace Prize is presented in Oslo (Norway); the others in Stockholm. The first Economics prize was awarded in 1969."),
    ("Match the Indian Nobel laureates with the year:\na. Rabindranath Tagore  b. C. V. Raman  c. Amartya Sen  d. Kailash Satyarthi\n1. 1913  2. 1930  3. 1998  4. 2014",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-1, b-2, c-4, d-3"], 0,
     PYQ + "Mother Teresa – Peace 1979; Abhijit Banerjee – Economics 2019; Kailash Satyarthi shared 2014 Peace with Malala Yousafzai."),
    ("The Ramon Magsaysay Award, often called 'Asia's Nobel Prize', is presented in:",
     ["The Philippines", "Japan", "Singapore", "Thailand"], 0,
     PYQ + "Named after a Philippine president; first given in 1958. Indian recipients include Vinoba Bhave (first Indian, 1958), Mother Teresa and Arvind Kejriwal."),
    ("Match the award with its field:\na. Pulitzer Prize  b. Abel Prize  c. Turing Award  d. Grammy Award\n1. Journalism and literature  2. Mathematics  3. Computer science  4. Music",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0,
     PYQ + "The Turing Award (ACM) is called the 'Nobel of computing'; the Fields Medal is for mathematicians under 40, every four years."),
    ("Which Bengaluru-based musician has won three Grammy Awards?",
     ["Ricky Kej", "A. R. Rahman", "Zakir Hussain", "Raghu Dixit"], 0,
     "Ricky Kej won in 2015 ('Winds of Samsara') and twice for 'Divine Tides' (2022, 2023). Zakir Hussain won three Grammys at the 2024 ceremony."),
    ("At the 95th Academy Awards (2023), which Indian works won Oscars?",
     ["'Naatu Naatu' (RRR) – Best Original Song, and 'The Elephant Whisperers' – Best Documentary Short", "'RRR' – Best Picture",
      "'All That Breathes' – Best Documentary Feature", "'Lagaan' – Best Foreign Language Film"], 0,
     "'The Elephant Whisperers' was shot in Mudumalai (Tamil Nadu). 'Lagaan' (2002) was only nominated."),
    ("The 'Green Nobel' and the 'Green Oscar' are the popular names of which awards respectively?",
     ["Goldman Environmental Prize and Whitley Award", "Right Livelihood Award and Goldman Prize", "Whitley Award and Champions of the Earth",
      "Champions of the Earth and Right Livelihood Award"], 0,
     "The Right Livelihood Award is called the 'Alternative Nobel'; Champions of the Earth is the UN Environment Programme's award."),
    ("The Karnataka Ratna, the state's highest civilian honour, was first given in 1992 to:",
     ["Kuvempu and Dr. Rajkumar", "S. Nijalingappa and C. N. R. Rao", "Bhimsen Joshi and Shivakumara Swamiji", "Puneeth Rajkumar and D. Veerendra Heggade"], 0,
     PYQ + "Puneeth Rajkumar received it posthumously in 2021. Like the Bharat Ratna, it is not given every year."),
    ("The Pampa Award, the Karnataka government's highest award for Kannada literature, was instituted in 1987. Its first recipient was:",
     ["Kuvempu", "D. R. Bendre", "Shivaram Karanth", "Masti Venkatesha Iyengar"], 0,
     PYQ + "Named after Adikavi Pampa, author of 'Vikramarjuna Vijaya'. Bendre had died in 1981, before the award began."),
    ("Karnataka Rajyotsava Awards are presented every year on:",
     ["1 November", "26 January", "15 August", "2 October"], 0,
     PYQ + "1 November 1956 – formation of Mysore State; renamed Karnataka on 1 November 1973. The awards cover literature, arts, sports, social service and more."),
    ("'Nadoja', an honorary title, is conferred by which institution?",
     ["Kannada University, Hampi", "University of Mysore", "Karnataka Sahitya Academy", "Kannada Sahitya Parishat"], 0,
     "Nadoja means 'teacher of the land'. Kannada University was established in 1991 at Hampi (Vidyaranya)."),
    ("The Basava Puraskara instituted by the Karnataka government honours contributions to:",
     ["Social reform and equality", "Classical music", "Sports", "Scientific research"], 0,
     "Named after the 12th-century reformer Basavanna; Karnataka declared him 'Cultural Leader of Karnataka' in 2024."),
    ("Consider the statements:\nI. The Kuvempu Rashtriya Puraskar is given to writers in any Indian language.\nII. The Fields Medal is awarded every year.\nWhich is/are correct?",
     I_II, 0, "Only I. The Kuvempu award (Rashtrakavi Kuvempu Trust, from 2013) is national; the Fields Medal is given every four years at the International Congress of Mathematicians."),
    ("Assertion (A): Banu Mushtaq's 'Heart Lamp' was not eligible for the Booker Prize itself.\nReason (R): The International Booker Prize is for fiction translated into English, "
     "while the Booker Prize is for novels written in English.",
     AR, 0, "Heart Lamp was translated from Kannada, so it competed for the International Booker. R explains A."),
]

TOPICS = {
    "Awards, Honours and Prizes": [
        ("1 · Indian National Awards – Civilian, Gallantry, Literary, Film and Sports", INDIAN_AWARDS),
        ("2 · International Awards and Karnataka State Awards", WORLD_KARNATAKA_AWARDS),
    ],
}

NOTES = {
    "Awards, Honours and Prizes": [
        {"title": "Awards, honours and prizes – revision sheet", "md": """## 1. Civilian awards of India
- **Bharat Ratna** and **Padma** awards – instituted 2 January 1954; order: Bharat Ratna > Padma Vibhushan > Padma Bhushan > Padma Shri
- Bharat Ratna: first (1954) – C. Rajagopalachari, S. Radhakrishnan, C. V. Raman; first posthumous – Lal Bahadur Shastri (1966); first woman – Indira Gandhi (1971)
- Foreigners – Khan Abdul Ghaffar Khan (1987), Nelson Mandela (1990); only sportsperson – Sachin Tendulkar (2014)
- Karnataka – M. Visvesvaraya (1955), Bhimsen Joshi (2009), C. N. R. Rao (2014)
- **2024 (five)** – Karpoori Thakur, L. K. Advani, P. V. Narasimha Rao, Charan Singh, M. S. Swaminathan
- Padma awards announced on Republic Day eve; conferred by the President

## 2. Gallantry
| Wartime | Peacetime |
|---|---|
| Param Vir Chakra | Ashoka Chakra |
| Maha Vir Chakra | Kirti Chakra |
| Vir Chakra | Shaurya Chakra |
- First Param Vir Chakra – Major Somnath Sharma (1947)

## 3. Literature
| Award | Key facts |
|---|---|
| Jnanpith | Set up 1961; first 1965 – G. Sankara Kurup (Malayalam); Hindi most, **Kannada 8** |
| Kannada Jnanpith | Kuvempu 1967, Bendre 1973, Karanth 1977, Masti 1983, Gokak 1990, Ananthamurthy 1994, Karnad 1998, Kambar 2010 |
| Recent Jnanpith | 58th (2023) Gulzar, Rambhadracharya; 59th (2024) Vinod Kumar Shukla |
| Sahitya Akademi | 1954; 24 languages (22 + English, Rajasthani) |
| Saraswati Samman | K. K. Birla Foundation, 1991 |
| Booker 2025 | David Szalay – 'Flesh' (Kiran Desai shortlisted); 2024 – Samantha Harvey 'Orbital' |
| International Booker 2025 | **Banu Mushtaq – 'Heart Lamp'** (Kannada; translator Deepa Bhasthi); 2022 – Geetanjali Shree 'Tomb of Sand' |

## 4. Cinema, sport, science
- **Dadasaheb Phalke** – 1969, first Devika Rani; Dr. Rajkumar 1995; Mohanlal (for 2023)
- Khel Ratna → **Major Dhyan Chand Khel Ratna** (2021); Arjuna 1961 – players; Dronacharya 1985 – coaches
- **Rashtriya Vigyan Puraskar** (from 2024): Vigyan Ratna, Vigyan Shri, Vigyan Yuva–Shanti Swarup Bhatnagar, Vigyan Team; 13 domains; announced 11 May, presented 23 August
- Gandhi Peace Prize – 1995, ₹1 crore; National Teachers' Award – 5 September
- Oscars 2023 – 'Naatu Naatu' (RRR), 'The Elephant Whisperers'

## 5. International
- **Nobel** – first 1901; Economics from 1969; 10 December; Peace in **Oslo**, rest in Stockholm
- Indians: Tagore 1913, Raman 1930, Mother Teresa 1979, Amartya Sen 1998, Satyarthi 2014, Abhijit Banerjee 2019
- **Nobel 2025**: Peace – María Corina Machado; Literature – László Krasznahorkai; Chemistry – Kitagawa, Robson, Yaghi (MOFs); Physics – Clarke, Devoret, Martinis (quantum tunnelling in circuits); Medicine – Brunkow, Ramsdell, Sakaguchi (regulatory T cells); Economics – Mokyr, Aghion, Howitt (innovation-led growth)
| Award | Field / nickname |
|---|---|
| Ramon Magsaysay | 'Asia's Nobel', Philippines |
| Pulitzer | Journalism, USA |
| Abel / Fields | Mathematics (Fields – under 40, every 4 years) |
| Turing | Computing (ACM) |
| Grammy | Music – Ricky Kej 3 |
| Goldman / Whitley | 'Green Nobel' / 'Green Oscar' |
| Right Livelihood | 'Alternative Nobel' |

## 6. Karnataka
- **Karnataka Ratna** – 1992, first Kuvempu and Dr. Rajkumar; Puneeth Rajkumar 2021 (posthumous)
- **Pampa Award** – 1987, first Kuvempu; Rajyotsava Awards – 1 November
- Nadoja – Kannada University, Hampi; Basava Puraskara – social reform; Kuvempu Rashtriya Puraskar – national literary award

## ⚠ Traps
- Booker ≠ International Booker; Kumari Kamala – Padma **Bhushan** 1970
- Vigyan Puraskar ceremony 23 August, not 28 February
- One Nation, One Election committee – Ram Nath Kovind (not Subhash Kashyap)
"""}],
}
