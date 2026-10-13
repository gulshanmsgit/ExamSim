"""KRIES Computer Teacher · Data Structures · P2-KRD-01 Introduction to Data Structures and P2-KRD-02 Primitive Data Structures
(2 topics × 3 sets × 30), with revision NOTES. Owner's request (14 Oct 2026): one topic per heading of the KRIES Data Structures syllabus,
previous-year and previous-year-pattern questions, as for C Programming. Set 2 of Introduction PULLS the GPSTR 'Time and Space Complexity'
set (tools/p2u8_d.py – repeats by design, see REUSE in check_packs.py). Real previous-year questions keep their exact wording, printed option
order and `source`. Official answers: KEA final keys for GTTC 2024 (Technician Gr-III CS – C1). KSET/KEA questions come from
packs/pyq-p2.json; PGCET answers were worked out by ExamSim; the parsed Legislative Council Data Entry Operator P2 key does not match the
booklet, so its answer is marked as worked out by ExamSim. Sizes assume 4-byte int, 1-byte char, ASCII and a 64-bit system."""
from p2u8_d import COMPLEXITY
from p2u7_a import kset, PYQ, GTTC, NOTE

DS_BASICS = [
    ("Which of the following is a linear data structure?", ["Tree", "Graph", "Stack", "Hash table"], 2, "Stack elements form a sequence." + NOTE,
     "Legislative Council 2024 Data Entry Operator P2 · Q72"),
    ("To represent hierarchical relationship between elements, which data structure is suitable?", ["Dequeue", "Priority", "Tree", "Graph"], 2,
     "A tree models parent–child hierarchy." + NOTE, "PGCET 2023 M.Tech CS · Q8"),
    kset("KEA 2026 CS Paper-2 · Q3"),
    kset("KEA 2026 CS Paper-2 · Q4"),
    kset("KEA 2026 CS Paper-2 · Q12"),
    ("____ is a method used to encode information into a format that can be used and understood by computer system.", ["Data structure", "Data definition",
                                                                                                                       "Data representation", "Data crunching"], 2,
     "Data representation = how information is coded (binary, ASCII, floating point …)." + NOTE, "PGCET 2025 MCA · Q34"),
    ("Consider a linked list, visiting each element of the linked list is known as", ["Sorting", "Merging", "Traversal", "Inserting"], 2,
     "Traversal = visiting every element once." + NOTE, "PGCET 2026 CS · Q2"),
    ("What is the time complexity of accessing an element in an array by its index?", ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 0,
     "The address is computed directly from the index." + NOTE, "PGCET 2024 M.Tech CS · Q19"),
    ("A data structure is", ["A way of organising and storing data so that it can be used efficiently", "A programming language", "A type of computer", "A file format"], 0,
     PYQ + "Choice of data structure decides the efficiency of the algorithm."),
    ("'Algorithms + Data Structures = Programs' is the title of a book by", ["Niklaus Wirth", "Donald Knuth", "Dennis Ritchie", "Alan Turing"], 0, "Wirth also designed Pascal."),
    ("Which of these is a primitive data structure?", ["int", "Stack", "Queue", "Tree"], 0, "Primitive types are operated on directly by machine instructions."),
    ("Which is a non-linear data structure?", ["Tree", "Stack", "Queue", "Array"], 0, PYQ + "Trees and graphs are non-linear."),
    ("In a linear data structure", ["Elements form a sequence – each, except the ends, has one predecessor and one successor", "Elements form a hierarchy",
                                    "Every element is joined to every other", "Elements have no order"], 0, "Arrays, stacks, queues, linked lists."),
    ("Which data structure is dynamic – its size can change while the program runs?", ["Linked list", "Static array", "int", "char"], 0, "Nodes are allocated as needed."),
    ("An array holds elements of one type, while a structure (record) can hold elements of different types. Arrays are therefore", ["Homogeneous", "Heterogeneous",
                                                                                                                                  "Non-linear", "Dynamic"], 0,
     "Structures are heterogeneous."),
    ("Which is NOT a basic operation on data structures?", ["Compiling", "Traversing", "Searching", "Merging"], 0, "Also inserting, deleting and sorting."),
    ("Combining two sorted lists into one sorted list is called", ["Merging", "Traversing", "Searching", "Hashing"], 0, "Used in merge sort."),
    ("An abstract data type (ADT) specifies", ["The data and the operations on it, without saying how they are implemented", "The exact memory layout", "Machine code",
                                               "A file format"], 0, PYQ + "E.g. a stack ADT: push, pop, peek, isEmpty."),
    ("To store a family tree, the most suitable data structure is a", ["Tree", "Stack", "Queue", "Array of integers"], 0, "Parent–child relations."),
    ("A road map of cities and roads is best stored as a", ["Graph", "Stack", "Queue", "Binary tree"], 0, "Cities = vertices, roads = edges."),
    ("Jobs sent to a shared printer are handled in the order they arrive. The suitable data structure is a", ["Queue", "Stack", "Tree", "Graph"], 0, "First in, first out."),
    ("The time complexity of an algorithm is", ["The number of steps it takes, as a function of the input size", "The time taken to write it", "The processor's clock speed",
                                                "The compile time"], 0, "Expressed with O, Ω and Θ."),
    ("Space complexity measures", ["The memory an algorithm needs, as a function of the input size", "The disk size", "The program length in lines",
                                   "The number of variable names"], 0, "Fixed part + variable part (stack, dynamic data)."),
    ("For linear search, the best case occurs when", ["The key is the first element", "The key is the last element", "The key is absent", "The array is sorted"], 0,
     "One comparison: O(1)."),
    ("Using extra memory, such as a lookup table, to make a program faster is called", ["A time–space trade-off", "Recursion", "A hash collision", "Fragmentation"], 0,
     "Less time, more space (or the reverse)."),
    ("Which is NOT one of the properties of an algorithm (Knuth)?", ["It must be written in C", "Finiteness", "Definiteness", "Effectiveness"], 0,
     "Also input and output."),
    ("Processed, meaningful data is called", ["Information", "Raw data", "A record", "A field"], 0, "Data → processing → information."),
    ("A collection of related fields (e.g. roll number, name, marks of one student) is a", ["Record", "File", "Database", "Byte"], 0,
     "Field → record → file → database."),
    ("Which data structure best represents many-to-many relationships, such as friendships in a social network?", ["Graph", "Tree", "Stack", "Queue"], 0,
     "A tree allows only one parent per node."),
    ("The 'undo' feature of a text editor is naturally implemented with a", ["Stack", "Queue", "Graph", "Heap"], 0, "The last change is undone first."),
]

