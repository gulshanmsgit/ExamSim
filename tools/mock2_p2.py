"""GPSTR / CST 2026 · Mock Set 2 · Paper 2 (Computer Science) – 100 new questions in the planner's unit weights (same format as
tools/mock1_p2.py). Every numerical and code output was worked out by hand."""
from packlib import AR

U1 = [
    ("(1101.11)₂ in decimal is:", ["13.75", "13.5", "11.75", "13.3"], 0, "8 + 4 + 1 = 13; .11₂ = 0.5 + 0.25 = 0.75."),
    ("The BCD (8421) code of the decimal number 59 is:", ["0101 1001", "0011 1011", "0101 1010", "0111 1001"], 0, "Each digit separately: 5 = 0101, 9 = 1001."),
    ("The hexadecimal equivalent of 11010110₂ is:", ["D6", "C6", "D5", "B6"], 0, "1101 = D, 0110 = 6."),
    ("The 1's complement of 1010 is:", ["0101", "0110", "1011", "1101"], 0, "Invert every bit."),
    ("(A + B)(A + B') simplifies to:", ["A", "B", "AB", "A + B"], 0, "= A + BB' = A + 0 = A."),
    ("By De Morgan's theorem, (A·B)' equals:", ["A'·B'", "A' + B'", "A + B", "(A + B)'"], 1, "(AB)' = A' + B' and (A + B)' = A'·B'."),
    ("An XOR gate gives output 1 when:", ["both inputs are 1", "both inputs are 0", "the inputs are different", "at least one input is 1"], 2, "A ⊕ B = A'B + AB'."),
    ("Consider the statements:\n(a) Standard ASCII is a 7-bit code.\n(b) Unicode can represent Kannada characters.\n(c) EBCDIC was used on IBM mainframes.\nWhich are correct?",
     ["(a) and (b)", "(b) and (c)", "(a) and (c)", "(a), (b) and (c)"], 3, "All three are correct."),
    ("Assertion (A): A compiler translates the whole source program before execution.\nReason (R): An interpreter produces a separate object-code file.", AR, 2,
     "An interpreter translates and executes statement by statement and does not produce an object file."),
    ("The number of rows in the truth table of a function of 4 variables is:", ["8", "16", "32", "4"], 1, "2⁴ = 16."),
]

U2 = [
    ("The number of reflexive relations on a set with 3 elements is:", ["8", "64", "512", "27"], 1, "2^(n² − n) = 2⁶ = 64."),
    ("The value of C(10, 3) is:", ["720", "120", "210", "30"], 1, "10 × 9 × 8 / 6 = 120."),
    ("A graph has 10 edges. The sum of the degrees of all its vertices is:", ["10", "20", "5", "100"], 1, "Handshaking lemma: sum of degrees = 2 × edges."),
    ("Which of the following is a tautology?", ["p ∧ ¬p", "p ∨ ¬p", "p → ¬p", "p ∧ q"], 1, "p ∨ ¬p is always true; p ∧ ¬p is a contradiction."),
    ("The number of edges in the complete bipartite graph K₃,₃ is:", ["6", "9", "15", "3"], 1, "m × n = 3 × 3 = 9."),
    ("The number of functions from a set of 3 elements to a set of 2 elements is:", ["6", "8", "9", "5"], 1, "|B|^|A| = 2³ = 8."),
    ("A Hasse diagram is used to represent a:", ["partial order", "equivalence relation", "function", "group"], 0, "It shows a poset without loops and transitive edges."),
    ("A full binary tree has 7 internal nodes. The number of leaves is:", ["6", "7", "8", "14"], 2, "In a full binary tree, leaves = internal nodes + 1."),
]

