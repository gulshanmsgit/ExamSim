"""P2 · Unit 10 – Artificial Intelligence · second, DETAILED note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". The first short sheets stay in p2u10_a/b.
Worked examples (A* vs greedy, minimax and alpha–beta, perceptron for AND, entropy, certainty factors) were computed with a
script on 19 Oct 2026. Facts follow Russell & Norvig (AIMA) and Rich & Knight."""

TOPICS = {}  # notes only

T = " – detailed notes with worked examples"

NOTES = {
    "Approaches to AI": [{"title": "Approaches to AI" + T, "md": """## Four views of AI (Russell & Norvig)
| | Human-like | Rational |
|---|---|---|
| **Thinking** | cognitive modelling (think like humans) | laws of thought (logic) |
| **Acting** | **Turing test** (act like humans) | **rational agent** (do the right thing) – the textbook's approach |

## Turing test (Alan Turing, 1950, "Computing Machinery and Intelligence")
- An interrogator chats in text with a human and a machine; if they can't tell which is which, the machine passes ("imitation game")
- Needs NLP, knowledge representation, automated reasoning, machine learning; the **total** Turing test adds vision and robotics
- Criticism: Searle's **Chinese Room** (symbol manipulation without understanding); **CAPTCHA** = reverse Turing test
- History: term "AI" coined by **John McCarthy** at the **Dartmouth conference, 1956**; Logic Theorist (Newell & Simon), LISP (McCarthy 1958), ELIZA (Weizenbaum 1966), expert systems (1970s–80s: MYCIN, DENDRAL), AI winters, Deep Blue beat Kasparov (1997), Watson (2011), AlphaGo (2016), large language models (2020s)

## Rational agents
- **Agent** perceives the environment through **sensors** and acts through **actuators**; agent function maps percept sequences to actions
- **Rational agent**: picks the action expected to maximise its **performance measure** given its percepts and knowledge
- **PEAS** description – taxi: Performance (safe, fast, legal), Environment (roads, traffic), Actuators (steering, brake), Sensors (camera, GPS)
- Environment types: fully vs **partially observable**, deterministic vs **stochastic**, episodic vs **sequential**, static vs **dynamic**, discrete vs continuous, single vs multi-agent (crossword: fully observable, deterministic, static; taxi: the hard end of everything)
- Agent types: **simple reflex** (condition–action rules), **model-based reflex** (internal state), **goal-based**, **utility-based**, **learning** agents (critic, learning element, problem generator)

## State-space representation
- Problem = **initial state, actions (operators), transition model, goal test, path cost**
- State space = graph of states; solution = path from initial to goal state
- Examples: **8-puzzle** (9!/2 = 181,440 reachable states), water-jug (4 L and 3 L jugs → get 2 L), missionaries and cannibals, 8-queens, Tower of Hanoi, route finding
- Water jug solution: (0,0) → (0,3) → (3,0) → (3,3) → (4,2) → (0,2) → (2,0)

## Heuristic search
- **Heuristic** h(n) = estimated cost from n to the goal; admissible if it never overestimates
- 8-puzzle heuristics: h₁ = misplaced tiles, h₂ = **Manhattan distance** (h₂ dominates h₁)
- **Hill climbing**: move to the best neighbour; problems – **local maxima, plateaus, ridges**; fixes – random restarts, sideways moves, **simulated annealing** (accept worse moves with probability e^(−ΔE/T)), **local beam search**, **genetic algorithms** (selection, crossover, mutation)
- Best-first, A*, AO* (AND–OR graphs), constraint satisfaction (backtracking, forward checking, arc consistency), means–ends analysis

## Game playing
- **Minimax**: MAX picks the highest, MIN the lowest backed-up value
  - Root MAX with MIN children whose leaves are (3, 12, 8), (2, 4, 6), (14, 5, 2) → MIN values 3, 2, 2 → **root value 3**
- **Alpha–beta pruning**: α = best for MAX so far, β = best for MIN; prune when α ≥ β; same answer as minimax
  - In the tree above, after the first child gives α = 3, the second child's first leaf 2 ≤ 3 prunes its remaining 2 leaves → **2 leaves pruned**
  - Best ordering: O(b^(d/2)) instead of O(bᵈ) → can search twice as deep
- Evaluation functions for cut-off depth; Monte Carlo tree search (AlphaGo); chess branching factor ≈ 35

## Traps
- "AI" was coined in 1956 at Dartmouth (McCarthy); the Turing test is from 1950
- Hill climbing is greedy local search – it can get stuck
- Alpha–beta never changes the minimax value, only saves work"""}],

    "Knowledge Representation": [{"title": "Knowledge representation" + T, "md": """## What a KR scheme must offer
Representational adequacy, inferential adequacy, inferential efficiency, acquisitional efficiency. Kinds of knowledge: declarative (facts) vs procedural (how-to), meta-knowledge, heuristic, structural.

## Logic
- **Propositional logic**: simple, no objects/relations
- **First-order predicate logic (FOPL)**: objects, predicates, functions, quantifiers – "All men are mortal": ∀x Man(x) → Mortal(x)
- Inference: modus ponens, **unification** (find substitutions: Knows(John, x) and Knows(y, Mother(y)) unify with {y/John, x/Mother(John)}), **resolution** (convert to **CNF/clausal form**, negate the goal, derive the empty clause – refutation), forward and backward chaining
- Skolemisation removes ∃ (∃x Loves(x, Mary) → Loves(A, Mary))
- Horn clauses → **Prolog**: `mortal(X) :- man(X).  man(socrates).  ?- mortal(socrates).` → yes

## Semantic networks
- Graph of nodes (concepts/objects) and labelled arcs (**IS-A**, **A-KIND-OF**, HAS-PART, instance); **inheritance** of properties along IS-A links
- Example: Tweety –IS-A→ Bird –IS-A→ Animal; Bird –CAN→ Fly
- Weak at quantifiers and exceptions (penguins); Quillian (1968)

## Frames (Marvin Minsky, 1975)
- Structured records for stereotyped objects: **slots** and **fillers**, default values, **procedural attachments** (if-needed, if-added demons), inheritance via a-kind-of hierarchy
- Frame "Hotel room": slots bed, phone, location; default check-out 12:00
- Basis of object-oriented knowledge representation

## Scripts (Schank & Abelson, 1977)
- Stereotyped **sequences of events**: entry conditions, roles, props, scenes, results – the classic **restaurant script** (entering, ordering, eating, paying, leaving)
- Allows answering questions about events not stated explicitly

## Conceptual dependency (Roger Schank)
- Language-independent meaning using **primitive acts**: **ATRANS** (transfer possession – give), **PTRANS** (physical transfer – go), MTRANS (mental – tell), MBUILD, PROPEL, MOVE, GRASP, INGEST, EXPEL, SPEAK, ATTEND
- "John gave Mary a book" → John ATRANS book from John to Mary

## Rules and ontologies
- **Production rules**: IF condition THEN action; working memory + rule base + inference engine; conflict resolution (specificity, recency)
- **Ontology**: formal specification of concepts and relations in a domain (classes, properties, instances) – OWL, RDF, WordNet; upper ontologies; description logics

## Expert systems
- Components: **knowledge base** (facts + rules), **inference engine** (forward chaining – data-driven; backward chaining – goal-driven), **user interface**, **explanation facility**, knowledge-acquisition module, working memory
- Built by a **knowledge engineer** with a **domain expert**; shells (e.g. EMYCIN, CLIPS)
- Famous: **MYCIN** (blood infections, certainty factors, backward chaining), **DENDRAL** (molecular structure – first expert system), XCON/R1 (VAX configuration), PROSPECTOR (geology)

## Reasoning under uncertainty
- **Probability / Bayesian networks** (DAG + conditional probability tables; Bayes' rule)
- **Certainty factors** (MYCIN): CF ∈ [−1, 1]; combining two positive CFs: CF = CF₁ + CF₂(1 − CF₁) → 0.6 and 0.4 give **0.76**
- **Dempster–Shafer** theory (belief and plausibility); **fuzzy logic** (Zadeh, 1965 – degrees of membership 0..1; AND = min, OR = max, NOT = 1 − μ); non-monotonic reasoning (default logic, circumscription)

## Traps
- Frames = objects with slots; scripts = event sequences
- MYCIN used backward chaining and certainty factors
- Resolution proves by contradiction (refutation)"""}],

    "Problem Solving by Searching": [{"title": "Search strategies" + T, "md": """## Problem-solving agent
Formulate goal → formulate problem (states, actions, goal test, path cost) → search → execute. Search tree nodes store state, parent, action, path cost g(n), depth.
- Measures: **completeness**, **optimality**, **time**, **space** in terms of b (branching factor), d (depth of shallowest goal), m (max depth)

## Uninformed (blind) search
| Strategy | Frontier | Complete | Optimal | Time | Space |
|---|---|---|---|---|---|
| **BFS** | FIFO queue | yes | yes (unit costs) | O(bᵈ) | **O(bᵈ)** |
| **Uniform-cost** | priority queue on g | yes | **yes** | O(b^(1 + C*/ε)) | same |
| **DFS** | LIFO stack | no (infinite paths) | no | O(bᵐ) | **O(bm)** |
| Depth-limited | stack, limit l | no | no | O(bˡ) | O(bl) |
| **Iterative deepening (IDDFS)** | DFS with limits 0, 1, 2 … | yes | yes (unit costs) | O(bᵈ) | **O(bd)** |
| **Bidirectional** | two BFS frontiers meeting | yes | yes | **O(b^(d/2))** | O(b^(d/2)) |
- IDDFS repeats shallow levels but costs only about b/(b − 1) times BFS – the preferred uninformed method for large spaces
- b = 10, d = 6: BFS ≈ 10⁶ nodes in memory; bidirectional ≈ 2 × 10³

## Informed (heuristic) search
- **Greedy best-first**: expand the node with the smallest **h(n)** – fast but not optimal or complete
- **A\\***: expand the smallest **f(n) = g(n) + h(n)**; **optimal if h is admissible** (tree search) or **consistent** (graph search); complete
- **Admissible**: h(n) ≤ true cost h*(n); **consistent (monotone)**: h(n) ≤ c(n, n′) + h(n′) (consistent ⇒ admissible)
- Worked: edges S–A 1, S–B 4, A–B 2, A–C 5, A–D 12, B–C 2, C–D 3; h: S 7, A 6, B 4, C 3, D 0
  - **A\\*** expands S (f 7), A (7), B (1 + 2 + 4 = 7), C (5 + 3 = 8), D → path **S A B C D, cost 8** (optimal)
  - **Greedy** follows the smallest h: S → B → C → D, cost **9** (not optimal)
- Memory-bounded: IDA*, RBFS, SMA*; A* with h = 0 is uniform-cost search
- Heuristic quality: **effective branching factor** b*; a heuristic h₂ **dominates** h₁ if h₂ ≥ h₁ everywhere (and both admissible) – it expands fewer nodes
- Relaxed problems give admissible heuristics (8-puzzle: tiles can move anywhere → misplaced tiles; move to adjacent squares → Manhattan distance)

## Traps
- BFS is optimal only when all step costs are equal
- DFS uses linear memory but may never finish
- A* with an inadmissible heuristic may return a sub-optimal path"""}],

    "Natural Language Processing": [{"title": "Natural language processing" + T, "md": """## Levels of language analysis
**Phonology** (sounds) → **morphology** (word structure – stems, affixes: un-happi-ness) → **syntax** (sentence structure) → **semantics** (meaning) → **pragmatics** (meaning in context/intent) → **discourse** (across sentences – anaphora "he", "it") → world knowledge

## Grammars and languages
- Formal grammar G = (V, Σ, P, S); **Chomsky hierarchy**: regular ⊂ context-free ⊂ context-sensitive ⊂ unrestricted
- Natural-language syntax is mostly described with **context-free grammars (CFGs)**:
```
S  → NP VP          NP → Det N | Det Adj N | Name
VP → V NP | V NP PP PP → P NP
Det → the | a        N → dog | park   V → saw   P → in
```
"the dog saw a cat in the park" → parse tree with S at the root; the PP can attach to the verb or to "a cat" → **ambiguity**
- Other formalisms: **transition networks (ATN** – augmented transition networks, Woods), definite clause grammars (Prolog), unification grammars, dependency grammar

## Parsing techniques
- **Top-down** (start from S, expand – recursive descent; problem: left recursion) vs **bottom-up** (start from words, reduce – shift-reduce)
- **Chart parsing / dynamic programming**: **CYK** (needs Chomsky normal form, O(n³)), **Earley** parser (any CFG)
- Probabilistic CFGs choose the most likely parse; deterministic parsing; part-of-speech (POS) tagging with HMMs; tokenisation, stemming (Porter) vs lemmatisation, stop-word removal

## Ambiguity
- **Lexical** ("bank" – river/money), **syntactic/structural** ("I saw the man with the telescope"), **semantic**, **referential/anaphoric** ("John told Bill he won"), pragmatic

## Semantic analysis
- Map syntax to meaning: logical forms (FOPL), semantic grammars, **case grammar** (Fillmore – agent, object, instrument, location), conceptual dependency, word-sense disambiguation, semantic role labelling
- Lexical semantics: synonyms, antonyms, hypernyms (WordNet)

## Pragmatics and discourse
- Speech acts (request, promise), implicature, coherence, **anaphora resolution**, dialogue management

## Applications
Machine translation (rule-based → statistical → neural; Google Translate, Bhashini for Indian languages), information retrieval and search, question answering, chatbots and virtual assistants, sentiment analysis, text summarisation, speech recognition, spell/grammar checking, named-entity recognition, spam filtering
- Modern NLP: word embeddings (word2vec), **transformers** (attention, 2017), large language models (BERT, GPT)

## Traps
- Pragmatics = meaning in context; semantics = literal meaning
- CYK requires Chomsky normal form
- Morphology deals with word structure, syntax with sentence structure"""}],

    "Artificial Neural Networks & Applications": [{"title": "Neural networks and learning" + T, "md": """## Biological to artificial neuron
- **McCulloch–Pitts neuron (1943)**: weighted sum of binary inputs compared with a threshold
- Artificial neuron: y = f(Σ wᵢxᵢ + b) – weights, bias, **activation function**
| Activation | Formula | Range / note |
|---|---|---|
| Step (threshold) | 1 if net ≥ θ else 0 | perceptron |
| **Sigmoid** | 1/(1 + e⁻ˣ) | (0, 1); sigmoid(0) = 0.5, sigmoid(2) ≈ 0.881; vanishing gradients |
| tanh | (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ) | (−1, 1) |
| **ReLU** | max(0, x) | fast, used in deep nets |
| Softmax | eˣⁱ/Σeˣʲ | probabilities for classes |

## Perceptron (Frank Rosenblatt, 1958)
- Single layer; learning rule **wᵢ ← wᵢ + η(t − y)xᵢ**, b ← b + η(t − y)
- Learns only **linearly separable** functions (AND, OR, NOT) – **not XOR** (Minsky & Papert, 1969 → first AI winter)
- Worked: AND, η = 1, start w = (0, 0), b = 0 → converges to **w = (2, 1), b = −2** (one valid separating line)

## Multilayer networks and backpropagation
- Input layer → hidden layer(s) → output layer; feed-forward; a hidden layer lets the net learn XOR and any continuous function (universal approximation)
- **Backpropagation** (Rumelhart, Hinton, Williams, 1986): forward pass → error at output → propagate error gradients backwards (chain rule) → update weights by **gradient descent** (w ← w − η ∂E/∂w)
- Learning rate, epochs, batch / stochastic / mini-batch gradient descent, momentum; overfitting → regularisation, dropout, early stopping
- Other networks: **Hopfield** (recurrent, associative memory), **Kohonen SOM** (self-organising map, unsupervised), RBF networks, **CNN** (images – convolution, pooling), **RNN/LSTM** (sequences), transformers

## Types of learning
| Type | Data | Examples |
|---|---|---|
| **Supervised** | labelled (input, output) | classification (spam/not), regression (price); decision trees, k-NN, SVM, naive Bayes, neural nets |
| **Unsupervised** | unlabelled | **clustering** (k-means), association rules, dimensionality reduction (PCA) |
| **Reinforcement** | rewards/penalties from an environment | game playing, robotics; agent, state, action, reward, policy; **Q-learning**; exploration vs exploitation |
| Semi-supervised, self-supervised | few labels / labels from data itself | |
- **Decision tree (ID3)**: choose the attribute with the highest **information gain**; entropy of 9 positive / 5 negative examples = **0.940** bits
- Evaluation: training/test split, cross-validation, confusion matrix, accuracy, precision, recall, F1

## Applications of AI
Medical diagnosis and imaging, agriculture (crop disease detection, weather), education (adaptive tutoring), finance (fraud detection, credit scoring), speech and face recognition, self-driving vehicles, recommendation systems, robotics, smart cities, e-governance chatbots; India – **IndiaAI Mission** (2024), Bhashini (language translation)
- Ethics: bias, privacy, explainability, job impact

## Traps
- A single perceptron cannot learn XOR
- Backpropagation adjusts weights using the gradient of the error
- Clustering is unsupervised; classification is supervised; reinforcement learning uses rewards"""}],
}
