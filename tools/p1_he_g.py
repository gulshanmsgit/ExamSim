"""Paper 1 · Health Education · P1-HE-07 Growing with Self-Confidence (2 sub-topics × 20), with revision NOTES.
Coverage (planner): growth, development & maturity; anxiety & depression; drugs & drug abuse; sexual harassment.
References: DSERT/NCERT Health and Physical Education texts; NCERT Biology class 12 (ch. 8, drugs and alcohol abuse); WHO adolescent
health; POCSO Act 2012 (amended 2019); Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013; NDPS
Act 1985; Ministry of Social Justice (Nasha Mukt Bharat Abhiyaan); Tele-MANAS. One REAL previous-year question (KSET 2023 Education,
principles of development) is used; its answer was worked out by ExamSim."""
from packlib import AR, I_II

PYQ = "PYQ pattern (TET / GPSTR / KSET Education). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

GROWTH_MIND = [
    ("Which of the following is not a principle of growth and development?",
     ["It is continuous and orderly.", "It is influenced by genetic and environmental factors.", "It occurs in isolation from the environment.",
      "It involves both qualitative and quantitative changes."], 2, "Development always results from interaction of heredity and environment." + NOTE, "KSET 2023 Education · Q1"),
    ("'Growth' and 'development' differ because:",
     ["Growth is quantitative (size, weight); development is qualitative and lifelong (skills, functions)", "Both mean only physical changes",
      "Growth continues lifelong; development stops at puberty", "Development can be measured only in kilograms"], 0, PYQ + "Growth may stop after maturity; development continues."),
    ("Maturation means:",
     ["Changes that unfold naturally from heredity, without special training", "Learning by practice", "Forgetting", "Social adjustment only"], 0,
     "Example: a child walks when the muscles and nerves are ready."),
    ("Development proceeds from head to toe. This is the ______ principle.",
     ["Cephalocaudal", "Proximodistal", "General-to-specific", "Integration"], 0, PYQ + "Proximodistal – from the centre of the body outwards."),
    ("According to the WHO, adolescence covers the age group of:",
     ["10–19 years", "5–10 years", "18–25 years", "13–30 years"], 0, "Youth: 15–24; young people: 10–24."),
    ("Adolescence is often called a period of 'storm and stress'. This phrase is associated with:",
     ["G. Stanley Hall", "Jean Piaget", "B. F. Skinner", "Lev Vygotsky"], 0, PYQ + "Rapid physical, emotional and social changes."),
    ("Secondary sexual characters in boys during puberty are mainly controlled by the hormone:",
     ["Testosterone", "Oestrogen", "Insulin", "Thyroxine"], 0, "Girls – oestrogen and progesterone; first menstruation is menarche."),
    ("The Government of India's programme for adolescent health (10–19 years), launched in 2014, is:",
     ["Rashtriya Kishor Swasthya Karyakram (RKSK)", "Janani Suraksha Yojana", "Mission Indradhanush", "POSHAN Abhiyaan"], 0, PYQ + "It has peer educators and adolescent-friendly health clinics."),
    ("Self-confidence is best described as:",
     ["Trust in one's own abilities and judgement", "Believing one is better than everyone", "Never asking for help", "Avoiding new tasks"], 0,
     "Over-confidence ignores limits; healthy confidence is realistic."),
    ("Albert Bandura's term for a person's belief in their ability to succeed at a particular task is:",
     ["Self-efficacy", "Self-actualisation", "Self-concept", "Ego"], 0, PYQ + "Sources: past success, watching others succeed, encouragement, calm physical state."),
    ("Which practice by a teacher best builds students' self-confidence?",
     ["Giving tasks at the right level and praising effort and progress", "Comparing students publicly", "Punishing every mistake", "Giving only very hard tasks"], 0,
     "Success experiences and specific feedback build confidence."),
    ("Persistent sadness, loss of interest in activities, poor sleep and appetite for two weeks or more are signs of:",
     ["Depression", "Normal tiredness", "Anxiety only", "Good mental health"], 0, PYQ + "Needs counselling or medical help; it is treatable."),
    ("Excessive worry, restlessness, a racing heart and fear about future events are typical of:",
     ["Anxiety", "Depression only", "Schizophrenia", "Dementia"], 0, "Mild anxiety before exams is normal; persistent anxiety needs help."),
    ("India's national tele-mental-health helpline (Tele-MANAS) number is:",
     ["14416", "1098", "112", "181"], 0, PYQ + "1098 – child helpline; 181 – women's helpline; 112 – emergency."),
    ("World Mental Health Day is observed on:",
     ["10 October", "7 April", "26 June", "1 December"], 0, "7 April – World Health Day; 26 June – anti-drug day; 1 December – World AIDS Day."),
    ("Which of the following is a healthy way of coping with stress?",
     ["Regular exercise, talking to trusted people and good sleep", "Using alcohol to relax", "Skipping meals", "Isolating oneself completely"], 0, PYQ + "Also yoga, meditation, time management."),
    ("Which statement about adolescence is correct?",
     ["Peer influence becomes very strong", "Physical growth stops", "Children lose interest in identity", "Emotions become very stable"], 0, "Erikson: identity vs role confusion."),
    ("Erikson's psychosocial stage during adolescence is:",
     ["Identity vs role confusion", "Trust vs mistrust", "Industry vs inferiority", "Intimacy vs isolation"], 0, PYQ + "Industry vs inferiority – school age; intimacy vs isolation – young adult."),
    ("Consider the statements:\nI. Growth is mainly quantitative.\nII. Development stops when growth stops.\nWhich is/are correct?",
     I_II, 0, "Only I. Development continues throughout life."),
    ("Assertion (A): Adolescents need guidance and counselling in school.\nReason (R): Adolescence brings rapid physical, emotional and social changes.",
     AR, 0, "R explains A."),
]