COMPLEXITY_PRACTICE = [
    kset("KEA 2026 CS Paper-2 · Q6"),
    kset("KSET 2025 CS&A · Q67"),
    ("What is the time complexity?\nfor (i = 0; i < n; i++) sum += a[i];", ["O(n)", "O(1)", "O(n²)", "O(log n)"], 0, PYQ + "One loop of n steps."),
    ("What is the time complexity?\nfor (i = 0; i < n; i++)\n  for (j = 0; j < n; j++)\n    c[i][j] = 0;", ["O(n²)", "O(n)", "O(2n)", "O(n log n)"], 0, "n × n steps."),
    ("What is the time complexity?\nfor (i = 0; i < n; i++)\n  for (j = 0; j < 10; j++)\n    s++;", ["O(n)", "O(n²)", "O(10ⁿ)", "O(log n)"], 0, "The inner loop is a constant 10."),
    ("What is the time complexity?\nfor (i = 1; i <= n; i = i * 3) s++;", ["O(log n)", "O(n)", "O(n/3)", "O(3ⁿ)"], 0, "i takes the values 1, 3, 9, … – about log₃ n steps."),
    ("What is the time complexity of three nested loops, each running n times?", ["O(n³)", "O(3n)", "O(n²)", "O(n log n)"], 0, "n · n · n."),
    ("What is the time complexity?\nfor (i = 1; i * i <= n; i++) s++;", ["O(√n)", "O(n)", "O(log n)", "O(n²)"], 0, PYQ + "The loop stops when i exceeds √n."),
    ("What is the time complexity?\nfor (i = 0; i < n; i++) s++;\nfor (j = 0; j < n; j++) s++;", ["O(n)", "O(n²)", "O(2ⁿ)", "O(log n)"], 0,
     "Two loops one after the other: n + n = 2n."),
    ("The naive recursive Fibonacci function fib(n) = fib(n − 1) + fib(n − 2) runs in", ["Exponential time, O(2ⁿ)", "O(n)", "O(log n)", "O(n²)"], 0,
     "The same values are recomputed again and again."),
    ("The recursive factorial function fact(n) = n × fact(n − 1) takes", ["O(n) time and O(n) stack space", "O(1) time", "O(n²) time", "O(log n) space"], 0,
     "n calls are active at the deepest point."),
    ("Assigning a value to a[5] takes", ["O(1)", "O(n)", "O(log n)", "O(5)"], 0, "Constant time, whatever the array size."),
    ("Multiplying two n × n matrices with the usual triple loop takes", ["O(n³)", "O(n²)", "O(n)", "O(2ⁿ)"], 0, "n² entries, each a sum of n products."),
    ("For n = 4, how many times does count++ run?\nfor (i = 0; i < n; i++)\n  for (j = i; j < n; j++)\n    count++;", ["10", "16", "6", "4"], 0, PYQ + "4 + 3 + 2 + 1 = n(n + 1)/2."),
    ("How many times does the body run?\nfor (i = 1; i <= 64; i = i * 2) s++;", ["7", "6", "64", "32"], 0, "1, 2, 4, 8, 16, 32, 64."),
    ("Summing an array with a loop and one variable needs extra space of", ["O(1)", "O(n)", "O(n²)", "O(log n)"], 0, "Only the sum and the index."),
    ("Making a copy of an array of n elements needs extra space of", ["O(n)", "O(1)", "O(log n)", "O(n²)"], 0, "One new element per element."),
    ("For large n, which function grows fastest?", ["2ⁿ", "n¹⁰", "n log n", "n²"], 0, "An exponential eventually beats any polynomial."),
    ("Which complexity is the best (fastest) for large n?", ["O(log n)", "O(n)", "O(n log n)", "O(√n)"], 0, "log n < √n < n < n log n."),
    ("An O(n) algorithm takes 2 seconds for n = 1,000. For n = 4,000 it takes about", ["8 seconds", "2 seconds", "32 seconds", "16 seconds"], 0, "Four times the input, four times the time."),
    ("An O(n³) algorithm takes 1 second for n = 100. For n = 200 it takes about", ["8 seconds", "2 seconds", "4 seconds", "3 seconds"], 0, "2³ = 8."),
    ("Binary search on a sorted array of 128 elements needs at most how many comparisons?", ["8", "7", "128", "64"], 0, "⌊log₂ 128⌋ + 1."),
    ("Inserting at the end of an array that still has free space takes", ["O(1)", "O(n)", "O(log n)", "O(n²)"], 0, "No shifting is needed."),
    ("Finding the maximum of an unsorted array of n elements takes", ["Θ(n)", "Θ(1)", "Θ(log n)", "Θ(n²)"], 0, "Every element must be looked at."),
    ("Finding the maximum of an array sorted in ascending order takes", ["O(1)", "O(n)", "O(log n)", "O(n log n)"], 0, "It is the last element."),
    ("The recurrence T(n) = T(n − 1) + 1 solves to", ["O(n)", "O(log n)", "O(n²)", "O(1)"], 0, "One unit of work per level, n levels."),
    ("The recurrence T(n) = 2T(n/2) + 1 solves to", ["O(n)", "O(n log n)", "O(log n)", "O(n²)"], 0, "The number of nodes in the recursion tree is about 2n."),
    ("The recurrence T(n) = T(n/2) + 1 solves to", ["O(log n)", "O(n)", "O(1)", "O(n log n)"], 0, "That is binary search."),
    ("Recursive binary search on n elements uses stack space of", ["O(log n)", "O(1)", "O(n)", "O(n²)"], 0, "The depth of recursion is log n (iterative: O(1))."),
    ("Which statement about asymptotic notation is correct?", ["Big-O gives an upper bound on the growth rate", "Big-O gives the exact running time",
                                                               "Big-O depends on the processor", "Big-O includes constant factors"], 0, "Ω is a lower bound, Θ a tight bound."),
]

