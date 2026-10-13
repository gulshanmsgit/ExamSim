"""Paper 2 · Unit 10 · P2-U10-01 Approaches to AI, P2-U10-02 Knowledge Representation and P2-U10-03 Problem Solving by Searching
(3 topics × 2 sets × 30), with revision NOTES.
References: Stuart Russell & Peter Norvig, Artificial Intelligence – A Modern Approach (2nd/3rd ed.); Elaine Rich & Kevin Knight,
Artificial Intelligence (production systems, problem characteristics, scripts, conceptual dependency). Each set mixes REAL previous-year
questions (exact wording, printed option order, `source`) with new ones. KSET 2023–25 questions come from packs/pyq-p2.json; GFGC 2021
answers were worked out by ExamSim (no official key). Search traces, minimax/alpha-beta values and heuristic values were worked out by hand."""
from p2u7_a import kset, PYQ, NOTE

TURING_AGENTS = [
    kset("KSET 2023 CS&A · Q71"),
    kset("KSET 2024 CS&A · Q91"),
    kset("KSET 2025 CS&A · Q91"),
    kset("KSET 2024 CS&A · Q92"),
    ("Which of the following is a proposed means of testing the intelligence of a machine?", ["Turing Test", "Turning Test", "Tuning Test", "Timing Test"], 0,
     "Turing's 'imitation game' (1950)." + NOTE, "GFGC 2021 CS · Q113"),
    ("An agent is composed of", ["Architecture", "Agent function", "Perception sequence", "Architecture and program"], 3,
     "Agent = architecture + program (Russell & Norvig)." + NOTE, "GFGC 2021 CS · Q116"),
    ("The process of removing details from a given state representation is called", ["Extraction", "Abstraction", "Information Retrieval", "Mining of data"], 1,
     "Abstraction keeps only what matters for the problem." + NOTE, "GFGC 2021 CS · Q117"),
    ("The field that investigates the mechanics of human intelligence is", ["Psychology", "Cognitive Science", "Sociology", "Learning"], 1,
     "Cognitive science combines AI models with psychology." + NOTE, "GFGC 2021 CS · Q118"),
    ("Russell and Norvig group definitions of AI into four approaches:", ["Thinking humanly, acting humanly, thinking rationally and acting rationally",
                                                                         "Search, logic, learning and vision", "Weak, strong, narrow and general AI",
                                                                         "Symbolic, connectionist, evolutionary and fuzzy"], 0,
     PYQ + "Acting humanly = Turing test; thinking rationally = laws of thought; acting rationally = rational agents."),
    ("The Turing test was proposed by", ["Alan Turing, in 1950", "John McCarthy, in 1956", "Marvin Minsky, in 1969", "Herbert Simon, in 1957"], 0,
     "Paper: 'Computing Machinery and Intelligence'."),
    ("The term 'Artificial Intelligence' was coined at the 1956 Dartmouth conference by", ["John McCarthy", "Alan Turing", "Marvin Minsky", "Allen Newell"], 0,
     "McCarthy also created LISP."),
    ("The 'total Turing test' adds tests of", ["Perception (computer vision) and object manipulation (robotics)", "Speed", "Memory size", "Arithmetic"], 0,
     "The interrogator can also pass objects to the machine."),
    ("To pass the Turing test, a computer needs", ["Natural language processing, knowledge representation, automated reasoning and machine learning",
                                                   "A fast processor alone", "A large disk", "A camera"], 0, "Russell & Norvig, ch. 1."),
    ("Which argument claims that passing the Turing test would not prove real understanding?", ["John Searle's Chinese room argument", "Turing's imitation game",
                                                                                               "The frame problem", "Gödel's incompleteness theorem"], 0,
     "Symbol manipulation without understanding."),
    ("A rational agent is one that", ["Acts to maximise its expected performance measure, given its percept sequence and knowledge", "Always succeeds",
                                      "Thinks exactly like a human", "Never makes mistakes"], 0, PYQ + "Rational ≠ omniscient."),
    ("The PEAS description of a task environment stands for", ["Performance measure, Environment, Actuators, Sensors", "Plan, Execute, Act, Sense",
                                                               "Percept, Environment, Action, State", "Program, Engine, Agent, System"], 0, "E.g. a taxi: safety, roads, steering, cameras."),
    ("A simple reflex agent chooses actions on the basis of", ["The current percept alone, using condition–action rules", "The full percept history", "A utility function",
                                                               "Future goals"], 0, "A model-based agent also keeps internal state."),
    ("An agent that chooses among goal-achieving actions using a measure of how desirable each outcome is, is a", ["Utility-based agent", "Simple reflex agent",
                                                                                                                    "Model-based reflex agent", "Table-driven agent"], 0,
     "Goal-based agents only distinguish goal / not goal."),
    ("Chess played with a clock is, as a task environment,", ["Fully observable, strategic, sequential, semi-dynamic, discrete and multi-agent",
                                                              "Partially observable and continuous", "Episodic and single-agent", "Stochastic and continuous"], 0,
     "Russell & Norvig's environment table."),
    ("Automated taxi driving is, as a task environment,", ["Partially observable, stochastic, dynamic and continuous", "Fully observable and deterministic",
                                                          "Static and discrete", "Episodic and single-agent"], 0, PYQ + "The hardest combination."),
    ("A state space representation of a problem consists of", ["States, an initial state, operators (actions), a goal test and a path cost", "A goal state alone",
                                                               "A database", "A neural network"], 0, "Problem solving = searching this space."),
    ("In the water-jug problem with a 4-litre and a 3-litre jug, a state is written as", ["(x, y) – the litres in the 4-litre and the 3-litre jug", "x alone",
                                                                                          "A single integer", "A string of moves"], 0,
     "Start (0, 0); goal (2, n). Rich & Knight."),
    ("How many states of the 8-puzzle are reachable from a given start state?", ["9!/2 = 181,440", "9! = 362,880", "8! = 40,320", "2⁹ = 512"], 0,
     PYQ + "Half of all arrangements are unreachable (parity)."),
    ("The missionaries-and-cannibals problem is an example of", ["A toy problem solved by state space search", "A machine-learning data set", "A sorting problem",
                                                                "A database query"], 0, "States record who is on each bank and where the boat is."),
    ("A production system consists of", ["A set of rules, a database (working memory) and a control strategy", "A set of rules alone", "A compiler", "A neural network"], 0,
     "Plus a rule applier (Rich & Knight)."),
    ("A good control strategy for search must", ["Cause motion and be systematic", "Be random", "Repeat states", "Avoid the goal"], 0, "Rich & Knight, ch. 2."),
    ("In chess, the steps of a solution are", ["Irrecoverable – a move cannot be undone", "Ignorable", "Recoverable", "Decomposable"], 0,
     "Theorem proving: ignorable; 8-puzzle: recoverable."),
    ("Strong AI claims that", ["Suitably programmed machines can really have minds and understanding", "Machines can simulate intelligence but not have it",
                               "AI is impossible", "Robots alone can be intelligent"], 0, "Weak AI claims only that machines can act intelligently."),
    ("ELIZA (1966), an early program that imitated a psychotherapist, was written by", ["Joseph Weizenbaum", "Alan Turing", "John McCarthy", "Edward Feigenbaum"], 0,
     "It used simple pattern matching."),
    ("Which languages are traditionally associated with AI?", ["LISP and PROLOG", "COBOL and FORTRAN", "HTML and CSS", "SQL and PL/SQL"], 0,
     "LISP (McCarthy, 1958); PROLOG (Colmerauer, 1972). Python dominates today."),
]

