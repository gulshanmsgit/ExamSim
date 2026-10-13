"""KRIES Computer Teacher · C Programming · P2-KRC-07 Structures and Unions and P2-KRC-08 Bitwise Operators (2 topics × 2 sets × 30),
with NOTES. Pulls the matching GPSTR questions of 'Programming in C – Part 1' (tools/p2u4_b.py), adds REAL previous-year questions
(KSET 2024/2025 from packs/pyq-p2.json; PGCET 2026 read from the page image, answer worked out by ExamSim) and new ones. Sizes assume
a typical 32/64-bit compiler (4-byte int and float, 8-byte double, natural alignment) and are stated in each question. Every bit pattern
and output was worked out by hand."""
from p2u4_b import SEQUENCE as S, ARRAYS_STRINGS as A
from p2u7_a import kset, PYQ, NOTE

STRUCTURES = [
    A[11], A[12], A[13], A[14], A[17], A[18], A[24], A[25], A[26],
    kset("KSET 2025 CS&A · Q25"),
    ("A structure in C is declared with the keyword", ["struct", "structure", "record", "class"], 0, "class is C++."),
    ("A structure is a collection of", ["Variables of possibly different types under one name", "Variables of one type alone", "Functions",
                                        "Pointers to the same type"], 0, "An array holds elements of one type."),
    ("Members of a structure variable s are accessed with", ["The dot operator, e.g. s.roll", "The arrow operator, s->roll", "s[roll]", "s::roll"], 0,
     "-> is used with a pointer to a structure."),
    ("struct student { int roll; char name[20]; };  on its own", ["Defines a type – no memory is allocated until a variable is declared", "Allocates 24 bytes",
                                                                  "Creates a variable named student", "Is an error without typedef"], 0,
     PYQ + "struct student s1; then allocates memory."),
    ("What is printed?\nstruct point { int x, y; } p = {3, 4};\nprintf(\"%d\", p.x + p.y);", ["7", "34", "3", "Compile error"], 0, "Members are initialised in order."),
    ("For  struct emp e[10];  the salary of the third employee is", ["e[2].salary", "e[3].salary", "e.salary[2]", "e->salary[3]"], 0,
     PYQ + "An array of structures: index first, then the member."),
    ("For  struct a { int x; struct b { int y; } in; } v;  the member y is accessed as", ["v.in.y", "v.y", "v->in->y", "v.b.y"], 0, "Nested structure: outer.inner.member."),
    ("For  struct point *p = &pt;  which expression accesses the member x?", ["p->x or (*p).x", "*p.x", "p.x", "&p->x"], 0, "p->x is shorthand for (*p).x."),
    ("The expression  *p.x  is parsed as", ["*(p.x)", "(*p).x", "p->x", "An error in every case"], 0, PYQ + ". binds tighter than *, so write (*p).x or p->x."),
    ("When a structure variable is passed to a function by value", ["A copy of the whole structure is made", "Its address alone is passed",
                                                                    "Its first member alone is passed", "It is not allowed in C"], 0,
     "Pass a pointer to avoid copying large structures."),
    ("struct { int a; float b; } s;  with 4-byte int and float – sizeof(s) is", ["8", "4", "5", "16"], 0, "4 + 4 with no padding needed."),
    ("What is printed?\nstruct s { int a; int b; } x = {1};\nprintf(\"%d %d\", x.a, x.b);", ["1 0", "1 garbage", "0 1", "Compile error"], 0,
     "Members without initialisers become 0."),
    ("struct { int x; } a, b;  declares", ["Two variables of an unnamed structure type", "A type named a", "An error", "One variable"], 0, "The tag may be left out."),
    ("struct point p = {.y = 5, .x = 2};  (C99) gives", ["x = 2, y = 5", "x = 5, y = 2", "A compile-time error", "x = 0, y = 5"], 0, "Designated initialisers name the members."),
    ("For  struct st { char name[20]; } s;  which statement stores \"Ravi\" in name?", ["strcpy(s.name, \"Ravi\");", "s.name = \"Ravi\";", "s->name = \"Ravi\";",
                                                                                       "*s.name = \"Ravi\";"], 0, PYQ + "An array cannot be assigned with =."),
    ("Can a C function return a structure?", ["Yes – the whole structure is returned by value", "No, only a pointer to it", "No, structures cannot leave a function",
                                              "Yes, if it has one member"], 0, "E.g. struct point mid(struct point a, struct point b)."),
    ("What is printed?\nstruct item { int qty; } it[3] = {{2}, {5}, {3}};\nint i, t = 0;\nfor (i = 0; i < 3; i++) t += it[i].qty;\nprintf(\"%d\", t);", ["10", "5", "3", "253"], 0,
     "2 + 5 + 3."),
    ("If p points to e[0] of an array of structures, p + 1 points to", ["e[1] – advanced by the size of one structure", "The next member of e[0]",
                                                                         "e[0] plus one byte", "e[2]"], 0, "Pointer arithmetic scales by sizeof(struct)."),
    ("p->a++  increments", ["The member a (postfix – after its value is used)", "The pointer p", "Both p and a", "Nothing"], 0, "-> binds tighter than ++."),
    ("The main difference between an array and a structure is that", ["An array holds elements of one type; a structure can hold members of different types",
                                                                      "A structure is always faster", "An array cannot be passed to a function", "Structures cannot contain arrays"], 0,
     "Array elements are accessed by index, structure members by name."),
]

