"""Previous-year paper · Karnataka PGCET 2023 (23 Sep 2023) · M.E./M.Tech · Computer Science Engineering · version A1 · 75 Q
(Part A Q1–50 one mark each, Part B Q51–75 two marks each), 100 marks.
Source: KEA question-paper archive (p2_2023_pg_cet_m_tech_cs_2023_18062026.pdf, URL in tools/pyq_manifest.tsv; scanned,
transcribed from the page images). Options (A)–(D) as printed.
No key for this paper was found on KEA's site, so every answer was worked out by ExamSim and is NOT the official key.
Skipped as ambiguous: Q16 (Kruskal, Prim and Dijkstra are all greedy), Q31 (confidentiality and integrity are both goals),
Q37 (the weak entity is not identified), Q46 (options printed garbled), Q49 (JSP and servlets both fit)."""

SRC = "PGCET 2023 M.Tech CS · Q{}"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

Q = {

1: ('If P(A) = 6/11, P(B) = 5/11 and P(A ∪ B) = 7/11, then the value of P(B/A) is :', ['1/3', '1', '2/5', '2/3'], 3, 'P(A ∩ B) = 6/11 + 5/11 − 7/11 = 4/11; P(B/A) = 4/6 = 2/3.'),
2: ('If f(x) is a probability density function of a continuous random variable, then :', ['∫₋∞^∞ f(x) dx = 0', '∫₋∞^∞ f(x) dx = 1', '∫₋∞^∞ f(x) dx > 1', '∫₋∞^∞ f(x) dx < 0'], 1, 'Total probability is 1.'),
3: ('The standard deviation of the Binomial distribution is :', ['√npq', '√np', 'npq', 'pq'], 0, 'Variance npq.'),
4: ('The number of elements in the power set P(S) of the set S = {1, 2, 3} is :', ['4', '2', '1', '8'], 3, '2³ = 8.'),
5: ('If f(x) = ax + b where a and b are integers, f(−1) = − 5 and f(3) = 3, then the values of a and b are :', ['− 3, − 1', '0, 2', '2, − 3', '2, 3'], 2, '−a + b = −5 and 3a + b = 3 give a = 2, b = −3.'),
6: ('The value of a₂ for the recurrence relation of aₙ = 17aₙ₋₁ + 30n, with a₀ = 3 is :', ['4387', '2381', '1437', '5484'], 2, 'a₁ = 51 + 30 = 81; a₂ = 1377 + 60 = 1437.'),
7: ('Abstract Data type is :', ['User-defined', 'Pre-defined', 'Self-defined', 'Program-defined'], 0, 'An ADT is defined by the programmer.'),
8: ('To represent hierarchical relationship between elements, which data structure is suitable?', ['Dequeue', 'Priority', 'Tree', 'Graph'], 2, 'A tree models parent–child hierarchy.'),
9: ("Which of the following is the most commonly used data structure for implementing Dijkstra's Algorithm ?", ['Max priority queue', 'Stack', 'Circular queue', 'Min priority queue'], 3, 'The vertex with the smallest distance is taken next.'),
10: ("Prim's algorithm is a :", ['Divide and conquer algorithm', 'Greedy algorithm', 'Dynamic Programming', 'Approximation algorithm'], 1, 'Adds the cheapest edge each step.'),
11: ('What is the source ?', ['Vertex with no incoming edges', 'Vertex with no leaving edges', 'Centre vertex', 'Vertex with the least weight'], 0, 'A sink has no leaving edges.'),
12: ('In simple chaining, what data structure is appropriate ?', ['Singly linked list', 'Doubly linked list', 'Circular linked list', 'Binary trees'], 0, 'Each hash bucket keeps a singly linked chain.'),
13: ('What can be the value of m in the division method ?', ['Any prime number', 'Any even number', '2ᵖ − 1', '2ᵖ'], 0, 'h(k) = k mod m works best with a prime m not close to a power of 2.'),
14: ('Which is an important file used by the system and should not be altered or removed from the disk?', ['Hidden file', 'Archived file', 'System file', 'Read-only file'], 2, 'System files (marked with the S attribute in Windows) are needed for the OS to run.'),
15: ('An element at position i in an array has its left child of a binary tree stored at position', ['2i', '2i + 1', 'i/2', 'i²'], 0, '1-based sequential representation.'),
17: ('How many min terms are formed for n variables ?', ['2n', '2 + n', '2ⁿ', '2 log n'], 2, 'Each variable is true or false.'),
18: ('Which of the following is an optimal gate level implementation of digital circuit?', ['Gate-level minimization', 'Door-level minimization', 'Gate-level maximization', 'Circuit-level maximization'], 0, 'Gate-level minimization finds the simplest gate realisation of a Boolean function (Mano, ch. 3).'),
19: ('____ Flip Flop is a slight modification of SR Flip Flop.', ['D', 'T', 'JK', 'IJK'], 2, 'JK removes the invalid S = R = 1 state by toggling.'),
20: ('In which addressing mode is the effective address equal to the address part of the instruction?', ['Indirect register', 'Direct', 'Register direct', 'Relative'], 1, 'Direct (absolute) addressing.'),
21: ('A control unit that utilizes a ROM to store binary control information is called', ['Microprogrammed control unit', 'Hardwired control unit', 'Arithmetic control unit', 'Input output control unit'], 0, 'The ROM is the control memory holding microinstructions.'),
22: ('For NFA with epsilon moves, which of the following is correct ?', ['δ : Q × Σ = P(Q)', 'δ : Q × (Σ ∪ Σ+) = P(Q)', 'δ : Q × (Σ+) = P(Q)', 'δ : Q × (Σ ∪ ε) = P(Q)'], 3, 'ε-NFA transitions on symbols or ε.'),
23: ("The maximum number of states present in DFA that is constructed from NFA with 'n' states is ____.", ['2*n', '2+n', '2.n!', '2ⁿ'], 3, 'Subset construction.'),
24: ('The turing machine that always halts irrespective of acceptance of languages is called ____.', ['Multi-tape', 'Halting TM', 'Non-Halting TM', 'Empty TM'], 1, 'A decider (halting TM) accepts the recursive languages.'),
25: ('____ governs the computer operations.', ['Application software', 'System software', 'User', 'Utility software'], 1, 'e.g. the operating system.'),
26: ('Which of the following is not a system software ?', ['Loader', 'Linker', 'Assembler', 'DBMS'], 3, 'A DBMS is application software.'),
27: ('The object code of the header files are linked to programs whenever required by using ____ software.', ['Loader', 'Linker', 'Assembler', 'Compiler'], 1, "The linker joins the program's object code with the library code behind the header declarations."),
28: ('Which of the following statement is true ?', ['Dynamic linking is done runtime', 'Compilation is dynamic', 'Linux supports static linking', 'Memory consumption is more in dynamic linking'], 0, 'Shared libraries are linked at load/run time.'),
29: ('The concept of ____ is that the combined size of the program, data, and stack may exceed the amount of physical memory available for it.', ['Primary memory', 'Virtual memory', 'Cache memory', 'Logical memory'], 1, 'Only the parts in use are kept in main memory.'),
30: ('The purpose of TLB (Translational Lookaside Buffer) is :', ['Speed up paging', 'Slow down paging', 'Address calculation', 'Thrashing'], 0, 'Without a TLB every reference needs two memory accesses (page table + data).'),
32: ('The situations for the occurrence of scheduling are listed\ni. When a process exits.\nii. When a new process is created.\niii. When an I/O interrupt occurs.\niv. When a clock interrupt occurs.\nWhich of the following statements are correct ?', ['i, ii, iii and iv', 'Only i and ii', 'Only i, ii and iii', 'i and ii, but not iii'], 0, 'Tanenbaum lists all four.'),
33: ('Which of the following is not a constraint in SQL ?', ['Primary key', 'Not Null', 'Check', 'Union'], 3, 'UNION is a set operator.'),
34: ('Choose the incorrect statement :', ['A relation in 2NF must also be in 1NF', 'A relation in 3NF must also be in 2NF', 'A relation in 3NF must also be in BCNF', 'A relation in BCNF must also be in 3NF'], 2, 'BCNF is stricter.'),
35: ('Customer has a savings account but it was not reflected in any other database in the bank.', ['Atomicity', 'Security', 'Data Inconsistency', 'Isolation'], 2, 'Copies disagree = inconsistency.'),
36: ('When transaction Ti requests a data item currently held by Tj, Ti is allowed to wait only if it has a timestamp smaller than that of Tj (that is, Ti is older than Tj).\nOtherwise, Ti is rolled back (dies). This is :', ['Wait-die', 'Wait-wound', 'Wound-wait', 'Wait'], 0, 'Older waits, younger dies.'),
38: ('All logs are created and stored in ____ storage when the deferred database method is used, and data is synced to the database when a transaction commits.', ['Stable', 'Unstable', 'System', 'Recovery'], 0, 'Logs go to stable storage.'),
39: ('5NF is designed to cope with :', ['transitive dependency', 'join dependency', 'multivalued dependency', 'inconsistency'], 1, '5NF = project-join normal form.'),
40: ('The facilities available in the Internet are :\ni. electronic mail\nii. remote login\niii. file transfer\niv. word processing', ['i and ii', 'i, ii and iii', 'i, ii and iv', 'ii, iii and iv'], 1, 'Word processing is a local application.'),
41: ('Which protocol does the PPP protocol provide for handling the capabilities of the connection/link on the network?', ['LCP', 'NCP', 'Both LCP and NCP', 'TCP'], 0, "PPP's Link Control Protocol sets up, tests and negotiates link options; the Network Control Protocols configure network-layer protocols."),
42: ('The IPv6 version of BGP is', ['MP-BGPv4', 'BGPv5', 'BGP IPv6', 'MP-BGPv2'], 0, 'Multiprotocol extensions to BGP-4 (RFC 4760) carry IPv6 routes.'),
43: ('The value of acknowledgement field in a segment defines :', ['sequence number of the byte received previously', 'total number of bytes to receive', 'sequence number of the next byte to be received', 'sequence of zeros and ones'], 2, 'TCP ACKs are cumulative.'),
44: ('Which among the following features is present in IPv6 but not in IPv4?', ['Fragmentation', 'Header checksum', 'Options', 'Auto configuration'], 3, 'Stateless address autoconfiguration (SLAAC); IPv6 dropped the header checksum and router fragmentation.'),
45: ('In IPv6 header, the base header can be followed by up to ______ extension headers.', ['4', '8', '6', '7'], 2, 'Forouzan: up to six extension headers – hop-by-hop, destination, routing, fragmentation, authentication, ESP.'),
47: ('What is a common technology used for communication between the presentation tier and the application tier in web-based architectures ?', ['HTML', 'CSS', 'JSON', 'SQL'], 2, 'REST APIs exchange JSON.'),
48: ('The ____ tier would be responsible for handling database queries and transactions.', ['Presentation', 'Application', 'Data', 'Database'], 2, 'Three tiers: presentation, application (logic), data.'),
50: ('Which of the following objects is used to store user-specific data that persists across multiple pages in ASP ?', ['Application', 'Session', 'Server', 'Request'], 1, 'Application is shared by all users.'),
51: ('If P and Q are two statements then (p → q) ↔ (~q → ~p) is :', ['Contradiction', 'Contingency', 'Tautology', 'Contrapositive'], 2, 'A statement is equivalent to its contrapositive.'),
52: ('If f : [2, ∞) → R is the function defined by f(x) = x² − 4x + 5, then the range of f is :', ['R', '[1, ∞)', '[4, ∞)', '[5, ∞)'], 1, 'f(x) = (x − 2)² + 1 ≥ 1 (the paper prints [2, 0)).'),
53: ('A bag contains 5 black and 6 red balls. The number of ways in which 2 black and 3 red balls can be selected is :', ['200', '100', '300', '50'], 0, '⁵C₂ × ⁶C₃ = 10 × 20.'),
54: ('Match the following :\na. Completeness\nb. Time Complexity\nc. Space Complexity\ni. How long does it take to find a solution ?\nii. How much memory is needed to perform the search ?\niii. Is the strategy guaranteed to find the solution when there is one ?', ['a-iii, b-ii, c-i', 'a-i, b-ii, c-iii', 'a-iii, b-i, c-ii', 'a-i, b-iii, c-ii'], 2, 'Search-strategy criteria (Russell & Norvig).'),
55: ('The pre-order traversal of a binary search tree is given by\n12, 8, 6, 2, 7, 9, 10, 16, 15, 19, 17, 20.\nThen the post-order traversal of this tree is :', ['2, 6, 7, 8, 9, 10, 12, 15, 16, 17, 19, 20', '2, 7, 6, 10, 9, 8, 15, 17, 20, 19, 16, 12', '7, 2, 6, 8, 9, 10, 20, 17, 19, 15, 16, 12', '7, 6, 2, 10, 9, 8, 15, 16, 17, 20, 19, 12'], 1, 'Rebuild the BST from the preorder, then list children before parents.'),
56: ('Consider a hash table of size 10. Using linear probing, find the locations of 72, 27, 36, 92 in the table.', ['2, 7, 6, 3', '3, 7, 4, 2', '3, 5, 2, 7', '4, 7, 5, 4'], 0, '92 collides at 2 and moves to 3.'),
57: ('The minimum possible depth of a binary tree with 23 nodes is :', ['3', '4', '6', '2'], 1, '⌊log₂ 23⌋ = 4 (root at depth 0).'),
58: ("Find the complement of x'yz' + x'y'z :", ["(x + y' + z) (x + y + z')", "(z' + y' + x') + (x + y + z)", 'xyz(x + y + z)', "(x + y + z) (x' + y' + z')"], 0, 'De Morgan on each term.'),
59: ('Which of the following registers holds the micro instructions when the computation of the next address is done and read from memory ?', ['Micro register', 'Pipeline register', 'Parallel register', 'Buffer'], 1, 'The control data register (pipeline register) holds the current microinstruction while the next address is computed.'),
60: ('Which memory is employed to compensate for the speed differential between main memory access time and processor logic in computer systems ?', ['Secondary', 'Primary', 'Cache', 'Auxiliary'], 2, 'Cache sits between the CPU and main memory.'),
61: ('A computer with cache access time of 100 ns, a main memory access time of 1000 ns, and a hit ratio of ____ produces an average access time of 200 ns.', ['0·9', '0·7', '0·5', '0'], 0, '200 = 100h + 1100(1 − h) (a miss costs cache + memory) → h = 0.9.'),
62: ('Match the following :\nLanguage\na. Type 0\nb. Type 1\nc. Type 2\nd. Type 3\nAutomata Machine\ni. Regular\nii. Context-Free\niii. Context-Sensitive\niv. Recursively Enumerable', ['a-iii, b-ii, c-i, d-iv', 'a-i, b-ii, c-iii, d-iv', 'a-iv, b-iii, c-ii, d-i', 'a-i, b-iii, c-ii, d-iv'], 2, 'Chomsky hierarchy.'),
63: ('The minimum number of states in DFA that accepts the binary strings that are divisible by 3 is ____.', ['1', '2', '3', '5'], 2, 'One state per remainder.'),
64: ('Which of the following statements are true ?\ni. Recursively enumerable languages are not accepted by TM.\nii. A halting problem is an undecidable problem.', ['i and ii are true', 'i is false and ii is true', 'i and ii are false', 'i is true and ii is false'], 1, 'RE languages are exactly those accepted by TMs.'),
65: ('In the context of compilers, which of the following is not an intermediate representation of the source program ?', ['Abstract syntax tree', 'Control flow graph', 'Symbol table', 'Three address code'], 2, 'The symbol table is a supporting data structure.'),
66: ('Consider L₂ is a context free language and L₁ is a regular language. Which of the following language is not context free ?', ['L₁ ∪ (L₂ ∪ L₂′)', '(L₁′ ∪ L₂′)′', 'L₁ ∩ L₂′', '(L₁ ∩ L₂) (L₁′ ∩ L₂)'], 2, 'L₂′ need not be context-free; the others reduce to Σ*, L₁ ∩ L₂ or a concatenation of CFLs.'),
67: ('Consider a computer system with a byte addressable memory of size 2³² bytes. Assume the computer system has a direct mapped cache of size 32 KB (1 KB = 2¹⁰ bytes) and each cache block is of size 64 bytes. The size of the tag field is ____ bits.', ['17', '13', '21', '45'], 0, 'Offset 6 bits (64 B), index 9 bits (512 lines), tag 32 − 15 = 17.'),
68: ('Consider, for example, a system with 64 MB of user memory, one printer, and two 64-MB processes that each want to print something. Process A requests and gets the printer, then starts to compute the values to print. Before it has finished with the computation, it exceeds its time quantum and is swapped or paged out. Process B now runs and tries, unsuccessfully, to acquire the printer. This situation leads to :', ['Deadlock', 'No Deadlock', 'Partial Deadlock', 'Semi-Deadlock'], 0, "Tanenbaum's example: A holds the printer, B holds the memory."),
69: ('Which of the following are not process items ?', ['Address space', 'Global variables', 'Child processes', 'Registers'], 3, 'Registers are per-thread items (Tanenbaum).'),
70: ('Identify the incorrect statement regarding the page replacement algorithms and its principle.', ['NRU (Not Recently Used) - Removes a page at random from the lowest numbered nonempty class', 'FIFO -First In, First Out', 'LRU -Throw out the page that has been used for the longest time', 'Second chance - Simple modification of FIFO'], 2, 'LRU throws out the page that has NOT been used for the longest time.'),
71: ('Which of the following is a true statement about cursors in SQL ?', ['Cursors are used to execute a single SQL statement at a time.', 'Cursors are used to retrieve a subset of rows from a table based on a specific condition.', 'Cursors are used to update multiple rows in a table at once.', 'Cursors are used to perform calculations on the data stored in a table.'], 1, "A cursor walks through a query's result set row by row."),
72: ('Which of the following set of dependencies is suitable for making a relation R(ABCD) to be in 3NF but not in BCNF ?', ['{AB->CD, A->C, D->B}', '{AB->CD, C->DA}', '{A->BCD, C->A, D->B}', '{AB->CD, C->A, D->B}'], 3, 'Keys AB, AD, BC, CD: every attribute is prime, so 3NF, but C → A has a non-superkey left side.'),
73: ('Which of the following is a true statement about serializability in database system ?', ['Serializability is a property that ensures the correctness of concurrent transactions.', 'Serializable schedules always result in a deadlock situation.', 'Conflict serializability ensures that transactions can be executed in parallel without any conflict.', 'A schedule is serializable if and only if it is a conflict serializable schedule.'], 0, 'View-serializable schedules need not be conflict-serializable.'),
74: ('In a connection, the value of cwnd is 4000 and the value of rwnd is 5000. The host has sent 1,000 bytes, which have not been acknowledged. How many more bytes can be sent ?', ['4000', '1000', '2000', '3000'], 3, 'min(4000, 5000) − 1000.'),
75: ('The port number ____ and ____ is used for data and control connection.', ['21, 20', '20, 21', '20, 12', '12, 21'], 1, 'FTP data 20, control 21.'),
}


def sets():
    out = []
    for lo in (1, 26, 51):
        qs = [(q, o, a, e + NOTE, SRC.format(n)) for n in sorted(Q) if lo <= n <= lo + 24 for q, o, a, e in [Q[n]]]
        out.append({"name": f"Q{lo}–{lo + 24}", "questions": qs, "keep_order": True})
    return out


TOPIC = "PGCET 2023 – M.Tech Computer Science"
