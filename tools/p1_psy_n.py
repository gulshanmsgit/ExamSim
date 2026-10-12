"""Paper 1 · Educational Psychology · P1-PSY-17 Learning Theories – Trial & Error, Classical Conditioning (2 sub-topics × 20), with
revision NOTES. Coverage (planner): Thorndike; Pavlov.
References: E. L. Thorndike, Animal Intelligence (1898/1911) and Educational Psychology (1913); I. P. Pavlov, Conditioned Reflexes (1927);
J. B. Watson & R. Rayner (1920); S. K. Mangal, Advanced Educational Psychology; Woolfolk, Educational Psychology. REAL previous-year
questions come from KSET Education 2023 and 2025 and GFGC 2021 Education (options read from the page images); answers were worked out
by ExamSim and say so."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KSET Education / TET). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

THORNDIKE = [
    ("Match List-I and List-II in the following:\n(Learning Theory) (a) Trial & Error  (b) Classical Conditioning  (c) Operant Conditioning  (d) Learning by Insight\n"
     "(Psychologists) (i) B.F. Skinner  (ii) Kohler  (iii) Thorndike  (iv) Pavlov",
     ["a-iii, b-iv, c-i, d-ii", "a-iii, b-ii, c-i, d-iv", "a-ii, b-iii, c-iv, d-i", "a-iv, b-ii, c-iii, d-i"], 0,
     "Thorndike – trial and error; Pavlov – classical; Skinner – operant; Köhler – insight." + NOTE, "GFGC 2021 Education · Q33"),
    ("Match List-I with List-II\n(Theory of learning) a) Trial and Error  b) Classical Conditioning  c) Operant Conditioning  d) Learning by Insight\n"
     "(Main tenet) i. Mental abilities are involved in the process of learning  ii. Reinforcement is used  iii. Sign learning is done  iv. Artificial stimulus is used  v. Law of exercise",
     ["a-i, b-ii, c-iii, d-v", "a-i, b-iii, c-ii, d-iv", "a-v, b-iv, c-ii, d-i", "a-iii, b-ii, c-iv, d-v"], 2,
     "Trial and error – laws of exercise/effect; classical – an artificial (conditioned) stimulus such as a bell; operant – reinforcement; insight – mental/cognitive." + NOTE,
     "KSET 2025 Education · Q28"),
    ("Match List-I with List-II:\n(Problem solving strategy) a. Trial and Error  b. Algorithm  c. Heuristic  d. Insight\n"
     "(Description) i. Using previous experience and knowledge to solve problems  ii. Applying systematic step-by-step procedure  iii. Trying different solutions till it works  "
     "iv. Suddenly realizing solutions without a systematic approach",
     ["a-i, b-ii, c-iii, d-iv", "a-ii, b-i, c-iv, d-iii", "a-iv, b-iii, c-ii, d-i", "a-iii, b-ii, c-i, d-iv"], 3,
     "Heuristics are rules of thumb drawn from experience." + NOTE, "KSET 2023 Education · Q3"),
    ("Thorndike's theory of learning is also called:",
     ["Connectionism (S–R bond theory)", "Gestalt theory", "Cognitive field theory", "Social learning theory"], 0,
     PYQ + "Learning = forming connections (bonds) between stimulus and response."),
    ("In Thorndike's classic experiment, a hungry cat learnt to escape from a:",
     ["Puzzle box to reach food outside", "Skinner box by pressing a lever", "Maze to find cheese", "Cage by insight with sticks"], 0,
     "Time taken to escape fell gradually over trials – the 'learning curve'."),
    ("The gradual fall in errors and time over trials in Thorndike's experiment shows that learning is:",
     ["Gradual, by trial and error, not sudden insight", "Sudden", "Innate", "Impossible for animals"], 0, PYQ + "Contrast with Köhler's sudden insight in chimpanzees."),
    ("Thorndike's three primary laws of learning are:",
     ["Law of readiness, law of exercise and law of effect", "Law of similarity, contrast and contiguity", "Law of primacy, recency and intensity", "Law of closure, proximity and similarity"], 0,
     PYQ + "Gestalt laws: closure, proximity, similarity."),
    ("'Satisfying results strengthen a connection; annoying results weaken it' is Thorndike's:",
     ["Law of effect", "Law of readiness", "Law of exercise", "Law of disuse"], 0, "Basis of the use of rewards in teaching."),
    ("'Practice makes a man perfect' is the essence of the:",
     ["Law of exercise (use and disuse)", "Law of effect", "Law of readiness", "Law of multiple response"], 0, PYQ + "Law of use strengthens; law of disuse weakens connections."),
    ("A teacher first arouses students' interest and motivation before starting a new lesson. This applies Thorndike's:",
     ["Law of readiness", "Law of effect", "Law of exercise", "Law of analogy"], 0, "Readiness – when the learner is prepared, acting is satisfying."),
    ("Which of the following is one of Thorndike's subsidiary (secondary) laws?",
     ["Law of multiple response", "Law of closure", "Law of Prägnanz", "Law of reinforcement schedules"], 0,
     PYQ + "Others: set or attitude, prepotency of elements, response by analogy, associative shifting."),
    ("Thorndike's 'law of response by analogy' says that in a new situation the learner:",
     ["Responds as in a similar situation met before", "Makes random responses only", "Does not respond", "Responds only after reward"], 0, "Linked to transfer of learning."),
    ("Thorndike later revised his laws; which law did he weaken most?",
     ["The law of exercise – mere repetition without reward does not ensure learning", "The law of effect", "The law of readiness", "None of them"], 0,
     PYQ + "He also stressed that reward works better than punishment."),
    ("Which classroom practice is based on trial-and-error learning?",
     ["Letting students try different ways to solve a puzzle, with feedback", "Giving the answer before the problem", "Only lecturing", "Punishing every mistake"], 0,
     "Useful for motor skills such as typing, cycling."),
    ("Thorndike is called the 'father of educational psychology' mainly because he:",
     ["Applied experimental methods to learning and wrote 'Educational Psychology' (1903, 1913)", "Discovered classical conditioning", "Founded psychoanalysis", "Proposed multiple intelligences"], 0,
     PYQ + "He also contributed to measurement of intelligence and achievement."),
    ("A limitation of the trial-and-error theory is that it:",
     ["Neglects the role of understanding and insight", "Ignores practice", "Ignores reward", "Applies only to children"], 0, "Gestalt psychologists criticised it as mechanical."),
    ("In the law of effect, which statement is correct?",
     ["Rewards should follow the correct response immediately", "Punishment works better than reward", "Delay in reward always helps", "Effect does not matter"], 0, PYQ + "Immediate feedback strengthens the bond."),
    ("The S–R in 'S–R bond' stands for:",
     ["Stimulus – Response", "Sensation – Reaction", "Skill – Reward", "Situation – Reflex"], 0, "Connections between situations and responses."),
    ("Consider the statements:\nI. Thorndike experimented with cats in a puzzle box.\nII. Thorndike's law of effect says punishment strengthens learning more than reward.\nWhich is/are correct?",
     I_II, 0, "Only I."),
    ("Assertion (A): Teachers should praise correct answers immediately.\nReason (R): According to the law of effect, satisfying consequences strengthen the S–R connection.",
     AR, 0, "R explains A."),
]

PAVLOV = [
    ("Ivan Pavlov, a Russian physiologist, discovered classical conditioning while studying:",
     ["Digestion (salivation) in dogs", "Problem solving in cats", "Insight in chimpanzees", "Lever pressing in rats"], 0,
     PYQ + "He received the Nobel Prize (1904) for work on digestion."),
    ("In Pavlov's experiment, the food that naturally caused salivation was the:",
     ["Unconditioned stimulus (UCS)", "Conditioned stimulus (CS)", "Neutral response", "Conditioned response"], 0, "Natural salivation to food = unconditioned response (UCR)."),
    ("The bell, which at first produced no salivation, was originally a:",
     ["Neutral stimulus that became the conditioned stimulus", "Unconditioned stimulus", "Unconditioned response", "Reinforcer in operant learning"], 0,
     PYQ + "After repeated pairing with food, the bell alone caused salivation."),
    ("Salivation to the bell alone after repeated pairing is the:",
     ["Conditioned response (CR)", "Unconditioned response", "Unconditioned stimulus", "Spontaneous recovery"], 0, "CS → CR."),
    ("For classical conditioning to occur most effectively, the conditioned stimulus should be presented:",
     ["Just before the unconditioned stimulus", "Long after the unconditioned stimulus", "Only once", "Without the unconditioned stimulus ever"], 0,
     PYQ + "Forward (delayed) conditioning; backward conditioning is weak."),
    ("When the bell is sounded repeatedly without food, salivation gradually stops. This is:",
     ["Extinction", "Generalisation", "Discrimination", "Higher-order conditioning"], 0, "Extinction is not forgetting; the response can reappear."),
    ("After extinction and a rest, the conditioned response suddenly reappears on hearing the bell. This is:",
     ["Spontaneous recovery", "Discrimination", "Generalisation", "Inhibition"], 0, PYQ + "Shows the response was suppressed, not erased."),
    ("A dog conditioned to a bell also salivates to a similar-sounding buzzer. This is:",
     ["Stimulus generalisation", "Stimulus discrimination", "Extinction", "Spontaneous recovery"], 0, "Responding to stimuli similar to the CS."),
    ("A dog learns to salivate to a high-pitched bell but not a low-pitched one (only the first is followed by food). This is:",
     ["Stimulus discrimination", "Generalisation", "Extinction", "Higher-order conditioning"], 0, PYQ + "Differential reinforcement."),
    ("When a conditioned stimulus (bell) is used to condition a new neutral stimulus (light) without food, it is called:",
     ["Higher-order (second-order) conditioning", "Extinction", "Operant conditioning", "Insight"], 0, "The bell acts like the UCS for the light."),
    ("J. B. Watson's 'Little Albert' experiment (1920) showed that:",
     ["Fear can be learnt through classical conditioning", "Insight solves problems", "Rewards strengthen responses", "Intelligence is inherited"], 0,
     PYQ + "A white rat was paired with a loud noise; Albert's fear generalised to other furry objects."),
    ("A child who was scolded harshly in maths class develops anxiety on seeing a maths book. This is best explained by:",
     ["Classical conditioning", "Insight learning", "Social learning only", "Trial and error"], 0, "The book became a conditioned stimulus for fear."),
    ("Gradually exposing a person to a feared object while keeping them relaxed (to remove a conditioned fear) is:",
     ["Systematic desensitisation", "Flooding with punishment", "Positive reinforcement", "Shaping"], 0, PYQ + "Developed by Joseph Wolpe; based on counter-conditioning."),
    ("Classical conditioning mainly explains the learning of:",
     ["Involuntary (reflex) and emotional responses", "Complex problem solving", "Voluntary skills like writing", "Abstract reasoning"], 0, "Operant conditioning explains voluntary behaviour."),
    ("In classical conditioning, the learner's role is mainly:",
     ["Passive – the response is elicited by a stimulus", "Active – the learner operates on the environment", "Insightful", "Imitative"], 0, PYQ + "In operant conditioning the response is emitted by the learner."),
    ("Which school practice uses classical conditioning to create a positive attitude?",
     ["Making the classroom warm and pleasant so that school becomes linked with good feelings", "Giving homework daily", "Using only textbooks", "Strict silence"], 0,
     "Pleasant associations build liking for school and subjects."),
    ("Pavlov's classical conditioning is also called:",
     ["Respondent conditioning / Type S conditioning", "Instrumental conditioning", "Operant conditioning", "Observational learning"], 0, PYQ + "Skinner called operant conditioning Type R."),
    ("Who is regarded as the founder of behaviourism, who built on Pavlov's work?",
     ["J. B. Watson", "Carl Rogers", "Sigmund Freud", "Wilhelm Wundt"], 0, "Watson, 'Psychology as the Behaviorist Views It' (1913)."),
    ("Consider the statements:\nI. In classical conditioning the bell is the conditioned stimulus.\nII. Extinction means the response is permanently erased.\nWhich is/are correct?",
     I_II, 0, "Only I. Spontaneous recovery shows extinction is not permanent erasure."),
    ("Assertion (A): Pupils may come to fear a subject that was taught harshly.\nReason (R): A neutral stimulus repeatedly paired with an unpleasant experience can come to produce fear.",
     AR, 0, "Classical conditioning of emotions; R explains A."),
]

TOPICS = {
    "Learning Theories – Trial & Error, Classical Conditioning": [
        ("1 · Thorndike – Trial and Error, Connectionism and Laws of Learning", THORNDIKE),
        ("2 · Pavlov – Classical Conditioning and its Educational Implications", PAVLOV),
    ],
}

NOTES = {
    "Learning Theories – Trial & Error, Classical Conditioning": [
        {"title": "Thorndike and Pavlov – revision sheet", "md": """## Thorndike – trial and error (connectionism, S–R bond)