PRIMITIVE_NUM_CHAR = [
    kset("KSET 2025 CS&A · Q27"),
    ("If negative members are stored in 2's complement form, then range of numbers that can be stored in 8 bits is ____",
     ["−127 to +127", "−127 to +128", "−128 to +127", "−128 to +128"], 2, "−2⁷ … 2⁷ − 1." + NOTE, "PGCET 2025 MCA · Q38"),
    ("A floating-point number is said to be normalized, if the MSB (Most Significant Bit) of the mantissa is ____.", ["−1", "0", "1", "2"], 2,
     "No leading zeros in the mantissa." + NOTE, "PGCET 2024 MCA · Q12"),
    ("Primitive data structures are those that", ["Are operated on directly by machine instructions – int, char, float, pointers", "Are built from other structures",
                                                  "Are always linked", "Have no fixed size"], 0, PYQ + "Non-primitive: arrays, lists, stacks, queues, trees, graphs."),
    ("Negative integers are stored in most computers in", ["2's complement form", "Sign-magnitude form", "BCD", "ASCII"], 0, "It has a single zero and simple addition."),
    ("A 32-bit signed int can hold values from", ["−2,147,483,648 to +2,147,483,647", "0 to 4,294,967,295", "−32,768 to +32,767", "−2³² to +2³²"], 0, "−2³¹ … 2³¹ − 1."),
    ("−5 in 8-bit 2's complement is", ["11111011", "10000101", "11111010", "00000101"], 0, "5 = 00000101; invert → 11111010; add 1."),
    ("The character 'A' is stored in one byte as", ["01000001 (ASCII 65)", "00001010", "11000001", "01100001"], 0, "01100001 is 'a' (97)."),
    ("Kannada letters are stored in computers using", ["Unicode, e.g. UTF-8 with several bytes per letter", "7-bit ASCII", "EBCDIC", "BCD"], 0,
     "ASCII has only 128 characters."),
    ("An IEEE 754 single-precision float has", ["1 sign bit, 8 exponent bits and 23 fraction bits", "1, 11 and 52 bits", "16 integer and 16 fraction bits", "8 bits only"], 0,
     "Double: 1, 11, 52."),
    ("The value 0.1 cannot be stored exactly in a float because", ["0.1 has no finite binary fraction", "Floats are integers", "0.1 is negative", "Floats have no exponent"], 0,
     "Like 1/3 in decimal."),
    ("On a little-endian machine, the 32-bit value 0x12345678 stored at address 100 has which byte at address 100?", ["0x78", "0x12", "0x34", "0x56"], 0,
     "The least significant byte comes first (x86)."),
    ("Which is NOT a primitive operation on integers?", ["Sorting", "Addition", "Comparison", "Bitwise AND"], 0, "Sorting works on a collection."),
    ("C has no separate Boolean type before C99; a condition is", ["An int: 0 means false, any non-zero value means true", "A char 'T' or 'F'", "A float", "A string"], 0,
     "C99 added _Bool."),
    ("An 8-bit unsigned value 255 plus 1 gives", ["0 (it wraps around)", "256", "−1", "An error"], 0, "Unsigned arithmetic is modulo 2⁸."),
    ("The values of 17 / 5 and 17 % 5 (integers) are", ["3 and 2", "3.4 and 2", "3 and 0.4", "4 and 3"], 0, "Quotient and remainder."),
    ("The value of 'a' + 2, printed with %c, is", ["c", "99", "a2", "b"], 0, "97 + 2 = 99 = 'c'."),
    ("To turn a digit character c ('0'–'9') into its value, compute", ["c − '0'", "c + '0'", "c − 'a'", "c / 10"], 0, "'7' − '0' = 7."),
    ("Typical sizes of char, int, float and double are", ["1, 4, 4 and 8 bytes", "1, 2, 2 and 4 bytes", "2, 4, 8 and 16 bytes", "1, 8, 4 and 8 bytes"], 0,
     "Turbo C uses a 2-byte int."),
    ("Which is often listed with int, char and float as a primitive data structure?", ["Pointer", "Linked list", "Queue", "Tree"], 0, "It holds an address."),
    ("A 16-bit unsigned integer can hold values from", ["0 to 65,535", "−32,768 to 32,767", "0 to 32,767", "0 to 65,536"], 0, "2¹⁶ − 1."),
    ("double gives about how many significant decimal digits?", ["15–16", "6–7", "3", "30"], 0, "float gives about 6–7."),
    ("How many bits are needed to store any one of 100 different values?", ["7", "6", "100", "8"], 0, "2⁶ = 64 < 100 ≤ 128 = 2⁷."),
    ("Storing money as a whole number of paise instead of a float number of rupees avoids", ["Rounding errors of binary fractions", "Overflow in every case",
                                                                                              "Sign problems", "Endianness problems"], 0, "Integers are exact."),
    ("The value of  '7' − '0' + 1  is", ["8", "56", "'8'", "7"], 0, "7 + 1."),
    ("One byte can hold how many different values?", ["256", "255", "8", "128"], 0, "2⁸."),
    ("A char variable holding 'B' contains the bit pattern", ["01000010", "01000001", "01100010", "00000010"], 0, "'B' = 66."),
    ("A pointer variable on a 64-bit system occupies", ["8 bytes, whatever type it points to", "1 byte", "The size of the pointed-to type", "2 bytes"], 0,
     "It stores a memory address."),
    ("The smallest addressable unit of memory in most computers is the", ["Byte", "Bit", "Word", "Nibble"], 0, "Each byte has its own address."),
    ("The data type of a variable decides", ["The memory it occupies, the values it can hold and the operations allowed on it", "Its name alone", "The file it is saved in",
                                             "Its address"], 0, "That is what makes a type an abstract data type."),
]

