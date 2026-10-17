"""Paper 1 · Current Affairs · planner topic P1-GK-17 Current State and National Affairs – a Karnataka set (30) and a National set
(10), the owner's 75% Karnataka / 25% national rule – with detailed notes (NOTES). P1-GK-17 is a General Knowledge row of the planner
that the structure pack leaves out (current affairs), so it lives in this subject with its plan ID.
Sources: Government of Karnataka budget speeches and press releases, DIPR, KDEM, PIB, Election Commission, Supreme Court and RBI
releases. REAL previous-year questions come from the KEA 2025–26 GK papers and UPSC-coaching entrance tests (no published key that
matches; answers worked out by ExamSim and marked so). Office-holders are 'as of mid-2026'; check for changes before the exam."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC current affairs). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

KARNATAKA = [
    ("Expand KTCP.",
     ["Karnataka Transparency and Controlled Plan", "Karnataka Town and Country Planning", "Karnataka Town Controlling Plan", "Karnataka Transport Control Plan"], 1,
     "The Karnataka Town and Country Planning Act, 1961 governs master plans and land use in towns." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q77"),
    ("Who is the current Chairperson (as in January 2026) of Karnataka's Vision Group Information Technology (VGIT)?",
     ["Nandan Nilekani", "Narayana Murthy", "Sudha Murthy", "S. Gopalakrishnan (Kris)"], 3,
     "Infosys co-founder Kris Gopalakrishnan heads the state's Vision Group on IT." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q91"),
    ("India's first dedicated 'Quantum City' will be established at",
     ["Hesaraghatta, Bengaluru", "Cyberabad, Hyderabad", "Guindy, Chennai", "Sector 62, Noida"], 0,
     "Karnataka announced 'Q-City' near Hesaraghatta at the Quantum India Bengaluru summit (2025) under its quantum mission." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q99"),
    ("Expand KSTePS",
     ["Kannada Science and Technology Papers Society", "Karnataka State Technology Promotion Society", "Karnataka Science and Technology Promoters Society", "Karnataka Science and Technology Promotion Society."], 3,
     "KSTePS works under the Department of Science and Technology, Government of Karnataka." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q100"),
    ("What is B-SMILE?",
     ["It is a dedicated special-purpose vehicle (SPV) to execute big ticket infrastructure projects in Bengaluru.", "It is a programme launched by the Government of Karnataka to reduce infant mortality rate in Bengaluru.",
      "It is a programme launched by BBMP to improve oral hygiene among the residents of Bengaluru.", "It is a programme launched by Government of Karnataka to reduce iron deficiency among the pregnant women residing in Bengaluru."], 0,
     "Bengaluru Smart Infrastructure Limited (B-SMILE) is an SPV for projects such as tunnel roads and flyovers." + NOTE, "UPSC coaching entrance 2025 (19 Jul) · Q10"),
    ("Among the statements related to The Karnataka Platform-based Gig Workers (Social Security and Welfare) Bill, 2024, which statement is wrong?",
     ["It was introduced to protect the rights of platform-based Gig workers.", "It places obligations on aggregators in relation to social security, occupational health and safety.",
      "Every aggregator shall register with the Board within sixty days from date of commencement of this Act.", "Three years imprisonment is suggested as penalty for the aggregators if they violate any provisions of the Bill."], 3,
     "The law provides fines for aggregators, not three years' imprisonment; it also creates a welfare board and a welfare fee." + NOTE, "UPSC coaching entrance 2025 (19 Jul) · Q11"),
    ("The program implemented to develop basic literacy and statistical skills among 4th and 5th standard students in Karnataka is",
     ["'ODU' Karnataka", "'KALI' Karnataka", "'NALI' Karnataka", "'KELU' Karnataka"], 0,
     "Odu Karnataka is a remedial reading-and-arithmetic programme for classes 4–5; Nali-Kali is activity learning for classes 1–3." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q30"),
    ("Name the mission which has the objective to achieve distributed growth of Karnataka's digital economy outside Bengaluru and this mission is led by KDEM:",
     ["Beyond Bengaluru", "Besides Bengaluru", "Outside Bengaluru", "Along with Bengaluru"], 0,
     "KDEM (Karnataka Digital Economy Mission) develops clusters such as Mysuru, Mangaluru and Hubballi–Dharwad–Belagavi." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q88"),
    ("In Karnataka who is the Chief Patron of \"Yeshasvini Co-operative Members Health Care Trust\"?",
     ["Chief Minister", "Minister for Co-operation", "Minister for Family and Health Care", "Minister for Rural Development and Panchayat Raj"], 0,
     "The Chief Minister is the Chief Patron; the Co-operation Minister is the Patron of the Yeshasvini scheme for members of co-operatives." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q99"),
    ("Who is known as \"Encyclopedia of the Forest\" in Karnataka?",
     ["Saalumarada Timmakka", "Tulsi Gowda", "Dr. Shanti Tummala", "Bhagyamma"], 1,
     "Tulsi Gowda of the Halakki tribe (Uttara Kannada), Padma Shri 2020, knew every plant species of the forest; she died in December 2024." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q59"),
    ("Identify the programme implemented to promote ecofriendly and sustainable agricultural practices in Karnataka in 2026-27:",
     ["Vasudhamrutha", "Neeriddare Nale", "Millet Hub", "Phaladhare"], 0,
     "The 2026-27 Karnataka budget announced 'Vasudhamrutha' to improve soil organic content and eco-friendly farming." + NOTE, "UPSC coaching entrance 2026 (HK) · Q35"),
    ("Grama Panchayath Libraries in Karnataka renamed as",
     ["Pusthaka Kendra", "Arivu Kendra", "Vidhyarthi Kendra", "Niranthara Kendra"], 1,
     "Gram Panchayat libraries were upgraded as 'Arivu Kendras' (knowledge centres) with digital resources." + NOTE, "UPSC coaching entrance 2026 (HK) · Q22"),
    ("The five guarantee schemes of the Government of Karnataka (2023) are Shakti, Gruha Jyothi, Gruha Lakshmi, Anna Bhagya and:",
     ["Yuva Nidhi", "Ksheera Bhagya", "Vidyasiri", "Arogya Karnataka"], 0, PYQ + "Yuva Nidhi gives monthly support to unemployed graduates and diploma holders."),
    ("The 'Shakti' scheme of Karnataka provides:",
     ["Free travel for women in state-run (non-premium) buses", "Free electricity up to 200 units", "₹2,000 a month to the woman head of a family", "Free rice"], 0, "It started on 11 June 2023."),
    ("Under 'Gruha Jyothi', households get:",
     ["Free electricity up to 200 units a month", "Free LPG cylinders", "Free bus passes", "Free mobile phones"], 0, PYQ + "Gruha Lakshmi gives ₹2,000 a month to the woman head."),
    ("The Greater Bengaluru Governance Act led to the BBMP being replaced in 2025 by the:",
     ["Greater Bengaluru Authority (GBA) with five city corporations", "Bengaluru Development Authority only", "BMRCL", "Bengaluru Rural Zilla Panchayat"], 0, "The five corporations were notified in September 2025."),
    ("Ramanagara district was renamed in 2025 as:",
     ["Bengaluru South", "Kempegowda Nagar", "Magadi", "Bengaluru Rural"], 0, PYQ + "Its headquarters remains Ramanagara town."),
    ("Who inaugurated the Mysuru Dasara in 2025?",
     ["Banu Mushtaq", "Sudha Murty", "S. L. Bhyrappa", "Hamsalekha"], 0, "She won the International Booker Prize 2025 for 'Heart Lamp'."),
    ("Banu Mushtaq's 'Heart Lamp', winner of the International Booker Prize 2025, was translated from Kannada by:",
     ["Deepa Bhasthi", "Geetanjali Shree", "Daisy Rockwell", "Vivek Shanbhag"], 0, PYQ + "It is the first Kannada book to win the prize."),
    ("Royal Challengers Bengaluru (RCB) won their first IPL title in:",
     ["2025", "2016", "2009", "2023"], 0, "A stampede near Chinnaswamy Stadium during the celebrations on 4 June 2025 killed 11 people."),
    ("The Karnataka State Commission for Backward Classes conducted a fresh socio-educational (caste) survey in:",
     ["September–October 2025", "2011", "2001", "2019"], 0, PYQ + "The earlier Kantharaj report survey was done in 2015."),
    ("Internal reservation among Scheduled Castes in Karnataka was studied by the commission headed by:",
     ["Justice H. N. Nagamohan Das", "Justice A. J. Sadashiva", "Justice Santosh Hegde", "Justice John Michael D'Cunha"], 0, "The Sadashiva commission had studied it earlier (2012)."),
    ("D. K. Shivakumar was sworn in as Chief Minister of Karnataka in June 2026 after the resignation of:",
     ["Siddaramaiah", "B. S. Yediyurappa", "Basavaraj Bommai", "H. D. Kumaraswamy"], 0,
     PYQ + "Siddaramaiah resigned in May 2026; Shivakumar took the oath on 3 June 2026 with G. Parameshwara as Deputy CM."),
    ("The Governor of Karnataka since July 2021 is:",
     ["Thaawarchand Gehlot", "Vajubhai Vala", "H. R. Bhardwaj", "Arif Mohammad Khan"], 0, "He administered the oath to Chief Minister D. K. Shivakumar on 3 June 2026."),
    ("Namma Metro's Yellow Line (R. V. Road – Bommasandra), opened in August 2025, serves mainly:",
     ["Electronic City", "Whitefield", "Kengeri", "Yelahanka"], 0, PYQ + "The Purple and Green lines were the first two."),
    ("'Invest Karnataka 2025', the global investors' meet, was held in Bengaluru in:",
     ["February 2025", "November 2022", "June 2024", "January 2026"], 0, "Investment intentions of over ₹10 lakh crore were announced."),
    ("The Karnataka Global Capability Centres (GCC) Policy 2024–29 aims to attract:",
     ["500 new GCCs", "50 new GCCs", "5,000 new GCCs", "No new GCCs"], 0, PYQ + "It also aims at about 3.5 lakh jobs."),
    ("Consider the statements:\nI. Kalyana Karnataka Utsava is celebrated on 17 September.\nII. The Kalyana Karnataka region includes Bagalkote and Vijayapura.",
     I_II, 0, "Kalyana Karnataka = Bidar, Kalaburagi, Yadgir, Raichur, Koppal, Ballari and Vijayanagara."),
    ("Assertion (A): Karnataka's guarantee schemes increased the state's welfare spending.\nReason (R): Schemes like Gruha Lakshmi and Anna Bhagya involve direct transfers to households.",
     AR, 0, "They account for a large share of the state budget."),
    ("Match the scheme with its benefit:\na. Shakti  b. Gruha Jyothi  c. Gruha Lakshmi  d. Yuva Nidhi\n1. Free bus travel for women  2. Free electricity  3. ₹2,000 a month to woman head  4. Unemployment allowance",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Guarantee schemes are frequently asked."),
]

NATIONAL = [
    ("Find the correct pair from the following:\nList-I (Commissions) – List-II (Current Chairpersons as in December 2025)\n(a) NITI Aayog – Narendra Modi\n(b) Election Commission of India – Gyanesh Kumar\n(c) National Human Rights Commission – Dr. V. Anantha Nageswaran\n(d) Karnataka State Human Rights Commission – Justice Dr. S. R. Nayak\nCodes:",
     ["(a), (c) and (d)", "(a) and (b)", "(a), (b) and (c)", "(b), (c) and (d)"], 1,
     "The PM chairs NITI Aayog and Gyanesh Kumar is CEC; Dr Anantha Nageswaran is the Chief Economic Adviser, not NHRC chair (Justice V. Ramasubramanian). Only option 2 leaves out (c)." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q92"),
    ("World's first CNG terminal is located in",
     ["Karnataka", "Uttar Pradesh", "Rajasthan", "Gujarat"], 3,
     "The world's first CNG port terminal is being built at Bhavnagar port, Gujarat." + NOTE, "UPSC coaching entrance 2026 (HK) · Q51"),
    ("Who was elected Vice-President of India in September 2025?",
     ["C. P. Radhakrishnan", "Jagdeep Dhankhar", "M. Venkaiah Naidu", "Om Birla"], 0, PYQ + "Jagdeep Dhankhar resigned in July 2025."),
    ("Justice Surya Kant became the Chief Justice of India in November 2025, succeeding:",
     ["Justice B. R. Gavai", "Justice D. Y. Chandrachud", "Justice Sanjiv Khanna", "Justice U. U. Lalit"], 0, "Justice Gavai was the first Buddhist CJI."),
    ("Under 'GST 2.0' (from 22 September 2025), most goods fall into two main GST slabs of:",
     ["5% and 18%", "12% and 28%", "0% and 40%", "10% and 20%"], 0, PYQ + "A 40% rate applies to some luxury and sin goods."),
    ("India's four Labour Codes came into force on:",
     ["21 November 2025", "1 April 2020", "15 August 2023", "26 January 2024"], 0, "They replaced 29 central labour laws."),
    ("Group Captain Shubhanshu Shukla became the first Indian to visit the International Space Station in 2025 aboard the:",
     ["Axiom-4 mission", "Gaganyaan-1", "Soyuz T-11", "Artemis II"], 0, PYQ + "Rakesh Sharma flew on Soyuz T-11 in 1984."),
    ("The next Census of India, with caste enumeration, has its reference date as:",
     ["1 March 2027", "1 March 2021", "1 January 2026", "1 October 2030"], 0, "Snow-bound areas have an earlier reference date of 1 October 2026."),
    ("The Indian women's team won its first ICC Women's ODI World Cup in November 2025 by defeating:",
     ["South Africa", "Australia", "England", "New Zealand"], 0, PYQ + "The final was played at Navi Mumbai."),
    ("The Governor of the Reserve Bank of India since December 2024 is:",
     ["Sanjay Malhotra", "Shaktikanta Das", "Urjit Patel", "Raghuram Rajan"], 0, "He was earlier the Revenue Secretary."),
]

TOPICS = {
    "Current State and National Affairs": [("1 · Karnataka", KARNATAKA), ("2 · National", NATIONAL)],
}

NOTES = {
    "Current State and National Affairs": [{"title": "Karnataka and national affairs – detailed notes (2023 – mid-2026)", "md": """# Current state and national affairs

