"""Paper 1 · Educational Psychology · P1-PSY-16 21st Century Learning Skills (2 sub-topics × 20), with revision NOTES.
Coverage (planner): communication, critical thinking, creative thinking, collaboration.
References: Partnership for 21st Century Learning (P21) Framework; WHO, Life Skills Education in Schools (1997); NEP 2020 (§ 4.4–4.6);
J. P. Guilford (1950, 1967), E. P. Torrance (TTCT), Graham Wallas, The Art of Thought (1926); Edward de Bono; Alex Osborn; Elliot
Aronson (jigsaw); Frank Lyman (think-pair-share); J. H. Flavell (metacognition); NCERT/DSERT D.El.Ed. texts. No previous-year question
on this exact topic was found in the downloaded papers; all questions are "PYQ pattern" questions on themes common in KSET Education /
TET / GPSTR papers."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KSET Education / TET). "

FOUR_CS = [
    ("The '4 Cs' of 21st-century learning are:",
     ["Critical thinking, Communication, Collaboration and Creativity", "Content, Classroom, Curriculum and Control", "Computers, Coding, Cloud and Cyber-safety", "Courage, Care, Character and Culture"], 0,
     PYQ + "From the P21 framework (Partnership for 21st Century Learning)."),
    ("The P21 framework groups 21st-century skills into:",
     ["Learning skills, literacy skills and life skills", "Reading, writing and arithmetic", "Cognitive, affective and psychomotor", "Physical, mental and spiritual"], 0,
     "Learning skills – 4 Cs; literacy – information, media, technology; life skills – flexibility, leadership, initiative, productivity, social skills."),
    ("Critical thinking mainly involves:",
     ["Analysing and evaluating information and arguments to reach a reasoned judgement", "Accepting whatever the textbook says", "Memorising answers", "Criticising others"], 0,
     PYQ + "Ask: What is the evidence? Is it reliable? What are other views?"),
    ("Which classroom activity best develops critical thinking?",
     ["Comparing two news reports on the same event and judging their reliability", "Copying notes from the board", "Reciting a poem by heart", "Writing the same word ten times"], 0,
     "Higher-order thinking: analyse, evaluate."),
    ("The Socratic method develops critical thinking through:",
     ["Probing questions that make learners examine their own ideas", "Lectures without questions", "Rote drills", "Silent reading only"], 0, PYQ + "Named after Socrates."),
    ("Effective communication in the classroom requires:",
     ["Clear message, active listening and suitable feedback", "Only the teacher speaking", "Complex language", "Avoiding questions"], 0, "Communication is two-way."),
    ("Nodding, eye contact and gestures are examples of:",
     ["Non-verbal communication", "Written communication", "Formal communication only", "Noise"], 0, PYQ + "Non-verbal cues often carry much of the message's emotion."),
    ("Anything that disturbs or distorts a message during communication is called:",
     ["Noise (barrier)", "Feedback", "Channel", "Encoding"], 0, "Barriers: physical noise, language, emotions, perception."),
    ("Collaboration as a 21st-century skill means:",
     ["Working with others towards a shared goal, sharing responsibility", "Competing to defeat classmates", "Working alone silently", "Copying a friend's work"], 0, PYQ + "Group projects, cooperative learning."),
    ("In the 'Jigsaw' cooperative learning technique (Elliot Aronson), each student:",
     ["Becomes an expert on one part and teaches it to the group", "Works alone on the whole topic", "Only listens to the teacher", "Competes individually for marks"], 0,
     "Positive interdependence and individual accountability."),
    ("'Think–Pair–Share', a collaborative strategy introduced by Frank Lyman, involves:",
     ["Thinking alone, discussing with a partner, then sharing with the class", "Reading, writing and testing", "Listening, copying and memorising", "Asking the teacher only"], 0, PYQ + "Gives every learner thinking time."),
    ("Which NEP 2020 aim is most directly linked to 21st-century skills?",
     ["Reducing rote learning and promoting critical thinking, creativity and communication", "Increasing the syllabus load", "Making board exams harder", "Removing activities from school"], 0,
     "NEP 2020 also stresses experiential learning and life skills."),
    ("Information literacy means:",
     ["The ability to find, evaluate and use information effectively", "Knowing how to read only", "Typing speed", "Owning many books"], 0, PYQ + "Media literacy – judging media messages; ICT literacy – using technology."),
    ("Checking whether a viral WhatsApp message is true before forwarding it shows:",
     ["Media literacy and critical thinking", "Creativity only", "Collaboration", "Rote memory"], 0, "Check the source, date and other reliable reports."),
    ("'Learning how to learn' – being aware of and controlling one's own thinking – is called:",
     ["Metacognition (J. H. Flavell)", "Maturation", "Socialisation", "Imprinting"], 0, PYQ + "Planning, monitoring and evaluating one's learning."),
    ("Which is an example of a 'life skill' in the P21 framework?",
     ["Flexibility and adaptability", "Multiplication tables", "Spelling", "Handwriting"], 0, "Also leadership, initiative, productivity, social and cross-cultural skills."),
    ("A teacher assigns a group project where students must plan, divide roles and present together. This mainly develops:",
     ["Collaboration and communication", "Rote memory", "Handwriting", "Physical fitness only"], 0, PYQ + "Group work builds teamwork."),
    ("Which statement about 21st-century skills is correct?",
     ["They are needed for work and citizenship in a fast-changing, technology-rich world", "They replace all subject knowledge", "They can be learnt only by adults", "They are only computer skills"], 0, "Skills are built through subjects, not instead of them."),
    ("Consider the statements:\nI. Communication includes listening.\nII. Collaboration means students competing against each other.\nWhich is/are correct?",
     I_II, 0, "Only I. Collaboration is working together."),
    ("Assertion (A): Project-based learning develops 21st-century skills.\nReason (R): Projects require students to think, create, communicate and work in teams.",
     AR, 0, "R explains A."),
]

CREATIVE_LIFE = [
    ("Creative thinking is closely related to which kind of thinking described by J. P. Guilford?",
     ["Divergent thinking", "Convergent thinking", "Rote thinking", "Concrete thinking"], 0,
     PYQ + "Divergent – many possible answers; convergent – one correct answer."),
    ("Which question encourages divergent thinking?",
     ["In how many ways can we use a newspaper?", "What is the capital of Karnataka?", "What is 7 × 8?", "Who wrote the Ramayana?"], 0, "Open-ended questions have many answers."),
    ("The four components of creativity measured in the Torrance Tests of Creative Thinking are:",
     ["Fluency, flexibility, originality and elaboration", "Speed, accuracy, memory and attention", "Knowledge, comprehension, application, analysis", "Reading, writing, listening, speaking"], 0,
     PYQ + "Fluency – number of ideas; flexibility – variety; originality – uniqueness; elaboration – detail."),
    ("Graham Wallas's four stages of the creative process, in order, are:",
     ["Preparation, incubation, illumination, verification", "Incubation, preparation, verification, illumination", "Illumination, preparation, incubation, verification", "Verification, illumination, incubation, preparation"], 0,
     "Illumination is the 'aha' moment."),
    ("Brainstorming, in which ideas are generated freely without criticism, was developed by:",
     ["Alex Osborn", "Edward de Bono", "Howard Gardner", "Jerome Bruner"], 0, PYQ + "Quantity first, evaluation later."),
    ("Edward de Bono is known for:",
     ["Lateral thinking and the 'Six Thinking Hats'", "The theory of multiple intelligences", "Operant conditioning", "The zone of proximal development"], 0, "Each hat is a mode of thinking (white – facts, red – feelings, black – caution, yellow – benefits, green – creativity, blue – control)."),
    ("Which classroom climate best supports creativity?",
     ["Accepting unusual ideas and allowing mistakes", "Punishing wrong answers", "Insisting on one correct method", "Strict silence always"], 0, PYQ + "Psychological safety encourages risk-taking."),
    ("The WHO (1997) lists how many core life skills?",
     ["Ten", "Five", "Seven", "Twelve"], 0, "Self-awareness, empathy, critical thinking, creative thinking, decision making, problem solving, effective communication, interpersonal relationships, coping with stress, coping with emotions."),
    ("Which of the following is one of the WHO's ten core life skills?",
     ["Empathy", "Typing", "Swimming", "Calculation"], 0, PYQ + "Life skills help adolescents deal with everyday challenges."),
    ("Understanding and sharing another person's feelings is:",
     ["Empathy", "Sympathy only", "Self-awareness", "Assertiveness"], 0, "Empathy – feeling with; sympathy – feeling for."),
    ("Choosing the best option after considering alternatives and consequences is the life skill of:",
     ["Decision making", "Coping with emotions", "Self-awareness", "Interpersonal relationships"], 0, PYQ + "Linked to problem solving."),
    ("Which activity mainly develops problem-solving skills?",
     ["Working out how to reduce plastic waste in the school", "Copying answers", "Listening to a lecture only", "Memorising dates"], 0, "Real problems call for defining, generating options, choosing and checking."),
    ("Digital citizenship includes:",
     ["Using technology safely, responsibly and ethically", "Using social media all day", "Sharing passwords with friends", "Downloading pirated software"], 0, PYQ + "Cyber safety, digital etiquette, protecting privacy."),
    ("A student who invents a new way to explain a science concept through a skit is mainly showing:",
     ["Creativity", "Rote learning", "Convergent thinking", "Imitation only"], 0, "Original and useful idea."),
    ("Which is NOT a characteristic of creative persons?",
     ["Strict conformity and fear of new ideas", "Curiosity", "Tolerance of ambiguity", "Independent thinking"], 0, PYQ + "Creative people are open to experience."),
    ("Convergent thinking is required most in:",
     ["Solving a multiple-choice arithmetic problem with one correct answer", "Writing a story", "Designing a poster", "Suggesting uses for a brick"], 0, "Guilford's structure of intellect."),
    ("Coping with stress as a life skill involves:",
     ["Recognising stress and using healthy ways to manage it", "Avoiding all work", "Using drugs", "Blaming others"], 0, PYQ + "Exercise, time management, talking to others."),
    ("'Assertiveness' as a communication skill means:",
     ["Expressing one's views and needs clearly and respectfully", "Shouting to win", "Always agreeing", "Remaining silent"], 0, "Between passive and aggressive."),
    ("Consider the statements:\nI. Divergent thinking produces many possible answers.\nII. Fluency in creativity means the originality of an idea.\nWhich is/are correct?",
     I_II, 0, "Only I. Fluency = number of ideas; originality = uniqueness."),
    ("Assertion (A): Open-ended questions help develop creativity.\nReason (R): They allow many acceptable answers and encourage divergent thinking.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "21st Century Learning Skills": [
        ("1 · The 4 Cs – Critical Thinking, Communication, Collaboration; Literacies", FOUR_CS),
        ("2 · Creative Thinking and Life Skills", CREATIVE_LIFE),
    ],
}

NOTES = {
    "21st Century Learning Skills": [
        {"title": "21st-century learning skills – revision sheet", "md": """## P21 framework
