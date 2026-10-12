"""Paper 2 · Unit 3 · P2-U3-03 Data Representation and P2-U3-04 Computer Arithmetic (2 topics × 2 sets × 30), with revision NOTES.
References: M. Morris Mano, Computer System Architecture (3rd ed., chs. 3 and 10); IEEE 754-2008.
Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final
key for GTTC 2024 Technician Gr-III CS (booklet C1). KSET/KEA questions come from packs/pyq-p2.json; PGCET answers were worked out by
ExamSim (options read from the page images). The parsed Legislative Council Data Entry Operator P2 key does not match the booklet, so
its answer is marked as worked out by ExamSim. Every conversion, complement, IEEE 754, Hamming, BCD and Booth answer was checked by
computation."""
from p2u7_a import kset, PYQ, GTTC, NOTE

NUMBER_SYSTEMS = [
    kset("KSET 2024 CS&A · Q13"),
    kset("KSET 2025 CS&A · Q11"),
    ("Conversion of decimal number (61)₁₀ to its binary number equivalent is",
     ["(110011)₂", "(11001110)₂", "(111101)₂", "(111100)₂"], 2, "61 = 32 + 16 + 8 + 4 + 1 = 111101₂." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q84"),
    ("Conversion of decimal number 100 to Octal and Hexadecimal is ____ and ____",
     ["123(8), AB(16)", "64(8), 144(16)", "144(8), 64(16)", "74(8), A1(16)"], 2,
     "100 = 1·64 + 4·8 + 4 → 144₈; 100 = 6·16 + 4 → 64₁₆." + NOTE, "PGCET 2024 MCA · Q8"),
    ("Given the following Lists :\nList-I\na. 10101(2)\nb. DAD(16)\nc. One's (complement) of 1101(2)\nd. 401(8)\nList-II\n"
     "i. 6655(8)\nii. 101(16)\niii. 21(10)\niv. 0010(2)\nIdentify the correct match.",
     ["a-ii; b-i; c-iii; d-iv", "a-i; b-ii; c-iv; d-iii", "a-iii; b-i; c-iv; d-ii", "a-iv; b-i; c-ii; d-iii"], 2,
     "10101₂ = 21; DAD₁₆ = 3501 = 6655₈; 1's complement of 1101 = 0010; 401₈ = 257 = 101₁₆." + NOTE, "PGCET 2024 MCA · Q10"),
    ("The one's complement of binary number 101010 is :", ["010110", "010101", "110111", "101011"], 1,
     "Invert every bit: 101010 → 010101." + NOTE, "PGCET 2023 MCA · Q28"),
    ("With respect to Binary, Octal and Hexadecimal number systems:\nS1: Octal and Hexadecimal representation offer compact representation "
     "than binary\nS2: Binary numbers are fundamental in computing and are used at the lowest level in digital system\nWhich of the following is correct?",
     ["Both S1 and S2 are true", "Both S1 and S2 are false", "S1 is true and S2 is false", "S2 is true and S1 is false"], 0,
     "One octal digit = 3 bits, one hex digit = 4 bits, so both are compact; hardware works in binary." + NOTE, "PGCET 2025 MCA · Q37"),
    ("If negative members are stored in 2's complement form, then range of numbers that can be stored in 8 bits is ____",
     ["−127 to +127", "−127 to +128", "−128 to +127", "−128 to +128"], 2, "n-bit 2's complement: −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 = −128 … +127." + NOTE,
     "PGCET 2025 MCA · Q38"),
    ("53 in 2's complement form is ____.", ["1001011", "001010", "0110101", "001011"], 2,
     "A positive number is the same in 2's complement: 53 = 110101, with a 0 sign bit → 0110101." + NOTE, "PGCET 2025 MCA · Q39"),
    ("Decimal equivalent of the 763.4₍₈₎ is ____.", ["499.5", "499", "49.95", "459.9"], 0,
     "7·64 + 6·8 + 3 + 4/8 = 448 + 48 + 3 + 0.5 = 499.5." + NOTE, "PGCET 2025 MCA · Q40"),
    ("The magnitude of the binary number 10111011 in 1's complement and 2's complement representation are ____ and ____ respectively.",
     ["−69, −68", "−68, −69", "−59, −58", "−58, −59"], 1,
     "Sign bit 1. 1's complement: invert → 01000100 = 68 → −68. 2's complement: invert + 1 → 01000101 = 69 → −69." + NOTE, "PGCET 2025 MCA · Q41"),
    ("1's and 2's complement of −24₍₁₀₎ in binary are ____ and ____.",
     ["100111, 101000", "011000, 011001", "101000, 100111", "011001, 011000"], 0,
     "24 = 011000 (6 bits); invert → 100111 (1's complement); add 1 → 101000 (2's complement)." + NOTE, "PGCET 2025 MCA · Q42"),
    ("Which of the following are valid hexadecimal numbers?\n(i) 1A3F\n(ii) 29GF\n(iii) FF12\n(iv) 7BHE",
     ["(i), (ii) and (iv)", "(i), (ii) and (iii)", "(i) and (iii)", "(i), (iii) and (iv)"], 2,
     "Hex digits are 0–9 and A–F; G and H are not allowed." + NOTE, "PGCET 2026 MCA · Q44"),
    ("The decimal number 25₁₀ is represented in binary as ____", ["1 1 0 0 1", "1 0 1 0 1", "1 1 1 0 0", "1 0 0 1 1"], 0,
     "25 = 16 + 8 + 1 = 11001." + NOTE, "PGCET 2026 MCA · Q45"),
    ("Arrange the following steps in correct order to binary:\n(i) Repeat division until becomes 0\n(ii) Divide the number by 2\n"
     "(iii) Write the remainder\n(iv) Write the remainder in reverse order",
     ["(i) → (ii) → (iii) → (iv)", "(ii) → (iii) → (i) → (iv)", "(iii) → (i) → (iv) → (ii)", "(iv) → (ii) → (iii) → (i)"], 1,
     "Divide by 2, note the remainder, repeat until the quotient is 0, then read the remainders bottom-up." + NOTE, "PGCET 2026 MCA · Q46"),
    ("Arrange the steps to find two's complement of a binary number.\n(i) Take 1's complement\n(ii) Write the binary number\n(iii) Add 1\n(iv) Obtain final result",
     ["(iv) → (i) → (iii) → (ii)", "(ii) → (iii) → (i) → (iv)", "(ii) → (i) → (iii) → (iv)", "(i) → (ii) → (iii) → (iv)"], 2,
     "Write the number, invert it, add 1, read the result." + NOTE, "PGCET 2026 MCA · Q49"),
    ("The 2's complement of 101000 is", ["011000", "010101", "010111", "000111"], 0,
     "Invert → 010111, add 1 → 011000 (shortcut: copy bits up to the first 1 from the right, invert the rest)." + NOTE,
     "Legislative Council 2024 Data Entry Operator P2 · Q85"),
    ("The base (radix) of the hexadecimal number system is", ["16", "8", "10", "2"], 0, "Digits 0–9 and A–F."),
    ("(1011.101)₂ in decimal is", ["11.625", "11.5", "13.625", "11.75"], 0, PYQ + "8 + 2 + 1 = 11; .101 = 0.5 + 0.125 = 0.625."),
    ("The binary number 11010110 in hexadecimal is", ["D6", "6D", "D5", "C6"], 0, "Group in fours from the right: 1101 0110 = D 6."),
    ("The octal number 725 in binary is", ["111010101", "111001101", "110010101", "111010110"], 0, "Each octal digit → 3 bits: 7 = 111, 2 = 010, 5 = 101."),
    ("The decimal fraction 0.625 in binary is", ["0.101", "0.011", "0.110", "0.1001"], 0,
     PYQ + "Multiply by 2: 1.25 → 1, 0.5 → 0, 1.0 → 1, giving 0.101."),
    ("The 9's complement of the decimal number 5307 is", ["4692", "4693", "5307", "4793"], 0, "Subtract each digit from 9: 9999 − 5307 = 4692."),
    ("The 10's complement of the decimal number 2470 is", ["7530", "7529", "2470", "8530"], 0, "10⁴ − 2470 = 7530 (= 9's complement 7529 + 1)."),
    ("Which representations of signed binary numbers have two representations of zero (+0 and −0)?",
     ["Signed-magnitude and 1's complement", "2's complement", "Excess-3 code", "Gray code"], 0,
     PYQ + "2's complement has a single zero, which is why it is used in hardware."),
    ("−18 in 8-bit 2's complement is", ["11101110", "10010010", "11101101", "01101110"], 0,
     "18 = 00010010; invert → 11101101; add 1 → 11101110. (10010010 is signed-magnitude.)"),
    ("The 8-bit 2's complement number 10000000 represents", ["−128", "−0", "+128", "−127"], 0, "It is the most negative value; it has no positive counterpart."),
    ("Sign-extending the 4-bit 2's complement number 1011 to 8 bits gives", ["11111011", "00001011", "10001011", "10110000"], 0,
     "Copy the sign bit into the new high-order positions; the value (−5) is unchanged."),
    ("The hexadecimal number 2F in decimal is", ["47", "45", "32", "63"], 0, "2·16 + 15 = 47."),
    ("The largest unsigned number that can be stored in 12 bits is", ["4095", "4096", "2047", "1023"], 0, PYQ + "2¹² − 1 = 4095 (FFF₁₆)."),
]

FLOAT_CODES = [
    ("Given the following Lists :\nList-I\na. BCD code\nb. EBCDIC\nc. ASCII\nd. Unicode\nList-II\n"
     "i. Code used for encoding characters in IBM mainframe systems\nii. Codes widely used for character encoding standard for electronic communication\n"
     "iii. Universal character encoding standard that can represent virtually all written languages\niv. Code used to represent decimal digits in binary form\n"
     "Identify the correct match.",
     ["a-iii; b-iv; c-i; d-ii", "a-iv; b-i; c-ii; d-iii", "a-iv; b-iii; c-ii; d-i", "a-i; b-ii; c-iii; d-iv"], 1,
     "BCD – decimal digits; EBCDIC – IBM mainframes; ASCII – communication standard; Unicode – all scripts." + NOTE, "PGCET 2024 MCA · Q11"),
    ("A floating-point number is said to be normalized, if the MSB (Most Significant Bit) of the mantissa is ____.", ["−1", "0", "1", "2"], 2,
     "Normalization shifts the mantissa until its most significant bit is 1 (no leading zeros)." + NOTE, "PGCET 2024 MCA · Q12"),
    ("In floating-point representation, the part that represents a signed and fixed-point number, and the position of the decimal point are called as ____ and ____",
     ["Mantissa, Exponent", "Exponent, Mantissa", "Float, Exponent", "Mantissa, Float"], 0,
     "m × rᵉ: the mantissa holds the signed fixed-point number, the exponent gives the position of the point (Mano, ch. 3)." + NOTE, "PGCET 2024 MCA · Q14"),
    ("A floating point number typically consists of\n(i) Sign bit\n(ii) Parity bit\n(iii) Mantissa (Significand)\n(iv) Exponent",
     ["(i), (ii) and (iv)", "(i), (iii) and (iv)", "(ii), (iii) and (iv)", "(i), (ii) and (iii)"], 1, "A parity bit is an error-detection bit, not part of the number." + NOTE,
     "PGCET 2026 MCA · Q48"),
    ("Match the Characters in List-I with their correct ASCII Property in List-II.\n(a) 'A'\n(b) 'a'\n(c) '0' (Zero)\n(d) ' ' (Space)\n"
     "(i) ASCII 32 (Decimal)\n(ii) ASCII 48 (Decimal)\n(iii) ASCII 65 (Decimal)\n(iv) ASCII differ from (i) by 32",
     ["a – i, b – iii, c – iv, d – ii", "a – i, b – iv, c – iii, d – ii", "a – iii, b – iv, c – i, d – ii", "a – iii, b – iv, c – ii, d – i"], 3,
     "'A' = 65, 'a' = 97 (32 more than 'A'), '0' = 48, space = 32." + NOTE, "PGCET 2026 MCA · Q47"),
    ("A computer uses 8 bit unsigned fixed-point representation with 4 bits for integer and 4 bits for fraction. What is the largest number it can represent?",
     ["15.9375", "16", "15.5", "31.875"], 0, "1111.1111₂ = 15 + 15/16 = 15.9375." + NOTE, "PGCET 2026 CS · Q24"),
    ("Which of the following is NOT a type of computer code?", ["ASCI", "EDIC", "EBCDIC", "Gray code"], 1,
     "ASCII, EBCDIC and Gray code are codes; 'EDIC' is not." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q72"),
    ("Which among the following is correct about 85₁₀ equivalent 4-bit BCD code?", ["0111 0110", "1000 0101", "10000011", "0010 0101"], 1,
     "Each decimal digit is coded separately: 8 = 1000, 5 = 0101." + NOTE, "PGCET 2025 MCA · Q36"),
    ("Data types found in the registers of digital computers are classified as",
     ["Numbers for arithmetic, letters of the alphabet and other discrete symbols", "Integers alone", "Characters alone", "Floating-point numbers alone"], 0,
     "Mano, ch. 3: all are coded in binary."),
    ("In fixed-point representation, the binary point is",
     ["At an assumed fixed position – the extreme right for integers or the extreme left for fractions", "Stored explicitly with every number",
      "Moved by an exponent field", "Marked by a separate flag bit"], 0, PYQ + "Only floating point stores a movable point (the exponent)."),
    ("In IEEE 754 single precision (32 bits), the sign, exponent and fraction fields have", ["1, 8 and 23 bits", "1, 11 and 52 bits", "1, 7 and 24 bits", "1, 8 and 24 bits"], 0,
     PYQ + "The leading 1 of a normalized number is hidden, giving 24 bits of precision."),
    ("The exponent bias used in IEEE 754 single precision is", ["127", "128", "1023", "255"], 0, "Stored exponent = true exponent + 127 (2ᵏ⁻¹ − 1 with k = 8)."),
    ("IEEE 754 double precision (64 bits) uses an exponent bias of", ["1023", "127", "2047", "511"], 0, "11-bit exponent: 2¹⁰ − 1 = 1023; 52-bit fraction."),
    ("The decimal number 5.75 in IEEE 754 single precision (hex) is", ["40B80000", "40A80000", "C0B80000", "40B00000"], 0,
     "5.75 = 101.11 = 1.0111 × 2²; exponent 2 + 127 = 129 = 10000001; bits 0 10000001 0111000… = 40B80000."),
    ("The IEEE 754 single-precision pattern C1200000 (hex) represents", ["−10.0", "−1.25", "+10.0", "−20.0"], 0,
     "Sign 1; exponent 10000010 = 130 → 2³; fraction .01 → 1.25; value = −1.25 × 8 = −10."),
    ("Compared with fixed point of the same word length, floating-point representation gives",
     ["A much wider range of values, at the cost of precision", "Exact representation of every real number", "Faster integer addition",
      "A smaller range but more precision"], 0, "The exponent extends the range; the mantissa width limits precision."),
    ("The even-parity bit for the 7-bit message 1011001 is", ["0", "1", "Two parity bits are needed", "It cannot be decided"], 0,
     PYQ + "The message already has four 1s (even), so P = 0."),
    ("The odd-parity bit for the 7-bit message 1101010 is", ["1", "0", "Two parity bits are needed", "It cannot be decided"], 0,
     "Four 1s – one more 1 makes the total odd."),
    ("A single parity bit can", ["Detect any odd number of bit errors but cannot correct them", "Detect any two-bit error",
                               "Detect every burst error", "Detect and correct single-bit errors"], 0, "Two flipped bits leave the parity unchanged."),
    ("How many check bits does a Hamming code need to correct single-bit errors in 4 data bits?", ["3", "2", "4", "1"], 0,
     PYQ + "2ᵖ ≥ m + p + 1 → p = 3 for m = 4: the (7, 4) Hamming code."),
    ("How many check bits does a Hamming code need for single-error correction of 8 data bits?", ["4", "3", "5", "8"], 0,
     "2ᵖ ≥ 8 + p + 1: p = 3 gives 8 < 12, p = 4 gives 16 ≥ 13 → 4 (12-bit code word)."),
    ("To correct up to t bit errors, a code needs a minimum Hamming distance of", ["2t + 1", "t + 1", "2t", "t"], 0,
     "To detect d errors the minimum distance is d + 1."),
    ("The Hamming distance between 10110 and 11011 is", ["3", "2", "4", "1"], 0, "XOR = 01101 → three 1s."),
    ("The Excess-3 code of the decimal digit 5 is", ["1000", "0101", "0111", "1001"], 0, "5 + 3 = 8 = 1000."),
    ("Which decimal code is self-complementing (its 9's complement is obtained by inverting the bits)?", ["Excess-3", "8421 BCD", "Gray code", "ASCII"], 0,
     PYQ + "Also 2421 code; 8421 BCD is not self-complementing."),
    ("The Gray code of the binary number 0110 is", ["0101", "0110", "0111", "0011"], 0, "g₃ = b₃; gᵢ = bᵢ₊₁ ⊕ bᵢ → 0, 1, 0, 1."),
    ("Standard ASCII is a", ["7-bit code with 128 characters", "8-bit code with 256 characters", "6-bit code with 64 characters", "16-bit code with 65,536 characters"], 0,
     "Extended ASCII and EBCDIC use 8 bits."),
    ("UTF-8 encodes one Unicode character in", ["1 to 4 bytes", "Exactly 2 bytes", "Exactly 4 bytes", "7 bits"], 0, "ASCII characters take one byte in UTF-8."),
    ("Which error-detection method divides the data by a generator polynomial and appends the remainder?",
     ["Cyclic redundancy check (CRC)", "Single parity", "One's-complement checksum", "Two-out-of-five code"], 0, "The receiver divides again; a non-zero remainder means an error."),
    ("In packed BCD, one byte holds", ["Two decimal digits", "One decimal digit", "One ASCII character", "Eight decimal digits"], 0,
     "Unpacked BCD uses one byte per digit."),
]

ADD_SUB = [
    kset("KEA 2026 CS Paper-2 · Q32"),
    ("The sum of the binary numbers 10110.10 and 11010.01 is", ["48", "48.5", "48.75", "48.25"], 2,
     "22.5 + 26.25 = 48.75 (110000.11₂)." + NOTE, "PGCET 2026 MCA · Q17"),
    ("In 2's complement addition, overflow is detected when", ["The carry into the sign bit differs from the carry out of it",
                                                               "There is a carry out of the sign bit", "Both operands are negative", "The result is zero"], 0,
     PYQ + "V = Cₙ ⊕ Cₙ₋₁; an end carry alone is not an overflow."),
    ("In 8-bit 2's complement, adding 01110000 and 01010000 gives", ["An overflow – the result 11000000 looks negative", "+192 with no overflow",
                                                                     "An underflow", "A correct result with an end carry"], 0,
     "112 + 80 = 192 > 127: two positives give a negative-looking sum."),
    ("Overflow cannot occur in 2's complement when", ["A positive and a negative number are added", "Two positive numbers are added",
                                                       "Two negative numbers are added", "A negative number is subtracted from a positive one"], 0,
     "The sum of opposite signs always lies between the two operands."),
    ("Subtraction A − B in 2's complement hardware is done as", ["A + (2's complement of B)", "A + B'", "B + (2's complement of A)", "A − B with a borrow chain only"], 0,
     "The adder-subtractor complements B with XOR gates and sets the input carry to 1."),
    ("In 1's complement addition, a carry out of the sign bit is", ["Added back to the least significant bit (end-around carry)", "Discarded",
                                                                   "Treated as overflow", "Used to complement the result"], 0, PYQ + "In 2's complement the end carry is discarded."),
    ("In 2's complement addition, a carry out of the sign-bit position is", ["Discarded", "Added to the LSB", "Always an overflow", "Stored as the sign"], 0,
     "Overflow is decided by comparing the last two carries, not by the end carry."),
    ("In signed-magnitude addition, when the two signs differ, the hardware",
     ["Subtracts the smaller magnitude from the larger and gives the result the sign of the larger", "Adds the magnitudes and keeps the sign of A",
      "Adds the magnitudes and takes the sign of B", "Complements both numbers and adds them"], 0, "Mano, ch. 10 (addition/subtraction algorithm)."),
    ("7 − 5 in 4-bit 2's complement (0111 + 1011) gives", ["0010, with the end carry discarded", "1010", "0011", "1100"], 0, "0111 + 1011 = 1 0010 → 0010 = +2."),
    ("(−3) + (−4) in 4-bit 2's complement (1101 + 1100) gives", ["1001 = −7, no overflow", "0111 = +7", "1001 with overflow", "1000 = −8"], 0,
     "1101 + 1100 = 1 1001; carries into and out of the sign are both 1, so no overflow."),
    ("(+5) + (+4) in 4-bit 2's complement gives", ["An overflow – the result 1001 reads as −7", "0101", "1001 = +9 with no overflow", "An underflow"], 0,
     PYQ + "+9 is outside −8 … +7."),
    ("When adding the BCD digits 0111 and 0101, the correction step is", ["Add 0110, because the binary sum 1100 is greater than 1001", "Subtract 0110",
                                                                          "No correction is needed", "Add 0011"], 0,
     PYQ + "7 + 5 = 12: 1100 + 0110 = 1 0010 → digits 1 and 2."),
    ("The BCD sum of 0101 1000 (58) and 0011 0100 (34) is", ["1001 0010", "1000 1100", "1001 1100", "0101 1100"], 0,
     "Low digit 8 + 4 = 12 → 0010 with carry; high digit 5 + 3 + 1 = 9 → 92."),
    ("In a 4-bit adder-subtractor, subtraction (M = 1) is obtained by", ["XOR gates complementing the B inputs and an input carry of 1", "AND gates on the A inputs",
                                                                         "A decoder on the outputs", "Setting the input carry to 0 and leaving B unchanged"], 0,
     "A + B' + 1 = A − B."),
    ("In a carry look-ahead adder, the generate and propagate terms are", ["Gᵢ = AᵢBᵢ and Pᵢ = Aᵢ ⊕ Bᵢ", "Gᵢ = Aᵢ + Bᵢ and Pᵢ = AᵢBᵢ",
                                                                           "Gᵢ = Aᵢ ⊕ Bᵢ and Pᵢ = AᵢBᵢ", "Gᵢ = Aᵢ'Bᵢ and Pᵢ = AᵢBᵢ'"], 0, "Cᵢ₊₁ = Gᵢ + PᵢCᵢ."),
    ("The main drawback of a ripple-carry adder is", ["The carry must pass through every stage, so delay grows with the number of bits",
                                                     "It cannot add negative numbers", "It needs a clock", "It uses more gates than a carry look-ahead adder"], 0,
     "Carry look-ahead removes this at the cost of more gates."),
    ("BCD subtraction is commonly done by adding the", ["9's or 10's complement of the subtrahend", "1's complement of the minuend",
                                                        "Gray code of the subtrahend", "Excess-3 code of the result"], 0, "Same idea as r's / (r−1)'s complement subtraction."),
    ("After the ALU computes A − B with A equal to B, the status bit that becomes 1 is", ["Z (zero)", "V (overflow)", "S (sign)", "I (interrupt enable)"], 0,
     "The result is all 0s."),
    ("For unsigned numbers, A − B is computed as A + B' + 1. An end carry of 1 means", ["A ≥ B", "A < B", "Overflow", "The result is negative"], 0,
     PYQ + "No end carry means A < B and the result is the 2's complement of B − A."),
    ("(+9) − (+13) in signed-magnitude form gives", ["−4 (sign 1, magnitude 0100)", "+4", "−22", "+22"], 0, "Magnitudes subtracted, sign of the larger (13)."),
    ("In 8-bit 2's complement, (−100) + (−50)", ["Overflows, because −150 is below −128", "Gives −150 with no overflow", "Gives an exponent underflow",
                                                 "Needs an end-around carry"], 0, "Two negatives give a positive-looking result."),
    ("An arithmetic shift-left of a 2's complement number", ["Multiplies it by 2, with overflow if the sign bit changes", "Divides it by 2",
                                                             "Keeps the sign bit and shifts in 1s", "Is the same as a circular shift"], 0, "Mano: overflow flip-flop Vs = R₇ ⊕ R₆ before the shift."),
    ("Arithmetic shift-right of 11110100 (−12) gives", ["11111010 (−6)", "01111010 (+122)", "11101000 (−24)", "11111011 (−5)"], 0,
     "The sign bit is copied, so the value is halved."),
    ("Adding two 4-digit BCD numbers in parallel needs", ["Four BCD adder stages, one per digit", "One 16-bit binary adder with no correction",
                                                         "Two BCD adder stages", "Eight full adders only"], 0, "Each stage is a 4-bit adder + correction logic."),
    ("In 8-bit 2's complement, the 2's complement of 00000000 is", ["00000000 (the end carry is dropped)", "11111111", "10000000", "00000001"], 0,
     "Zero has a single representation."),
    ("The hexadecimal sum 3A + 2F is", ["69", "59", "6A", "5F"], 0, "58 + 47 = 105 = 69₁₆."),
    ("The binary difference 1101 − 0110 is", ["0111", "0110", "1011", "1001"], 0, "13 − 6 = 7."),
    ("Using 9's complement, 832 − 457 equals", ["375", "374", "1375", "425"], 0, "832 + 542 = 1374; end-around carry: 374 + 1 = 375."),
    ("In Mano's signed-magnitude add/subtract algorithm, a result of −0 is avoided by", ["Clearing the sign bit when the magnitude of the result is zero",
                                                                                       "Adding 1 to the result", "Switching to 1's complement", "Ignoring the overflow bit"], 0,
     "The flowchart sets As = 0 when A = 0."),
]

MUL_DIV = [
    kset("KSET 2024 CS&A · Q12"),
    ("The result of 101₂ × 10₂ is ____.", ["1010₂", "1000₂", "1110₂", "1100₂"], 0, "5 × 2 = 10 = 1010₂ (multiplying by 10₂ is a left shift)." + NOTE,
     "PGCET 2026 MCA · Q50"),
    ("In Booth's algorithm, when the bit pair (Qₙ, Qₙ₊₁) is (1, 0), the step is",
     ["Subtract the multiplicand (add its 2's complement), then arithmetic shift right", "Add the multiplicand, then shift", "Shift only",
      "Shift left and add"], 0, PYQ + "10 = start of a string of 1s; 01 = end of the string (add); 00 and 11 = shift only."),
    ("In Booth's algorithm, when the bit pair (Qₙ, Qₙ₊₁) is (0, 1), the step is",
     ["Add the multiplicand to the partial product, then arithmetic shift right", "Subtract the multiplicand, then shift", "Shift only",
      "Complement the partial product"], 0, "The string of 1s has ended."),
    ("The main advantage of Booth's algorithm is that it", ["Multiplies signed 2's complement numbers directly and skips over strings of 1s",
                                                            "Works only for unsigned numbers", "Needs no shifting", "Uses repeated division"], 0,
     "A string of 1s from 2ᵏ to 2ᵐ is handled as 2ᵏ⁺¹ − 2ᵐ."),
    ("The Booth recoding of the multiplier 01110 (with an implied 0 to its right) is", ["+1 0 0 −1 0", "0 +1 +1 +1 0", "+1 0 0 +1 0", "−1 0 0 +1 0"], 0,
     "Digit i = bᵢ₋₁ − bᵢ: 16 − 2 = 14 = 01110."),
    ("For the multiplier 01110, Booth's algorithm performs how many additions/subtractions?", ["2", "3", "4", "1"], 0,
     "One subtraction where the string of 1s starts, one addition where it ends."),
    ("Booth's algorithm performs the most additions/subtractions when the multiplier", ["Has alternating 0s and 1s (e.g. 010101…)", "Is all 1s", "Is all 0s",
                                                                                      "Is a power of two"], 0, PYQ + "Every bit pair is 01 or 10."),
    ("Multiplying two n-bit numbers gives a product of at most", ["2n bits", "n bits", "n + 1 bits", "n² bits"], 0, "E.g. 4-bit × 4-bit: 15 × 15 = 225 needs 8 bits."),
    ("In Mano's hardware multiply algorithm, the sequence counter SC is initially set to", ["The number of bits in the multiplier", "Zero",
                                                                                           "The number of 1s in the multiplier", "Twice the word length"], 0,
     "One add-and-shift cycle per multiplier bit."),
    ("A combinational array multiplier for two 4-bit numbers needs how many AND gates to form the partial products?", ["16", "8", "4", "32"], 0,
     "Every bit of one number ANDed with every bit of the other: 4 × 4."),
    ("Booth multiplication of 0111 (+7) by 1101 (−3) gives the 8-bit product", ["11101011 (−21)", "00010101 (+21)", "11101010", "10010101"], 0,
     "21 = 00010101 → 2's complement 11101011."),
    ("In restoring division, when the partial remainder becomes negative after subtracting the divisor, the hardware",
     ["Adds the divisor back and records a quotient bit of 0", "Records a quotient bit of 1", "Shifts the quotient right", "Uses Booth recoding"], 0,
     "Non-restoring division avoids this extra addition."),
    ("Non-restoring division differs from restoring division because it", ["Skips the restore step: a negative remainder is shifted and the divisor is added in the next step",
                                                                           "Adds the divisor twice in every step", "Needs no quotient bits",
                                                                           "Works only for floating-point numbers"], 0, "Each step is one add or one subtract."),
    ("In Mano's division algorithm, divide overflow occurs when", ["The upper half of the dividend is greater than or equal to the divisor",
                                                                    "The divisor is negative", "The quotient is zero", "The dividend is odd"], 0,
     PYQ + "The quotient would not fit in n bits."),
    ("In Mano's division hardware, the divide-overflow flip-flop DVF is set when", ["The quotient would need more bits than the register, e.g. division by zero",
                                                                                     "The remainder is zero", "The dividend is negative", "The divisor is one"], 0,
     "The operation is stopped and DVF signals the error."),
    ("In signed-magnitude multiplication or division, the sign of the result is", ["As ⊕ Bs", "As", "Bs", "As · Bs"], 0, "Like signs give +, unlike signs give −."),
    ("The binary division 0111 ÷ 0010 gives", ["Quotient 0011, remainder 0001", "Quotient 0010, remainder 0011", "Quotient 0011, remainder 0000",
                                               "Quotient 0100, remainder 0001"], 0, "7 ÷ 2 = 3 remainder 1."),
    ("Floating-point multiplication is done by", ["Multiplying the mantissas and adding the exponents (subtracting one bias)",
                                                  "Adding the mantissas and multiplying the exponents", "Aligning the exponents and adding the mantissas",
                                                  "Dividing the mantissas and subtracting the exponents"], 0, PYQ + "The product is then normalized."),
    ("Before floating-point addition, the exponents are equalized by", ["Shifting the mantissa of the number with the smaller exponent to the right",
                                                                        "Shifting the larger number's mantissa left", "Adding the exponents",
                                                                        "Setting both exponents to zero"], 0, "Then the mantissas are added and the result normalized."),
    ("Floating-point division is done by", ["Subtracting the exponents (adding the bias back) and dividing the mantissas", "Adding the exponents",
                                            "Multiplying the mantissas", "Subtracting the mantissas"], 0, "The divisor's mantissa must not be zero."),
    ("Shifting the mantissa left and decrementing the exponent until the first significant bit is 1 is called", ["Normalization", "Biasing", "Truncation", "Rounding to zero"], 0,
     "It keeps the maximum number of significant bits."),
    ("Extra bits kept to the right of the mantissa during floating-point arithmetic to reduce rounding error are called", ["Guard bits", "Parity bits", "Sign bits", "Bias bits"], 0,
     "IEEE 754 uses guard, round and sticky bits."),
    ("Multiplying an unsigned binary number by 8 can be done by", ["Shifting it left by 3 positions", "Shifting it right by 3 positions", "Shifting it left by 8 positions",
                                                                   "Adding it to itself three times"], 0, "8 = 2³."),
    ("Booth's algorithm applied to M = 0101 and Q = 0110 gives the 8-bit product", ["00011110", "00011010", "00110000", "11100010"], 0, "5 × 6 = 30 = 00011110."),
    ("Bit-pair recoding (modified Booth / radix-4) of the multiplier", ["Halves the number of partial products by scanning three bits at a time", "Doubles the number of partial products",
                                                                        "Works only for unsigned numbers", "Removes the need for shifting"], 0, "Digits are 0, ±1, ±2."),
    ("A Wallace tree speeds up multiplication by", ["Adding the partial products with layers of carry-save adders", "Using Booth recoding only",
                                                    "Using one ripple adder for each row", "Repeated subtraction"], 0, "Only the final two rows need a carry-propagate adder."),
    ("At the end of non-restoring division, if the final remainder is negative", ["The divisor is added once to correct the remainder", "The quotient is complemented",
                                                                                  "Nothing is done", "The dividend is added back"], 0, "The quotient bits are already correct."),
    ("Dividing a 2n-bit dividend by an n-bit divisor by the restoring method needs how many shift-and-subtract cycles?", ["n", "2n", "n/2", "n²"], 0,
     "One quotient bit per cycle."),
    ("Booth's algorithm needs which extra flip-flop next to the multiplier register?", ["Qₙ₊₁, an appended bit that starts at 0", "A carry look-ahead flip-flop",
                                                                                        "A parity flip-flop", "The divide-overflow flip-flop"], 0,
     "Qₙ and Qₙ₊₁ are inspected in every step."),
]

TOPICS = {
    "Data Representation": [
        ("1 · Data Types, Number Systems, Conversion and Complements", NUMBER_SYSTEMS),
        ("2 · Fixed and Floating Point Representation, Codes and Error Detection", FLOAT_CODES),
    ],
    "Computer Arithmetic": [
        ("1 · Addition and Subtraction – Signed Magnitude, 2's Complement, Overflow and BCD", ADD_SUB),
        ("2 · Multiplication (Booth's Algorithm) and Division Algorithms", MUL_DIV),
    ],
}

NOTES = {
    "Data Representation": [{"title": "Data representation – revision sheet", "md": """## Number systems
| Base | Digits | Group of bits |
|---|---|---|
| Binary 2 | 0 1 | – |
| Octal 8 | 0–7 | 3 |
| Decimal 10 | 0–9 | – |
| Hex 16 | 0–9 A–F | 4 |
- Decimal → base r: divide by r, read remainders bottom-up; fractions: multiply by r, read the integer parts top-down (0.625 = 0.101₂)
- Worked: 100 = 144₈ = 64₁₆; 1234 = 4D2₁₆ = 2322₈; F3E₁₆ = 3902; 763.4₈ = 499.5; DAD₁₆ = 3501 = 6655₈

## Complements (r's and (r−1)'s)
- (r−1)'s: subtract each digit from r−1 (9's of 5307 = 4692; 1's = invert bits)
- r's = (r−1)'s + 1 (10's of 2470 = 7530; 2's = invert + 1; shortcut: copy up to the first 1 from the right, invert the rest)
- Signed numbers: signed-magnitude and 1's complement have **+0 and −0**; 2's complement has one zero
- n-bit 2's complement range **−2ⁿ⁻¹ … 2ⁿ⁻¹−1** (8 bits: −128 … +127); 1's complement / signed magnitude: −127 … +127
- −18 = 11101110; 10000000 = −128; sign extension copies the sign bit

## Fixed and floating point
- Fixed point: point assumed at the right (integers) or left (fractions); 4.4 unsigned max = 15.9375
- Floating point m × rᵉ; **normalized** = mantissa MSB is 1
- IEEE 754 single: 1 + 8 + 23, bias 127; double: 1 + 11 + 52, bias 1023; hidden leading 1
- 5.75 = 40B80000; C1200000 = −10.0

## Codes and error detection
- BCD 8421 (85 = 1000 0101); packed BCD = 2 digits/byte; Excess-3 = BCD + 3 (self-complementing); 2421 self-complementing
- Gray code: one bit changes between successive values; ASCII 7-bit (A = 65, a = 97, 0 = 48, space = 32); EBCDIC 8-bit (IBM); Unicode/UTF-8 1–4 bytes
- Parity detects odd numbers of errors; Hamming: 2ᵖ ≥ m + p + 1 (4 data → 3 check, 8 data → 4); detect d errors: distance d + 1; correct t: 2t + 1
- CRC: divide by a generator polynomial, append the remainder
"""}],
    "Computer Arithmetic": [{"title": "Computer arithmetic – revision sheet", "md": """## Addition and subtraction
- 2's complement: A − B = A + B' + 1; **discard** the end carry
- 1's complement: **end-around carry** (add the carry back to the LSB)
- **Overflow** V = Cₙ ⊕ Cₙ₋₁ – only when both operands have the same sign and the result's sign differs; never for opposite signs
- Signed magnitude: same signs → add magnitudes; different signs → subtract smaller from larger, sign of the larger; clear the sign for a zero result
- Unsigned A − B: end carry 1 → A ≥ B
- BCD addition: if the 4-bit sum > 9 or a carry occurs, **add 0110**
- Carry look-ahead: Gᵢ = AᵢBᵢ, Pᵢ = Aᵢ ⊕ Bᵢ, Cᵢ₊₁ = Gᵢ + PᵢCᵢ; ripple adder delay grows with n
- Arithmetic shift left = ×2 (overflow if the sign changes); arithmetic shift right = ÷2 (sign copied)

## Multiplication
- n × n bits → 2n-bit product; shift-and-add: one cycle per multiplier bit (SC = n)
- **Booth** (signed 2's complement): look at Qₙ Qₙ₊₁ (Qₙ₊₁ starts at 0)
  - 10 → subtract M, then ASHR; 01 → add M, then ASHR; 00 / 11 → ASHR only
  - recoding 01110 → +1 0 0 −1 0; worst case: alternating 0101…
- Bit-pair (radix-4) Booth halves the partial products; Wallace tree = carry-save adders; array multiplier n × n AND gates

## Division
- Restoring: subtract; if negative, add the divisor back (quotient bit 0)
- Non-restoring: no restore – next step adds the divisor; final correction if the remainder is negative
- Divide overflow (DVF): upper half of dividend ≥ divisor (e.g. ÷ 0)
- Sign of product/quotient = As ⊕ Bs

## Floating-point arithmetic
- Add/subtract: align (shift the smaller exponent's mantissa right), add, normalize
- Multiply: add exponents (subtract one bias), multiply mantissas, normalize
- Divide: subtract exponents (add the bias), divide mantissas
- Guard bits reduce rounding error
"""}],
}
