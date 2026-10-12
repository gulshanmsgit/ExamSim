"""Paper 1 · General English · P1-ENG-08 Transformation – Active / Passive Voice (2 sub-topics × 20), with revision NOTES.
References: Wren & Martin, High School English Grammar and Composition (§ 'Active and Passive Voice'); Michael Swan, Practical English
Usage. REAL previous-year questions come from the KEA 2025–26 Kannada-English-Computer papers, GTTC 2024 KEC and Legislative Council
2024 Data Entry Operator P2. KEA has published no key for the KEA papers; the parsed GTTC KEC and Data Entry keys do not match the
scanned booklet for these questions (GTTC Q66 key = 'Why was your brother written…', Data Entry Q61 key = 'The door let be shut'),
so every answer here was worked out by ExamSim and says so. Skipped: GTTC KEC Q46 (its key picks a reading that changes the subject)."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC English). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

TENSES = [
    ("Change the voice for the given sentence.\nThe teacher has written letters.",
     ["Letters are written by the teacher", "Letter has been written by the teacher", "Letters have been written by the teacher", "Letters is written by the teacher"], 2,
     "Present perfect active (has + V3) → passive has/have + been + V3; the plural subject 'letters' takes 'have'." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q58"),
    ("Which of the following sentences is the Passive Voice form of the sentence given below.\n\"Have you received the letters from your sister?\"",
     ["Are the letters received by you from your sister?", "Is your sister received letters by you?", "Have the letters being received by you from your sister?",
      "Have the letters been received by you from your sister?"], 3,
     "Present perfect question: Have + object + been + V3 + by + agent. 'Being' is used only for continuous tenses." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q52"),
    ("One of the following sentences is in Active Voice. Identify it.",
     ["Rules must be followed.", "I will reach home by 5 pm.", "Your suggestion is taken.", "This book was originally written in English."], 1,
     "The others use be + past participle. 'I will reach home' – the subject does the action, and 'reach home' has no passive." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q68"),
    ("Change the voice: She writes a letter.",
     ["A letter is written by her.", "A letter was written by her.", "A letter is being written by her.", "A letter has written by her."], 0,
     PYQ + "Simple present: am/is/are + V3."),
    ("Change the voice: They are building a bridge.",
     ["A bridge is being built by them.", "A bridge is built by them.", "A bridge was being built by them.", "A bridge has been built by them."], 0,
     PYQ + "Present continuous: am/is/are + being + V3."),
    ("Change the voice: Ravi broke the window.",
     ["The window was broken by Ravi.", "The window is broken by Ravi.", "The window has been broken by Ravi.", "The window was broke by Ravi."], 0,
     "Simple past: was/were + V3 (break – broke – broken)."),
    ("Change the voice: The police were questioning the suspect.",
     ["The suspect was being questioned by the police.", "The suspect was questioned by the police.", "The suspect is being questioned by the police.", "The suspect had been questioned by the police."], 0,
     PYQ + "Past continuous: was/were + being + V3."),
    ("Change the voice: He had finished the work before noon.",
     ["The work had been finished by him before noon.", "The work has been finished by him before noon.", "The work was being finished by him before noon.", "The work had finished by him before noon."], 0,
     "Past perfect: had + been + V3."),
    ("Change the voice: She will sing a song.",
     ["A song will be sung by her.", "A song would be sung by her.", "A song will be sang by her.", "A song will sung by her."], 0,
     PYQ + "Simple future: will/shall + be + V3 (sing – sang – sung)."),
    ("Change the voice: They will have completed the project by March.",
     ["The project will have been completed by them by March.", "The project will be completed by them by March.", "The project would have completed by them by March.",
      "The project will have being completed by them by March."], 0, "Future perfect: will have + been + V3."),
    ("Change the voice: You must obey the rules.",
     ["The rules must be obeyed by you.", "The rules must obeyed by you.", "The rules must have obeyed by you.", "The rules are obeyed by you."], 0,
     PYQ + "Modals: modal + be + V3 (can/could/may/might/must/should/would + be + V3)."),
    ("Change the voice: We can solve this problem.",
     ["This problem can be solved by us.", "This problem could be solved by us.", "This problem can solved by us.", "This problem can be solve by us."], 0, "Modal + be + V3."),
    ("Which tense normally has NO passive form in English?",
     ["Present perfect continuous", "Present perfect", "Simple past", "Simple future"], 0,
     PYQ + "Perfect-continuous tenses and the future continuous are not normally put into the passive."),
    ("Change the voice: He loves me.",
     ["I am loved by him.", "Me is loved by him.", "I am loved by he.", "I was loved by him."], 0,
     "Object pronouns become subjects: me → I, him → he, them → they; the agent after 'by' takes the object form."),
    ("Which of the following sentences CANNOT be changed into the passive voice?",
     ["The baby sleeps peacefully.", "The cat killed the rat.", "She sang a song.", "They built a house."], 0,
     PYQ + "Only transitive verbs (verbs with an object) have a passive; 'sleep' is intransitive."),
    ("Choose the correct passive of: He gave me a book.",
     ["I was given a book by him.", "I was give a book by him.", "A book was give to me by him.", "Me was given a book by him."], 0,
     "With two objects either can become the subject: 'I was given a book by him' or 'A book was given to me by him'."),
    ("Change the voice: Who wrote this letter?",
     ["By whom was this letter written?", "Who was written this letter?", "By whom this letter was written?", "Whom was this letter written?"], 0,
     PYQ + "'Who' → 'By whom', then question order: was + subject + V3."),
    ("Change the voice of the following sentence:\nWho was doing this?",
     ["By whom was doing this?", "Who has done it?", "By whom is this done?", "By whom was this being done?"], 3,
     "Past continuous question: By whom + was + object + being + V3." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q37"),
    ("Change the voice: Did he invite you?",
     ["Were you invited by him?", "Was you invited by him?", "Did you invited by him?", "Are you invited by him?"], 0, "Did + V1 (simple past question) → Was/Were + subject + V3."),
    ("Convert the following sentence from active voice to passive voice.\nWhy did your brother write such a letter?",
     ["Why was your brother written such a letter?", "Why did your brother was written such a letter?", "Why did such a letter wrote your brother?",
      "Why was such a letter written by your brother?"], 3,
     "The object 'such a letter' becomes the subject: Why + was + such a letter + written + by your brother?" + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q66"),
]

SPECIAL = [
    ("Change the voice of the given sentence\n'Shut the door'",
     ["The door is shut by me", "The door was shut by him", "Let the door be shut", "The door let be shut"], 2,
     "Imperative (order) → Let + object + be + V3." + NOTE, "Legislative Council 2024 Data Entry Operator P2 · Q61"),
    ("Identify the right form of the passive voice of the following sentence:\n\"They let him go home early\"",
     ["He was allowed to go home early", "He was let go home early", "He had been let to go home early", "He has been allowed to go home early"], 0,
     "In the passive 'let' is normally replaced by 'allowed to'; the tense stays simple past." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q49"),
    ("Change the voice: Please help me.",
     ["You are requested to help me.", "Let me be helped.", "I am helped please.", "Help is requested by me."], 0,
     PYQ + "Requests (please/kindly) → You are requested to…; advice → You are advised to…; orders → You are ordered to…"),
    ("Change the voice: Do it at once.",
     ["Let it be done at once.", "It is done at once.", "Let it done at once.", "It was done at once."], 0, "Let + object + be + V3."),
    ("Change the voice: Don't touch the wire.",
     ["Let the wire not be touched.", "Let not the wire touched.", "The wire is not touched.", "Don't let the wire touched."], 0,
     PYQ + "Negative imperative → Let + object + not + be + V3 (or: You are warned not to touch the wire)."),
    ("Change the voice: There is no time to waste.",
     ["There is no time to be wasted.", "There is no time to wasted.", "There is no time being wasted.", "There was no time to be wasted."], 0, "Active infinitive (to + V1) → passive infinitive (to be + V3)."),
    ("Change the voice: They laughed at the beggar.",
     ["The beggar was laughed at by them.", "The beggar was laughed by them.", "The beggar laughed at them.", "The beggar was being laughed by them."], 0,
     PYQ + "Prepositional verbs keep the preposition: laugh at, look after, send for, listen to."),
    ("Change the voice: She looks after her mother.",
     ["Her mother is looked after by her.", "Her mother is looked by her.", "Her mother was looked after by her.", "Her mother looks after by her."], 0, "Keep 'after' with the verb."),
    ("Change the voice: Someone has stolen my purse.",
     ["My purse has been stolen.", "My purse has been stolen by someone else.", "My purse is stolen by somebody.", "My purse had stolen."], 0,
     PYQ + "An indefinite agent (someone, people, they) is usually dropped in the passive."),
    ("Change the voice: People speak English all over the world.",
     ["English is spoken all over the world.", "English was spoken by people all over the world.", "English is speaking all over the world.", "English spoken all over the world."], 0,
     "'By people' is omitted."),
    ("Choose the correct passive: The news surprised me.",
     ["I was surprised at the news.", "I was surprised by news.", "I am surprised to the news.", "The news was surprised by me."], 0,
     PYQ + "Some verbs take other prepositions: surprised at, pleased with, known to, interested in, contained in."),
    ("Choose the correct passive: His conduct pleased me.",
     ["I was pleased with his conduct.", "I was pleased by his conduct only.", "I pleased with his conduct.", "His conduct was pleased by me."], 0, "pleased with / satisfied with."),
    ("Choose the correct passive: I know him.",
     ["He is known to me.", "He is known by me.", "He was knew to me.", "He is knowing to me."], 0, PYQ + "'Known to', not 'known by'."),
    ("Choose the correct passive: The jar contains milk.",
     ["Milk is contained in the jar.", "Milk is contained by the jar.", "The milk contained in jar.", "Milk was contain in the jar."], 0, "'Contained in'."),
    ("Change the voice: They elected him captain.",
     ["He was elected captain by them.", "Captain was elected him by them.", "He elected captain by them.", "He is elected captain by them."], 0,
     PYQ + "Factitive verbs (elect, make, appoint, call): the object becomes the subject; the complement stays after the verb."),
    ("Change into active voice: The cake was eaten by the children.",
     ["The children ate the cake.", "The children have eaten the cake.", "The children eat the cake.", "The children were eating the cake."], 0,
     "Was + V3 (simple past passive) → simple past active."),
    ("Change into active voice: The thief has been caught by the police.",
     ["The police have caught the thief.", "The police caught the thief.", "The police had caught the thief.", "The police has been catching the thief."], 0,
     PYQ + "Has been + V3 → have/has + V3; 'police' is plural."),
    ("Change the voice: It is time to close the shop.",
     ["It is time for the shop to be closed.", "It is time to be closed the shop.", "The shop is time to close.", "It is time the shop closed by us."], 0, "to + V1 → for + object + to be + V3."),
    ("Consider the statements:\nI. In the passive voice, the object of the active sentence becomes the subject.\nII. The passive voice is formed with 'be' + present participle (-ing).\nWhich is/are correct?",
     I_II, 0, "Only I. The passive uses 'be' + PAST participle (V3)."),
    ("Assertion (A): 'Let the work be finished' is the passive form of 'Finish the work'.\nReason (R): Imperative sentences are changed into the passive with let + object + be + past participle.",
     AR, 0, "R states the rule that produces A."),
]

TOPICS = {
    "Transformation – Active / Passive Voice": [
        ("1 · Passive Forms in Different Tenses, Modals and Questions", TENSES),
        ("2 · Imperatives, Prepositional Verbs and Special Cases", SPECIAL),
    ],
}

NOTES = {
    "Transformation – Active / Passive Voice": [
        {"title": "Active and passive voice – rules at a glance", "md": """## Basic rule
