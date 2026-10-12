"""Paper 1 · Educational Psychology · P1-PSY-14 Transfer of Learning and P1-PSY-15 Learning Styles & Domains of Learning
(2 topics × 2 sub-topics × 20), with revision NOTES.
References: S. K. Mangal, Advanced Educational Psychology; Woolfolk, Educational Psychology; Bloom et al. (1956), Krathwohl, Bloom &
Masia (1964), Anderson & Krathwohl (2001), R. H. Dave (1970), E. J. Simpson (1972), A. J. Harrow (1972); D. A. Kolb (1984); N. Fleming
(VARK, 1987); Honey & Mumford (1986); DSERT D.El.Ed. psychology texts. REAL previous-year questions come from KSET Education 2023 and
2024; answers were worked out by ExamSim and say so. The rest are "PYQ pattern" questions on themes common in KSET Education / TET /
GPSTR papers."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KSET Education / TET). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

TRANSFER_TYPES = [
    ("Transfer of learning means:",
     ["The effect of learning in one situation on learning or performance in another situation", "Moving a student to another school",
      "Forgetting what was learnt", "Learning by rote only"], 0, PYQ + "'Learning for transfer' is the main aim of education."),
    ("When learning to ride a bicycle makes it easier to learn to ride a motorcycle, it is:",
     ["Positive transfer", "Negative transfer", "Zero transfer", "Retroactive inhibition"], 0, PYQ + "Earlier learning helps the new learning."),
    ("A person used to driving on the left finds it hard to drive on the right in another country. This is:",
     ["Negative transfer", "Positive transfer", "Zero transfer", "Bilateral transfer"], 0, "Earlier learning interferes with new learning."),
    ("Learning history has no effect on learning to swim. This is:",
     ["Zero (neutral) transfer", "Positive transfer", "Negative transfer", "Vertical transfer"], 0, PYQ + "No common elements, so no effect."),
    ("Skill learnt with the right hand making it easier to do the same task with the left hand is:",
     ["Bilateral transfer", "Vertical transfer", "Zero transfer", "Negative transfer"], 0, "Transfer from one side of the body to the other."),
    ("Learning addition helps in learning multiplication. This is mainly:",
     ["Vertical transfer", "Lateral transfer", "Zero transfer", "Bilateral transfer"], 0,
     PYQ + "Vertical – lower to higher-level learning; lateral (horizontal) – to a similar level in a different situation."),
    ("Using classroom knowledge of percentages to calculate discounts while shopping is an example of:",
     ["Lateral (horizontal) transfer", "Vertical transfer", "Negative transfer", "Zero transfer"], 0, "Same level of skill applied to a new, everyday situation."),
    ("Which statement about transfer is correct?",
     ["Transfer is more likely when the two situations share common elements", "Transfer is automatic in every case",
      "Transfer happens only in mathematics", "Transfer always reduces learning"], 0, PYQ + "Similarity of content, method and goals increases transfer."),
    ("Which teaching practice best promotes positive transfer?",
     ["Linking lessons to real-life situations and teaching general principles", "Rote memorisation of isolated facts",
      "Teaching each subject in complete isolation", "Avoiding examples"], 0, PYQ + "Understanding, generalisation and varied practice support transfer."),
    ("Proactive interference is related to which kind of transfer?",
     ["Negative transfer – old learning disturbs new learning", "Positive transfer", "Zero transfer", "Bilateral transfer"], 0,
     "Retroactive interference – new learning disturbs recall of old learning."),
    ("Which factor reduces the chance of transfer?",
     ["Learning by rote without understanding", "Meaningful learning", "Practice in many settings", "Learning general principles"], 0, PYQ + "Mechanical learning stays tied to the original setting."),
    ("A teacher teaches 'balance of forces' and then asks students to explain why a boat floats. The teacher is trying to develop:",
     ["Transfer of learning", "Rote memory", "Negative transfer", "Habit of copying"], 0, "Applying a principle to a new situation."),
    ("The learner's attitude 'I can use this elsewhere' increases transfer. This shows the importance of:",
     ["The learner's awareness and intention to transfer", "Fatigue", "Punishment", "Heredity only"], 0, PYQ + "Metacognition and motivation help transfer."),
    ("Learning Kannada grammar helps a student learn Telugu grammar more easily. This is:",
     ["Positive lateral transfer", "Negative vertical transfer", "Zero transfer", "Bilateral transfer"], 0, "Similar languages share elements."),
    ("Learning a new typing layout after years on another layout causes many errors. This shows:",
     ["Negative transfer", "Positive transfer", "Zero transfer", "Vertical transfer"], 0, "Old habits compete with the new responses."),
    ("Which is NOT a type of transfer of learning?",
     ["Reverse-motivation transfer", "Positive transfer", "Lateral transfer", "Sequential (vertical) transfer"], 0, PYQ + "Recognised types: positive, negative, zero; lateral, vertical; bilateral."),
    ("Transfer of training in a skill such as handwriting from one hand to the other was studied in experiments on:",
     ["Bilateral transfer", "Classical conditioning", "Insight", "Imprinting"], 0, "Mirror-drawing experiments are often cited."),
    ("For transfer to occur, which condition is most important?",
     ["Learning must be thorough and understood", "The test must be difficult", "The teacher must be strict", "The class must be small"], 0, PYQ + "Weak learning transfers poorly."),
    ("Consider the statements:\nI. Positive transfer helps new learning.\nII. Zero transfer means the earlier learning makes new learning impossible.\nWhich is/are correct?",
     I_II, 0, "Only I. Zero transfer means no effect at all; interference is negative transfer."),
    ("Assertion (A): Teachers should give examples from many different situations.\nReason (R): Varied practice helps learners generalise and transfer learning.",
     AR, 0, "R explains A."),
]

TRANSFER_THEORIES = [
    ("The 'theory of formal (mental) discipline' of transfer is based on:",
     ["Faculty psychology – the mind has faculties (memory, reasoning) that can be trained like muscles", "Identical elements", "Generalisation of experience", "Gestalt insight"], 0,
     PYQ + "It justified studying Latin and mathematics to 'train the mind'; experiments by William James and Thorndike weakened it."),
    ("Who proposed the 'theory of identical elements' of transfer?",
     ["E. L. Thorndike (with Woodworth)", "C. H. Judd", "W. C. Bagley", "Wolfgang Köhler"], 0, PYQ + "Transfer occurs to the extent that two tasks share identical elements – content, method, attitude."),
    ("C. H. Judd's 'theory of generalisation' of transfer was supported by his experiment on:",
     ["Boys throwing darts at a target under water (refraction)", "Cats in a puzzle box", "Dogs and salivation", "Chimpanzees and sticks"], 0,
     PYQ + "Boys who were taught the principle of refraction adjusted better when the depth changed – principles transfer, not just elements."),
    ("According to Judd, transfer takes place mainly through:",
     ["Understanding of general principles", "Exercise of mental faculties", "Identical stimulus–response bonds only", "Punishment"], 0, "Generalisation of experience."),
    ("The Gestalt explanation of transfer is called the theory of:",
     ["Transposition – transfer of insight into relationships and patterns", "Formal discipline", "Identical elements", "Ideals"], 0,
     PYQ + "Köhler's hens chose the 'lighter' of two shades even with new pairs – they learnt the relationship."),
    ("W. C. Bagley's theory states that transfer takes place through:",
     ["Ideals – values such as neatness or honesty learnt as conscious ideals", "Faculties of the mind", "Identical elements", "Reflexes"], 0,
     "Theory of ideals (generalisation of ideals)."),
    ("Which theory would support teaching Latin to improve reasoning in all subjects?",
     ["Formal discipline", "Identical elements", "Generalisation", "Transposition"], 0, PYQ + "Modern research does not support this general 'mind training'."),
    ("Thorndike found that training in estimating the area of rectangles did not improve estimating other shapes much. This supports:",
     ["Identical elements theory", "Formal discipline theory", "Theory of ideals", "Faculty psychology"], 0, "Little transfer without common elements."),
    ("Teaching a principle and then giving varied applications follows which theory?",
     ["Generalisation (Judd)", "Formal discipline", "Identical elements only", "Mental faculties"], 0, "Principles carry over to new situations."),
    ("Match the theory with the psychologist:\na. Identical elements  b. Generalisation  c. Transposition  d. Ideals\n1. Thorndike  2. Judd  3. Gestalt (Köhler)  4. Bagley",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Formal discipline – faculty psychology (no single founder)."),
    ("The 'transposition' theory holds that what is transferred is:",
     ["The perception of relationships (insight)", "Isolated habits", "Muscle strength", "Exact responses"], 0, "Gestaltists stress the whole pattern."),
    ("The educational implication of the identical-elements theory is that school learning should be:",
     ["Similar to the real-life situations where it will be used", "Abstract and unrelated to life", "Based only on memory drills", "Free of practice"], 0,
     PYQ + "Hence practical, life-related curricula."),
    ("Which statement about the theory of formal discipline is correct?",
     ["It treats the mind as made of separate faculties strengthened by exercise", "It was proposed by Judd", "It is based on Gestalt psychology", "It denies any transfer"], 0, "Faculty psychology."),
    ("Which of the following increases transfer according to most modern views?",
     ["Teaching for understanding, generalisation and metacognition", "More drill on unrelated tasks", "Studying difficult subjects only", "Learning without feedback"], 0,
     PYQ + "Woolfolk: 'high-road' transfer needs mindful abstraction; 'low-road' transfer comes from much practice."),
    ("Judd's experiment showed that the group that knew the principle of refraction:",
     ["Did better when the target's depth was changed", "Did worse than the other group", "Did the same as the other group", "Refused to throw"], 0, "Principle → generalisation → transfer."),
    ("'Low-road' transfer (Salomon and Perkins) happens through:",
     ["Much practice until the skill is automatic", "Conscious abstraction of a principle", "Punishment", "Insight only"], 0, "High-road transfer needs mindful abstraction of principles."),
    ("A student who learns 'honesty in the classroom' and then returns lost money in the market shows transfer of:",
     ["An ideal (Bagley)", "Identical elements", "Mental faculties", "Motor skills"], 0, PYQ + "Ideals and attitudes transfer."),
    ("Which of the following is NOT a theory of transfer of learning?",
     ["Theory of operant conditioning", "Theory of identical elements", "Theory of generalisation", "Theory of formal discipline"], 0, "Operant conditioning is Skinner's learning theory."),
    ("Consider the statements:\nI. Thorndike rejected the theory of formal discipline.\nII. Judd stressed understanding of general principles.\nWhich is/are correct?",
     I_II, 2, "Both are correct."),
    ("Assertion (A): Learning a principle helps solve many new problems.\nReason (R): According to the generalisation theory, principles are what transfer from one situation to another.",
     AR, 0, "R explains A (Judd)."),
]

STYLES = [
    ("Which of the following educational theorists is often associated with Experiential Learning?",
     ["Jean Piaget", "Lev Vygotsky", "B. F. Skinner", "David A. Kolb"], 3,
     "Kolb (1984): concrete experience → reflective observation → abstract conceptualisation → active experimentation." + NOTE, "KSET 2023 Education · Q16"),
    ("Which of the following is a potential limitation of expository learning?",
     ["It encourages excessive creativity and imagination", "It may not cater to diverse learning styles", "It limits student engagement and participation",
      "It depends too heavily on technology"], 1, "Teacher-led explanation suits listeners/readers best; it can leave other styles behind." + NOTE, "KSET 2024 Education · Q33"),
    ("A learning style is:",
     ["A learner's preferred way of taking in and processing information", "A fixed IQ level", "A type of school uniform", "A teaching aid"], 0, PYQ + "Good teaching uses many modes to reach all styles."),
    ("In the VARK model, the letters stand for:",
     ["Visual, Aural, Read/Write, Kinaesthetic", "Verbal, Analytical, Reflective, Kinetic", "Visual, Active, Rational, Knowledge", "Vocal, Auditory, Reading, Kinetic"], 0,
     PYQ + "Proposed by Neil Fleming (1987)."),
    ("A learner who understands best through charts, diagrams and mind-maps is a:",
     ["Visual learner", "Auditory learner", "Kinaesthetic learner", "Read/write learner"], 0, "Use graphic organisers."),
    ("A learner who learns best by doing, touching and moving is a:",
     ["Kinaesthetic (tactile) learner", "Visual learner", "Auditory learner", "Reflective learner"], 0, PYQ + "Use activities, models, role-play, experiments."),
    ("A learner who prefers lectures, discussions and recordings is a(n):",
     ["Auditory (aural) learner", "Visual learner", "Kinaesthetic learner", "Field-dependent learner"], 0, "Use discussion, read-aloud, audio."),
    ("The correct order of Kolb's experiential learning cycle is:",
     ["Concrete experience → Reflective observation → Abstract conceptualisation → Active experimentation",
      "Active experimentation → Concrete experience → Abstract conceptualisation → Reflective observation",
      "Reflective observation → Concrete experience → Active experimentation → Abstract conceptualisation",
      "Abstract conceptualisation → Concrete experience → Reflective observation → Active experimentation"], 0, PYQ + "Kolb's four styles: diverging, assimilating, converging, accommodating."),
    ("In Kolb's model, a learner who prefers abstract conceptualisation and active experimentation (practical problem-solving) is called:",
     ["Converger", "Diverger", "Assimilator", "Accommodator"], 0, "Diverger – CE + RO; assimilator – AC + RO; accommodator – CE + AE."),
    ("Honey and Mumford's four learning styles are:",
     ["Activist, Reflector, Theorist, Pragmatist", "Visual, Aural, Read/Write, Kinaesthetic", "Diverger, Assimilator, Converger, Accommodator", "Field-dependent, Field-independent, Global, Serial"], 0,
     PYQ + "Based on Kolb's cycle."),
    ("Witkin's cognitive style in which a learner can easily separate details from the surrounding context is:",
     ["Field-independent", "Field-dependent", "Impulsive", "Kinaesthetic"], 0, "Field-dependent learners see the whole and prefer social, structured settings."),
    ("A teacher who uses pictures, stories, group activities and demonstrations in one lesson is mainly:",
     ["Addressing different learning styles", "Wasting class time", "Following rote learning", "Using only the lecture method"], 0, PYQ + "Multisensory teaching."),
    ("Which learning style would benefit most from written notes, lists and textbooks?",
     ["Read/Write", "Kinaesthetic", "Aural", "Visual-spatial only"], 0, "VARK."),
    ("Kagan's cognitive style that contrasts quick but error-prone responding with slow, careful responding is:",
     ["Impulsive versus reflective", "Field dependent versus independent", "Visual versus verbal", "Serial versus holistic"], 0, "Reflective learners make fewer errors."),
    ("Howard Gardner's theory, often confused with learning styles, is actually a theory of:",
     ["Multiple intelligences", "Learning styles", "Transfer of learning", "Moral development"], 0, PYQ + "Linguistic, logical-mathematical, spatial, musical, bodily-kinaesthetic, interpersonal, intrapersonal, naturalist."),
    ("A 'global' learner, compared with a 'sequential' learner, prefers to:",
     ["See the big picture first", "Learn in small linear steps", "Avoid examples", "Learn only by memorising"], 0, "Felder–Silverman model."),
    ("Learning by doing, popularised by John Dewey, mainly suits which style?",
     ["Kinaesthetic / experiential", "Purely auditory", "Read/write only", "Rote"], 0, PYQ + "Dewey: 'Learning by doing' and project method."),
    ("Which statement about learning styles is correct?",
     ["Teachers should vary methods so that every learner can participate", "Every student has only one fixed style for life",
      "Learning styles are measured by IQ tests", "Learning styles are the same as intelligence"], 0, "Preferences can change with tasks and age."),
    ("Consider the statements:\nI. Kolb's model is a cycle of four stages.\nII. VARK was proposed by Jean Piaget.\nWhich is/are correct?",
     I_II, 0, "Only I. VARK – Neil Fleming."),
    ("Assertion (A): A single teaching method rarely suits every learner.\nReason (R): Learners differ in the ways they prefer to receive and process information.",
     AR, 0, "R explains A."),
]

DOMAINS = [
    ("In reference to Anderson and Krathwohl's Taxonomy of Cognition which one of the following is correct?",
     ["Remember, Understand, Apply, Analyse, Evaluate and Create", "Knowledge, Comprehension, Application, Analysis and Synthesis",
      "Receiving, Responding, Valuing, Organizing and Characterization", "Attitudes, Values, Interest and Appreciation"], 0,
     "The revised Bloom's taxonomy (2001) uses verbs and puts Create at the top." + NOTE, "KSET 2023 Education · Q45"),
    ("Who is the father of Psychomotor Domains?",
     ["Morrison", "R. H. Dave", "Hunt", "Herbart"], 1,
     "Of the options, R. H. Dave (1970) gave a psychomotor taxonomy; Simpson (1972) and Harrow (1972) gave others." + NOTE, "KSET 2023 Education · Q46"),
    ("Which one of the following is CORRECT of \"R.H. Dave's Taxonomy of Psychomotor Domain\".",
     ["Imitation, Manipulation, Precision, Articulation, Naturalization", "Perception, Set guided, Response mechanism, Adoption",
      "Reflex Movement, Basic fundamental movement, Perceptual ability, Skilled movement, Non-discursive", "Acquiring, Knowledge, Executing Action, Transfer"], 0,
     "Option 2 is Simpson's sequence and option 3 is Harrow's." + NOTE, "KSET 2024 Education · Q74"),
    ("Krathwohl's affective domain focuses on",
     ["Receiving, Responding, Valuing, Organizing and Characterizing", "Receiving, Valuing, Organizing, Responding and Characterizing",
      "Responding, Valuing, Characterizing, Organising and Receiving", "Valuing, Responding, Characterizing, Organising and Receiving"], 0,
     "Krathwohl, Bloom & Masia (1964); the order goes from simple attention to a value system that guides behaviour." + NOTE, "KSET 2024 Education · Q76"),
    ("Bloom's original Taxonomy of Educational Objectives (cognitive domain) was published in:",
     ["1956", "1964", "2001", "1972"], 0, PYQ + "Benjamin Bloom and colleagues; affective 1964; revised cognitive 2001."),
    ("The correct order of the original Bloom's cognitive domain (lowest to highest) is:",
     ["Knowledge, Comprehension, Application, Analysis, Synthesis, Evaluation", "Knowledge, Application, Comprehension, Synthesis, Analysis, Evaluation",
      "Comprehension, Knowledge, Analysis, Application, Evaluation, Synthesis", "Evaluation, Synthesis, Analysis, Application, Comprehension, Knowledge"], 0, PYQ + "Six levels."),
    ("In the revised taxonomy (2001), which level is at the top?",
     ["Create", "Evaluate", "Analyse", "Remember"], 0, "Synthesis was renamed 'Create' and moved above 'Evaluate'."),
    ("The three domains of learning objectives are:",
     ["Cognitive, Affective and Psychomotor", "Visual, Auditory and Kinaesthetic", "Physical, Mental and Spiritual", "Knowledge, Skill and Memory"], 0,
     PYQ + "Head (thinking), heart (feeling) and hands (doing)."),
    ("'Students will appreciate the beauty of nature' is an objective in which domain?",
     ["Affective", "Cognitive", "Psychomotor", "Conative only"], 0, "Attitudes, interests, values, appreciation."),
    ("'Students will draw a neat labelled diagram of the heart' mainly belongs to which domain?",
     ["Psychomotor", "Affective", "Cognitive only", "Social"], 0, PYQ + "Skill of drawing; recalling the labels is cognitive."),
    ("'Students will compare the features of two poems' belongs to which cognitive level?",
     ["Analysis", "Knowledge", "Comprehension", "Application"], 0, "Compare, classify, distinguish – analysis."),
    ("Which action verb best fits the 'Application' level?",
     ["Solve / use", "Define / list", "Judge / justify", "Design / compose"], 0, PYQ + "Define/list – knowledge; judge – evaluation; design – synthesis/create."),
    ("The highest level of Krathwohl's affective domain is:",
     ["Characterisation by a value (value complex)", "Receiving", "Responding", "Valuing"], 0, "The value system becomes part of one's character."),
    ("E. J. Simpson's psychomotor taxonomy (1972) begins with:",
     ["Perception", "Imitation", "Reflex movements", "Naturalisation"], 0,
     "Simpson: perception, set, guided response, mechanism, complex overt response, adaptation, origination."),
    ("The highest level in R. H. Dave's psychomotor taxonomy is:",
     ["Naturalisation", "Imitation", "Precision", "Manipulation"], 0, PYQ + "Skill becomes automatic and natural."),
    ("A. J. Harrow's taxonomy of the psychomotor domain begins with:",
     ["Reflex movements", "Perception", "Imitation", "Origination"], 0, "Harrow: reflex, basic-fundamental, perceptual abilities, physical abilities, skilled movements, non-discursive communication."),
    ("Which objective belongs to the 'Evaluation' level of Bloom's cognitive domain?",
     ["Students will judge which solution is better and give reasons", "Students will recall the formula", "Students will explain in their own words", "Students will list the steps"], 0,
     PYQ + "Judge, justify, criticise, appraise."),
    ("Match the domain with its classifier:\na. Cognitive (1956)  b. Affective (1964)  c. Psychomotor (1970)\n1. Bloom  2. Krathwohl  3. R. H. Dave",
     ["a-1, b-2, c-3", "a-2, b-1, c-3", "a-3, b-2, c-1", "a-1, b-3, c-2"], 0, "Simpson (1972) and Harrow (1972) also classified the psychomotor domain."),
    ("Consider the statements:\nI. 'Valuing' is a level of the affective domain.\nII. 'Synthesis' is the highest level of the revised (2001) taxonomy.\nWhich is/are correct?",
     I_II, 0, "Only I. In the revised taxonomy 'Create' is highest; 'synthesis' was in the 1956 version (fifth level)."),
    ("Assertion (A): Teachers should write objectives in all three domains.\nReason (R): Education aims at the development of knowledge, attitudes and skills.",
     AR, 0, "Head, heart and hand – R explains A."),
]

TOPICS = {
    "Transfer of Learning": [
        ("1 · Meaning, Types and Factors of Transfer", TRANSFER_TYPES),
        ("2 · Theories of Transfer and Educational Implications", TRANSFER_THEORIES),
    ],
    "Learning Styles & Domains of Learning": [
        ("1 · Learning Styles – VARK, Kolb, Honey & Mumford, Cognitive Styles", STYLES),
        ("2 · Domains of Learning – Cognitive, Affective and Psychomotor", DOMAINS),
    ],
}

NOTES = {
    "Transfer of Learning": [
        {"title": "Transfer of learning – revision sheet", "md": """## Meaning
