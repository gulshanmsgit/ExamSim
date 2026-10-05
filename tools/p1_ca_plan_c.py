"""Paper 1 · Current Affairs · planner topic P1-CA-07 United Nations Organizations and Headquarters (2 sub-topics × 20), with
detailed notes (NOTES).
Sources: un.org (UN Charter, principal organs, specialised agencies), the agencies' own websites, MEA, news reports up to mid-2026.
Most questions are REAL previous-year questions from VAO 2024, PSI 2023, Legislative Council 2024 Paper-1, GTTC 2024 GK (official KEA
key), KEA 2025–26 GK papers, KSET 2025 General Paper and a UPSC-coaching entrance test (answers worked out by ExamSim unless marked
official). Heads of organisations change often, so the notes give them "as of mid-2026" and questions avoid them."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

UN_SYSTEM = [
    ("The Food and Agriculture Organization (FAO) of United Nations had decided which of the following year as International Year of Millets?",
     ["2021", "2023", "2013", "2014"], 1,
     "The UN General Assembly declared 2023 the International Year of Millets on India's proposal; FAO led the observance." + NOTE,
     "Legislative Council 2024 Asst/Computer Operator P1 · Q10"),
    ("Which of the following organisation brings out the publication known as \"World Economic Outlook\"?",
     ["The International Monetary Fund", "The United Nations Development Program", "The World Economic Forum", "The World Bank"], 0,
     "The IMF publishes the World Economic Outlook twice a year (April and October)." + NOTE, "PSI 2023 General Paper · Q33"),
    ("Term 'Reserve Tranche' is associated with which of the following organisation?",
     ["World Trade Organisation (WTO)", "International Monetary Fund (IMF)", "World Bank", "Asian Development Bank (ADB)"], 1,
     "The reserve tranche is the part of a member's IMF quota paid in reserve assets; the member can draw it without conditions." + NOTE,
     "Legislative Council 2024 Data Entry P1 · Q70"),
    ("Expand UNODA.",
     ["United Nations Organization for Defence Affairs", "United Nations Office for Disarmament Affairs",
      "United Nations Office for Defence Arms", "United Nations Office for Deficiency Affairs"], 1,
     "UNODA (New York) supports disarmament work, including the Arms Trade Treaty and weapons of mass destruction." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q93"),
    ("Indicate the correct chronological order for the setting up of the following institutions.\n(a) GATT\n(b) IMF\n(c) European Union\n(d) WTO",
     ["(a), (b), (c), (d)", "(b), (c), (d), (a)", "(b), (a), (c), (d)", "(b), (a), (d), (c)"], 2,
     "IMF – December 1945; GATT – signed 1947 (in force 1948); European Union – Maastricht Treaty, 1993; WTO – 1 January 1995." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q23"),
    ("Consider the following pairs:\nInstitution – Year of Establishment\na. International Monetary Fund (IMF) – 27th December, 1945\nb. Multilateral Investment Guaranty Agency (MIGA) – 1988\nc. New Development Bank or BRICS Bank – 2012\nd. Asian Infrastructure Investment Bank (AIIB) – 2020\nHow many pairs in the above are correctly matched ?",
     ["All 4", "Only 3", "Only 2", "Only 1"], 2,
     "IMF (27 Dec 1945) and MIGA (1988) are right. The NDB was agreed at Fortaleza in 2014 (working from 2015) and the AIIB started in January 2016." + NOTE,
     "UPSC coaching entrance 2026 (HK) · Q19"),
    ("Match the following:\nList-I (Report)\n(a) International Migration Outlook\n(b) Global Education Monitoring Report\n(c) World Development Report\n(d) World Economic Outlook\n(e) World Investment Report\nList-II (Published by)\n(i) UNESCO\n(ii) OECD\n(iii) IMF\n(iv) UNCTAD\n(v) World Bank",
     ["a – v, b – iv, c – iii, d – ii, e – i", "a – ii, b – i, c – v, d – iii, e – iv", "a – ii, b – i, c – iv, d – v, e – iii", "a – v, b – iv, c – ii, d – i, e – iii"], 1,
     "OECD – International Migration Outlook; UNESCO – GEM Report; World Bank – World Development Report; IMF – World Economic Outlook; UNCTAD – World Investment Report." + NOTE,
     "KEA 2025 GK (HK, 21 Dec 2025) · Q59"),
    ("Which organizations conducted jointly the Financial Sector Assessment Program (FSAP) in 2025?",
     ["World Bank and IMF", "World Economic Forum and ADB", "World Bank and ADB", "ADB and New Development Bank"], 0,
     "The FSAP, started in 1999, is a joint IMF–World Bank review of a country's financial sector; India's latest was released in 2025." + NOTE,
     "KEA 2026 GK-2 (HK, 9 May 2026) · Q82"),
    ("The United Nations Organization came into existence on:",
     ["24 October 1945", "26 June 1945", "10 December 1948", "1 January 1942"], 0,
     PYQ + "The Charter was signed at San Francisco on 26 June 1945 and came into force on 24 October 1945 (UN Day)."),
    ("Which principal organ of the UN has five permanent members with veto power?",
     ["Security Council", "General Assembly", "Economic and Social Council", "Trusteeship Council"], 0,
     "The P5 are China, France, Russia, the UK and the USA; the other 10 members are elected for two years."),
    ("The International Court of Justice, the principal judicial organ of the UN, is located at:",
     ["The Hague", "Geneva", "New York", "Vienna"], 0, PYQ + "It has 15 judges elected for nine years; it is the only principal organ outside New York."),
    ("Which principal organ of the UN suspended its operations in 1994 after the last trust territory, Palau, became independent?",
     ["Trusteeship Council", "Economic and Social Council", "Security Council", "Secretariat"], 0, "The UN has six principal organs in the Charter."),
    ("Match the UN agency with its headquarters:\na. UNESCO  b. FAO  c. IAEA  d. UNEP\n1. Paris  2. Rome  3. Vienna  4. Nairobi",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0,
     PYQ + "UNEP (1972) is the first UN agency headquartered in a developing country."),
    ("Which of these UN bodies is headquartered in Geneva?",
     ["World Health Organization", "UNICEF", "UNDP", "International Maritime Organization"], 0,
     "UNICEF and UNDP are in New York; the IMO is in London."),
    ("The oldest of the present UN specialised agencies, founded in 1865, is the:",
     ["International Telecommunication Union (ITU)", "Universal Postal Union (UPU)", "International Labour Organization (ILO)", "World Meteorological Organization (WMO)"], 0,
     "ITU (Geneva) – 1865; UPU (Bern) – 1874; ILO (Geneva) – 1919."),
    ("The International Labour Organization, which won the Nobel Peace Prize in 1969, was set up in:",
     ["1919, under the Treaty of Versailles", "1945, with the UN Charter", "1948", "1957"], 0,
     "It became the first specialised agency of the UN in 1946 and has a tripartite structure (governments, employers, workers)."),
    ("Who was the first woman President of the UN General Assembly?",
     ["Vijaya Lakshmi Pandit", "Indira Gandhi", "Sarojini Naidu", "Hansa Mehta"], 0,
     PYQ + "She presided over the 8th session (1953). Hansa Mehta helped draft the Universal Declaration of Human Rights."),
    ("Consider the statements:\nI. India was one of the founding members of the United Nations.\nII. India has been a non-permanent member of the UN Security Council eight times.",
     I_II, 2, "India signed the Charter in 1945 even before independence; its eighth term was 2021–22."),
    ("Assertion (A): The International Civil Aviation Organization is headquartered in Montreal.\nReason (R): All UN specialised agencies are headquartered in Europe.",
     AR, 2, "Several agencies are outside Europe – ICAO (Montreal), IMF and World Bank (Washington), UNEP (Nairobi)."),
    ("The six official languages of the United Nations are Arabic, Chinese, English, French, Russian and:",
     ["Spanish", "Hindi", "German", "Portuguese"], 0, "Arabic was added in 1973; English and French are the working languages of the Secretariat."),
]

OTHER_ORGS = [
    ("Match the following International Organisations and Headquarters:\nInternational Organisation\na) African Union (AU)\nb) Association of Southeast Asian Nations (ASEAN)\nc) North Atlantic Treaty Organisation (NATO)\nd) World Trade Organisation (WTO)\nHeadquarters\ni. Brussels\nii. Addis Ababa\niii. Geneva\niv. Jakarta\nSelect the correct answer using the codes given below:",
     ["a – i, b – ii, c – iii, d – iv", "a – ii, b – iv, c – i, d – iii", "a – ii, b – iv, c – iii, d – i", "a – iv, b – ii, c – iii, d – i"], 1,
     "AU – Addis Ababa (Ethiopia); ASEAN – Jakarta; NATO – Brussels; WTO – Geneva." + NOTE, "VAO 2024 Paper-1 · Q10"),
    ("Match the following:\nOrganisation – Headquarters\na) BIMSTEC  i. Manila\nb) IMF  ii. Dhaka\nc) Asian Development Bank  iii. Washington D.C\nd) WHO  iv. Geneva",
     ["a – ii, b – iii, c – i, d – iv", "a – ii, b – iii, c – iv, d – i", "a – iv, b – ii, c – iii, d – i", "a – i, b – iii, c – ii, d – iv"], 0,
     "BIMSTEC – Dhaka; IMF – Washington D.C.; ADB – Manila; WHO – Geneva." + NOTE, "VAO 2024 Paper-1 · Q93"),
    ("Which is the 31st member country of NATO, a Western Alliance?",
     ["Iceland", "Greenland", "Finland", "Ireland"], 2,
     "Finland joined on 4 April 2023 and Sweden became the 32nd member on 7 March 2024." + NOTE, "PSI 2023 General Paper · Q14"),
    ("Which of the following group of four countries are members of G20?",
     ["Argentina, Mexico, South Africa, Turkey", "Australia, Canada, Malaysia, New Zealand", "Brazil, Iran, Saudi Arabia, Vietnam", "Indonesia, Japan, Singapore, South Korea"], 0,
     "Malaysia, New Zealand, Iran, Vietnam and Singapore are not G20 members; the African Union joined in 2023 (New Delhi summit)." + NOTE,
     "PSI 2023 General Paper · Q15"),
    ("Economic Freedom Index (EFI) is released by which organisation?",
     ["World Economic Forum", "The Heritage Foundation and Wall Street Journal", "World Bank", "Institute of Economics and Peace"], 1,
     "The Index of Economic Freedom was started in 1995 by the Heritage Foundation with The Wall Street Journal." + NOTE,
     "Legislative Council 2024 Data Entry P1 · Q45"),
    ("IUCN Red List refers to a list that contains the details of",
     ["Extinct species all over the world", "Hybrid varieties of crop plants", "Crop plant varieties introduced from foreign countries", "Weed plants of Asia"], 0,
     "The Red List records the extinction risk of species worldwide, from Least Concern to Extinct. IUCN is headquartered at Gland, Switzerland." + KEY,
     "GTTC 2024 Asst Gr-II GK · Q37"),
    ("The organisation that publishes the data of endangered, threatened, vulnerable species of organisms is :",
     ["WWF", "MAB", "JFM", "IUCN"], 3,
     "IUCN (International Union for Conservation of Nature, 1948) publishes the Red List and Red Data Books." + NOTE, "KEA 2026 GK-2 (NHK, 25 Jan 2026) · Q56"),
    ("BIMSTEC stands for",
     ["Bay of International Maritime Security Trade Economic Cooperation", "Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation",
      "Border Initiative of Maritime and Trade Economic Cooperation", "Bengal International Strategic Trade and Economic Council"], 1,
     "Set up in 1997 (Bangkok Declaration), it has 7 members; the secretariat is in Dhaka." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q99"),
    ("Which one of the following country is not a member of OPEC organization?",
     ["Nigeria", "Saudi Arabia", "Iran", "Qatar"], 3,
     "Qatar left OPEC on 1 January 2019. OPEC (founded at Baghdad, 1960) has its headquarters in Vienna." + NOTE, "UPSC coaching entrance 2026 (HK) · Q70"),
    ("Match List I with List II and select the correct answer using the codes given below:\nList I (Organizations)\n(a) SAARC\n(b) ASEAN\n(c) OPEC\n(d) EU\nList II (Focus / Goal)\n(i) Promote regional peace and prosperity in South Asia.\n(ii) Coordinate petroleum policies and stabilize oil markets\n(iii) Political and Economic integration of Europe.\n(iv) Economic growth and Political Cooperation in South-East Asia.",
     ["a – i, b – iv, c – ii, d – iii", "a – ii, b – i, c – iv, d – iii", "a – iv, b – iii, c – ii, d – i", "a – i, b – ii, c – iii, d – iv"], 0,
     "SAARC – South Asia; ASEAN – South-East Asia; OPEC – oil policies; EU – European integration." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q25"),
    ("Consider the following statements related to Earth Hour:\na) It is a climate change and environmental conservation related awareness program/movement.\nb) It was launched by United Nations Environment Program (UNEP)\nc) It was launched in 2007 in Australia.\nd) Voluntary switch off of non-essential lights for 1 hour is a part of this movement.\nHow many of the above statement(s) is/are correct?",
     ["All of them are correct", "Only three of them are correct", "Only two of them are correct", "Only one is correct"], 1,
     "Earth Hour was started by WWF (not UNEP) in Sydney in 2007; it is held on the last Saturday of March." + NOTE, "KSET 2025 General Paper · Q44"),
    ("Consider the following statements related to International Solar Alliance (ISA).\na) ISA is a global intergovernmental organization dedicated to advancing solar power adoption for a carbon-neutral future.\nb) It is a collaborative initiative between India and Germany.\nc) The headquarters of ISA is in Bonn, Germany.\nd) All the SAARC countries are the members of ISA also.\nWhich of the above statement(s) is/are correct?",
     ["All of them", "a, b and d only", "a and b only", "a only"], 3,
     "ISA was launched by India and France at COP21, Paris (2015); its headquarters is at Gurugram, India; not every SAARC country (e.g. Pakistan) is a member." + NOTE,
     "KSET 2025 General Paper · Q45"),
    ("The headquarters of the SAARC Secretariat is at:",
     ["Kathmandu", "New Delhi", "Dhaka", "Colombo"], 0, PYQ + "SAARC was founded at Dhaka in 1985; Afghanistan joined in 2007 as the 8th member."),
    ("Which country became the 11th member of ASEAN in October 2025?",
     ["Timor-Leste", "Papua New Guinea", "Bangladesh", "Sri Lanka"], 0,
     "It was admitted at the 47th ASEAN summit at Kuala Lumpur. ASEAN was founded at Bangkok in 1967."),
    ("The headquarters of INTERPOL is at:",
     ["Lyon, France", "The Hague, Netherlands", "Geneva, Switzerland", "Brussels, Belgium"], 0,
     PYQ + "Europol is at The Hague."),
    ("Match the organisation with its headquarters:\na. Commonwealth Secretariat  b. OECD  c. UNICEF  d. International Committee of the Red Cross\n1. London  2. Paris  3. New York  4. Geneva",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-4, c-3, d-2", "a-4, b-2, c-1, d-3"], 0,
     "Amnesty International is also in London; UNICEF is one of the UN funds based in New York."),
    ("The New Development Bank set up by the BRICS countries has its headquarters at:",
     ["Shanghai", "New Delhi", "Moscow", "Johannesburg"], 0, PYQ + "Its first president was India's K. V. Kamath; the AIIB is headquartered in Beijing."),
    ("Consider the statements:\nI. The World Economic Forum publishes the Global Gender Gap Report.\nII. UNDP publishes the Human Development Report.",
     I_II, 2, "WEF (Cologny, Geneva) also publishes the Global Risks Report; UNDP's HDI was devised by Mahbub ul Haq and Amartya Sen."),
    ("Assertion (A): India is a member of the Quad along with the USA, Japan and Australia.\nReason (R): The Quad is a military alliance with a mutual-defence clause like NATO.",
     AR, 2, "The Quad is an informal strategic dialogue with no mutual-defence treaty; NATO's Article 5 is a mutual-defence clause."),
    ("The headquarters of the World Wide Fund for Nature (WWF) and of IUCN are both located at:",
     ["Gland, Switzerland", "Geneva, Switzerland", "Nairobi, Kenya", "Washington D.C., USA"], 0,
     "WWF was founded in 1961; its logo is the giant panda."),
]

TOPICS = {
    "United Nations Organizations and Headquarters": [("1 · The UN System – Organs, Agencies and Reports", UN_SYSTEM),
                                                      ("2 · Other International Organisations and Headquarters", OTHER_ORGS)],
}

NOTES = {
    "United Nations Organizations and Headquarters": [{"title": "United Nations – organs, agencies, headquarters (detailed)", "md": """# United Nations Organization (UNO)

