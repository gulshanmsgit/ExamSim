"""Paper 2 · Unit 3 · P2-U3-07 Central Processing Unit and P2-U3-08 Input-Output Organization (2 topics × 2 sets × 30), with revision NOTES.
References: M. Morris Mano, Computer System Architecture (3rd ed., chs. 8, 9 and 11); Hamacher, Computer Organization; Intel 8085 manual.
Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final key
for Legislative Council Secretariat 2024 Junior Console Operator P2 (A1). KSET 2023–25 and KEA 2026 questions come from packs/pyq-p2.json;
GFGC 2021 and PGCET answers were worked out by ExamSim (options read from the page images). KSET 2024 Q14/Q15, KSET 2025 Q18 and KEA 2026 Q49
(I/O) are already used in Unit 6 (p2u6_h), so they are not repeated here. Effective-address, RPN, pipeline and baud-rate answers were
checked by hand."""
from p2u7_a import kset, PYQ, KLC, NOTE

REG_STACK_FORMATS = [
    ("Which of the following types of processors, typically use specialized architecture?\n(a) GPUs (Graphics Processing Units)\n(b) DSPs (Digital Signal Processors)\n"
     "(c) FPGAs (Field Programmable Gate Arrays)\n(d) RISC Processors", ["a and b only", "a, b and c only", "a, b and d only", "a, b, c and d"], 1,
     "GPUs, DSPs and FPGAs are specialised; RISC is a general-purpose design style." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q21"),
    ("In Mano's general register organization (seven registers on a bus system), the two source registers are selected by", ["Two multiplexers driven by SELA and SELB",
                                                                                                                              "One decoder", "The program counter", "The stack pointer"], 0,
     PYQ + "The outputs go to the A and B inputs of the ALU."),
    ("In the same organization, the destination register is selected by", ["A 3 × 8 decoder driven by SELD", "A multiplexer", "The ALU", "The OPR field"], 0,
     "The decoder enables the load input of one register."),
    ("The control word of Mano's seven-register CPU has", ["14 bits: SELA 3, SELB 3, SELD 3, OPR 5", "16 bits", "12 bits: 3 + 3 + 3 + 3", "8 bits"], 0,
     "OPR selects one of the ALU operations."),
    ("For the micro-operation R1 ← R2 + R3, the control word sets", ["SELA = R2, SELB = R3, SELD = R1, OPR = ADD", "SELA = R1, SELB = R2, SELD = R3",
                                                                    "SELD = R2, SELA = R1", "OPR = SUB"], 0, "Sources on the buses, destination on the decoder."),
    ("A stack works on the principle", ["Last in, first out (LIFO)", "First in, first out (FIFO)", "Random access by address", "Priority order"], 0, "PUSH and POP work on the top."),
    ("The register that holds the address of the top of the stack is the", ["Stack pointer (SP)", "Program counter", "Data register", "Accumulator"], 0,
     "SP changes on every push and pop."),
    ("A register stack of 64 words needs a stack pointer of", ["6 bits", "8 bits", "64 bits", "5 bits"], 0, PYQ + "2⁶ = 64; FULL and EMTY flags record the state."),
    ("In Mano's memory stack, which grows toward lower addresses, PUSH is", ["SP ← SP − 1, then M[SP] ← DR", "M[SP] ← DR, then SP ← SP + 1",
                                                                             "DR ← M[SP], then SP ← SP + 1", "SP ← SP + 1 only"], 0, "POP: DR ← M[SP], SP ← SP + 1."),
    ("Popping from an empty stack causes", ["Stack underflow", "Stack overflow", "A page fault", "A cache miss"], 0, "Pushing onto a full stack causes overflow."),
    ("Stack-organized computers evaluate arithmetic expressions most easily in", ["Reverse Polish (postfix) notation", "Infix notation", "Prefix with brackets",
                                                                                 "Binary-coded decimal"], 0, PYQ + "Operands are pushed; an operator pops two and pushes the result."),
    ("The reverse Polish form of (A + B) * (C + D) is", ["A B + C D + *", "A B C D + + *", "+ A B * + C D", "A + B C D + *"], 0, "Each operator follows its operands."),
    ("The value of the reverse Polish expression  3 4 * 5 6 * +  is", ["42", "35", "72", "27"], 0, "12 + 30."),
    ("The reverse Polish form of A * B + C * D is", ["A B * C D * +", "A B C D * * +", "A * B C * D +", "* A B * C D +"], 0, "Multiplications first, then the addition."),
    ("Zero-address instructions are used in", ["Stack-organized computers", "Accumulator machines", "General-register machines", "Machines without memory"], 0,
     PYQ + "ADD pops two operands and pushes the sum."),
    ("One-address instructions use an implied", ["Accumulator (AC) for one operand and the result", "Stack", "Program counter", "Index register"], 0, "LOAD A, ADD B, STORE T…"),
    ("Evaluating X = (A + B) * (C + D) with three-address instructions needs", ["3 instructions", "2 instructions", "4 instructions", "8 instructions"], 0,
     "ADD R1, A, B; ADD R2, C, D; MUL X, R1, R2."),
    ("With zero-address (stack) instructions, X = (A + B) * (C + D) needs", ["8 instructions", "3 instructions", "5 instructions", "6 instructions"], 0,
     "PUSH A, PUSH B, ADD, PUSH C, PUSH D, ADD, MUL, POP X."),
    ("With two-address instructions, X = (A + B) * (C + D) needs", ["6 instructions", "4 instructions", "3 instructions", "8 instructions"], 0,
     "MOV R1, A; ADD R1, B; MOV R2, C; ADD R2, D; MUL R1, R2; MOV X, R1."),
    ("With one-address instructions, X = (A + B) * (C + D) needs", ["7 instructions", "5 instructions", "6 instructions", "8 instructions"], 0,
     "LOAD A; ADD B; STORE T; LOAD C; ADD D; MUL T; STORE X."),
    ("Three-address instructions give", ["Short programs but long instruction words", "Long programs but short instructions", "No memory references",
                                         "Always faster decoding"], 0, "The address fields make each instruction long."),
    ("In a RISC load/store architecture, memory is accessed only by", ["LOAD and STORE instructions", "Every arithmetic instruction", "Branch instructions", "Stack instructions"], 0,
     "Arithmetic works on registers."),
    ("The common fields of an instruction format are", ["Operation code, mode and address fields", "Sign, exponent and mantissa", "Label, comment and result",
                                                        "Tag, index and offset"], 0, "The mode field gives the addressing mode."),
    ("An instruction set with 100 different operations needs an opcode of at least", ["7 bits", "6 bits", "8 bits", "100 bits"], 0, PYQ + "2⁶ = 64 < 100 ≤ 128 = 2⁷."),
    ("A 16-bit instruction has two register fields on a machine with 16 registers. How many bits are left for the opcode?", ["8", "4", "12", "6"], 0, "16 − 4 − 4."),
    ("Giving instructions with fewer address fields longer opcodes, within a fixed instruction length, is called", ["Expanding opcode", "Microprogramming", "Pipelining",
                                                                                                                  "Relocation"], 0, "It makes room for more operations."),
    ("A memory stack is used mainly to", ["Save return addresses and processor status during subroutine calls and interrupts", "Hold the program code",
                                          "Store the page table", "Hold I/O data"], 0, "It also passes parameters and holds local variables."),
    ("The bounds of a memory stack can be checked with", ["Two processor registers holding the upper and lower limits", "The program counter", "A parity bit", "The ALU flags"], 0,
     "SP is compared with them after each push or pop."),
    ("The four status bits commonly set by the ALU are", ["Carry, sign, zero and overflow", "Parity, interrupt, halt and trap", "Read, write, execute and wait",
                                                          "Fetch, decode, execute and store"], 0, "Conditional branches test them."),
    ("In a register stack, PUSH (stack growing upward) is", ["SP ← SP + 1, then M[SP] ← DR", "DR ← M[SP], then SP ← SP − 1", "SP ← 0", "M[SP] ← DR only"], 0,
     "Mano's register stack; FULL is set when SP wraps to 0."),
]

MODES_RISC = [
    kset("KSET 2023 CS&A · Q98"),
    kset("KSET 2024 CS&A · Q17"),
    kset("KSET 2025 CS&A · Q15"),
    kset("KSET 2024 CS&A · Q16"),
    kset("KSET 2025 CS&A · Q19"),
    kset("KEA 2026 CS Paper-2 · Q22"),
    ("Match the following :\nL1  MOV AL, DATA\nL2  MOV BH, 'A'\nL3  MOV AX, [BX + 4]\nL4  MOV [BX + D1], CL\ni. Immediate address mode\nii. Direct data-addressing mode\n"
     "iii. Register relative addressing mode\niv. Base-plus-indirect addressing mode\nCode :  L1 L2 L3 L4",
     ["ii i iv iii", "iv i iii ii", "ii iv iii i", "ii i iii iv"], 3,
     "DATA is a memory address (direct); 'A' is a constant (immediate); [BX + 4] is register relative; [BX + DI] is base-plus-index." + NOTE, "GFGC 2021 CS · Q18"),
    ("In which addressing mode is the effective address equal to the address part of the instruction?", ["Indirect register", "Direct", "Register direct", "Relative"], 1,
     "Direct (absolute) addressing." + NOTE, "PGCET 2023 M.Tech CS · Q20"),
    ("Match List – I that has addressing mode with List – II that contains its description.\n(a) Immediate\n(b) Direct\n(c) Register\n(d) Register Indirect\n"
     "(i) Operand is in memory, instructions specifies the memory address.\n(ii) Operand value is the part of the instructions itself\n(iii) Operand is in CPU register\n"
     "(iv) Register contains address of the operand",
     ["a – ii, b – i, c – iii, d – iv", "a – i, b – iii, c – iv, d – ii", "a – iii, b – ii, c – iv, d – i", "a – ii, b – iv, c – i, d – iii"], 0,
     "Immediate – operand in the instruction; direct – its address; register – in a register; register indirect – address in a register." + NOTE, "PGCET 2026 CS · Q16"),
    ("Which Instruction Set Architecture (ISA) is used in the modern processors like ARM?", ["RISC", "CISC", "VLIW", "EPIC"], 0, "ARM = Advanced RISC Machine." + KLC,
     "Legislative Council 2024 Junior Console Operator P2 · Q33"),
    ("Let Tp be the clock cycle time. The time taken to execute 5 instructions in a pipelined processor, if the first instruction takes 4 clock cycles.",
     ["8 Tp", "16 Tp", "20 Tp", "14 Tp"], 0, "A 4-stage pipeline: (k + n − 1) cycles = 4 + 4 = 8." + NOTE, "GFGC 2021 CS · Q16"),
    ("Consider a four-stage pipeline processor in which each instruction on an average has 2 clock cycle stalls, then the speed up of this pipelined processor compared to "
     "an un-pipelined processor is ____", ["1.33", "2", "8", "0.5"], 0, "Speed-up = depth / (1 + stalls per instruction) = 4 / 3." + NOTE, "GFGC 2021 CS · Q22"),
    ("A processor has a branch misprediction penalty of 12 cycles and the branch instructions make 20% of the instructions. What is the average increase in execution time "
     "due to branch mispredictions?", ["2.4 cycles", "3.6 cycles", "5.0 cycles", "6.0 cycles"], 0,
     "0.20 × 12 = 2.4 cycles per instruction (taking every branch as mispredicted, as the question intends)." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q27"),
    ("Which of the following can be used to mitigate the performance penalty caused by pipeline stalls in a processor?\na) Data forwarding\nb) Branch prediction\n"
     "c) Instruction level parallelism\nd) Out of order execution\ne) Register renaming", ["a, b and d", "a, b, d and e", "b, d and e", "a, b, c, d and e"], 1,
     "Forwarding, prediction, out-of-order execution and renaming all hide stalls." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q28"),
    ("Which of the following is an example of a pipeline hazard?", ["Branch Misprediction", "Cache miss", "Data dependency between instructions", "Instruction fetch stall"], 2,
     "A data dependency causes a data hazard." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q30"),
    ("In implied addressing mode, the operand is", ["Specified implicitly by the definition of the instruction", "Given in the address field",
                                                   "In memory at the address held in a register", "In the program counter"], 0, "E.g. CMA (complement accumulator)."),
    ("In indirect addressing, the address field contains", ["The address of a memory word that holds the effective address", "The operand itself", "A register number",
                                                            "An offset from PC"], 0, "Two memory reads to reach the operand."),
    ("In indexed addressing, the effective address is", ["Address field + index register", "PC + address field", "The base register alone", "The operand itself"], 0,
     PYQ + "Used for arrays: the index register holds the element offset."),
    ("Base-register addressing is mainly used for", ["Relocation of programs in memory", "Immediate constants", "Loop counters", "Interrupts"], 0,
     "Only the base register changes when the program moves."),
    ("Autoincrement mode is convenient for", ["Stepping through arrays held in memory", "Subroutine calls", "Constants", "Interrupts"], 0, "The register is incremented after the access."),
    ("A two-word instruction at addresses 200–201 has address field 500. After the fetch PC = 202, R1 = 400 and XR = 100. The effective address in relative mode is",
     ["702", "500", "600", "400"], 0, PYQ + "Mano's example: EA = PC + address field = 202 + 500."),
    ("For the same instruction (address field 500, XR = 100), the effective address in indexed mode is", ["600", "702", "500", "100"], 0, "500 + 100."),
    ("Which addressing mode needs no memory reference to fetch the operand?", ["Immediate", "Direct", "Indirect", "Indexed"], 0, "Register mode also needs none."),
    ("After the instruction has been fetched, how many memory references does indirect addressing need to get the operand?", ["2", "1", "0", "3"], 0,
     "One for the address, one for the operand."),
    ("Which is a characteristic of RISC processors?", ["Fixed-length instructions executed mostly in one clock cycle, with hardwired control",
                                                       "Many complex addressing modes", "Microprogrammed control with variable-length instructions", "Memory-to-memory arithmetic"], 0,
     PYQ + "Also many registers and a load/store design."),
    ("Which is a characteristic of CISC processors?", ["A large instruction set with variable-length formats and many addressing modes", "A pure load/store architecture",
                                                       "Register windows", "Single-cycle execution of every instruction"], 0, "Usually microprogrammed."),
    ("Overlapped register windows in RISC processors are used to", ["Pass parameters between procedures without memory accesses", "Store the page table",
                                                                     "Hold microinstructions", "Speed up division"], 0, "Berkeley RISC / SPARC."),
    ("Which of these is a CISC architecture?", ["Intel x86", "ARM", "MIPS", "RISC-V"], 0, "VAX and IBM 370 are other CISC examples."),
    ("A delayed branch in a RISC pipeline means", ["The instruction after the branch (in the delay slot) is executed before the branch takes effect",
                                                   "The branch waits for an interrupt", "Branches are executed twice", "Branches are removed by the assembler"], 0,
     "The compiler fills the slot with a useful instruction."),
    ("A 5-stage pipeline executes 100 instructions with no stalls in", ["104 cycles", "500 cycles", "100 cycles", "105 cycles"], 0, PYQ + "k + n − 1 = 5 + 99."),
]

IO_INTERFACE = [
    ("Input or output devices attached to a computer are called", ["Peripherals", "Registers", "Buses", "Processors"], 0, "Keyboards, printers, disks, displays."),
    ("An input-output interface is needed between the CPU and peripherals mainly because", ["Peripherals differ from the CPU in signal type, speed, data format and operating mode",
                                                                                           "The CPU cannot address memory", "Peripherals have no power supply",
                                                                                           "Memory is too fast"], 0, PYQ + "Mano, ch. 11."),
    ("An I/O bus consists of", ["Data lines, address lines and control lines", "Data lines alone", "Power and ground lines", "Address lines and a clock"], 0,
     "The address selects the interface."),
    ("The four kinds of I/O command an interface may receive are", ["Control, status, data output and data input", "Read, write, fetch and decode", "Push, pop, call and return",
                                                                    "Add, subtract, shift and halt"], 0, "Mano, ch. 11."),
    ("In isolated I/O", ["I/O and memory have separate address spaces, and the CPU uses separate instructions such as IN and OUT", "I/O registers are memory locations",
                         "No control lines are needed", "DMA is required"], 0, PYQ + "Memory-mapped I/O uses ordinary memory instructions."),
    ("An advantage of memory-mapped I/O is that", ["Every memory-reference instruction can also work on I/O registers", "The whole address space stays free for memory",
                                                  "Separate IN/OUT instructions are faster", "It needs no address decoding"], 0, "The cost is part of the address space."),
    ("Memory-mapped I/O reduces the memory addresses available because", ["Part of the address space is assigned to I/O registers", "I/O devices need cache",
                                                                          "DMA uses memory", "Interrupts use memory"], 0, "Isolated I/O avoids this."),
    ("A processor with its own instruction set that runs I/O programs (channel programs) is an", ["I/O processor (IOP)", "ALU", "Floating-point unit", "Cache controller"], 0,
     "It frees the CPU from I/O work."),
    ("The drawback of strobe-controlled asynchronous transfer is that", ["The source cannot know whether the destination actually received the data",
                                                                         "Two control lines are needed", "It needs a common clock", "It works for serial data alone"], 0,
     PYQ + "Handshaking solves this."),
    ("Handshaking uses", ["Two control signals – e.g. 'data valid' from the source and 'data accepted' from the destination", "One strobe pulse", "A common clock",
                          "Parity bits"], 0, "Each unit tells the other what it has done."),
    ("In handshaking, a fault in the destination unit can be detected by", ["A timeout – the source waits too long for the reply signal", "Parity checking", "A checksum",
                                                                            "Raising the clock rate"], 0, "Then an error routine is run."),
    ("Two units with independent clocks transfer data using", ["Asynchronous transfer (strobe or handshaking)", "A shared clock", "Memory-mapped I/O", "DMA"], 0,
     "Most CPU–peripheral transfers are asynchronous."),
    ("In a destination-initiated strobe transfer", ["The destination raises the strobe to request data, and the source puts the data on the bus",
                                                    "The source sends data without being asked", "The CPU clock times the transfer", "Data is sent serially"], 0,
     "The source-initiated version is the reverse."),
    ("Which peripheral transfers data the slowest?", ["Keyboard", "Magnetic disk", "Solid-state drive", "Gigabit network card"], 0, "It depends on human typing speed."),
    ("Each peripheral has its own controller, which", ["Operates the device and communicates with the interface", "Runs user programs", "Stores the operating system",
                                                       "Replaces the CPU"], 0, "E.g. a disk controller."),
    ("An interface with four registers selects one of them using", ["Register-select inputs RS1 and RS0 plus a chip-select CS", "Eight select lines", "The program counter",
                                                                    "The interrupt vector"], 0, PYQ + "Mano's example interface unit."),
    ("The status register of an interface tells the CPU", ["Whether the device is ready, busy or has an error", "The next instruction", "The memory size", "The cache contents"], 0,
     "Flag bits such as FGI and FGO."),
    ("Port A and port B of a programmable interface hold", ["Data being transferred in or out", "Microinstructions", "Page tables", "Interrupt priorities"], 0,
     "The control register sets their direction."),
    ("In synchronous data transfer between CPU and memory, both units", ["Share a common clock", "Use handshaking signals", "Use start and stop bits", "Use DMA"], 0,
     "Transfers happen on clock edges."),
    ("Which device is purely an output peripheral?", ["Printer", "Keyboard", "Scanner", "Microphone"], 0, "The others are input devices."),
    ("A touch screen is", ["Both an input and an output device", "An input device alone", "An output device alone", "A storage device"], 0, "It displays and senses touch."),
    ("Compared with the CPU, most peripherals transfer data", ["Much more slowly, so synchronization is needed", "Faster", "At exactly the same rate", "Without control signals"], 0,
     "Hence buffering and flags."),
    ("Character-oriented peripherals such as terminals exchange data mostly as", ["ASCII (alphanumeric) codes", "Floating-point numbers", "Microinstructions", "Page numbers"], 0,
     "One character per transfer."),
    ("Three-state (tri-state) buffers allow", ["Several sources to share one bus line, only one being enabled at a time", "Faster ALU operations", "Storing three bits",
                                               "Error correction"], 0, "The disabled outputs are in the high-impedance state."),
    ("A computer that uses one common bus and common read/write lines for both memory and I/O uses", ["Memory-mapped I/O", "Isolated I/O", "Programmed DMA",
                                                                                                       "Direct cache access"], 0, "Isolated I/O has separate I/O read/write lines."),
    ("A keyboard interface tells the CPU that a key has been pressed by", ["Setting a status flag (or raising an interrupt)", "Changing the program counter",
                                                                          "Filling a cache line", "Moving the stack pointer"], 0, "The CPU then reads the data register."),
    ("Arrange the source-initiated handshake: (a) the destination accepts the data and raises 'data accepted' (b) the source places the data and raises 'data valid' "
     "(c) the source removes 'data valid' (d) the destination lowers 'data accepted'", ["b, a, c, d", "a, b, c, d", "b, c, a, d", "c, a, b, d"], 0,
     PYQ + "Each step waits for the other unit's signal."),
    ("The Intel 8255 is a", ["Programmable peripheral interface with three 8-bit ports", "DMA controller", "Interrupt controller", "Serial communication chip"], 0,
     "Ports A, B and C."),
    ("When an interface receives a control command, it", ["Activates the peripheral and tells it what to do", "Writes to memory", "Changes the PC", "Halts the CPU"], 0,
     "E.g. rewind a tape or start a disk."),
    ("The I/O address placed on the address lines is used to", ["Select the interface (and the register within it) for the transfer", "Select a memory bank",
                                                                "Select a cache way", "Select a microinstruction"], 0, "Each interface decodes its own addresses."),
]

TRANSFER_INTERRUPT = [
    ("Match the 8085 hardware interrupt with its vector address\nInterrupt: L1. RST 7.5  L2. RST 6.5  L3. RST 5.5  L4. TRAP\nVector Address: i. 003CH  ii. 0034H  iii. 002CH  iv. 0024H\n"
     "Code: L1 L2 L3 L4", ["i ii iii iv", "ii iii i iv", "iii ii i iv", "iv ii iii i"], 0,
     "Vector = n × 8 for RST n: 7.5 → 3CH, 6.5 → 34H, 5.5 → 2CH, TRAP (4.5) → 24H." + NOTE, "GFGC 2021 CS · Q54"),
    ("The three modes of transferring data between the CPU and I/O devices are", ["Programmed I/O, interrupt-initiated I/O and DMA", "Strobe, handshake and clock",
                                                                                 "Serial, parallel and USB", "Polling, paging and caching"], 0, PYQ + "Mano, ch. 11."),
    ("Finding the interrupting device by software polling is", ["Simple but slow when many devices are connected", "The fastest method", "Done by a daisy chain", "Done by DMA"], 0,
     "The polling order sets the priority."),
    ("In a daisy-chain priority interrupt", ["The device electrically nearest the CPU has the highest priority", "The farthest device has the highest priority",
                                             "All devices have equal priority", "Priority is set by software alone"], 0, PYQ + "The acknowledge passes from device to device."),
    ("In a daisy chain, a device that has a pending interrupt", ["Blocks the acknowledge (PO = 0) and puts its vector address on the bus", "Passes the acknowledge on (PO = 1)",
                                                                 "Ignores the acknowledge", "Resets the CPU"], 0, "Devices further down see PI = 0."),
    ("A parallel priority interrupt circuit uses", ["An interrupt register, a mask register and a priority encoder", "A daisy chain", "A DMA controller", "A shift register"], 0,
     "The encoder outputs the vector of the highest-priority request."),
    ("The mask register in a priority interrupt unit", ["Disables (masks) selected interrupt requests", "Stores the vector addresses", "Counts interrupts",
                                                        "Holds the return address"], 0, "Set by the program."),
    ("In a vectored interrupt, the CPU obtains the address of the service routine from", ["The interrupting device (its vector)", "A fixed location only",
                                                                                          "Polling every device", "The DMA controller"], 0,
     "Non-vectored interrupts branch to a fixed location."),
    ("A non-maskable interrupt such as TRAP in the 8085 is used for", ["Critical events such as power failure – it cannot be disabled", "Keyboard input",
                                                                       "Timer ticks that may be ignored", "Software exceptions alone"], 0, "It has the highest priority."),
    ("When the CPU accepts an interrupt, it first", ["Completes the current instruction, saves PC (and status) and branches to the service routine",
                                                     "Discards the current instruction", "Clears memory", "Halts"], 0, "Then IEN is cleared to block nesting (in simple CPUs)."),
    ("A divide-by-zero detected by the CPU causes", ["An internal interrupt (trap)", "An external interrupt", "A DMA request", "A cache miss"], 0,
     "External interrupts come from devices or timers."),
    ("A software interrupt is", ["Started by executing an instruction, e.g. a supervisor call to the OS", "Caused by a power failure", "Caused by an I/O device",
                                 "Caused by a timer"], 0, "INT n on x86."),
    ("In DMA, the controller requests the buses with BR, and the CPU replies with", ["BG (bus grant), after putting its bus lines in the high-impedance state", "An interrupt",
                                                                                      "A strobe", "A parity bit"], 0, PYQ + "The DMA controller then drives the buses."),
    ("A DMA controller contains", ["An address register, a word-count register and a control register", "A data register alone", "The program counter", "A page table"], 0,
     "The CPU loads them before the transfer."),
    ("In cycle-stealing DMA", ["The controller transfers one word and returns the bus, stealing single memory cycles from the CPU", "The whole block is sent while the CPU waits",
                               "The CPU transfers each word", "Interrupts are disabled"], 0, "The CPU slows down a little."),
    ("In burst-mode DMA", ["A block of words is transferred in one continuous burst while the CPU is held off the bus", "One word per cycle is stolen",
                           "The CPU executes the I/O program", "No bus request is made"], 0, "Used for fast devices such as disks."),
    ("When the word count of a DMA transfer reaches zero, the controller", ["Stops and interrupts the CPU", "Starts again", "Halts the computer", "Clears memory"], 0,
     "The CPU then checks the result."),
    ("DMA is best suited for", ["High-speed block transfers such as disk to memory", "Single keystrokes", "Printing one character", "Reading a switch"], 0,
     "Programmed I/O suits slow, small transfers."),
    ("The Intel 8237 and 8259 are, respectively, a", ["DMA controller and a programmable interrupt controller", "Interrupt controller and a DMA controller", "Timer and a UART",
                                                      "Peripheral interface and a timer"], 0, "8255 = PPI, 8253/8254 = timer, 8251 = USART."),
    ("An I/O processor (channel) differs from a simple DMA controller because it", ["Fetches and executes its own I/O instructions (channel programs)", "Cannot access memory",
                                                                                     "Is slower than programmed I/O", "Uses no bus"], 0, "The CPU only starts the channel program."),
    ("In asynchronous serial transmission, each character is framed by", ["A start bit (0) and one or more stop bits (1)", "A clock pulse", "Two parity bits",
                                                                          "A header and trailer of bytes"], 0, PYQ + "The line rests at 1 between characters."),
    ("A terminal sends 10 characters per second, each with 1 start bit, 8 data bits and 2 stop bits. The baud rate is", ["110", "80", "100", "88"], 0,
     PYQ + "11 bits × 10 characters per second."),
    ("With 1 start bit, 8 data bits and 1 stop bit, the fraction of transmitted bits that carry data is", ["80%", "100%", "90%", "70%"], 0, "8 / 10."),
    ("A UART (universal asynchronous receiver-transmitter)", ["Converts parallel data to serial for transmission and back on reception", "Is a DMA controller",
                                                              "Stores interrupt vectors", "Decodes addresses"], 0, "It also adds the start, stop and parity bits."),
    ("Synchronous serial transmission", ["Sends blocks of characters without start/stop bits per character, keeping the two clocks in step",
                                         "Uses start and stop bits for every character", "Needs no clock", "Is slower than asynchronous transmission"], 0,
     "Sync characters mark the start of a block."),
    ("In the 8085, which interrupt is non-maskable and has the highest priority?", ["TRAP", "RST 7.5", "RST 6.5", "INTR"], 0, PYQ + "INTR has the lowest priority."),
    ("The 8085 interrupts in order of priority (highest first) are", ["TRAP, RST 7.5, RST 6.5, RST 5.5, INTR", "INTR, RST 5.5, RST 6.5, RST 7.5, TRAP",
                                                                      "RST 7.5, TRAP, RST 6.5, RST 5.5, INTR", "TRAP, INTR, RST 7.5, RST 6.5, RST 5.5"], 0,
     "TRAP is both edge and level triggered."),
    ("Interrupt latency is", ["The delay between an interrupt request and the start of its service routine", "The time a service routine takes",
                              "The time between two interrupts", "The time to switch off interrupts"], 0, "Lower latency suits real-time systems."),
    ("During a DMA transfer, the CPU", ["Can continue internal work that does not need the buses", "Executes each data transfer instruction", "Is switched off",
                                       "Must poll the device"], 0, "It waits only when it needs the bus."),
    ("Which mode of transfer gives the highest data rate for block transfers?", ["DMA", "Programmed I/O", "Interrupt-initiated I/O", "Polling with handshaking"], 0,
     "Data does not pass through the CPU."),
]

TOPICS = {
    "Central Processing Unit": [
        ("1 · General Register Organization, Stack Organization and Instruction Formats", REG_STACK_FORMATS),
        ("2 · Addressing Modes, RISC and CISC Computers (with Pipelining)", MODES_RISC),
    ],
    "Input-Output Organization": [
        ("1 · Peripheral Devices, Input-Output Interface and Asynchronous Data Transfer", IO_INTERFACE),
        ("2 · Modes of Transfer, Priority Interrupt, DMA and Serial Communication", TRANSFER_INTERRUPT),
    ],
}

NOTES = {
    "Central Processing Unit": [{"title": "CPU – revision sheet", "md": """## General register organization
- 7 registers on a bus system; SELA/SELB drive two MUXes (ALU inputs), SELD drives a 3 × 8 decoder (destination)
- Control word 14 bits = SELA 3 + SELB 3 + SELD 3 + OPR 5; R1 ← R2 + R3 → SELA = R2, SELB = R3, SELD = R1, OPR = ADD
- ALU status bits: C (carry), S (sign), Z (zero), V (overflow)

## Stack organization
- LIFO; SP = top; 64-word register stack → 6-bit SP, FULL/EMTY flags
- Memory stack growing down: PUSH SP ← SP − 1, M[SP] ← DR; POP DR ← M[SP], SP ← SP + 1; limit registers check overflow/underflow
- Reverse Polish: (A + B) * (C + D) → A B + C D + *; 3 4 * 5 6 * + = 42

## Instruction formats – X = (A + B) * (C + D)
| Format | Instructions |
|---|---|
| Three-address | 3 (short program, long instructions) |
| Two-address | 6 |
| One-address (AC) | 7 |
| Zero-address (stack) | 8 |
- Opcode bits ≥ ⌈log₂ operations⌉ (100 ops → 7 bits); expanding opcode

## Addressing modes (EA = effective address)
| Mode | EA / operand |
|---|---|
| Implied | in the opcode (CMA) |
| Immediate | operand in the instruction (no memory access) |
| Register / register indirect | in register / address in register |
| Direct | address field |
| Indirect | M[address field] (2 memory accesses) |
| Relative | PC + address field |
| Indexed | XR + address field |
| Base register | base + address (relocation) |
| Autoincrement/decrement | register indirect, then ±1 |
- Mano example: PC = 202, address 500, XR = 100 → relative 702, indexed 600

## RISC vs CISC and pipelining
- RISC: few simple instructions, fixed length, load/store, many registers, register windows, hardwired, ~1 cycle, delayed branch (ARM, MIPS, SPARC, RISC-V)
- CISC: many instructions and modes, variable length, memory operands, microprogrammed (x86, VAX)
- Pipeline: k stages, n instructions → k + n − 1 cycles; speed-up nk / (k + n − 1); with s stall cycles per instruction speed-up = k / (1 + s)
- Hazards: structural, data (dependency – forwarding), control/instruction (branches – prediction, delay slots); stalls reduced by forwarding, prediction, out-of-order execution, register renaming
"""}],
    "Input-Output Organization": [{"title": "I/O organization – revision sheet", "md": """## Interface
- Needed because of differences in signals, speed, data format and modes; I/O bus = data + address + control lines
- Commands: control, status, data output, data input; registers chosen by CS, RS1, RS0 (ports A, B, control, status)
- Isolated I/O (separate address space, IN/OUT, I/O read/write lines) vs memory-mapped I/O (I/O registers are memory addresses; all memory instructions work)
- IOP / channel runs its own I/O programs; chips: 8255 PPI, 8251 USART, 8253/54 timer, 8257/8237 DMA, 8259 PIC

## Asynchronous transfer
- Strobe (one line; source- or destination-initiated) – no acknowledgement
- Handshaking (two lines: data valid / data accepted; timeout detects faults): b → a → c → d sequence
- Synchronous transfer uses a common clock (CPU–memory)

## Modes of transfer
1. Programmed I/O – CPU polls the flag (busy waiting)
2. Interrupt-initiated I/O – device interrupts when ready
3. DMA – BR/BG; address, word-count and control registers; burst vs cycle stealing; interrupt when the count reaches 0

## Priority interrupt
- Software polling; daisy chain (nearest device highest; PI/PO; vector on the bus); parallel (interrupt register + mask register + priority encoder)
- Vectored vs non-vectored; maskable vs non-maskable; internal (trap), external, software interrupts
- 8085: TRAP (24H, NMI) > RST 7.5 (3CH) > RST 6.5 (34H) > RST 5.5 (2CH) > INTR; interrupt latency = request → start of ISR

## Serial communication
- Asynchronous: start bit 0, 5–8 data bits, optional parity, 1–2 stop bits; 10 char/s × 11 bits = 110 baud; UART
- Synchronous: blocks with sync characters, no start/stop bits per character
"""}],
}