- Experiment: hungry **cat in a puzzle box**, food outside; time to escape fell gradually → learning curve
- **Primary laws:** readiness · exercise (use/disuse) · **effect** (satisfying results strengthen bonds)
- Subsidiary laws: multiple response, set/attitude, prepotency of elements, response by analogy, associative shifting
- Later revision: exercise alone not enough; reward stronger than punishment
- 'Father of educational psychology' (Educational Psychology, 1903/1913)
- Classroom: motivate first (readiness), practice with feedback (exercise), immediate praise (effect)
- Criticism: mechanical, ignores understanding (Gestalt)

## Pavlov – classical conditioning (respondent, Type S)
- Dogs, digestion research; Nobel Prize 1904
| Term | Example |
|---|---|
| UCS | food |
| UCR | salivation to food |
| NS → CS | bell |
| CR | salivation to bell |
- CS just before UCS (forward/delayed) works best
- **Extinction** (CS without UCS), **spontaneous recovery**, **generalisation**, **discrimination**, **higher-order conditioning**
- Watson & Rayner – **Little Albert** (1920): conditioned fear; Watson – founder of behaviourism
- Wolpe – **systematic desensitisation** (counter-conditioning)
- Explains involuntary and emotional learning (school phobia, liking for a teacher)

## Compare
| | Classical (Pavlov) | Operant (Skinner) | Trial & error (Thorndike) | Insight (Köhler) |
|---|---|---|---|---|
| Key | stimulus pairing | reinforcement | law of effect/exercise | sudden understanding |
| Learner | passive | active | active | active, cognitive |
"""}],
}