HEURISTIC_GAMES = [
    kset("KSET 2023 CS&A · Q77"),
    kset("KSET 2025 CS&A · Q92"),
    ("Adversarial search problems use", ["Competitive Environment", "Cooperative Environment", "Neither competitive nor cooperative Environment",
                                         "Both Competitive and cooperative Environment"], 0, "Games: the agents' goals conflict." + NOTE, "GFGC 2021 CS · Q119"),
    ("General algorithm applied on game tree for making decision of Win/Lose is", ["DFS/BFS Search Algorithms", "Heuristic Search Algorithms", "Greedy Search Algorithms",
                                                                                  "Min/Max Algorithms"], 3, "Minimax." + NOTE, "GFGC 2021 CS · Q125"),
    ("A heuristic function h(n) gives", ["An estimate of the cost of the cheapest path from node n to a goal", "The exact cost from the start", "The depth of n",
                                         "The number of children of n"], 0, PYQ + "Heuristics use domain knowledge."),
    ("The simplest heuristic method, which proposes a solution and then checks it, is", ["Generate-and-test", "Hill climbing", "A*", "Minimax"], 0,
     "Hill climbing adds feedback from the test."),
    ("Hill climbing can get stuck at", ["Local maxima, plateaus and ridges", "The goal", "The start state", "Leaf nodes of a game tree"], 0,
     "It looks only at immediate neighbours."),
    ("A useful remedy for a plateau in hill climbing is", ["Making a big jump to a new region of the search space", "Backtracking one step", "Stopping at once",
                                                           "Using a smaller step"], 0, "Backtracking helps with local maxima; trying several directions helps with ridges."),
    ("Simulated annealing", ["Sometimes accepts worse moves, with a probability that falls as the 'temperature' is lowered", "Never accepts a worse move",
                             "Always accepts worse moves", "Uses a game tree"], 0, PYQ + "Probability e^(−ΔE/T) helps escape local maxima."),
    ("Best-first search keeps the nodes generated but not yet expanded in the", ["OPEN list (a priority queue)", "CLOSED list", "Stack", "Goal set"], 0,
     "CLOSED holds the nodes already expanded."),
    ("Means–ends analysis, used in GPS (Newell and Simon), works by", ["Reducing the difference between the current state and the goal", "Making random moves",
                                                                       "Exhaustive search", "Learning weights"], 0, "It picks operators that reduce the difference."),
    ("Cryptarithmetic puzzles such as SEND + MORE = MONEY are solved as", ["Constraint satisfaction problems", "Game-playing problems", "Clustering problems", "Parsing problems"], 0,
     "Map colouring is another CSP."),
    ("AND–OR graphs (problem reduction) are searched with the", ["AO* algorithm", "Minimax algorithm", "Bubble sort", "Kruskal's algorithm"], 0,
     "AND arcs mean all sub-problems must be solved."),
    ("A MAX root has two MIN children whose leaves are (3, 5) and (2, 9). The minimax value of the root is", ["3", "9", "2", "5"], 0,
     PYQ + "MIN gives 3 and 2; MAX picks 3."),
    ("In the same tree, alpha–beta pruning (left to right) does not need to examine the leaf", ["9", "2", "3", "5"], 0,
     "After the right MIN node sees 2 ≤ α = 3, its other child is pruned."),
    ("With perfect move ordering, alpha–beta search examines about", ["O(b^(d/2)) nodes, against O(bᵈ) for plain minimax", "O(bd) nodes", "O(d) nodes", "O(b²) nodes"], 0,
     "It can search about twice as deep in the same time."),
    ("In alpha–beta pruning, α is", ["The best (highest) value found so far for MAX along the path", "The best value for MIN", "The depth limit", "The branching factor"], 0,
     "β is the best (lowest) value for MIN; prune when α ≥ β."),
    ("One move by one player in a game tree is called a", ["Ply", "Branching factor", "Node", "Epoch"], 0, "A full move is two plies."),
    ("In depth-limited game search, positions at the depth limit are scored with", ["A static evaluation function", "Random numbers", "The goal test", "The path cost"], 0,
     "E.g. material balance in chess."),
    ("The horizon effect in game search is", ["An unavoidable bad event pushed just beyond the search depth, so the program cannot see it", "Running out of memory",
                                              "A drawn game", "Pruning the best move"], 0, "Quiescence search reduces it."),
    ("IBM's Deep Blue defeated world chess champion Garry Kasparov in", ["1997", "1985", "2005", "2016"], 0, PYQ + "AlphaGo beat Lee Sedol at Go in 2016."),
    ("Chess is a two-player zero-sum game, which means", ["One player's gain equals the other player's loss", "Both players can win", "Scores are always zero",
                                                          "No one can win"], 0, "Minimax assumes an optimal opponent."),
    ("Games with dice, such as backgammon, are searched with", ["Expectiminimax, which has chance nodes", "Plain minimax", "Breadth-first search", "Hill climbing"], 0,
     "Chance nodes take the expected value."),
    ("An upper bound on the number of tic-tac-toe board configurations is", ["3⁹ = 19,683", "9! = 362,880", "2⁹ = 512", "9² = 81"], 0, "Each square is X, O or empty."),
    ("Simple hill climbing moves to", ["The first successor that is better than the current state", "The best of all successors", "A random successor",
                                       "The worst successor"], 0, "Steepest-ascent hill climbing examines all successors."),
    ("Local beam search keeps", ["The k best states at each step", "All generated states", "One state", "No states"], 0, "It shares information among the k searches."),
    ("For the 8-puzzle, the Manhattan-distance heuristic h₂ and the misplaced-tiles heuristic h₁ satisfy", ["h₂ ≥ h₁, so h₂ is the better admissible heuristic",
                                                                                                            "h₁ ≥ h₂", "h₂ is not admissible", "They are always equal"], 0,
     PYQ + "h₂ dominates h₁."),
    ("AlphaGo combined deep neural networks with", ["Monte Carlo tree search", "Bubble sort", "Plain minimax without evaluation", "Breadth-first search"], 0,
     "Random play-outs estimate position values."),
    ("A constraint satisfaction problem is defined by", ["Variables, their domains and constraints on the values they may take together",
                                                        "A start state and a goal state alone", "A game tree", "A set of training examples"], 0,
     "Solved with backtracking plus heuristics such as minimum remaining values."),
    ("Heuristic search differs from blind (uninformed) search because it", ["Uses problem-specific knowledge to guide the search", "Explores every node",
                                                                           "Never finds a solution", "Uses no memory"], 0, "The heuristic ranks the frontier nodes."),
]