Effect of learning in one situation on learning/performance in another. Aim of education = **learning for transfer**.

## Types
| Type | Meaning | Example |
|---|---|---|
| Positive | helps new learning | cycle → motorcycle |
| Negative | hinders new learning | left-hand → right-hand driving |
| Zero (neutral) | no effect | history → swimming |
| Lateral (horizontal) | same level, new situation | % in class → discount in shop |
| Vertical (sequential) | lower → higher level | addition → multiplication |
| Bilateral | one side of body → other | right hand → left hand |
- Proactive interference ≈ negative transfer (old disturbs new); retroactive = new disturbs old

## Theories
| Theory | Name | Key idea |
|---|---|---|
| Formal / mental discipline | faculty psychology | mind's faculties trained like muscles (Latin, maths) |
| Identical elements | **Thorndike** & Woodworth | transfer ∝ common elements |
| Generalisation | **C. H. Judd** | principles transfer – dart under water (refraction) |
| Transposition | **Gestalt (Köhler)** | relationships / insight transfer – hens & shades |
| Ideals | **W. C. Bagley** | ideals like neatness, honesty transfer |
- Salomon & Perkins: **low-road** (much practice, automatic) vs **high-road** (mindful abstraction)

## Teaching for transfer
Link to real life · teach principles · varied examples · understanding, not rote · metacognition · overlearning of basics
"""}],
    "Learning Styles & Domains of Learning": [
        {"title": "Learning styles and domains of learning – revision sheet", "md": """## Learning styles
