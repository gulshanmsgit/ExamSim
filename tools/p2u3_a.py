"""Paper 2 · Unit 3 · P2-U3-01 Digital Logic – Combinational and P2-U3-02 Digital Logic – Sequential (2 topics × 2 sub-topics × 30),
with revision NOTES.
References: M. Morris Mano, Digital Design (5th ed.) and Computer System Architecture (3rd ed., chs. 1–2); Floyd, Digital Fundamentals.
Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final
keys for GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1; options read from the page images where the OCR lost exponents).
KSET 2023–25 and KEA 2026 CS Paper-2 questions come from packs/pyq-p2.json; KSET/KEA/PGCET answers were worked out by ExamSim. Skipped
as garbled (complement bars lost in OCR): PGCET 2023 MCA Q11, PGCET 2024 MCA Q87, PGCET 2026 CS Q13, Q23, PGCET 2026 MCA Q18, GFGC 2021
Q13; Raichur 2024 Q11 (shift direction not stated). Every K-map, adder, counter and memory-size answer was checked by hand."""
from packlib import AR, I_II
from p2u7_a import kset, PYQ, GTTC, NOTE

GATES_KMAP = [
    kset("KSET 2023 CS&A · Q91"),
    kset("KSET 2024 CS&A · Q4"),
    kset("KSET 2025 CS&A · Q8"),
    kset("KEA 2026 CS Paper-2 · Q23"),
    kset("KEA 2026 CS Paper-2 · Q24"),
    ("Which of the following is an optimal gate level implementation of digital circuit?",
     ["Gate-level minimization", "Door-level minimization", "Gate-level maximization", "Circuit-level maximization"], 0,
     "Gate-level minimization finds the simplest gate realisation of a Boolean function (Mano, ch. 3)." + NOTE, "PGCET 2023 M.Tech CS · Q18"),
    ("The minimum number of 2-input NAND gates required to implement a 2-input XOR gate is",
     ["4", "5", "6", "7"], 0, "Classic 4-NAND XOR: X = (AB)', then output = ((A·X)' · (B·X)')'. With NOR gates it needs 5." + NOTE, "PGCET 2024 M.Tech CS · Q37"),
    ("If x and y are Boolean variables, then which of the following statement is/are incorrect?\na. x∨0 = x, x∧1 = x   b. x∨x' = 1, x∧x' = 0   c. x∧(x∨y) = x   d. x∧(x∧y) = x∨y",
     ["a, b and c", "a only", "c only", "d only"], 3, "x∧(x∧y) = x∧y, not x∨y; a – identity, b – complement, c – absorption laws are correct." + NOTE, "PGCET 2024 MCA · Q86"),
    ("In Boolean algebra, if a∧x = b∧x and a∧x' = b∧x', then which of the following statements is correct?",
     ["a > b", "a < b", "a = b²", "a = b"], 3, "a = a∧(x∨x') = (a∧x)∨(a∧x') = (b∧x)∨(b∧x') = b." + NOTE, "PGCET 2024 MCA · Q89"),
    ("In Boolean algebra [B, ∧, ∨, ', 0, 1] the value of x'∧(x∨y) is",
     ["x∧y", "x'∧y", "x'∧y'", "x∧x'"], 1, "Distribute: (x'∧x)∨(x'∧y) = 0∨(x'∧y) = x'∧y." + NOTE, "PGCET 2024 MCA · Q90"),
    ("In Boolean algebra, which of the following is correct?",
     ["x∧y = x'∨y", "x∨y = x'∧y", "x∧(x∨y) = x", "x∨1 = x"], 2, "Absorption law; x∨1 = 1." + NOTE, "PGCET 2025 MCA · Q14"),
    ("In Boolean algebra, simplified form of (x∧y)∨x'∨y' is",
     ["1", "0", "y", "x"], 0, "x'∨y' = (x∧y)' by De Morgan, so the expression is P∨P' = 1." + NOTE, "PGCET 2025 MCA · Q15"),
    ("Given the following statements:\nS1: NAND and NOR are universal gates\nS2: AND, OR, NOT are basic gates\nWhich of the following is the correct answer?",
     ["S1: true and S2: true", "S1: false and S2: false", "S1: false and S2: true", "S1: true and S2: false"], 0,
     "Any Boolean function can be built from NAND alone or NOR alone." + NOTE, "PGCET 2025 MCA · Q27"),
    ("The Boolean expressions (AB)' = A' + B' and (A + B)' = A'B' represent",
     ["Absorption law", "Distributive law", "De Morgan's law", "Idempotent law"], 2, "De Morgan's theorems." + NOTE, "PGCET 2026 MCA · Q19"),
    ("A digital computer works with signals that have:",
     ["Two discrete levels representing 0 and 1", "Continuously varying levels", "Ten voltage levels", "Only analog values"], 0, PYQ + "Binary digits (bits)."),
    ("The output of an XOR gate is 1 when:",
     ["The inputs are different", "Both inputs are 1", "Both inputs are 0", "Any input is 1"], 0, PYQ + "A ⊕ B = A'B + AB'; XNOR is 1 when inputs are equal (equality detector)."),
    ("Using Boolean algebra, A + A'B simplifies to:",
     ["A + B", "AB", "A", "B"], 0, PYQ + "A + A'B = (A + A')(A + B) = A + B."),
    ("Using the absorption law, A + AB simplifies to:",
     ["A", "B", "AB", "A + B"], 0, "A(1 + B) = A."),
    ("The dual of the Boolean identity A + 0 = A is:",
     ["A · 1 = A", "A · 0 = 0", "A + 1 = 1", "A' + 0 = A'"], 0, PYQ + "Swap + and ·, and 0 and 1."),
    ("How many different Boolean functions of two variables are possible?",
     ["16", "4", "8", "2"], 0, "2^(2^n) = 2^4 = 16 for n = 2."),
    ("In a K-map, cells are arranged in Gray-code order (00, 01, 11, 10) so that:",
     ["Adjacent cells differ in only one variable", "Cells are in numerical order", "Minterms are grouped by parity", "Maxterms come first"], 0,
     PYQ + "This lets adjacent 1s be combined."),
    ("In a 4-variable K-map, a group of 8 adjacent 1s (an octet) eliminates how many variables?",
     ["3", "1", "2", "4"], 0, "Pair – 1 variable, quad – 2, octet – 3."),
    ("Simplify F(A, B, C) = Σm(1, 3, 5, 7).",
     ["C", "A", "B'", "AC"], 0, PYQ + "All minterms with C = 1 → F = C."),
    ("Simplify F(A, B, C, D) = Σm(0, 2, 8, 10).",
     ["B'D'", "A'B'", "BD", "C'D'"], 0, "The four corner cells form a quad: B = 0 and D = 0."),
    ("'Don't-care' conditions in a K-map are used to:",
     ["Form larger groups when convenient, giving a simpler expression", "Always be treated as 1", "Always be treated as 0", "Increase the number of gates"], 0,
     PYQ + "Marked X or d."),
    ("F(A, B) = Σm(1, 2) is equivalent to:",
     ["A ⊕ B", "A ⊙ B (XNOR)", "A + B", "AB"], 0, "m1 = A'B, m2 = AB'."),
    ("A prime implicant that covers at least one minterm not covered by any other prime implicant is called:",
     ["An essential prime implicant", "A redundant implicant", "A don't-care", "A maxterm"], 0, PYQ + "It must appear in the minimal SOP."),
    ("To make a NOT gate from a 2-input NAND gate, you:",
     ["Join both inputs together", "Ground one input", "Connect the output to an input", "It is impossible"], 0, "(A·A)' = A'."),
    ("Consider the statements:\nI. A canonical SOP expression uses minterms.\nII. A canonical POS expression uses minterms.\nWhich is/are correct?",
     I_II, 0, "Only I. POS uses maxterms."),
    ("Assertion (A): NAND is called a universal gate.\nReason (R): AND, OR and NOT can all be built using only NAND gates.",
     AR, 0, "R explains A."),
]

