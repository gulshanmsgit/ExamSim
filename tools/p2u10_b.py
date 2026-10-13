"""Paper 2 · Unit 10 · P2-U10-04 Natural Language Processing and P2-U10-05 Artificial Neural Networks & Applications
(2 topics × 2 sets × 30), with revision NOTES.
References: Russell & Norvig, AIMA (chs. 18–23); Jurafsky & Martin, Speech and Language Processing; Tom Mitchell, Machine Learning;
Rich & Knight (case grammar, conceptual parsing). Each set mixes REAL previous-year questions (exact wording, printed option order,
`source`) with new ones. Official answers: KEA final keys for GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1). KSET/KEA questions
come from packs/pyq-p2.json (the parsing questions there are compiler questions, used here for the syllabus item 'Parsing Techniques');
GFGC 2021 answers were worked out by ExamSim. Perceptron, entropy, metric and GA answers were computed by hand."""
from p2u7_a import kset, PYQ, GTTC, NOTE

GRAMMAR_PARSING = [
    kset("KSET 2023 CS&A · Q56"),
    kset("KSET 2024 CS&A · Q79"),
    kset("KEA 2026 CS Paper-2 · Q42"),
    ("The usual order of the stages of natural language analysis is", ["Morphological → syntactic → semantic → discourse and pragmatic analysis",
                                                                       "Semantic → syntactic → morphological", "Pragmatic → morphological → syntactic",
                                                                       "Syntactic → morphological → semantic"], 0, PYQ + "Rich & Knight list these five steps."),
    ("Splitting 'unhappiness' into un + happy + ness is", ["Morphological analysis", "Syntactic analysis", "Semantic analysis", "Pragmatic analysis"], 0,
     "Morphemes are the smallest meaningful units."),
    ("Natural-language syntax is usually modelled (approximately) with", ["Context-free grammars", "Regular grammars alone", "Turing machines", "Lookup tables"], 0,
     "Some features need more (agreement, cross-serial dependencies)."),
    ("A context-free grammar is a 4-tuple made of", ["Non-terminals, terminals, productions and a start symbol", "States, inputs, outputs and transitions",
                                                     "Nouns, verbs, adjectives and adverbs", "Tokens, rules, trees and parsers"], 0, "G = (V, T, P, S)."),
    ("A parse tree shows", ["How a sentence is derived from the start symbol by the grammar rules", "The meaning of the sentence", "How often each word occurs",
                            "The pronunciation"], 0, "Leaves are the words."),
    ("'I saw the man with a telescope' is an example of", ["Structural (syntactic) ambiguity – two parse trees", "Lexical ambiguity", "A spelling error",
                                                           "A pragmatic error"], 0, PYQ + "Who has the telescope? (prepositional-phrase attachment)"),
    ("The word 'bank' (river bank or money bank) shows", ["Lexical ambiguity", "Syntactic ambiguity", "Pragmatic ambiguity", "No ambiguity"], 0,
     "One word, several meanings."),
    ("Top-down parsing", ["Starts from the start symbol and expands rules to match the words", "Starts from the words and builds up to S", "Uses no grammar",
                          "Is the same as tokenisation"], 0, "Bottom-up parsing works the other way."),
    ("Shift-reduce parsing is a kind of", ["Bottom-up parsing", "Top-down parsing", "Semantic analysis", "Morphological analysis"], 0, "It shifts words onto a stack and reduces by rules."),
    ("The CYK parsing algorithm needs the grammar in", ["Chomsky normal form, and runs in O(n³) time", "Greibach normal form, in O(n) time", "Any form, in O(n²) time",
                                                       "Regular form, in O(1) time"], 0, PYQ + "A dynamic-programming parser."),
    ("Chart parsers such as Earley's algorithm avoid repeated work by", ["Storing partial parses (edges) in a chart – dynamic programming", "Random guessing",
                                                                         "Backtracking alone", "Ignoring the grammar"], 0, "Earley's algorithm handles any CFG in O(n³)."),
    ("Augmented transition networks (ATNs), used in early NLP systems, are", ["Recursive transition networks with registers and tests", "Neural networks",
                                                                              "Semantic networks", "Bayesian networks"], 0, "Woods (1970)."),
    ("A recursive-descent parser loops for ever on a rule such as", ["NP → NP PP (left recursion)", "NP → Det N", "VP → V NP", "S → NP VP"], 0,
     "Left recursion must be removed for top-down parsing."),
    ("With S → NP VP, NP → Det N and VP → V NP, how many NP nodes does the parse tree of 'the dog chased a cat' have?", ["2", "1", "3", "4"], 0,
     "'the dog' and 'a cat'."),
    ("Splitting text into words, numbers and punctuation marks is", ["Tokenisation", "Stemming", "Parsing", "Tagging"], 0, "Usually the first step of NLP."),
    ("Stemming differs from lemmatisation because stemming", ["Chops off suffixes by rules (studies → studi), while lemmatisation finds the dictionary form (study)",
                                                              "Uses a dictionary", "Translates words", "Tags parts of speech"], 0, PYQ + "The Porter stemmer is a classic example."),
    ("Words such as 'the', 'is' and 'of', often removed in text processing, are called", ["Stop words", "Stems", "Lemmas", "Named entities"], 0, "They carry little topic information."),
    ("Labelling each word as noun, verb, adjective and so on is", ["Part-of-speech (POS) tagging", "Parsing", "Stemming", "Translation"], 0, "A step before parsing."),
    ("A classic statistical model for part-of-speech tagging is the", ["Hidden Markov model", "Decision table", "Semantic network", "Script"], 0, "Decoded with the Viterbi algorithm."),
    ("A bigram language model estimates", ["P(wᵢ | wᵢ₋₁) – the probability of a word given the previous word", "The meaning of a sentence", "The grammar rules",
                                           "The part of speech"], 0, "N-gram models use the previous n − 1 words."),
    ("Finite-state transducers are widely used in NLP for", ["Morphological analysis", "Pragmatics", "Discourse analysis", "Speech synthesis alone"], 0,
     "Morphology is mostly regular."),
    ("Definite clause grammars (DCGs) are written in", ["PROLOG", "LISP", "C", "SQL"], 0, "Grammar rules become Horn clauses."),
    ("A dependency parse links", ["Each word to its head word with a labelled relation", "Words into nested phrases with no heads", "Words in alphabetical order",
                                  "Sentences into paragraphs"], 0, "Constituency parsing builds nested phrases."),
    ("Chomsky's sentence 'Colorless green ideas sleep furiously' is", ["Grammatically correct but meaningless", "Ungrammatical and meaningless", "Grammatical and meaningful",
                                                                       "A pragmatic error"], 0, PYQ + "Syntax and semantics are separate levels."),
    ("Subject–verb agreement ('he runs' but 'they run') is handled in grammars by", ["Feature structures and unification", "Stemming", "Stop-word removal", "Bigrams alone"], 0,
     "Features such as number and person must unify."),
    ("A probabilistic CFG resolves ambiguity by", ["Choosing the parse with the highest probability", "Choosing the shortest parse", "Rejecting the sentence", "Choosing at random"], 0,
     "Rule probabilities come from a treebank."),
    ("A treebank, such as the Penn Treebank, is", ["A corpus of sentences annotated with parse trees", "A database of word meanings", "A neural network", "A dictionary of stems"], 0,
     "Used to train and test parsers."),
]

