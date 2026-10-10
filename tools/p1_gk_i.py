"""Paper 1 · General Knowledge · P1-GK-13 Indian Economics – Major Industries, Projects, Public Undertakings (2 × 20) and
P1-GK-15 Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary (3 × 20), with detailed revision NOTES.
Shared by GPSTR and KRIES (KRIES Paper 1 items D and G – Constitution and public administration), so they stay in English
like the other GK topics. References: M. Laxmikanth – Indian Polity, NCERT Indian Constitution at Work (class 11), NCERT
Indian Economic Development, Ramesh Singh – Indian Economy, KTBS Social Science. REAL previous-year questions come from the
KEA 2025–26 general-knowledge papers (KEA has no published key – answers worked out by ExamSim) and GTTC 2024 GK (official
KEA final key). Skipped as ambiguous: KEA 2026 GK-2 (NHK) Q3, Q8, Q13, Q14; GK-2 (HK) Q47; GK-3 (NHK) Q47."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

INDUSTRIES = [
    ("India's first successful modern cotton textile mill was set up in 1854 at:",
     ["Bombay (by C.N. Davar)", "Ahmedabad", "Kolkata", "Kanpur"], 0, PYQ + "Ahmedabad is called the 'Manchester of India'; Coimbatore the 'Manchester of South India'."),
    ("India's first jute mill was set up in 1855 at:",
     ["Rishra, near Kolkata (Hooghly basin)", "Kanpur", "Surat", "Dhaka"], 0, "The jute industry is concentrated along the Hooghly in West Bengal."),
    ("The Tata Iron and Steel Company (TISCO) was established in 1907 at:",
     ["Jamshedpur", "Bhilai", "Bhadravati", "Durgapur"], 0, PYQ + "Founded by Jamsetji Tata's vision (Dorabji Tata); steel production began in 1912."),
    ("Match the public-sector steel plants with the countries that helped set them up:\na. Bhilai  b. Rourkela  c. Durgapur  d. Bokaro\n"
     "1. Soviet Union  2. West Germany  3. United Kingdom  4. Soviet Union (later plan)",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-3, b-2, c-1, d-4", "a-1, b-3, c-2, d-4"], 0,
     PYQ + "Bhilai (Chhattisgarh) and Bokaro (Jharkhand) – USSR; Rourkela (Odisha) – West Germany; Durgapur (West Bengal) – Britain."),
    ("The Visvesvaraya Iron and Steel plant (Mysore Iron Works), started in 1923, is located at:",
     ["Bhadravati", "Toranagallu", "Hosapete", "Kudremukh"], 0, "Started by the Mysore State under Dewan M. Visvesvaraya; it used charcoal from Malnad forests."),
    ("The Industrial Policy Resolution of 1956 is known for:",
     ["Dividing industries into three schedules (A, B, C) with the public sector in the lead", "Abolishing industrial licensing",
      "Introducing GST", "Creating NITI Aayog"], 0, PYQ + "Schedule A – exclusively State; B – State to increase its role; C – private sector. It reflected the Mahalanobis (2nd Plan) strategy."),
    ("The New Industrial Policy of 1991 is associated with:",
     ["Liberalisation, privatisation and globalisation (de-licensing of most industries)", "Nationalisation of banks", "The Green Revolution",
      "The Bombay Plan"], 0, "Introduced by the Narasimha Rao government (Finance Minister Manmohan Singh) during the 1991 balance-of-payments crisis."),
    ("The 'Make in India' initiative was launched in:",
     ["September 2014", "August 2015", "January 2016", "May 2020"], 0, PYQ + "Its lion logo is made of gears; the 2020 Production Linked Incentive (PLI) schemes followed."),
    ("India's first oil refinery was set up in 1901 at:",
     ["Digboi (Assam)", "Barauni (Bihar)", "Koyali (Gujarat)", "Mangaluru (Karnataka)"], 0, "Digboi is one of the oldest operating refineries in the world."),
    ("The Sindri fertilizer plant (1951), one of independent India's first public-sector units, is in:",
     ["Jharkhand", "Kerala", "Punjab", "Odisha"], 0, PYQ + "FACT at Udyogamandal (Kerala) is the other early fertilizer company."),
    ("The Index of Industrial Production (IIP) in India is released by:",
     ["The National Statistics Office (MoSPI)", "The Reserve Bank of India", "NITI Aayog", "The Ministry of Commerce"], 0,
     "The current base year is 2011-12; the eight core industries carry about 40% of the IIP weight."),
    ("Among the eight core industries, the largest weight is carried by:",
     ["Refinery products", "Coal", "Cement", "Fertilizers"], 0,
     PYQ + "Core industries: coal, crude oil, natural gas, refinery products, fertilizers, steel, cement, electricity; refinery products ≈ 28%."),
    ("The Micro, Small and Medium Enterprises Development (MSMED) Act was passed in:",
     ["2006", "1991", "2014", "1999"], 0, "MSMEs are classified by investment and turnover (revised in 2020 and again in 2025)."),
    ("The Delhi–Mumbai Industrial Corridor (DMIC) is being developed with financial and technical support from:",
     ["Japan", "Russia", "France", "Germany"], 0, PYQ + "Projects are coordinated by NICDC (National Industrial Corridor Development Corporation)."),
    ("Which node of the Chennai–Bengaluru Industrial Corridor is in Karnataka?",
     ["Tumakuru", "Hubballi", "Kalaburagi", "Mangaluru"], 0, "Tumakuru also has the HAL helicopter factory (Bidarehalla Kaval) and a Japanese industrial township proposal."),
    ("Assertion (A): Most of India's integrated iron and steel plants are located in or near the Chota Nagpur plateau.\n"
     "Reason (R): The region has rich deposits of iron ore and coal.", AR, 0, "Raw-material location explains the cluster (Jamshedpur, Bokaro, Durgapur, Rourkela)."),
    ("Consider the statements:\nI. India's jute industry is concentrated in the Hooghly basin of West Bengal.\nII. India is the largest producer of raw jute in the world.",
     I_II, 2, PYQ + "Both are correct; Bangladesh is the other major jute producer."),
    ("Match the industrial centres with their products:\na. Chittaranjan  b. Perambur  c. Yelahanka (Bengaluru)  d. Sindri\n"
     "1. Electric locomotives  2. Railway coaches (ICF)  3. Rail wheels and axles  4. Fertilizers",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4"], 0, "Rail Wheel Factory, Yelahanka was set up in 1984."),
    ("Which industry is known as the 'sunrise industry' that made Bengaluru the 'Silicon Valley of India'?",
     ["Information technology and software services", "Cotton textiles", "Sugar", "Jute"], 0, "Karnataka was the first state to announce an IT policy (1997)."),
    ("The 'Bombay Plan' of 1944 for India's economic development was prepared by:",
     ["Leading Indian industrialists such as J.R.D. Tata and G.D. Birla", "The Planning Commission", "M.N. Roy", "The British Government"], 0,
     PYQ + "M.N. Roy wrote the 'People's Plan' (1945); the Planning Commission was set up in 1950."),
]

PROJECTS_PSU = [
    ("Which of the below are correctly matched?\nOrganisation – Year of establishment\n(a) Export-Import Bank of India – 1983\n"
     "(b) Small Industries Development Bank of India (SIDBI) – 1991\n(c) Securities and Exchange Board of India (SEBI) – 1992\n"
     "(d) Industrial Finance Corporation of India (IFCI) – 1948\nSelect the correct answer using the codes given below",
     ["a, b and c only", "b and d only", "a, c and d only", "c and d only"], 3,
     "EXIM Bank – 1982; SIDBI – 1990; SEBI – statutory body in 1992 (set up in 1988); IFCI – 1948, India's first development finance institution." + KEY,
     "GTTC 2024 Asst Gr-II GK · Q63"),
    ("To be granted 'Maharatna' status, a CPSE must have (among other conditions) an average annual net profit over three years of more than:",
     ["₹5,000 crore", "₹500 crore", "₹1,000 crore", "₹50,000 crore"], 0,
     PYQ + "Other conditions: Navratna status, listed on a stock exchange, average turnover above ₹25,000 crore and net worth above ₹15,000 crore."),
    ("Which company became India's 14th Maharatna in October 2024?",
     ["Hindustan Aeronautics Limited (HAL)", "Bharat Electronics Limited (BEL)", "BEML Limited", "Mazagon Dock Shipbuilders"], 0,
     "HAL is headquartered in Bengaluru; other Maharatnas include ONGC, NTPC, SAIL, BHEL, IOC, Coal India and GAIL."),
    ("The 'Navratna' scheme for profit-making public sector enterprises was introduced in:",
     ["1997", "1991", "2009", "1985"], 0, PYQ + "Maharatna came in 2009/10; Miniratna (Category I and II) also exists."),
    ("The Bhakra Nangal project is built on the river:",
     ["Sutlej", "Beas", "Ravi", "Chenab"], 0, "Its reservoir is the Gobind Sagar; Nehru called such dams 'the temples of modern India'."),
    ("The Hirakud dam, one of the longest earthen dams in the world, is built across:",
     ["Mahanadi (Odisha)", "Godavari", "Damodar", "Narmada"], 0, PYQ + "Built in 1957 near Sambalpur."),
    ("The Damodar Valley Corporation (1948), India's first multipurpose river valley project, was modelled on:",
     ["The Tennessee Valley Authority of the USA", "The Aswan project of Egypt", "The Three Gorges project of China", "The Hoover dam"], 0,
     "The Damodar was called the 'Sorrow of Bengal' because of its floods."),
    ("Match the projects with their rivers:\na. Sardar Sarovar  b. Tehri  c. Nagarjuna Sagar  d. Tungabhadra dam\n1. Narmada  2. Bhagirathi  3. Krishna  4. Tungabhadra",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4"], 0,
     PYQ + "Tungabhadra dam is at Hosapete (Vijayanagara district), a joint project with Andhra Pradesh."),
    ("Which public sector undertaking is NOT headquartered in Bengaluru?",
     ["NMDC Limited", "Bharat Electronics Limited", "BEML Limited", "Hindustan Aeronautics Limited"], 0, "NMDC (iron-ore mining) is headquartered in Hyderabad."),
    ("The central government department that manages disinvestment of public sector undertakings is:",
     ["DIPAM (Department of Investment and Public Asset Management)", "DPIIT", "NITI Aayog", "SEBI"], 0, "The Department of Disinvestment was renamed DIPAM in 2016."),
    ("Air India was formally handed over to the Tata Group (through Talace Pvt. Ltd.) in:",
     ["January 2022", "March 2020", "August 2023", "October 2019"], 0, PYQ + "Tata had founded the airline as Tata Airlines in 1932."),
    ("NITI Aayog, which replaced the Planning Commission, came into existence on:",
     ["1 January 2015", "15 August 2014", "1 April 2017", "26 January 2015"], 0, "The Prime Minister is its chairperson."),
    ("Which Five-Year Plan, based on the Mahalanobis model, gave priority to heavy and basic industries?",
     ["Second Plan (1956–61)", "First Plan (1951–56)", "Fourth Plan", "Eighth Plan"], 0, PYQ + "The First Plan focused on agriculture (Harrod–Domar model)."),
    ("KIOCL Limited, a central PSU headquartered in Bengaluru, is mainly associated with:",
     ["Iron-ore pellets (pelletisation plant at Mangaluru)", "Aircraft", "Coal mining", "Fertilizers"], 0,
     "Its Kudremukh mines closed in 2006 after a Supreme Court order to protect the Western Ghats forests."),
    ("Mazagon Dock Shipbuilders Ltd., Mumbai, builds:",
     ["Warships and submarines", "Railway coaches", "Fighter aircraft", "Satellites"], 0, "It built the Scorpène (Kalvari class) submarines."),
    ("The Life Insurance Corporation of India (LIC) listed its shares through India's then-largest IPO in:",
     ["May 2022", "May 2019", "March 2021", "November 2023"], 0, "LIC was formed in 1956 by nationalising life insurance companies."),
    ("The Indira Gandhi Canal, which irrigates western Rajasthan, starts from the:",
     ["Harike barrage (confluence of the Sutlej and Beas, Punjab)", "Bhakra dam", "Sardar Sarovar dam", "Tehri dam"], 0,
     PYQ + "It is one of the longest irrigation canals in India and turned parts of the Thar desert green."),
    ("Assertion (A): Navratna status gives a PSU board more financial and operational autonomy.\nReason (R): Navratna companies are owned by state governments.",
     AR, 2, "R is false: Navratnas are central public sector enterprises (CPSEs)."),
    ("Consider the statements:\nI. The Hirakud dam is built on the Mahanadi in Odisha.\nII. The Almatti dam is built on the Kaveri.",
     I_II, 0, PYQ + "Almatti (Lal Bahadur Shastri Sagar) is on the Krishna in Vijayapura/Bagalkote; KRS is on the Kaveri."),
    ("Which Karnataka-based public sector company manufactures earth-moving equipment, metro coaches and defence vehicles?",
     ["BEML Limited", "BEL", "ITI Limited", "HMT"], 0, "BEML (1964) has plants at KGF, Mysuru and Bengaluru; HMT made watches and machine tools."),
]

RIGHTS = [
    ("Match the following:\nList-I (Rights)\n(a) Right to Constitutional Remedies\n(b) Right to Freedom of Religion\n(c) Right Against Exploitation\n(d) Right to Equality\n"
     "List-II (Articles)\n(i) Articles 25 - 28\n(ii) Article 32\n(iii) Articles 14 - 18\n(iv) Articles 23 - 24",
     ["a - iii, b - iv, c - i, d - ii", "a - iv, b - i, c - ii, d - iii", "a - ii, b - i, c - iv, d - iii", "a - i, b - ii, c - iv, d - iii"], 2,
     "Equality 14–18, Freedom 19–22, Exploitation 23–24, Religion 25–28, Cultural & educational 29–30, Remedies 32." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q64"),
    ("Which of the following Directive Principles of State Policy has been added by 42nd Amendment to the Constitution?",
     ["Organise village panchayats", "Organise animal husbandry", "To secure opportunities for healthy development of children", "To prohibit the slaughter of cows"], 2,
     "The 42nd Amendment (1976) added Art. 39(f) (healthy development of children), 39A (free legal aid), 43A (workers in management) and 48A "
     "(environment). Village panchayats (Art. 40) and Art. 48 were in the original Constitution." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q69"),
    ("Who has the power to prescribe qualifications to acquire Indian citizenship?",
     ["The President", "The Governor", "The State Legislature", "The Parliament"], 3,
     "Art. 11 empowers Parliament to regulate citizenship by law – the Citizenship Act, 1955." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q2"),
    ("Match the sources with the features that have been borrowed in the Indian Constitution:\nList I (Source)\na. Constitution of Ireland\nb. Constitution of Australia\n"
     "c. Constitution of France\nd. Constitution of South Africa\nList II (Borrowed feature)\ni. Concurrent List\n"
     "ii. Procedure for amending the Constitution and the procedure for electing members of the Rajya Sabha\niii. Directive Principles of State Policy\n"
     "iv. Liberty and Fraternity in the Preamble",
     ["a-ii, b-iii, c-i, d-iv", "a-iv, b-ii, c-iii, d-i", "a-iii, b-i, c-iv, d-ii", "a-i, b-iv, c-ii, d-iii"], 2,
     "Ireland – DPSP; Australia – Concurrent List; France – Republic, liberty, equality, fraternity; South Africa – amendment procedure, election of Rajya Sabha members." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q7"),
    ("Read the statements with regard to the Directive Principles of State Policy:\na. The Directive Principles of State Policy are incorporated in Part IV of the Constitution.\n"
     "b. The Directive Principles of State Policy are legally enforceable.\nc. The Directive Principles of State Policy are legally justiciable.\nIdentify the correct statement/s:",
     ["Only a", "b and c", "Only b", "a and b"], 0, "DPSPs (Arts 36–51, Part IV) are non-justiciable (Art. 37)." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q11"),
    ("Which of the following statements is not a characteristic of a federal system?",
     ["The Supremacy of the Constitution", "Rigid Constitution", "There is no decentralization of power", "Independent judiciary"], 2,
     "Federalism divides power between the Centre and states; India is 'a Union of States' with a unitary bias." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q63"),
    ("The words 'Socialist', 'Secular' and 'Integrity' were added to the Preamble by the:",
     ["42nd Amendment, 1976", "44th Amendment, 1978", "1st Amendment, 1951", "86th Amendment, 2002"], 0,
     PYQ + "The Preamble has been amended only once. The Kesavananda Bharati case (1973) held that it is part of the Constitution (Berubari, 1960, had said it was not)."),
    ("Free and compulsory education for children of 6–14 years became a Fundamental Right under:",
     ["Article 21A, inserted by the 86th Amendment (2002)", "Article 45, original Constitution", "Article 51A(k)", "Article 29"], 0,
     "The RTE Act came into force on 1 April 2010; Art. 45 now covers early childhood care for children below six."),
    ("Match the writs with their meaning:\na. Habeas corpus  b. Mandamus  c. Quo warranto  d. Certiorari\n"
     "1. 'To have the body' – against illegal detention  2. 'We command' – to perform a public duty  3. 'By what authority' – against usurping a public office  "
     "4. 'To be certified' – quashing an order of a lower court",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0,
     PYQ + "Prohibition stops a lower court from continuing a case. The Supreme Court issues writs under Art. 32, High Courts under Art. 226."),
    ("'Untouchability' is abolished and its practice forbidden in any form under:",
     ["Article 17", "Article 15", "Article 18", "Article 23"], 0, "Art. 18 abolishes titles; Art. 23 prohibits traffic in human beings and forced labour."),
    ("The Fundamental Duties (Article 51A) were added on the recommendation of the:",
     ["Swaran Singh Committee, by the 42nd Amendment", "Sarkaria Commission", "Balwant Rai Mehta Committee", "Kothari Commission"], 0,
     PYQ + "Ten duties were added in 1976; the 11th (parents to provide education to children 6–14) came with the 86th Amendment, 2002. Borrowed from the USSR."),
    ("The Right to Property was removed from the list of Fundamental Rights by the 44th Amendment (1978) and is now a constitutional right under:",
     ["Article 300A", "Article 31", "Article 19(1)(f)", "Article 265"], 0, "Art. 265 – no tax except by authority of law."),
    ("Which of the following Fundamental Rights are available ONLY to citizens of India?",
     ["Articles 15, 16, 19, 29 and 30", "Articles 14, 20, 21 and 22", "Articles 25 to 28", "Article 32 only"], 0,
     "Arts 14, 20, 21, 22 and 25–28 are available to foreigners too (except enemy aliens)."),
    ("Assertion (A): Directive Principles cannot be enforced by any court.\nReason (R): Article 37 says they are not enforceable by courts but are fundamental in the governance of the country.",
     AR, 0, "R is the exact reason given in the Constitution."),
    ("The Uniform Civil Code for citizens is mentioned in:",
     ["Article 44", "Article 40", "Article 48", "Article 39A"], 0, PYQ + "Goa already has a common civil code; Uttarakhand passed a UCC law in 2024."),
    ("Dr. B.R. Ambedkar called which Article 'the very soul of the Constitution and the very heart of it'?",
     ["Article 32", "Article 21", "Article 14", "Article 368"], 0, "Art. 32 – right to move the Supreme Court for enforcement of Fundamental Rights."),
    ("India's system of single citizenship was borrowed from the constitution of:",
     ["The United Kingdom", "The USA", "Canada", "Ireland"], 0, PYQ + "UK also gave parliamentary government, rule of law and the writs."),
    ("Article 19 originally guaranteed seven freedoms. How many does it guarantee now?",
     ["Six", "Seven", "Five", "Eight"], 0, "The freedom to acquire, hold and dispose of property (19(1)(f)) was deleted in 1978."),
    ("Which of the following is NOT a way of losing Indian citizenship under the Citizenship Act, 1955?",
     ["Failing to vote in two general elections", "Renunciation", "Termination (voluntarily acquiring another country's citizenship)", "Deprivation by the Government"], 0,
     "Citizenship is acquired by birth, descent, registration, naturalisation and incorporation of territory."),
    ("Assertion (A): The Right to Education is a Fundamental Right under Article 21A.\nReason (R): The 42nd Amendment moved 'education' from the State List to the Concurrent List.",
     AR, 1, "Both are true, but the shift to the Concurrent List (1976) is not why education became a Fundamental Right (86th Amendment, 2002)."),
]

LEGISLATURE = [
    ("Which of the following statements are CORRECT regarding the Governor?\n(a) Governor is an integral part of the state Legislature.\n"
     "(b) He/She nominates 1/6 of the members of state Legislative Council.\n(c) He/She nominates one member from Anglo-Indian community to the state Legislative Assembly.\n"
     "(d) He/She promulgates Ordinances when the state Legislature is not in session.",
     ["(a), (b) and (c) are correct", "(a), (b) and (d) are correct", "(a) and (b) are correct", "(c) and (d) are correct"], 1,
     "Anglo-Indian nomination to Lok Sabha and Assemblies ended with the 104th Amendment (2020); ordinances – Art. 213." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q50"),
    ("As per Article 330, how many seats can be reserved for SC and ST in the Lok Sabha?",
     ["84 and 47 respectively", "52 and 27 respectively", "72 and 37 respectively", "65 and 45 respectively"], 0,
     "After the 2008 delimitation, 84 Lok Sabha seats are reserved for SCs and 47 for STs." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q51"),
    ("Match the following List I with List II and choose the correct answer.\nList I (Speaker): (a) Shivaraj Patil (b) G.M.C. Balayogi (c) Meira Kumar (d) Om Birla\n"
     "List II (Lok Sabha): (i) Seventeenth Lok Sabha (ii) Fifteenth Lok Sabha (iii) Tenth Lok Sabha (iv) Twelfth Lok Sabha",
     ["a - iii, b - iv, c - i, d - ii", "a - iv, b - iii, c - ii, d - i", "a - iii, b - iv, c - ii, d - i", "a - ii, b - iii, c - iv, d - i"], 2,
     "Shivraj Patil – 10th; Balayogi – 12th; Meira Kumar (first woman Speaker) – 15th; Om Birla – 17th and 18th." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q52"),
    ("Consider the following statements and select the correct answer using the codes given below:\n(a) The President of India appoints the leader of the majority party in the Lok Sabha as the Prime Minister.\n"
     "(b) The Prime Minister is the Head of the country.\n(c) The Prime Minister is the Leader of the Lower House of the Parliament.\n(d) The Prime Minister is the Chief spokesperson of the Central Government.",
     ["(a), (b), (c) and (d) are correct", "(a), (c) and (d) are correct", "(a), (b) and (c) are correct", "(b), (c) and (d) are correct"], 1,
     "The President is the head of the State; the PM is the head of the government." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q44"),
    ("The correct statements about 'calling attention notice' are\n(a) It is a device of calling the attention of a Minister to a matter of urgent public importance.\n"
     "(b) Its main purpose is to seek an authoritative statement from the Minister.\n(c) It does not involve any censure against Government.\n"
     "(d) It is an Indian innovation in the parliamentary procedure since 1952.",
     ["(a), (b), (c) and (d)", "(a), (b) and (c)", "(b), (c) and (d)", "(c), (d) and (a)"], 1,
     "It is an Indian innovation, but in use since 1954, not 1952. Zero Hour is also an Indian innovation (1962)." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q45"),
    ("Which one of the following is the correct sequence of stage of Law Making in the Indian Parliament?",
     ["Report stage, Committee stage, First reading, Second reading, Third reading", "First reading, Second reading, Third reading, Committee stage, Report stage",
      "Committee stage, First reading, Second reading, Third reading, Report stage", "First reading, Second reading, Committee stage, Report stage, Third reading"], 3,
     "Introduction (first reading) → general discussion (second reading) → committee and report (consideration) stages → third reading (passing)." + NOTE,
     "KEA 2026 GK-3 (NHK, 10 May 2026) · Q46"),
    ("Which of the following statements are CORRECT regarding legislative council?\n(a) 1/3 are elected by the members of local bodies.\n(b) 1/12 are elected by graduates.\n"
     "(c) 1/3 are elected by the members of the legislative assembly of the state.\n(d) 1/6 are nominated by President.",
     ["(a), (b) and (c) are correct", "(b), (c) and (d) are correct", "(a) and (b) are correct", "(c) and (d) are correct"], 0,
     "1/3 local bodies, 1/3 MLAs, 1/12 graduates, 1/12 teachers, 1/6 nominated by the GOVERNOR (Art. 171)." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q49"),
    ("Which among the following countries have parliamentary system of government?\n(a) Britain\n(b) India\n(c) Brazil\n(d) Sri Lanka",
     ["(a) and (b) are correct", "(b) and (c) are correct", "(b) and (d) are correct", "(c) and (d) are correct"], 0,
     "Brazil has a presidential system and Sri Lanka an executive presidency." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q98"),
    ("The President of India is elected by an electoral college consisting of:",
     ["Elected members of both Houses of Parliament and elected members of state Legislative Assemblies (including Delhi and Puducherry)",
      "All members of both Houses of Parliament only", "Elected members of Lok Sabha and Legislative Councils",
      "All members of Parliament and all members of state legislatures including nominated members"], 0,
     PYQ + "Nominated members and members of Legislative Councils do not vote; the Vice-President is elected by ALL members of both Houses."),
    ("The President can be removed by impeachment (Article 61) only for:",
     ["Violation of the Constitution", "Proved misbehaviour or incapacity", "Losing a vote of confidence", "Corruption proved in court"], 0,
     "'Proved misbehaviour or incapacity' is the ground for removing Supreme Court and High Court judges."),
    ("The ex-officio Chairman of the Rajya Sabha is:",
     ["The Vice-President of India", "The Speaker of the Lok Sabha", "The President of India", "The Prime Minister"], 0,
     PYQ + "The Deputy Chairman is elected from among Rajya Sabha members."),
    ("Who certifies whether a Bill is a Money Bill (Article 110)?",
     ["The Speaker of the Lok Sabha", "The President", "The Finance Minister", "The Chairman of the Rajya Sabha"], 0,
     "The Rajya Sabha can only delay a Money Bill by 14 days; it can be introduced only in the Lok Sabha with the President's recommendation."),
    ("A joint sitting of both Houses of Parliament (Article 108) is presided over by the Speaker and CANNOT be held for:",
     ["A Money Bill or a Constitution Amendment Bill", "An ordinary Bill", "A Bill rejected by the Rajya Sabha", "A Bill pending for over six months"], 0,
     PYQ + "Joint sittings have been held only three times: Dowry Prohibition (1961), Banking Service Commission (1978) and POTA (2002)."),
    ("How many members are nominated to the Rajya Sabha by the President for their knowledge in literature, science, art and social service?",
     ["12", "2", "10", "14"], 0, "Art. 80; the maximum strength of Rajya Sabha is 250."),
    ("The minimum age to become a member of the Lok Sabha and of the Rajya Sabha respectively is:",
     ["25 and 30 years", "21 and 25 years", "30 and 35 years", "25 and 35 years"], 0, "The President and Vice-President must be at least 35."),
    ("Ordinances can be issued by the President under Article ____ and by the Governor under Article ____.",
     ["123; 213", "213; 123", "356; 365", "110; 199"], 0, PYQ + "An ordinance lapses six weeks after the legislature reassembles."),
    ("The size of the Council of Ministers (including the PM) cannot exceed 15% of the total strength of the Lok Sabha. This was introduced by the:",
     ["91st Amendment, 2003", "52nd Amendment, 1985", "61st Amendment, 1988", "74th Amendment, 1992"], 0, "For states, 15% of the Assembly but not fewer than 12 ministers."),
    ("The Karnataka Legislative Assembly and Legislative Council have respectively:",
     ["224 elected members and 75 members", "224 and 60 members", "250 and 75 members", "234 and 78 members"], 0,
     PYQ + "Karnataka is one of six states with a bicameral legislature; the Council is a permanent house."),
    ("The Governor of a state is appointed by the President and holds office:",
     ["During the pleasure of the President (Art. 156)", "For a fixed five-year term that cannot be cut short", "Until removed by the state Assembly", "For life"], 0,
     "Arts 153–155; the normal term is five years."),
    ("Assertion (A): The Lok Sabha can be dissolved by the President before its term ends.\nReason (R): The Speaker vacates office immediately on the dissolution of the Lok Sabha.",
     AR, 2, "R is false: the Speaker continues until just before the first meeting of the new Lok Sabha."),
]

JUDICIARY = [
    ("Read the statements with regard to High Court mentioned below:\n(a) The Chief Justice of a High Court can appoint officers and staff of the High Court without any interference from the executive.\n"
     "(b) The Judges of a High Court are appointed by the President.\n(c) The President can transfer a Judge from one High Court to another after consulting the Chief Justice of India.\n"
     "(d) A Judge of a High Court cannot be removed from his office.\nIdentify the correct statements",
     ["(a), (b) and (c)", "(a), (c) and (d)", "(b), (c) and (d)", "(a), (b) and (d)"], 0,
     "A High Court judge can be removed like a Supreme Court judge – by an address of Parliament on proved misbehaviour or incapacity (Arts 217, 218)." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q61"),
    ("Which of the following options regarding NHRC is correct?",
     ["Chairman should be a retired Chief Justice of Supreme Court of India or retired Chief Justice of a High Court",
      "Chairman is appointed by the President on the recommendation of Prime Minister and his Council of Ministers",
      "It can amend Constitution to safeguard human rights", "It promotes research on human rights"], 3,
     "Since 2019 the chairperson is a retired CJI or Supreme Court judge, appointed on a committee's recommendation (PM, Speaker, Home Minister, "
     "opposition leaders, Deputy Chairman of RS); NHRC is statutory (1993)." + NOTE, "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q66"),
    ("Which of the following is/are the constitutional bodies?\n(a) NITI Aayog\n(b) Finance Commission\n(c) GST Council\n(d) National Medical Commission",
     ["(a) and (d)", "(a) and (b)", "(b) only", "(b) and (c)"], 3,
     "Finance Commission – Art. 280; GST Council – Art. 279A (101st Amendment). NITI Aayog is an executive body; NMC is statutory (2019)." + NOTE,
     "KEA 2026 GK-1 (HK, 22 Feb 2026) · Q41"),
    ("Consider the following statements with reference to the Independence of State Public Service Commission\n(a) Chairpersons and members can only be removed by the President on specific grounds after a Supreme Court inquiry.\n"
     "(b) Their salaries, allowances and pensions are determined by the Governor but cannot be changed to their disadvantage during their term.\n"
     "(c) They are ineligible for other Government jobs, limiting potential pressure or inducement.\n(d) While appointed by the Governor, the removal process is insulated, emphasizing their independent role.\n"
     "How many of the above statements is/are correct?",
     ["All the four statements are correct", "Only three statements are correct", "Only two statements are correct", "Only one statement is correct"], 0,
     "Arts 316–319: appointed by the Governor, removed only by the President (misbehaviour after a Supreme Court inquiry); expenses charged on the Consolidated Fund." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q29"),
    ("Which of the following statements about Emergency Provisions exercised by the President of India is/are correct?\n(a) Under Article 352, the President can declare a National Emergency.\n"
     "(b) Under Article 365, the President can impose Presidential Rule on any state.\n(c) Under Article 356, the President can suspend the fundamental rights of citizens.\n"
     "(d) Article 359 empowers the President to proclaim a Financial Emergency.",
     ["(a) and (b) only", "(a) only", "(c) only", "(c) and (d) only"], 1,
     "352 – National Emergency; 356 – President's Rule; 359 – suspension of enforcement of Fundamental Rights; 360 – Financial Emergency." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q30"),
    ("Read the following statements regarding Tribunals in Indian Constitution.\n(a) Original constitution provides for the establishment of Tribunals.\n(b) Tribunals are mentioned in Part-XIV-A.\n"
     "(c) Articles 323A and 323B deal with Tribunals.\n(d) The Parliament passed the Administrative Tribunals Act in 1985.\nIdentify the correct statements.",
     ["(a), (b) and (c)", "(b), (c) and (d)", "(b) and (c) only", "(c) and (d) only"], 1,
     "Part XIV-A (Arts 323A, 323B) was added by the 42nd Amendment, 1976 (Swaran Singh Committee)." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q91"),
    ("Read the following statements regarding the National Commission for Scheduled Tribes (STs):\na. The Commission is a constitutional body.\n"
     "b. Article 338A provides for the establishment of the Commission.\nc. The separate National Commission for STs came into existence in 2004.\n"
     "d. The President of India is the Chairperson of the Commission.\nIdentify the correct statements:",
     ["a, c and d", "a, b and d", "a, b and c", "b, c and d"], 2,
     "Created by the 89th Amendment (2003), functioning from 2004; its chairperson is appointed by the President." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q6"),
    ("Consider the pairs and identify the 'incorrect' pair.\nList-I (High Court) – List-II (Seat/Bench)",
     ["Allahabad – Lucknow", "Karnataka – Dharwad & Kalburgi (Gulbarga)", "Madhya Pradesh – Gwalior and Indore", "Madras – Coimbatore"], 3,
     "The Madras High Court's bench is at Madurai." + NOTE, "KEA 2026 GK-2 (HK, 9 May 2026) · Q49"),
    ("Consider the following statements:\nStatement-I: Chief Information Commissioner should be a member of Parliament or member of legislature of any state.\n"
     "Statement-II: He should be a person of eminence in public life with wide knowledge and experience in Law, Science, Technology, Social Service, Management and Administration.",
     ["Statement-I is correct and statement-II is incorrect.", "Statement-II is correct and statement-I is incorrect.", "Both statement-I and statement-II are correct.",
      "Both statement-I and statement-II are incorrect."], 1,
     "Under the RTI Act, 2005 the CIC must NOT be an MP or MLA or hold any office of profit." + NOTE, "KEA 2026 GK-3 (NHK, 10 May 2026) · Q50"),
    ("Who appoints the Municipal Commissioner of the Municipal Corporation?",
     ["The President of India", "The Mayor", "The Governor", "The State Government"], 3,
     "The commissioner (usually an IAS officer) is the chief executive appointed by the state government; the Mayor is the elected head." + NOTE,
     "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q10"),
    ("At its inauguration in 1950 the Supreme Court had 8 judges (including the CJI). Its present sanctioned strength is:",
     ["34 (CJI + 33)", "31", "26", "30"], 0, PYQ + "Raised from 31 to 34 by the Supreme Court (Number of Judges) Amendment Act, 2019."),
    ("Which statement about writ jurisdiction is correct?",
     ["High Courts (Art. 226) can issue writs for Fundamental Rights and also for other legal rights", "Only the Supreme Court can issue writs",
      "The Supreme Court can issue writs for any legal right under Art. 32", "Writs are issued only by tribunals"], 0,
     "Art. 32 is limited to Fundamental Rights, so the High Courts' writ jurisdiction is wider."),
    ("The advisory jurisdiction of the Supreme Court, under which the President may seek its opinion, is in:",
     ["Article 143", "Article 131", "Article 137", "Article 129"], 0, PYQ + "131 – original jurisdiction (Centre–state disputes); 137 – review; 129 – court of record."),
    ("The 'collegium' system of appointing judges evolved from the:",
     ["Second Judges case (1993)", "Kesavananda Bharati case (1973)", "Minerva Mills case (1980)", "S.R. Bommai case (1994)"], 0,
     "The Third Judges case (1998) expanded it to the CJI and four senior-most judges; the NJAC (99th Amendment) was struck down in 2015."),
    ("The Comptroller and Auditor General of India (Art. 148) submits his audit reports on the Union's accounts to:",
     ["The President, who lays them before Parliament", "The Prime Minister", "The Finance Minister", "The Chief Justice"], 0,
     PYQ + "The Public Accounts Committee examines them; the CAG is called the 'guardian of the public purse'."),
    ("Which statement about the Election Commission of India is correct?",
     ["It became a multi-member body in 1993 and works under Article 324", "Its members are elected by Parliament",
      "It conducts panchayat elections in every state", "The CEC can be removed by the President at will"], 0,
     "Panchayat and municipal elections are run by State Election Commissions (Art. 243K); the CEC is removed like a Supreme Court judge."),
    ("The 16th Finance Commission, which made recommendations for 2026–31, was chaired by:",
     ["Arvind Panagariya", "N.K. Singh", "Y.V. Reddy", "Raghuram Rajan"], 0, PYQ + "N.K. Singh chaired the 15th; Finance Commissions are set up every five years under Art. 280."),
    ("Which of these is a statutory anti-corruption body in Karnataka?",
     ["Karnataka Lokayukta (Karnataka Lokayukta Act, 1984)", "Karnataka Public Service Commission", "State Election Commission", "Karnataka Legislative Council"], 0,
     "The Lokpal and Lokayuktas Act was passed in 2013; India's first Lokpal was Justice P.C. Ghose (2019)."),
    ("Under the Right to Information Act, 2005, information concerning the life or liberty of a person must be supplied within:",
     ["48 hours", "30 days", "7 days", "15 days"], 0, PYQ + "Ordinary requests: 30 days; first appeal to the departmental appellate authority, second to the Information Commission."),
    ("The Attorney General of India (Art. 76) and the Advocate General of a state (Art. 165) are appointed respectively by:",
     ["The President and the Governor", "The Chief Justice and the High Court", "Parliament and the state legislature", "The Prime Minister and the Chief Minister"], 0,
     "The Attorney General can speak in either House of Parliament but cannot vote."),
]

TOPICS = {
    "Indian Economics – Major Industries, Projects, Public Undertakings": [
        ("1 · Major Industries and Industrial Policy", INDUSTRIES),
        ("2 · River Valley Projects and Public Sector Undertakings", PROJECTS_PSU),
    ],
    "Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary": [
        ("1 · Preamble, Citizenship, Fundamental Rights, DPSP and Duties", RIGHTS),
        ("2 · Union and State Legislature and Executive", LEGISLATURE),
        ("3 · Judiciary, Constitutional Bodies and Public Administration", JUDICIARY),
    ],
}

NOTES = {
    "Indian Economics – Major Industries, Projects, Public Undertakings": [
        {"title": "Industries, projects and PSUs – revision notes", "md": """## 1. Firsts and locations