U3 = [
    ("A CPU runs at 2 GHz and an instruction takes 4 clock cycles. The time for one instruction is:", ["0.5 ns", "2 ns", "4 ns", "8 ns"], 1, "Clock period = 0.5 ns; 4 × 0.5 = 2 ns."),
    ("If 40% of a program can be parallelised, the maximum speed-up with unlimited processors (Amdahl's law) is about:", ["1.4", "1.67", "2.5", "40"], 1, "1 / (1 − 0.4) = 1/0.6 ≈ 1.67."),
    ("A direct-mapped cache has 64 lines of 16 bytes each and addresses are 32 bits. The tag, index and offset bits are:", ["22, 6, 4", "20, 8, 4", "24, 4, 4", "22, 4, 6"], 0,
     "Offset log₂16 = 4, index log₂64 = 6, tag 32 − 10 = 22."),
    ("Zero-address instructions are used in:", ["accumulator-based machines", "stack-based machines", "register-memory machines", "RISC load/store machines"], 1, "Operands are taken from the top of the stack."),
    ("Two positive signed numbers are added and the result appears negative. This indicates:", ["a carry only", "an overflow", "an underflow", "a parity error"], 1, "Overflow = carry into the sign bit ≠ carry out of it."),
    ("In a D flip-flop, the next state Q(t+1) equals:", ["Q(t)", "D", "D'", "Q(t)'"], 1, "The output follows the input at the clock edge."),
    ("Consider the statements about cache write policies:\n(a) Write-through updates main memory on every write.\n(b) Write-back uses a dirty bit.\n(c) Write-back always causes more memory traffic than write-through.\nWhich are correct?",
     ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0, "Write-back usually causes less traffic because a block is written only when replaced."),
    ("Assertion (A): SRAM must be refreshed periodically.\nReason (R): DRAM stores each bit as charge on a capacitor.", AR, 3,
     "SRAM uses flip-flops and needs no refresh; DRAM leaks charge and must be refreshed."),
    ("Daisy chaining is a method of:", ["memory interleaving", "assigning interrupt priority", "cache replacement", "pipelining"], 1, "Devices are connected in series; the nearest has the highest priority."),
    ("A control memory in a microprogrammed control unit stores:", ["user programs", "microinstructions", "data operands", "page tables"], 1, "Each machine instruction is carried out by a microprogram."),
]