## 1. Basics
| Point | Fact |
|---|---|
| Idea | **Atlantic Charter** (1941, Roosevelt & Churchill) → **Declaration by United Nations** (1 Jan 1942) – name coined by **F. D. Roosevelt** |
| Planning | Dumbarton Oaks (1944), Yalta (Feb 1945) |
| Charter signed | **26 June 1945**, **San Francisco** (50 countries; Poland signed later → **51 founding members**) |
| Came into existence | **24 October 1945** → **UN Day** |
| Members | **193** (latest: **South Sudan, 2011**); observers: Holy See, Palestine |
| Headquarters | **New York** (land donated by John D. Rockefeller Jr.); other offices: Geneva, Vienna, Nairobi |
| Official languages | **6** – Arabic, Chinese, English, French, Russian, Spanish (Arabic added 1973); working languages: English, French |
| Predecessor | **League of Nations** (1920, Geneva; dissolved 1946) |
| India | **Founding member** (signed in 1945, before independence) |

## 2. Six principal organs
| Organ | Key facts |
|---|---|
| **General Assembly** | All 193 members, one vote each; President elected yearly. 80th session (2025–26) President: **Annalena Baerbock** (Germany). First woman President: **Vijaya Lakshmi Pandit** (India, 1953) |
| **Security Council** | **15 members**: 5 permanent with **veto** (**USA, UK, France, Russia, China**) + 10 non-permanent elected for **2 years**. India – non-permanent **8 times** (last **2021–22**); seeks a permanent seat (with Brazil, Germany, Japan = **G4**) |
| **Economic and Social Council (ECOSOC)** | **54 members**, 3-year terms; coordinates the specialised agencies |
| **Trusteeship Council** | Suspended **1 Nov 1994** after **Palau** became independent |
| **International Court of Justice (ICJ)** | **The Hague**, Netherlands – the only principal organ outside New York; **15 judges**, **9-year** terms. Indian judges: B. N. Rau, Nagendra Singh (President 1985–88), R. S. Pathak, **Dalveer Bhandari** |
| **Secretariat** | Headed by the **Secretary-General** – appointed by the GA on the SC's recommendation, 5-year term |

