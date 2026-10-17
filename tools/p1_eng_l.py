"""Paper 1 · General English · P1-ENG-12 Comprehension Passages (2 sub-topics × 20).
Coverage (planner): local, global, factual, critical, inferential comprehension.
Each question repeats its passage so that it can be read on its own in any order. REAL previous-year passages and questions come from
the KEA 2025–26 Kannada-English-Computer papers and the KSET 2024 and 2025 General Papers (no published key that matches; answers worked
out by ExamSim and marked so); printed spacing lost in the scans has been restored and one misprint ("was met merely") corrected to "was not merely". The other passages are short original passages
written for ExamSim in the same pattern."""

PYQ = "PYQ pattern (KEA / KSET reading comprehension). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

NATURE = ("Read the following passage and answer the question.\n(Note: In questions on synonyms and antonyms, the answer is to be given according to the sense in which the word has been used in the passage, not just on the basis of its literal meaning)\n"
          "Nature is like business. Business sense dictates that we guard our capital and live from the interest. Nature's capital is the enormous diversity of living things. "
          "Without it, we cannot feed ourselves, cure ourselves of illness or provide industry with the raw materials of wealth creation. Bad agriculture practice triggers twenty four billion "
          "tonnes of topsoil erosion a year losing the equivalent of 9 million tonnes of grain output. Cutting this kind of unsuitable exploitation and instituting \"Sustainable utilization\" "
          "will help turn the environmental crisis around.\n\n")
MANSION = ("Read the following passage carefully and choose the correct answer:\n"
           "The old mansion, abandoned for decades, carried a silence that was not merely the absence of sound, but a presence of memories left unspoken. Its corridors, once alive with "
           "laughter, now echoed only the faint whisper of time. Those who visited, claimed that the house mourned its forgotten inhabitants, as though every creaking floorboard remembered "
           "footsteps that would never return. Yet, amidst this melancholic decay, there remained an inexplicable beauty-proof that even ruin could preserve fragments of grace.\n\n")
WATER = ("Read the passage given below and answer the question that follows:\n"
         "Water conflicts have reached unmanageable levels in India. They have divided the country in many ways. There are divisions prevailing both between states and within states. "
         "Water conflicts have caused rifts between villages, castes and individuals. They have caused a serious threat to the federal structure of India. They have also affected the poor "
         "people the most.\nConflicts are the logical developments in the absence of proper democratic, legal and administrative mechanisms to handle the issues. The very nature of water is "
         "also a reason for this. It can be divided, carried and stored. One can include or exclude access to water for others.\nThe management of water conflicts requires multiple systems in "
         "place. It should include policy, political, social and ecological interventions. A sound legal system is also required to address and resolve disputes that arise out of "
         "socio-cultural issues. Water conflicts have always remained unresolved due to a lack of these interventional systems. Due to various political priorities, some water conflicts "
         "receive adequate attention, whereas some other conflicts receive insufficient attention.\n\n")
CENTURY = ("Read the passage given below and answer the question based on your understanding of the passage:\n"
           "The intellectual life of the 19th century was more complex than that of the previous age. This was due to several causes. First, the area concerned was larger than ever before; "
           "America and Russia made important contributions, and Europe became more aware than formerly of Indian philosophies, both ancient and modern. Second, science which had been a chief "
           "source of novelty since the 17th century, made new conquests, specially in Geology, Biology and Organic Chemistry. Third, machine production profoundly altered the social structure "
           "and gave men a conception of their powers in relation to the physical environment. Fourth, a profound revolt, both philosophical and political, against traditional systems in "
           "thought, in politics and in Economics, gave rise to attacks on many beliefs and institutions that had hitherto been regarded as unassailable. This revolt had two very different "
           "forms, one romantic, the other rationalistic. (I am using these words in a liberal sense). The romantic revolt passes from Byron to Schopenhauer and Nietzsche to Mussolini and "
           "Hitler; the rationalistic revolt begins with the French philosophers of the revolution, passes on, somewhat softened, to the philosophical radicals in England, then acquires a "
           "deeper form in Marx and issues in Soviet Russia.\n\n")