COMB_CIRCUITS = [
    kset("KEA 2026 CS Paper-2 · Q28"),
    ("Decoder is a logic circuit with n inputs and how many outputs?",
     ["n²", "2ⁿ", "1", "n² + 1"], 1, "An n-to-2ⁿ line decoder activates one output for each input combination." + GTTC, "GTTC 2024 Lecturer CS · Q40"),
    ("Number of output in a half adder is",
     ["1", "2", "3", "4"], 1, "Sum and Carry." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q71"),
    ("The characteristics of the combinational circuits are:\na. Output at any time is function of inputs at that time.\nb. Contains memory elements.\nc. Do not have feedback path.\n"
     "d. Clock is used to trigger the circuit to obtain the outputs.",
     ["Only a and b", "Only a and c", "Only b and c", "Only b and d"], 1, "Memory, feedback and clocks belong to sequential circuits." + NOTE, "PGCET 2024 M.Tech CS · Q24"),
    ("A 4 to 1 multiplexer has four data inputs I0, I1, I2, I3, two select lines S1 and S0, and one output y. If S1S0 = 10, which input is connected to the output?",
     ["I0", "I1", "I2", "I3"], 2, "Select value 10₂ = 2 → I2." + NOTE, "PGCET 2026 CS · Q21"),
    ("For a half adder with inputs A and B, the outputs are:",
     ["Sum = A ⊕ B, Carry = AB", "Sum = AB, Carry = A ⊕ B", "Sum = A + B, Carry = AB", "Sum = A ⊙ B, Carry = A + B"], 0, PYQ + "A half adder cannot add an incoming carry."),
    ("For a full adder with inputs A, B and Cin, the sum and carry-out are:",
     ["S = A ⊕ B ⊕ Cin; Cout = AB + Cin(A ⊕ B)", "S = AB + Cin; Cout = A ⊕ B", "S = A + B + Cin; Cout = ABCin", "S = A ⊕ B; Cout = A + B"], 0,
     "Cout can also be written AB + BCin + ACin (majority function)."),
    ("A full adder can be built from:",
     ["Two half adders and one OR gate", "Two half adders only", "One half adder and one AND gate", "Three XOR gates only"], 0, PYQ + "The two half-adder carries are ORed."),
    ("In an n-bit ripple-carry adder, the delay grows:",
     ["Linearly with n, because each stage waits for the previous carry", "Logarithmically", "Not at all", "Exponentially"], 0, "A carry look-ahead adder computes carries in parallel to reduce delay."),
    ("For a half subtractor computing A − B, the borrow output is:",
     ["A'B", "AB'", "AB", "A + B"], 0, PYQ + "Difference = A ⊕ B."),
    ("A 3-to-8 line decoder has:",
     ["3 inputs and 8 outputs, exactly one output active at a time", "8 inputs and 3 outputs", "3 inputs and 3 outputs", "1 input and 8 outputs"], 0, "Each output is one minterm."),
    ("Any 3-variable Boolean function can be implemented with:",
     ["A 3-to-8 decoder and an OR gate collecting the required minterms", "A single AND gate", "A half adder", "A 2-to-1 multiplexer only"], 0, PYQ + "Mano: decoder + OR = sum of minterms."),
    ("An 8-to-3 encoder (octal to binary) has:",
     ["8 inputs and 3 outputs", "3 inputs and 8 outputs", "8 inputs and 8 outputs", "1 input and 3 outputs"], 0, "Reverse of a decoder."),
    ("A priority encoder:",
     ["Gives the code of the highest-priority active input when several inputs are 1", "Activates all outputs", "Works only with one input", "Is a sequential circuit"], 0,
     PYQ + "It also has a 'valid' output for when no input is active."),
    ("How many select lines are needed for an 8-to-1 multiplexer?",
     ["3", "8", "2", "4"], 0, "2ⁿ inputs need n select lines."),
    ("A multiplexer is also called a:",
     ["Data selector", "Data distributor", "Code converter", "Comparator"], 0, PYQ + "A demultiplexer is a data distributor."),
    ("How many 4-to-1 multiplexers are needed to build a 16-to-1 multiplexer?",
     ["5", "4", "8", "16"], 0, "Four in the first level + one to select among them."),
    ("How many 2-to-1 multiplexers are needed to build an 8-to-1 multiplexer?",
     ["7", "8", "4", "3"], 0, PYQ + "4 + 2 + 1 = 7."),
    ("A 1-to-8 demultiplexer needs how many select lines?",
     ["3", "8", "1", "2"], 0, "A decoder with an enable input can work as a demultiplexer."),
    ("For a 1-bit magnitude comparator, the output 'A > B' is:",
     ["AB'", "A'B", "A ⊙ B", "AB"], 0, PYQ + "A = B is A ⊙ B (XNOR); A < B is A'B."),
    ("Convert binary 1011 to Gray code.",
     ["1110", "1101", "1011", "0111"], 0, "g3 = 1; g2 = 1⊕0 = 1; g1 = 0⊕1 = 1; g0 = 1⊕1 = 0."),
    ("Which gate is used to build parity generators and checkers?",
     ["XOR", "AND", "NAND", "NOR"], 0, PYQ + "XOR of all bits gives even-parity bit."),
    ("Adding 0111 and 0101 with a 4-bit binary adder gives:",
     ["1100", "1010", "1110", "0100"], 0, "7 + 5 = 12 = 1100."),
    ("In a BCD adder, when the 4-bit sum exceeds 9 (or a carry occurs), the correction is to add:",
     ["0110 (6)", "0011 (3)", "1001 (9)", "1010 (10)"], 0, PYQ + "This skips the six invalid codes 1010–1111."),
    ("A BCD-to-seven-segment decoder is used to:",
     ["Display decimal digits on a 7-segment display", "Add BCD numbers", "Store BCD data", "Convert analog to digital"], 0, "Each digit lights a pattern of segments a–g."),
    ("Short unwanted pulses at a combinational output caused by unequal path delays are called:",
     ["Hazards (glitches)", "Races", "Latches", "Fan-out errors"], 0, PYQ + "A static-1 hazard can be removed by adding a redundant (consensus) term."),
    ("Which circuit compares two binary numbers and outputs A > B, A = B and A < B?",
     ["Magnitude comparator", "Multiplexer", "Encoder", "Counter"], 0, "IC 7485 is a 4-bit comparator."),
    ("A 4-to-1 multiplexer can implement any 3-variable function by:",
     ["Using two variables as select lines and feeding 0, 1, the third variable or its complement to the data inputs", "Using all three variables as select lines",
      "Adding an OR gate only", "It cannot"], 0, PYQ + "Mano: implementing Boolean functions with multiplexers."),
    ("Consider the statements:\nI. A decoder has more outputs than inputs.\nII. An encoder has more outputs than inputs.\nWhich is/are correct?",
     I_II, 0, "Only I."),
    ("Assertion (A): A ripple-carry adder is slow for wide words.\nReason (R): Each full adder must wait for the carry from the previous stage.",
     AR, 0, "R explains A."),
]

FLIPFLOPS = [
    kset("KEA 2026 CS Paper-2 · Q27"),
    ("What will be the frequency of the output from a JK flip-flop when J = 1, K = 1 and a clock with pulse waveform is given?",
     ["Half the frequency of clock input", "Equal to the frequency of clock input", "Twice the frequency of clock input", "Independent of the frequency of clock input"], 0,
     "With J = K = 1 the output toggles on every active clock edge, so its period is two clock periods." + GTTC, "GTTC 2024 Lecturer CS · Q39"),
    ("Along with synchronous control inputs what to use to transfer a change in the flip-flop?",
     ["0", "1", "clock", "present output"], 2, "Synchronous inputs (J, K, D, T) act only at the clock edge." + GTTC, "GTTC 2024 Lecturer CS · Q41"),
    ("The functional difference between SR flipflop and JK flipflop is",
     ["JK flipflop is faster than SR flipflop", "JK flipflop is slower than SR flipflop", "JK flipflop accepts both inputs 1", "JK flipflop does not require external clock"], 2,
     "For J = K = 1 the JK toggles; S = R = 1 is not allowed in an SR flip-flop." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q73"),
    ("Race around condition is an undesirable phenomenon in Flip-Flops. The remedy for the same is",
     ["S-R", "D-Flip flop", "J-K Flip flop", "Master slave JK Flipflop"], 3,
     "Master–slave (or edge-triggered) design lets the output change only once per clock pulse." + NOTE, "PGCET 2024 M.Tech CS · Q80"),
    ("A sequential circuit differs from a combinational circuit because its output depends on:",
     ["Present inputs and the past history (stored state)", "Present inputs only", "Clock frequency only", "Power supply only"], 0, PYQ + "It contains memory elements – flip-flops."),
    ("The difference between a latch and a flip-flop is that:",
     ["A latch is level-sensitive; a flip-flop changes only at a clock edge", "A latch is edge-triggered; a flip-flop is level-sensitive", "A latch has no memory", "A flip-flop stores two bits"], 0,
     "Edge triggering avoids multiple changes during one clock pulse."),
    ("In an SR latch built with NOR gates, the input combination that is not allowed is:",
     ["S = 1, R = 1", "S = 0, R = 0", "S = 1, R = 0", "S = 0, R = 1"], 0, PYQ + "Both outputs would be forced to 0 and the next state is unpredictable."),
    ("In an SR latch built with NAND gates (active-low inputs), the forbidden input is:",
     ["S' = 0, R' = 0", "S' = 1, R' = 1", "S' = 1, R' = 0", "S' = 0, R' = 1"], 0, "NAND latch inputs are active low."),
    ("The next state of a D flip-flop is:",
     ["Q(t+1) = D", "Q(t+1) = D'", "Q(t+1) = Q'", "Q(t+1) = D ⊕ Q"], 0, PYQ + "Used as a delay element and in registers."),
    ("The characteristic equation of a JK flip-flop is:",
     ["Q(t+1) = JQ' + K'Q", "Q(t+1) = J + K'Q", "Q(t+1) = J ⊕ K", "Q(t+1) = JK + Q"], 0, "JK = 00 hold, 01 reset, 10 set, 11 toggle."),
    ("In a JK flip-flop, J = 0 and K = 1 at the clock edge gives:",
     ["Q = 0 (reset)", "Q = 1 (set)", "Toggle", "No change"], 0, PYQ + "JK = 01 resets the flip-flop; 10 sets it."),
    ("The characteristic equation of a T flip-flop is:",
     ["Q(t+1) = T ⊕ Q", "Q(t+1) = T", "Q(t+1) = TQ", "Q(t+1) = T + Q"], 0, "T = 1 toggles; T = 0 holds."),
    ("A T flip-flop can be made from a JK flip-flop by:",
     ["Connecting J and K together as the T input", "Grounding K", "Connecting J to Q", "Inverting the clock"], 0, PYQ + "Then JK is 00 (hold) or 11 (toggle)."),
    ("A D flip-flop can be made from a JK flip-flop by connecting:",
     ["J = D and K = D'", "J = K = D", "J = D' and K = D", "J = 1 and K = D"], 0, "Then JK is never 11 and Q follows D."),
    ("The race-around condition in a level-triggered JK flip-flop occurs when:",
     ["J = K = 1 and the clock pulse is longer than the flip-flop's propagation delay", "J = K = 0", "J = 1, K = 0", "The clock is very short"], 0,
     PYQ + "The output keeps toggling during the pulse."),
    ("In the excitation table of a JK flip-flop, the transition Q: 0 → 1 requires:",
     ["J = 1, K = X (don't care)", "J = 0, K = 1", "J = X, K = 0", "J = 1, K = 1 only"], 0, "Excitation tables are used to design counters."),
    ("In the excitation table of an SR flip-flop, the transition Q: 1 → 0 requires:",
     ["S = 0, R = 1", "S = 1, R = 0", "S = X, R = 0", "S = 1, R = 1"], 0, PYQ + "Reset the flip-flop: S = 0, R = 1."),
    ("Preset and clear inputs of a flip-flop are:",
     ["Asynchronous – they act immediately, independent of the clock", "Synchronous with the clock", "Used only in combinational circuits", "Data inputs"], 0, "Used to initialise the flip-flop."),
    ("The minimum time the data input must be stable BEFORE the clock edge is the:",
     ["Setup time", "Hold time", "Propagation delay", "Clock period"], 0, PYQ + "Hold time – stable time AFTER the edge."),
    ("In a Mealy machine, the output depends on:",
     ["The present state and the present inputs", "The present state only", "The inputs only", "The clock only"], 0, "Moore machine – output depends on the present state only."),
    ("How many flip-flops are needed for a state machine with 10 states?",
     ["4", "10", "3", "5"], 0, PYQ + "⌈log₂ 10⌉ = 4."),
    ("The characteristic equation of an SR flip-flop (with the condition SR = 0) is:",
     ["Q(t+1) = S + R'Q", "Q(t+1) = S'R + Q", "Q(t+1) = SR + Q'", "Q(t+1) = S ⊕ R"], 0, "S sets, R resets, otherwise Q holds; S = R = 1 is excluded."),
    ("A flip-flop is also known as a:",
     ["Bistable multivibrator", "Monostable multivibrator", "Astable multivibrator", "Schmitt trigger"], 0, PYQ + "It has two stable states."),
    ("Three T flip-flops with T = 1 are connected in cascade (each output clocks the next). If the clock is 8 kHz, the output of the last flip-flop is:",
     ["1 kHz", "4 kHz", "2 kHz", "8 kHz"], 0, "Each stage divides by 2: 8 → 4 → 2 → 1 kHz."),
    ("A sequential circuit whose state changes only at clock edges is called:",
     ["Synchronous", "Asynchronous", "Combinational", "Analog"], 0, PYQ + "Asynchronous circuits change whenever inputs change."),
    ("A flip-flop stores:",
     ["One bit", "One byte", "Four bits", "One word"], 0, "n flip-flops store n bits."),
    ("Consider the statements:\nI. A D flip-flop has no invalid input combination.\nII. A T flip-flop holds its state when T = 1.\nWhich is/are correct?",
     I_II, 0, "Only I. T = 1 toggles."),
    ("Consider the statements:\nI. In a Moore machine the output depends only on the present state.\nII. Master–slave JK flip-flops remove the race-around condition.\nWhich is/are correct?",
     I_II, 2, "Both."),
    ("Assertion (A): A JK flip-flop with J = K = 1 can be used as a frequency divider.\nReason (R): It toggles on every active clock edge.",
     AR, 0, "Output frequency = clock/2; R explains A."),
]

REG_COUNTER_MEM = [
    ("Which of the following are correct statements about counters?\n(a) Counters are sequential circuits\n(b) Counters can be synchronous or asynchronous\n"
     "(c) Counters is an example for combinational circuits\n(d) Counters can count pulses",
     ["(a), (b), (c) and (d)", "(a), (b) and (d)", "(b), (c) and (d)", "(a) and (c)"], 1, "Counters are built from flip-flops, so they are sequential, not combinational." + NOTE,
     "PGCET 2026 CS · Q14"),
    ("The popular TTL IC 7490 is a:",
     ["Decade (mod-10) ripple counter", "4-bit shift register", "3-to-8 decoder", "Full adder"], 0, PYQ + "7493 – 4-bit binary counter; 74138 – 3-to-8 decoder; 7483 – 4-bit adder."),
    ("A register is:",
     ["A group of flip-flops that stores a binary word", "A single logic gate", "A type of decoder", "An analog device"], 0, PYQ + "An n-bit register has n flip-flops."),
    ("The four types of shift registers by data movement are:",
     ["SISO, SIPO, PISO and PIPO", "SR, JK, D and T", "Up, down, ring and Johnson", "SSI, MSI, LSI and VLSI"], 0, "S = serial, P = parallel, I = in, O = out."),
    ("Which shift register converts serial data to parallel data?",
     ["SIPO", "PISO", "SISO", "PIPO"], 0, PYQ + "PISO converts parallel to serial (e.g. for transmission)."),
    ("Shifting a binary number one place to the left (with 0 entering) is equivalent to:",
     ["Multiplying by 2", "Dividing by 2", "Adding 1", "Complementing"], 0, "Right shift divides by 2 (for unsigned numbers)."),
    ("How many clock pulses are needed to load 4 bits serially into an empty 4-bit SISO shift register?",
     ["4", "1", "8", "2"], 0, PYQ + "One bit enters per clock."),
    ("A universal shift register (e.g. IC 74194) can:",
     ["Shift left, shift right, load in parallel and hold", "Only shift right", "Only count", "Only decode"], 0, "Mode-select inputs S1 S0 choose hold, shift right, shift left or parallel load."),
    ("A ring counter with n flip-flops has how many states?",
     ["n", "2n", "2ⁿ", "n − 1"], 0, PYQ + "A single 1 circulates."),
    ("A 4-bit Johnson (twisted-ring) counter has how many states?",
     ["8", "4", "16", "15"], 0, "2n states; the complement of the last output is fed back to the first."),
    ("In an asynchronous (ripple) counter:",
     ["Each flip-flop is clocked by the output of the previous one", "All flip-flops share the same clock", "No flip-flops are used", "Outputs change simultaneously"], 0,
     PYQ + "Delays add up along the chain."),
    ("A 4-bit ripple counter uses flip-flops with 10 ns propagation delay each. The maximum safe clock frequency is about:",
     ["25 MHz", "100 MHz", "10 MHz", "40 MHz"], 0, "Total delay 4 × 10 = 40 ns → f = 1/40 ns = 25 MHz."),
    ("In a synchronous counter:",
     ["All flip-flops are triggered by the same clock at the same time", "Each flip-flop clocks the next", "There is no clock", "Only one flip-flop is used"], 0,
     PYQ + "Faster than ripple counters; uses gates to decide which flip-flops toggle."),
    ("How many flip-flops are needed for a mod-10 (decade) counter?",
     ["4", "10", "3", "5"], 0, "⌈log₂ 10⌉ = 4."),
    ("The maximum count of a 4-bit binary counter is:",
     ["15", "16", "4", "8"], 0, PYQ + "It counts 0 to 15 (mod 16)."),
    ("A decade (BCD) counter counts from 0 to 9 and then resets on reaching:",
     ["1010", "1001", "1111", "1000"], 0, "The 1010 state is detected and used to clear the flip-flops."),
    ("To make a mod-6 counter from a 3-bit binary ripple counter, the counter is reset when it reaches:",
     ["110", "101", "111", "011"], 0, PYQ + "States 000–101 remain."),
    ("A mod-16 counter driven by a 1.6 MHz clock gives an output frequency of:",
     ["100 kHz", "1.6 MHz", "16 MHz", "160 kHz"], 0, "Counters divide frequency by their modulus."),
    ("Which level of integration has the highest number of gates per chip?",
     ["VLSI", "LSI", "MSI", "SSI"], 0, PYQ + "SSI < MSI < LSI < VLSI (ULSI beyond)."),
    ("Which logic family is known for very low power consumption?",
     ["CMOS", "ECL", "TTL", "RTL"], 0, "ECL is the fastest (non-saturating) but power hungry."),
    ("The number of gate inputs that one gate output can drive reliably is called:",
     ["Fan-out", "Fan-in", "Noise margin", "Propagation delay"], 0, PYQ + "Fan-in = number of inputs of a gate."),
    ("A memory unit with k address lines and n data lines stores:",
     ["2ᵏ words of n bits each", "k words of n bits", "n words of 2ᵏ bits", "k × n words"], 0, "Mano, memory unit."),
    ("How many address lines are needed for a 1K × 8 memory?",
     ["10", "8", "1024", "13"], 0, PYQ + "1K = 1024 = 2¹⁰."),
    ("A 64K × 16 memory has:",
     ["16 address lines, 16 data lines and a capacity of 128 KB", "64 address lines and 16 data lines", "16 address lines and 64 data lines", "20 address lines and 8 data lines"], 0,
     "64K = 2¹⁶ words × 2 bytes = 128 KB."),
    ("How many 256 × 4 RAM chips are needed to build a 1K × 8 memory?",
     ["8", "4", "2", "16"], 0, PYQ + "(1024/256) × (8/4) = 4 × 2 = 8."),
    ("Static RAM differs from dynamic RAM because SRAM:",
     ["Stores bits in flip-flops and needs no refreshing", "Stores bits in capacitors and needs refreshing", "Is non-volatile", "Is slower and cheaper"], 0,
     "DRAM uses capacitors, is denser and cheaper, and must be refreshed."),
    ("Which ROM can be erased with ultraviolet light and reprogrammed?",
     ["EPROM", "Mask ROM", "PROM", "EEPROM"], 0, PYQ + "EEPROM and Flash are erased electrically."),
    ("A PLA differs from a PAL because in a PLA:",
     ["Both the AND array and the OR array are programmable", "Only the OR array is programmable", "Neither array is programmable", "There is no AND array"], 0,
     "PAL: programmable AND array, fixed OR array."),
    ("Consider the statements:\nI. A Johnson counter with n flip-flops has 2n states.\nII. A ripple counter is faster than a synchronous counter.\nWhich is/are correct?",
     I_II, 0, "Only I."),
    ("Assertion (A): A Johnson counter gives twice as many states as a ring counter with the same flip-flops.\nReason (R): The Johnson counter feeds back the complement of the last flip-flop's output.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Digital Logic – Combinational": [
        ("1 · Digital Computers, Logic Gates, Boolean Algebra and K-map Simplification", GATES_KMAP),
        ("2 · Combinational Circuits – Adders, Subtractors, Decoders, Encoders and Multiplexers", COMB_CIRCUITS),
    ],
    "Digital Logic – Sequential": [
        ("1 · Latches, Flip-Flops (SR, D, JK, T) and Sequential Circuits", FLIPFLOPS),
        ("2 · Registers, Counters, Integrated Circuits and the Memory Unit", REG_COUNTER_MEM),
    ],
}

NOTES = {
    "Digital Logic – Combinational": [
        {"title": "Combinational logic – revision sheet", "md": """## Gates and Boolean algebra
- Basic: AND, OR, NOT; **universal: NAND, NOR**; XOR = A'B + AB' (1 when different); XNOR = equality
- NAND-only XOR needs **4** gates (NOR-only 5); NOT from NAND – join inputs
- Laws: identity (x+0=x, x·1=x), complement, idempotent, **absorption** (x + xy = x, x(x+y) = x), x + x'y = x + y, **De Morgan** ((AB)' = A' + B', (A+B)' = A'B'), duality
- Number of functions of n variables = 2^(2ⁿ)

## K-maps
- Gray order 00 01 11 10; pair eliminates 1 variable, quad 2, octet 3; corners and edges are adjacent
- Σm(1,3,5,7) = C; Σm(0,2,8,10) = B'D'; Σm(0,2,4,6) = C'
- Don't-cares (X) help make larger groups; essential prime implicants; canonical SOP (minterms) / POS (maxterms)
- Variable-entered map: 4 variables with 2 map-entered → 4 cells

## Combinational circuits (no memory, no feedback, no clock)
| Circuit | Key facts |
|---|---|
| Half adder | S = A⊕B, C = AB (2 outputs) |
| Full adder | S = A⊕B⊕Cin, Cout = AB + Cin(A⊕B); = 2 HA + OR |
| Half subtractor | D = A⊕B, Borrow = A'B |
| Ripple adder | delay ∝ n; carry look-ahead is faster |
| BCD adder | add 0110 if sum > 9 |
| Decoder | n → 2ⁿ, one minterm per output; decoder + OR = any function |
| Encoder | 2ⁿ → n; priority encoder |
| MUX | 2ⁿ:1 with n select lines (data selector); 16:1 = 5 × 4:1; 8:1 = 7 × 2:1 |
| DEMUX | 1:2ⁿ (data distributor) |
| Comparator | A>B = AB', A=B = A⊙B, A<B = A'B |
- Binary→Gray: g = b ⊕ (b >> 1) (1011 → 1110); parity – XOR; hazards – add consensus term
"""}],
    "Digital Logic – Sequential": [
        {"title": "Sequential logic – revision sheet", "md": """## Latches and flip-flops
- Sequential = output depends on inputs + stored state; latch (level) vs flip-flop (edge); bistable multivibrator
- **SR**: NOR latch – S=R=1 invalid; NAND latch – S'=R'=0 invalid; Q+ = S + R'Q (SR = 0)
- **D**: Q+ = D (no invalid state; delay; registers)
- **JK**: Q+ = JQ' + K'Q; 00 hold, 01 reset, 10 set, 11 toggle; race-around when J=K=1 with a long pulse → **master–slave** / edge triggering
- **T**: Q+ = T ⊕ Q; JK→T: J = K = T; JK→D: J = D, K = D'
- J=K=1 → output = clock/2 (frequency divider)
- Excitation: JK 0→1 = (1, X); SR 1→0 = (0, 1); D = Q+
- Preset/clear asynchronous; setup time (before edge), hold time (after edge)
- Mealy (state + input) vs Moore (state only); flip-flops for N states = ⌈log₂ N⌉

## Registers and counters
- Shift registers SISO, SIPO (serial→parallel), PISO, PIPO; left shift ×2; universal 74194
- Ring counter n states; **Johnson 2n** states
- Ripple (asynchronous) – delays add (4 × 10 ns → 25 MHz max); synchronous – common clock
- n-bit counter: 0 … 2ⁿ−1; decade counter resets at 1010; mod-6 resets at 110; mod-N divides frequency by N

## ICs and memory
- SSI < MSI < LSI < VLSI; CMOS low power, ECL fastest, TTL common; fan-in/fan-out, noise margin
- Memory with k address and n data lines = 2ᵏ × n; 1K × 8 → 10 address lines; 64K × 16 → 16 lines, 128 KB
- Chips needed = (total words / chip words) × (total width / chip width)
- SRAM (flip-flops, no refresh) vs DRAM (capacitors, refresh); ROM, PROM, EPROM (UV), EEPROM, Flash
- PLA (AND + OR programmable) vs PAL (AND programmable, OR fixed)
"""}],
}