## 3. Secretaries-General
| # | Name | Country | Term |
|---|---|---|---|
| 1 | Trygve Lie | Norway | 1946–52 |
| 2 | Dag Hammarskjöld | Sweden | 1953–61 (died in a plane crash; posthumous Nobel) |
| 3 | **U Thant** | **Myanmar (Burma)** | 1961–71 – first Asian |
| 4 | Kurt Waldheim | Austria | 1972–81 |
| 5 | **Javier Pérez de Cuéllar** | **Peru** | 1982–91 |
| 6 | Boutros Boutros-Ghali | Egypt | 1992–96 – first African |
| 7 | Kofi Annan | Ghana | 1997–2006 (Nobel 2001 with the UN) |
| 8 | Ban Ki-moon | South Korea | 2007–16 |
| 9 | **António Guterres** | **Portugal** | 2017–**31 Dec 2026**; selection of the 10th SG is under way in 2026 |

**Trap:** VAO 2024 swapped Pérez de Cuéllar (Peru) and Guterres (Portugal).

## 4. Specialised agencies and other UN bodies – headquarters
| Body | HQ | Set up | Remember |
|---|---|---|---|
| **ITU** – International Telecommunication Union | Geneva | **1865** | Oldest; World Telecom Day 17 May |
| **UPU** – Universal Postal Union | **Bern** | 1874 | World Post Day 9 Oct |
| **ILO** – International Labour Organization | Geneva | **1919** (Treaty of Versailles) | Tripartite; **Nobel Peace 1969**; first UN specialised agency (1946) |
| **FAO** – Food and Agriculture Organization | **Rome** | 1945 (16 Oct = World Food Day) | Led the **International Year of Millets 2023** (India's proposal) |
| **UNESCO** – Educational, Scientific and Cultural Org. | **Paris** | 1945 (in force 1946) | World Heritage list; GEM Report |
| **WHO** – World Health Organization | **Geneva** | **7 April 1948** (World Health Day) | Pandemic Agreement adopted May 2025; USA withdrew in Jan 2026 |
| **IMF** – International Monetary Fund | **Washington D.C.** | Bretton Woods 1944; **27 Dec 1945** | **World Economic Outlook**, Global Financial Stability Report; SDR, reserve tranche |
| **World Bank** (IBRD) | Washington D.C. | 1944/45 | **World Development Report**; IDA (1960), IFC (1956), **MIGA (1988)**, ICSID |
| **WTO** – World Trade Organization | **Geneva** | **1 Jan 1995** (replaced GATT, 1947/48) | Marrakesh Agreement 1994; not a UN agency (related organisation) |
| **IAEA** – International Atomic Energy Agency | **Vienna** | 1957 | "Atoms for Peace"; Nobel 2005 |
| **UNIDO**, **UNODC** | Vienna | 1966 / 1997 | Industrial development / drugs and crime |
| **WMO** – World Meteorological Organization | Geneva | 1950 (23 March) | With UNEP set up the **IPCC** (1988) |
| **WIPO** – World Intellectual Property Org. | Geneva | 1967 | **Global Innovation Index** |
| **ICAO** – International Civil Aviation Org. | **Montreal** | 1944 (Chicago Convention), 1947 | |
| **IMO** – International Maritime Org. | **London** | 1948 | Only UN agency HQ in the UK |
| **IFAD**, **WFP** | **Rome** | 1977 / 1961 | WFP – **Nobel Peace 2020** |
| **UN Tourism** (UNWTO) | **Madrid** | 1975 | |
| **UNEP** – UN Environment Programme | **Nairobi** | **1972** (Stockholm conference) | First UN HQ in a developing country; Emissions Gap Report |
| **UN-Habitat** | Nairobi | 1978 | |
| **UNICEF** | New York | 1946 | Nobel 1965 |
| **UNDP** | New York | 1965 | **Human Development Report** (HDI) |
| **UNFPA** | New York | 1969 | State of World Population |
| **UN Women** | New York | 2010 | |
| **UNODA** – Office for **Disarmament Affairs** | New York | 1998 (as department 1982) | |
| **UNHCR** – Refugee agency | Geneva | 1950 | Nobel 1954 and 1981 |
| **UNCTAD** | Geneva | 1964 | **World Investment Report** |
| **UNFCCC** secretariat | **Bonn** | 1992 (Rio) | COPs; Paris Agreement 2015 |
| **UN University** | **Tokyo** | 1973 | |

## 5. Other international organisations
| Organisation | HQ | Founded | Members / notes |
|---|---|---|---|
| **NATO** | **Brussels** | 1949 (Washington Treaty) | **32**: Finland **31st** (Apr 2023), **Sweden 32nd** (Mar 2024); Art. 5 – collective defence |
| **ASEAN** | **Jakarta** | 1967 (Bangkok Declaration) | **11** – **Timor-Leste** joined Oct 2025 |
| **African Union** | **Addis Ababa** | 2002 (OAU 1963) | 55; joined **G20** in 2023 |
| **European Union** | Brussels | 1993 (Maastricht) | 27 (UK left 2020); euro |
| **SAARC** | **Kathmandu** | 1985 (Dhaka) | 8 – Afghanistan joined 2007 |
| **BIMSTEC** | **Dhaka** | 1997 | 7: Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka, Thailand – **Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation** |
| **OPEC** | **Vienna** | 1960 (**Baghdad**) | Qatar left 2019, Ecuador 2020, Angola 2024 |
| **G20** | No secretariat | 1999 | 19 countries + EU + AU; India presidency 2023 (New Delhi) |
| **BRICS / NDB** | NDB: **Shanghai** | 2009 / NDB 2014–15 | Indonesia full member Jan 2025; India chairs BRICS in 2026 |
| **AIIB** | **Beijing** | **2016** | India is the 2nd largest shareholder |
| **ADB** | **Manila** | 1966 | |
| **SCO** | Beijing (secretariat) | 2001 | 10 members – Iran 2023, Belarus 2024 |
| **Commonwealth** | London | 1949 (London Declaration) | 56 members – Gabon and Togo joined 2022 |
| **OECD** | Paris | 1961 | International Migration Outlook |
| **WEF** | Cologny, Geneva | 1971 | Davos meeting; Global Gender Gap, Global Risks reports |
| **INTERPOL** | **Lyon** | 1923 | Europol – The Hague |
| **ICRC** (Red Cross) | Geneva | 1863 (Henry Dunant) | Nobel 1917, 1944, 1963 |
| **Amnesty International** | London | 1961 | Nobel 1977 |
| **IUCN** | **Gland**, Switzerland | 1948 | **Red List** of threatened species (extinction risk) |
| **WWF** | Gland, Switzerland | 1961 | **Earth Hour** – started in **Sydney, 2007**, last Saturday of March (not UNEP!) |
| **International Solar Alliance** | **Gurugram**, India | 2015 (India + **France**, COP21 Paris) | Not all SAARC states are members |
| **ICC** (International Criminal Court) | The Hague | 2002 (Rome Statute) | India is not a member |
| **Quad** | – | 2007, revived 2017 | India, USA, Japan, Australia – informal dialogue, no defence treaty |

## 6. Who publishes which report?
| Report / index | Publisher |
|---|---|
| World Economic Outlook, Global Financial Stability Report | **IMF** |
| World Development Report | **World Bank** |
| Human Development Report | **UNDP** |
| World Investment Report | **UNCTAD** |
| Global Education Monitoring Report | **UNESCO** |
| International Migration Outlook | **OECD** |
| Global Gender Gap, Global Risks | **WEF** |
| Index of Economic Freedom | **Heritage Foundation** (with the Wall Street Journal) |
| Global Peace Index | Institute for Economics and Peace |
| Corruption Perceptions Index | Transparency International (Berlin) |
| World Press Freedom Index | Reporters Without Borders (Paris) |
| Global Innovation Index | **WIPO** |
| Living Planet Report | WWF |
| Emissions Gap Report | UNEP |
| World Happiness Report | Wellbeing Research Centre (Oxford) with Gallup and UN SDSN |
| State of Food Security and Nutrition | FAO (with IFAD, UNICEF, WFP, WHO) |
| Financial Sector Assessment Program (FSAP) | **IMF + World Bank** jointly |

## 7. Heads (as of mid-2026 – these change, check before the exam)
UN SG **António Guterres** · WHO **Tedros Adhanom Ghebreyesus** · IMF **Kristalina Georgieva** · World Bank **Ajay Banga** · WTO **Ngozi Okonjo-Iweala** (2nd term from Sept 2025) · IAEA **Rafael Grossi** · ILO **Gilbert Houngbo** · FAO **Qu Dongyu** · UNEP **Inger Andersen** · ITU **Doreen Bogdan-Martin**.

## 8. Traps and confusions
- UN came into existence **24 Oct 1945**; the Charter was signed **26 June 1945**.
- **WTO** (trade, Geneva) vs **UN Tourism** (formerly UNWTO, Madrid).
- **UNEP – Nairobi**, not Geneva; **UPU – Bern**, not Geneva; **IMO – London**; **ICAO – Montreal**.
- **Earth Hour** – WWF, not UNEP. **ISA** – India + France, HQ Gurugram (not Bonn; Bonn hosts the UNFCCC).
- **GATT (1947)** came before the WTO (1995); the IMF (1945) came before GATT.
- **NDB** agreed 2014 (Fortaleza), **AIIB** started 2016 – not 2012 / 2020.
"""}],
}