BOOKS = ("Read the following passage carefully and answer the question:\n"
         "Books are a great treasure house of knowledge. They are the living examples of man's march on the path to higher and higher civilization. The great men who died long ago live in "
         "their books. We feel their very personality and existence when we read their books. We feel as if they were conversing with us.\n"
         "Books not only store civilization, but also carry it forward. All coming generations get the light of knowledge from the books written by their ancestors and try to improve upon "
         "that knowledge. Civilization cannot make much headway in a country where there are not many great books. We get through books the latest knowledge in the fields of arts, science, "
         "commerce, etc. This knowledge is helpful to us and enables us to achieve success in the field of our choice.\n"
         "Books are never failing friends. They never desert us, not even when all fair-weather friends have deserted us. They dispel the dark clouds of gloom from our minds and increase our "
         "happiness if we are already happy. Through the ages, the scriptures and other great books have provided immeasurable solace to the wounded and strife-torn humanity.\n"
         "There may be books prescribed for some course or profession, but then there are books for general study. The books of literature poetry, drama, novel, short stories, etc., are "
         "generally highly thrilling and inspiring, if they are written by a good author. There may be tragic, comical or humorous books. The question is that of an individual's choice.\n"
         "To be a lover of books, though not to be a bookworm, is a sign of good luck. A voracious reader gets much more pleasure from reading books than a miser gets in hoarding money. "
         "The knowledge embedded in books is valuable; so is pleasure obtained from reading them. A good book absorbs the whole spirit of man; the reader's pleasure is indescribable.\n\n")

# original ExamSim passages
KERE = ("Read the passage and answer the question.\n"
        "For centuries, villages in Karnataka depended on tanks, or 'keres', built by local rulers and communities. A kere caught the monsoon rain, recharged the wells around it and gave "
        "water for cattle and crops through the dry months. Each village had a 'neerganti', a water-keeper, who opened the sluices fairly and kept the tank bed clean. When piped water and "
        "borewells arrived, many keres were neglected; encroachment and silt reduced their size. In recent years, several villages have desilted their tanks with the help of volunteers and "
        "the Panchayat, and the wells around them have filled again. The lesson is simple: water that is managed together lasts longer than water that each family pumps alone.\n\n")
TEACHER = ("Read the passage and answer the question.\n"
           "When Meena joined the village school as a teacher, half her pupils did not come regularly. Instead of scolding them, she visited their homes in the evenings. She learnt that "
           "many children looked after younger siblings while their parents worked in the fields. Meena started a small corner in the classroom where the little ones could play with blocks "
           "and picture books. Attendance rose within a month. Parents who had never visited the school began to attend meetings. 'I did not change the children,' Meena said later, 'I only "
           "changed the reason they had for staying away.'\n\n")
PLASTIC = ("Read the passage and answer the question.\n"
           "Plastic was once hailed as a wonder material: light, cheap and almost indestructible. Its greatest strength has become its greatest problem. A plastic bag used for twenty "
           "minutes may survive for hundreds of years, breaking into tiny pieces called microplastics that enter soil, rivers and even the food we eat. Bans on single-use plastic help, "
           "but they work only when people carry cloth bags, shops refuse to stock banned items and towns collect and recycle waste properly. The answer, therefore, lies less in a single "
           "law than in millions of small daily choices.\n\n")