| Industry | First / main centre | Note |
|---|---|---|
| Cotton textile | Bombay 1854 (C.N. Davar) | Ahmedabad – Manchester of India; Coimbatore – of South India |
| Jute | Rishra 1855 (Hooghly) | India = largest raw-jute producer |
| Iron & steel | TISCO Jamshedpur 1907 | Mysore Iron Works, Bhadravati 1923 (Visvesvaraya) |
| Oil refinery | Digboi 1901 | |
| Fertilizer (PSU) | Sindri 1951 | FACT Kerala |

## 2. Steel plants and partners
| Plant | State | Partner |
|---|---|---|
| Bhilai | Chhattisgarh | USSR |
| Rourkela | Odisha | West Germany |
| Durgapur | West Bengal | UK |
| Bokaro | Jharkhand | USSR |
| JSW Vijayanagar (Toranagallu) | Karnataka | private – largest single-location plant |

## 3. Policies
| Year | Policy |
|---|---|
| 1944 | Bombay Plan (industrialists) |
| 1948 | Industrial Policy Resolution |
| 1956 | IPR – Schedules A/B/C, public sector 'commanding heights' (2nd Plan, Mahalanobis) |
| 1991 | New Industrial Policy – LPG, de-licensing |
| 2006 | MSMED Act |
| 2014 | Make in India (25 Sep) |
| 2020 | PLI schemes |
- **IIP** – NSO (MoSPI), base 2011-12; **8 core industries** ≈ 40% of IIP (refinery products ≈ 28% – highest)
- Corridors: DMIC (Japan); Chennai–Bengaluru (Tumakuru node); NICDC coordinates