KR_SCHEMES = [
    kset("KSET 2023 CS&A · Q74"),
    kset("KSET 2025 CS&A · Q93"),
    kset("KSET 2024 CS&A · Q94"),
    kset("KSET 2025 CS&A · Q94"),
    kset("KSET 2023 CS&A · Q72"),
    ("Which is not a property of representational of knowledge?", ["Representational verification", "Representational adequacy", "Inferential adequacy",
                                                                  "Inferential efficiency"], 0,
     "The four properties are representational adequacy, inferential adequacy, inferential efficiency and acquisitional efficiency." + NOTE, "GFGC 2021 CS · Q114"),
    ("A semantic network represents knowledge as", ["A graph of nodes (concepts) joined by labelled arcs (relations such as IS-A)", "A table of numbers",
                                                    "A list of IF–THEN rules", "A neural network"], 0, PYQ + "Quillian (1968)."),
    ("In a semantic network, the IS-A link supports", ["Inheritance of properties from a class to its members", "Arithmetic", "Parsing", "Backtracking"], 0,
     "Canary IS-A Bird, Bird HAS Wings → canaries have wings."),
    ("Frames, proposed by Marvin Minsky, represent knowledge as", ["Structures of slots and fillers (attribute–value pairs) with default values", "Logic sentences",
                                                                   "Production rules", "Neural weights"], 0, "Frames can inherit from parent frames."),
    ("A script, such as the 'restaurant' script, represents", ["A stereotyped sequence of events in a familiar situation", "A single fact", "A logical proof",
                                                               "A probability table"], 0, PYQ + "Schank and Abelson."),
    ("Which is NOT a component of a script?", ["Activation function", "Entry conditions", "Roles and props", "Scenes"], 0,
     "Scripts have entry conditions, results, props, roles, track and scenes."),
    ("In conceptual dependency, PTRANS means", ["Transfer of the physical location of an object", "Transfer of possession", "Transfer of mental information",
                                                "Application of force"], 0, "ATRANS = possession, MTRANS = information, PROPEL = force."),
    ("'John gave Mary a book' is represented in conceptual dependency mainly with", ["ATRANS", "PTRANS", "MTRANS", "INGEST"], 0,
     "The abstract relationship (possession) is transferred."),
    ("An ontology is", ["An explicit, formal specification of the concepts of a domain and their relationships", "A database index", "A neural network",
                        "A programming language"], 0, "Gruber's definition."),
    ("The W3C language for writing ontologies on the semantic web is", ["OWL", "HTML", "SQL", "CSS"], 0, "Built on RDF; queried with SPARQL."),
    ("Knowledge written in the form IF condition THEN action is called", ["Production rules", "Frames", "Scripts", "Semantic nets"], 0,
     "Used in rule-based expert systems."),
    ("First-order (predicate) logic is more expressive than propositional logic because it has", ["Variables, predicates and quantifiers (∀, ∃)", "More connectives",
                                                                                                   "No variables", "Truth tables"], 0, "It can talk about objects and relations."),
    ("'All students like AI' in predicate logic is", ["∀x (Student(x) → Likes(x, AI))", "∀x (Student(x) ∧ Likes(x, AI))", "∃x (Student(x) → Likes(x, AI))",
                                                      "Student(AI) → Likes(x)"], 0, PYQ + "∀ goes with →; ∃ goes with ∧."),
    ("The resolution method of inference needs the sentences in", ["Conjunctive normal form (clauses)", "Disjunctive normal form", "English", "Truth-table form"], 0,
     "Proof by refutation: add the negated goal and derive the empty clause."),
    ("Unifying Knows(John, x) and Knows(y, Mary) gives the substitution", ["{y/John, x/Mary}", "{x/John, y/Mary}", "{x/y}", "No unifier exists"], 0,
     "Each variable is replaced so that both become Knows(John, Mary)."),
    ("From P and P → Q, inferring Q is called", ["Modus ponens", "Modus tollens", "Resolution by refutation", "Abduction"], 0, "Modus tollens: ¬Q and P → Q give ¬P."),
    ("PROLOG programs are made of", ["Horn clauses (facts and rules)", "Frames", "Scripts", "Neural layers"], 0, "A Horn clause has at most one positive literal."),
    ("Which is NOT one of the four properties of a good knowledge representation system?", ["Compilation speed", "Representational adequacy", "Inferential efficiency",
                                                                                             "Acquisitional efficiency"], 0, "Rich & Knight."),
    ("Knowing how to ride a bicycle is an example of", ["Procedural knowledge", "Declarative knowledge", "Meta-knowledge", "Heuristic knowledge"], 0,
     "Declarative knowledge is 'knowing that'."),
    ("The 'frame problem' in AI is the difficulty of", ["Stating what does NOT change when an action is performed", "Drawing frames", "Storing images", "Finding a frame rate"], 0,
     "McCarthy and Hayes (1969)."),
    ("Skolemization is used to", ["Remove existential quantifiers by introducing Skolem constants or functions", "Remove universal quantifiers", "Add negations",
                                  "Convert sentences to DNF"], 0, "A step in converting to clause form."),
    ("Inheritable knowledge is best represented with", ["Semantic networks or frames with IS-A hierarchies", "Truth tables", "Arrays", "Stacks"], 0, "Rich & Knight's four kinds of knowledge."),
    ("Classical logic is monotonic, which means", ["Adding new facts never invalidates earlier conclusions", "Conclusions can be withdrawn", "It handles default rules",
                                                   "It is probabilistic"], 0, "Default reasoning is non-monotonic."),
    ("In the frame for 'Elephant', the slot colour = grey is a", ["Default value that a particular elephant's frame may override", "Rule", "Script scene", "Quantifier"], 0,
     "Frames store typical values; exceptions are written in the instance frame."),
    ("Conceptual graphs (John Sowa) are closely related to", ["Semantic networks", "Neural networks", "Decision trees", "Hash tables"], 0, "They map to first-order logic."),
]