UNIONS_ENUM = [
    A[15], A[16],
    kset("KSET 2025 CS&A · Q26"),
    ("The size of a union is", ["The size of its largest member (plus any padding)", "The sum of the sizes of its members", "The size of its first member", "Always 4 bytes"], 0,
     PYQ + "All members share the same memory."),
    ("In a union, all members", ["Share the same memory location", "Have separate memory", "Must be of the same type", "Are initialised to 0"], 0,
     "Writing one member overwrites the others."),
    ("What is printed?\nunion u { int i; char c; } x;\nx.i = 65;\nprintf(\"%c\", x.c);", ["A (on a little-endian machine)", "65", "Garbage on every machine", "Compile error"], 0,
     PYQ + "c overlaps the lowest-addressed byte of i, which holds 65 on little-endian x86."),
    ("At any time, a union variable meaningfully holds", ["The value of one member", "The values of all members", "Two members", "None of its members"], 0,
     "The member written last."),
    ("union u { int i; float f; } x = {10};  initialises", ["The first member i", "The member f", "Both members", "Nothing"], 0,
     "A brace initialiser applies to the first member (C99 also allows {.f = 1.5})."),
    ("With 8-byte double aligned on 8 bytes, sizeof(union { char a[10]; int b; double c; }) is", ["16", "10", "22", "8"], 0,
     PYQ + "Largest member 10 bytes, rounded up to a multiple of 8."),
    ("Union members are accessed with", ["The . and -> operators, as for structures", "Index numbers", "The :: operator", "Library functions"], 0, "Same syntax as structures."),
    ("typedef is used to", ["Give a new name (alias) to an existing type", "Create a new type with new storage", "Define a macro", "Declare a variable"], 0,
     "typedef unsigned long ulong;"),
    ("After  typedef struct { int x, y; } Point;  a variable is declared as", ["Point p;", "struct Point p;", "typedef Point p;", "Point.p;"], 0,
     "The structure has no tag, only the typedef name."),
    ("typedef char *String;  String a, b;  — a and b are", ["Both char pointers", "a a char pointer, b a char", "Both chars", "An error"], 0,
     PYQ + "typedef makes a true type name; compare with #define."),
    ("#define String char *  then  String a, b;  — b is", ["A char", "A char pointer", "An error", "A string"], 0, "Text substitution gives char *a, b;."),
    ("enum color { RED, GREEN, BLUE };  — BLUE has the value", ["2", "3", "1", "0"], 0, "Enumerators start at 0 by default."),
    ("enum { A = 5, B, C = 10, D };  — the values of B and D are", ["6 and 11", "6 and 10", "1 and 3", "5 and 10"], 0, PYQ + "Each enumerator is one more than the previous."),
    ("The enumeration constants of an enum are of type", ["int", "char", "float", "string"], 0, "They can be used wherever an int constant can."),
    ("In an enum, two enumeration constants", ["May have the same value", "Must have different values", "Cannot be negative", "Must be consecutive"], 0,
     "enum { X = 1, Y = 1 }; is legal."),
    ("What is printed?\nenum days { MON = 1, TUE, WED };\nprintf(\"%d\", WED);", ["3", "2", "WED", "0"], 0, "MON = 1, TUE = 2, WED = 3."),
    ("The bit field  unsigned int a : 4;  can hold the values", ["0 to 15", "0 to 4", "0 to 16", "−8 to 7"], 0, "4 bits: 2⁴ − 1 = 15."),
    ("Which is NOT allowed with a bit-field member?", ["Taking its address with &", "Assigning it a value", "Using it in an expression", "Printing it"], 0,
     PYQ + "A bit field may not start on a byte boundary, so it has no address; arrays of bit fields are not allowed either."),
    ("Bit fields are declared with the type", ["unsigned int, signed int or int (and _Bool in C99)", "float", "double", "char arrays"], 0,
     "Compilers may allow other integer types."),
    ("Bit fields are mainly used to", ["Pack several small values or flags into one word to save memory", "Speed up floating-point maths", "Store strings",
                                       "Build linked lists"], 0, "Also to match hardware register layouts."),
    ("struct { unsigned a : 1; unsigned b : 2; unsigned c : 3; } s;  typically has sizeof(s) equal to", ["4 (one unsigned int)", "6", "1", "3"], 0,
     "The 6 bits fit in one unsigned int storage unit (implementation-defined)."),
    ("What is printed?\nstruct { unsigned v : 2; } s;\ns.v = 5;\nprintf(\"%u\", s.v);", ["1", "5", "2", "0"], 0, "Only the low 2 bits of 101 are kept → 01."),
    ("With 4-byte int and padding, the sizes of  struct { int a; char b; }  and  union { int a; char b; }  are typically", ["8 and 4", "5 and 4", "8 and 5", "4 and 4"], 0,
     PYQ + "The structure is padded to a multiple of 4; the union needs only its largest member."),
    ("A union inside a structure is often used to", ["Store one of several kinds of data, with a tag member telling which", "Copy arrays", "Define functions",
                                                     "Build header files"], 0, "A 'variant record' or tagged union."),
    ("typedef int Arr[5];  Arr x;  — x is", ["An array of 5 ints", "An int", "A pointer to int", "An error"], 0, "typedef can name array types too."),
    ("enum constants are useful in a switch because", ["Named constants make the case labels readable", "They allow float cases", "They remove the need for break",
                                                       "They are faster than int"], 0, "case RED: … case GREEN: …"),
    ("Which statement about typedef is NOT true?", ["It allocates memory for a new type", "It creates an alias for an existing type", "It can simplify complex declarations",
                                                    "It is handled by the compiler, not the preprocessor"], 0, "No memory is allocated by a typedef."),
]

