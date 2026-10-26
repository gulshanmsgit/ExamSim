"""Real KEA 2026 general-knowledge questions (Paper 1) for the KRIES Paper 1 subjects, sorted into items A–O (owner, 26 Oct 2026).
Source: the English text of the five bilingual KEA 2026 GK papers in sources/pyq/ocr (GK-1 NHK 11 Jan, GK-2 NHK 25 Jan, GK-3 NHK 10 May,
GK-1 HK 22 Feb, GK-2 HK 9 May) – only questions NOT already used in tools/*.py. Wording kept as printed (spaces restored where the OCR
lost them); where the OCR blurred a roman numeral in the answer codes, the code that matches the facts was restored and this is said in
the explanation. No official key has been published – every answer was worked out by ExamSim. Skipped: questions with garbled or missing
text, answers that could not be confirmed, and ones whose premise could not be checked. kries_p1.pulled() adds these to each subject's
'KEA Previous-Year Questions' topic."""

NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"
FIX = " (A roman numeral blurred in the scan was restored in the codes.)"
G1N, G2N, G3N = "KEA 2026 GK-1 (NHK, 11 Jan 2026)", "KEA 2026 GK-2 (NHK, 25 Jan 2026)", "KEA 2026 GK-3 (NHK, 10 May 2026)"
G1H, G2H = "KEA 2026 GK-1 (HK, 22 Feb 2026)", "KEA 2026 GK-2 (HK, 9 May 2026)"
AB = ["Both Statement I and Statement II are correct and Statement II explains Statement I",
      "Both Statement I and Statement II are correct, but Statement II does not explain Statement I",
      "Statement I is correct, but Statement II is incorrect", "Statement I is incorrect, but Statement II is correct"]


def q(text, opts, ans, expl, paper, n):
    return (text, opts, ans, expl + NOTE, f"{paper} · Q{n}")