## 4. River valley projects
| Project | River | State |
|---|---|---|
| Bhakra Nangal | Sutlej | HP/Punjab (Gobind Sagar) |
| Hirakud | Mahanadi | Odisha |
| DVC (1948, model TVA) | Damodar | Jharkhand/WB |
| Sardar Sarovar | Narmada | Gujarat |
| Tehri | Bhagirathi | Uttarakhand |
| Nagarjuna Sagar | Krishna | Telangana/AP |
| Tungabhadra | Tungabhadra | Karnataka (Hosapete) |
| Almatti | Krishna | Karnataka |
| KRS | Kaveri | Karnataka |

## 5. Public sector undertakings
- **Navratna 1997, Maharatna 2009**; Maharatna: avg net profit > ₹5,000 cr, turnover > ₹25,000 cr, net worth > ₹15,000 cr
- **HAL – 14th Maharatna (Oct 2024)**
- Bengaluru HQs: HAL, BEL, BEML, ITI, HMT, KIOCL, ISRO; NMDC – Hyderabad
- DIPAM (2016) manages disinvestment; Air India → Tata (Jan 2022); LIC IPO (May 2022)
- NITI Aayog replaced Planning Commission on 1 Jan 2015
- Finance institutions: IFCI 1948 (first DFI), EXIM 1982, NABARD 1982, SIDBI 1990, SEBI statutory 1992