BITWISE_LOGIC = [
    S[10],
    kset("KSET 2024 CS&A · Q25"),
    ("Match the following operators in C to their purpose.\nList-I\n(a) ^\n(b) >>\n(c) <<\n(d) |\nList-II\n(i) Performs bitwise OR operations\n(ii) Multiplies by power of 2\n"
     "(iii) Divides by power of 2\n(iv) Performs bitwise EX-OR operations",
     ["a – iii, b – iv, c – ii, d – i", "a – iv, b – iii, c – ii, d – i", "a – ii, b – iii, c – iv, d – i", "a – iv, b – ii, c – iii, d – i"], 1,
     "^ is XOR, >> divides and << multiplies by powers of 2, | is OR." + NOTE, "PGCET 2026 CS · Q93"),
    ("The value of  12 & 10  is", ["8", "14", "6", "2"], 0, "1100 & 1010 = 1000."),
    ("The value of  12 | 10  is", ["14", "8", "6", "22"], 0, "1100 | 1010 = 1110."),
    ("The value of  12 ^ 10  is", ["6", "14", "8", "2"], 0, "1100 ^ 1010 = 0110."),
    ("What is printed?\nprintf(\"%d\", ~0);", ["−1", "0", "1", "65535 on every system"], 0, PYQ + "All bits 1 is −1 in 2's complement."),
    ("The value of  ~5  (int) is", ["−6", "−5", "4", "10"], 0, "~x = −(x + 1)."),
    ("Which expression is non-zero exactly when n is odd?", ["n & 1", "n | 1", "n ^ 1", "~n"], 0, "The lowest bit of an odd number is 1."),
    ("To set bit k of x (make it 1), use", ["x | (1 << k)", "x & (1 << k)", "x ^ ~k", "x & ~(1 << k)"], 0, "OR with a mask that has a 1 at position k."),
    ("To clear bit k of x (make it 0), use", ["x & ~(1 << k)", "x | (1 << k)", "x ^ (1 << k)", "x & (1 << k)"], 0, "AND with a mask that has a 0 at position k."),
    ("To toggle (flip) bit k of x, use", ["x ^ (1 << k)", "x | (1 << k)", "x & ~(1 << k)", "~x << k"], 0, "XOR with 1 flips a bit."),
    ("After  a = 5, b = 9;  a ^= b; b ^= a; a ^= b;  the values are", ["a = 9, b = 5", "a = 5, b = 9", "a = 12, b = 9", "a = 0, b = 0"], 0,
     PYQ + "The XOR swap needs no temporary variable."),
    ("For any int x, the value of  x ^ x  is", ["0", "x", "−1", "2x"], 0, "Equal bits XOR to 0."),
    ("Bitwise operators can be applied to", ["Integer types such as char, int and long", "float and double", "Strings", "Whole arrays"], 0,
     "Using them on float is a compile-time error."),
    ("The values of  5 & 2  and  5 && 2  are", ["0 and 1", "1 and 1", "0 and 0", "7 and 1"], 0, PYQ + "101 & 010 = 0, but both 5 and 2 are true for &&."),
    ("Among &, ^ and |, the order of precedence (highest first) is", ["& then ^ then |", "| then ^ then &", "^ then & then |", "All three are equal"], 0,
     "All are below == and above &&."),
    ("x & 0x0F gives", ["The lowest 4 bits of x", "The highest 4 bits of x", "x with its low 4 bits cleared", "x × 15"], 0, "0x0F is a mask of four 1s."),
    ("The value of  0xF0 | 0x0F  is", ["255", "0", "240", "15"], 0, "0xFF."),
    ("For  unsigned char c = 0x0F;  the value of  (unsigned char) ~c  is", ["0xF0 (240)", "0x0F", "0xFF", "0"], 0, "Every bit is inverted."),
    ("What is printed?\nint n = 13, c = 0;\nwhile (n) { c += n & 1; n >>= 1; }\nprintf(\"%d\", c);", ["3", "4", "13", "1"], 0, "13 = 1101 has three 1 bits."),
    ("For n > 0, the test  (n & (n − 1)) == 0  checks whether n is", ["A power of 2", "Even", "Odd", "Prime"], 0,
     PYQ + "n & (n − 1) clears the lowest 1 bit; only powers of 2 have a single 1 bit."),
    ("Which bitwise operator is unary?", ["~", "&", "|", "^"], 0, "~ (one's complement) takes one operand."),
    ("If x = 13, then after  x &= 6;  x is", ["4", "6", "15", "13"], 0, "1101 & 0110 = 0100."),
    ("In a ^ b, a result bit is 1 when", ["The two bits differ", "Both bits are 1", "Both bits are 0", "Either bit is 1"], 0, "Exclusive OR."),
    ("The value of  0x55 & 0xAA  is", ["0", "0xFF", "0x55", "0xAA"], 0, "01010101 & 10101010 share no 1 bits."),
    ("In bitwise OR, a result bit is 0 only when", ["Both bits are 0", "Both bits are 1", "The bits differ", "Either bit is 0"], 0, "Otherwise it is 1."),
    ("What is printed?\nprintf(\"%d\", 7 & 3 | 8);", ["11", "3", "15", "8"], 0, "& before |: (7 & 3) = 3, then 3 | 8 = 11."),
    ("With 32-bit int, the value of  (-1) & 0xFF  is", ["255", "−1", "0", "−255"], 0, "−1 has all bits set; the mask keeps the low 8."),
    ("XOR is used in simple encryption because", ["Applying the same key twice gives back the original (x ^ k ^ k = x)", "It cannot be reversed",
                                                  "It doubles the value", "It never changes the data"], 0, "Decryption is the same operation."),
]

