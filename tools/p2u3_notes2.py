"""P2 · Unit 3 – Computer System Architecture · second, DETAILED note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". The first short sheets stay in p2u3_a … e.
Numericals (Booth trace, complements, BCD, IEEE 754, cache address split, AMAT, pipeline speed-up, memory chips, Gray code)
were computed with a script on 19 Oct 2026. Facts follow M. Morris Mano (Digital Logic and Computer Design; Computer System
Architecture)."""

TOPICS = {}  # notes only

T = " – detailed notes with worked examples"

NOTES = {
    "Digital Logic – Combinational": [{"title": "Combinational logic" + T, "md": """## Logic gates
| Gate | Expression | Output 1 when |
|---|---|---|
| AND | AB | all inputs 1 |
| OR | A + B | any input 1 |
| NOT | A′ | input 0 |
| **NAND** | (AB)′ | any input 0 – **universal** |
| **NOR** | (A + B)′ | all inputs 0 – **universal** |
| XOR | A ⊕ B = A′B + AB′ | inputs differ (odd number of 1s) |
| XNOR | (A ⊕ B)′ | inputs equal |
- NOT from NAND: tie inputs; AND = NAND + NOT (2 NANDs); OR = 3 NANDs (De Morgan); XOR needs 4 NANDs
- Positive vs negative logic; fan-in, fan-out, propagation delay; logic families TTL (5 V), CMOS (low power)

## Boolean algebra and K-maps (recap)
- De Morgan: (AB)′ = A′ + B′, (A + B)′ = A′B′; absorption A + AB = A; A + A′B = A + B
- K-map in Gray order; groups of 1, 2, 4, 8; don't-cares help; Σm(0, 2, 4, 5, 6) → **C′ + AB′**
- Gray code changes one bit at a time: binary 110 → Gray **101** (b ⊕ (b >> 1))

## Combinational circuits (output depends only on present inputs)
| Circuit | Function | Size facts |
|---|---|---|
| **Half adder** | S = A ⊕ B, C = AB | 1 XOR + 1 AND |
| **Full adder** | S = A ⊕ B ⊕ Cin, Cout = AB + Cin(A ⊕ B) | 2 half adders + 1 OR |
| Ripple-carry adder | n full adders chained | delay grows with n → **carry look-ahead** adder (G = AB, P = A ⊕ B) |
| Half / full subtractor | D = A ⊕ B, borrow = A′B | |
| Adder-subtractor | XOR gates on B with M (0 add, 1 subtract → 2's complement) | |
| **Decoder** n × 2ⁿ | one output line per input combination | 3 × 8 decoder; implements any function with an OR gate |
| **Encoder** 2ⁿ × n | reverse; **priority encoder** handles several active inputs | 8 × 3 (octal → binary) |
| **Multiplexer** 2ⁿ × 1 | selects one of 2ⁿ inputs with **n select lines** | 16 × 1 MUX needs 4 select lines; implements any n + 1 variable function |
| Demultiplexer 1 × 2ⁿ | one input to one of 2ⁿ outputs | same as a decoder with enable |
| Comparator | A > B, A = B, A < B | equality via XNOR |
| BCD to 7-segment, code converters, parity generator/checker | | parity = XOR of bits |
- Bigger MUX from smaller: 8 × 1 from two 4 × 1 + one 2 × 1; 32 × 1 from 4 × 1 MUXes needs 8 + 2 + 1 = 11

## Traps
- NAND and NOR are universal; XOR is not
- A 2ⁿ × 1 MUX has n select lines
- A full adder = two half adders + an OR gate"""}],

    "Digital Logic – Sequential": [{"title": "Sequential logic" + T, "md": """## Latches and flip-flops (output depends on input and present state)
- **SR latch** (NOR or NAND); S = R = 1 is **invalid** (forbidden) for NOR latch
- Latch = level-triggered; **flip-flop** = edge-triggered (master–slave or edge-detect)

| FF | Characteristic equation | Behaviour |
|---|---|---|
| **SR** | Q⁺ = S + R′Q (SR = 0) | set, reset, no change, invalid |
| **D** | Q⁺ = D | delay / data latch |
| **JK** | Q⁺ = JQ′ + K′Q | like SR, but J = K = 1 **toggles** |
| **T** | Q⁺ = T ⊕ Q | toggle when T = 1 |
- **Excitation tables** (what input gives a wanted transition): JK 0→0: J = 0, K = X; 0→1: J = 1, K = X; 1→0: J = X, K = 1; 1→1: J = X, K = 0
- **Race-around** condition in a level-triggered JK with J = K = 1 → fixed by **master–slave** or edge triggering
- Conversions: D from JK (J = D, K = D′); T from JK (J = K = T)
- Setup time, hold time, propagation delay; preset and clear (asynchronous)

## Sequential circuit analysis and design
- **Mealy** machine: output depends on state **and** input; **Moore**: output depends on state only
- State table, state diagram, state reduction, state assignment, excitation equations
- Number of flip-flops for N states = ⌈log₂ N⌉

## Registers
- n-bit register = n flip-flops with a common clock
- **Shift registers**: SISO, SIPO, PISO, **PIPO**; left/right/bidirectional, universal shift register
- Shifting n-bit data serially takes n clock pulses (SISO in + out: 2n − 1 for the last bit to appear)
- Ring counter (n FFs → n states), **Johnson (twisted-ring) counter** (n FFs → **2n** states)

## Counters
| Type | Feature |
|---|---|
| **Ripple (asynchronous)** | each FF clocked by the previous FF's output; slow (delays add); 4-bit counts 0–15 |
| **Synchronous** | all FFs share the clock; faster |
| Up / down / up-down | |
| **Mod-N** | N states; needs ⌈log₂ N⌉ FFs – **mod-10 (decade/BCD) counter needs 4 FFs**; reset at state N |
- n-bit binary counter: modulus 2ⁿ; frequency division by 2ⁿ at the last FF (4-bit: f/16)

## Integrated circuits and memory unit
- Scale: SSI (< 10 gates), MSI (10–100), LSI (100–10,000), **VLSI** (> 10,000), ULSI
- Memory unit: k address lines and n data lines → **2ᵏ words × n bits** (e.g. 1K × 8 has 10 address and 8 data lines)
- RAM (SRAM – flip-flops; DRAM – capacitors, refresh), ROM types (mask ROM, PROM, EPROM – UV, EEPROM, flash); PLA, PAL programmable logic

## Traps
- J = K = 1 toggles; S = R = 1 is invalid
- Johnson counter with n flip-flops has 2n states; ring counter n
- Mealy outputs change with inputs; Moore outputs change only with state"""}],

    "Data Representation": [{"title": "Data representation" + T, "md": """## Number systems
- Radix r: binary 2, octal 8, decimal 10, hexadecimal 16
- 156₁₀ = 10011100₂ = 234₈ = 9C₁₆; group 3 bits for octal, 4 for hex
- Fractions: multiply by 2 repeatedly (0.375 = 0.011₂); 0.1 has no exact binary form

## Complements
- **(r − 1)'s complement**: subtract each digit from r − 1 (1's complement: flip bits; 9's complement of 3456 = 6543)
- **r's complement** = (r − 1)'s complement + 1 (2's complement; 10's complement of 3456 = 6544)
- −6 in 8-bit 2's complement = **11111010**
- Subtraction by complements: A − B = A + (r's complement of B); discard the end carry (r's) or add it back (end-around carry, 1's)

## Signed number representation (n bits)
| Form | Range (8 bits) | Zero |
|---|---|---|
| Sign-magnitude | −127 … +127 | two zeros |
| 1's complement | −127 … +127 | two zeros |
| **2's complement** | **−128 … +127** | one zero |

## Fixed and floating point
- Fixed point: binary point at a fixed position (integers, fractions)
- **IEEE 754 single**: 1 sign + 8 exponent (bias **127**) + 23 fraction; value (−1)ˢ × 1.f × 2^(e − 127)
  - −0.75 = −1.1₂ × 2⁻¹ → s = 1, e = 126 = 01111110, f = 100… → **0xBF400000**
  - 5.75 → 0x40B80000
- Double: 1 + 11 (bias 1023) + 52; special values: e all 0s → zero/denormal; all 1s → ∞ or NaN
- **Normalisation** keeps one 1 before the point (hidden bit); overflow/underflow; precision vs range trade-off

## Codes
| Code | Note |
|---|---|
| **BCD (8421)** | each decimal digit in 4 bits; 1010–1111 invalid; 59 = 0101 1001 |
| **Excess-3** | BCD + 3 (5 → 1000); self-complementing |
| 2421, 84-2-1 | weighted, self-complementing |
| **Gray** | one bit changes between successive values (encoders); 6 → 101 |
| ASCII (7-bit), EBCDIC (8-bit IBM), Unicode | characters |
- BCD addition: if a digit sum > 9 (or a carry), add 6 (0110) – 59 + 38 → 1001 0111 = 97

## Error detection and correction
- **Parity** bit (even/odd) detects any odd number of errors
- **Hamming code**: parity bits at positions 1, 2, 4, 8 …; 2ᵖ ≥ m + p + 1; corrects single-bit errors (SEC), with an extra overall parity detects double errors (SEC-DED); data 1011 → codeword 0110011
- CRC (polynomial division) for bursts; checksums
- Hamming distance d: detect d − 1, correct ⌊(d − 1)/2⌋

## Traps
- 2's complement has a single zero and an asymmetric range
- IEEE single bias is 127
- BCD 1010 is invalid; Excess-3 is not weighted"""}],

    "Computer Arithmetic": [{"title": "Computer arithmetic" + T, "md": """## Addition and subtraction
**Signed magnitude**: compare signs – same sign → add magnitudes, keep the sign; different signs → subtract the smaller magnitude from the larger, take the larger's sign (hardware needs a comparator)

**2's complement**: just add (subtraction = add the 2's complement); discard the carry out
- **Overflow** when two numbers of the same sign give a result of the opposite sign; detected as **carry into the sign bit ≠ carry out of the sign bit** (V = Cₙ ⊕ Cₙ₋₁)
- 8-bit: 127 + 1 = 10000000 = −128 → overflow; −128 − 1 also overflows
- Adding a positive and a negative number can never overflow

**BCD addition**: add binary digits; if the result > 9 or a carry occurs, add 6 → 59 + 38: 1001 + 1000 = 10001 → +0110 → 0111 carry 1; 0101 + 0011 + 1 = 1001 → **97**

## Multiplication
- Shift-and-add (unsigned): for each multiplier bit 1, add the shifted multiplicand
- **Booth's algorithm** (signed, 2's complement): look at the pair (Q₀, Q₋₁) each step
| Q₀ Q₋₁ | Action |
|---|---|
| 0 0 / 1 1 | just arithmetic shift right (A, Q, Q₋₁) |
| 1 0 | A ← A − M, then shift |
| 0 1 | A ← A + M, then shift |
**Worked 7 × (−3) with 5 bits**: M = 00111, −M = 11001, Q = 11101, A = 00000, Q₋₁ = 0
| Step | Q₀Q₋₁ | Operation | A | Q | Q₋₁ |
|---|---|---|---|---|---|
| 1 | 10 | A − M = 11001, shift | 11100 | 11110 | 1 |
| 2 | 01 | A + M = 00011, shift | 00001 | 11111 | 0 |
| 3 | 10 | A − M = 11010, shift | 11101 | 01111 | 1 |
| 4 | 11 | shift | 11110 | 10111 | 1 |
| 5 | 11 | shift | 11111 | 01011 | 1 |
Result A:Q = 11111 01011 = **−21** ✓
- Booth handles strings of 1s efficiently; worst case alternating 0101…; **modified (radix-4) Booth** halves the steps
- Array multipliers (combinational), Wallace tree

## Division
- **Restoring division**: shift left, subtract divisor; if the result is negative, restore (add back) and set the quotient bit 0, else 1
- **Non-restoring division**: if negative, next step **adds** instead of restoring → fewer operations; a final correction of the remainder may be needed
- Divide overflow when the quotient doesn't fit; division by zero detection

## Floating-point arithmetic
- Add/subtract: **align exponents** (shift the smaller number's mantissa right), add mantissas, **normalise**, round
- Multiply: add exponents (subtract one bias), multiply mantissas, normalise; divide: subtract exponents, divide mantissas
- Rounding modes: round to nearest even (default), toward 0, ±∞; guard, round and sticky bits

## Decimal arithmetic unit
- BCD adder: 4-bit binary adder + correction logic (add 6 when the sum > 9) – output carry K + Z₈Z₄ + Z₈Z₂

## Traps
- Overflow = carry into sign ≠ carry out of sign
- Booth: 10 → subtract, 01 → add
- Non-restoring division avoids the restore step"""}],

    "Basic Computer Organization and Design": [{"title": "Mano's basic computer" + T, "md": """## Stored-program organisation and instruction codes
- Memory 4096 × 16 → **12-bit address**; instruction = **I (1 bit) + opcode (3 bits) + address (12 bits)**
- I = 0 → **direct** address; I = 1 → **indirect** (memory word holds the effective address)
- Three instruction formats: **memory-reference** (opcode 000–110), **register-reference** (opcode 111, I = 0 → 7xxx), **input-output** (opcode 111, I = 1 → Fxxx)

## Registers
| Register | Bits | Purpose |
|---|---|---|
| **DR** | 16 | data register (memory operand) |
| **AR** | 12 | address register |
| **AC** | 16 | accumulator |
| **IR** | 16 | instruction register |
| **PC** | 12 | program counter |
| **TR** | 16 | temporary register |
| INPR / OUTR | 8 | input / output character |
| E | 1 | extended accumulator bit (carry) |
| SC | 4 | sequence counter (timing T0–T15) |
- Registers and memory connected by a **16-bit common bus** with select lines S2 S1 S0 (8 sources)

## Instruction set
- **Memory-reference** (7): **AND**, **ADD**, **LDA** (load AC), **STA** (store AC), **BUN** (branch unconditionally), **BSA** (branch and save return address – subroutine call), **ISZ** (increment and skip if zero)
- **Register-reference** (12): CLA, CLE, CMA, CME, CIR, CIL, INC, SPA, SNA, SZA, SZE, HLT
- **I/O** (6): INP, OUT, SKI, SKO, ION, IOF
- Instruction-set completeness: arithmetic/logic, data transfer, program control, I/O instructions

## Timing and control
- **Hardwired control** (gates, decoders, SC + 4 × 16 timing decoder → T0 … T15; fast) vs **microprogrammed control** (control memory of microinstructions; flexible, slower)
- SC is cleared to 0 after each instruction

## Instruction cycle
- **T0**: AR ← PC; **T1**: IR ← M[AR], PC ← PC + 1 (fetch); **T2**: decode D0–D7 ← IR(12–14), AR ← IR(0–11), I ← IR(15); **T3**: indirect → AR ← M[AR] (or execute register/I/O instruction)
- Execution of memory-reference instructions starts at **T4**:
  - ADD: D1T4: DR ← M[AR]; D1T5: AC ← AC + DR, E ← Cout, SC ← 0
  - BSA: M[AR] ← PC, AR ← AR + 1 (T4); PC ← AR (T5)
  - ISZ: DR ← M[AR] (T4); DR ← DR + 1 (T5); M[AR] ← DR, if DR = 0 then PC ← PC + 1 (T6)
- Flowchart: fetch → decode → (indirect?) → execute → check interrupt

## Input-output and interrupt
- FGI (input flag) set when a new character is in INPR; FGO (output flag) set when OUTR is ready
- **Program interrupt**: IEN (interrupt enable) + flag set → at the end of an instruction cycle the interrupt cycle stores PC in location 0 and branches to location 1: R T0: AR ← 0, TR ← PC; R T1: M[AR] ← TR, PC ← 0; R T2: PC ← PC + 1, IEN ← 0, R ← 0, SC ← 0

## Traps
- Memory-reference opcodes 000–110; 111 marks register or I/O instructions (I decides which)
- BSA is the subroutine call (return with an indirect BUN)
- PC and AR are 12 bits; AC, DR, IR, TR are 16 bits"""}],

    "Programming the Basic Computer": [{"title": "Programming the basic computer" + T, "md": """## Machine language vs assembly language
- Machine language: binary/hex instruction codes (e.g. 2004 = LDA 004 in hex)
- **Assembly language**: symbolic opcodes and addresses; one line = label, instruction, comment
- **Pseudo-instructions** (assembler directives, not machine code): **ORG N** (origin – next instruction at address N), **END**, **DEC N** (decimal constant), **HEX N** (hex constant)
- Example – add two numbers:
```
      ORG 100
      LDA A     / load first operand
      ADD B     / add second
      STA C     / store sum
      HLT
A,    DEC 83
B,    DEC -23
C,    DEC 0
      END
```
After running, C = **60**.

## The assembler
- **Two-pass assembler**: **pass 1** builds the **address symbol table** (labels → addresses) using a location counter (LC); **pass 2** translates instructions to binary using the opcode table, pseudo-instruction table and symbol table
- Two passes are needed because of **forward references** (a label used before it is defined)
- Error checks: undefined labels, invalid opcodes

## Program loops
```
      ORG 100
      LDA ADS   / address of the first number
      STA PTR   / initialise pointer
      LDA NBR   / -100
      STA CTR   / initialise counter
      CLA
LOP,  ADD PTR I / add the number pointed to (indirect)
      ISZ PTR   / next address
      ISZ CTR   / count; skip when zero
      BUN LOP
      STA SUM
      HLT
```
- Counters count up from a negative value with **ISZ** (skip when it reaches 0); pointers use **indirect addressing**

## Arithmetic and logic programs
- Multiplication by **repeated add and shift** (CIL/CIR shift through E); double-precision addition with the carry in E
- Logic operations: AND is an instruction; OR via De Morgan (CMA, AND, CMA); XOR built from AND, OR, complement
- Shifts: CIL (circular left), CIR (circular right) through E; arithmetic shift needs extra handling of the sign

## Subroutines
- Call: **BSA SUB** stores the return address in location SUB and jumps to SUB + 1
- Return: **BUN SUB I** (indirect branch through the saved address)
- Parameters passed in AC or in locations following the BSA instruction

## Input-output programming
- Input a character: `CIF, SKI / BUN CIF / INP / OUT / STA CHR` – wait until FGI = 1 (busy-wait loop), then input
- Output: `COF, SKO / BUN COF / OUT`
- Interrupt-driven I/O: service routine at address 1 saves registers (AC, E), checks flags, serves the device, restores, ION, returns with BUN 0 I

## Traps
- ORG, END, DEC, HEX generate no machine code
- Pass 1 builds the symbol table; pass 2 generates code
- BSA + BUN I implement call and return"""}],

    "Central Processing Unit": [{"title": "Central processing unit" + T, "md": """## General register organisation
- A bank of registers (R1–R7) connected to the ALU through two multiplexers (select A and B buses) and a destination decoder
- Control word (14 bits in Mano): SELA (3) | SELB (3) | SELD (3) | OPR (5) → e.g. R1 ← R2 + R3 → 010 011 001 00010

## Stack organisation
- **Register stack** (64 words, SP 6 bits, FULL and EMTY flags) or **memory stack** (part of memory; SP, often growing downward)
- PUSH: SP ← SP + 1, M[SP] ← DR (register stack); POP: DR ← M[SP], SP ← SP − 1
- Used for subroutine calls, interrupts, expression evaluation (**zero-address** instructions on postfix code)
- Evaluate (3 + 4) × (5 + 6) on a stack: push 3, 4, ADD → 7; push 5, 6, ADD → 11; MUL → **77**

## Instruction formats (X = (A + B) × (C + D))
| Format | Program |
|---|---|
| **Three-address** | ADD R1, A, B · ADD R2, C, D · MUL X, R1, R2 (3 instructions) |
| **Two-address** | MOV R1, A · ADD R1, B · MOV R2, C · ADD R2, D · MUL R1, R2 · MOV X, R1 (6) |
| **One-address** (accumulator) | LOAD A · ADD B · STORE T · LOAD C · ADD D · MUL T · STORE X (7) |
| **Zero-address** (stack) | PUSH A · PUSH B · ADD · PUSH C · PUSH D · ADD · MUL · POP X (8) |
- Fewer addresses → shorter instructions but longer programs; RISC uses load/store with three registers

## Addressing modes (effective address EA)
| Mode | EA / operand | Example |
|---|---|---|
| **Implied** | operand implied by the opcode | CMA, stack ops |
| **Immediate** | operand is in the instruction | MOV R1, #5 |
| **Register** | operand in a register | ADD R1, R2 |
| Register indirect | EA = (R) | LOAD (R1) |
| Autoincrement / autodecrement | EA = (R), then R ± 1 | array scanning |
| **Direct** | EA = address field | LOAD 500 |
| **Indirect** | EA = M[address field] | LOAD @500 |
| **Relative** | EA = PC + offset | branches |
| **Indexed** | EA = XR + address field | arrays |
| Base register | EA = base + displacement | relocation |
Worked (Mano): address field 500, PC 202 after fetch, R1 = 400, XR = 100, M[500] = 800, M[702] = 325, M[600] = 900, M[800] = 300, M[400] = 700
→ direct EA 500 (operand 800); immediate operand 500; indirect EA 800 (operand 300); relative EA 702 (325); indexed EA 600 (900); register operand 400; register indirect EA 400 (700)

## Data transfer, manipulation and program control
- Instruction types: data transfer (LOAD, STORE, MOV, PUSH, POP, IN, OUT), arithmetic, logical and bit manipulation, shifts (logical, arithmetic, circular), program control (BR, JMP, SKP, CALL, RET, compare, test)
- **Status flags**: C (carry), S (sign), Z (zero), V (overflow)
- Program interrupts: external (I/O, timer), internal (traps – overflow, divide by zero, invalid opcode), software interrupts (supervisor call)

## RISC vs CISC
| RISC | CISC |
|---|---|
| few, simple instructions; fixed length | many, complex; variable length |
| **load/store** architecture – only LOAD/STORE touch memory | memory operands in many instructions |
| one instruction per cycle, **pipelining** friendly | multi-cycle instructions |
| many registers, register windows (overlapped) | fewer registers |
| hardwired control | microprogrammed control |
| ARM, MIPS, SPARC, RISC-V | Intel x86, VAX, IBM 370 |

## Pipelining (overview)
- k-stage pipeline, n instructions: time = (k + n − 1) cycles vs nk → speed-up = nk/(k + n − 1) → approaches k
  - k = 5, n = 100 → 104 cycles, speed-up ≈ **4.81**
- Hazards: **structural** (resource conflict), **data** (RAW, WAR, WAW – fix by forwarding/bypassing, stalls, compiler reordering), **control/branch** (fix by branch prediction, delayed branch)
- Instruction pipeline stages (5): IF, ID, EX, MEM, WB; arithmetic pipelines (floating-point adder); vector processing, array processors

## Traps
- Zero-address instructions need a stack
- Relative addressing adds the PC; indexed adds an index register
- Pipeline speed-up never exceeds the number of stages"""}],

    "Input-Output Organization": [{"title": "Input-output organisation" + T, "md": """## Peripheral devices
Keyboard, mouse, monitor, printer, magnetic disk/tape; characters in ASCII; I/O devices differ in speed, data format and operating mode from the CPU → need an **interface**

## Input-output interface
- Resolves differences: conversion of signals, synchronisation (speed), data formats, operating modes
- **I/O bus**: data lines, address lines (device select), control lines (commands: control, status, data output, data input)
- **Isolated I/O** (separate I/O instructions and address space – IN/OUT) vs **memory-mapped I/O** (devices share memory addresses; any memory instruction works)
- Interface unit example: ports A and B, control and status registers, chip select, register select lines

## Asynchronous data transfer
- No common clock between units → timing by control signals
- **Strobe control**: one control line (source- or destination-initiated) – no confirmation that data was received
- **Handshaking**: two control lines – **data valid** and **data accepted** (source-initiated) or **ready for data** (destination-initiated) → reliable; timeout detects failures
- **Asynchronous serial transfer**: each character framed with a **start bit (0)**, data bits, optional parity, **stop bit(s) (1)**; line idle at 1
  - 8 data bits + start + 1 stop = 10 bits/char → 1200 baud ≈ 120 characters/s
- UART (universal asynchronous receiver-transmitter); synchronous serial sends blocks with a shared clock

## Modes of transfer
| Mode | How | CPU involvement |
|---|---|---|
| **Programmed I/O** | CPU checks the status flag in a loop | busy waiting, wasteful |
| **Interrupt-initiated I/O** | device interrupts the CPU when ready | CPU free meanwhile, one interrupt per word |
| **DMA** | DMA controller transfers blocks directly between memory and device; CPU gives up the bus (**bus request / bus grant**) | one interrupt per block |
- DMA modes: **burst** (whole block at once), **cycle stealing** (one word per stolen memory cycle); DMA controller registers: address register, word count register, control register
- **I/O processors (IOP) / channels**: dedicated processors running I/O programs (selector, multiplexer channels)

## Priority interrupt
- Decides which device is served first when several interrupt
- **Polling** (software checks devices in priority order – slow)
- **Daisy chaining** (hardware, serial): devices in series along the interrupt-acknowledge line – the device nearest the CPU has the highest priority
- **Parallel priority** interrupt: interrupt register + mask register + **priority encoder** → vector address (VAD)
- Interrupt cycle: push PC, jump to the service routine via the vector; ISR saves registers, services, restores, returns (RTI)
- Vectored vs non-vectored interrupts; maskable vs non-maskable (NMI)

## Serial communication
- Simplex, half-duplex, full-duplex lines; asynchronous (character) vs synchronous (bit-oriented, e.g. HDLC frames with flag 01111110 and bit stuffing)
- Standards: RS-232 (old serial port), USB (serial bus, hot-pluggable), modems for telephone lines

## Traps
- Handshaking uses two control lines; strobe uses one
- In daisy chaining the device closest to the CPU wins
- DMA steals memory cycles, not CPU registers"""}],

    "Memory Hierarchy": [{"title": "Memory hierarchy" + T, "md": """## Hierarchy
Registers → **cache** → **main memory** → auxiliary memory (disk, tape); going down: larger, cheaper per bit, slower. Works because of **locality of reference** – **temporal** (recently used items reused) and **spatial** (nearby items used soon).

## Main memory
- RAM chips (static SRAM, dynamic DRAM) and ROM (bootstrap loader)
- Chip sizing: build 64K × 16 from 2K × 8 chips → (64K/2K) × (16/8) = 32 × 2 = **64 chips**; 64K words need **16 address lines** (11 go to each chip, 5 to a 5 × 32 decoder for chip select)
- Memory address map assigns address ranges to RAM/ROM chips

## Auxiliary memory
- Magnetic disks (tracks, sectors, cylinders; seek + rotational latency + transfer), magnetic tape (sequential), optical disks, SSDs

## Associative memory (content-addressable memory, CAM)
- Accessed by **content**, not address: argument register A, key register K (mask), match register M; all words compared **in parallel**
- Fast search, expensive hardware; used in **TLBs** and cache tag matching

## Cache memory
- Hit ratio h = hits/(hits + misses); **average access time** = h × Tc + (1 − h) × (Tc + Tm) (hierarchical)
  - Tc = 10 ns, Tm = 100 ns, h = 0.9 → 0.9 × 10 + 0.1 × 110 = **20 ns** (simultaneous access: 0.9 × 10 + 0.1 × 100 = 19 ns)
  - AMAT = hit time + miss rate × miss penalty → 1 + 0.05 × 100 = **6 cycles**
- **Mapping** – 32-bit address, 64 KB cache, 32-byte blocks → 2048 lines, offset 5 bits:
| Mapping | Address split | Note |
|---|---|---|
| **Direct** | tag **16** · line **11** · offset 5 | one possible line; simple; conflict misses |
| **4-way set associative** | tag **18** · set 9 · offset 5 | block in any of 4 lines of its set |
| **Fully associative** | tag **27** · offset 5 | any line; needs associative search |
- **Replacement**: LRU, FIFO, random (not needed for direct mapping)
- **Write policies**: **write-through** (update memory every write – simple, more traffic; write buffer) vs **write-back** (update memory only when the block is replaced – **dirty bit**); write-allocate vs no-write-allocate
- Misses: **compulsory** (cold), **capacity**, **conflict**; multi-level caches (L1, L2, L3); split I/D caches

## Virtual memory
- Address space (virtual) larger than memory space (physical); pages (blocks of address space) mapped to frames (blocks of memory)
- Page table (memory or associative); **TLB** caches translations; page fault → OS loads the page
- Replacement algorithms: FIFO, LRU, optimal; working set; thrashing

## Memory management hardware
- Segmentation and paging hardware: logical address = segment + page + word; segment table and page table, base/limit
- **Memory protection**: access rights (read, write, execute), privileged mode, bounds checking
- Relocation, sharing of common programs

## Traps
- Direct mapping needs no replacement algorithm
- Write-back needs a dirty bit
- Associative memory is searched by content in parallel"""}],
}