## ⚠ Traps
- Almatti is on the **Krishna**, not Kaveri; KRS is on the Kaveri
- EXIM Bank 1982 (not 1983), SIDBI 1990 (not 1991) – GTTC 2024 key
- Chittaranjan = locomotives, Perambur = ICF coaches, Yelahanka = Rail Wheel Factory
"""}],
    "Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary": [
        {"title": "Indian Constitution – revision notes (FRs, legislature, executive, judiciary)", "md": """## 1. Sources
| Source | Borrowed |
|---|---|
| UK | parliamentary system, single citizenship, rule of law, writs |
| USA | Fundamental Rights, judicial review, impeachment, independent judiciary |
| Ireland | DPSP, nomination to RS, President's election method |
| Australia | Concurrent List, joint sitting, trade & commerce |
| Canada | federation with strong Centre, residuary powers with Centre |
| France | Republic, liberty-equality-fraternity |
| South Africa | amendment procedure, election of RS members |
| USSR | Fundamental Duties, justice in Preamble |

## 2. Fundamental Rights (Part III)
| Right | Articles |
|---|---|
| Equality | 14–18 (17 untouchability, 18 titles) |
| Freedom | 19–22 (21 life & liberty; 21A education – 86th Amdt 2002) |
| Against exploitation | 23–24 |
| Religion | 25–28 |
| Cultural & educational | 29–30 |
| Constitutional remedies | 32 ('heart and soul' – Ambedkar) |
- Only to citizens: **15, 16, 19, 29, 30**
- Property: removed by 44th Amdt 1978 → **Art. 300A**
- Writs: habeas corpus, mandamus, prohibition, certiorari, quo warranto (SC – 32, HC – 226, wider)