SHIFTS = [
    S[11],
    kset("KSET 2025 CS&A · Q24"),
    ("The value of  1 << 3  is", ["8", "3", "4", "16"], 0, "1 shifted left 3 places = 2³."),
    ("The value of  64 >> 2  is", ["16", "32", "256", "8"], 0, "64 / 4."),
    ("Without overflow, x << n is equivalent to", ["x × 2ⁿ", "x / 2ⁿ", "x + n", "x ^ n"], 0, "Each left shift doubles the value."),
    ("For unsigned x, x >> n is equivalent to", ["x / 2ⁿ (integer division)", "x × 2ⁿ", "x − n", "x % n"], 0, "Each right shift halves it."),
    ("For a negative signed int x, the result of x >> 1 is", ["Implementation-defined – most compilers copy the sign bit (arithmetic shift)",
                                                              "A logical shift filling 0 on every compiler", "Undefined for every value", "A compile-time error"], 0,
     PYQ + "Use unsigned types when a logical shift is needed."),
    ("With 32-bit int, the expression  1 << 32  is", ["Undefined behaviour", "0", "1", "2³²"], 0, "The shift count must be less than the width."),
    ("The value of  5 << 2  is", ["20", "10", "7", "1"], 0, "5 × 4."),
    ("The value of  100 >> 3  is", ["12", "12.5", "300", "13"], 0, "100 / 8 = 12 (integer)."),
    ("After  unsigned char c = 0x81;  c = c << 1;  c is", ["0x02", "0x102", "0x40", "0x81"], 0, "10000001 → 1 00000010; the 9th bit is lost when stored in 8 bits."),
    ("Which expression gives bit k (0 or 1) of x?", ["(x >> k) & 1", "x >> (k & 1)", "(x & k) >> 1", "x << k"], 0, PYQ + "Move bit k to position 0, then mask it."),
    ("C has no rotate operator. An 8-bit left rotate by 1 of unsigned char x is written", ["(x << 1) | (x >> 7)", "x << 1", "(x >> 1) | x", "x ^ (x << 1)"], 0,
     "The top bit comes back in at the bottom."),
    ("The value of  1 << 2 + 1  is", ["8", "5", "3", "6"], 0, PYQ + "+ binds tighter than <<: 1 << 3."),
    ("Shifts are sometimes used instead of * and / because", ["Shifting is usually faster for powers of two", "They work on floats", "They are more readable",
                                                              "They never overflow"], 0, "Modern compilers do this automatically."),
    ("For n = 5,  for (i = 7; i >= 0; i--) printf(\"%d\", (n >> i) & 1);  prints", ["00000101", "10100000", "101", "5"], 0, "The 8 bits of 5, most significant first."),
    ("The value of  (1 << 4) − 1  is", ["15 (binary 1111)", "16", "8", "3"], 0, "A mask of the lowest k bits is (1 << k) − 1."),
    ("((x & 0x0F) << 4) | ((x & 0xF0) >> 4)  for x = 0x5A gives", ["0xA5", "0x5A", "0xFF", "0x00"], 0, "It swaps the two nibbles of a byte."),
    ("If x = 3, then after  x <<= 2;  x is", ["12", "6", "5", "1"], 0, "3 × 4."),
    ("Dividing a non-negative int x by 8 can be written as", ["x >> 3", "x << 3", "x >> 8", "x & 8"], 0, "8 = 2³."),
    ("The right operand of << or >> must be", ["A non-negative integer smaller than the width of the left operand", "Any float", "Negative for a right shift",
                                               "A character"], 0, "Otherwise the behaviour is undefined."),
    ("(x << 3) + (x << 1) equals", ["10x", "11x", "6x", "24x"], 0, "8x + 2x."),
    ("The value of  0xFF >> 4  is", ["15", "240", "16", "4"], 0, "11111111 → 00001111."),
    ("On a compiler with arithmetic right shift, −8 >> 1 gives", ["−4", "4", "2147483644", "−16"], 0, "The sign bit is copied."),
    ("For a 32-bit int x, the value of  (x >> 31) & 1  is", ["1 if x is negative, 0 otherwise", "The lowest bit of x", "x / 31", "Always 0"], 0, "Bit 31 is the sign bit."),
    ("After  x = 1; x <<= 3; x |= 1;  x is", ["9", "8", "4", "16"], 0, "1 → 8 → 1001."),
    ("For  unsigned char c = 200;  the value of  (unsigned char)(c << 1)  is", ["144", "400", "100", "0"], 0, "400 − 256 = 144 (the top bit is lost)."),
    ("What is printed?\nint n = 40, k = 0;\nwhile (n) { n >>= 1; k++; }\nprintf(\"%d\", k);", ["6", "5", "40", "3"], 0, "40 = 101000 has 6 significant bits."),
    ("With  #define READ 1,  #define WRITE 2,  #define EXEC 4  and  perm = READ | EXEC;  the value of  perm & WRITE  is", ["0 – no write permission", "2", "5", "1"], 0,
     PYQ + "perm = 101; WRITE = 010."),
    ("The value of  3 >> 1 << 1  is", ["2", "3", "6", "1"], 0, "Left to right: 3 >> 1 = 1, 1 << 1 = 2 (the lowest bit is lost)."),
]