EXPERT_REASONING = [
    kset("KSET 2025 CS&A · Q95"),
    kset("KSET 2024 CS&A · Q97"),
    ("What is another type of default reasoning ?", ["Monotonic reasoning", "Analogical reasoning", "Bitonic reasoning", "Non-Monotonic reasoning"], 3,
     "Default conclusions may be withdrawn later." + NOTE, "GFGC 2021 CS · Q115"),
    ("How the Bayesian network can be used to answer any query?", ["Full distribution", "Joint distribution", "Partial distribution", "No distribution"], 1,
     "The network encodes the full joint distribution, from which any query can be answered." + NOTE, "GFGC 2021 CS · Q121"),
    ("The truth value of traditional set theory is ____ and that of fuzzy set is ____", ["Either 0 or 1, between 0 and 1", "Between 0 & 1, either 0 or 1",
                                                                                         "Between 0 & 1, between 0 and 1", "Either 0 or 1, either 0 or 1"], 0,
     "Crisp membership is 0 or 1; fuzzy membership is any value in [0, 1]." + NOTE, "GFGC 2021 CS · Q120"),
    ("The main components of an expert system are", ["Knowledge base, inference engine and user interface", "Compiler, linker and loader", "CPU, memory and I/O",
                                                     "Sensors, actuators and environment"], 0, PYQ + "Plus an explanation facility and a knowledge-acquisition module."),
    ("The inference engine of an expert system", ["Applies the rules of the knowledge base to the facts to reach conclusions", "Stores the facts", "Talks to the user",
                                                  "Acquires knowledge"], 0, "It uses forward or backward chaining."),
    ("The person who extracts knowledge from human experts and builds the knowledge base is the", ["Knowledge engineer", "End user", "Domain expert", "System analyst"], 0,
     "The domain expert supplies the knowledge."),
    ("MYCIN was an expert system for", ["Diagnosing bacterial blood infections and recommending antibiotics", "Analysing mass spectra", "Configuring VAX computers",
                                        "Playing chess"], 0, PYQ + "Stanford, 1970s; backward chaining with certainty factors."),
    ("DENDRAL inferred", ["Molecular structures from mass-spectrometry data", "Diseases", "Mineral deposits", "Computer configurations"], 0, "One of the first expert systems."),
    ("PROSPECTOR was used for", ["Mineral exploration – locating ore deposits", "Medical diagnosis", "Chemistry", "Chess"], 0, "XCON (R1) configured VAX computers at DEC."),
    ("Forward chaining is", ["Data-driven – it starts from known facts and applies rules to reach conclusions", "Goal-driven", "Random", "Used in games alone"], 0,
     "Used in XCON and OPS5."),
    ("Backward chaining is", ["Goal-driven – it starts from a hypothesis and looks for facts that support it", "Data-driven", "Random", "Used for planning alone"], 0,
     "Used in MYCIN and PROLOG."),
    ("An expert system shell such as EMYCIN or CLIPS is", ["An expert system with an empty knowledge base, ready for knowledge of a new domain", "A command interpreter",
                                                           "A hardware unit", "A database"], 0, "It keeps the inference engine and interface."),
    ("The explanation facility of an expert system answers questions such as", ["'Why do you ask that?' and 'How did you reach this conclusion?'", "'What is the time?'",
                                                                                "'Where is the file?'", "'Who is the user?'"], 0, "It shows the chain of rules used."),
    ("In MYCIN, certainty factors range from", ["−1 to +1", "0 to 1", "0 to 100", "−100 to 0"], 0, "+1 = definitely true, −1 = definitely false."),
    ("If P(H) = 0.01, P(E | H) = 0.9 and P(E) = 0.1, then by Bayes' theorem P(H | E) is", ["0.09", "0.9", "0.01", "0.009"], 0, PYQ + "0.9 × 0.01 / 0.1."),
    ("A Bayesian network is", ["A directed acyclic graph of random variables, each with a conditional probability table", "An undirected graph of neurons", "A decision tree",
                               "A semantic network"], 0, "Arcs show direct influence."),
    ("Dempster–Shafer theory represents uncertainty using", ["Belief and plausibility intervals", "Crisp sets", "Truth tables", "Neural weights"], 0,
     "It can express ignorance explicitly."),
    ("Default reasoning such as 'birds fly unless known otherwise' is", ["Non-monotonic – the conclusion can be withdrawn when new facts arrive", "Monotonic",
                                                                         "Deductive certainty", "Purely probabilistic"], 0, "Penguins are the classic exception."),
    ("A truth maintenance system (TMS) is used to", ["Record beliefs with their justifications and revise them when assumptions change", "Store neural weights",
                                                     "Parse sentences", "Schedule processes"], 0, "Doyle's JTMS, de Kleer's ATMS."),
    ("In fuzzy sets, μ(A ∩ B)(x) is", ["min(μA(x), μB(x))", "max(μA(x), μB(x))", "μA(x) × μB(x) always", "1 − μA(x)"], 0, "Union uses max; complement 1 − μ."),
    ("If μA(x) = 0.3, the membership of x in the complement of A is", ["0.7", "0.3", "1.3", "0"], 0, "1 − 0.3."),
    ("Converting a fuzzy output into a single crisp value is called", ["Defuzzification", "Fuzzification", "Normalization", "Inference"], 0, "E.g. the centroid method."),
    ("Fuzzy set theory was introduced by", ["Lotfi Zadeh, in 1965", "John McCarthy, in 1956", "Judea Pearl, in 1988", "Edward Feigenbaum, in 1977"], 0,
     "Pearl developed Bayesian networks."),
    ("A major limitation of rule-based expert systems is that they", ["Lack common sense and fail outside their narrow domain", "Are always slow", "Cannot explain",
                                                                      "Forget their rules"], 0, "Knowledge acquisition is also a bottleneck."),
    ("When several rules match at once, a production system picks one using", ["Conflict resolution, e.g. specificity or recency", "Random deletion", "Backpropagation",
                                                                               "Hashing"], 0, "Refractoriness stops a rule firing twice on the same data."),
    ("The Rete algorithm is used in rule engines such as OPS5 and CLIPS to", ["Match many rules against many facts efficiently", "Train neural networks",
                                                                              "Sort data", "Parse sentences"], 0, "It caches partial matches."),
    ("With the rules A → B and B → C and the fact A, forward chaining derives", ["B and then C", "B alone", "C without B", "Nothing"], 0, "Each new fact may trigger more rules."),
    ("Reasoning from an observed effect to its most likely cause, as in diagnosis, is", ["Abduction", "Deduction", "Induction", "Resolution"], 0,
     "Induction generalises from examples."),
]