PYQ26 = {
    "A": [
        q("Consider the following statements with reference to PM Vishwakarma Scheme.\n(a) This scheme was launched on 17 September, 2025 on the occasion of Vishwakarma day.\n"
          "(b) Related to enhance the skills of artisans.\n(c) Is implemented by MoMSME, MSDE and MoF collectively.\n"
          "(d) The financial outlay of this scheme is 13,000 crores starting from FY 2023-24 to FY 2027-28\nHow many of the above statements is/are correct?",
          ["All the four statements are correct", "Only three statements are correct", "Only two statements are correct", "Only one statement is correct"], 1,
          "The scheme was launched on 17 September 2023, not 2025; (b), (c) and (d) are correct.", G1N, 20),
        q("Which among the following UN Councils was suspended in 1994?", ["Economic and Social Council", "Human Rights Council", "Trusteeship Council",
                                                                          "Political and Economic Council"], 2,
          "The Trusteeship Council suspended operation on 1 November 1994 after Palau, the last trust territory, became independent.", G1N, 27),
        q("What is the key factor of India's maritime grand strategy?", ["To dominate the Indian Ocean region", "To secure Sea Lanes of Communication (SLoCs)",
                                                                         "To ensure capacity and capability building in the coastal area", "To conduct and join naval exercises"], 1,
          "Securing the sea lanes that carry India's trade and energy is the core aim.", G1N, 28),
        q("Name the Union Minister for Ports, Shipping and Waterways who inaugurated new projects worth Rs. 1500 crore to mark Golden Jubilee celebrations of the New "
          "Mangalore Port Trust (NMPT) in November 2025.", ["Jyotiraditya Scindia", "Sarbananda Sonowal", "Gajendra Singh", "Hardeep Singh"], 1,
          "Sarbananda Sonowal is the Union Minister of Ports, Shipping and Waterways.", G1N, 32),
        q("Which of the following is a major reason for the growing geopolitical importance of the Indian Ocean in the 21st Century?",
          ["The Indian Ocean has no significant natural resources", "It is landlocked and has limited strategic value",
           "Over 80% of global maritime oil trade passes through key chokepoints in the Indian Ocean", "It is primarily used for regional fishing and has minimal global relevance"], 2,
          "Hormuz, Bab-el-Mandeb and Malacca carry most seaborne oil.", G1N, 76),
        q("The Government of India has recently initiated steps to acquire which island in the Lakshadweep archipelago for defence and strategic purposes?",
          ["Minicoy Island", "Bitra Island", "Agatti Island", "Kavaratti Island"], 1, "Bitra, the smallest inhabited island, was proposed for defence use in 2025.", G1N, 96),
        q("Which of the following statements with regard to ICC Women's World Cup is/are correct?\n(a) India has reached finals three times.\n"
          "(b) Australia, England, New Zealand and India are the countries which have won the one day ICC Women's World Cup till now.\n"
          "(c) In 2025, final match of ICC Women's Cricket World Cup was held in India and Australia was defeated by India.\n"
          "(d) Australia is the country which has won the ICC Women's World Cup highest number of times.",
          ["(a), (b) and (d)", "(b), (c) and (d)", "(a), (c) and (d)", "(a), (b), (c) and (d)"], 0,
          "India beat South Africa (not Australia) in the 2025 final at Navi Mumbai; India's finals: 2005, 2017, 2025.", G1N, 97),
        q("Which of the following statements is/are correct with respect to 'SHANTI' Bill, 2025?\n(a) It enables limited private participation in the nuclear sector under "
          "regulatory oversight.\n(b) The full form of 'SHANTI' is 'Sustainable Harnessing and Administration of Nuclear Emission for Transforming India'.\n"
          "(c) It supports India's clean-energy transition and the long-term objective of achieving 100 GW nuclear energy capacity by 2047.",
          ["(a), (b) and (c)", "(a) only", "(b) only", "(a) and (c)"], 3,
          "SHANTI = Sustainable Harnessing and Advancement of Nuclear energy for Transforming India – (b) misstates it.", G1N, 98),
        q("Which of the following statements about INSV Kaundinya is/are incorrect?\na. INSV Kaundinya embarked on its maiden voyage from Porbandar to Muscat.\n"
          "b. The full form of INSV is Indian Naval Ship Vessel.\nc. It is modelled on a 5th century CE ship depicted in the paintings of Ajanta Caves.",
          ["a and b", "b and c", "a and c", "Only b"], 3, "INSV = Indian Naval Sailing Vessel; the stitched ship sailed Porbandar–Muscat in December 2025.", G2N, 82),
        q("NASA's SpaceX Crew-9 astronauts have successfully returned to Earth after completing the agency's ninth commercial crew rotation mission. Identify the astronaut "
          "who was not a part of the mission.", ["Sunita Williams", "Shubhanshu Shukla", "Butch Wilmore", "Nick Hague"], 1,
          "Shubhanshu Shukla flew on Axiom-4 (2025).", G2N, 84),
        q("Name the scheme launched by Indian Railways with an objective to provide safety and security to women, travelling by trains for their entire journey, from "
          "starting station to destination station.", ["Mission Shakti", "Nirbhaya Fund", "Meri Saheli", "One Stop Centre Scheme"], 2, "RPF's 'Meri Saheli' initiative.", G2N, 85),
        q("Which of the following statements regarding Khaleda Zia, the former Prime Minister of Bangladesh, is/are correct?\na. She was the country's second female Prime "
          "Minister.\nb. Her husband was Ziaur Rahman.\nc. She belonged to Bangladesh Nationalist Party.", ["Only b", "b and c", "a and b", "a, b and c"], 1,
          "She was Bangladesh's first woman Prime Minister (1991).", G2N, 90),
        q("R. Chidambaram served as the 2nd Principal Scientific Advisor to Government of India between 2002-2018 under three Prime Ministers. Those Prime Ministers were:\n"
          "a. Atal Bihari Vajpayee\nb. Inder Kumar Gujral\nc. Manmohan Singh\nd. Narendra Modi", ["b, c and d", "a, b and c", "a, b and d", "a, c and d"], 3,
          "2002–2018 covers Vajpayee, Manmohan Singh and Modi.", G2N, 96),
        q("How many of the following are correctly matched?\nInternational Centre – Country\n(a) International Water Management Institute – Sri Lanka\n"
          "(b) International Livestock Research Institute – Denmark\n(c) International Food Policy Research Institute – USA\n(d) International Potato Centre – Peru\n"
          "(e) International Rice Research Institute – Philippines", ["Only two pairs are correct", "Only three pairs are correct", "Only four pairs are correct",
                                                                       "All the pairs are correct"], 2, "ILRI is in Nairobi, Kenya.", G3N, 81),
        q("Consider the following international institutes/centres.\n(a) International Crops Research Institute for the Semi-Arid Tropics (ICRISAT)\n"
          "(b) International Centre for Integrated Mountain Development (ICIMOD)\n(c) International Rice Research Institute (IRRI)\n"
          "(d) Centre for International Forestry Research (CIFOR)\nHow many of the above is/are located in India?",
          ["Only three of them", "Only two of them", "Only one of them", "None of them"], 2, "ICRISAT – Hyderabad; ICIMOD – Kathmandu; IRRI – Philippines; CIFOR – Indonesia.", G3N, 84),
        q("'Project Kusha' is a programme under the Defence Research and Development Organisation for the Indian Air Force and Indian Navy. The goal of 'Project Kusha' "
          "is to design a mobile long range ____ missile system.", ["Anti-tank guided", "Surface-to-surface", "Surface-to-air", "Air-to-air"], 2,
          "An indigenous long-range air-defence (surface-to-air) system.", G3N, 88),
        q("Match the following.\nList-I (Country): (a) Germany (b) Brazil (c) Turkey (d) France\n"
          "List-II (President): (i) Luiz Inacio Lula da Silva (ii) Recep Tayyip Erdogan (iii) Emmanuel Macron (iv) Frank-Walter Steinmeier",
          ["a-i, b-ii, c-iii, d-iv", "a-iv, b-i, c-ii, d-iii", "a-iii, b-ii, c-i, d-iv", "a-iv, b-iii, c-i, d-ii"], 1,
          "Germany – Steinmeier, Brazil – Lula, Turkey – Erdogan, France – Macron." + FIX, G3N, 90),
        q("Asha Bhosle, the renowned Indian playback singer, businesswoman and actress passed away on 12th April, 2026. Among the following film songs, which is not sung "
          "by her?", ["Yaara seeli seeli (Lekin)", "Dil Cheez Kya Hai (Umrao Jaan)", "Mera Kuch Samaan (Ijaazat)", "Radha Kaisa Na Jale (Lagaan)"], 0,
          "'Yaara Seeli Seeli' was sung by Lata Mangeshkar.", G3N, 91),
        q("Given below are two statements, one labelled as Assertion (A) and the other labelled as Reason (R).\nAssertion (A): India is seeking permanent membership of "
          "Security Council of UNO.\nReason (R): India is a nuclear power country.",
          ["Both (A) and (R) are true and (R) is the correct explanation of (A)", "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
           "(A) is true and (R) is false", "(A) is false and (R) is true"], 1, "India's claim rests on population, democracy, economy and UN contributions.", G1H, 65),
        q("Indian Institutes of Science Education and Research (IISERs) have been established by Government of India. In which of the following places IISERs are located?\n"
          "(a) Mumbai (b) Bhopal (c) Mohali (d) Bengaluru (e) Kolkata (f) Tirupati (g) Berhampur (h) Delhi",
          ["(a), (b), (d), (e) and (h)", "(b), (c), (e) and (g)", "(b), (c), (e), (f) and (g)", "(a), (b), (c), (d), (e), (f), (g) and (h)"], 2,
          "IISERs: Pune, Kolkata, Mohali, Bhopal, Thiruvananthapuram, Tirupati, Berhampur.", G2H, 84),
        q("In April 2026, ISRO has successfully conducted the second integrated air drop test (IADT-02) for which of its upcoming mission?",
          ["NISAR", "Gaganyaan", "Chandrayaan-4", "LuPEX/Chandrayaan-5"], 1, "Air-drop tests check the crew-module parachutes of Gaganyaan.", G2H, 86),
        q("Colonel Sonam Wangchuk (retd), a revered Indian Army Officer who passed away on April 10, 2026 is popularly known as",
          ["Sher Shah", "The Rambo of the Indian Army", "Lion of Ladakh", "Lion of Naushera"], 2, "Maha Vir Chakra (Kargil, 1999).", G2H, 89),
        q("Consider the members of Organisation of Petroleum Exporting Countries (OPEC)\n(a) Iran (b) Bahrain (c) Qatar (d) Oman (e) Kuwait (f) United Arab Emirates\n"
          "How many of the above countries are the members of OPEC?", ["Only five of them", "Only four of them", "Only three of them", "Only two of them"], 2,
          "Iran, Kuwait and the UAE; Qatar left in 2019; Bahrain and Oman are not members.", G2H, 96),
    ],
    "B": [
        q("Match List-I with List-II:\n(a) Nitrogen cycle (b) Water cycle (c) Carbon cycle (d) Sulfur cycle\n(i) Photosynthesis and respiration "
          "(ii) Mineralization, oxidation, assimilation and reduction (iii) Nitrogen fixation and denitrification (iv) Evaporation, condensation and precipitation",
          ["a-iii, b-ii, c-i, d-iv", "a-i, b-ii, c-iv, d-iii", "a-ii, b-iii, c-iv, d-i", "a-iii, b-iv, c-i, d-ii"], 3, "Each cycle with its key processes." + FIX, G1N, 24),
        q("Which Health Planning Committee in India is known for introducing the concept of three-tier health care delivery?", ["Mudaliar Committee", "Bhore Committee",
                                                                                                                              "Kartar Singh Committee", "Shrivastava Committee"], 1,
          "Bhore Committee (1946).", G1N, 25),
        q("Below are the two statements:\nStatement-I: Hot tea cools faster during winter than during summer.\nStatement-II: Rate of cooling is directly proportional to "
          "surrounding temperature.", ["Statement-I and Statement-II are correct", "Statement-I and Statement-II are wrong",
                                       "Statement-I is correct and Statement-II is the correct explanation of Statement-I",
                                       "Statement-I is correct but Statement-II is not the correct explanation of Statement-I"], 3,
          "Newton's law: rate of cooling is proportional to the temperature DIFFERENCE, which is larger in winter.", G1N, 33),
        q("Atmospheric pressures recorded at Bangalore, Delhi, Mumbai and Shimla on a day are 1.2, 1.02, 1.21 and 1.01 respectively. The place at which water boils first "
          "on the said day is", ["Delhi", "Mumbai", "Shimla", "Bangalore"], 2, "Lower pressure, lower boiling point.", G1N, 62),
        q("The correct process that takes place when match stick is struck against the rubbing surface.", ["White Phosphorous converts to Black Phosphorous",
                                                                                                             "Black Phosphorous converts to White Phosphorous",
                                                                                                             "Red Phosphorous converts to White Phosphorous",
                                                                                                             "Red Phosphorous converts to Black Phosphorous"], 2,
          "Friction heat turns some red phosphorus into white phosphorus, which ignites.", G1N, 64),
        q("The correct statement/s regarding 'Royal Water' is/are\n(i) It was a water used only by 'Royal families' for drinking purpose\n(ii) It dissolves gold and platinum\n"
          "(iii) It is highly corrosive\n(iv) It is a fuming liquid", ["(i), (ii), (iii) and (iv)", "(i) and (ii)", "(ii), (iii) and (iv)", "Only (i)"], 2,
          "Aqua regia = 3 HCl : 1 HNO₃.", G1N, 65),
        q("Pick out the incorrect statement/s about geostationary satellite.\n(a) Its time period is 24 hours\n(b) Its height from the surface of earth is 36000 km\n"
          "(c) It revolves in polar plane\n(d) It revolves in equatorial plane", ["(a), (b) and (c)", "(a) and (c)", "Only (c)", "Only (d)"], 2,
          "Geostationary orbits lie in the equatorial plane.", G1N, 66),
        q("A motorcyclist leans inwards while taking a sharp turn. This is done", ["to reduce speed", "to reduce friction", "to get necessary centripetal force",
                                                                                   "to get necessary centrifugal force"], 2, "Leaning provides the inward force for circular motion.", G1N, 67),
        q("Detergents are added to water for washing clothes, because they cleanse clothes by", ["increasing the viscosity of water", "increasing the surface tension of water",
                                                                                                   "decreasing the viscosity of water", "decreasing the surface tension of water"], 3,
          "Lower surface tension lets water wet the fabric.", G1N, 68),
        q("Identify the CORRECT sequential steps of decomposition.\n(a) Catabolism (b) Mineralisation (c) Humification (d) Leaching (e) Fragmentation",
          ["(a), (b), (c), (d), (e)", "(e), (d), (a), (c), (b)", "(e), (b), (c), (a), (d)", "(e), (d), (b), (a), (c)"], 1,
          "Fragmentation → leaching → catabolism → humification → mineralisation.", G1N, 71),
        q("A batsman hits a cricket ball which then rolls on a level ground. After covering a short distance, the ball comes to rest. The ball slows to a stop because",
          ["the batsman did not hit the ball hard enough", "velocity is proportional to the force exerted on the ball", "there is a force on the ball opposing the motion",
           "there is no unbalanced force on the ball, so the ball wants to come to rest"], 2, "Friction opposes the motion.", G1N, 75),
        q("Consider the following statements:\na. Helium is used as a 'lifting gas'.\nb. Helium is the lightest gas.\nc. Helium is a non-explosive and inert gas.\n"
          "Which of the following options is correct with respect to helium?", ["a and b are true and c is the correct explanation for a",
                                                                               "a and c are true and b is the correct explanation for a", "b and c are true and a is wrong",
                                                                               "a is true and c is the correct explanation for a"], 3,
          "Hydrogen is the lightest gas; helium is used because it is light and does not burn.", G2N, 37),
        q("Which of the following statements is/are incorrect with respect to the boiling point of water?\na. Boiling point of water changes with altitude.\n"
          "b. Boiling point of water increases with non-volatile solutes.\nc. Boiling point of water is always 100°C and does not change.\n"
          "d. Boiling point of water decreases with increase of external pressure.", ["a, b and c", "c and d", "b, c and d", "b and c"], 1,
          "Higher pressure raises the boiling point (pressure cooker).", G2N, 38),
        q("10% of sugar solution can be prepared by dissolving in the following manner:\na. 10 g of sugar in 10 g of water.\nb. 10 g of sugar in 1 litre of water.\n"
          "c. 10 g of sugar in 10 g of water.\nd. 10 g of sugar in 100 mL of water.", ["Only a", "Both a and b", "Only c", "Only d"], 3,
          "Of the choices, 10 g in 100 mL of water is the intended 10% (mass/volume) solution.", G2N, 39),
        q("Identify the name of the chemical using the following hints:\nHint (i): It's used in moisturizing creams.\nHint (ii): It generates fire when reacted with "
          "Potassium Permanganate (KMnO₄).\nHint (iii): It's used widely in sanitizers.", ["Acrylic acid", "Acetone", "Glycerin", "Isopropanol"], 2,
          "Glycerin + KMnO₄ ignites spontaneously; glycerin is a humectant in creams and sanitizers.", G2N, 40),
        q("In plants, food is transported from the source to sink organs mainly in the form of:", ["Proteins", "Lipids", "Sucrose", "Starch"], 2, "Phloem carries sucrose.", G2N, 42),
        q("The poisonous gas liberated when Chloroform (CHCl₃) is oxidized by air in the presence of light is :", ["Methyl Isocyanide", "Methyl Cyanide", "Hydrochloric acid",
                                                                                                                    "Phosgene"], 3, "Chloroform is stored in dark bottles for this reason.", G2N, 44),
        q("Based on the number of heart chambers, some of the animals have been categorized below. Identify the correct group/groups:\na. 2 chambered — Fish, Man, Frog\n"
          "b. 3 chambered — Frog, Salamander, Snake\nc. 4 chambered — Bird, Man, Gorilla\nd. 1 chambered — Tortoise, Fish, Toad",
          ["a group only", "a and c groups", "b and c groups", "d group only"], 2, "Fish 2, amphibians and most reptiles 3, birds and mammals 4.", G2N, 45),
        q("Identify the chronological steps involved in food digestion in human beings:\na. Absorption b. Digestion c. Assimilation d. Egestion e. Ingestion",
          ["a, c, d, b, e", "e, b, a, c, d", "d, a, b, c, e", "b, a, c, e, d"], 1, "Ingestion → digestion → absorption → assimilation → egestion.", G2N, 46),
        q("\"When a body is immersed fully or partially in a fluid, it experiences an upward force that is equal to the weight of the fluid displaced by it.\" This statement "
          "is associated with:", ["Archimedes Principle", "Newton's Gravitational Law", "Einstein's General Theory of Relativity", "Bernoulli's Principle"], 0,
          "Buoyancy.", G2N, 47),
        q("Consider the following statements:\nStatement I: Longer conducting wires have greater resistance than smaller conducting wires.\nStatement II: Resistance of a "
          "conducting wire is inversely proportional to its length.", AB, 2, "R = ρL/A – directly proportional to length.", G2N, 48),
        q("Match the following:\na. Frequency of Vibration b. Time period of Vibration c. Loudness of Sound d. Pitch of Sound\n"
          "i. Depends on Amplitude ii. Number of Vibrations in one second iii. Depends on frequency iv. Time taken for one complete vibration",
          ["a-iv, b-iii, c-ii, d-i", "a-i, b-ii, c-iii, d-iv", "a-iv, b-i, c-ii, d-iii", "a-ii, b-iv, c-i, d-iii"], 3, "Loudness – amplitude; pitch – frequency.", G2N, 49),
        q("A seasoned cricketer lowers his hands while catching a ball. The scientific reason behind this is:", ["to not drop a catch.",
                                                                                                                "to increase the time of application of retarding force.",
                                                                                                                "to decrease the time of application of retarding force.",
                                                                                                                "to attract an audience."], 1,
          "Same change of momentum over a longer time means a smaller force.", G2N, 50),
        q("Reason for water to be used as a coolant in automobiles is:", ["its specific heat capacity is high.", "its thermal conductivity is high.",
                                                                          "its specific heat capacity is low.", "its thermal conductivity is low."], 0, "It absorbs much heat per degree.", G2N, 51),
        q("An instrument used to measure Humidity is:", ["Barometer", "Anemometer", "Hygrometer", "Ceilometer"], 2, "Barometer – pressure; anemometer – wind speed.", G2N, 79),
        q("Consider the following statements.\n(a) Raw mangoes shrivel when pickled in salt water\n(b) Wilted flowers revive when placed in fresh water\n"
          "(c) Blood cells collapse when suspended in saline water\n(d) People taking a lot of salt or salty food experience water retention in tissue cells and intercellular spaces\n"
          "Select the correct reason(s) among the following.", ["Osmosis and Diffusion", "Osmosis and Sedimentation", "Osmosis only", "Absorption only"], 2,
          "All four are movements of water across membranes.", G3N, 2),
        q("Acceleration due to gravity on a planet is independent of", ["Mass of the planet", "Radius of the planet", "Density of the planet", "Velocity of the planet"], 3,
          "g = GM/R².", G3N, 4),
        q("____ is the micro-nutrients required in small quantity for plants growth.", ["Boron, Copper, Chlorine, Zinc", "Nitrogen, Potassium, Phosphorus, Iron",
                                                                                        "Phosphorus, Iron, Molybdenum, Zinc", "Potassium, Nitrogen, Zinc, Iron"], 0,
          "N, P, K are macronutrients.", G3N, 6),
        q("Match the following:\n(a) Chromium (b) Silver (c) Tin (d) Zinc\n(i) Electroplated on iron of food can (ii) Electroplated on iron of bridges and automobiles "
          "(iii) Electroplated on jewellery (iv) Electroplated on wheel rims and bath taps", ["a-i, b-ii, c-iii, d-iv", "a-iv, b-iii, c-i, d-ii", "a-iv, b-iii, c-ii, d-i",
                                                                                               "a-ii, b-iii, c-i, d-iv"], 1, "Zinc coating = galvanisation." + FIX, G3N, 9),
        q("When the male partner fails to inseminate the female or very low sperm count in the ejaculation, that leads to infertility. This can be corrected by using which "
          "one of the following techniques?", ["Tissue culture", "Cell culture", "Artificial insemination", "Cryopreservation"], 2, "AI places semen directly.", G3N, 10),
        q("Consider the process of heating water in a round bottom flask.\n(a) When water is heated, hot water sinks down and cold water rises up.\n"
          "(b) When water is heated, hot water rises up and cold water sinks down.\n(c) When water is heated, the cold water from the sides of flask moves down towards the source of heat.\n"
          "(d) When water is heated, the hot water from the sides of flask moves downwards towards the source of heat.\nThe correct statement/s is/are",
          ["Only statement (a)", "Statements (b), (c) and (d)", "Only (b) and (c)", "Only (b) and (d)"], 2, "Convection currents.", G3N, 12),
        q("Match the items given in List-I to item given in List-II.\n(Name of Mosquito/fly): (a) Anopheles (b) Aedes (c) Culex (d) Tsetse fly\n"
          "(Disease): (i) Dengue (ii) Elephantiasis (iii) African Sleeping Sickness (iv) Malaria", ["a-iii, b-ii, c-iv, d-i", "a-iv, b-iii, c-i, d-ii", "a-iv, b-i, c-ii, d-iii",
                                                                                                        "a-ii, b-iv, c-iii, d-i"], 2, "Culex spreads filariasis." + FIX, G3N, 15),
        q("In Sugar industry, in the manufacture of ethyl alcohol from molasses, the enzymes which convert sugar to alcohol are", ["Invertase and Lipase", "Amylase and Lipase",
                                                                                                                                  "Invertase and Zymase", "Zymase and Amylase"], 2,
          "Invertase: sucrose → glucose + fructose; zymase: glucose → ethanol.", G3N, 16),
        q("Which of the following properties can't change while a charged particle moves freely in a magnetic field?\n(a) Mass (b) Charge (c) Velocity (d) Momentum",
          ["(a) and (b) only", "(a) and (c) only", "(b) and (c) only", "(c) and (d) only"], 0, "The force changes the direction of velocity and momentum.", G3N, 17),
        q("Which of the following gases can be used for storage of fresh sample of an oil for a long time?", ["Helium and Nitrogen", "Carbon dioxide and Oxygen",
                                                                                                             "Nitrogen and Oxygen", "Carbon dioxide and Helium"], 0,
          "Inert gases prevent oxidation (rancidity).", G3N, 18),
        q("Working principle of electric fuse depends on", ["Magnetic effect of electric current", "Joule's heating effect of electric current",
                                                            "Chemical effect of electric current", "Mechanical effect of electric current"], 1, "The fuse wire melts.", G3N, 19),
        q("Read the following statements:\nStatement I: Golden rice is a genetically modified plant developed for enhanced Vitamin 'A' content.\n"
          "Statement II: The first transgenic cow, Rosie, produced human protein enriched with α-1-antitrypsin.",
          ["Statement I and Statement II are correct", "Statement I and Statement II are incorrect", "Statement I is correct and Statement II is incorrect",
           "Statement I is incorrect and Statement II is correct"], 2, "Rosie's milk had human α-lactalbumin; α-1-antitrypsin came from transgenic sheep.", G1H, 3),
        q("Match List-I with List-II:\n(a) Vitamin-A (b) Vitamin-D (c) Vitamin-E (d) Vitamin-B12\n(i) Cyanocobalamin (ii) Calciferol (iii) Tocopherol (iv) Retinol",
          ["a-iv, b-ii, c-iii, d-i", "a-iv, b-iii, c-ii, d-i", "a-iii, b-iv, c-i, d-ii", "a-i, b-iii, c-iv, d-ii"], 0, "Chemical names of vitamins." + FIX, G1H, 4),
        q("A 35% (v/v) solution of ethylene glycol is used in cars. The correct reason for this is", ["It is an antifreeze for cooling the engine", "As a fuel for combustion",
                                                                                                    "As a shining substance", "Helps to open airbag"], 0,
          "It lowers the freezing point of the coolant.", G1H, 9),
        q("The mixture which can be used to join railway tracks is", ["Copper oxide + Iron", "Carbon + Aluminium", "Iron(III) oxide + Aluminium", "Aluminium oxide + Iron"], 2,
          "Thermite reaction gives molten iron.", G1H, 14),
        q("A person A lifts a 10 kg object and keeps it at a height of 1 m in 3 seconds. Another person B lifts a 5 kg object and keeps it at a height of 2 m in 4 seconds. Then:",
          ["A has done more work than B", "B has done more work than A", "A has delivered more power than B", "B has delivered more power than A"], 2,
          "Both do 98 J of work; A takes less time (32.7 W vs 24.5 W).", G1H, 15),
        q("A copper cube (A) and an aluminium cube (B) of same volume are immersed completely in water. Then:", ["The buoyant force on cube (A) is greater",
                                                                                                                  "The buoyant force on cube (B) is greater",
                                                                                                                  "The buoyant force on both of them is same",
                                                                                                                  "The cube (B) will become weightless in water"], 2,
          "Buoyant force depends on the displaced volume.", G1H, 16),
        q("The minimum attainable temperature is", ["0 °C", "−20 °C", "273 °C", "−273.15 °C"], 3, "Absolute zero, 0 K.", G1H, 17),
        q("SI unit of the power of a lens is", ["Meter", "Dioptre", "Watt", "Volt"], 1, "P = 1/f (in metres).", G1H, 71),
        q("Two tin cans A and B are filled with equal amount of water. A is painted with black colour from outside and B with white colour. Both are kept in mid-day "
          "sunlight for half an hour. Identify the correct statement.", ["Temperature of water in tin can A is more because black colour absorbs more heat.",
                                                                          "Temperature of water in tin can B is more because white colour absorbs more heat.",
                                                                          "Temperature of water in tin can A is more because black colour reflects most of the heat",
                                                                          "Temperature of water in tin can B is more because white colour reflects most of the heat"], 0,
          "Black surfaces absorb radiation well.", G2H, 2),
        q("Tooth enamel made up of calcium hydroxyapatite is the hardest substance in the body. Teeth are corroded when pH of the mouth changes to", ["< 5.5", "~ 7", "> 7", "> 10"], 0,
          "Acids from sugars lower the pH below 5.5.", G2H, 4),
        q("Match List-I with List-II:\n(a) Heart (b) Lungs (c) Kidney (d) Skeletal system\n(i) Emphysema (ii) Tetany (iii) Angina (iv) Uremia",
          ["a-i, b-ii, c-iv, d-iii", "a-iii, b-i, c-iv, d-ii", "a-ii, b-iv, c-i, d-iii", "a-iv, b-ii, c-iii, d-i"], 1, "Organ disorders." + FIX, G2H, 6),
        q("Consider the following statements:\nStatement I: The colour of the scattered light depends on the size of the scattering particles.\n"
          "Statement II: The colour of clear sky is due to scattering of light.", ["Statement I is only correct", "Statement II is only correct",
                                                                                    "Both statement I and statement II are correct", "Both statement I and statement II are incorrect"], 2,
          "Small molecules scatter blue light most.", G2H, 7),
        q("Match the following:\n(a) Spherical Mirrors (b) Spherical lens (c) Glass Prism (d) Optical fibers\n(i) Refraction of light (ii) Total internal reflection "
          "(iii) Reflection of light (iv) Dispersion of light", ["a-i, b-ii, c-iii, d-iv", "a-iii, b-i, c-iv, d-ii", "a-iii, b-i, c-ii, d-iv", "a-iv, b-i, c-iii, d-ii"], 1,
          "Mirror – reflection; lens – refraction; prism – dispersion; fibre – TIR." + FIX, G2H, 8),
        q("From below mentioned disorders, identify how many of them are the disorders of muscular and skeletal system.\nMyasthenia gravis, Tetany, Arthritis, Gout, Osteoporosis",
          ["two only", "three only", "four only", "all five"], 3, "All are muscle or bone/joint disorders.", G2H, 10),
        q("Consider the following statements:\nFrom the Sun, heat comes to us by a process known as Radiation.\n(a) Radiation does not require any medium.\n"
          "(b) Radiation can take place whether a medium is present or not.\n(c) Radiation requires medium.", ["All statements are correct", "Only statements (a) and (c) are correct",
                                                                                                           "Only statements (a) and (b) are correct", "Only statements (b) and (c) are correct"], 2,
          "Radiation travels even through vacuum.", G2H, 12),
        q("When groundnut oil is heated with caustic soda solution, the products formed are", ["A soap and Glycerol", "A detergent and Glycerol", "Only soap", "Only detergent"], 0,
          "Saponification.", G2H, 14),
    ],
    "C": [
        q("Consider the following statements:\n(i) India is a monsoon-oriented country.\n(ii) South-West monsoon generally brings more rain to India.\n"
          "(iii) North-East monsoon rains are mainly confined to eastern and southern India.\n(iv) Monsoon is always a gamble in India.\nAmong the above statements, which is/are correct?",
          ["(i) only", "(i) and (ii)", "(ii) and (iii)", "(i), (ii), (iii) and (iv)"], 3, "All four are standard textbook statements.", G1N, 79),
        q("La Nina is suspected to have caused recent floods in Australia. How is La Nina different from El Nino?\n(i) La Nina is characterised by unusually cold ocean "
          "temperature in the equatorial Indian Ocean whereas El Nino is characterised by unusually warm ocean temperature in the equatorial Pacific Ocean.\n"
          "(ii) El Nino has an adverse effect on the South-West monsoon in India, but La Nina has no effect on the monsoon climate.\nWhich of the statements given above is/are correct?",
          ["Only (i)", "Only (ii)", "Neither (i) nor (ii)", "Both (i) and (ii)"], 2, "La Nina is a cold phase in the equatorial PACIFIC and usually strengthens India's monsoon.", G1N, 81),
        q("The Bay of Bengal experiences 4 times higher frequency of cyclones compared to Arabian Sea due to\n(a) Warm sea surface temperature\n"
          "(b) Inflow of cold water from rivers\n(c) Moisture-laden winds\n(d) Geographical shape\nIdentify the correct reasons.", ["(a) and (c)", "(a) and (d)", "(a), (c) and (d)",
                                                                                                                                 "(b), (c) and (d)"], 2,
          "River inflow does not cause cyclones.", G1N, 87),
        q("Which among the following is the correct sequence of ports found from north to south in Karnataka?", ["Karawara, Kumta, Ankola, Bhatkal", "Ankola, Karawara, Bhatkal, Kumta",
                                                                                                                 "Karawara, Bhatkal, Kumta, Ankola", "Karawara, Ankola, Kumta, Bhatkal"], 3,
          "All four are in Uttara Kannada, in that order from north.", G1N, 88),
        q("Identify the correct pairs from the following:\nDivisions – Taluk\na. Bengaluru – Channagiri\nb. Belagavi – Honnavara\nc. Kalaburagi – Maski\nd. Mysuru – Brahmavara",
          ["a and b are correct", "a, b and c are correct", "c and d are correct", "a, b, c and d are correct"], 3,
          "Channagiri (Davanagere), Honnavar (Uttara Kannada), Maski (Raichur), Brahmavar (Udupi).", G2N, 33),
        q("Match the following:\n(Lake) a. Fateh Sagar b. Nako Lake c. Khecheopalri Lake d. Bhimtal Lake\n(State) i. Himachal Pradesh ii. Uttarakhand iii. Rajasthan iv. Sikkim",
          ["a-iii, b-i, c-iv, d-ii", "a-iii, b-i, c-ii, d-iv", "a-iii, b-iv, c-i, d-ii", "a-ii, b-i, c-iv, d-iii"], 0, "Fateh Sagar is at Udaipur.", G2N, 71),
        q("Find the correct pairs from the following:\nIslands in Karnataka – District\na. Coconut Island – Udupi\nb. Anjediva Island – Dakshina Kannada\nc. Kurumgad Island – Uttara Kannada",
          ["Only a and b", "Only a and c", "Only b and c", "a, b and c"], 1, "Anjediva belongs to Goa.", G2N, 77),
        q("Select the correct order of clouds according to their altitude (highest first):\na. Cirrus clouds b. Altostratus clouds c. Cirrostratus clouds d. Nimbostratus clouds",
          ["a, c, b, d", "a, d, c, b", "d, b, c, a", "b, a, d, c"], 0, "High (cirrus, cirrostratus) → middle (altostratus) → low (nimbostratus).", G2N, 78),
        q("Consider the following statements regarding the tributaries of Gandak.\n(a) Kali Gandak is the tributary of Gandak.\n(b) Burhi Gandak is the tributary of Kali Gandak.",
          ["(a) only", "(b) only", "Both (a) and (b)", "Neither (a) nor (b)"], 0, "Burhi Gandak is a separate river that joins the Ganga.", G3N, 32),
        q("Read the statements with regard to the currents of Indian Ocean.\n(a) In the northern section of Indian Ocean, there is a reversal of ocean currents between summer and winter.\n"
          "(b) Indian Ocean being a half ocean, not fully extended in northern and southern hemisphere.\n(c) Indian Ocean is completely landlocked in the north.\n"
          "(d) There is no influence of monsoon winds on the currents.", ["(a) and (b)", "(a), (b) and (d)", "(a), (c) and (d)", "(a), (b) and (c)"], 3,
          "Monsoon winds reverse the northern currents.", G3N, 33),
        q("Exclusive Economic Zone (EEZ) of any country extends upto", ["100 Nautical Miles", "12 Nautical Miles", "200 Nautical Miles", "12 km"], 2,
          "Territorial sea 12 nm; EEZ 200 nm (UNCLOS).", G3N, 34),
        q("Consider the following statements with reference to Karnataka's Coastal Plains.\nStatement-I: It is narrower in the north and broader in the south.\n"
          "Statement-II: Western Ghats are nearer in the northern coastal plain shore and far in the southern coastal plain shore.", AB, 0,
          "The Ghats come close to the sea in Uttara Kannada.", G3N, 35),
        q("These are imaginary lines joining places having the same elevation above mean sea level.", ["Hachures", "Spot Heights", "Contours", "Benchmark"], 2, "Contour lines.", G3N, 37),
        q("Match List-I with List-II.\n(Isopleth maps): (a) Isohyets (b) Isobars (c) Isobaths (d) Isohalines\n(Specification): (i) Equal pressure (ii) Equal salinity "
          "(iii) Equal rainfall (iv) Equal depths", ["a-iii, b-i, c-iv, d-ii", "a-i, b-iii, c-iv, d-ii", "a-ii, b-i, c-iii, d-iv", "a-iv, b-ii, c-iii, d-i"], 0,
          "Hyet = rain, bar = pressure, bath = depth, hal = salt." + FIX, G3N, 38),
        q("Match List-I with List-II.\n(Countries): (a) Israel (b) Saudi Arabia (c) Iran (d) U.S.A.\n(Deserts): (i) Dasht-e-Lut (ii) Negev (iii) Mojave (iv) Nafud",
          ["a-i, b-iii, c-ii, d-iv", "a-iii, b-ii, c-i, d-iv", "a-ii, b-iv, c-i, d-iii", "a-i, b-iv, c-iii, d-ii"], 2, "Negev – Israel; Nafud – Saudi Arabia." + FIX, G3N, 39),
        q("Match the following:\n(Meteorological Station): (a) Amboli (b) Pulingoth (c) Pirmed (d) Cherrapunji\n(State): (i) Meghalaya (ii) Kerala (iii) Karnataka (iv) Maharashtra",
          ["a-i, b-ii, c-iii, d-iv", "a-ii, b-iii, c-iv, d-i", "a-iii, b-iv, c-ii, d-i", "a-iv, b-iii, c-ii, d-i"], 3, "High-rainfall stations." + FIX, G1H, 32),
        q("Write the salts found in ocean water in decreasing order.", ["Calcium sulphate, Calcium carbonate, Sodium chloride, Magnesium chloride",
                                                                        "Calcium sulphate, Calcium carbonate, Magnesium chloride, Sodium chloride",
                                                                        "Sodium chloride, Calcium carbonate, Magnesium chloride, Calcium sulphate",
                                                                        "Sodium chloride, Magnesium chloride, Calcium sulphate, Calcium carbonate"], 3,
          "NaCl ≈ 77.8%, MgCl₂ ≈ 10.9%, then sulphates; CaCO₃ is least.", G1H, 35),
        q("A High sea is a", ["Sea is at a higher elevation", "Area of international waters open to all nations", "Area of high conflicts between two nations",
                              "Sea which is having higher importance"], 1, "Beyond every country's EEZ.", G1H, 36),
        q("Identify the wrongly matched pair/pairs.\nName of the Garden – Location\n(a) Amrit Udyan – New Delhi\n(b) Shalimar Bagh – Srinagar\n(c) Lodhi Garden – Agra\n"
          "(d) Acharya Jagadish Chandra Bose Indian Botanic Garden – Cuttack", ["(b) and (c)", "(a) and (c)", "(c) and (d)", "(d) only"], 2,
          "Lodhi Garden is in Delhi; the Botanic Garden is at Howrah.", G1H, 84),
        q("Match List-I with List-II:\n(Countries): (a) Iraq (b) Iran (c) Libya (d) Myanmar\n(Petroleum production areas): (i) Kirkuk (ii) Naft-i-Shah (iii) Zelten (iv) Singu",
          ["a-i, b-ii, c-iii, d-iv", "a-iv, b-ii, c-iii, d-i", "a-i, b-iii, c-ii, d-iv", "a-iv, b-iii, c-ii, d-i"], 0, "Each oilfield with its country." + FIX, G2H, 32),
        q("Which of the following river system is good example for Dendritic River pattern in Karnataka?", ["Nandidurga River System", "Manjra-Karanja River System",
                                                                                                            "Kali River System", "Cauvery River System"], 3,
          "Like a tree with branches – the Cauvery and its many tributaries.", G2H, 33),
        q("Match the following:\n(Wettest place in Karnataka): (a) Amagaon (b) Mundrote (c) Hulikal (d) Agumbe\n(Taluk): (i) Khanapur (ii) Thirthahalli (iii) Hosanagara (iv) Madikeri",
          ["a-i, b-ii, c-iii, d-iv", "a-ii, b-iii, c-i, d-iv", "a-i, b-iv, c-iii, d-ii", "a-iii, b-iv, c-i, d-ii"], 2, "Amagaon (Belagavi), Mundrote (Kodagu)." + FIX, G2H, 34),
        q("Which among the below is the correct order of estuaries found from north to south in Karnataka?", ["Tadadi – Sita – Udyavara – Gurupura", "Tadadi – Udyavara – Sita – Gurupura",
                                                                                                              "Sita – Tadadi – Gurupura – Udyavara", "Sita – Tadadi – Udyavara – Gurupura"], 0,
          "Tadadi (Uttara Kannada), Sita and Udyavara (Udupi), Gurupura (Mangaluru).", G2H, 35),
        q("Match the following.\n(Winds): (a) Berg (b) Bora (c) Santa Ana (d) Loo\n(Countries): (i) India (ii) North America (iii) Italy (iv) South Africa",
          ["a-i, b-iii, c-ii, d-iv", "a-iv, b-iii, c-ii, d-i", "a-iii, b-ii, c-iv, d-i", "a-ii, b-iii, c-iv, d-i"], 1, "Local winds." + FIX, G2H, 36),
        q("Which of the following statements are correct with reference to tide?\n(a) The moon's gravitational pull to greater extent and to a lesser extent the sun's "
          "gravitational pulls are the major causes for the occurrence of tides.\n(b) The highest tides in the world occur in the Bay of Fundy in Nova Scotia, Canada.\n"
          "(c) Tides are helpful in desilting the sediments and in removing polluted water.\n(d) When the tide is channelled between islands or into bays and estuaries, they are called tidal currents.",
          ["(a) and (b) only correct", "(a) and (c) only correct", "(a), (c) and (d) are correct", "(a), (b), (c) and (d) are correct"], 3, "NCERT Class 11 statements.", G2H, 37),
        q("Which of the following sequence is correct from west to east related to Indian lakes?", ["Sambhar lake, Wular lake, Pulicat lake, Kolleru lake",
                                                                                                    "Wular lake, Sambhar lake, Pulicat lake, Kolleru lake",
                                                                                                    "Sambhar lake, Wular lake, Kolleru lake, Pulicat lake",
                                                                                                    "Wular lake, Sambhar lake, Kolleru lake, Pulicat lake"], 1,
          "Longitudes: Wular ≈ 74.6°E, Sambhar ≈ 75.1°E, Pulicat ≈ 80.2°E, Kolleru ≈ 81.2°E.", G2H, 40),
    ],
    "D": [
        q("Which of the following indicators of poverty under living standard dimension of Multidimensional Poverty Index are included?\n(a) Electricity\n(b) Public Expenditure\n"
          "(c) Housing\n(d) Sanitation", ["(a), (b) and (c)", "(b) only", "(a), (b), (c) and (d)", "(a), (c) and (d)"], 3,
          "Living-standard indicators: cooking fuel, sanitation, drinking water, electricity, housing, assets (and bank account in India).", G1N, 17),
        q("Which of the following expenditure items is/are considered as Revenue Expenditure?\n(a) Expenditure on General Administration\n(b) Defence Personnel Pension\n"
          "(c) Interest Payments\n(d) National Highways Construction", ["(a) and (b)", "(a), (b) and (c)", "(a), (b), (c) and (d)", "(d) only"], 1,
          "Building highways creates assets – capital expenditure.", G1N, 18),
        q("The Fiscal Responsibility and Budget Management (FRBM) Act of India became effective from", ["2004", "2001", "1991", "2005"], 0, "Enacted 2003, in force from July 2004.", G1N, 21),
        q("Which of the following is NOT a Non-Banking Financial Intermediary?", ["SIDBI", "SEBI", "SFCs", "GIC"], 1, "SEBI is the market regulator.", G1N, 22),
        q("Who coined the term 'Green Revolution' for the first time?", ["M.S. Swaminathan", "M.S. Randhawa", "William S. Gaud", "Norman Borlaug"], 2, "USAID's William Gaud, 1968.", G1N, 78),
        q("Consider the following formulas regarding NNP:\n(a) NNP = GNP − Depreciation\n(b) NNP = GDP + Income from Abroad − Depreciation\n(c) NNP = GDP − Depreciation",
          ["(a) and (b) are correct", "(a) and (c) are correct", "(b) and (c) are correct", "(a), (b) and (c) are correct"], 0, "GDP − depreciation is NDP.", G3N, 54),
        q("The higher value of Gender Inequality Index (GII) indicates", ["Less disparities between females and males and more loss to human development",
                                                                          "Less disparities between females and males and less loss to human development",
                                                                          "More disparities between females and males and more loss to human development",
                                                                          "More disparities between females and males and less loss to human development"], 2, "GII runs from 0 to 1.", G3N, 55),
        q("Which of the following items are not included in the estimation of National Income?\n(a) Production for self consumption\n(b) Services of housewives\n"
          "(c) Black market income\n(d) Dearness allowance of employees", ["(a) and (b)", "(b), (c) and (d)", "(b) and (c)", "(a), (b) and (c)"], 2,
          "Own-account production and DA are included.", G1H, 40),
        q("The Central Statistical Office of India measures Gross Value Added as", ["Total output minus Total Intermediate Consumption", "Total output plus Total Intermediate Consumption",
                                                                                    "Total output minus Gross Mixed Income", "Total output plus Gross Mixed Income"], 0,
          "GVA = output − intermediate consumption.", G1H, 70),
        q("Which is the correct chronological order in the establishment of the committees constituted to measure the poverty in India?\n(a) V.M. Dandekar & Neelakantha Rath "
          "committee\n(b) Rangarajan committee\n(c) D.T. Lakdawala committee\n(d) Suresh Tendulkar committee", ["(a), (d), (b), (c)", "(d), (c), (b), (a)", "(a), (c), (b), (d)",
                                                                                                              "(a), (c), (d), (b)"], 3, "1971, 1993, 2009, 2014.", G2H, 28),
        q("Consider the following rows related to the merger of commercial banks.\n(a) Syndicate Bank – Canara Bank\n(b) Corporation Bank – Union Bank\n"
          "(c) Andhra Bank – Punjab National Bank\n(d) United Bank of India – Indian Bank\nWhich of the above row/s is/are correct?",
          ["Only (a)", "Only (a) and (b)", "Only (a), (b) and (c)", "All (a), (b), (c) and (d)"], 1, "2020: Andhra Bank → Union Bank; United Bank → PNB.", G2H, 69),
        q("Which of the following are the functions of NITI Aayog?\n(a) Vision and scenario planning\n(b) Centralised planning\n(c) Capacity Building",
          ["(a) and (b) are correct", "(b) and (c) are correct", "(a) and (c) are correct", "(a), (b) and (c) are correct"], 2, "NITI replaced top-down planning.", G2H, 71),
        q("Gender Inequality Index measures gender inequality to which of the following?", ["Literacy, Empowerment and Economic status",
                                                                                            "Reproductive Health, Empowerment and Economic status",
                                                                                            "Standard of living, literacy and social status", "Education, standard of living and Empowerment"], 1,
          "Three dimensions of UNDP's GII.", G2H, 74),
        q("As per the Union Budget 2025-26, arrange the following revenue sources in decreasing order of their contribution.\n(a) GST (b) Corporate tax (c) Income tax (d) Excise duty",
          ["(c), (a), (b), (d)", "(a), (b), (c), (d)", "(a), (c), (b), (d)", "(c), (b), (a), (d)"], 0, "Rupee comes from: income tax 22 p, GST 18 p, corporation tax 17 p, excise 5 p.", G2H, 78),
    ],
    "E": [
        q("What is the main purpose of the \"SUCHI YOJANE\"?", ["Distribution of free sanitary pads to school girls aged 10-18 years",
                                                                "Distribution of free sanitary pads to school girls aged 10-16 years",
                                                                "Sale of sanitary pads to school girls aged 10-18 years", "Sale of sanitary pads to school girls aged 10-16 years"], 0,
          "Karnataka's Suchi scheme for adolescent girls.", G2H, 80),
    ],
    "F": [
        q("Consider the following statements regarding the causes of Carnatic Wars.\n(a) Austrian succession war was a cause for First Carnatic War.\n"
          "(b) Conflict between Nasir Jung and Muzaffar Jung for Hyderabad throne was a cause for Second Carnatic War.\n"
          "(c) Defeat of Anwaruddin by Dupleix in the battle of Adyar was a cause for Second Carnatic War.\n(d) Seven years war was a cause for Third Carnatic War.",
          ["(b), (c) and (d) are correct", "(a), (c) and (d) are correct", "(a), (b) and (d) are correct", "(a), (b) and (c) are correct"], 2,
          "Adyar (1746) belongs to the First Carnatic War.", G1N, 3),
        q("Consider the following statements with reference to Ancient Scripts of India.\n(a) Brahmi was written from left to right.\n(b) Kharoshti was written from right to left.\n"
          "(c) Aramaic was written from left to right.\nIdentify the correct statements.", ["(a) and (b) are only correct", "(b) and (c) are only correct", "(a) and (c) are only correct",
                                                                                          "(a), (b) and (c) are correct"], 0, "Aramaic, like Kharosthi, ran right to left.", G1N, 6),
        q("Consider the following statements regarding Sepoy Mutinies against British.\nStatement-I: Sepoys of 47 Regiment of Barrackpore revolted against British in 1824.\n"
          "Statement-II: British ordered 47th Regiment to march to Burma for the First Anglo-Burmese War", AB, 0,
          "Sea travel to Burma was against their caste beliefs.", G1N, 7),
        q("Devi Chaudhurani who was picturised in Bankim Chandra Chatterjee's historical novel 'Devi Chaudhurani' was the leader of which of the following rebellion?",
          ["Ahom rebellion", "Savantavadi rebellion", "Paika rebellion", "Fakir-Sanyasi rebellion"], 3, "Bengal, late 18th century.", G1N, 8),
        q("Which Pallava ruler married Shanka, the daughter of Rashtrakuta Amoghavarsha?", ["Narasimhavarman I", "Parameshwaravarman II", "Nandivarman III", "Aparajithavarman"], 2,
          "A Pallava–Rashtrakuta marriage alliance.", G1N, 9),
        q("Who among the following is regarded as the pioneer of Irrigation in colonial India?", ["Montgomery Martin", "Arthur Cotton", "Lt. Col. Sir Frederick Stanley",
                                                                                                    "Sir M. Visvesvaraya"], 1, "Godavari and Krishna anicuts.", G1N, 36),
        q("Consider the following statements.\n(i) Pallava temples are the earliest temples of Dravidian style.\n(ii) They are renowned for the rock-cut temples.\n"
          "(iii) Pallava architecture influenced the architecture of the far east.\n(iv) Pallavas learnt the rock-cut art from Sri Lanka.\nWhich of the above statements are correct?",
          ["(i), (ii), (iii) and (iv)", "(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)"], 1, "Rock-cut art was not learnt from Sri Lanka." + FIX, G1N, 37),
        q("Identify the correct pairs among the following (Rigvedic names of rivers):\n(a) Ravi – Parushni\n(b) Chenab – Asikni\n(c) Jhelum – Vitasta\n(d) Sutlej – Vipasa",
          ["(a) and (d) only", "(a) and (c) only", "(b) and (d) only", "(a), (b) and (c) only"], 3, "Vipasa is the Beas; the Sutlej is Shutudri.", G1N, 42),
        q("Consider the following statements regarding Bengal:\nStatement I: In 1765, Robert Clive introduced the Dual Government System.\n"
          "Statement II: The British were given the Diwani rights to collect revenue and the Nizam was given the responsibility of administration, law and order.", AB, 2,
          "The Nawab (Nizamat), not the Nizam, kept administration.", G2N, 17),
        q("In which of the following places Stupa was not built?", ["Bharhut", "Sanchi", "Sarnath", "Karle"], 3, "Karle is famous for its rock-cut chaitya hall.", G2N, 19),
        q("Match the Republics during 6th century BCE with their ruling clans:\n(Republic): a. Vaishali b. Pava c. Pippalivana d. Mithila\n(Clan): i. Moriya ii. Lichchavi "
          "iii. Videha iv. Mallas", ["a-i, b-iii, c-ii, d-iv", "a-ii, b-iv, c-i, d-iii", "a-ii, b-i, c-iv, d-iii", "a-i, b-ii, c-iii, d-iv"], 1, "Mallas of Pava; Moriyas of Pippalivana.", G2N, 20),
        q("Identify the two works of Bhasa:\na. Dutavakyam b. Hayagrivavadha c. Ravanavadha d. Charudattam", ["a and b", "a and d", "a and c", "b and d"], 1,
          "Bhasa's plays include Dutavakyam and Charudattam.", G2N, 21),
        q("Who was/were the commander(s) of British army during the Fourth Anglo-Mysore War?\na. General Stuart b. Arthur Wellesley c. General Artherton d. Colonel Goddard e. General Harris",
          ["a and e", "Only b", "a and d", "b and e"], 0, "General Harris led the Madras army, General Stuart the Bombay army (1799).", G2N, 22),
        q("Consider the following statements related to Keladi Nayakas:\n(A) Rani Chennamma refused to give shelter to Maratha Chatrapati Rajaram who had escaped from the Mughals.\n"
          "(B) Venkatappa Nayaka defeated the 'Queen of Pepper' Channabhairadevi of Gerusoppe and annexed her kingdom.\n(C) All of them were Vaishnavites.",
          ["(A) only", "(B) only", "(A) and (C) only", "(B) and (C) only"], 1, "Chennamma sheltered Rajaram; the Nayakas were Veerashaivas.", G3N, 20),
        q("Meadows Taylor in his work entitled 'A Noble Queen' gives the details of which of the following queen?", ["Chand Bibi", "Channabyradevi", "Rani Durgavathi", "Ahalya Bai"], 0,
          "Chand Bibi of Ahmadnagar.", G3N, 21),
        q("Identify the incorrect statement regarding the Bhakti Movement in South India.\n(a) Nayanars and Alvars started the Bhakti Movement in South India.\n"
          "(b) To attain Moksha Nayanars propounded the worship of Shiva and Alvars the worship of Vishnu.\n(c) In the Bhakti Movement at South India only the upper class were identified.\n"
          "(d) 63 Nayanars & 12 Alvars spread the Bhakti Movement in South India.", ["(a) and (b) are incorrect", "(d) only is incorrect", "(b) and (d) are incorrect",
                                                                                      "(c) only is incorrect"], 3, "Saints came from all castes.", G3N, 25),
        q("Arrange the following in chronological order.\n(a) Paika Rebellion (b) Kuka movement (c) Revolt of Dondia Wagha (d) Diwan Velu Thampi's Revolt",
          ["(c), (d), (a), (b)", "(a), (b), (c), (d)", "(a), (c), (d), (b)", "(c), (a), (b), (d)"], 0, "1800, 1809, 1817, 1870s.", G3N, 28),
        q("Identify the correctly matched pairs.\n(a) Portuguese – Santhome (b) Dutch – Karaikal (c) Dane – Tranquebar (d) French – Mahe",
          ["(a), (b), (c) and (d) are correct", "(b) and (c) are correct", "(b) and (d) are correct", "(a), (c) and (d) are correct"], 3, "Karaikal was French.", G3N, 29),
        q("Which of the following statements are correct regarding Vijayanagara trade?\n(a) Spices like pepper, cloves and cardamom etc. were exported by them.\n"
          "(b) Bhatkal, Honnavara and Mangaluru were the important ports during Vijayanagara period.\n(c) Gold coins only were used as the medium of exchange.\n"
          "(d) Traders from Arab, China and Portugal had trade relation with the Vijayanagara Empire.", ["(a), (c) and (d) are correct", "(a), (b) and (d) are correct",
                                                                                                          "(a), (b), (c) and (d) are correct", "(b), (c) and (d) are correct"], 1,
          "Silver and copper coins were also used.", G3N, 31),
        q("Consider the following statements:\n(a) The Indus Civilization had been extended 12,99,600 sq.km\n(b) The Indus Civilization was smaller than Egypt, Mesopotamian Civilizations.",
          ["(a) is incorrect and (b) is also incorrect", "(a) is correct and (b) is incorrect", "(a) is incorrect and (b) is correct", "(a) is correct and (b) is also correct"], 1,
          "It was larger than Egypt and Mesopotamia.", G1H, 42),
        q("Consider the following:\n(a) Anand Mahal (b) Malik Jahan Mosque (c) Asar Mahal\nWhich of the above monuments are associated with Ibrahim Adil Shah II?",
          ["(a) only", "(b) only", "(a) and (b)", "(b) and (c)"], 2, "Asar Mahal was built by Muhammad Adil Shah (1646).", G1H, 44),
        q("Find the correct pairs of the Gupta temples.\n(a) The Dashavatara temple – Deogarh\n(b) The Vishnu temple – Jabalpur (Tigawa)\n(c) The Parvati temple – Sanchi\n"
          "(d) The Shiva temple – Bhumara", ["(a) and (b) are correct", "(a), (b) and (d) are correct", "(b) and (c) are correct", "(c) and (d) are correct"], 1,
          "The Parvati temple is at Nachna.", G1H, 54),
        q("Identify the correct pair from the following:\n(a) Indra – Purandara (b) Dasyu – Gavishti (c) Sarasvati – Naditama (d) Ayas – Sahasra",
          ["(a) and (d) are correct", "(b) and (c) are correct", "(a) and (c) are correct", "(c) and (d) are correct"], 2,
          "Indra 'destroyer of forts'; Sarasvati 'best of rivers'; Gavishti means war (search for cows).", G1H, 56),
        q("The vast mounds of Harappa were first reported in 1827 by", ["Charles Masson", "Alexander Cunningham", "James Prinsep", "Richard Strachey"], 0,
          "Masson visited the site in 1826–27.", G1H, 57),
        q("Consider the following statements with reference to Portuguese.\n(a) They maintained friendly relations with Vijayanagara Empire.\n(b) They followed the policy of "
          "religious intolerance.\n(c) Albuquerque conquered Ormuz from Persians.\n(d) They had no trade settlements in Bengal and Coromandel coast.",
          ["(a), (b), (c) and (d) are correct", "(a) and (b) are correct", "(a), (b) and (c) are correct", "(b), (c) and (d) are correct"], 2,
          "They had Hooghly and San Thome.", G2H, 17),
        q("Which among the following Tribal Rebellion is called as 'Ulgulan'?", ["Santhal Rebellion", "Naga Rebellion", "Kol's Rebellion", "Munda Rebellion"], 3,
          "Birsa Munda's 'great tumult' (1899–1900).", G2H, 18),
        q("Consider the following and select the incorrect statement/s regarding Sikandar Lodi.\n(a) He constructed Agra city.\n(b) Introduced 'Gaz-i-Sikandari' land measurement.\n"
          "(c) Composed Persian poems by his pen-name 'Gulrukhi'.\n(d) He was successor of Ibrahim Lodi.", ["(a) and (b) are incorrect", "(b) and (c) are incorrect",
                                                                                                           "(c) and (d) are incorrect", "(d) only is incorrect"], 3,
          "Ibrahim Lodi succeeded Sikandar.", G2H, 22),
        q("Select the correct statement/statements about Gautamiputra Satakarni.\n(a) He claimed the title of 'Eka Brahmana' or 'Vishishta Brahmana'.\n"
          "(b) He claimed himself as \"destroyer of the pride of Kshatriyas\"", ["Only (a) is correct", "Only (b) is correct", "Both (a) and (b) are wrong", "Both (a) and (b) are correct"], 3,
          "Both titles are in the Nasik inscription of his mother.", G2H, 26),
        q("Match List-I (Tirthankaras) with List-II (Symbols)\n(a) Ajitnath (b) Sambhavnath (c) Padmaprabha (d) Abhinandanath\n(i) Horse (ii) Monkey (iii) Elephant (iv) Red Lotus",
          ["a-i, b-ii, c-iii, d-iv", "a-iii, b-i, c-iv, d-ii", "a-iv, b-iii, c-ii, d-i", "a-i, b-iv, c-iii, d-ii"], 1, "Lanchhanas of the 2nd to 6th Tirthankaras.", G2H, 77),
        q("Match the following:\n(Delhi Sultans): (a) Qutbuddin Aibak (b) Iltutmish (c) Ghiasuddin Tughlaq (d) Ibrahim Lodi\n(Cause of death): (i) Due to illness (ii) Fell from "
          "his horse while playing Chaugan (iii) Killed in the battlefield (iv) Collapsed wooden pavilion", ["a-i, b-iii, c-ii, d-iv", "a-iv, b-i, c-iii, d-ii", "a-ii, b-i, c-iv, d-iii",
                                                                                                                "a-i, b-iv, c-iii, d-ii"], 2, "Ibrahim Lodi died at Panipat (1526)." + FIX, G2H, 95),
        q("The 'Begar' system was one of the major causes for Tribal Rebellion. Here 'Begar' means", ["Begging", "Unpaid Labour", "Poverty", "Imposition of heavy Land Revenue"], 1,
          "Forced labour without wages.", G2H, 99),
    ],
    "G": [
        q("Which among the following Tribunal/Commission settles disputes related to recruitment and all service matters of Central Government employees?",
          ["Central Administrative Tribunal", "Union Public Service Commission", "State Administrative Tribunal", "Securities Appellate Tribunal"], 0, "Article 323A.", G2N, 1),
        q("Consider the following statements regarding secularism in the Constitution of India:\nStatement I: The term 'Secular' was added to the Preamble by the 42nd "
          "Constitutional Amendment Act of 1976.\nStatement II: Articles 25-28, guaranteeing freedom of religion, mandate India to be a secular state.", AB, 1,
          "Both are true, but the 1976 insertion is not explained by Articles 25–28.", G2N, 3),
        q("Consider the following statements with regard to the Government of India Act, 1935:\na. The Act divided the powers between the Centre and the Provinces.\n"
          "b. The Act provided for the adoption of diarchy at the Centre.\nc. The Act introduced Universal Adult Franchise.\nd. The Act provided for the establishment of the Reserve Bank of India.",
          ["a, b and c", "a, b and d", "a, c and d", "b, c and d"], 1, "Franchise stayed limited (about 10%).", G2N, 12),
        q("Consider the following statements:\n(a) A Bill passed by the Parliament can become an Act only if it receives the assent of the President.\n(b) President may withhold "
          "his/her assent to the Bill\n(c) He/She can reject the Bill\n(d) He/She may give his/her assent to the Bill", ["(a), (b) and (c) are correct", "(a), (b) and (d) are correct",
                                                                                                                         "(b), (c) and (d) are correct", "(c), (d) and (a) are correct"], 1,
          "Article 111: assent, withhold, or return (non-money bills).", G3N, 47),
        q("Consider the following statements:\n(i) Youth parliament was started to acquaint the younger generations with practices and procedures of Parliament.\n"
          "(ii) To imbibe the spirit of discipline and tolerance in the minds of youth.\n(iii) To inculcate in the student community the basic values of democracy.\n"
          "(iv) The scheme of youth parliament started on the recommendation of Fourth All India Whips Conference.", ["(i), (ii) and (iii) are correct", "(i), (ii), (iii) and (iv) are correct",
                                                                                                                     "(ii), (iii) and (iv) are correct", "(ii) and (iii) are correct"], 1,
          "Ministry of Parliamentary Affairs scheme.", G3N, 48),
        q("The first President of National Human Rights Commission of India.", ["Justice H.L. Dattu", "Justice Ranganath Misra", "Justice A.S. Anand", "Justice Arun Mishra"], 1,
          "NHRC was set up in 1993.", G3N, 51),
        q("\"Collegium System\" is related with", ["Judicial Review", "Judicial Activism", "Judicial Appointment", "Judicial Powers"], 2,
          "Appointment and transfer of judges.", G3N, 96),
        q("In which of the following periods, there existed a coalition government at the centre?", ["1952 - 57", "1977 - 79", "1980 - 84", "1984 - 89"], 1,
          "The Janata government of 1977–79.", G1H, 68),
        q("What is the primary role of civil society in democratic governance?", ["Implementing government programmes", "Holds the state accountable",
                                                                                  "Replacing elected representatives in delivering services",
                                                                                  "Framing economic policies independent of the legislature"], 1, "Watchdog role.", G1H, 99),
        q("Consider the following statements.\nStatement-I: The Chairman and members of State Public Service Commission are appointed by the Governor\n"
          "Statement-II: The Chairman and members of State Public Service Commission are removed by the Governor", ["Both statements I and II are correct",
                                                                                                                    "Both statements I and II are incorrect",
                                                                                                                    "Statement-I is correct but statement-II is incorrect",
                                                                                                                    "Statement-II is correct but statement-I is incorrect"], 2,
          "Only the President can remove them (Article 317).", G2H, 44),
        q("Consider the following statements related to Attorney General of India:\n(i) He can argue in favour of litigations filed against the Union of India.\n"
          "(ii) He can attend any court of India for the discharge of his duty.\n(iii) He has the power to participate in the discussions of both the Houses of Parliament.\n"
          "(iv) He has the power to cast vote in the sessions of Parliament.", ["(i) and (ii) correct", "(ii) and (iii) correct", "(i), (ii) and (iv) correct",
                                                                                "(i), (ii), (iii) and (iv) correct"], 1, "Article 88: speaks but cannot vote.", G2H, 47),
    ],
    "H": [
        q("When the rate of interest in a bank is reduced from 5% to 4%, a man deposits Rs. 2000 more and his annual income remains the same. The original deposit is",
          ["Rs. 7500", "Rs. 8000", "Rs. 8500", "Rs. 7000"], 1, "0.05x = 0.04(x + 2000) → x = 8000.", G1N, 46),
        q("A small cat can catch 12 rats in 6 minutes and a big cat can catch 6 rats in 12 minutes. If there are sufficient rats, how many rats can both the cats catch "
          "together in 20 minutes?", ["8", "40", "50", "60"], 2, "2 + 0.5 = 2.5 rats per minute × 20.", G1N, 47),
        q("The perimeter of two squares are 20 cm and 48 cm. The perimeter of a third square whose area is the sum of the area of the two squares is", ["52", "42", "13", "12"], 0,
          "Sides 5 and 12 → 25 + 144 = 169 → side 13.", G1N, 54),
        q("The product of two numbers is 4107. If the H.C.F of these numbers is 37, then the greatest number is", ["101", "107", "111", "185"], 2,
          "4107 = 37 × 111 = 37² × 3.", G1N, 57),
        q("A man bought some oranges at Rs. 30 per dozen and bought the same number of oranges at Rs. 25 per dozen. He sold these oranges at Rs. 32 per dozen and gained Rs. 270. "
          "The total number of oranges bought by him was:", ["60 dozen", "45 dozen", "50 dozen", "70 dozen"], 0, "Average cost 27.5, profit 4.5 per dozen; 270 / 4.5.", G2N, 63),
        q("If the angles of a triangle are in the ratio 3 : 2 : 7, then the angles are:", ["45°, 30°, 105°", "42°, 28°, 98°", "48°, 32°, 112°", "60°, 40°, 80°"], 0,
          "180 / 12 = 15.", G2N, 66),
        q("A fitness app shows that a user walked, on average of 10,000 steps per day over a week. If on the last 3 days, the step counts were 9000, 12,000 and 10,400 "
          "respectively, what is the average number of steps for the first 4 days of the week?", ["9600", "9500", "9560", "9650"], 3, "(70000 − 31400) / 4.", G2N, 68),
        q("A paint company mixes red, blue and green paints in the ratio 1 : 2 : 3 to make a wall coating. If 60 litres of the mixture is prepared, how much red and blue "
          "paint is used together?", ["10 litres", "15 litres", "20 litres", "30 litres"], 3, "3/6 of 60.", G2N, 69),
        q("The least number which when divided by 5, 7 and 9 leaves a remainder 3, but when divided by 6 leaves no remainder is:", ["138", "318", "633", "948"], 1,
          "315k + 3 divisible by 6 → k = 1.", G3N, 65),
        q("A school receives 600 books for its Book Bank to be distributed to Mathematics, English and Social studies sections in the ratio 3:2:1. Later 10% of Mathematics and "
          "25% of English books were found damaged. If the undamaged total was 460, how many social studies books were in good condition?", ["50", "40", "30", "20"], 1,
          "Maths 300 − 30, English 200 − 50 → 420; 460 − 420.", G3N, 68),
        q("The average weight of 6 patients in a hospital ward is 72 kg. A new patient is admitted and now the average weight becomes 68 kg. Find the weight of the new patient in kg.",
          ["54", "44", "45", "55"], 1, "7 × 68 − 6 × 72.", G3N, 69),
        q("Chaitra saves Rs. 2 per day in her piggy bank. After 100 days she puts her total savings amount in a bank at 4% simple interest annually. How much interest does "
          "she earn in 2 years?", ["10", "16", "12", "20"], 1, "200 × 4 × 2 / 100.", G3N, 72),
        q("Ratio of curved surface area to total surface area of a cylinder is 11 : 18. Also area of its circular end is 616 cm². Then the volume of the cylinder is",
          ["11576 cm³", "13552 cm³", "12785 cm³", "16415 cm³"], 1, "h : (r + h) = 11 : 18 → r = 14, h = 22; V = 616 × 22.", G3N, 73),
        q("There are some cows and ducks. The total number of legs is equal to 14 more than twice the number of heads. The number of cows is", ["5", "6", "7", "8"], 2,
          "Each cow adds 2 extra legs: 14 / 2.", G2H, 56),
        q("At a music concert, 30% of audience were women. Of the rest, 60% were men and the rest were children. If there were 1400 children, then what is the total number of audience?",
          ["5000", "4000", "3000", "2000"], 0, "Children = 40% of 70% = 28%.", G2H, 61),
        q("Digit 1 is occurring 136 times on writing all of the page numbers of a book. What will be the total number of pages in the book? (Book's page number starts from 1)",
          ["194", "195", "200", "295"], 1, "1–99 use 20 ones; 100–195 use 116.", G2H, 62),
        q("A shopkeeper sells an article at Rs 96 and gets x% of profit. However, when he sells it at Rs 68 he loses (x − 5)% of cost price. What is the original cost of the article?",
          ["76", "80", "84", "88"], 1, "96 + 68 = C(2 + 0.05) → C = 80.", G2H, 63),
        q("P, Q and R can complete a job in 8 days. If Q does half what P and R together do in 1 day, then in how many days can Q alone do the half work?", ["7", "12", "10", "9"], 1,
          "Q = 1/3 of the total rate = 1/24 per day; half the work takes 12 days.", G2H, 100),
    ],
    "I": [
        q("The Nagar Rebellion resulted in", ["Accession of Krishnaraja Wadiyar III", "Dethronement of Krishnaraja Wadiyar III", "Appointment of Cubbon as Commissioner",
                                              "The Subsidiary Treaty"], 1, "In 1831 the British took over Mysore's administration.", G1N, 41),
        q("Correctly match the Organisations in List I with the Centres in List II:\na. Karnataka Sabha b. Justice Party c. Satyashodhak Samaj d. Mazzini Club\n"
          "i. Pune ii. Belgaum iii. Dharwad iv. Madras", ["a-i, b-ii, c-iii, d-iv", "a-ii, b-iii, c-i, d-iv", "a-iii, b-iv, c-i, d-ii", "a-ii, b-i, c-iv, d-iii"], 2,
          "Karnataka Sabha – Dharwad (1890).", G2N, 24),
        q("Arrange the following in chronological order:\na. Mysore Infant Marriage Act b. Gold Mining in Kolar c. Mysore Civil Service Examinations "
          "d. Shivanasamudra Hydroelectric Power Project", ["a, b, d, c", "b, c, a, d", "d, c, a, b", "a, d, b, c"], 1, "1880, 1891, 1894, 1902.", G2N, 27),
        q("Identify which is not the feature of Hoysala Architecture style?", ["Star shaped base", "Used Red sandstone", "Navaranga has Bhuvaneshwari in the ceiling",
                                                                              "The pillared hall has pierced windows"], 1, "Hoysalas used soapstone (chloritic schist).", G3N, 23),
        q("Consider the following statements regarding the unification of Karnataka.\n(a) Dhar Committee supported state re-organization.\n(b) J.V.P. Committee was in favour "
          "of creation of Andhra state.\n(c) Fazal Ali Commission was also called as state re-organization commission.\n(d) Fazal Ali Commission was a three-member commission.",
          ["(a), (b) and (c) are correct", "(b), (c) and (d) are correct", "(a), (b) and (d) are correct", "Only (c) and (d) are correct"], 1,
          "The Dhar Commission (1948) advised against linguistic states.", G3N, 26),
        q("Match the following:\n(Musicians): (a) Kadri Gopalnath (b) Rafique Khan (c) S. Ballesh (d) Mysore Manjunath\n(Instruments): (i) Shehnai (ii) Violin (iii) Sitar (iv) Saxophone",
          ["a-iv, b-ii, c-iii, d-i", "a-i, b-iii, c-ii, d-iv", "a-iv, b-iii, c-i, d-ii", "a-ii, b-iv, c-i, d-iii"], 2, "Musicians of Karnataka." + FIX, G1H, 94),
    ],
    "K": [
        q("Consider the following statements regarding Karnataka's Global Capability Centres (GCCs) policy 2024-29.\n(a) It aims to attract 500 new GCCs.\n(b) Generates 3.5 lakh jobs.\n"
          "(c) It is expected to contribute USD 50 billion to the state economy by 2029.", ["Only (a) is correct", "(a) and (b) are correct", "(a) and (c) are correct",
                                                                                           "(a), (b) and (c) are correct"], 3, "Karnataka's first GCC policy.", G3N, 56),
        q("Consider the following statements:\n(a) Hyderabad Karnataka was officially renamed as Kalyana Karnataka in 2019.\n(b) Kalyana Karnataka comprises Bagalkote and Vijayapura.\n"
          "(c) Kalyana Karnataka was a part of Hyderabad state ruled by British in Pre-Independence era.\n(d) Central University of Karnataka was established in Kalyana Karnataka.",
          ["(a) is correct", "(b) is correct", "(c) is correct", "(a) and (d) are correct"], 3, "The region was under the Nizam; the university is at Kalaburagi.", G1H, 62),
    ],
    "L": [
        q("Consider the following statements:\nI. State Governments in India are responsible for planning, approving, implementing, operating and monitoring the drinking water "
          "schemes under the Jal Jeevan Mission.\nII. Drinking water is a State Subject in India.", AB, 0, "Water is in the State List (Entry 17).", G2N, 53),
        q("Among the duties of Grama Panchayat, which of the following is not specified as mandatory in Karnataka Gram Swaraj and Panchayat Raj Act, 1993?\n"
          "(a) To protect and nurture the biodiversity of the area.\n(b) To prepare the voter list of Grama Panchayat.\n(c) To sanction the government land for development.\n"
          "(d) To promote communal harmony and unity among all groups of people.", ["(a) and (d)", "(c) and (d)", "(b) and (c)", "(c) and (a)"], 2,
          "Voter lists are prepared by the State Election Commission; land is sanctioned by the government.", G3N, 41),
        q("According to Karnataka Gram Swaraj and Panchayat Raj Act 1993, the following terminology indicates the body consisting of persons registered as voters in the "
          "electoral rolls relating to a village comprised within the area of Gram Panchayat at the village.", ["General body of Gram Panchayat", "Gram Sabha",
                                                                                                                "Ward Sabha/Habitation Sabha", "Voter list of Gram Panchayat"], 1,
          "Article 243(b) definition too.", G3N, 43),
        q("'National Social Assistance Programme' (NSAP) – 1995, a 100% Centrally sponsored scheme, aims at ensuring minimum national standards to\n(a) the aged (b) widows "
          "(c) disabled (d) widowers", ["Only (d) is correct", "(a) and (b) are correct", "(a) and (c) are correct", "(a), (b) and (c) are correct"], 3,
          "Old-age, widow and disability pensions.", G3N, 58),
        q("Consider the following statements regarding \"GS NIRNAY mobile application\".\n(i) The Ministry of Panchayati Raj launched the application\n"
          "(ii) Providing easy access to critical information discussed during a Gram Sabha\n(iii) Increasing transparency and efficiency in the functioning of Panchayats\n"
          "(iv) It aims to empower rural communities", ["(i), (ii) and (iii) are only correct", "(i), (ii), (iii) and (iv) are correct", "(iii) and (iv) are only correct",
                                                        "(i), (ii) and (iv) are only correct"], 1, "A Gram Sabha decisions app.", G3N, 79),
        q("According to 'Karnataka Gram Swaraj and Panchayat Raj Act', members of a Gram Panchayat may resign his membership by writing to the following.",
          ["Gram Panchayat Development Officer", "Adhyaksha of Gram Panchayat", "Assistant Commissioner", "Executive Officer"], 1, "A member writes to the Adhyaksha.", G1H, 76),
        q("At what time is a Gram Panchayat member required to submit a declaration of assets and liabilities?", ["Only after completing the term", "Only when asked by the public",
                                                                                                                 "At the time prescribed by Law, usually at the time of election and periodically thereafter",
                                                                                                                 "None of the above"], 2, "As the law prescribes.", G1H, 80),
        q("Consider the following statements:\nStatement I: People engaged in farm and Non-farm activities in rural areas have to be provided with various means that help them "
          "increase the productivity.\nStatement II: Rural Development refers to overall development of village economy.", ["Both Statements I and II are correct",
                                                                                                                              "Statement I is correct but Statement II is incorrect",
                                                                                                                              "Statement I is incorrect and Statement II is correct",
                                                                                                                              "Both Statements I and II are incorrect"], 0,
          "NCERT Economics, rural development.", G2H, 30),
    ],
    "N": [
        q("Consider the following statements with reference to Sameer App.\n(a) The app provides hourly updates on National Air Quality Index (AQI)\n(b) The app is published by CPCB\n"
          "(c) The app can give AQI upto 1000\n(d) The app lists the cities in colour codes", ["All the four statements are correct", "Only three statements are correct",
                                                                                               "Only two statements are correct", "Only one statement is correct"], 1,
          "The AQI scale goes up to 500.", G1N, 52),
        q("Consider the following statements:\n(a) The Disaster Management Act was passed by the parliament in 2005.\n(b) The Union Home Minister acts as the Chairperson of the "
          "National Disaster Management Authority (NDMA)\n(c) The NDMA may not have more than nine members including Vice Chairman.\n(d) The tenure of the members of NDMA shall be five years.",
          ["(a), (b) and (c)", "(a), (c) and (d)", "(b), (c) and (d)", "(a), (b), (c) and (d)"], 1, "The Prime Minister chairs NDMA.", G1N, 80),
        q("Sustainable Development Goals comprise:", ["17 Goals, 169 Targets and 232 Indicators", "17 Targets, 169 Goals and 232 Indicators", "17 Indicators, 169 Goals, 232 Targets",
                                                      "17 Goals, 169 Indicators and 232 Targets"], 0, "Agenda 2030.", G2N, 31),
        q("Consider the following:\na. Water Hyacinth b. Lantana c. Carrot Grass d. Dodo e. Passenger Pigeon\nOf these, the species introduced to India unintentionally or "
          "deliberately, but they became weeds are:", ["a, b, c only", "a, d, e only", "b, c, d only", "c, d, e only"], 0, "Dodo and passenger pigeon are extinct birds.", G2N, 43),
        q("The amount of biodegradable organic matter in sewage water can be estimated by measuring:", ["Density of organic matter", "Density of floating debris",
                                                                                                        "Solubility of organic matter", "Biochemical oxygen demand"], 3, "BOD.", G2N, 57),
        q("The thickness of the Ozone in a column of air from the ground to the top of atmosphere is measured in terms of:", ["Dobmon units", "Dobson units", "Dalton units",
                                                                                                                             "Dialation units"], 1, "1 DU = 0.01 mm of ozone at STP.", G2N, 58),
        q("In February 2025, the Union Ministry of Petroleum and Natural Gas invited bids for Hydrocarbon exploration in three blocks under HELP policy. Which is this "
          "ecologically sensitive area at the heart of the resulting protests?", ["Bombay High", "Wedge Bank", "Palk Bay", "Wheeler Island"], 1,
          "Wadge Bank off Kanyakumari is a rich fishing ground.", G2N, 60),
        q("Consider the following Assertion (A) and Reason (R):\nAssertion (A): The Sharavathi valley wildlife Sanctuary in Karnataka has been designated as \"Tiger Reserve\" under "
          "Project Tiger.\nReason (R): The Sanctuary is contiguous with the Kudremukh National Park and forms a critical corridor for tiger movement between the Western Ghats and the Eastern Ghats.",
          ["Both 'A' and 'R' are correct, and 'R' is the correct explanation of 'A'", "Both 'A' and 'R' are correct, but 'R' is not the correct explanation of 'A'",
           "'A' is correct, but 'R' is incorrect", "Both 'A' and 'R' are incorrect"], 3, "Sharavathi Valley is a lion-tailed macaque sanctuary, not a tiger reserve.", G3N, 99),
        q("Read the following statements:\nStatement I: Rain water normally has a pH of 5.6\nStatement II: Nitrogen Oxides and sulphur dioxide cause acid rain.",
          ["Statement I is correct and Statement II is incorrect", "Both the Statements I and II are correct", "Both the Statements I and II are incorrect",
           "Statement I is incorrect and Statement II is correct"], 1, "CO₂ makes normal rain slightly acidic.", G1H, 13),
        q("Photochemical Smog extensively damages the plant life. Choose the correct options that can be used to control or reduce the formation of photochemical Smog.\n"
          "(i) Usage of catalytic converters in automobiles\n(ii) Inhibition of formation of hydrocarbons and NOx in the atmosphere.\n(iii) Plantation of Pinus, Pyrus and Vitis plants\n"
          "(iv) By increasing the concentration of Ozone", ["(ii) and (iv) only", "(i), (ii) and (iii)", "(i), (ii) and (iv)", "(i) and (ii) only"], 1,
          "Ozone is part of the smog; these plants metabolise NO₂." + FIX, G2H, 1),
        q("What is 'SAFAR'?", ["System of Air travel and Fair Advancement Research", "System of Air Quality and Weather Forecasting and Research",
                               "System of Air travel and Family Adoption Research", "System of Air Quality and Fair Weather Academic Record"], 1, "Run by IITM Pune.", G2H, 83),
    ],
    "O": [
        q("In a family of six members, Raju is the father of Rohit and is married to Asha. Raju has a sister Rekha, whose daughter is Shwetha. Rohit has a sister Ritu. How is "
          "Raju related to Ritu?", ["Father", "Son", "Brother", "Grandfather"], 0, "Ritu is Rohit's sister.", G2N, 61),
        q("If LUCKY is coded as NSEIA in a certain language, then how will HAPPY be coded in that language?", ["JYRNA", "JARNY", "JRAYN", "JYANR"], 0,
          "+2, −2, +2, −2, +2.", G2N, 65),
        q("In a row of 6 people, A is sitting third to the right of B and fourth to the right of C. D is sitting on the immediate left of A and immediate right of E. F is "
          "sitting on the immediate right of A. Who is sitting at the extreme left end?", ["A", "B", "C", "D"], 2, "Order: C, B, E, D, A, F.", G2N, 70),
        q("If UNIVERSE is coded as RLHSCQPC then the correct code of AXIOM is", ["YVHMK", "XVHLK", "YVHLK", "YVHMJ"], 1, "Letters move back 3, 2, 1, 3, 2, 1 …", G3N, 67),
        q("Pointing to a woman in a portrait, Mr. Nihal said, 'She is my sister's mother's only daughter-in-law'. How is the lady in the portrait related to Mr. Nihal?",
          ["Mother", "Sister", "Daughter", "Wife"], 3, "His mother's only daughter-in-law is his wife.", G3N, 71),
        q("If A means '+', B means '−', C means '×' and D means '÷', then 30 B 24 D 4 C 3 A 2 =", ["12", "14", "16", "18"], 1, "30 − 24 ÷ 4 × 3 + 2 = 30 − 18 + 2.", G1H, 27),
        q("If prime numbers are assigned to English alphabets from A to Z in order, then MAT will be", ["31 1 67", "41 1 67", "37 2 71", "41 2 71"], 3,
          "M = 13th prime 41, A = 2, T = 20th prime 71.", G2H, 55),
        q("A and B like to have apple juice and orange juice. A and C like to have apple and banana juice. B and D like to have mango and orange juice. C, D and E like to have "
          "pineapple and banana juice. Who likes banana, mango, pineapple and orange juice?", ["B", "A", "D", "C"], 2, "D is in both the mango-orange and pineapple-banana groups.", G2H, 65),
    ],
}
