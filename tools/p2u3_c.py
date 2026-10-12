"""Paper 2 · Unit 3 · P2-U3-05 Basic Computer Organization and Design and P2-U3-06 Programming the Basic Computer (2 topics × 2 sets × 30),
with revision NOTES.
References: M. Morris Mano, Computer System Architecture (3rd ed., chs. 4, 5, 6 and 7); Hamacher, Computer Organization (control sequences).
Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final
keys for Legislative Council Secretariat 2024 (Computer Operator P2, Junior Console Operator P2 – booklet A1). KSET 2023–25 questions
come from packs/pyq-p2.json; GFGC 2021 and PGCET answers were worked out by ExamSim (options read from the page images). The parsed
Legislative Council Data Entry Operator P2 key does not match the booklet, so its answer is marked as worked out by ExamSim. Basic-computer
instruction codes and program traces were checked by hand."""
from p2u7_a import kset, PYQ, KLC, NOTE

ORGANIZATION = [
    kset("KSET 2023 CS&A · Q93"),
    kset("KSET 2023 CS&A · Q94"),
    kset("KSET 2025 CS&A · Q12"),
    ("Match the following in relation to addressing registers.\nList-1\n(a) Memory Address (MAR)\n(b) Memory Buffer (MBR)\n(c) Program Counter (PC)\n"
     "(d) Input/Output (I/O)\nList-2\ni) Holds the address of next instruction\nii) Holds the address of active memory location\n"
     "iii) Communicates with I/O devices\niv) Holds the information on its own to and from memory",
     ["a – iv, b – i, c – iii, d – ii", "a – ii, b – iv, c – i, d – iii", "a – ii, b – i, c – iii, d – iv", "a – iv, b – iii, c – ii, d – i"], 1,
     "MAR – address of the memory word being accessed; MBR – data going to or coming from memory; PC – next instruction; I/O register – device." + KLC,
     "Legislative Council 2024 Computer Operator P2 · Q4"),
    ("Match the following with respect to connections between processor and memory.\nList – I (Registers)\n(a) IR\n(b) MAR\n(c) MDR\n(d) PC\n"
     "List – II (Usage)\n(i) Keeps track of execution of a program\n(ii) Holds the instruction that is currently being executed\n"
     "(iii) Data to be written into or read out of the addressed location\n(iv) Holds the address of the location to be accessed",
     ["a – iii, b – iv, c – ii, d – i", "a – i, b – ii, c – iv, d – iii", "a – ii, b – iv, c – iii, d – i", "a – iv, b – ii, c – i, d – iii"], 2,
     "IR – current instruction; MAR – address; MDR – data; PC – program sequence." + NOTE, "PGCET 2026 MCA · Q34"),
    ("Which register is used as a working area in CPU ?", ["Program counter", "Stalk pointer", "Accumulator", "Instruction register"], 2,
     "Arithmetic and logic results are kept in the accumulator." + NOTE, "GFGC 2021 CS · Q14"),
    ("CPU Registers are used for\na) Storing data\nb) Storing instructions\nc) Storing intermediate results",
     ["Only a is correct", "Only b is correct", "Both a and c are correct", "a, b and c are correct"], 3,
     "Registers hold data (DR, AC), instructions (IR) and intermediate results (AC, TR)." + NOTE, "Legislative Council 2024 Data Entry Operator P2 · Q91"),
    ("Which of the following best defines a bus in a computer system?",
     ["A path for transferring data and instructions between components", "A memory unit", "An input/output device", "A register used for arithmetic operations"], 0,
     "A bus is a set of common lines (data, address, control)." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q34"),
    ("Which of the following is not an application of logic operations ?",
     ["Insert new bit values into a register.", "Change bit values.", "Delete a group of bits.", "Shift bit values in a register."], 3,
     "Selective set/clear/complement, mask (delete) and insert are logic microoperations; shifting is a separate shift microoperation (Mano, ch. 4)." + NOTE,
     "GFGC 2021 CS · Q17"),
    ("The stored-program concept means that", ["Instructions and data are both kept in memory and the CPU fetches the instructions from there",
                                               "The program is wired into the control unit", "Data are kept only in registers",
                                               "Each program runs on a separate processor"], 0, PYQ + "Von Neumann's idea; the PC holds the address of the next instruction."),
    ("The operation code (opcode) of an instruction", ["Specifies the operation to be performed", "Gives the address of the operand", "Holds the result",
                                                       "Is the value of the program counter"], 0, "The rest of the instruction gives the operand or its address."),
    ("An instruction of Mano's basic computer (16 bits) consists of", ["1 mode bit, a 3-bit opcode and a 12-bit address", "A 4-bit opcode and a 12-bit address with no mode bit",
                                                                       "An 8-bit opcode and an 8-bit address", "1 mode bit, a 4-bit opcode and an 11-bit address"], 0,
     PYQ + "I (bit 15) chooses direct or indirect addressing."),
    ("Mano's basic computer has a 4096 × 16 memory; its address register AR therefore has", ["12 bits", "16 bits", "10 bits", "8 bits"], 0, "2¹² = 4096; PC is also 12 bits."),
    ("When the mode bit I = 1 in a memory-reference instruction, the address field gives",
     ["An indirect address – the word there holds the effective address", "An immediate operand", "A direct address of the operand", "A register number"], 0,
     "One extra memory read is needed."),
    ("The address of the operand actually used by an instruction is called the", ["Effective address", "Base address", "Return address", "Relative address"], 0,
     "For a direct instruction it equals the address field."),
    ("In Mano's basic computer, the registers that have 12 bits are", ["AR and PC", "DR and AC", "IR and TR", "INPR and OUTR"], 0,
     "DR, AC, IR and TR are 16 bits; INPR and OUTR are 8 bits."),
    ("In the basic computer, INPR and OUTR each hold", ["8 bits (one character)", "16 bits", "12 bits", "4 bits"], 0, "They exchange characters with the terminal."),
    ("The register of the basic computer that holds temporary data during processing is", ["TR", "DR", "AR", "IR"], 0, "TR is used, for example, in the interrupt cycle."),
    ("The 16-bit common bus of the basic computer is driven by one of its seven sources, chosen by", ["Three select inputs S₂S₁S₀", "Two select inputs",
                                                                                                     "Sixteen select inputs", "The program counter"], 0,
     PYQ + "Memory and six registers; the selected source's output is placed on the bus."),
    ("The three instruction code formats of the basic computer are", ["Memory-reference, register-reference and input-output", "Arithmetic, logic and shift",
                                                                      "Load, store and branch", "Immediate, direct and indirect"], 0,
     "Opcode 000–110 = memory reference; 111 with I = 0 = register reference; 111 with I = 1 = I/O."),
    ("A register-reference instruction of the basic computer is recognised by", ["Opcode 111 and I = 0 (hex 7xxx)", "Opcode 111 and I = 1 (hex Fxxx)",
                                                                                  "Opcode 000", "I = 1 with any opcode"], 0, "The low 12 bits choose the operation (e.g. 7800 = CLA)."),
    ("The instruction with hexadecimal code F800 (INP) belongs to the", ["Input-output instructions", "Memory-reference instructions",
                                                                         "Register-reference instructions", "Indirect memory-reference instructions"], 0,
     "Fxxx = opcode 111 with I = 1."),
    ("How many instructions does Mano's basic computer have?", ["25", "16", "32", "7"], 0, "7 memory-reference + 12 register-reference + 6 input-output."),
    ("An instruction set is complete if it has instructions for", ["Arithmetic, logic and shift; moving data; program control and status checks; and input-output",
                                                                    "Arithmetic operations alone", "Data transfer and branching alone", "Floating-point and string operations"], 0,
     "Mano, ch. 5 (instruction set completeness)."),
    ("The register-transfer statement R2 ← R1 means", ["Copy the contents of R1 into R2", "Copy R2 into R1", "Swap R1 and R2", "Add R1 to R2"], 0,
     "R1 is unchanged."),
    ("In P: R2 ← R1, the control function P means", ["The transfer happens only when P = 1", "P is the destination register", "P is added to R2", "P clears R1"], 0,
     "P is a Boolean control condition."),
    ("To clear selected bits of register A (selective clear / masking), the logic microoperation used is", ["AND with a mask that has 0s in those positions",
                                                                                                             "OR with 1s", "XOR with 1s", "Complement"], 0,
     PYQ + "Selective set = OR; selective complement = XOR."),
    ("The logic microoperation used to set selected bits of a register to 1 is", ["OR", "AND", "XOR", "NOR"], 0, "A ← A ∨ B with 1s in B where bits must be set."),
    ("In a circular shift (rotate), the bit shifted out", ["Re-enters at the other end", "Is lost", "Goes only to the overflow flag", "Is replaced by 0"], 0,
     "A logical shift inserts 0; an arithmetic shift-right copies the sign."),
    ("In the basic computer, arithmetic and logic results are stored in", ["The accumulator (AC)", "The program counter", "The address register", "The instruction register"], 0,
     "The adder and logic circuit take AC and DR as inputs."),
]

CYCLE_CONTROL = [
    kset("KSET 2025 CS&A · Q14"),
    kset("KSET 2023 CS&A · Q96"),
    ("A control unit that utilizes a ROM to store binary control information is called", ["Microprogrammed control unit", "Hardwired control unit",
                                                                                          "Arithmetic control unit", "Input output control unit"], 0,
     "The ROM is the control memory holding microinstructions." + NOTE, "PGCET 2023 M.Tech CS · Q21"),
    ("Which of the following registers holds the micro instructions when the computation of the next address is done and read from memory ?",
     ["Micro register", "Pipeline register", "Parallel register", "Buffer"], 1,
     "The control data register (pipeline register) holds the current microinstruction while the next address is computed." + NOTE, "PGCET 2023 M.Tech CS · Q59"),
    ("The control unit of a computer is designed to go through an instruction cycle that is divided into following phases.\n(a) Fetch the instruction from memory\n"
     "(b) Decode the instruction\n(c) Execute the instruction",
     ["Only (b) and (c) are correct", "Only (c) is correct", "Only (a) is correct", "(a), (b) and (c) are correct"], 3, "Fetch → decode → execute, repeated." + NOTE,
     "PGCET 2026 MCA · Q42"),
    ("An instruction cycle refers to", ["Fetching an instruction", "Executing an instruction", "Fetching, decoding and Executing an instruction",
                                        "Reading and Executing an instruction"], 2, "All the phases together form one instruction cycle." + NOTE, "GFGC 2021 CS · Q15"),
    ("Which of the following describes a CPU's clock speed?", ["The number of cores in the CPU", "The rate at which the CPU can execute instructions",
                                                               "The size of the CPU cache memory", "The thermal design power of the CPU"], 1,
     "Clock speed (Hz) sets the pace of the timing signals." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q70"),
    ("Arrange the following control sequence for execution of instruction: ADD (R₃), R₁\n(a) R₃out, MARin, Read\n(b) Zout, R₁in, End\n(c) Zout, PCin, Yin, WMFC\n"
     "(d) MDRout, IRin\n(e) MDRout, Select Y, add, Zin\n(f) PCout, MARin, Read, Select 4, add, Zin\n(g) R₁out, Yin, WMFC",
     ["(a), (b), (c), (d), (e), (f), (g)", "(f), (c), (d), (a), (g), (e), (b)", "(g), (f), (e), (d), (a), (b), (c)", "(c), (a), (b), (g), (e), (d), (f)"], 1,
     "Fetch: PC to MAR and PC + 4 (f), update PC (c), load IR (d); execute: operand address R₃ (a), R₁ to Y (g), add (e), result to R₁ (b)." + NOTE,
     "PGCET 2026 CS · Q19"),
    ("In the basic computer, the timing signals T0–T15 are produced by", ["A 4-bit sequence counter and a 4 × 16 decoder", "A 4-flip-flop ring counter only",
                                                                          "The program counter", "The interrupt flip-flop"], 0,
     PYQ + "SC is cleared to 0 at the end of each instruction."),
    ("In a hardwired control unit, the control signals are generated by", ["Logic gates, flip-flops and decoders", "A control memory", "The ALU", "Software"], 0,
     "Fast, but hard to change."),
    ("Compared with hardwired control, microprogrammed control", ["Is easier to modify or extend, though usually slower", "Is always faster",
                                                                   "Needs no memory", "Is used only in RISC processors"], 0,
     "Changing the microprogram changes the control behaviour."),
    ("In microprogrammed control, the address of the next microinstruction is held in", ["The control address register (CAR)", "The program counter",
                                                                                          "The memory address register", "The accumulator"], 0,
     "The sequencer computes it; CDR holds the microinstruction read."),
    ("The first step (T0) of the fetch phase of the basic computer is", ["AR ← PC", "IR ← M[AR]", "PC ← PC + 1", "AR ← IR(0–11)"], 0, "Then the instruction is read at T1."),
    ("During T1 of the fetch phase, the basic computer performs", ["IR ← M[AR], PC ← PC + 1", "AR ← PC", "Decode IR(12–14)", "AC ← AC + DR"], 0,
     PYQ + "Fetch: T0 AR ← PC; T1 IR ← M[AR], PC ← PC + 1."),
    ("At T2 the basic computer", ["Decodes the opcode, loads AR with IR(0–11) and copies IR(15) to I", "Stores AC in memory", "Increments PC",
                                  "Checks the interrupt flags"], 0, "D0–D7 come from a 3 × 8 decoder on IR(12–14)."),
    ("For an indirect memory-reference instruction, the extra micro-operation at T3 is", ["AR ← M[AR]", "AR ← PC", "PC ← AR", "DR ← AC"], 0,
     "AR then holds the effective address."),
    ("The phases of an instruction cycle of the basic computer are", ["Fetch, decode, read the effective address if indirect, and execute",
                                                                      "Fetch and execute only", "Decode, store and fetch", "Interrupt, fetch and halt"], 0,
     "After execution the cycle repeats (or the interrupt cycle runs)."),
    ("The memory-reference instruction BSA (branch and save return address) performs", ["M[AR] ← PC, then PC ← AR + 1", "PC ← AR", "AC ← M[AR]", "M[AR] ← AC"], 0,
     PYQ + "Used to call subroutines."),
    ("ISZ increments the word at the effective address and", ["Skips the next instruction if the result is zero", "Branches unconditionally",
                                                              "Clears the accumulator", "Stores the return address"], 0, "Used as a loop counter."),
    ("BUN transfers control by", ["PC ← AR", "AR ← PC", "M[AR] ← PC", "PC ← PC + 1"], 0, "Branch unconditionally."),
    ("LDA in the basic computer is executed as", ["DR ← M[AR], then AC ← DR", "AC ← AR", "M[AR] ← AC", "AC ← AC + M[AR]"], 0,
     "The adder path goes through DR."),
    ("STA in the basic computer performs", ["M[AR] ← AC", "AC ← M[AR]", "AR ← AC", "PC ← AC"], 0, "Store accumulator."),
    ("Which of these is NOT a memory-reference instruction of the basic computer?", ["CLA", "ISZ", "BSA", "LDA"], 0,
     "CLA (7800) is register-reference; the seven MRIs are AND, ADD, LDA, STA, BUN, BSA, ISZ."),
    ("In the basic computer, the input flag FGI becomes 1 when", ["A new character is ready in INPR", "The output register is empty",
                                                                  "An interrupt is acknowledged", "The program halts"], 0, "INP clears FGI after transferring the character to AC."),
    ("The instructions ION and IOF", ["Set and clear the interrupt-enable flip-flop IEN", "Read and write a character", "Skip on the input or output flag",
                                      "Switch the computer on and off"], 0, "Interrupts are accepted only when IEN = 1."),
    ("The interrupt cycle of the basic computer", ["Saves the return address in memory location 0 and branches to location 1",
                                                   "Pushes PC on a stack and jumps to location 0", "Saves AC in location 1", "Clears PC and halts"], 0,
     PYQ + "RT0: AR ← 0, TR ← PC; RT1: M[AR] ← TR, PC ← 0; RT2: PC ← PC + 1, IEN ← 0, R ← 0, SC ← 0."),
    ("The interrupt flip-flop R of the basic computer is set to 1 when", ["IEN = 1 and FGI or FGO = 1, outside the fetch steps T0–T2", "IEN = 0",
                                                                          "FGI = 0 and FGO = 0", "The program counter overflows"], 0,
     "The current instruction finishes first; the interrupt cycle replaces the next fetch."),
    ("During the interrupt cycle IEN is cleared so that", ["No further interrupt is accepted until the service routine enables interrupts again",
                                                           "The flags are reset", "PC is incremented twice", "Input is disabled permanently"], 0,
     "The service routine ends with ION and BUN 0 I."),
    ("The I/O instruction SKI", ["Skips the next instruction if the input flag FGI is 1", "Skips if AC is zero", "Skips if FGO is 0", "Inputs a character"], 0,
     "SKO does the same for FGO."),
    ("Which of these is a register-reference instruction of the basic computer?", ["CMA (complement AC)", "ADD", "BSA", "INP"], 0,
     "CMA = 7200; ADD and BSA are memory-reference, INP is input-output."),
]

ASSEMBLY = [
    kset("KSET 2023 CS&A · Q95"),
    ("The address symbol table built in pass 1 of Mano's assembler stores", ["Each label with its binary address", "Each opcode with its mnemonic",
                                                                            "The object code of the program", "The comments of the program"], 0,
     "Pass 2 looks up the labels there."),
    ("The program that places object code in memory and prepares it for execution is the", ["Loader", "Assembler", "Editor", "Compiler"], 0,
     "A linker first combines separately assembled modules."),
    kset("KSET 2023 CS&A · Q21"),
    ("The pass numbers for each of the following activities :\n[ASSEMBLER PASSES]\n1. Object code generation\n2. Literals added to literal table\n"
     "3. Listing printed\n4. Address resolution of local symbols", ["1, 2, 1, 2", "2, 1, 2, 1", "2, 1, 1, 2", "1, 2, 2, 2"], 1,
     "Pass 1 builds the tables (literals, symbol addresses); pass 2 generates object code and prints the listing." + NOTE, "GFGC 2021 CS · Q53"),
    ("Match the following in relation to languages and codes.\nList-1\n(a) C\n(b) Java\n(c) Pneumonic code\n(d) Binary code\nList-2\ni) Assembly language\n"
     "ii) Procedure-oriented language\niii) Machine language\niv) Object-oriented language",
     ["a – iv, b – i, c – iii, d – ii", "a – ii, b – iv, c – iii, d – i", "a – iv, b – iii, c – ii, d – i", "a – ii, b – iv, c – i, d – iii"], 3,
     "C – procedural; Java – object-oriented; mnemonic code – assembly; binary – machine language." + KLC, "Legislative Council 2024 Computer Operator P2 · Q44"),
    ("Primary classification of programming languages are\n(a) Machine language\n(b) Assembly language\n(c) High level language\n(d) Pseudocode and Algorithms",
     ["Only (c) and (d) are correct", "Only (a) and (b) are correct", "Only (a), (b) and (c) are correct", "Only (a) and (d) are correct"], 2,
     "Pseudocode and algorithms are design aids, not programming languages." + NOTE, "PGCET 2026 MCA · Q33"),
    ("A program written as binary codes that the hardware executes directly is in", ["Machine language", "Assembly language", "A high-level language", "Pseudocode"], 0,
     "Often written in octal or hexadecimal for convenience."),
    ("Assembly language uses", ["Symbolic names (mnemonics) for operations and labels for addresses", "English sentences", "Binary digits alone", "Flowchart symbols"], 0,
     "An assembler translates it into machine code."),
    ("Each line of Mano's assembly language has the fields", ["Label, instruction and comment", "Opcode, operand and result", "Label, address and data",
                                                              "Header, body and trailer"], 0, PYQ + "The label field may be empty; a comment starts with '/'."),
    ("In Mano's assembly language, ORG N", ["Tells the assembler that the next instruction or data word goes at location N", "Branches to location N",
                                            "Defines the decimal constant N", "Ends the program"], 0, "A pseudo-instruction."),
    ("The pseudo-instruction END", ["Marks the end of the symbolic program", "Halts the computer", "Returns from a subroutine", "Ends a loop"], 0,
     "HLT is the machine instruction that stops execution."),
    ("The pseudo-instruction DEC N", ["Stores the signed decimal number N, converted to binary, at that location", "Decrements N", "Declares a variable named N",
                                      "Skips N locations"], 0, "HEX N stores a hexadecimal constant."),
    ("A pseudo-instruction is", ["A directive to the assembler, not a machine instruction", "An instruction that runs in a special mode", "A comment", "A macro call"], 0,
     PYQ + "ORG, END, DEC and HEX in Mano's assembler."),
    ("During pass 1, the assembler keeps track of instruction addresses with the", ["Location counter (LC)", "Program counter", "Stack pointer", "Instruction register"], 0,
     "LC is set by ORG and incremented after each line."),
    ("In a two-pass assembler, the first pass mainly", ["Assigns addresses to labels and builds the symbol table", "Generates object code", "Loads the program",
                                                        "Prints the listing only"], 0, "Pass 2 translates using the table."),
    ("In pass 2, Mano's assembler translates instructions using", ["The pseudo-instruction, MRI and non-MRI tables plus the address symbol table",
                                                                   "The source program only", "The loader", "The linker"], 0, "Symbolic addresses are replaced by binary addresses."),
    ("An assembler commonly needs two passes because", ["A label may be used before it is defined (forward reference)", "It must check spelling twice",
                                                        "It executes the program in pass 2", "It optimises loops"], 0, "Pass 1 finds every label's address first."),
    ("A one-pass assembler handles forward references by", ["Back-patching – filling in the addresses when the labels are defined", "Ignoring them",
                                                             "Interpreting the program", "Using macros"], 0, "It keeps a list of places to fix."),
    ("The output of an assembler is", ["Object (machine) code", "Source code", "A flowchart", "Assembly code"], 0, "Then the loader places it in memory."),
    ("In Mano's basic computer, LDA 500 (direct) and LDA 500 I (indirect) assemble to", ["2500 and A500", "2500 and 3500", "1500 and 9500", "2500 and 2501"], 0,
     PYQ + "LDA opcode = 010 → 2xxx; I = 1 adds 8 to the first hex digit."),
    ("The hexadecimal code 1100 in the basic computer means", ["ADD the word at address 100 to AC", "AND with the word at 100", "LDA 100", "BUN 100"], 0,
     "Opcode 001 = ADD (AND = 0, LDA = 2, STA = 3, BUN = 4, BSA = 5, ISZ = 6)."),
    ("The register-reference instruction CLA has the code", ["7800", "F800", "7400", "0800"], 0, "7400 = CLE, F800 = INP."),
    ("A program that assembles code on one computer for a different processor is a", ["Cross-assembler", "Interpreter", "Loader", "Debugger"], 0,
     "Used for embedded systems."),
    ("A macro differs from a subroutine because a macro", ["Is expanded in-line wherever it is used, at assembly time", "Is called with BSA at run time",
                                                           "Must be written in machine code", "Cannot have parameters"], 0, "Faster, but the program grows."),
    ("Assembly language programs are", ["Machine-dependent – each processor family has its own", "Portable across all processors", "Interpreted line by line",
                                        "Independent of the instruction set"], 0, PYQ + "High-level languages are machine-independent."),
    ("Each assembly-language instruction usually translates into", ["One machine instruction", "Many machine instructions", "No machine instruction",
                                                                     "One high-level statement"], 0, "A one-to-one translation (except pseudo-instructions and macros)."),
    ("Basic-computer instructions are commonly written as four hexadecimal digits because each instruction is", ["16 bits long", "12 bits long", "8 bits long", "32 bits long"], 0,
     "4 bits per hex digit."),
    ("Which language level is closest to the hardware?", ["Machine language", "Assembly language", "C", "Python"], 0, "Assembly is one level above it."),
    ("An interpreter differs from a compiler because it", ["Translates and executes the program statement by statement", "Produces a complete object program first",
                                                           "Works only on assembly language", "Needs a linker"], 0, "A compiler translates the whole program before execution."),
]

LOOPS_IO = [
    ("A program loop is", ["A sequence of instructions executed many times, each time with different data", "A single instruction", "An interrupt routine",
                           "A list of constants"], 0, "Mano, ch. 6."),
    ("In Mano's loop programs, a counter is set to −N and ISZ is used because", ["ISZ increments the counter and skips the branch back when it reaches zero",
                                                                                 "ISZ decrements the counter to −N", "ISZ clears the counter", "ISZ halts the computer"], 0,
     PYQ + "The basic computer has no decrement-and-branch instruction."),
    ("To step through an array in the basic computer, a loop uses", ["A pointer word used with indirect addressing and incremented each pass", "Immediate addressing",
                                                                     "A hardware stack", "The interrupt flag"], 0, "E.g. ADD PTR I, then ISZ PTR."),
    ("The basic computer has no multiply instruction, so multiplication is programmed with", ["Repeated shifts (CIL/CIR) and additions in a loop", "A MUL instruction",
                                                                                              "Repeated division", "The I/O instructions"], 0,
     "Check each multiplier bit; add the shifted multiplicand when it is 1."),
    ("To add two 32-bit numbers on the 16-bit basic computer, the program", ["Adds the low halves first, then the high halves plus the carry left in E",
                                                                              "Adds the high halves first", "Uses one ADD", "Cannot do it"], 0, "Double-precision addition."),
    ("The basic computer has AND but no OR instruction. A OR B is programmed as", ["(A' AND B')', using CMA and AND", "A + B", "A XOR B", "A shift and an add"], 0,
     PYQ + "De Morgan's law."),
    ("To do a logical shift-right of AC in the basic computer", ["Clear E with CLE, then CIR", "Use CIL twice", "Use CMA then INC", "Use SPA"], 0,
     "CIR circulates AC and E together; E must hold 0."),
    ("In Mano's basic computer, a subroutine is called with", ["BSA, which stores the return address in the first word of the subroutine", "BUN", "ISZ", "ION"], 0,
     "Execution continues at the second word."),
    ("A basic-computer subroutine returns to the caller with", ["An indirect branch through its first word (BUN SUB I)", "HLT", "Another BSA", "ION"], 0,
     PYQ + "The first word holds the return address."),
    ("Parameters can be passed to a basic-computer subroutine by", ["Placing them in AC or in the words just after the BSA call", "A hardware stack",
                                                                    "Registers R0–R7", "INPR"], 0, "The subroutine reads them through its return-address word."),
    ("In most processors, a CALL instruction", ["Pushes the return address on the stack and jumps to the subroutine", "Pops the stack", "Clears the PC",
                                                "Disables interrupts"], 0, "RET pops it back into PC."),
    ("A basic-computer subroutine called with BSA cannot call itself recursively because", ["Its single stored return address would be overwritten",
                                                                                              "BSA is too slow", "Recursion needs floating point",
                                                                                              "Indirect addressing is not allowed"], 0, "Recursion needs a stack."),
    ("A character-input routine of the basic computer", ["Waits with SKI and BUN until FGI = 1, then uses INP", "Uses INP immediately without checking",
                                                         "Uses OUT followed by SKO", "Uses IOF, then INP"], 0, PYQ + "Programmed (polled) input."),
    ("Before OUT, a program tests FGO with SKO because", ["OUTR may still hold the previous character until FGO = 1", "FGO clears AC", "SKO loads OUTR",
                                                          "OUT is a memory-reference instruction"], 0, "FGO = 1 means the printer is ready."),
    ("The drawback of programmed (polled) I/O is that", ["The CPU wastes time waiting in a loop for the device flag", "It needs DMA", "It cannot transfer characters",
                                                         "It needs a two-pass assembler"], 0, "Interrupts or DMA avoid this."),
    ("Packing two 8-bit characters into one 16-bit word of the basic computer needs", ["Shifting the first character left 8 times (CIL) and adding the second",
                                                                                       "One ADD", "Multiplying by 2", "An OR instruction"], 0, "Mano, ch. 6 (character manipulation)."),
    ("An interrupt service routine must", ["Save AC and E (the processor registers) before using them and restore them before returning", "Save only PC",
                                           "Save nothing", "Save all of memory"], 0, PYQ + "The return address is already in location 0."),
    ("The basic computer returns from an interrupt service routine with", ["ION, then BUN 0 I (indirect through location 0)", "HLT", "BSA 0", "IOF"], 0,
     "Interrupts are enabled again just before the return."),
    ("A loop that uses a counter set to −100 and ISZ executes its body", ["100 times", "99 times", "101 times", "Forever"], 0, "ISZ reaches 0 on the 100th increment."),
    ("SZA in a loop is used to", ["Skip the next instruction if AC is zero", "Set AC to zero", "Skip if E is zero", "Store AC"], 0, "SZE tests E."),
    ("To branch when AC is negative, a basic-computer program uses", ["SPA followed by BUN", "SNA followed by HLT", "SZE", "CME"], 0,
     "SPA skips the next instruction when AC is positive (sign bit 0), so the BUN after it is taken only when AC is negative."),
    ("The basic computer computes A − B by", ["Loading B, CMA, INC (2's complement), then ADD A", "Using SUB", "Using AND", "Using CIR"], 0,
     PYQ + "There is no subtract instruction."),
    ("A FOR loop of a high-level language becomes, in assembly,", ["A counter, a compare/skip test and a branch back", "A single instruction",
                                                                  "A subroutine call", "An interrupt"], 0, "The compiler generates the loop structure."),
    ("In Mano's assembly, a subroutine's return address is kept in", ["The first word of the subroutine (its label)", "Memory location 0", "The last word",
                                                                      "The top of a stack"], 0, "Location 0 is used by the interrupt cycle."),
    ("Which basic-computer instructions change the normal sequence of execution?", ["BUN, BSA and ISZ", "LDA, STA and ADD", "AND, ADD and LDA", "CMA, CLA and INC"], 0,
     "Register-reference skip instructions (SPA, SNA, SZA, SZE) and SKI/SKO can also skip one instruction."),
    ("Nested loops in assembly language need", ["A separate counter (or register) for each loop", "One counter for all loops", "No counters", "An interrupt"], 0,
     "The inner counter is re-initialised on each outer pass."),
    ("After this basic-computer program runs, C holds:\nLDA A\nADD B\nSTA C\nHLT\nA, DEC 83\nB, DEC −23\nC, DEC 0", ["60", "106", "−60", "83"], 0,
     PYQ + "AC = 83 + (−23) = 60, stored in C."),
    ("The I/O instructions of the basic computer are recognised by", ["Opcode 111 with I = 1; the low 12 bits choose INP, OUT, SKI, SKO, ION or IOF",
                                                                      "Opcode 000", "I = 0", "An address field of 0"], 0, "Hex codes F800, F400, F200, F100, F080, F040."),
    ("The main benefit of subroutines is that", ["The same code can be used from many places, saving memory", "They always run faster than in-line code",
                                                 "They need no return", "They use no memory"], 0, "The cost is the call/return overhead."),
    ("Compared with polling, interrupt-driven I/O", ["Lets the CPU do other work until the device raises its flag", "Is always faster than DMA",
                                                     "Needs no service routine", "Removes the need for flags"], 0, "The device interrupts when it is ready."),
]

TOPICS = {
    "Basic Computer Organization and Design": [
        ("1 · Stored Program Organization, Instruction Codes, Computer Registers, Common Bus and Instructions", ORGANIZATION),
        ("2 · Timing and Control, Instruction Cycle, Memory-Reference Instructions, Input-Output and Interrupt", CYCLE_CONTROL),
    ],
    "Programming the Basic Computer": [
        ("1 · Machine Language, Assembly Language and the Assembler", ASSEMBLY),
        ("2 · Program Loops, Subroutines and Input-Output Programming", LOOPS_IO),
    ],
}

NOTES = {
    "Basic Computer Organization and Design": [{"title": "Mano's basic computer – revision sheet", "md": """## Organization
- Stored program (von Neumann): instructions + data in one memory; PC holds the next instruction's address
- Memory 4096 × 16; instruction = **I (1) | opcode (3) | address (12)**; I = 1 → indirect (one extra read)
- Effective address = address actually used for the operand

| Register | Bits | Use |
|---|---|---|
| DR | 16 | data register |
| AR | 12 | address register (MAR) |
| AC | 16 | accumulator (working area) |
| IR | 16 | instruction register |
| PC | 12 | program counter |
| TR | 16 | temporary register |
| INPR / OUTR | 8 | input / output character |
- Common bus: 16 lines, 7 sources chosen by S₂S₁S₀
- Microoperations: R2 ← R1; P: R2 ← R1 (only when P = 1); selective set = OR, selective clear/mask = AND, selective complement = XOR; shifts: logical, circular, arithmetic

## Instructions (25)
- Memory-reference (opcode 000–110; hex 0–6 direct, 8–E indirect): AND 0, ADD 1, LDA 2, STA 3, BUN 4, BSA 5, ISZ 6
- Register-reference (7xxx): CLA 7800, CLE 7400, CMA 7200, CME 7100, CIR 7080, CIL 7040, INC 7020, SPA 7010, SNA 7008, SZA 7004, SZE 7002, HLT 7001
- I/O (Fxxx): INP F800, OUT F400, SKI F200, SKO F100, ION F080, IOF F040
- Complete instruction set: arithmetic/logic/shift, data transfer, program control/status, I/O

## Timing, instruction cycle, interrupt
- SC (4-bit) + 4 × 16 decoder → T0…T15; 3 × 8 decoder on IR(12–14) → D0…D7
- Fetch: T0 AR ← PC; T1 IR ← M[AR], PC ← PC + 1; T2 decode, AR ← IR(0–11), I ← IR(15); T3 AR ← M[AR] if indirect
- LDA: DR ← M[AR], AC ← DR; STA: M[AR] ← AC; BUN: PC ← AR; **BSA: M[AR] ← PC, PC ← AR + 1**; ISZ: increment, skip if 0
- Flags FGI (input ready), FGO (output ready), IEN (ION/IOF), R (interrupt cycle)
- R ← 1 when IEN·(FGI + FGO) outside T0–T2; interrupt cycle: return address → location 0, PC ← 1, IEN ← 0
- Hardwired control (gates, fast) vs microprogrammed (control memory/ROM, CAR, CDR = pipeline register, easy to change)
"""}],
    "Programming the Basic Computer": [{"title": "Programming the basic computer – revision sheet", "md": """## Languages and the assembler
- Machine language (binary/hex) → assembly (mnemonics, labels; machine-dependent; one line ≈ one instruction) → high-level
- Mano's line: **label, instruction, comment (/)**; pseudo-instructions ORG N, END, DEC N, HEX N (directives, not machine code)
- Two-pass assembler: **pass 1** – location counter, address symbol table (labels, literals); **pass 2** – object code using pseudo, MRI, non-MRI and symbol tables, listing
- Two passes are needed for forward references; one-pass assemblers back-patch
- Codes: LDA 500 = 2500, LDA 500 I = A500; ADD = 1xxx; CLA = 7800
- Macro = expanded in-line at assembly time; subroutine = called at run time; cross-assembler = for another processor

## Loops and arithmetic
- Counter = −N, ISZ skips the branch back when it reaches 0; pointer + indirect addressing for arrays
- Subtract: CMA, INC, ADD; OR via De Morgan (CMA, AND, CMA); logical shift: CLE then CIR/CIL
- Multiply by shift-and-add; double precision: low halves, then high halves + E

## Subroutines and I/O
- Call: BSA SUB (return address in SUB's first word); return: BUN SUB I; parameters in AC or after the call; no recursion
- Input: SKI / BUN back / INP; output: SKO / BUN back / OUT (programmed I/O = busy waiting)
- Interrupt service routine: save AC and E, service the device, restore, ION, BUN 0 I
- Pack two characters: CIL × 8 then ADD
"""}],
}