Object of the active → subject of the passive; verb → **be + past participle (V3)**; subject → **by + object form** (I→me, he→him, they→them).
Only **transitive** verbs (with an object) have a passive.

## Tense table (write a letter)
| Tense | Active | Passive |
|---|---|---|
| Simple present | writes | is written |
| Present continuous | is writing | is **being** written |
| Present perfect | has written | has **been** written |
| Simple past | wrote | was written |
| Past continuous | was writing | was being written |
| Past perfect | had written | had been written |
| Simple future | will write | will be written |
| Future perfect | will have written | will have been written |
| Modals | can/must write | can/must **be** written |
- No passive (normally): present/past/future perfect continuous, future continuous

## Questions
- Yes/no: Did he invite you? → **Were you invited** by him?
- Who → **By whom**: Who wrote it? → By whom was it written?
- Why/when/where stay in front: Why did he write it? → Why **was it written** by him?

## Imperatives
- Order: Shut the door → **Let the door be shut**
- Negative: Don't touch it → Let it **not** be touched
- Request: Please help me → **You are requested** to help me; advice → You are advised to…
- let → **allowed to**: They let him go → He was allowed to go

## Special cases
- Keep prepositions: laughed **at**, looked **after**, sent **for**
- Not 'by': known **to**, pleased **with**, surprised **at**, interested **in**, contained **in**, filled **with**
- Drop vague agents: by people / someone / they
- Two objects: He gave me a book → I was given a book / A book was given to me
- Factitive: They made him king → He was made king

## ⚠ Traps
- 'being' only in continuous tenses; 'been' only in perfect tenses
- Plural subject → have/were
"""}],
}
