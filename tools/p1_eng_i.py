"""Paper 1 · General English · P1-ENG-09 Transformation – Types of Sentences (2 sub-topics × 20), with revision NOTES.
Coverage (planner): positive, negative, Wh-questions, yes/no questions, orders/requests, how & what exclamatory.
References: Wren & Martin, High School English Grammar and Composition (§ 'Transformation of Sentences', 'Question Tags'); Michael Swan,
Practical English Usage. REAL previous-year questions (question tags) come from GTTC 2024 KEC and Legislative Council 2024 Data Entry
Operator P2; the parsed keys for these papers do not match the scanned booklets, so answers were worked out by ExamSim and say so.
KEA 2026 KEC (NHK) Q38 on simple sentences is kept for P1-ENG-11 Clauses."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / SSC English). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

ASSERT_QUESTION = [
    ("Choose the correct question tag for the statement given below.\nI do not dare to fight with you,",
     ["Will I", "Should I", "Do I", "Can I"], 2,
     "'Dare' is used here as an ordinary verb with 'do not', so the tag uses 'do': …, do I?" + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q57"),
    ("Choose the appropriate question tag for the given sentence.\nChildren play cricket everyday, ___?",
     ["Don't they", "Didn't they", "Don't children", "Didn't children"], 0,
     "Simple present, positive statement → negative tag with 'don't' and a pronoun (they)." + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q61"),
    ("These movies are really cringeworthy.\nChoose the correct question tag for the given statement",
     ["Don't they?", "Are they?", "Aren't they?", "Aren't some?"], 2, "Positive statement with 'are' → negative tag 'aren't they?'" + NOTE,
     "Legislative Council 2024 Data Entry Operator P2 · Q44"),
    ("Choose the appropriate 'Question Tag' for the given sentence.\nI am preparing today's breakfast, ___?",
     ["doesn't I?", "aren't I?", "am I?", "isn't I?"], 1, "The negative tag for 'I am' is the special form 'aren't I?'" + NOTE,
     "Legislative Council 2024 Data Entry Operator P2 · Q63"),
    ("Change into a negative sentence without changing the meaning: He is always punctual.",
     ["He is never late.", "He is never punctual.", "He is not always late.", "He was never late."], 0,
     PYQ + "Use an opposite word with 'not/never': always punctual = never late."),
    ("Change into a negative sentence: Only a fool can say so.",
     ["None but a fool can say so.", "A fool cannot say so.", "Only a fool cannot say so.", "No fool can say so."], 0, "Only → None but (for persons) / nothing but (for things)."),
    ("Change into an affirmative sentence: No one was absent.",
     ["Everyone was present.", "Everyone was absent.", "Someone was absent.", "No one was present."], 0, PYQ + "not absent = present; no one = everyone."),
    ("Change into an affirmative sentence: He is not as tall as his brother.",
     ["His brother is taller than he is.", "He is taller than his brother.", "He is as tall as his brother.", "His brother is not taller than him."], 0,
     "Negative positive degree → comparative with the other subject."),
    ("Change into a yes/no question: She can swim.",
     ["Can she swim?", "Does she can swim?", "She can swim?", "Can she swims?"], 0, PYQ + "Auxiliary/modal moves before the subject."),
    ("Change into a yes/no question: They went to Mysuru.",
     ["Did they go to Mysuru?", "Did they went to Mysuru?", "Went they to Mysuru?", "Do they went to Mysuru?"], 0,
     "No auxiliary → use do/does/did + base form (go, not went)."),
    ("Form a Wh-question for the underlined part: Ravi lives in Hassan. (underlined: in Hassan)",
     ["Where does Ravi live?", "Where Ravi lives?", "Where does Ravi lives?", "Who lives in Hassan?"], 0, PYQ + "Wh-word + do/does/did + subject + base verb."),
    ("Form a Wh-question for the underlined subject: Meena broke the glass. (underlined: Meena)",
     ["Who broke the glass?", "Who did break the glass?", "Whom broke the glass?", "Who did Meena break?"], 0,
     "When 'who' asks about the subject, no 'do/did' is needed."),
    ("Change the interrogative into an assertive sentence: Can anyone bear such an insult?",
     ["No one can bear such an insult.", "Anyone can bear such an insult.", "Everyone can bear such an insult.", "Someone cannot bear such an insult."], 0,
     PYQ + "A rhetorical positive question = a strong negative statement."),
    ("Change the interrogative into an assertive sentence: Is it not a shame to cheat?",
     ["It is a shame to cheat.", "It is not a shame to cheat.", "Cheating is good.", "It was a shame to cheat."], 0, "A negative rhetorical question = a positive statement."),
    ("Change the assertive into an interrogative sentence: Nobody likes to be insulted.",
     ["Who likes to be insulted?", "Does nobody like to be insulted?", "Who does not like to be insulted?", "Do everybody like to be insulted?"], 0,
     PYQ + "Nobody/no one → 'Who…?' rhetorical question."),
    ("Choose the correct question tag: Let's go for a walk, ___?",
     ["shall we?", "will you?", "don't we?", "won't we?"], 0, PYQ + "'Let's' → 'shall we?'; imperatives → 'will you?' (Close the door, will you?)."),
    ("Choose the correct question tag: Nobody called me, ___?",
     ["did they?", "didn't they?", "did he?", "didn't he?"], 0, "Negative words (nobody, never, hardly) make the statement negative → positive tag; nobody → they."),
    ("Choose the correct question tag: She has finished her work, ___?",
     ["hasn't she?", "has she?", "doesn't she?", "didn't she?"], 0, "Repeat the auxiliary 'has' in the negative."),
    ("Consider the statements:\nI. A positive statement normally takes a negative question tag.\nII. 'I am right, amn't I?' is the standard tag in English.\nWhich is/are correct?",
     I_II, 0, "Only I. The standard form is 'aren't I?'."),
    ("Assertion (A): 'He never comes late, does he?' is correct.\nReason (R): 'Never' makes the statement negative, so the tag is positive.",
     AR, 0, "R explains A."),
]

IMPERATIVE_EXCLAIM = [
    ("Change into an exclamatory sentence: It is a very beautiful flower.",
     ["What a beautiful flower it is!", "How a beautiful flower it is!", "What beautiful flower it is!", "How beautiful a flower is it!"], 0,
     PYQ + "What + a/an + adjective + noun + subject + verb!"),
    ("Change into an exclamatory sentence: The night is very dark.",
     ["How dark the night is!", "What dark the night is!", "How dark is the night!", "What a dark the night is!"], 0, "How + adjective/adverb + subject + verb!"),
    ("Change into an assertive sentence: What a fine day it is!",
     ["It is a very fine day.", "It is not a fine day.", "Is it a fine day?", "What is a fine day."], 0, PYQ + "Replace What/How with 'very'."),
    ("Change into an assertive sentence: How cleverly he answered!",
     ["He answered very cleverly.", "He answered cleverly?", "He did not answer cleverly.", "How he answered cleverly."], 0, "How + adverb → very + adverb."),
    ("Change into an exclamatory sentence: I wish I were young again.",
     ["O that I were young again!", "What I were young again!", "How young I am again!", "Alas, I am young again!"], 0,
     PYQ + "Wishes: 'O that…!' / 'If only…!'; sorrow: 'Alas!'; joy: 'Hurrah!'"),
    ("Change into an assertive sentence: Alas! The old man is dead.",
     ["It is sad that the old man is dead.", "The old man is happily dead.", "Is the old man dead?", "How dead the old man is!"], 0, "'Alas' expresses sorrow."),
    ("Change into an exclamatory sentence: It is very foolish of him to say that.",
     ["How foolish of him to say that!", "What foolish of him to say that!", "How foolish he is to said that!", "What a foolish to say that!"], 0, "How + adjective + …!"),
    ("Change into an imperative sentence: You should respect your elders.",
     ["Respect your elders.", "You respect your elders?", "Let you respect your elders.", "Respects your elders."], 0, PYQ + "Imperatives begin with the base verb; the subject 'you' is understood."),
    ("Change into an imperative sentence: You are requested to close the door.",
     ["Please close the door.", "Close the door, isn't it?", "Let the door closed.", "You close door."], 0, "Request → Please/Kindly + verb."),
    ("Change into a negative imperative: You must not waste time.",
     ["Do not waste time.", "Not waste time.", "Don't wasting time.", "No waste time."], 0, "Do not / Don't + base verb; Never + verb."),
    ("Change into an assertive sentence: Never tell a lie.",
     ["You should never tell a lie.", "You never told a lie.", "Do you tell a lie?", "Never you tell a lie?"], 0, PYQ + "Imperative → You should/must…"),
    ("Change into an assertive sentence: Let us go home.",
     ["I propose that we should go home.", "Let us went home.", "We go home?", "Go home, let us."], 0, "Let us → I propose/suggest that we should…"),
    ("Change into an assertive sentence: Please give me a glass of water.",
     ["I request you to give me a glass of water.", "You gave me a glass of water.", "Give me a glass of water?", "Let me give a glass of water."], 0, PYQ + "Please… → I request you to…"),
    ("Which of the following is an imperative sentence?",
     ["Shut the window.", "The window is shut.", "Is the window shut?", "What a big window it is!"], 0, "Order/command/request."),
    ("Which of the following is an exclamatory sentence?",
     ["How sweetly she sings!", "She sings sweetly.", "Does she sing sweetly?", "Sing sweetly."], 0, PYQ + "Expresses sudden feeling; ends with '!'"),
    ("Which kind of sentence is: 'Kindly lend me your pen.'?",
     ["Imperative (request)", "Exclamatory", "Interrogative", "Assertive"], 0, "Requests are imperative sentences."),
    ("Change into an interrogative sentence: Everyone knows the earth is round.",
     ["Who does not know that the earth is round?", "Does everyone know the earth is round.", "Who knows the earth is round?", "Is the earth round?"], 0,
     PYQ + "Everyone… → Who does not…? (rhetorical)."),
    ("The four kinds of sentences according to function are:",
     ["Assertive (declarative), interrogative, imperative and exclamatory", "Simple, compound, complex and mixed", "Active, passive, direct and indirect", "Positive, comparative, superlative and negative"], 0,
     "Simple/compound/complex is the classification by structure."),
    ("Consider the statements:\nI. 'What a lovely garden!' is an exclamatory sentence.\nII. 'Please sit down.' is an assertive sentence.\nWhich is/are correct?",
     I_II, 0, "Only I. 'Please sit down' is imperative (request)."),
    ("Assertion (A): 'How beautiful the sunset is!' can be changed to 'The sunset is very beautiful.'\nReason (R): In changing exclamatory to assertive, 'How' is usually replaced by 'very'.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Transformation – Types of Sentences": [
        ("1 · Affirmative–Negative, Assertive–Interrogative and Question Tags", ASSERT_QUESTION),
        ("2 · Imperative (Orders/Requests) and Exclamatory (How/What) Sentences", IMPERATIVE_EXCLAIM),
    ],
}

NOTES = {
    "Transformation – Types of Sentences": [
        {"title": "Types of sentences – transformation rules", "md": """## Kinds of sentences (by function)