## 3. DPSP (Part IV, 36–51) and Duties (51A)
- Non-justiciable (Art. 37); 40 – village panchayats; 44 – UCC; 45 – early childhood care; 48 – agriculture/cows; 48A – environment
- 42nd Amdt added 39(f), 39A, 43A, 48A
- Duties: Swaran Singh Committee, 42nd Amdt 1976 (10) + 86th 2002 (11th)
- Preamble amended once (42nd: socialist, secular, integrity); part of Constitution – Kesavananda 1973

## 4. Union and state executive / legislature
| Item | Fact |
|---|---|
| President's election | elected MPs + elected MLAs (incl. Delhi, Puducherry) |
| Impeachment (61) | violation of the Constitution |
| VP | ex-officio RS Chairman; elected by all MPs |
| Money Bill (110) | Speaker certifies; RS delay 14 days |
| Joint sitting (108) | Speaker presides; not for Money/Amendment Bills; held 1961, 1978, 2002 |
| RS nominated | 12 (Art. 80) |
| Ordinance | 123 (President), 213 (Governor) |
| Council of Ministers | ≤ 15% of house (91st Amdt 2003) |
| Reserved LS seats | SC 84, ST 47 |
| Legislative Council (171) | 1/3 local bodies, 1/3 MLAs, 1/12 graduates, 1/12 teachers, 1/6 nominated by **Governor** |
| Karnataka | Assembly 224, Council 75 |
| Law-making | 1st reading → 2nd → committee → report → 3rd |
- Speakers: Shivraj Patil 10th LS, Balayogi 12th, Meira Kumar 15th, Om Birla 17th & 18th
- Calling attention – Indian innovation since **1954**; Zero Hour – 1962
- Anglo-Indian nomination ended – 104th Amdt 2020