SEMANTICS_PRAGMATICS = [
    kset("KSET 2023 CS&A · Q76"),
    ("Semantic analysis", ["Maps the syntactic structure of a sentence to a representation of its meaning", "Splits words into morphemes", "Checks spelling",
                           "Finds the speaker's intention"], 0, PYQ + "E.g. into first-order logic."),
    ("Compositional semantics says that", ["The meaning of a sentence is built from the meanings of its parts and the way they are combined", "Words have no meaning",
                                           "Only context matters", "Meaning comes from pronunciation"], 0, "Frege's principle."),
    ("Choosing the correct sense of 'bass' (fish or music) from the context is", ["Word sense disambiguation", "Stemming", "Parsing", "Tokenisation"], 0,
     "WordNet lists the senses."),
    ("WordNet is", ["A lexical database that groups English words into sets of synonyms (synsets)", "A neural network", "A parser", "A search engine"], 0,
     "It also links hypernyms (IS-A)."),
    ("In 'John cut the bread with a knife', the knife fills the case role", ["Instrument", "Agent", "Object", "Location"], 0,
     PYQ + "Fillmore's case grammar: John = agent, bread = object."),
    ("'Can you pass the salt?' is understood as a request, not a yes/no question. This is", ["Pragmatics (an indirect speech act)", "Morphology", "Syntax", "Phonology"], 0,
     "Speech-act theory (Austin, Searle)."),
    ("Working out that 'It' refers to 'the laptop' in 'I bought a laptop. It is fast.' is", ["Anaphora (coreference) resolution", "Stemming", "POS tagging",
                                                                                           "Spelling correction"], 0, "Part of discourse analysis."),
    ("Pragmatic analysis uses", ["Context, the speaker's intention and world knowledge", "Grammar alone", "Word endings", "Character codes"], 0,
     "Meaning beyond the literal words."),
    ("Modern machine-translation systems such as Google Translate mainly use", ["Neural networks (sequence-to-sequence / transformer models)",
                                                                                "Hand-written grammar rules alone", "Dictionaries alone", "Regular expressions"], 0,
     "Earlier systems were rule-based, then statistical."),
    ("TF–IDF gives a high weight to a word that is", ["Frequent in the document but rare across the collection", "Common in every document", "Rare in the document",
                                                      "A stop word"], 0, "Used in information retrieval."),
    ("Finding whether a product review is positive or negative is", ["Sentiment analysis", "Named-entity recognition", "Parsing", "Machine translation"], 0,
     "Also called opinion mining."),
    ("Finding the names of persons, places and organisations in text is", ["Named-entity recognition", "Stemming", "Sentiment analysis", "Summarisation"], 0,
     "A kind of information extraction."),
    ("IBM Watson, which won the quiz show Jeopardy! in 2011, is an example of", ["A question-answering system", "A chess program", "An image classifier", "A database"], 0,
     "It combined NLP, retrieval and machine learning."),
    ("Converting spoken words into text is", ["Speech recognition", "Speech synthesis", "Machine translation", "Parsing"], 0, "Text-to-speech is speech synthesis."),
    ("A semantic grammar uses categories such as", ["Domain concepts (e.g. FLIGHT, CITY) instead of purely syntactic ones", "Noun and verb alone", "Characters", "Numbers"], 0,
     "Useful in narrow-domain interfaces."),
    ("Large language models such as GPT are based on the", ["Transformer architecture with self-attention", "Hidden Markov model", "Decision tree", "Semantic network"], 0,
     "Vaswani et al., 'Attention is all you need' (2017)."),
    ("Word embeddings such as word2vec represent words as", ["Dense vectors in which words with similar meanings lie close together", "Single integers", "Parse trees",
                                                             "Bit strings of their spelling"], 0, "king − man + woman ≈ queen."),
    ("Saying 'It's cold in here' to ask someone to close the window is", ["An indirect speech act understood through pragmatics", "A syntax error", "Lexical ambiguity",
                                                                          "A morphological rule"], 0, "The literal meaning is a statement."),
    ("'Every dog barks' in first-order logic is", ["∀x (Dog(x) → Barks(x))", "∃x (Dog(x) ∧ Barks(x))", "∀x (Dog(x) ∧ Barks(x))", "Dog(Barks)"], 0,
     "Semantic analysis often targets logic."),
    ("Spelling correction usually uses the", ["Minimum edit (Levenshtein) distance", "Branching factor", "Alpha–beta pruning", "Gini index"], 0,
     "Insertions, deletions and substitutions."),
    ("The minimum edit distance between 'cat' and 'cut' is", ["1", "2", "3", "0"], 0, "One substitution."),
    ("Extractive summarisation", ["Selects the most important sentences from the text", "Writes new sentences", "Translates the text", "Removes stop words alone"], 0,
     "Abstractive summarisation writes new text."),
    ("Early chatbots such as ELIZA worked mainly by", ["Pattern matching and canned responses", "Deep understanding", "Neural translation", "Database queries"], 0,
     "No real understanding."),
    ("Schank's SAM program understood simple stories using", ["Scripts", "Neural networks", "Regular expressions", "Bigrams"], 0, "SAM = Script Applier Mechanism."),
    ("Pragmatics deals with", ["How context and intention affect the meaning of an utterance", "Word structure", "Sentence structure", "Spelling"], 0,
     "Morphology = words; syntax = structure; semantics = literal meaning."),
    ("The study of speech sounds is", ["Phonology", "Morphology", "Syntax", "Pragmatics"], 0, "Phonetics studies the physical sounds."),
    ("Filling a table of (company, CEO) pairs from news articles is", ["Information extraction", "Machine translation", "Speech recognition", "Stemming"], 0,
     "Uses NER and relation extraction."),
    ("The BLEU score is used to evaluate", ["Machine-translation output", "Parsing speed", "Speech loudness", "Spelling"], 0, "It compares n-grams with reference translations."),
    ("India's National Language Translation Mission platform, which offers AI-based translation between Indian languages, is", ["Bhashini", "Aadhaar", "DigiLocker",
                                                                                                                                "UMANG"], 0,
     PYQ + "Launched by MeitY in 2022."),
]