> Office-holders change – check the latest before the exam.

## Karnataka – who's who
| Post | Name |
|---|---|
| Governor | **Thaawarchand Gehlot** (July 2021) |
| Chief Minister | **D. K. Shivakumar** (sworn in **3 June 2026**) – Deputy CM **G. Parameshwara** |
| Previous CM | **Siddaramaiah** (May 2023 – resigned May 2026; longest-serving CM, Jan 2026) |
| Council Chairman | Basavaraj Horatti |
| VGIT chair (Jan 2026) | **Kris Gopalakrishnan** |
U. T. Khader, Speaker 2023–26, became Health Minister in the Shivakumar ministry.

## Five guarantees (2023)
| Scheme | Benefit |
|---|---|
| **Shakti** (11 June 2023) | Free bus travel for women in state buses |
| **Gruha Jyothi** | Up to **200 units** free electricity |
| **Gruha Lakshmi** | **₹2,000/month** to woman head of family |
| **Anna Bhagya** | 10 kg grain (5 kg rice + cash) |
| **Yuva Nidhi** | ₹3,000 (graduates) / ₹1,500 (diploma) a month to the unemployed |

## Governance and places
- **Greater Bengaluru Authority** replaced BBMP (2025), with **five corporations**.
- **Ramanagara → Bengaluru South** district (2025). Karnataka has 31 districts (Vijayanagara the 31st, 2021).
- **Kalyana Karnataka** (renamed 2019): Bidar, Kalaburagi, Yadgir, Raichur, Koppal, Ballari, Vijayanagara; **Kalyana Karnataka Utsava – 17 Sept**; Article **371J** (2012).
- **Arivu Kendras** – upgraded Gram Panchayat libraries. **KTCP** – Karnataka Town and Country Planning Act (1961).
- Caste (socio-educational) survey – Sept–Oct 2025; SC internal reservation – **Justice H. N. Nagamohan Das** commission.
- **Gig Workers (Social Security and Welfare)** law – welfare board, welfare fee from aggregators, fines (no prison term).