| Model | Styles |
|---|---|
| **VARK** – Neil Fleming (1987) | Visual, Aural, Read/Write, Kinaesthetic |
| **Kolb** (1984) cycle | Concrete experience → Reflective observation → Abstract conceptualisation → Active experimentation |
| Kolb styles | Diverger (CE+RO), Assimilator (AC+RO), Converger (AC+AE), Accommodator (CE+AE) |
| Honey & Mumford | Activist, Reflector, Theorist, Pragmatist |
| Witkin | Field-dependent / field-independent |
| Kagan | Impulsive / reflective |
| Felder–Silverman | Global / sequential, active / reflective … |
- Gardner = **multiple intelligences** (not learning styles); Dewey – learning by doing

## Domains of learning (head – heart – hand)
**Cognitive – Bloom 1956:** Knowledge → Comprehension → Application → Analysis → Synthesis → Evaluation
**Revised – Anderson & Krathwohl 2001:** Remember → Understand → Apply → Analyse → Evaluate → **Create**
**Affective – Krathwohl 1964:** Receiving → Responding → Valuing → Organisation → Characterisation
**Psychomotor:**
| Author | Levels |
|---|---|
| **R. H. Dave 1970** | Imitation → Manipulation → Precision → Articulation → Naturalisation |
| E. J. Simpson 1972 | Perception → Set → Guided response → Mechanism → Complex overt response → Adaptation → Origination |
| A. J. Harrow 1972 | Reflex → Basic-fundamental → Perceptual → Physical abilities → Skilled movements → Non-discursive communication |

## Action verbs
Knowledge – define, list · Comprehension – explain · Application – solve, use · Analysis – compare, classify · Synthesis/Create – design, compose · Evaluation – judge, justify

## ⚠ Traps
- Revised taxonomy: Create is ABOVE Evaluate
- Krathwohl: Receiving → Responding → Valuing (not valuing first)
"""}],
}