FACTUAL_LOCAL = [
    (NATURE + "Choose the word which is nearly same in meaning to the word 'Triggers' as used in the passage.",
     ["Starts", "Makes", "Results", "Causes"], 3, "Bad agricultural practice 'triggers' (causes) soil erosion." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q61"),
    (NATURE + "Choose the word which is nearly opposite in meaning to the word 'Cutting' as used in the passage.",
     ["Uniting", "Increasing", "Joining", "Combining"], 1, "'Cutting' here means reducing exploitation; the opposite is increasing." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q62"),
    (MANSION + "The word \"melancholic\" in the passage is used as",
     ["A noun", "An adjective", "A verb", "An adverb"], 1, "'melancholic' qualifies the noun 'decay'." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q68"),
    (MANSION + "Choose the correct synonym for \"abandoned\".",
     ["Cherished", "Deserted", "Occupied", "Restored"], 1, "An abandoned house is deserted." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q69"),
    (WATER + "Which of the following is true in the context of the passage?",
     ["Water conflicts are absent in India.", "Water conflicts are the logical development in the absence of proper legal, democratic and administrative mechanisms.",
      "Villages have no water conflicts.", "The poor are not affected by water conflicts."], 1, "Stated directly at the start of the second paragraph." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q37"),
    (WATER + "Which of the following is the antonym of the word logical?",
     ["Mislogical", "Illogical", "Dislogical", "Imlogical"], 1, "The prefix il- is used before words beginning with l (illegal, illiterate, illogical)." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q38"),
    (CENTURY + "How many important causes does the author list out as responsible for the complexity of the intellectual life of 19th Century?",
     ["five", "four", "three", "six"], 1, "First, Second, Third and Fourth – four causes." + NOTE, "KSET 2024 General Paper · Q11"),
    (CENTURY + "Which area of the world became more aware of the Indian philosophies?",
     ["South America", "Europe", "Russia", "North America"], 1, "'…Europe became more aware than formerly of Indian philosophies'." + NOTE, "KSET 2024 General Paper · Q12"),
    (CENTURY + "What, according to the author, altered the social structure of the 19th Century?",
     ["Power structures", "Cultural systems", "Machine Production", "Physical Environment"], 2, "'Third, machine production profoundly altered the social structure'." + NOTE, "KSET 2024 General Paper · Q13"),
    (CENTURY + "Who began the rationalistic revolt, according to the author?",
     ["Mussolini", "French philosophers", "English radicals", "Nietzsche"], 1, "'the rationalistic revolt begins with the French philosophers of the revolution'." + NOTE, "KSET 2024 General Paper · Q14"),
    (CENTURY + "What does the author say about science in the 19th Century?",
     ["It had been the chief source of novelty", "It lacks moral responsibility", "It is the chief source of destruction", "It supported the established systems and institutions"], 0,
     "'science which had been a chief source of novelty since the 17th century, made new conquests'." + NOTE, "KSET 2024 General Paper · Q15"),
    (BOOKS + "Why are books, according to the passage, called 'never failing friends'?",
     ["Books do not betray individuals", "Books are inanimate", "Books give information to the reader", "Books are available in the market anytime unlike others"], 0,
     "'They never desert us, not even when all fair-weather friends have deserted us.'" + NOTE, "KSET 2025 General Paper · Q13"),
    (BOOKS + "Which of the following has been described as a sign of good luck?",
     ["Being a miser", "Having a lot of money", "Advancing the culture", "A passion for books"], 3, "'To be a lover of books… is a sign of good luck.'" + NOTE, "KSET 2025 General Paper · Q14"),
    (KERE + "According to the passage, who opened the sluices of the tank?",
     ["The neerganti (water-keeper)", "The local ruler", "The Panchayat president", "The volunteers"], 0, PYQ + "Factual question – the answer is stated in the passage."),
    (KERE + "The word 'encroachment' in the passage means:",
     ["Illegally occupying land that belongs to the tank", "Cleaning the tank", "Filling the tank with water", "Building a temple"], 0, PYQ + "Local (word-meaning) question; use the context."),
    (KERE + "What happened to the wells after the villages desilted their tanks?",
     ["They filled again", "They dried up", "They were closed", "They became salty"], 0, PYQ + "Stated in the passage."),
    (TEACHER + "Why were many pupils absent from Meena's school?",
     ["They looked after younger siblings while their parents worked", "They disliked the teacher", "The school was too far away", "They were ill"], 0, PYQ + "Factual detail."),
    (TEACHER + "Within how long did attendance rise?",
     ["A month", "A week", "A year", "Two days"], 0, PYQ + "'Attendance rose within a month.'"),
    (PLASTIC + "What are 'microplastics', according to the passage?",
     ["Tiny pieces into which plastic breaks", "A new kind of cloth bag", "A recycling machine", "Plastic used for twenty minutes"], 0, PYQ + "The definition is given in the passage."),
    (PLASTIC + "The word 'hailed' in the passage is closest in meaning to:",
     ["Praised", "Banned", "Frozen", "Called by shouting"], 0, PYQ + "'hailed as a wonder material' = welcomed with praise."),
]

INFERENTIAL_GLOBAL = [
    (NATURE + "Why does the author compare 'nature' to business?",
     ["Because of the capital depletion in nature and business", "Because of the similarity with which one should use both", "Because of the same interest level yield",
      "Because of the diversity of the various capital inputs"], 1, "Like a business, nature's capital must be guarded and only its 'interest' used." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q63"),
    (MANSION + "Identify the figure of speech used in:\n\"The house mourned its forgotten inhabitants\"",
     ["Simile", "Personification", "Hyperbole", "Metaphor"], 1, "A house is given the human feeling of mourning." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q70"),
    (WATER + "The author's main objective in writing the passage is to",
     ["Criticize the government.", "Prove that there are no water conflicts in India.", "Explain the various factors behind water conflicts.", "Say that water conflicts can never be resolved."], 2,
     "The passage explains the causes of water conflicts and what is needed to manage them." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q39"),
    (WATER + "Water conflicts can be resolved through\na. a sound legal system\nb. proper administrative mechanism\nc. understanding socio-cultural issues\nChoose the correct answer from the options given below.",
     ["c only", "a, b and c", "a only", "b only"], 1, "All three are mentioned as needed interventions." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q40"),
    (BOOKS + "How do books help in the progress of civilization?",
     ["Based on the earlier books, new knowledge is obtained", "Books provide solutions to many problems", "Books are a source of happiness", "Books are a means of livelihood"], 0,
     "Coming generations 'get the light of knowledge' from their ancestors' books and improve on it." + NOTE, "KSET 2025 General Paper · Q11"),
    (BOOKS + "What does the high quality of books produced by a country indicate?",
     ["It has a high rate of literacy", "It has a progressive civilization", "It is not an industrialized nation", "It has learned ancestors"], 1,
     "'Civilization cannot make much headway in a country where there are not many great books.'" + NOTE, "KSET 2025 General Paper · Q12"),
    (BOOKS + "Which of the following is the author's view about the knowledge and pleasure derived from books?\na) We get more of knowledge and less of pleasure.\nb) We get more of pleasure and less of knowledge.\nc) We get knowledge and pleasure in equal measure.",
     ["Only (a)", "Only (b)", "Either (a) or (b)", "Only (c)"], 3, "'The knowledge embedded in books is valuable; so is pleasure obtained from reading them.'" + NOTE, "KSET 2025 General Paper · Q15"),
    (KERE + "The main idea of the passage is that:",
     ["Water managed by the community lasts longer than water used individually", "Borewells are the best source of water", "Tanks should be filled with soil", "Rain is not needed in Karnataka"], 0,
     PYQ + "Global question – look at the last sentence."),
    (KERE + "Why were many keres neglected?",
     ["People came to depend on piped water and borewells", "The monsoon stopped completely", "Kings banned them", "Cattle drank all the water"], 0, PYQ + "Inference from the cause–effect link."),
    (KERE + "A suitable title for the passage is:",
     ["Reviving the Village Kere", "The History of Borewells", "Karnataka's Kings", "Cattle in Villages"], 0, PYQ + "A title reflects the central idea."),
    (KERE + "The author's attitude towards community water management is:",
     ["Approving", "Critical", "Indifferent", "Sarcastic"], 0, PYQ + "Critical (evaluative) comprehension – note 'The lesson is simple'."),
    (TEACHER + "What can be inferred about Meena's approach to problems?",
     ["She tried to understand the real cause before acting", "She believed in strict punishment", "She ignored the parents", "She wanted to leave the village"], 0, PYQ + "Inference from her home visits."),
    (TEACHER + "What does Meena mean by 'I only changed the reason they had for staying away'?",
     ["She removed the cause of absence by caring for the younger siblings at school", "She changed the children's behaviour by force", "She changed the school timings", "She gave the children money"], 0,
     PYQ + "Interpret the quotation in context."),
    (TEACHER + "The passage mainly shows that:",
     ["Understanding pupils' home situations can solve school problems", "Village children do not like school", "Parents never visit schools", "Teachers should not visit homes"], 0, PYQ + "Global comprehension."),
    (TEACHER + "Which quality of Meena is most clearly shown?",
     ["Empathy", "Anger", "Laziness", "Pride"], 0, PYQ + "Character inference."),
    (PLASTIC + "The phrase 'Its greatest strength has become its greatest problem' refers to plastic being:",
     ["Almost indestructible", "Light in weight", "Cheap", "Colourful"], 0, PYQ + "Plastic's durability makes it last for centuries as waste."),
    (PLASTIC + "According to the author, the solution to plastic pollution lies mainly in:",
     ["Millions of small daily choices along with laws", "A single strict law", "Making more plastic", "Burning plastic waste"], 0, PYQ + "Read the conclusion."),
    (PLASTIC + "Which of the following can be inferred from the passage?",
     ["A ban alone will fail if people and shops do not cooperate", "Plastic bags decompose in twenty minutes", "Microplastics are harmless", "Cloth bags are banned"], 0, PYQ + "Inferential comprehension."),
    (PLASTIC + "The tone of the passage is:",
     ["Thoughtful and persuasive", "Humorous", "Angry and abusive", "Romantic"], 0, PYQ + "Critical comprehension – the author argues for action calmly."),
    (PLASTIC + "Which statement would the author most likely agree with?",
     ["Carrying a cloth bag is a useful personal step against pollution", "Plastic is still a wonder material without problems", "Recycling is a waste of time", "Shops should stock more banned items"], 0,
     PYQ + "Critical comprehension – extend the author's argument."),
]

TOPICS = {
    "Comprehension Passages": [("1 · Factual and Local (Word-Level) Comprehension", FACTUAL_LOCAL),
                               ("2 · Inferential, Global and Critical Comprehension", INFERENTIAL_GLOBAL)],
}
