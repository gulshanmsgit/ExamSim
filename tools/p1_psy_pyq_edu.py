"""Paper 1 · Educational Psychology · real previous-year questions from the KSET / GFGC EDUCATION papers (owner, 23 Nov 2026:
"proceed next" – type up the Education papers so the previous-year tests get more psychology questions).

Papers (KEA archive, URLs in tools/pyq_manifest.tsv; bilingual booklets, English pages transcribed – page images checked where
the OCR was unclear): KSET 2023 Education (version B1), KSET 2024 Education (A1), KSET 2025 Education (A1), GFGC Asst Professor
2021–22 Education (A1). Only the questions on the GPSTR Educational Psychology syllabus that no earlier module had used are
here (earlier ones: p1_psy_*, p1_he_*, p1_ca_plan_d, …). Options are A–D in the printed order ((1)–(4) → A–D).
KEA has published no answer key for these Education papers, so every answer is worked out by ExamSim and says so.
Already used earlier: KSET 2023 Q9, Q16 (p1_psy_g and others). Left out as ambiguous (more than one defensible option, or an option list that does not fit the question): KSET 2023 Q8, Q14;
KSET 2024 Q21, Q22, Q62; KSET 2025 Q73, Q98; GFGC Q32, Q34, Q89. KSET 2023 Q5 (social cognition) fits no syllabus topic.
Each topic gets a set "3 · Previous-Year Questions (KSET & GFGC Education)" (build_subject accepts real-question sets of any
size ≥ 2), Piaget's stages sit with Growth and Development."""

NOTE = " (Answer worked out by ExamSim; KEA has published no key for this paper.)"
K23, K24, K25, GF = "KSET 2023 Education · Q{}", "KSET 2024 Education · Q{}", "KSET 2025 Education · Q{}", "GFGC 2021 Education · Q{}"
AR4 = ["Both (A) and (R) are true and (R) is the correct explanation of (A)", "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
       "(A) is true but (R) is false", "(A) is false but (R) is true"]
AR4b = ["Both (A) and (R) are true and (R) is the correct explanation of (A)", "Both (A) and (R) are true, but (R) is not the correct explanation of (A)",
        "(A) is true, but (R) is false", "(A) is false, but (R) is true"]

INTELLIGENCE = [
    ("According to Howard Gardner, intelligence is:",
     ["a set of integrated abilities influenced by one's experiences to different degrees.", "a consistent variation in behaviour accompanying changes in the stimulus patterns.",
      "the ability to think in usual and unusual ways to come up with unique solutions.", "the biopsychological potential to process relevant information in culturally relevant ways."], 3,
     "Gardner (Intelligence Reframed, 1999): 'a biopsychological potential to process information that can be activated in a cultural setting to solve problems or create products that are of value in a culture'. Option C describes creativity." + NOTE, K23.format(10)),
    ("Match List-I with List-II\nList-I (Descriptive Level)\na) Superior\nb) Mildly mentally-retarded\nc) Borderline\nd) High average\nList-II (IQ Ranges)\ni. 55 - 69\nii. 120 - 129\niii. 110 - 119\niv. 70 - 79\nv. 60 - 69\nChoose the correct answer:",
     ["a - i, b - ii, c - iii, d - iv", "a - iv, b - iii, c - ii, d - i", "a - ii, b - i, c - iv, d - iii", "a - i, b - ii, c - iv, d - iii"], 2,
     "Wechsler classification: superior 120–129, high average 110–119, borderline 70–79, mild mental retardation about 55–69 (item v is extra)." + NOTE, K24.format(26)),
    ("Which among the following expansions of progressive matrices used popularly as a non-verbal test of intelligence is INCORRECT?",
     ["Advanced Progressive Matrices (APM)", "Coloured Progressive Matrices (CPM)", "Radical Progressive Matrices (RPM)", "Standard Progressive Matrices (SPM)"], 2,
     "RPM means Raven's Progressive Matrices (J. C. Raven, 1938); its three forms are Standard, Coloured and Advanced." + NOTE, K24.format(28)),
    ("Which of the following represents non-verbal tests of intelligence?\ni. Alfred Binet's test\nii. Army Beta test\niii. Comprehension test\niv. Raven's Progressive Matrices test",
     ["i and ii", "ii and iii", "i and iv", "ii and iv"], 3,
     "Army Beta (1917, for recruits who could not read English) and Raven's matrices need no language; Binet's test and comprehension tests are verbal." + NOTE, K25.format(26)),
    ("Structure of Intellect (SI Model) is evolved by",
     ["Thurstone", "Guilford", "Cattel", "Eysenck"], 1,
     "J. P. Guilford's three-dimensional model: operations × contents × products (120, later 180 abilities). Thurstone gave the primary mental abilities." + NOTE, GF.format(27)),
]