DRUGS_SAFETY = [
    ("Heroin (smack) and morphine are obtained from:",
     ["The poppy plant (Papaver somniferum)", "Cannabis sativa", "Erythroxylum coca", "Tobacco"], 0, PYQ + "They are opioids – depressants that slow body functions."),
    ("Charas, ganja and bhang come from:",
     ["Cannabis sativa (cannabinoids)", "Poppy", "Coca", "Datura only"], 0, "Cannabinoids affect the cardiovascular system."),
    ("Cocaine, a powerful stimulant, is obtained from:",
     ["The coca plant (Erythroxylum coca)", "Poppy", "Cannabis", "Tea leaves"], 0, PYQ + "It interferes with dopamine transport, giving euphoria."),
    ("Alcohol acts on the central nervous system as a:",
     ["Depressant", "Stimulant", "Hallucinogen", "Vitamin"], 0, "Long-term use damages the liver (cirrhosis)."),
    ("Nicotine in tobacco:",
     ["Is a stimulant that raises blood pressure and heart rate and causes addiction", "Is a vitamin", "Cures cancer", "Has no effect on the body"], 0,
     PYQ + "Smoking is linked to lung, mouth and throat cancer; COTPA 2003 controls tobacco."),
    ("LSD is classified as a(n):",
     ["Hallucinogen", "Depressant", "Analgesic", "Antibiotic"], 0, "Hallucinogens alter perception."),
    ("Unpleasant symptoms when a dependent person suddenly stops a drug (shaking, sweating, anxiety) are called:",
     ["Withdrawal symptoms", "Side effects", "Immunity", "Tolerance"], 0, PYQ + "Tolerance – needing larger doses for the same effect."),
    ("Early warning signs of drug abuse in a student include:",
     ["Falling grades, absence, change in friends and secretive behaviour", "Improved sleep", "More interest in studies", "Regular exercise"], 0, "Teachers should counsel, not shame."),
    ("India's law that controls narcotic drugs and psychotropic substances is the:",
     ["NDPS Act, 1985", "COTPA, 2003", "Drugs and Cosmetics Act, 1940 only", "IPC 1860 only"], 0, PYQ + "COTPA – Cigarettes and Other Tobacco Products Act (no smoking in public places, no sale near schools)."),
    ("The International Day against Drug Abuse and Illicit Trafficking is observed on:",
     ["26 June", "31 May", "10 October", "5 June"], 0, "31 May – World No Tobacco Day; 5 June – World Environment Day."),
    ("The 'Nasha Mukt Bharat Abhiyaan' (2020) is run by which Union ministry?",
     ["Ministry of Social Justice and Empowerment", "Ministry of Defence", "Ministry of Education alone", "Ministry of Home Affairs alone"], 0,
     PYQ + "National toll-free drug de-addiction helpline: 14446."),
    ("The POCSO Act, 2012 protects children (below 18 years) from:",
     ["Sexual offences", "Child labour only", "Exam stress", "Malnutrition"], 0, "POCSO = Protection of Children from Sexual Offences; special courts; reporting is mandatory."),
    ("Under the POCSO Act, a teacher who learns that a child has been sexually abused must:",
     ["Report it to the police or Special Juvenile Police Unit (failure to report is an offence)", "Keep it secret", "Settle it with the family", "Wait for the parents to complain"], 0,
     PYQ + "Child-friendly procedures; identity of the child must not be disclosed."),
    ("The law that protects women from sexual harassment at the workplace in India is the:",
     ["Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013", "Dowry Prohibition Act, 1961",
      "Domestic Violence Act, 2005", "Maternity Benefit Act, 1961"], 0, "It followed the Supreme Court's Vishaka guidelines (1997)."),
    ("Under the POSH Act, 2013, every workplace with 10 or more employees must set up:",
     ["An Internal Complaints Committee", "A canteen committee", "A sports committee", "A Lok Adalat"], 0,
     PYQ + "Where there is none, a Local Committee is set up by the District Officer."),
    ("The Supreme Court's guidelines on sexual harassment at the workplace (1997) are known as:",
     ["Vishaka guidelines", "Shah Bano guidelines", "Kesavananda guidelines", "Maneka guidelines"], 0, "Vishaka v. State of Rajasthan."),
    ("'Good touch – bad touch' education in schools mainly aims to:",
     ["Help children recognise and report unsafe touch", "Teach sports skills", "Teach first aid", "Improve handwriting"], 0, PYQ + "Children learn to say No, move away and tell a trusted adult."),
    ("Which helpline number should a child in distress call in India?",
     ["1098 (Childline)", "100", "108", "14416"], 0, "108 – ambulance; 100/112 – police."),
    ("Consider the statements:\nI. Alcohol is a stimulant.\nII. Opioids such as heroin are depressants.\nWhich is/are correct?",
     I_II, 1, "Only II. Alcohol is also a depressant."),
    ("Assertion (A): Peer pressure is a common reason why adolescents start using drugs.\nReason (R): Adolescents strongly want acceptance by their friends.",
     AR, 0, "R explains A; life-skills education helps them refuse."),
]