## 5. Judiciary and bodies
| Body | Article / fact |
|---|---|
| Supreme Court | 124; 8 judges (1950) → 34 now; advisory 143; collegium – 2nd Judges case 1993 |
| High Court | 214; Karnataka benches Dharwad & Kalaburagi; Madras bench Madurai |
| Emergency | 352 national, 356 President's Rule, 359 suspend FR enforcement, 360 financial |
| Tribunals | Part XIV-A, 323A/B (42nd Amdt); Administrative Tribunals Act 1985 |
| CAG | 148 |
| EC | 324 (multi-member since 1993) |
| UPSC / SPSC | 315; SPSC appointed by Governor, removed by President |
| Finance Commission | 280; 16th – Arvind Panagariya (2026–31) |
| GST Council | 279A (101st Amdt, 2016) |
| NCST | 338A (89th Amdt 2003, from 2004) |
| NHRC | statutory 1993; chair = retired CJI/SC judge |
| AG / Advocate General | 76 / 165 |
| RTI | 2005; 30 days, life & liberty 48 hours; CIC must not be MP/MLA |
| Karnataka Lokayukta | 1984 Act; Lokpal Act 2013 (first Lokpal P.C. Ghose 2019) |

## ⚠ Traps
- 365 ≠ President's Rule (that is 356); 359 suspends FRs, 360 is financial emergency
- Legislative Council nominees – Governor, not President
- High Court judges CAN be removed (same as SC judges)
- NITI Aayog is not a constitutional body
"""}],
}
