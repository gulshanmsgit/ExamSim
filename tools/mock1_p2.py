"""GPSTR / CST 2026 · Mock Set 1 · Paper 2 (Computer Science) – 100 new questions split by the planner's unit weights
(U1 10, U2 8, U3 10, U4 12, U5 12, U6 12, U7 8, U8 11, U9 12, U10 5). KEA level, in the mix seen in KEA CS Paper-2 (5 Jul 2026),
KSET and GTTC papers: direct/applied, numericals, code output, multi-statement, match-the-following, assertion–reason.
Every numerical and output was worked out by hand and checked. SECTIONS = [(unit tag, [questions])]."""
from packlib import AR

U1 = [
    ("(2F)₁₆ + (17)₈ in decimal is:", ["62", "60", "64", "58"], 0, "2F₁₆ = 47, 17₈ = 15; 47 + 15 = 62."),
    ("The 8-bit 2's complement of 00101100 is:", ["11010100", "11010011", "11010101", "10101100"], 0, "Invert → 11010011, add 1 → 11010100."),
    ("The Gray code of the binary number 1011 is:", ["1110", "1101", "1010", "0111"], 0, "MSB stays 1; then 1⊕0 = 1, 0⊕1 = 1, 1⊕1 = 0 → 1110."),
    ("The Excess-3 code of the decimal digit 5 is:", ["1000", "0101", "0111", "1001"], 0, "5 + 3 = 8 → 1000."),
    ("The Boolean expression A + A'B simplifies to:", ["A + B", "AB", "A", "A' + B"], 0, "Absorption: A + A'B = (A + A')(A + B) = A + B."),
    ("Match the computer generation with its technology:\na. First  b. Second  c. Third  d. Fourth\n1. Vacuum tubes  2. Transistors  3. Integrated circuits  4. VLSI microprocessors",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Standard classification of computer generations."),
    ("The minimum number of bits needed to represent the decimal number 1000 in unsigned binary is:", ["9", "10", "11", "12"], 1, "2⁹ = 512 < 1000 < 1024 = 2¹⁰."),
    ("A byte-addressable memory of 1 KB needs how many address lines?", ["8", "10", "12", "16"], 1, "1 KB = 2¹⁰ bytes → 10 address lines."),
    ("Assertion (A): NAND is called a universal gate.\nReason (R): NAND gates alone can be used to build AND, OR and NOT gates.", AR, 0,
     "Any Boolean function can be realised with only NAND (or only NOR) gates."),
    ("Consider the statements:\n(a) Cache memory sits between the CPU and main memory.\n(b) EEPROM is volatile.\n(c) Registers are faster than cache.\nWhich are correct?",
     ["(a) and (c)", "(a) and (b)", "(b) and (c)", "(a), (b) and (c)"], 0, "EEPROM is non-volatile; registers are the fastest storage."),
]

U2 = [
    ("The number of non-empty proper subsets of a set with 5 elements is:", ["30", "31", "32", "25"], 0, "2⁵ = 32 subsets; remove ∅ and the set itself → 30."),
    ("The number of edges in the complete graph K₆ is:", ["12", "15", "30", "36"], 1, "n(n−1)/2 = 6 × 5 / 2 = 15."),
    ("The minimum number of people needed to be sure that at least two were born in the same month is:", ["12", "13", "24", "25"], 1, "Pigeonhole: 12 months + 1 = 13."),
    ("The number of distinct arrangements of the letters of the word LEVEL is:", ["120", "60", "30", "20"], 2, "5!/(2! × 2!) = 120/4 = 30 (two L and two E)."),
    ("A connected planar graph has 8 vertices and 12 edges. The number of faces (including the outer face) is:", ["4", "5", "6", "7"], 2, "Euler: V − E + F = 2 → F = 2 − 8 + 12 = 6."),
    ("The proposition p → q is logically equivalent to:", ["q → p", "¬p → ¬q", "¬q → ¬p", "p ∧ ¬q"], 2, "The contrapositive is equivalent; converse and inverse are not."),
    ("A relation that is reflexive, symmetric and transitive is called a/an:", ["partial order", "equivalence relation", "total order", "function"], 1,
     "Partial order = reflexive, antisymmetric, transitive."),
    ("Consider the statements about a linear programming problem:\n(a) The feasible region is a convex set.\n(b) If an optimum exists, it occurs at a corner point of the feasible region.\n"
     "(c) An LPP always has a unique optimal solution.\nWhich are correct?", ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0,
     "An LPP can have multiple optima, an unbounded solution or no feasible solution."),
]

U3 = [
    ("A 5-stage pipeline with 1 time unit per stage executes 100 instructions without stalls. The total time is:", ["100", "104", "105", "500"], 1, "k + n − 1 = 5 + 100 − 1 = 104 units."),
    ("Cache access time is 10 ns and main memory access time is 100 ns. On a miss the cache is checked first and then main memory. With a hit ratio of 0.9, the average access time is:",
     ["19 ns", "20 ns", "28 ns", "91 ns"], 1, "0.9 × 10 + 0.1 × (10 + 100) = 9 + 11 = 20 ns."),
    ("The number of address lines needed for a 64K × 8 memory chip is:", ["8", "14", "16", "64"], 2, "64K = 2¹⁶ locations → 16 address lines (8 data lines)."),
    ("In which addressing mode is the operand itself part of the instruction?", ["Direct", "Indirect", "Immediate", "Register indirect"], 2, "Example: MOV A, #25."),
    ("A JK flip-flop with J = K = 1 on a clock edge:", ["sets the output", "resets the output", "toggles the output", "holds the output"], 2, "J = K = 1 → toggle; J = K = 0 → hold."),
    ("Arrange in order of decreasing speed:\n1. Main memory\n2. Registers\n3. Magnetic disk\n4. Cache", ["2, 4, 1, 3", "4, 2, 1, 3", "2, 1, 4, 3", "1, 2, 4, 3"], 0, "Registers > cache > main memory > disk."),
    ("Direct Memory Access (DMA) is used to:", ["let the CPU execute two programs at once", "transfer data between I/O and memory without the CPU moving each word",
                                               "increase the cache size", "translate virtual addresses"], 1, "The DMA controller takes the bus and the CPU is interrupted only at the end of the block."),
    ("Consider the statements about RISC processors:\n(a) They use a small set of simple, fixed-length instructions.\n(b) Most instructions execute in one clock cycle.\n"
     "(c) They rely mainly on microprogrammed control.\nWhich are correct?", ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0,
     "RISC uses hardwired control; CISC commonly uses microprogrammed control."),
    ("Assertion (A): Interrupt-driven I/O uses the CPU more efficiently than programmed (polled) I/O.\nReason (R): In programmed I/O the CPU keeps checking the device status and wastes cycles.", AR, 0,
     "With interrupts the CPU does other work until the device signals it."),
    ("Match the register with its role:\na. Program Counter  b. Instruction Register  c. Memory Address Register  d. Accumulator\n1. Address of the next instruction  2. Instruction being decoded  3. Address sent to memory  4. Holds an ALU operand/result",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-3, b-2, c-1, d-4"], 0, "Basic CPU registers."),
]

U4 = [
    ("What is printed by printf(\"%d\", 7 / 2 * 2); in C?", ["7", "6", "8", "3"], 1, "Integer division: 7/2 = 3, then 3 × 2 = 6."),
    ("int a[] = {1, 2, 3, 4}; int *p = a + 1; printf(\"%d\", *(p + 2));  prints:", ["2", "3", "4", "garbage"], 2, "p points to a[1]; p + 2 points to a[3] = 4."),
    ("int i; for (i = 0; i < 5; i++); printf(\"%d\", i);  prints:", ["0", "4", "5", "01234"], 2, "The semicolon makes the loop body empty; the loop ends with i = 5."),
    ("int x = 2;\nswitch (x) { case 1: printf(\"A\"); case 2: printf(\"B\"); case 3: printf(\"C\"); break; default: printf(\"D\"); }\nThe output is:",
     ["B", "BC", "BCD", "ABC"], 1, "Execution starts at case 2 and falls through to case 3 until break."),
    ("Which storage class in C keeps a local variable's value between function calls?", ["auto", "register", "static", "extern"], 2, "A static local is initialised once and retains its value."),
    ("In C++, which of the following gives run-time polymorphism?", ["Function overloading", "Operator overloading", "Virtual functions", "Templates"], 2,
     "Overloading and templates are resolved at compile time."),
    ("Which statement about constructors is INCORRECT?", ["A constructor has the same name as the class", "A constructor has no return type",
                                                          "A constructor can be overloaded", "A constructor must always be declared virtual"], 3,
     "Constructors cannot be virtual in C++; destructors can."),
    ("Match the OOP concept with its description:\na. Encapsulation  b. Inheritance  c. Polymorphism  d. Abstraction\n1. Binding data and methods together  2. Reusing a base class  3. One interface, many forms  4. Showing only essential features",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Four pillars of OOP."),
    ("In CSS, which selector has the highest specificity?", ["p", ".note", "#main", "*"], 2, "ID > class > element > universal."),
    ("In JavaScript, typeof null returns:", ["\"null\"", "\"undefined\"", "\"object\"", "\"number\""], 2, "A long-standing quirk of the language."),
    ("Consider the statements about HTML:\n(a) <h1> is the largest default heading.\n(b) The <a> tag uses the href attribute for the link target.\n(c) <br> needs a closing </br> tag.\nWhich are correct?",
     ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0, "<br> is an empty (void) element."),
    ("Assertion (A): In C, an array name used in an expression usually decays to a pointer to its first element.\nReason (R): sizeof applied to an array name gives the size of a pointer.", AR, 2,
     "sizeof(array) gives the size of the whole array – one of the exceptions to decay – so R is false."),
]

U5 = [
    ("A relation is in 2NF and has no transitive dependency of a non-prime attribute on a key. The relation is in at least:", ["1NF only", "2NF only", "3NF", "BCNF"], 2,
     "2NF removes partial dependencies; 3NF also removes transitive dependencies."),
    ("For R(A, B, C, D) with FDs A → B, B → C, C → D, the candidate key is:", ["A", "B", "AB", "CD"], 0, "A⁺ = {A, B, C, D}."),
    ("Relation R has 3 tuples and S has 4 tuples. The number of tuples in R × S is:", ["7", "12", "3", "4"], 1, "Cartesian product: 3 × 4 = 12."),
    ("Which SQL clause filters groups after aggregation?", ["WHERE", "HAVING", "ORDER BY", "DISTINCT"], 1, "WHERE filters rows before grouping; HAVING filters groups."),
    ("The 'I' in ACID properties means that:", ["a transaction is all-or-nothing", "concurrent transactions do not interfere with each other",
                                               "committed data survives failures", "the database moves from one valid state to another"], 1,
     "Atomicity, Consistency, Isolation, Durability."),
    ("A column EMP.bonus has values 100, NULL, 200, NULL. SELECT COUNT(*), COUNT(bonus) FROM EMP returns:", ["4, 4", "4, 2", "2, 2", "2, 4"], 1, "COUNT(column) ignores NULLs."),
    ("Which of the following is a DDL command?", ["UPDATE", "DELETE", "TRUNCATE", "SELECT"], 2, "TRUNCATE (like CREATE, ALTER, DROP) is DDL; the others are DML."),
    ("The entity integrity constraint states that:", ["a foreign key must match a primary key", "a primary key cannot be NULL", "all attributes must be atomic", "no relation can be empty"], 1,
     "Referential integrity is about foreign keys."),
    ("Two-phase locking (2PL) guarantees:", ["freedom from deadlock", "conflict serializability", "no cascading rollback in every case", "maximum concurrency"], 1,
     "2PL ensures conflict-serializable schedules but can still deadlock; strict 2PL avoids cascading rollbacks."),
    ("In a B+ tree:", ["records (or data pointers) are stored only in leaf nodes", "every node stores data pointers", "leaf nodes are not linked", "the tree need not be balanced"], 0,
     "Internal nodes hold only keys for navigation; leaves are linked for range queries."),
    ("A weak entity set is identified by:", ["its own primary key", "a partial key together with the key of its owner entity", "a foreign key only", "a surrogate key only"], 1,
     "Shown by a double rectangle and an identifying relationship."),
    ("Match the relational algebra operator with its symbol:\na. Selection  b. Projection  c. Union  d. Join\n1. σ  2. π  3. ∪  4. ⋈",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Selection picks rows; projection picks columns."),
]

U6 = [
    ("Processes P1, P2, P3 arrive at time 0 in that order with burst times 24, 3 and 3 ms. Under FCFS the average waiting time is:", ["3 ms", "17 ms", "10 ms", "27 ms"], 1,
     "Waits 0, 24, 27 → 51/3 = 17 ms."),
    ("For the same processes (24, 3, 3 ms, all at time 0), the average waiting time under non-preemptive SJF is:", ["3 ms", "6 ms", "9 ms", "17 ms"], 0,
     "Order 3, 3, 24 → waits 0, 3, 6 → 9/3 = 3 ms."),
    ("With 3 frames and FIFO replacement, the reference string 7, 0, 1, 2, 0, 3, 0, 4 causes how many page faults?", ["5", "6", "7", "8"], 2,
     "7F 0F 1F 2F(7 out) 0 hit 3F(0 out) 0F(1 out) 4F(2 out) → 7 faults."),
    ("Belady's anomaly can occur with:", ["LRU", "Optimal", "FIFO", "All of these"], 2, "Only FIFO (a non-stack algorithm) can get more faults with more frames."),
    ("Which is NOT one of the four necessary conditions for deadlock?", ["Mutual exclusion", "Hold and wait", "Preemption", "Circular wait"], 2, "The condition is NO preemption."),
    ("The Banker's algorithm is used for deadlock:", ["prevention", "avoidance", "detection", "recovery"], 1, "It grants a request only if the system stays in a safe state."),
    ("The Linux command chmod 754 file gives the permissions:", ["rwxr-xr--", "rwxr-x--x", "rw-r-xr--", "rwxrw-r--"], 0, "7 = rwx (owner), 5 = r-x (group), 4 = r-- (others)."),
    ("A system uses 32-bit logical addresses and 4 KB pages. The number of bits for the page number is:", ["12", "20", "22", "32"], 1, "Offset = 12 bits (4 KB); 32 − 12 = 20."),
    ("Disk head is at cylinder 50. Requests in order: 82, 170, 43, 140. Under FCFS the total head movement is:", ["294", "324", "344", "364"], 2,
     "|82−50| + |170−82| + |43−170| + |140−43| = 32 + 88 + 127 + 97 = 344."),
    ("When a system spends more time paging than executing, the condition is called:", ["starvation", "thrashing", "deadlock", "fragmentation"], 1, "Caused by too few frames for the working set."),
    ("Assertion (A): A counting semaphore can take values greater than 1.\nReason (R): A binary semaphore can be used to implement mutual exclusion.", AR, 1,
     "Both true; R is about binary semaphores and does not explain A."),
    ("Match the compiler phase with its output:\na. Lexical analysis  b. Syntax analysis  c. Intermediate code generation  d. Code generation\n1. Tokens  2. Parse tree  3. Three-address code  4. Target machine code",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Phases of a compiler."),
]

U7 = [
    ("The software process model that puts the most emphasis on risk analysis is:", ["Waterfall", "Spiral", "V-model", "Big Bang"], 1, "Boehm's spiral model has a risk-analysis phase in every loop."),
    ("A control-flow graph has 10 edges, 8 nodes and 1 connected component. Its cyclomatic complexity is:", ["2", "3", "4", "18"], 2, "V(G) = E − N + 2P = 10 − 8 + 2 = 4."),
    ("Equivalence partitioning and boundary value analysis are techniques of:", ["white-box testing", "black-box testing", "regression testing only", "static analysis"], 1,
     "They use only the specification, not the code."),
    ("A good design has:", ["high coupling and low cohesion", "low coupling and high cohesion", "high coupling and high cohesion", "low coupling and low cohesion"], 1,
     "Modules should be independent (low coupling) and focused (high cohesion)."),
    ("Alpha testing is carried out:", ["by end users at their own site", "by the customer after delivery only", "by users at the developer's site", "by automated tools only"], 2,
     "Beta testing is by real users at their own sites."),
    ("Modifying software so that it works on a new operating system is called:", ["corrective maintenance", "adaptive maintenance", "perfective maintenance", "preventive maintenance"], 1,
     "Adaptive maintenance responds to changes in the environment."),
    ("In Scrum, a fixed time-box (usually 2–4 weeks) in which a usable increment is built is called a:", ["sprint", "milestone", "baseline", "release train"], 0, "Planned at sprint planning, reviewed at the sprint review."),
    ("Consider the statements about COCOMO:\n(a) Basic COCOMO estimates effort from size in KLOC.\n(b) The three modes are organic, semi-detached and embedded.\n(c) Effort grows linearly with size in all modes.\nWhich are correct?",
     ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0, "Effort = a(KLOC)^b with b > 1, so it grows faster than linearly."),
]

U8 = [
    ("The postfix form of A + B * C − D is:", ["AB+C*D−", "ABC*+D−", "ABC*D−+", "AB*C+D−"], 1, "* first: A + (BC*) − D → ABC*+ then D−."),
    ("The value of the postfix expression 6 2 3 + − 3 8 2 / + * is:", ["1", "7", "49", "5"], 1, "6 − (2+3) = 1; 3 + 8/2 = 7; 1 × 7 = 7."),
    ("The maximum number of nodes in a binary tree with 5 levels (root at level 1) is:", ["16", "25", "31", "32"], 2, "2⁵ − 1 = 31."),
    ("Which traversal of a binary search tree lists the keys in sorted order?", ["Preorder", "Inorder", "Postorder", "Level order"], 1, "Left, root, right gives ascending order."),
    ("A binary tree has preorder A B D E C F and inorder D B E A F C. Its postorder is:", ["D E B F C A", "D B E F C A", "E D B F C A", "D E B C F A"], 0,
     "Root A; left subtree B(D, E); right subtree C with left child F → D E B F C A."),
    ("The worst-case time complexity of quicksort and merge sort respectively is:", ["O(n log n), O(n log n)", "O(n²), O(n log n)", "O(n log n), O(n²)", "O(n²), O(n²)"], 1,
     "Quicksort degrades to O(n²) with bad pivots; merge sort is always O(n log n)."),
    ("The maximum number of comparisons binary search needs on a sorted array of 1000 elements is about:", ["10", "100", "500", "1000"], 0, "⌈log₂ 1001⌉ = 10."),
    ("Breadth-first search of a graph is usually implemented with a:", ["stack", "queue", "priority queue only", "hash table only"], 1, "DFS uses a stack (or recursion)."),
    ("A spanning tree of a connected graph with 10 vertices has how many edges?", ["8", "9", "10", "45"], 1, "A tree with n vertices has n − 1 edges."),
    ("Dijkstra's shortest-path algorithm follows the:", ["divide-and-conquer approach", "greedy approach", "dynamic-programming approach only", "backtracking approach"], 1,
     "It always picks the nearest unvisited vertex; it fails with negative edge weights."),
    ("Assertion (A): Linear probing can cause primary clustering in a hash table.\nReason (R): In linear probing a colliding key is placed in the next free slot, so filled slots form long runs.", AR, 0,
     "Long runs of occupied slots increase search time; quadratic probing reduces this."),
]

U9 = [
    ("Routing of packets between networks is the job of the OSI:", ["data link layer", "network layer", "transport layer", "session layer"], 1, "Routers work at layer 3."),
    ("The IP address 172.16.5.4 belongs to class:", ["A", "B", "C", "D"], 1, "First octet 128–191 → class B."),
    ("A /26 subnet provides how many usable host addresses?", ["30", "62", "64", "126"], 1, "32 − 26 = 6 host bits → 2⁶ − 2 = 62."),
    ("Match the protocol with its default port:\na. HTTPS  b. DNS  c. SMTP  d. SSH\n1. 443  2. 53  3. 25  4. 22",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Well-known ports."),
    ("The time to put a 1000-byte frame on a 1 Mbps link (transmission delay) is:", ["1 ms", "8 ms", "0.8 ms", "80 ms"], 1, "8000 bits ÷ 10⁶ bit/s = 8 ms."),
    ("The Hamming distance between 10101 and 11110 is:", ["2", "3", "4", "1"], 1, "XOR = 01011 → three 1s."),
    ("Classic Ethernet (IEEE 802.3) uses the access method:", ["CSMA/CA", "CSMA/CD", "Token passing", "Polling"], 1, "CSMA/CA is used by Wi-Fi (802.11)."),
    ("An IPv6 address is how many bits long?", ["32", "64", "128", "256"], 2, "Written as eight groups of four hex digits."),
    ("With a 3-bit sequence number, the maximum send window in Go-Back-N ARQ is:", ["3", "4", "7", "8"], 2, "2ⁿ − 1 = 7 (Selective Repeat: 2ⁿ⁻¹ = 4)."),
    ("Which is a symmetric-key encryption algorithm?", ["RSA", "Diffie–Hellman", "AES", "ECC"], 2, "AES uses one shared key; the others are public-key methods."),
    ("Consider the statements about TCP:\n(a) A connection is set up with a three-way handshake.\n(b) TCP guarantees in-order, reliable delivery.\n(c) TCP is a connectionless protocol.\nWhich are correct?",
     ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0, "UDP is the connectionless transport protocol."),
    ("Assertion (A): CRC can detect all burst errors shorter than the degree of the generator polynomial.\nReason (R): CRC uses modulo-2 division of the data by a generator polynomial.", AR, 1,
     "Both statements are true; R describes how CRC is computed, not why it catches short bursts."),
]

U10 = [
    ("The test proposed by Alan Turing in 1950 judges a machine intelligent if:", ["it solves mathematical theorems", "a human judge cannot tell it apart from a human in conversation",
                                                                                  "it plays chess better than humans", "it learns without data"], 1, "The 'imitation game'."),
    ("A* search is guaranteed to find an optimal path (tree search) when its heuristic is:", ["admissible", "negative", "random", "always zero only"], 0,
     "f(n) = g(n) + h(n); h must never overestimate the true cost."),
    ("A single-layer perceptron cannot learn the function:", ["AND", "OR", "NOT", "XOR"], 3, "XOR is not linearly separable; a hidden layer is needed."),
    ("Reducing words such as 'playing', 'played' and 'plays' to 'play' in NLP is called:", ["tokenisation", "stemming", "parsing", "named-entity recognition"], 1,
     "Lemmatisation does the same using a dictionary."),
    ("Forward chaining in a rule-based system is:", ["goal-driven", "data-driven", "random", "used only in neural networks"], 1, "It starts from known facts; backward chaining starts from the goal."),
]

SECTIONS = [("Unit 1 – Fundamentals", U1), ("Unit 2 – Discrete Structures", U2), ("Unit 3 – Computer Architecture", U3), ("Unit 4 – Programming & Web", U4),
            ("Unit 5 – DBMS", U5), ("Unit 6 – OS & System Software", U6), ("Unit 7 – Software Engineering", U7), ("Unit 8 – Data Structures & Algorithms", U8),
            ("Unit 9 – Networks", U9), ("Unit 10 – Artificial Intelligence", U10)]