Assertive/declarative · Interrogative · Imperative (order, request, advice) · Exclamatory

## Affirmative ↔ Negative (meaning unchanged)
- always → never + opposite (always punctual = never late)
- only → none but / nothing but
- everyone → no one … not; as … as ↔ not so … as / comparative

## Assertive ↔ Interrogative
- Yes/no: put the auxiliary first; no auxiliary → do/does/did + V1 (Did they **go**?)
- Wh-: Wh + aux + subject + V1; subject question → no do (Who broke it?)
- Rhetorical: positive question = strong negative (Can anyone bear it? = No one can bear it); negative question = positive

## Question tags
- Positive statement → negative tag; negative → positive
- Repeat the auxiliary; none → do/does/did; pronoun subject
- I am → **aren't I?**; Let's → **shall we?**; imperative → **will you?**
- nobody/never/hardly/seldom → positive tag (Nobody came, **did they**?)

## Exclamatory ↔ Assertive
- What + a/an + adj + noun …! ↔ It is a very …
- How + adj/adv + subject + verb! ↔ … very …
- Wish: O that…! / If only…! ; sorrow: Alas! ; joy: Hurrah!

## Imperative ↔ Assertive
- Order: Do it → You should/must do it
- Request: Please… → I request you to…
- Let us… → I propose/suggest that we should…
- Negative: Don't… / Never… → You should not / never…
"""}],
}