UNINFORMED = [
    kset("KSET 2023 CS&A · Q73"),
    ("A search problem is formally defined by", ["An initial state, actions, a transition model, a goal test and a path cost", "A heuristic alone", "A neural network",
                                                 "A database schema"], 0, PYQ + "Russell & Norvig, ch. 3."),
    ("Uninformed (blind) search strategies use", ["No information beyond the problem definition", "A heuristic", "Learned weights", "The distance to the goal"], 0,
     "BFS, DFS, UCS, depth-limited, iterative deepening, bidirectional."),
    ("Breadth-first search keeps its frontier in a", ["FIFO queue", "LIFO stack", "Priority queue ordered by h(n)", "Hash table"], 0, "Shallowest nodes are expanded first."),
    ("Depth-first search keeps its frontier in a", ["LIFO stack (or uses recursion)", "FIFO queue", "Priority queue", "Circular buffer"], 0, "The deepest node is expanded first."),
    ("Breadth-first search is optimal when", ["All step costs are equal", "Step costs are random", "The tree is infinite", "It uses a stack"], 0,
     "Otherwise use uniform-cost search."),
    ("Breadth-first search needs memory of the order of", ["O(bᵈ) – it keeps every frontier node", "O(bd)", "O(d)", "O(1)"], 0, "Memory is its main weakness."),
    ("Depth-first search needs memory of the order of", ["O(bm) – one path plus the unexpanded siblings", "O(bᵈ)", "O(b²)", "O(m!)"], 0, "m = maximum depth."),
    ("Depth-first search may fail to find a solution when", ["The search space has infinite paths", "The goal is shallow", "b = 1", "There are no cycles"], 0,
     "It is not complete in infinite spaces."),
    ("Depth-limited search", ["Runs DFS with a fixed depth limit l", "Has no limit", "Uses a heuristic", "Searches from both ends"], 0, "Incomplete if l < d."),
    ("Iterative deepening search", ["Repeats depth-limited search with limits 0, 1, 2, … – complete, optimal for unit costs and O(bd) in memory",
                                    "Uses a priority queue", "Searches from the goal backwards", "Is never complete"], 0, PYQ + "The preferred uninformed method for large spaces."),
    ("Uniform-cost search always expands the node with the", ["Lowest path cost g(n)", "Highest path cost", "Lowest heuristic h(n)", "Greatest depth"], 0,
     "It is Dijkstra's algorithm on a search tree."),
    ("Bidirectional search reduces the time to about", ["O(b^(d/2))", "O(bᵈ)", "O(d)", "O(b^(2d))"], 0, "Two searches of depth d/2 meet in the middle."),
    ("Bidirectional search needs", ["An explicit goal state and a way to compute predecessors", "A heuristic", "No goal state", "Random restarts"], 0,
     "The backward search starts from the goal."),
    ("In the tree A → (B, C), B → (D, E), C → (F), breadth-first search visits", ["A B C D E F", "A B D E C F", "A C F B E D", "D E B F C A"], 0, PYQ + "Level by level."),
    ("In the same tree, depth-first search (left child first) visits", ["A B D E C F", "A B C D E F", "A C F B D E", "D E F B C A"], 0, "As deep as possible first."),
    ("A complete binary tree of depth 3 (root at depth 0) has how many nodes?", ["15", "8", "7", "16"], 0, "1 + 2 + 4 + 8."),
    ("Iterative deepening re-expands the shallow levels, yet its time is still O(bᵈ) because", ["Most nodes are at the deepest level", "It uses a heuristic",
                                                                                                "It prunes the tree", "It stores every node"], 0, "The overhead is small."),
    ("To avoid expanding repeated states, graph search keeps", ["An explored (closed) set", "A larger queue", "A random seed", "A heuristic"], 0, "Tree search does not."),
    ("A problem-solving agent is a kind of", ["Goal-based agent", "Simple reflex agent", "Table-driven agent", "Pure learning agent"], 0, "It searches for a sequence of actions."),
    ("A node in a search tree contains", ["A state, its parent, the action, the path cost and the depth", "The state alone", "A heuristic alone", "Nothing"], 0,
     "The parent links give the solution path."),
    ("The branching factor b is", ["The maximum number of successors of a node", "The depth of the goal", "The number of goals", "The path cost"], 0, "d is the depth of the shallowest goal."),
    ("Search strategies are compared on", ["Completeness, optimality, time complexity and space complexity", "Colour and size", "Speed alone", "Programming language"], 0,
     "Russell & Norvig's four criteria."),
    ("Edges S→A cost 1, S→B cost 5, A→G cost 10, B→G cost 2. Uniform-cost search from S returns", ["S → B → G with cost 7", "S → A → G with cost 11", "S → G", "No path"], 0,
     PYQ + "It expands by g(n): A (1), B (5), then G via B (7) before G via A (11)."),
    ("On the same graph, breadth-first search (children in the order A, B) returns", ["S → A → G with cost 11 – not the cheapest", "S → B → G", "S → G", "No path"], 0,
     "BFS ignores costs; both paths have depth 2 and A is generated first."),
    ("Route finding between cities is an example of", ["A real-world search problem", "A toy problem", "A game", "A learning problem"], 0, "The 8-puzzle is a toy problem."),
    ("In the incremental formulation of the 8-queens problem, an action", ["Adds a queen to the leftmost empty column in a safe square", "Moves a queen at random",
                                                                           "Removes all queens", "Swaps two queens"], 0, "This shrinks the state space greatly."),
    ("When the search space is large and the solution depth is unknown, the usual uninformed choice is", ["Iterative deepening search", "Breadth-first search",
                                                                                                          "Depth-first search", "Depth-limited search with a small limit"], 0,
     "It combines BFS's completeness with DFS's memory use."),
    ("Depth-first search with backtracking (generating one successor at a time) needs memory of only", ["O(m)", "O(bᵈ)", "O(b^m)", "O(1) always"], 0,
     "Each node remembers which successor to generate next."),
    ("In breadth-first search, the goal test is best applied", ["When a node is generated (early goal test)", "At the root alone", "Never",
                                                                 "After every node has been expanded"], 0, "This saves one whole level."),
]