U4 = [
    ("printf(\"%d\", 10 % 3 * 2); prints:", ["2", "6", "0", "1"], 0, "% and * have equal precedence, left to right: (10 % 3) × 2 = 1 × 2 = 2."),
    ("char s[] = \"KEA\"; printf(\"%d\", sizeof(s)); prints:", ["3", "4", "2", "8"], 1, "Three characters plus the terminating '\\0'."),
    ("int x = 5; int *p = &x; *p = *p + 2; printf(\"%d\", x); prints:", ["5", "7", "2", "an address"], 1, "x is changed through the pointer."),
    ("int i = 1, s = 0; while (i <= 5) { s += i; i += 2; } printf(\"%d\", s); prints:", ["15", "9", "6", "5"], 1, "s = 1 + 3 + 5 = 9."),
    ("int f(int n) { return n <= 1 ? 1 : n * f(n - 1); }  The value of f(4) is:", ["10", "24", "12", "4"], 1, "4 × 3 × 2 × 1 = 24."),
    ("printf(\"%d\", 'A' + 1); prints:", ["B", "66", "65", "A1"], 1, "ASCII of 'A' is 65; %d prints the integer 66."),
    ("Which of the following is NOT a primitive data type in Java?", ["int", "boolean", "char", "String"], 3, "String is a class."),
    ("In C++, the default access specifier for members of a class is:", ["public", "private", "protected", "friend"], 1, "For a struct the default is public."),
    ("In an HTML form, the method that sends the form data in the URL is:", ["POST", "GET", "PUT", "DELETE"], 1, "GET appends data as a query string; POST sends it in the request body."),
    ("The CSS box model, from the inside out, is:", ["content, padding, border, margin", "content, border, padding, margin", "padding, content, border, margin", "margin, border, padding, content"], 0,
     "Padding is inside the border; margin is outside."),
    ("Match the C function with its purpose:\na. malloc  b. calloc  c. realloc  d. free\n1. Allocate a block (contents not initialised)  2. Allocate and set to zero  3. Resize an allocated block  4. Release memory",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Dynamic memory functions in <stdlib.h>."),
    ("Assertion (A): Java programs are platform independent.\nReason (R): Java supports multithreading.", AR, 1,
     "Platform independence comes from bytecode running on the JVM, not from multithreading."),
]

U5 = [
    ("For R(A, B, C) with FDs AB → C and C → B, the candidate keys are:", ["AB only", "AB and AC", "AC only", "ABC"], 1, "AB⁺ = ABC and AC⁺ = ACB; neither A, B nor C alone is a key."),
    ("The relation R(A, B, C) with AB → C and C → B is in:", ["BCNF", "3NF but not BCNF", "2NF but not 3NF", "1NF only"], 1,
     "C → B violates BCNF (C is not a superkey), but B is a prime attribute, so 3NF holds."),
    ("A LEFT OUTER JOIN of R and S returns:", ["only matching rows", "all rows of R, with NULLs where S has no match", "all rows of S only", "the Cartesian product"], 1, "Unmatched right-side columns are filled with NULL."),
    ("Two operations of different transactions conflict if they access the same data item and:", ["both are reads", "at least one is a write", "both are commits", "they are in the same transaction"], 1,
     "Read–write, write–read and write–write pairs conflict."),
    ("In the wait-die deadlock-prevention scheme, when an older transaction requests a lock held by a younger one, the older transaction:", ["is rolled back", "waits", "pre-empts the younger", "aborts the younger"], 1,
     "Older waits, younger dies; in wound-wait the older wounds (aborts) the younger."),
    ("How many clustered indexes can a table have?", ["One", "Two", "Any number", "None"], 0, "The rows can be physically ordered in only one way."),
    ("A view in SQL is:", ["a stored copy of a table", "a virtual table defined by a query", "an index", "a trigger"], 1, "Materialised views store results; ordinary views do not."),
    ("First normal form requires that:", ["there are no partial dependencies", "every attribute holds atomic values", "there are no transitive dependencies", "every determinant is a key"], 1, "No repeating groups or multi-valued cells."),
    ("A foreign key:", ["uniquely identifies each row of its own table", "refers to the primary key of another (or the same) table", "can never be NULL", "must be numeric"], 1,
     "It enforces referential integrity; it can be NULL unless declared NOT NULL."),
    ("Match the SQL command with its category:\na. COMMIT  b. GRANT  c. ALTER  d. INSERT\n1. TCL  2. DCL  3. DDL  4. DML",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Transaction, data-control, data-definition and data-manipulation languages."),
    ("Assertion (A): Checkpoints reduce the time needed for recovery after a crash.\nReason (R): Transactions that committed before the checkpoint need not be redone.", AR, 0,
     "Recovery starts from the last checkpoint instead of the beginning of the log."),
    ("SELECT DISTINCT dept FROM emp; returns:", ["every row of emp", "each department name once", "the number of departments", "only NULL departments"], 1, "DISTINCT removes duplicate values."),
]

U6 = [
    ("P1, P2, P3 arrive at time 0 with bursts 10, 4 and 6 ms. With Round Robin (quantum 4 ms, order P1, P2, P3) the average waiting time is:", ["8.67 ms", "7.33 ms", "10 ms", "6 ms"], 0,
     "P1 0–4, P2 4–8, P3 8–12, P1 12–16, P3 16–18, P1 18–20. Waits: P1 20 − 10 = 10, P2 4, P3 12 → 26/3 ≈ 8.67."),
    ("With 3 frames and LRU replacement, the reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 causes how many page faults?", ["8", "9", "10", "12"], 2,
     "Faults at 1, 2, 3, 4, 1, 2, 5, 3, 4, 5 (hits only at the second 1 and 2 after 5) = 10."),
    ("Internal fragmentation occurs in:", ["paging", "segmentation", "both equally", "neither"], 0, "The last page of a process may be partly empty; segmentation causes external fragmentation."),
    ("Which is NOT a requirement of a solution to the critical-section problem?", ["Mutual exclusion", "Progress", "Bounded waiting", "Pre-emption"], 3, "The three requirements are mutual exclusion, progress and bounded waiting."),
    ("A process moves from the Ready state to the Running state when it is:", ["blocked for I/O", "dispatched by the scheduler", "terminated", "swapped out"], 1, "The dispatcher gives it the CPU."),
    ("In UNIX, fork() returns to the child process the value:", ["the parent's PID", "0", "−1", "the child's PID"], 1, "The parent receives the child's PID; −1 means failure."),
    ("How many processes exist after a program calls fork() three times in a row (including the original)?", ["3", "4", "6", "8"], 3, "2³ = 8."),
    ("Disk head at cylinder 50; requests 82, 170, 43, 140. Under SSTF the total head movement is:", ["134", "144", "208", "344"], 0, "50→43 (7) →82 (39) →140 (58) →170 (30) = 134."),
    ("Spooling is mainly used for:", ["memory protection", "overlapping slow I/O (such as printing) with computation", "process synchronisation", "virtual memory"], 1,
     "Simultaneous Peripheral Operations On-Line."),
    ("The Linux command that lists the currently running processes is:", ["ls", "ps", "pwd", "cat"], 1, "top also shows them continuously."),
    ("The program that combines several object files and libraries into one executable is the:", ["loader", "linker", "assembler", "editor"], 1, "The loader then places the executable in memory."),
    ("Assertion (A): Each process has its own separate address space.\nReason (R): Threads of the same process share its code and data.", AR, 1,
     "Both true; R is about threads and does not explain A."),
]

U7 = [
    ("A Software Requirements Specification (SRS) mainly describes:", ["how the system will be coded", "what the system must do", "the test cases only", "the hardware design"], 1, "It states requirements, not design."),
    ("Function Point Analysis measures software size from:", ["lines of code", "the functionality delivered to the user", "number of programmers", "execution time"], 1, "Inputs, outputs, inquiries, files and interfaces."),
    ("Testing done after a change to make sure existing features still work is called:", ["unit testing", "regression testing", "acceptance testing", "smoke testing only"], 1, "Re-running earlier tests after modification."),
    ("The UML diagram that shows the time order of messages between objects is the:", ["class diagram", "sequence diagram", "use-case diagram", "deployment diagram"], 1, "Lifelines run downwards in time."),
    ("Arrange the phases of the waterfall model:\n1. Design\n2. Requirements analysis\n3. Testing\n4. Implementation (coding)", ["2, 1, 4, 3", "1, 2, 4, 3", "2, 4, 1, 3", "2, 1, 3, 4"], 0,
     "Requirements → design → coding → testing → maintenance."),
    ("A common measure of software reliability is:", ["lines of code", "Mean Time Between Failures (MTBF)", "cyclomatic complexity", "function points"], 1, "MTBF = MTTF + MTTR."),
    ("Consider the statements about prototyping:\n(a) It helps when requirements are unclear.\n(b) Users give feedback on an early working model.\n(c) The prototype must always become the final product.\nWhich are correct?",
     ["(a) and (b)", "(a) and (c)", "(b) and (c)", "(a), (b) and (c)"], 0, "A throw-away prototype is discarded once requirements are clear."),
    ("Match the CMM level with its name:\na. Level 1  b. Level 2  c. Level 3  d. Level 5\n1. Initial  2. Repeatable  3. Defined  4. Optimising",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "Level 4 is Managed."),
]

U8 = [
    ("The prefix form of (A + B) * C is:", ["+AB*C", "*+ABC", "AB+C*", "*AB+C"], 1, "Operator before operands: * (+AB) C."),
    ("Push 1, push 2, push 3, pop, push 4, pop, pop. The popped values in order are:", ["3, 4, 2", "3, 2, 4", "1, 2, 3", "4, 3, 2"], 0, "Stack is LIFO: pop 3; push 4; pop 4; pop 2."),
    ("The minimum number of levels of a binary tree with 15 nodes is:", ["3", "4", "5", "15"], 1, "A complete tree with 4 levels holds 2⁴ − 1 = 15 nodes."),
    ("The best-case time complexity of insertion sort is:", ["O(1)", "O(n)", "O(n log n)", "O(n²)"], 1, "On an already sorted array each element needs one comparison."),
    ("The array [10, 20, 15, 30, 40] represents a:", ["max-heap", "min-heap", "neither", "binary search tree"], 1, "Every parent is smaller than its children (10 < 20, 15; 20 < 30, 40)."),
    ("With h(k) = k mod 7, the keys 15 and 22 are hashed. What happens?", ["no collision", "a collision at slot 1", "a collision at slot 0", "a collision at slot 15"], 1, "15 mod 7 = 1 and 22 mod 7 = 1."),
    ("Kruskal's minimum-spanning-tree algorithm:", ["grows a single tree from a start vertex", "adds edges in increasing weight order, avoiding cycles", "needs negative weights", "is a dynamic-programming method"], 1,
     "It uses union–find to detect cycles; Prim's grows one tree."),
    ("In a circular queue of size n (one slot kept empty), the queue is full when:", ["front == rear", "(rear + 1) % n == front", "rear == n − 1", "front == 0"], 1, "front == rear means empty."),
    ("Accessing the k-th element of a singly linked list takes:", ["O(1)", "O(k)", "O(log k)", "O(k²)"], 1, "The list must be traversed from the head."),
    ("The Floyd–Warshall all-pairs shortest-path algorithm runs in:", ["O(n)", "O(n²)", "O(n³)", "O(n log n)"], 2, "Three nested loops over the vertices (dynamic programming)."),
    ("Assertion (A): Merge sort is a stable sorting algorithm.\nReason (R): Merge sort sorts in place using only O(1) extra space.", AR, 2,
     "Standard merge sort needs O(n) extra space for merging."),
]

U9 = [
    ("The subnet mask for a /20 network is:", ["255.255.240.0", "255.255.255.240", "255.255.224.0", "255.240.0.0"], 0, "20 ones: 255.255.11110000.0 = 255.255.240.0."),
    ("A /28 subnet has how many usable host addresses?", ["14", "16", "30", "6"], 0, "4 host bits: 2⁴ − 2 = 14."),
    ("The network address of the host 192.168.10.77/27 is:", ["192.168.10.64", "192.168.10.32", "192.168.10.77", "192.168.10.96"], 0, "Block size 32: 64 ≤ 77 < 96."),
    ("ARP is used to find:", ["the IP address from a domain name", "the MAC address for a known IP address", "the route to a network", "a free IP address"], 1, "DNS maps names to IPs."),
    ("The protocol that automatically assigns IP addresses to hosts is:", ["DNS", "DHCP", "ARP", "ICMP"], 1, "Dynamic Host Configuration Protocol."),
    ("The propagation delay over a 2000 km link with signal speed 2 × 10⁸ m/s is:", ["1 ms", "10 ms", "100 ms", "0.1 ms"], 1, "2 × 10⁶ m ÷ 2 × 10⁸ m/s = 0.01 s."),
    ("A noiseless channel of bandwidth 3000 Hz uses 2 signal levels. Its maximum bit rate (Nyquist) is:", ["3000 bps", "6000 bps", "12000 bps", "9000 bps"], 1, "2 × B × log₂L = 2 × 3000 × 1."),
    ("A channel has bandwidth 3000 Hz and signal-to-noise ratio 7. Its capacity (Shannon) is:", ["6000 bps", "9000 bps", "21000 bps", "3000 bps"], 1, "C = B log₂(1 + SNR) = 3000 × log₂8 = 9000 bps."),
    ("In a star topology, failure of the central hub/switch:", ["affects only one node", "brings down the whole network", "has no effect", "only slows the network"], 1, "Every link passes through the centre."),
    ("A switch works at the OSI:", ["physical layer", "data link layer", "transport layer", "application layer"], 1, "It forwards frames using MAC addresses (layer-3 switches also route)."),
    ("A digital signature is created using the:", ["receiver's public key", "sender's private key", "sender's public key", "shared secret key only"], 1,
     "Anyone can verify it with the sender's public key."),
    ("Assertion (A): UDP guarantees delivery of datagrams.\nReason (R): UDP has less overhead than TCP.", AR, 3, "UDP is unreliable and connectionless; its low overhead is true."),
]

U10 = [
    ("Breadth-first search is optimal when:", ["all step costs are equal", "the heuristic is admissible", "the graph has cycles", "the depth is infinite"], 0, "It finds the shallowest goal first."),
    ("Alpha–beta pruning is used to speed up:", ["A* search", "minimax search in games", "hill climbing", "genetic algorithms"], 1, "It skips branches that cannot change the minimax decision."),
    ("Supervised learning requires:", ["labelled training data", "no data", "only rewards", "unlabelled data only"], 0, "Unsupervised learning works on unlabelled data; reinforcement learning uses rewards."),
    ("In fuzzy logic, a truth value can be:", ["only 0 or 1", "any value from 0 to 1", "only −1, 0 or 1", "any integer"], 1, "Degrees of membership (Zadeh, 1965)."),
    ("The two main parts of an expert system are the:", ["compiler and loader", "knowledge base and inference engine", "CPU and memory", "sensor and actuator"], 1, "Example: MYCIN for diagnosis."),
]

SECTIONS = [("Unit 1 – Fundamentals", U1), ("Unit 2 – Discrete Structures", U2), ("Unit 3 – Computer Architecture", U3), ("Unit 4 – Programming & Web", U4),
            ("Unit 5 – DBMS", U5), ("Unit 6 – OS & System Software", U6), ("Unit 7 – Software Engineering", U7), ("Unit 8 – Data Structures & Algorithms", U8),
            ("Unit 9 – Networks", U9), ("Unit 10 – Artificial Intelligence", U10)]