TOPICS = {
    "Structures and Unions": [
        ("1 · Structures – Declaration, Accessing Elements, Arrays of Structures, Nested Structures and Pointers", STRUCTURES),
        ("2 · Unions, typedef, enum and Bit Fields", UNIONS_ENUM),
    ],
    "Bitwise Operators": [
        ("1 · Bitwise AND, OR, Exclusive OR and Complement", BITWISE_LOGIC),
        ("2 · Right Shift and Left Shift Operators and Bit Manipulation", SHIFTS),
    ],
}

NOTES = {
    "Structures and Unions": [{"title": "Structures and unions – revision sheet", "md": """## Structures
- `struct student { int roll; char name[20]; };` defines a type (no memory) → `struct student s1, s[50];`
- Access: `s1.roll`; pointer `p->roll` = `(*p).roll` (`*p.x` means `*(p.x)`); arrays of structures `e[2].salary`; nested `v.in.y`
- Initialise `{3, 4}` (missing members 0); C99 designated `{.y = 5, .x = 2}`
- Assignment `s1 = s2` copies all members; `==` between structures is not allowed; strings: `strcpy(s.name, "Ravi")`
- Passed/returned by value (a copy) – pass a pointer for large structures
- sizeof may exceed the sum of members (padding): `{char c; int i;}` = 8; `{char a; char b; int c;}` = 8 vs `{char a; int c; char b;}` = 12
- Self-referential structure `struct node { int data; struct node *next; };` → linked lists

## Unions
- All members share one memory location; size = largest member (rounded up for alignment); one member valid at a time
- `union { int i; char c[4]; }` = 4; `union { int a[10]; char y; }` = 40; `{char a[10]; int b; double c;}` = 16
- Initialiser sets the first member; tagged union = struct { tag; union {...}; }

## typedef, enum, bit fields
- `typedef unsigned long ulong;` alias (no memory); `typedef char *String; String a, b;` → two pointers (but `#define String char *` → b is a char)
- `enum color { RED, GREEN, BLUE };` → 0, 1, 2; `enum { A = 5, B, C = 10, D }` → B = 6, D = 11; enumerators are int, may repeat values
- Bit fields: `unsigned int a : 3;` → 0…7; no `&`, no arrays of bit fields; values wrap (5 in 2 bits → 1); used for flags and hardware registers
"""}],
    "Bitwise Operators": [{"title": "Bitwise operators – revision sheet", "md": """## Operators
| Op | Name | Example (12 = 1100, 10 = 1010) |
|---|---|---|
| `&` | AND | 12 & 10 = 8 |
| `|` | OR | 12 | 10 = 14 |
| `^` | XOR | 12 ^ 10 = 6 |
| `~` | complement (unary) | ~5 = −6, ~0 = −1 |
| `<<` | left shift (× 2ⁿ) | 5 << 2 = 20 |
| `>>` | right shift (÷ 2ⁿ) | 100 >> 3 = 12 |
- Integer operands only; precedence: shifts < `+ -`; `&` > `^` > `|`, all below `==` (so `a & b == c` is `a & (b == c)`)
- `5 & 2` = 0 but `5 && 2` = 1; `7 & 3 | 8` = 11; `1 << 2 + 1` = 8; `(x << 1) + (x >> 1)` with x = 2 → 5

## Bit tricks
- Test odd: `n & 1`; bit k: `(x >> k) & 1`
- Set `x | (1 << k)`; clear `x & ~(1 << k)`; toggle `x ^ (1 << k)`
- Power of two: `(n & (n − 1)) == 0`; count 1 bits: `c += n & 1; n >>= 1;`
- Mask of k ones: `(1 << k) − 1`; low nibble `x & 0x0F`; swap nibbles `((x & 0x0F) << 4) | ((x & 0xF0) >> 4)`
- XOR swap `a ^= b; b ^= a; a ^= b;`; `x ^ x = 0`; `x ^ k ^ k = x`
- Right shift of a negative signed value is implementation-defined (usually arithmetic); shifting by ≥ width is undefined
"""}],
}