NEURAL_NETS = [
    kset("KSET 2023 CS&A · Q78"),
    kset("KSET 2023 CS&A · Q79"),
    kset("KSET 2024 CS&A · Q98"),
    kset("KSET 2025 CS&A · Q98"),
    kset("KSET 2025 CS&A · Q100"),
    kset("KSET 2025 CS&A · Q38"),
    kset("KSET 2024 CS&A · Q95"),
    ("What is the correct sequence for a reinforcement learning agent interacting with its environment?", ["Explore → Receive reward → Select Action → Update policy",
                                                                                                           "Select Action → Explore → Receive Reward → Update policy",
                                                                                                           "Select Action → Receive Reward → Explore → Update policy",
                                                                                                           "Explore → Select Action → Receive Reward → Update policy"], 3,
     "The agent explores, chooses an action, gets a reward and updates its policy." + GTTC, "GTTC 2024 Lecturer CS · Q91"),
    ("Match the following and choose the correct option:\nList-I (Terms)\na. Reinforcement learning (RL)\nb. Gradient Descent\nc. Generative Adversarial Networks (GAN)\n"
     "d. Support Vector Machine (SVM)\nList-II (Description)\ni. A supervised learning algorithm that finds a hyperplane to separate different classes in a high-dimensional space\n"
     "ii. A learning paradigm in which an agent learns to take actions in an environment to maximize cumulative rewards.\n"
     "iii. An iterative optimization algorithm used to minimize the cost function in machine learning models.\n"
     "iv. A machine learning framework where two neural networks contest into each other to generate new data samples.",
     ["a – iv, b – ii, c – iii, d – i", "a – ii, b – iii, c – i, d – iv", "a – ii, b – iii, c – iv, d – i", "a – i, b – iii, c – ii, d – iv"], 2,
     "RL – rewards; gradient descent – minimise cost; GAN – two competing networks; SVM – separating hyperplane." + GTTC, "GTTC 2024 Lecturer CS · Q92"),
    ("What is the purpose of a neural network in artificial intelligence?", ["To create a database for storing large amounts of data",
                                                                            "To design user interfaces for better human-computer interaction",
                                                                            "To mimic the structure of the human brain and incorporate natural language processing and deep learning",
                                                                            "To develop hardware that can run software applications"], 2, "Brain-inspired learning models." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q65"),
    ("Match the following terms with their correct descriptions:\nTerms\na) Supervised learning\nb) Unsupervised learning\nc) Neural network\nd) Reinforcement learning\n"
     "Definition\ni. A type of learning where model learns from labelled data\nii. Computational model inspired by human brain used for pattern recognition\n"
     "iii. A type of learning where an agent learns by interacting with its environment and receives rewards and penalties\n"
     "iv. A type of learning model finds patterns in unlabelled data", ["a – i, b – iv, c – ii, d – iii", "a – i, b – iii, c – iv, d – ii", "a – iv, b – ii, c – i, d – iii",
                                                                       "a – ii, b – i, c – iv, d – iii"], 0, "Labelled → supervised; unlabelled → unsupervised; rewards → RL." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q67"),
    ("What is Adaline in neural networks ?", ["Adaptive Linear Element", "Automatic Linear Element", "Adaptive Line Element", "Adaptive Nonlinear element"], 0,
     "Widrow and Hoff (1960), trained with the LMS (delta) rule." + NOTE, "GFGC 2021 CS · Q122"),
    ("Dendrites are", ["Fibers of nerves", "Nuclear projections", "Other name for nucleus", "Twisted network"], 0,
     "Dendrites are the input fibres of a biological neuron; the axon carries the output." + NOTE, "GFGC 2021 CS · Q123"),
    ("The first mathematical model of a neuron (1943) was proposed by", ["McCulloch and Pitts", "Rosenblatt", "Minsky and Papert", "Hinton"], 0,
     "A threshold logic unit."),
    ("A single-layer perceptron cannot learn the XOR function because", ["XOR is not linearly separable", "XOR has too many inputs", "The learning rate is too small",
                                                                        "XOR needs negative weights"], 0, PYQ + "Shown by Minsky and Papert (1969); a hidden layer solves it."),
    ("A perceptron with weights (1, 1), bias −1.5 and a step activation (output 1 if the sum ≥ 0) computes", ["AND", "OR", "XOR", "NOT"], 0,
     PYQ + "Only 1 + 1 − 1.5 ≥ 0."),
    ("The same perceptron with bias −0.5 computes", ["OR", "AND", "XOR", "NAND"], 0, "Any input of 1 gives ≥ 0."),
    ("The perceptron learning rule updates each weight as", ["w ← w + η (t − y) x", "w ← w − x", "w ← η w", "w ← t × y"], 0, "t = target, y = output, η = learning rate."),
    ("The sigmoid, tanh and ReLU activation functions have output ranges", ["(0, 1), (−1, 1) and [0, ∞)", "(−1, 1), (0, 1) and (0, 1)", "[0, 1], [0, 1] and [0, 1]",
                                                                           "(0, ∞), (−∞, 0) and (0, 1)"], 0, "ReLU(x) = max(0, x)."),
    ("Deep networks with sigmoid activations often suffer from", ["Vanishing gradients", "Exploding memory", "Too few weights", "No learning rate"], 0,
     "The sigmoid's slope is at most 0.25; ReLU helps."),
    ("Hebbian learning is summed up as", ["'Neurons that fire together wire together'", "Minimise the squared error", "Maximise the margin", "Follow the reward"], 0,
     "Donald Hebb (1949)."),
    ("One epoch of training means", ["One pass of the whole training set through the network", "One weight update", "One neuron", "One layer"], 0,
     "Mini-batches give several updates per epoch."),
    ("If the learning rate is too high, gradient descent", ["May overshoot and oscillate or diverge", "Always converges faster", "Stops at once", "Has no effect"], 0,
     "Too low makes training slow."),
    ("Dropout during training helps to", ["Reduce overfitting by randomly switching off neurons", "Speed up inference", "Add layers", "Increase overfitting"], 0,
     "A regularisation technique."),
    ("The softmax function at the output layer", ["Turns scores into probabilities that add up to 1 (multi-class classification)", "Removes negative weights",
                                                  "Is used only in regression", "Initialises the weights"], 0, "Used with cross-entropy loss."),
    ("Convolutional neural networks are best known for", ["Image recognition", "Database indexing", "Sorting", "Compiling code"], 0,
     "RNNs and LSTMs suit sequences such as text."),
    ("A Kohonen self-organising map learns", ["Without labels (unsupervised), forming a topology-preserving map", "From labelled data", "From rewards", "With backpropagation"], 0,
     "Competitive learning."),
    ("Backpropagation computes the gradient of the loss with respect to each weight and then", ["Updates the weights by gradient descent, layer by layer from the output back",
                                                                                               "Adds more layers", "Removes neurons", "Labels the data"], 0,
     "Rumelhart, Hinton and Williams (1986)."),
    ("A feed-forward network with 4 inputs, 3 hidden units and 2 outputs (no biases) has how many weights?", ["18", "9", "24", "14"], 0, "4 × 3 + 3 × 2 (n·h + h·m)."),
    ("A neuron with inputs (1, 0, 1), weights (0.5, 0.3, 0.2) and bias 0 has a net input of", ["0.7", "1.0", "0.5", "0.3"], 0, "0.5 + 0 + 0.2."),
]

LEARNING_APPLICATIONS = [
    kset("KSET 2024 CS&A · Q100"),
    kset("KSET 2025 CS&A · Q96"),
    kset("KSET 2025 CS&A · Q97"),
    kset("KSET 2024 CS&A · Q99"),
    ("____ is the purpose of a confusion matrix in machine learning.", ["To evaluate regression performance", "To visualize the relationship between features",
                                                                         "To summarize the performance of a classification model", "To reduce the dimensionality of the dataset"], 2,
     "It counts TP, FP, FN and TN." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q66"),
    ("A dataset contains a feature that takes value ranging from 1 to 100. If you decide to use Min-Max normalization, what will be the normalized value of a data point with a "
     "value of 50?", ["0", "0.25", "0.5", "1"], 2, "(50 − 1) / (100 − 1) ≈ 0.495, i.e. about 0.5." + GTTC, "GTTC 2024 Lecturer CS · Q98"),
    ("Predicting the price of a house is a", ["Regression problem", "Classification problem", "Clustering problem", "Reinforcement-learning problem"], 0,
     "The output is a continuous number."),
    ("The ID3 decision-tree algorithm chooses the attribute to split on by", ["Highest information gain (largest drop in entropy)", "Alphabetical order",
                                                                              "Random choice", "Lowest information gain"], 0, "C4.5 uses the gain ratio; CART uses the Gini index."),
    ("The entropy of a set with 50% positive and 50% negative examples is", ["1 bit", "0", "0.5 bit", "2 bits"], 0, PYQ + "−0.5 log₂ 0.5 − 0.5 log₂ 0.5 = 1."),
    ("k-nearest neighbours is called a lazy learner because it", ["Stores the training data and does the work only when classifying", "Never classifies",
                                                                   "Trains for a very long time", "Needs no data"], 0, "The class is decided by the k closest examples."),
    ("The naive Bayes classifier assumes that", ["The features are conditionally independent given the class", "All features are equal", "There is one class",
                                                 "The data is unlabelled"], 0, "Simple and effective for text."),
    ("A support vector machine chooses the separating hyperplane that", ["Maximises the margin to the nearest training points", "Passes through the most points",
                                                                         "Minimises the margin", "Is always vertical"], 0, "Kernels handle non-linear data."),
    ("A model that scores 99% on the training data but only 60% on the test data is", ["Overfitting", "Underfitting", "Perfect", "Unsupervised"], 0,
     "It has memorised the training data."),
    ("With TP = 40, FP = 10 and FN = 20, the precision is", ["0.8", "0.67", "0.5", "0.4"], 0, PYQ + "TP / (TP + FP) = 40 / 50. Recall = 40 / 60 ≈ 0.67."),
    ("With TP = 50, TN = 30, FP = 10 and FN = 10, the accuracy is", ["80%", "50%", "70%", "90%"], 0, "(50 + 30) / 100."),
    ("k-fold cross-validation", ["Trains and tests k times, each time holding out a different fold for testing", "Uses one fixed test set", "Trains without data",
                                 "Uses k different models on the same split"], 0, "Gives a more reliable estimate."),
    ("Q-learning learns", ["The value of each action in each state, without needing a model of the environment", "A parse tree", "Cluster centres", "A decision tree"], 0,
     "Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') − Q(s, a)]."),
    ("The exploration–exploitation trade-off in reinforcement learning is often handled with", ["An ε-greedy policy", "Bubble sort", "Backpropagation alone", "A parse chart"], 0,
     "Explore with probability ε, otherwise take the best known action."),
    ("In reinforcement learning, the discount factor γ (0 ≤ γ < 1)", ["Makes future rewards count less than immediate ones", "Sets the learning rate", "Counts the states",
                                                                      "Is the reward itself"], 0, "Return = r₀ + γ r₁ + γ² r₂ + …"),
    ("Agglomerative hierarchical clustering", ["Starts with each point as its own cluster and repeatedly merges the closest pair", "Starts with one cluster and splits it",
                                               "Needs labels", "Uses rewards"], 0, "The result is a dendrogram."),
    ("Principal component analysis (PCA) is used to", ["Reduce the number of dimensions while keeping most of the variance", "Classify images", "Cluster text",
                                                       "Train perceptrons"], 0, "An unsupervised technique."),
    ("The three main operators of a genetic algorithm are", ["Selection, crossover and mutation", "Push, pop and peek", "Shift, reduce and accept", "Map, filter and reduce"], 0,
     PYQ + "Inspired by natural evolution."),
    ("Single-point crossover of the parents 11000 and 00111 after the second bit gives the children", ["11111 and 00000", "11000 and 00111", "10101 and 01010",
                                                                                                        "11011 and 00100"], 0, "11|000 + 00|111 → 11111 and 00|000 → 00000."),
    ("Mutation in a genetic algorithm", ["Randomly flips (changes) some genes to keep diversity", "Combines two parents", "Selects the fittest", "Stops the algorithm"], 0,
     "It helps avoid premature convergence."),
    ("Which is NOT usually called an application of AI?", ["Sorting a list with bubble sort", "Medical diagnosis", "Self-driving cars", "Speech recognition"], 0,
     "A fixed algorithm with no learning or reasoning."),
    ("Recognising faces in photos is a task of", ["Computer vision", "Natural language processing", "Expert systems", "Speech synthesis"], 0, "Usually done with CNNs."),
    ("A robot building a map of an unknown place while tracking its own position is solving", ["SLAM (simultaneous localisation and mapping)", "OCR", "NER", "CYK parsing"], 0,
     "Used in self-driving cars and vacuum robots."),
    ("Recommendation systems on shopping sites mainly use", ["Machine learning on user behaviour, e.g. collaborative filtering", "Bubble sort", "Compilers", "Spreadsheets"], 0,
     "Users who liked X also liked Y."),
    ("Generative AI chatbots such as ChatGPT are examples of", ["Large language models that generate text", "Expert system shells", "Search-engine indexes", "Compilers"], 0,
     "Trained on large text corpora, then fine-tuned."),
    ("Bias in AI systems most often comes from", ["Unrepresentative or biased training data", "Too much RAM", "Fast processors", "The programming language"], 0,
     "A key concern of responsible AI."),
]

TOPICS = {
    "Natural Language Processing": [
        ("1 · Grammar and Language, and Parsing Techniques", GRAMMAR_PARSING),
        ("2 · Semantic Analysis, Pragmatics and NLP Applications", SEMANTICS_PRAGMATICS),
    ],
    "Artificial Neural Networks & Applications": [
        ("1 · Artificial Neural Networks – Neurons, Perceptron, Activation and Backpropagation", NEURAL_NETS),
        ("2 · Supervised, Unsupervised and Reinforcement Learning, and Applications of AI", LEARNING_APPLICATIONS),
    ],
}

NOTES = {
    "Natural Language Processing": [{"title": "NLP – revision sheet", "md": """## Levels of analysis
Phonology → morphology (morphemes, stemming vs lemmatisation) → syntax (parsing) → semantics (meaning) → discourse (anaphora) → pragmatics (context, intention, speech acts)

## Grammar and parsing
- CFG = (V, T, P, S); Chomsky hierarchy: type 0 unrestricted, 1 context-sensitive, 2 context-free, 3 regular
- Ambiguity: lexical ('bank'), structural ('saw the man with a telescope'), pragmatic
- Top-down (recursive descent, LL; fails on left recursion, uses leftmost derivation) vs bottom-up (shift-reduce, LR – uses a stack, rightmost derivation in reverse)
- CYK (CNF, O(n³)); Earley / chart parsing (dynamic programming); ATNs (Woods); DCGs in PROLOG; probabilistic CFGs; treebanks
- Dependency vs constituency parsing; feature structures + unification for agreement
- Text processing: tokenisation, stop words, stemming (Porter), POS tagging (HMM, Viterbi), n-gram models

## Semantics, pragmatics, applications
- Compositional semantics; logic forms (∀x Dog(x) → Barks(x)); case grammar (agent, object, instrument); WordNet synsets; word sense disambiguation
- Pragmatics: indirect speech acts; discourse: anaphora/coreference
- Scripts for story understanding (SAM); ELIZA (pattern matching)
- Applications: MT (rule → statistical → neural/transformer; BLEU), IR (TF–IDF), sentiment analysis, NER, information extraction, QA (IBM Watson 2011), speech recognition/synthesis, summarisation, chatbots/LLMs (GPT); India's Bhashini
- Edit distance for spelling correction (cat → cut = 1); word embeddings (word2vec)
"""}],
    "Artificial Neural Networks & Applications": [{"title": "Neural networks and learning – revision sheet", "md": """## Neural networks
- Biological: dendrites (inputs), soma, axon (output), synapses (weights)
- McCulloch–Pitts (1943); Hebb (1949); perceptron (Rosenblatt 1958): y = step(w·x + b), w ← w + η(t − y)x
- Perceptron (1, 1): bias −1.5 → AND, −0.5 → OR; cannot learn XOR (not linearly separable – Minsky & Papert 1969)
- Adaline (Widrow–Hoff, LMS); multilayer perceptron + backpropagation (chain rule, gradient descent on the loss)
- Activations: step, sigmoid (0, 1), tanh (−1, 1), ReLU max(0, x) – non-linearity; softmax for classes
- Parameters of n–h–m net (no biases) = nh + hm; epoch, learning rate, vanishing gradient, dropout, overfitting
- CNN (images), RNN/LSTM (sequences), transformer (LLMs), GAN (generator vs discriminator), Kohonen SOM (unsupervised), Hopfield (associative memory)

## Learning paradigms
- Supervised (labelled; classification, regression): decision trees (ID3 information gain, entropy 50/50 = 1 bit), kNN (lazy), naive Bayes, SVM (max margin)
- Unsupervised (unlabelled): k-means, hierarchical clustering, PCA
- Reinforcement (rewards): agent, state, action, reward, policy; Q-learning, ε-greedy, discount γ; inverse RL learns the reward from an expert
- Evaluation: confusion matrix; precision TP/(TP+FP), recall TP/(TP+FN), accuracy; k-fold cross-validation; min–max normalisation (x − min)/(max − min)

## Genetic algorithms and fuzzy logic
- Selection (roulette wheel, tournament, rank, Boltzmann, steady state; elitism keeps the best), crossover, mutation
- Fitness share f(x)/Σf(x): population 13, 24, 8, 19 with f = x² → 576/1170 = 49.2%
- Fuzzy: ∪ max, ∩ min, complement 1 − μ

## Applications of AI
Expert systems, NLP, speech, computer vision, robotics (SLAM), games, recommendation systems, self-driving cars, medical diagnosis; concerns: bias, explainability
"""}],
}