STRINGS_POINTERS = [
    ("What is the purpose of a string data type in C programming?", ["To store numerical values", "To store True/False values", "To store Text and characters",
                                                                     "To perform mathematical operations"], 2, "A char array ending in '\\0'." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q88"),
    ("What is the output of the following program ?\n#include<stdio.h>\n#include<string.h>\nvoid main()\n{\n  printf(\"%d%d\", sizeof (\"bengaluru\"),\n    strlen(\"bengaluru\"));\n}",
     ["9 9", "10 9", "10 10", "9 10"], 1, "sizeof counts the '\\0'." + NOTE, "PGCET 2024 M.Tech CS · Q86"),
    kset("KEA 2026 CS Paper-2 · Q83"),
    ("In C, the string \"KEA\" occupies", ["4 bytes", "3 bytes", "1 byte", "6 bytes"], 0, PYQ + "Three characters and the terminating '\\0'."),
    ("Besides fixed-length and variable-length records, strings can be stored as", ["Linked lists of characters (or blocks of characters)", "Binary trees always",
                                                                                     "Hash tables of digits", "Graphs"], 0, "Lipschutz, ch. 3."),
    ("Storing a string's length in its first byte instead of ending it with a terminator (as Pascal does) allows", ["Finding the length in O(1)", "Unlimited length",
                                                                                                                   "Faster comparison in every case", "Using no memory"], 0,
     "C must scan to the '\\0' (O(n))."),
    ("What does len(\"data\") return?\nint len(char *s) { char *p = s; while (*p) p++; return p - s; }", ["4", "5", "3", "An address"], 0,
     PYQ + "Pointer subtraction gives the number of characters."),
    ("The loop  while ((*d++ = *s++));", ["Copies the string s to d, including the terminating '\\0'", "Compares s and d", "Reverses s", "Counts the characters"], 0,
     "The classic K&R strcpy."),
    ("Reversing a string of n characters in place with two pointers needs", ["⌊n/2⌋ swaps", "n swaps", "2n swaps", "n − 1 swaps"], 0, "Swap the ends and move inwards."),
    ("strcat(s1, s2) takes time proportional to", ["len(s1) + len(s2)", "len(s2) alone", "A constant", "len(s1) × len(s2)"], 0, "It must first find the end of s1."),
    ("Naive pattern matching of a pattern of length m in a text of length n checks at most how many starting positions?", ["n − m + 1", "n", "m", "n × m"], 0,
     "Each check costs up to m comparisons."),
    ("What is printed?\nchar *p = \"KARNATAKA\";\np += 3;\nprintf(\"%s\", p);", ["NATAKA", "KAR", "RNATAKA", "ATAKA"], 0, "p now points to the fourth character."),
    ("For  char *s = \"MYSURU\";  the value of  *(s + 2)  is", ["'S'", "'Y'", "'U'", "'M'"], 0, "M(0) Y(1) S(2)."),
    ("What is printed?\nchar *p = \"bengaluru\";\nint c = 0;\nwhile (*p) { if (strchr(\"aeiou\", *p)) c++; p++; }\nprintf(\"%d\", c);", ["4", "3", "5", "9"], 0,
     PYQ + "e, a, u, u."),
    ("Checking whether \"madam\" is a palindrome with two pointers p (start) and q (end) means", ["Comparing *p and *q while moving them towards each other",
                                                                                                "Comparing *p with *(p + 1)", "Counting the vowels", "Sorting the letters"], 0,
     "Stop when the pointers meet or a pair differs."),
    ("Inside a loop over a string,  if (*p >= 'a' && *p <= 'z') *p -= 32;", ["Converts lowercase letters to uppercase", "Converts uppercase to lowercase",
                                                                            "Removes the letters", "Counts the letters"], 0, "'a' − 32 = 'A'."),
    ("Storing names of different lengths as an array of char pointers (instead of a 2-D char array)", ["Saves memory, since each string uses only the space it needs",
                                                                                                         "Uses more memory", "Is not allowed in C", "Sorts the names automatically"], 0,
     "A 2-D array reserves the longest length for every row."),
    ("When sorting an array of char pointers (strings), it is efficient to swap", ["The pointers, not the characters", "Every character", "The lengths",
                                                                                   "The addresses of the array"], 0, "Only addresses move."),
    ("strcmp(\"Zebra\", \"apple\") returns a value that is", ["Negative, because 'Z' (90) < 'a' (97)", "Positive", "0", "Undefined"], 0, "Comparison uses character codes."),
    ("On a 64-bit system, with  char s[] = \"Hi\";  and  char *p = \"Hi\";  the values of sizeof(s) and sizeof(p) are", ["3 and 8", "3 and 3", "2 and 8", "8 and 8"], 0,
     "An array versus a pointer."),
    ("For the empty string \"\", strlen and sizeof give", ["0 and 1", "1 and 1", "0 and 0", "1 and 0"], 0, "It still has the '\\0'."),
    ("Inserting a character in the middle of a string stored in an array requires", ["Shifting all the following characters one place to the right", "Nothing",
                                                                                      "Changing the length byte only", "Rewriting the program"], 0, "O(n) work."),
    ("Deleting a character from the middle of a string stored in an array requires", ["Shifting all the following characters one place to the left",
                                                                                       "Setting it to a space", "Nothing", "Reallocating memory"], 0, "Including the '\\0'."),
    ("For  char s[20], *p = s + 7, *q = s + 2;  the value of  p − q  is", ["5", "9", "7", "2"], 0, "The number of characters between them."),
    ("strtok() is used to", ["Split a string into tokens separated by delimiter characters", "Join strings", "Reverse a string", "Compare strings"], 0,
     "strtok(s, \" \") gives the words one by one."),
    ("What is printed?\nchar *p = \"472\";\nint n = 0;\nwhile (*p) n = n * 10 + (*p++ - '0');\nprintf(\"%d\", n);", ["472", "274", "13", "4"], 0,
     "How atoi works."),
    ("To count how often each character occurs in a string, a common method uses", ["An array of 256 counters indexed by the character code", "A stack", "A queue",
                                                                                    "A binary tree"], 0, "count[(unsigned char)*p]++."),
    ("For  char *s = \"hello\";  the value of  strchr(s, 'l') − s  is", ["2", "3", "1", "4"], 0, "The first 'l' is at index 2."),
    ("char *p = \"abc\";  then  p[1]  and  *(p + 1)  are", ["Both 'b'", "'a' and 'b'", "'b' and an address", "Both addresses"], 0, "p[i] is *(p + i)."),
    ("For  char *s = \"data structure\";  the value of  strstr(s, \"struct\") − s  is", ["5", "4", "6", "0"], 0, "\"data \" takes positions 0–4."),
]

PRIMITIVE_PRACTICE = [
    ("What is printed?\nprintf(\"%c\", 'A' + 5);", ["F", "70", "E", "A5"], 0, "65 + 5 = 70 = 'F'."),
    ("What is printed?\nprintf(\"%d\", 'z' - 'a');", ["25", "26", "122", "1"], 0, "122 − 97."),
    ("On a compiler with signed 8-bit char, what is printed?\nprintf(\"%d\", (char)200);", ["−56", "200", "56", "−200"], 0, PYQ + "200 − 256."),
    ("What is printed?\nunsigned char c = 250;\nc += 10;\nprintf(\"%d\", c);", ["4", "260", "255", "0"], 0, "260 − 256."),
    ("What is printed?\nprintf(\"%.2f\", 10 / 4.0);", ["2.50", "2.00", "2.5", "2"], 0, "One real operand gives real division."),
    ("What is printed?\nprintf(\"%d\", 7 / 2 * 2);", ["6", "7", "8", "3"], 0, "7 / 2 = 3, then × 2."),
    ("What is printed?\nint x = 0x2A;\nprintf(\"%d\", x);", ["42", "2", "210", "32"], 0, "2 × 16 + 10."),
    ("What is printed?\nprintf(\"%o\", 64);", ["100", "64", "40", "1000000"], 0, "64 = 1 × 8²."),
    ("What is printed?\nfloat f = 1e-3;\nprintf(\"%f\", f);", ["0.001000", "1e-3", "0.000100", "0.010000"], 0, "%f prints six decimals."),
    ("What is printed?\nprintf(\"%d\", '0' + 5);", ["53", "5", "'5'", "48"], 0, "48 + 5."),
    ("What is printed?\nchar s[] = \"DATA\";\nprintf(\"%c\", *s + 1);", ["E", "A", "D1", "68"], 0, "*s = 'D' (68); 68 + 1 = 'E'."),
    ("What is printed?\nchar *p = \"STACK\";\nprintf(\"%c%c\", *p, *(p + 4));", ["SK", "ST", "SC", "KS"], 0, "First and last characters."),
    ("What is printed?\nchar s[10] = \"ab\";\nstrcat(s, \"cd\");\nprintf(\"%d\", (int)strlen(s));", ["4", "2", "10", "5"], 0, "\"abcd\"."),
    ("What is printed?\nchar s[] = \"queue\";\nprintf(\"%d\", (int)(sizeof(s) - strlen(s)));", ["1", "0", "5", "6"], 0, "The '\\0' byte."),
    ("What is printed?\nchar *s = \"tree\";\nwhile (*s) putchar(*s++ - 32);", ["TREE", "tree", "Tree", "An infinite loop"], 0, "Each lowercase letter minus 32."),
    ("What is printed?\nint count = 0;\nchar *p = \"a b c\";\nwhile (*p) if (*p++ == ' ') count++;\nprintf(\"%d\", count);", ["2", "3", "5", "1"], 0, "Two spaces."),
    ("What is printed?\nprintf(\"%s\", \"graph\" + 2);", ["aph", "graph", "gr", "ph"], 0, "A string literal is an address; + 2 skips two characters."),
    ("What is printed?\nchar s[] = \"LIST\";\ns[2] = '\\0';\nprintf(\"%s\", s);", ["LI", "LIST", "L", "LIT"], 0, "The string now ends at index 2."),
    ("What is printed?\nprintf(\"%d\", strcmp(\"abc\", \"abc\") == 0);", ["1", "0", "−1", "abc"], 0, "Equal strings give 0, so the comparison is true."),
    ("What is printed?\nint n = 0;\nchar *p = \"2026\";\nwhile (*p) n = n * 10 + (*p++ - '0');\nprintf(\"%d\", n + 1);", ["2027", "20261", "2026", "3"], 0,
     "The string becomes the number 2026."),
    ("What is printed?\nprintf(\"%d\", (int)sizeof(\"\"));", ["1", "0", "8", "2"], 0, "Just the '\\0'."),
    ("What is printed?\nchar a[] = \"abc\", b[] = \"abc\";\nprintf(\"%d\", a == b);", ["0", "1", "abc", "Compile error"], 0,
     PYQ + "Two different arrays have different addresses; use strcmp."),
    ("What is printed?\nprintf(\"%5.1f|\", 3.14159);", ["'  3.1|'", "'3.1|'", "'3.14159|'", "'00003.1|'"], 0, "Width 5, one decimal, right-justified."),
    ("What is printed?\nprintf(\"%x\", 255 + 1);", ["100", "ff", "256", "fg"], 0, "256 = 0x100."),
    ("What is printed?\ndouble d = 5 / 2;\nprintf(\"%.1f\", d);", ["2.0", "2.5", "3.0", "0.0"], 0, "Integer division first."),
    ("What is printed?\nfloat f = 0.5;\nprintf(\"%d\", f == 0.5);", ["1 – 0.5 is exact in binary", "0", "Compile error", "Undefined"], 0,
     PYQ + "0.5 = 2⁻¹ is exact; 0.1 is not."),
    ("What is printed?\nprintf(\"%d\", 1 + '1');", ["50", "2", "11", "'2'"], 0, "'1' is 49."),
    ("The value of  strlen(\"C\\tDS\")  is", ["4", "5", "6", "3"], 0, "\\t is one character."),
    ("What is printed?\nchar s[] = \"abcde\", *p = s + 1, *q = s + 3;\nprintf(\"%d\", (int)(q - p));", ["2", "3", "4", "1"], 0, "Index 3 − index 1."),
    ("What is printed?\nprintf(\"%c\", \"KEA\"[1]);", ["E", "K", "A", "Compile error"], 0, "A string literal can be indexed like an array."),
]

SET3 = "3 · Previous-Year Pattern Practice – Programs and Complexity"
TOPICS = {
    "Introduction to Data Structures": [
        ("1 · Definition, Classification and Operations on Data Structures", DS_BASICS),
        ("2 · Introduction to Time and Space Complexity – Asymptotic Notation", COMPLEXITY),
        (SET3, COMPLEXITY_PRACTICE),
    ],
    "Primitive Data Structures": [
        ("1 · Integer, Character and Float – Memory Representation and Primitive Operations", PRIMITIVE_NUM_CHAR),
        ("2 · Strings – Memory Representation and String Manipulation Using Pointers", STRINGS_POINTERS),
        ("3 · Previous-Year Pattern Practice – Programs and Output", PRIMITIVE_PRACTICE),
    ],
}

NOTES = {
    "Introduction to Data Structures": [{"title": "Introduction to data structures – revision sheet", "md": """## Definition and classification
- Data structure = organised way of storing data for efficient access and change; ADT = data + operations, implementation hidden
- **Primitive**: int, char, float, double, pointer (machine-level)
- **Non-primitive** → **linear** (array, stack, queue, linked list) | **non-linear** (tree, graph)
- Static (array, fixed size) vs dynamic (linked list); homogeneous (array) vs heterogeneous (structure)
- Choosing: hierarchy → tree; network → graph; undo/recursion → stack; printer jobs/BFS → queue
- Data → information; field → record → file

## Operations
Traversing, searching, inserting, deleting, sorting, merging

## Complexity
- Time / space as a function of input size n; best, average, worst case; time–space trade-off
- O (upper), Ω (lower), Θ (tight), o (strictly smaller); constants and lower terms dropped
- Growth: 1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!
| Code pattern | Time |
|---|---|
| single loop to n | O(n) |
| i = i × 2 (or × 3) | O(log n) |
| i × i ≤ n | O(√n) |
| two nested loops to n | O(n²) |
| j from i to n (n = 4 → 10 steps) | O(n²) |
| three nested loops | O(n³) |
| naive Fibonacci | O(2ⁿ) |
- Recurrences: T(n−1) + 1 → n; T(n/2) + 1 → log n; 2T(n/2) + 1 → n; 2T(n/2) + n → n log n
- Algorithm properties (Knuth): finiteness, definiteness, input, output, effectiveness
"""}],
    "Primitive Data Structures": [{"title": "Primitive data structures – revision sheet", "md": """## Integers
- 2's complement: n bits → −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 (8-bit −128…127; 32-bit ±2.1 × 10⁹); −5 = 11111011
- Unsigned 16-bit 0…65,535; unsigned arithmetic wraps (255 + 1 = 0 in 8 bits; 250 + 10 = 4)
- Operations: + − × / % (17 / 5 = 3, 17 % 5 = 2), comparison, bitwise
- Little-endian stores the least significant byte first (0x12345678 → 78 56 34 12)

## Characters
- ASCII 7-bit ('A' 65 = 01000001, 'a' 97, '0' 48, space 32); Unicode/UTF-8 for Kannada etc.
- Arithmetic on codes: 'a' + 2 = 'c'; c − '0' gives a digit's value; lowercase − 32 = uppercase

## Floating point
- IEEE 754: float 1 + 8 + 23 (≈ 7 digits), double 1 + 11 + 52 (≈ 15–16 digits); normalized mantissa starts with 1
- 0.1 is not exact (0.5 is) – never compare floats with ==; store money as integer paise

## Strings
- C: char array ending in '\\0' ("KEA" = 4 bytes; sizeof("") = 1); Pascal: length byte
- Representations: fixed-length, variable-length (terminator or length), linked
- Pointer idioms: length `while (*p) p++; return p − s;`; copy `while ((*d++ = *s++));`; reverse with two pointers (⌊n/2⌋ swaps); atoi `n = n*10 + (*p − '0')`
- Library: strlen, strcpy, strncpy, strcat (O(len1 + len2)), strcmp (code order: 'Z' < 'a'), strchr, strstr, strtok
- Array of char pointers saves space for ragged strings; sort by swapping pointers; compare with strcmp, not ==
"""}],
}