- **Learning skills (4 Cs):** Critical thinking · Communication · Collaboration · Creativity
- **Literacy skills:** information, media, technology (ICT)
- **Life skills:** flexibility, leadership, initiative, productivity, social skills
- NEP 2020: less rote, more critical thinking, creativity, experiential learning

## Critical thinking & communication
- Analyse, evaluate, infer; Socratic questioning; check sources (media literacy)
- Communication: sender → message → channel → receiver → feedback; barriers = noise; verbal & non-verbal; assertive ≠ aggressive
- Metacognition – J. H. Flavell ('learning how to learn')

## Collaboration
- Cooperative learning: **Jigsaw – Elliot Aronson**; **Think-Pair-Share – Frank Lyman**; group projects
- Positive interdependence + individual accountability

## Creativity
- **Guilford:** divergent (many answers) vs convergent (one answer)
- **Torrance (TTCT):** fluency, flexibility, originality, elaboration
- **Wallas (1926):** preparation → incubation → illumination → verification
- **Brainstorming – Alex Osborn**; **lateral thinking, Six Thinking Hats – Edward de Bono**
- Creative climate: accept odd ideas, allow mistakes, open-ended questions

## WHO 10 core life skills (1997)
Self-awareness · Empathy · Critical thinking · Creative thinking · Decision making · Problem solving · Effective communication · Interpersonal relationships · Coping with stress · Coping with emotions
"""}],
}