SKILLS_21 = [
    ("Which of the following are elements of critical thinking?\nI. Analysis\nII. Conformity\nIII. Evaluation\nIV. Creativity",
     ["I and III only", "II and IV only", "I, II and III only", "II, III and IV only"], 0,
     "Critical thinking analyses and evaluates claims and arguments. Conformity is its opposite; creativity belongs to creative thinking." + NOTE, K23.format(4)),
    ("Which of the following can be characterized as an important benefit of collaborative learning?",
     ["Decreased need of communication skills", "Reduced social interaction", "Improved critical thinking and problem solving skills", "Exposure to diverse perspectives is limited"], 2,
     "Working in groups makes learners explain, question and defend ideas; the other options are the opposite of what collaboration gives." + NOTE, K23.format(15)),
    ("Given below are two statements, labelled as Assertion (A) and Reason (R). Choose the correct answer from the codes given below:\nAssertion (A): Critical thinking involves identifying, evaluating and constructing argument.\nReason (R): The ability to infer a conclusion from one or multiple premises requires examining logical relationships among statements or data.",
     AR4, 0,
     "Both are true, and drawing inferences from premises by examining their logical relations is exactly what evaluating and constructing arguments needs." + NOTE, K24.format(30)),
    ("What is meant by 'Positive interdependence' in collaborative learning?",
     ["Ignoring the contributions of other group members", "Success of each member is linked to group success", "Collaborating with a diverse group of members", "Relying on oneself for learning"], 1,
     "Johnson & Johnson: members 'sink or swim together' – one of the five elements of cooperative learning, with individual accountability, promotive interaction, social skills and group processing." + NOTE, K25.format(40)),
]

STYLES = [
    ("Which aspect of experiential learning involves creating new concepts or modifying existing ones based on experience?",
     ["Active experimentation", "Concrete experience", "Abstract conceptualization", "Reflective observation"], 2,
     "Kolb's cycle: concrete experience → reflective observation → abstract conceptualization (forming or changing concepts) → active experimentation." + NOTE, K24.format(35)),
    ("There are two statements marked as Assertion (A) and Reason (R). Mark your answer as per the codes given below:\nAssertion (A): Classroom instruction should involve variety of strategies\nReason (R): There are individual learning styles among students",
     AR4b, 0,
     "Because learners differ in style (visual, auditory, kinaesthetic …), varied strategies reach more of them – R explains A." + NOTE, K25.format(19)),
    ("In experiential learning, what is the role of reflection?",
     ["To document the experience without any analysis", "To analyse the experience and derive deeper understanding", "To focus solely on the emotional aspect of the experience", "To avoid engagement in the experience altogether"], 1,
     "Reflective observation turns an experience into learning (Kolb; Dewey: 'we learn by reflecting on experience')." + NOTE, K25.format(34)),
]

GROWTH = [
    ("Which of the following is correct with regard to growth and development?",
     ["Not related to each other", "Independent of each other", "Correlated", "Cannot be said"], 2,
     "Growth (quantitative change) and development (qualitative change) go together and influence each other." + NOTE, K25.format(21)),
    ("Which of the following represents the right sequence of stages of cognitive development according to Piaget?\ni. Formal operational stage\nii. Pre-operational stage\niii. Sensory motor stage\niv. Concrete operational stage\nCodes:",
     ["i, ii, iii, iv", "ii, iii, iv, i", "iii, ii, iv, i", "iv, i, ii, iii"], 2,
     "Sensorimotor (0–2), pre-operational (2–7), concrete operational (7–11), formal operational (11+)." + NOTE, K25.format(25)),
]

BACKWARD = [
    ("Match List-I with List-II and select the correct option from the codes given below:\nList-I (Disability)\na. Dyslexia\nb. Dysgraphia\nc. Dyscalculia\nd. ADHA\nList-II (Description)\ni. Difficulty in handwriting and written expression.\nii. Difficulty in reading, spelling and writing.\niii. Difficulty in attention, hyperactivity and impulsivity.\niv. Difficulty in mathematical calculations.\nCodes: a b c d",
     ["iii ii iv i", "ii i iv iii", "iii iv i ii", "iv ii iii i"], 1,
     "Dyslexia – reading; dysgraphia – handwriting; dyscalculia – mathematics; ADHD ('ADHA' as printed) – attention and hyperactivity." + NOTE, K23.format(75)),
    ("The primary characteristic of children with dyslexia includes",
     ["Attention deficit disorders", "Divergent thinking, fluency in reading", "Inability to read fluently", "Engaging in repetitive locomotor action"], 2,
     "Dyslexia is a specific learning disability in reading (decoding, fluency, spelling), not an attention disorder." + NOTE, K24.format(94)),
]

SET = "3 · Previous-Year Questions (KSET & GFGC Education)"
TOPICS = {
    "Intelligence": [(SET, INTELLIGENCE)],
    "21st Century Learning Skills": [(SET, SKILLS_21)],
    "Learning Styles & Domains of Learning": [(SET, STYLES)],
    "Growth and Development": [(SET, GROWTH)],
    "Gifted, Backward and Creative Children": [(SET, BACKWARD)],
}