## Economy, technology
- **Invest Karnataka 2025** (Feb 2025); **GCC Policy 2024–29** – 500 new GCCs, ~3.5 lakh jobs.
- **KDEM – 'Beyond Bengaluru'** clusters; **B-SMILE** – SPV for big Bengaluru infrastructure (tunnel road etc.).
- **Q-City (Quantum City)** – Hesaraghatta; Karnataka Quantum Mission. **KSTePS** – Karnataka Science and Technology Promotion Society.
- Namma Metro **Yellow Line** (R. V. Road – Bommasandra, Electronic City) – Aug 2025.
- Budget 2026-27: **Vasudhamrutha** (eco-friendly, soil-health farming).

## Education and health
- **Odu Karnataka** – reading & arithmetic, classes 4–5; **Nali-Kali** – classes 1–3.
- **Yeshasvini** co-operative health scheme – Chief Patron: **Chief Minister**.

## People, culture, sport
- **Banu Mushtaq** – International Booker 2025, 'Heart Lamp' (tr. **Deepa Bhasthi**); inaugurated **Mysuru Dasara 2025**.
- **Tulsi Gowda** – 'Encyclopedia of the Forest' (Halakki tribe; d. Dec 2024). Saalumarada Thimmakka – tree planter.
- **RCB** – first IPL title, **3 June 2025**; Chinnaswamy stampede 4 June 2025 (Justice D'Cunha inquiry).
- Karnataka Ratna latest: **Puneeth Rajkumar** (posthumous).

## National
| Post / event | Fact |
|---|---|
| President | **Droupadi Murmu** (2022) |
| Vice-President | **C. P. Radhakrishnan** (Sept 2025, after Dhankhar resigned) |
| CJI | **Surya Kant** (24 Nov 2025) after B. R. Gavai |
| CEC | **Gyanesh Kumar** (Feb 2025) |
| RBI Governor | **Sanjay Malhotra** (Dec 2024) |
| CEA | V. Anantha Nageswaran |
| NHRC | Justice V. Ramasubramanian |
| GST 2.0 | 5% and 18% (+40%), from **22 Sept 2025** |
| Labour Codes | In force **21 Nov 2025** (4 codes replace 29 laws) |
| Census | Reference date **1 March 2027**, with caste enumeration |
| Space | **Shubhanshu Shukla** – Axiom-4, ISS (June–July 2025) |
| Cricket | Champions Trophy 2025 (men); **Women's ODI World Cup 2025** (beat South Africa) |
| Ports | World's first **CNG terminal** – Bhavnagar, **Gujarat** |
"""}],
}