INFORMED = [
    ("Greedy best-first search expands the node with the lowest", ["h(n), the estimated cost to the goal", "g(n), the path cost so far", "g(n) + h(n)", "Depth"], 0,
     PYQ + "It is fast but neither optimal nor complete (tree version)."),
    ("A* search expands the node with the lowest", ["f(n) = g(n) + h(n)", "h(n)", "g(n)", "g(n) − h(n)"], 0, PYQ + "g = cost so far, h = estimated cost to go."),
    ("A heuristic is admissible if it", ["Never overestimates the true cost to reach the goal", "Always overestimates", "Is always zero", "Is greater than g(n)"], 0,
     "Straight-line distance is admissible for road maps."),
    ("A* is guaranteed to find an optimal solution when", ["h is admissible (tree search) or consistent (graph search)", "h overestimates", "h is random",
                                                           "The graph has no goal"], 0, "Hart, Nilsson and Raphael (1968)."),
    ("A heuristic h is consistent (monotone) if, for every node n and successor n',", ["h(n) ≤ c(n, n') + h(n')", "h(n) ≥ c(n, n') + h(n')", "h(n) = 0", "h(n') > h(n)"], 0,
     "Every consistent heuristic is admissible."),
    ("Greedy best-first search", ["Is not optimal and, as tree search, not complete", "Is always optimal", "Uses g(n) only", "Needs no heuristic"], 0,
     "It can go down a misleading path."),
    ("Graph: S→A cost 2, S→B cost 1, A→G cost 4, B→G cost 6; h(S) = 5, h(A) = 3, h(B) = 6, h(G) = 0. A* returns", ["S → A → G with cost 6", "S → B → G with cost 7",
                                                                                                                  "S → G", "No path"], 0,
     PYQ + "f(A) = 5, f(B) = 7; expanding A gives G with f = 6, which is chosen before B."),
    ("With h(n) = 0 for every node, A* behaves like", ["Uniform-cost search", "Depth-first search", "Greedy best-first search", "Hill climbing"], 0, "f(n) = g(n)."),
    ("If h(n) equals the true remaining cost h*(n) everywhere, A*", ["Expands only nodes on an optimal path", "Expands every node", "Never terminates", "Becomes DFS"], 0,
     "A perfect heuristic leaves nothing to search."),
    ("To reduce A*'s memory use, one can use", ["IDA* or SMA*", "Breadth-first search", "Depth-first search without a limit", "Greedy search"], 0,
     "IDA* = iterative deepening on f; SMA* = memory-bounded A*."),
    ("A better heuristic gives an effective branching factor b* that is", ["Closer to 1", "Larger", "Exactly b", "Zero"], 0, "Fewer nodes are generated."),
    ("Heuristics such as Manhattan distance for the 8-puzzle can be obtained by", ["Solving a relaxed version of the problem", "Random guessing", "Running BFS",
                                                                                   "Counting moves backwards"], 0, "Relax 'a tile can move only into the blank'."),
    ("For the textbook 8-puzzle start state (7 2 4 / 5 _ 6 / 8 3 1) and goal (_ 1 2 / 3 4 5 / 6 7 8), h₁ (misplaced tiles) and h₂ (Manhattan distance) are",
     ["8 and 18", "8 and 26", "7 and 18", "6 and 14"], 0, "All 8 tiles are misplaced; distances 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2 = 18 (Russell & Norvig)."),
    ("If h₁ and h₂ are both admissible, then max(h₁, h₂) is", ["Admissible and at least as good as either", "Not admissible", "Always zero", "Inconsistent"], 0,
     "It dominates both."),
    ("On the Romania map, greedy best-first search from Arad finds a path to Bucharest of cost 450, while A* finds", ["418 – the optimal path", "450 as well", "500", "366"], 0,
     "Via Sibiu, Rimnicu Vilcea and Pitesti (Russell & Norvig)."),
    ("Straight-line distance is an admissible heuristic for road travel because", ["No road between two points can be shorter than the straight line", "It is exact",
                                                                                   "It overestimates", "Roads are straight"], 0, "Triangle inequality."),
    ("Hill climbing is like greedy search except that it", ["Keeps no frontier – it moves to the best neighbour and forgets the rest", "Is optimal", "Uses A*", "Uses a queue"], 0,
     "That is why it gets stuck."),
    ("Branch and bound in search", ["Discards paths whose cost already exceeds the best solution found", "Expands every node", "Uses random restarts", "Ignores costs"], 0,
     "A* adds an estimate of the remaining cost."),
    ("Recursive best-first search (RBFS)", ["Mimics best-first search using only linear space", "Uses exponential memory", "Ignores the heuristic", "Is a local search"], 0,
     "It remembers the best alternative f-value."),
    ("In the worst case, A* takes time", ["Exponential in the solution depth", "Linear", "Constant", "Logarithmic"], 0, "A good heuristic reduces it in practice."),
    ("In A*, g(n) is", ["The cost of the path from the start to n", "The estimated cost from n to the goal", "The depth of n", "The number of children of n"], 0,
     "h(n) is the estimate to the goal."),
    ("h₂ dominates h₁ when", ["h₂(n) ≥ h₁(n) for every node n (both admissible)", "h₂(n) ≤ h₁(n)", "h₂ is inconsistent", "h₁ = 0"], 0, "The dominating heuristic expands fewer nodes."),
    ("Which statement about an admissible heuristic is true?", ["h(goal) = 0 and h(n) ≤ the true cost to the goal", "h(n) ≥ the true cost", "h(n) is random",
                                                                "h(goal) > 0"], 0, "It is optimistic."),
    ("A* is optimally efficient, which means", ["No other optimal algorithm using the same heuristic expands fewer nodes (ignoring ties)", "It uses the least memory",
                                                "It never backtracks", "It needs no heuristic"], 0, "Its weakness is memory."),
    ("Uniform-cost search is the special case of A* with", ["h(n) = 0", "g(n) = 0", "h(n) = ∞", "f(n) = h(n)"], 0, "Greedy best-first ignores g instead."),
    ("If h overestimates the true cost, A*", ["May return a non-optimal path", "Becomes breadth-first search", "Never terminates", "Is unaffected"], 0,
     "Admissibility is what guarantees optimality."),
    ("A node has g = 4 and h = 7. Its A* value f is", ["11", "3", "28", "7"], 0, "f = g + h."),
    ("A commonly used admissible heuristic for road route finding is", ["The straight-line distance to the goal", "The number of cities visited",
                                                                        "The distance already travelled", "Zero except at the goal"], 0, "h_SLD in Russell & Norvig."),
    ("Heuristic functions trade", ["Some accuracy for a large saving in search effort", "Memory for nothing", "Correctness for speed in every case", "Nothing at all"], 0,
     "Good heuristics are cheap to compute and close to the true cost."),
    ("Informed search differs from uninformed search in that it", ["Uses an evaluation function with problem-specific knowledge", "Searches blindly",
                                                                   "Uses a FIFO queue alone", "Cannot find solutions"], 0, "Best-first, greedy, A*."),
]