TOPICS = {
    "Growing with Self-Confidence": [
        ("1 · Growth, Development, Maturity, Self-Confidence, Anxiety and Depression", GROWTH_MIND),
        ("2 · Drugs and Drug Abuse, and Protection from Sexual Harassment", DRUGS_SAFETY),
    ],
}

NOTES = {
    "Growing with Self-Confidence": [
        {"title": "Growing with self-confidence – revision sheet", "md": """## Growth, development, maturity
- Growth – quantitative (height, weight), stops after maturity; development – qualitative, lifelong
- Maturation – natural unfolding by heredity; learning – by practice
- Principles: continuous & orderly, cephalocaudal (head→toe), proximodistal (centre→outward), general→specific, individual differences, heredity × environment
- Adolescence (WHO) **10–19**; 'storm and stress' – G. Stanley Hall; Erikson – identity vs role confusion
- Hormones: testosterone (boys), oestrogen & progesterone (girls); menarche
- **RKSK 2014** – adolescent health programme

## Self-confidence and mental health
- Self-efficacy – **Bandura**; build it with suitable tasks, praise for effort, success experiences
- Depression – sadness/loss of interest ≥ 2 weeks; anxiety – excessive worry, restlessness
- Coping: exercise, sleep, talking, yoga, meditation, time management
- **Tele-MANAS 14416**; World Mental Health Day **10 Oct**

## Drugs
| Drug | Source | Type |
|---|---|---|
| Heroin, morphine | poppy (Papaver) | opioid – depressant |
| Charas, ganja, bhang | Cannabis sativa | cannabinoid |
| Cocaine | coca (Erythroxylum) | stimulant |
| LSD | synthetic | hallucinogen |
| Alcohol | fermentation | depressant |
| Nicotine | tobacco | stimulant, addictive |
- Tolerance, dependence, withdrawal symptoms; warning signs: falling grades, new friends, secrecy
- Laws: **NDPS Act 1985**, COTPA 2003; Nasha Mukt Bharat Abhiyaan 2020 (MoSJE), helpline **14446**
- Days: anti-drug day **26 June**; No Tobacco Day 31 May

## Sexual harassment
- **POCSO Act 2012** (amended 2019): children < 18; mandatory reporting; special courts; child's identity secret
- **POSH Act 2013**: Internal Complaints Committee (10+ employees), Local Committee (District Officer); based on **Vishaka (1997)**
- Helplines: Childline **1098**, women **181**, emergency **112**
- Good touch – bad touch: say No, go away, tell a trusted adult
"""}],
}