TOPICS = {
    "Approaches to AI": [
        ("1 · Turing Test, Rational Agents and State Space Representation", TURING_AGENTS),
        ("2 · Heuristic Search Techniques and Game Playing", HEURISTIC_GAMES),
    ],
    "Knowledge Representation": [
        ("1 · Logic, Semantic Networks, Frames, Rules, Scripts, Conceptual Dependency and Ontologies", KR_SCHEMES),
        ("2 · Expert Systems and Reasoning under Uncertainty", EXPERT_REASONING),
    ],
    "Problem Solving by Searching": [
        ("1 · Problem-solving Agents and Uninformed Search – BFS, DFS and Bidirectional", UNINFORMED),
        ("2 · Informed Search – Greedy Best-first, A* and Heuristic Functions", INFORMED),
    ],
}

NOTES = {
    "Approaches to AI": [{"title": "Approaches to AI – revision sheet", "md": """## Definitions (Russell & Norvig)
| | Human-like | Rational |
|---|---|---|
| Thinking | cognitive modelling (cognitive science) | laws of thought (logic) |
| Acting | Turing test | rational agent |
- Turing (1950, imitation game); total Turing test adds vision and robotics; Searle's Chinese room; strong vs weak AI
- AI named by McCarthy (Dartmouth, 1956); LISP, PROLOG; ELIZA (Weizenbaum)

## Agents
- Agent = architecture + program; PEAS (Performance, Environment, Actuators, Sensors)
- Types: simple reflex (condition–action), model-based, goal-based, utility-based, learning
- Environments: fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, single/multi-agent
- Rational agent maximises expected performance (not omniscient)

## State space representation
- States, initial state, operators, goal test, path cost; water jug (x, y); 8-puzzle 9!/2 states; missionaries and cannibals
- Production system = rules + working memory + control strategy (must cause motion and be systematic)
- Problem characteristics: decomposable, ignorable (theorem proving) / recoverable (8-puzzle) / irrecoverable (chess)

## Heuristic search and games
- Generate-and-test; hill climbing (simple vs steepest ascent; local maxima, plateau, ridge); simulated annealing; beam search; best-first (OPEN/CLOSED); means–ends analysis (GPS); CSPs; AND–OR graphs (AO*)
- Minimax (MAX/MIN, ply, static evaluation); alpha–beta: α = best for MAX, β = best for MIN, prune when α ≥ β, best case O(b^(d/2))
- Horizon effect; expectiminimax for chance games; Deep Blue 1997, AlphaGo 2016 (MCTS)
"""}],
    "Knowledge Representation": [{"title": "Knowledge representation – revision sheet", "md": """## Schemes
- Logic: propositional; first-order (∀ with →, ∃ with ∧); resolution (CNF, refutation), unification, Skolemization, modus ponens, Horn clauses (PROLOG)
- Semantic network (nodes + labelled arcs, IS-A inheritance; Quillian); conceptual graphs (Sowa)
- Frames (Minsky): slots, fillers, defaults, inheritance
- Production rules: IF condition THEN action
- Scripts (Schank & Abelson): entry conditions, roles, props, scenes, results, track – e.g. restaurant
- Conceptual dependency (Schank): ATRANS (possession), PTRANS (location), MTRANS (information), PROPEL, INGEST…
- Ontologies: formal specification of concepts and relations; OWL/RDF, queried with SPARQL
- Good KR: representational adequacy, inferential adequacy, inferential efficiency, acquisitional efficiency
- Frame problem; monotonic vs non-monotonic (default) reasoning; procedural vs declarative knowledge

## Expert systems
- Knowledge base + inference engine + user interface (+ explanation facility, knowledge acquisition); knowledge engineer
- Forward chaining (data-driven, XCON/OPS5, Rete) vs backward chaining (goal-driven, MYCIN, PROLOG)
- MYCIN (blood infections, certainty factors −1…+1), DENDRAL (mass spectra), PROSPECTOR (minerals), XCON/R1 (VAX); shells EMYCIN, CLIPS
- Conflict resolution: specificity, recency, refractoriness

## Uncertainty
- Bayes: P(H|E) = P(E|H) P(H) / P(E); Bayesian network = DAG + CPTs (encodes the joint distribution)
- Dempster–Shafer (belief, plausibility); TMS; abduction (effect → cause)
- Fuzzy (Zadeh 1965): membership in [0, 1]; ∪ = max, ∩ = min, complement 1 − μ; defuzzification; fuzzy equivalence = reflexive, symmetric, transitive
"""}],
    "Problem Solving by Searching": [{"title": "Search – revision sheet", "md": """## Problem formulation
Initial state, actions, transition model, goal test, path cost; node = state + parent + action + g + depth; b = branching factor, d = goal depth, m = max depth

## Uninformed search
| Strategy | Frontier | Complete | Optimal | Time | Space |
|---|---|---|---|---|---|
| BFS | FIFO | yes | unit costs | O(bᵈ) | O(bᵈ) |
| Uniform-cost | priority g | yes | yes | ≈O(b^(1+C*/ε)) | same |
| DFS | LIFO | no (infinite) | no | O(bᵐ) | O(bm) |
| Depth-limited | LIFO | if l ≥ d | no | O(bˡ) | O(bl) |
| Iterative deepening | LIFO | yes | unit costs | O(bᵈ) | O(bd) |
| Bidirectional | two | yes | unit costs | O(b^(d/2)) | O(b^(d/2)) |
- Graph search keeps an explored set; BFS: goal test on generation

## Informed search
- Greedy best-first: f = h (fast, not optimal); A*: f = g + h; UCS = A* with h = 0
- Admissible: h ≤ true cost (h(goal) = 0); consistent: h(n) ≤ c(n, n') + h(n') → A* optimal
- Dominance: h₂ ≥ h₁ → fewer expansions; max of admissible heuristics is admissible; relaxed problems give heuristics
- 8-puzzle: h₁ misplaced tiles, h₂ Manhattan (textbook start: 8 and 18)
- Romania: greedy 450, A* 418; memory-bounded: IDA*, RBFS, SMA*
"""}],
}
