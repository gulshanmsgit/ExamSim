"""KRIES Computer Teacher · Computer Fundamentals and C Programming · P2-KRC-01 Introduction to C Programming and P2-KRC-02 C Instructions
(2 topics × 2 sets × 30), with revision NOTES. Owner's request (13 Oct 2026): one topic per heading of the KRIES C syllabus, previous-year
and previous-year-pattern questions. Each set PULLS the matching GPSTR questions of 'Programming in C – Part 1' (tools/p2u4_b.py – they
repeat by design, see REUSE in check_packs.py), adds REAL previous-year questions (exact wording, printed option order, `source`) and new
questions. Official answers: KEA final keys for GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1). KSET/KEA questions come from
packs/pyq-p2.json; PGCET answers were worked out by ExamSim (options read from the page images). References: Kernighan & Ritchie,
The C Programming Language; Yashavant Kanetkar, Let Us C; E. Balagurusamy, Programming in ANSI C. Every output was traced by hand."""
from p2u4_b import TOKENS as T, SEQUENCE as S
from p2u7_a import kset, PYQ, GTTC, NOTE

HISTORY_STRUCTURE = [
    T[2], T[11], T[14], T[16], T[26],
    ("C was developed by", ["Dennis Ritchie at AT&T Bell Laboratories (1972)", "Ken Thompson at MIT", "Bjarne Stroustrup at Bell Labs", "James Gosling at Sun Microsystems"], 0,
     PYQ + "Stroustrup created C++, Gosling created Java."),
    ("C was developed from which earlier language?", ["B (itself derived from BCPL)", "Pascal", "FORTRAN", "COBOL"], 0,
     "BCPL (Martin Richards) → B (Ken Thompson) → C (Dennis Ritchie)."),
    ("C was originally developed to write", ["The UNIX operating system", "MS-DOS", "Windows", "The Java virtual machine"], 0, "UNIX was rewritten in C in 1973."),
    ("C is often called a middle-level language because it", ["Combines high-level constructs with low-level features such as pointers and bit operations",
                                                              "Lies halfway between assembly and machine code", "Has no data types", "Runs only on medium-sized computers"], 0,
     PYQ + "It is used for both system and application programs."),
    ("The first ANSI standard for C (C89) was approved in", ["1989", "1972", "1978", "1999"], 0, "C89/C90; later C99, C11, C17."),
    ("The book 'The C Programming Language' (1978), which defined K&R C, was written by", ["Brian Kernighan and Dennis Ritchie", "Ken Thompson and Dennis Ritchie",
                                                                                            "Kernighan and Pike", "Ritchie and Stroustrup"], 0, "Hence 'K&R C'."),
    ("Execution of every C program begins with", ["The main() function", "The first function written in the file", "The #include line", "The last function in the file"], 0,
     PYQ + "A program has exactly one main()."),
    ("Every C statement is terminated by a", ["Semicolon (;)", "Colon (:)", "Full stop (.)", "Comma (,)"], 0, "A block { } needs no semicolon after it."),
    ("A multi-line comment in C is written as", ["/* comment */", "// comment //", "<!-- comment -->", "# comment"], 0, "// single-line comments came with C99 (and C++)."),
    ("In the usual structure of a C program, which section comes first?", ["Documentation (comment) section", "main() function", "User-defined functions",
                                                                           "Global declarations"], 0,
     "Documentation → link (#include) → definition (#define) → global declarations → main() → subprograms."),
    ("The #include <stdio.h> lines of a C program form the", ["Link section", "Definition section", "Global declaration section", "Subprogram section"], 0,
     "#define lines form the definition section."),
    ("The correct order of steps in building a C program is", ["Preprocessing → compiling → assembling → linking", "Compiling → preprocessing → linking → assembling",
                                                               "Linking → compiling → preprocessing → assembling", "Assembling → compiling → linking → preprocessing"], 0,
     PYQ + ".c → .i → .s → .o/.obj → executable."),
    ("On Windows, a compiled and linked C program is saved as a file with extension", [".exe", ".c", ".h", ".i"], 0, ".c = source, .h = header, .obj = object file."),
    ("The C character set consists of", ["Letters, digits, special characters and white spaces", "Letters and digits alone", "Keywords and identifiers",
                                        "ASCII control codes alone"], 0, "Tokens are built from these characters."),
    ("Which character is NOT part of the basic C source character set?", ["@", "#", "_", "~"], 0, PYQ + "$, @ and ` are outside the basic source character set."),
    ("Which escape sequence moves the cursor to the beginning of the next line?", ["\\n", "\\t", "\\b", "\\r"], 0, "\\t = tab, \\b = backspace, \\r = carriage return."),
    ("The escape sequence \\0 represents", ["The null character (ASCII 0)", "The digit zero", "A tab", "End of file"], 0, "It ends every C string; '0' is ASCII 48."),
    ("The smallest individual units of a C program are called", ["Tokens", "Statements", "Functions", "Blocks"], 0,
     "Keywords, identifiers, constants, strings, operators and special symbols."),
    ("Extra spaces, tabs and newlines between tokens in C source code are", ["Ignored by the compiler (except inside strings and character constants)", "Errors",
                                                                             "Treated as zero", "Comments that must be closed"], 0, "C is free-form."),
    ("Why does  Printf(\"Hi\");  fail to build in C?", ["C is case-sensitive, so Printf is not the library function printf", "Printf needs two arguments",
                                                       "Strings must use single quotes", "A semicolon is missing"], 0, "The linker finds no function named Printf."),
    ("In  int main() { … return 0; }  the value 0 returned to the operating system indicates", ["Successful termination", "An error", "That the program restarts",
                                                                                               "Nothing at all"], 0, "A non-zero value usually signals an error."),
    ("printf() and scanf() are declared in the header file", ["<stdio.h>", "<conio.h>", "<math.h>", "<string.h>"], 0, "stdio = standard input-output."),
    ("C programs are normally", ["Compiled into machine code before they run", "Interpreted line by line", "Run on a virtual machine like Java", "Run only as scripts"], 0,
     "Hence C programs run fast."),
    ("The linker in C", ["Combines object code with library code to produce an executable", "Removes comments", "Checks syntax", "Expands macros"], 0,
     "The preprocessor removes comments and expands macros."),
    ("C programs are called portable because", ["The same source can be compiled and run on different machines with little or no change", "They need no compilation",
                                                "They need no operating system", "They are small"], 0, "Machine-dependent parts are kept in libraries."),
]

CONSTANTS_TYPES = [
    T[0], T[1], T[3], T[4], T[5], T[6], T[7], T[10], T[13], T[19], T[20], T[22], T[23], T[24], T[28], T[29],
    ("Which of the following is true for variable names in 'C'-programming?",
     ["They can contain alphanumeric characters as well as special character", "It is not an error to declare a variable to be one of the keywords",
      "Variable names cannot start with a digit", "Variable can be of any length"], 2,
     "Only letters, digits and _ are allowed, a keyword cannot be a name, and only the first 31 characters are significant." + GTTC, "GTTC 2024 Lecturer CS · Q16"),
    ("What is the purpose of a string data type in C programming?", ["To store numerical values", "To store True/False values", "To store Text and characters",
                                                                     "To perform mathematical operations"], 2,
     "A C string is a char array ending in '\\0'." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q88"),
    ("Integer, real and character constants are called", ["Primary constants", "Secondary constants", "Derived constants", "Enumeration constants"], 0,
     "Secondary constants: arrays, pointers, structures, unions, enums (Kanetkar)."),
    ("Which is a valid integer constant in C?", ["-275", "27,500", "27 500", "2.75E2"], 0, "No commas or spaces; 2.75E2 is a real constant."),
    ("In the real constant 3.2e-5, the part after 'e' is the", ["Exponent", "Mantissa", "Base", "Suffix"], 0, "3.2 × 10⁻⁵: 3.2 is the mantissa."),
    ("Which is a valid character constant?", ["'A'", "\"A\"", "'AB'", "A"], 0, "\"A\" is a string literal (two bytes: 'A' and '\\0')."),
    ("Which of these is NOT a keyword in C?", ["main", "auto", "volatile", "goto"], 0, PYQ + "main is a function name, not a keyword."),
    ("Variable names in C may contain", ["Letters, digits and underscores, but must not begin with a digit", "Any characters including spaces", "Letters alone",
                                         "Letters and hyphens"], 0, "total_marks is valid; 2nd, total-marks and total marks are not."),
    ("On a 16-bit compiler such as Turbo C, the range of int is", ["−32768 to +32767", "−32767 to +32768", "0 to 65535", "−2147483648 to +2147483647"], 0,
     PYQ + "2 bytes: −2¹⁵ … 2¹⁵ − 1; unsigned int: 0 … 65535."),
    ("Typical sizes of float and double are", ["4 and 8 bytes", "2 and 4 bytes", "8 and 16 bytes", "4 and 4 bytes"], 0, "long double is usually 10, 12 or 16 bytes."),
    ("The printf/scanf format specifier for a long int is", ["%ld", "%lf", "%Lf", "%u"], 0, "%lf = double (scanf), %Lf = long double, %u = unsigned int."),
    ("A named value that cannot be changed while the program runs can be created with", ["const or #define", "static", "auto", "volatile"], 0,
     "const int MAX = 10;  or  #define MAX 10 (symbolic constant)."),
    ("int a, b = 5;  declares", ["Two int variables, of which only b is initialised to 5", "Two variables both set to 5", "An error",
                                "a as 5 and b uninitialised"], 0, "Each initialiser applies to one variable."),
    ("The data type void means", ["No value – e.g. a function that returns nothing", "Zero", "An empty string", "Any integer"], 0,
     "void * is a generic pointer."),
]

ARITHMETIC = [
    T[8], T[9], T[18], T[27], S[0], S[1], S[2], S[3],
    ("In C, instructions are of three types:", ["Type declaration, arithmetic and control instructions", "Input, output and process", "Load, store and branch",
                                               "Compile, link and run"], 0, PYQ + "Kanetkar, Let Us C."),
    ("Which arithmetic instruction is INVALID in C?", ["a + b = c;", "c = a + b;", "c = a * b + 3;", "c = (a + b) / 2;"], 0,
     "The left side of = must be a variable (an lvalue)."),
    ("What is the value of 5 / 2 in C?", ["2", "2.5", "3", "2.0"], 0, "int / int gives an int; the fraction is dropped."),
    ("What is the value of 5.0 / 2 in C?", ["2.5", "2", "3", "0"], 0, "One real operand makes it real division."),
    ("After  float a = 5 / 2;  a holds", ["2.000000", "2.500000", "3.000000", "0.000000"], 0,
     PYQ + "5 / 2 is evaluated as int (2) first, then converted to float."),
    ("After  int k = 7.9 / 2;  k holds", ["3", "3.95", "4", "7"], 0, "7.9 / 2 = 3.95; assigning to int truncates it."),
    ("In  i + f  (int i, float f), the type of the result is", ["float, because the int is converted", "int", "always double", "char"], 0,
     "Usual arithmetic conversions: the 'lower' type is promoted."),
    ("With  int a = 7, b = 2;  the value of  (float) a / b  is", ["3.5", "3.0", "3", "4"], 0, "The cast applies to a only, so the division is real."),
    ("With  int a = 7, b = 2;  the value of  (float) (a / b)  is", ["3.0", "3.5", "4.0", "0.0"], 0, "a / b = 3 (int) is computed first, then cast."),
    ("After  char ch = 321;  (8-bit char) ch holds", ["65, i.e. 'A' (321 − 256)", "321", "0", "A compile-time error"], 0,
     "Only the low 8 bits are kept when an int is assigned to a char."),
    ("Which use of the % operator is INVALID in C?", ["7.5 % 2", "7 % 2", "-7 % 2", "7 % -2"], 0, "% needs integer operands; use fmod() for reals."),
    ("To compute a raised to the power b in C, one uses", ["pow(a, b) from <math.h>", "a ^ b", "a ** b", "exp(a, b)"], 0,
     PYQ + "^ is bitwise XOR in C; C has no exponent operator."),
    ("The value of  'a' + 1  (ASCII) is", ["98", "97", "65", "An error"], 0, "A char takes part in arithmetic as its code ('a' = 97)."),
    ("On a 16-bit compiler, after  int x = 32767; x = x + 1;  x is", ["−32768 (it wraps around)", "32768", "0", "An error"], 0,
     "Signed overflow is formally undefined, but such compilers wrap around."),
    ("If a = 4, then after  a *= 2 + 3;  a is", ["20", "11", "14", "24"], 0, "a = a * (2 + 3): the right side is evaluated first."),
    ("The value of  3 / 2 * 2.0  is", ["2.0", "3.0", "1.5", "2.5"], 0, "3 / 2 = 1 (int), then 1 * 2.0 = 2.0."),
    ("The value of  2 * 3 / 4 + 4 / 4 + 8 - 2 + 5 / 8  (int arithmetic) is", ["8", "9", "7", "8.625"], 0,
     PYQ + "6 / 4 = 1; 4 / 4 = 1; 5 / 8 = 0 → 1 + 1 + 8 − 2 + 0 = 8."),
    ("Which declaration is INVALID in C (all inside one function)?", ["int a = b = 5;  (b not declared before)", "int a = 5, b = a;", "float x = 1.5;", "char c = 'z';"], 0,
     "A variable must be declared before it is used."),
    ("In  k = 3 + 2 % 5 - 1;  k is", ["4", "0", "5", "2"], 0, "2 % 5 = 2 → 3 + 2 − 1 = 4."),
    ("In an expression with an int and a double operand, the int is converted to", ["double", "float", "long", "char"], 0, "char < int < long < float < double."),
    ("With 32-bit int, the expression  -1 < 1u  evaluates to", ["0 (false) – −1 is converted to a large unsigned value", "1 (true)", "A compile-time error",
                                                               "A random value"], 0, PYQ + "-1 becomes 4294967295 when compared with an unsigned int."),
    ("The correct way to cast x to int in C is", ["(int) x", "int: x", "x as int", "<int> x"], 0, "(type) expression."),
]

OPERATORS_IO = [
    T[12], T[15], T[17], T[21], T[25], S[4], S[5], S[6], S[7], S[8], S[9], S[17], S[18], S[24], S[25], S[26], S[27],
    kset("KSET 2023 CS&A · Q2"),
    kset("KEA 2026 CS Paper-2 · Q81"),
    ("What will be the output of the following program ?\n#include<stdio.h>\nvoid main( )\n{\n  int a = printf (\"happy\");\n  printf (\"%d\", a);\n}",
     ["happy", "happy5", "happy1", "error"], 1, "printf returns the number of characters printed (5)." + NOTE, "PGCET 2024 M.Tech CS · Q91"),
    ("Which of these are unformatted console input-output functions?", ["getchar(), putchar(), gets(), puts()", "printf() and scanf()", "fprintf() and fscanf()",
                                                                        "sprintf() and sscanf()"], 0, PYQ + "printf/scanf are formatted I/O (they use format strings)."),
    ("In  scanf(\"%d\", &n);  the & is needed because", ["scanf must receive the address of n to store the value there", "& means 'and'", "n is already a pointer",
                                                        "It converts n to int"], 0, "For a char array (string) the name itself is an address."),
    ("printf(\"%5.2f\", 3.14159) prints", ["' 3.14' (width 5, two decimals)", "'3.14159'", "'3.1'", "'03.14'"], 0, "The number is right-justified in 5 columns."),
    ("printf(\"%-5d|\", 42) prints", ["'42   |' (left-justified in width 5)", "'   42|'", "'00042|'", "'42|'"], 0, "'-' left-justifies; '0' pads with zeros."),
    ("scanf(\"%s\", s) reads", ["Characters up to the first white space", "A whole line including spaces", "Exactly one character", "Digits alone"], 0,
     "Use fgets() (or gets(), now removed) to read a line with spaces."),
    ("scanf() returns", ["The number of input items successfully read", "The value read", "Always 0", "The number of characters typed"], 0, "EOF at end of input."),
    ("Which operator has the highest precedence?", ["*", "+", "&&", "="], 0, "Arithmetic > relational > logical > assignment."),
    ("The value of  !5 + 3  is", ["3", "4", "8", "0"], 0, "!5 = 0 (any non-zero value is true), and ! binds tighter than +."),
    ("The value of  10 + 20 * 3 / 4 % 5  is", ["10", "25", "12", "13"], 0, PYQ + "* / % left to right: 60 / 4 = 15, 15 % 5 = 0 → 10."),
    ("To print a % sign with printf, the format string uses", ["%%", "\\%", "%c", "/%"], 0, "printf(\"50%%\") prints 50%."),
]

TOPICS = {
    "Introduction to C Programming": [
        ("1 · History, Structure of a C Program and the Character Set", HISTORY_STRUCTURE),
        ("2 · Constants, Variables, Keywords and Data Types", CONSTANTS_TYPES),
    ],
    "C Instructions": [
        ("1 · Type Declaration, Arithmetic Instructions and Type Conversion", ARITHMETIC),
        ("2 · Operators, Hierarchy of Operators and Input-Output Statements", OPERATORS_IO),
    ],
}

NOTES = {
    "Introduction to C Programming": [{"title": "Introduction to C – revision sheet", "md": """## History
- BCPL (Martin Richards, 1967) → B (Ken Thompson, 1970) → **C (Dennis Ritchie, AT&T Bell Labs, 1972)**, written for UNIX
- K&R C (Kernighan & Ritchie book, 1978); ANSI C89 / ISO C90; C99 (// comments, long long, bool); C11; C17
- Middle-level language: high-level constructs + pointers, bit operations; portable; compiled; case-sensitive

## Structure of a C program
1. Documentation (comments `/* … */`)  2. Link section (`#include <stdio.h>`)  3. Definition (`#define PI 3.14`)
4. Global declarations  5. `main()` – execution starts here (exactly one)  6. User-defined functions
- Every statement ends with `;`; `return 0;` = success
- Build: preprocess (.i) → compile (.s) → assemble (.o/.obj) → link (.exe/a.out)

## Character set and tokens
- Letters, digits, special characters, white space (not in basic set: `$ @ \\``)
- Escape sequences: `\\n` newline, `\\t` tab, `\\b` backspace, `\\r` carriage return, `\\0` null, `\\\\` backslash, `\\'`, `\\"`
- Tokens: keywords (32 in C89), identifiers, constants, strings, operators, special symbols

## Constants, variables, data types
- Primary constants: integer (`-275`, `010` octal = 8, `0x1F` = 31), real (`3.2e-5`, type double), character (`'A'` = 65)
- Secondary: arrays, pointers, structures, unions, enums
- Identifiers: letters, digits, `_`; not starting with a digit; not a keyword; case-sensitive
- Sizes (typical 32-bit): char 1, short 2, int 4 (Turbo C: 2 → −32768…32767), long 4/8, float 4, double 8
- signed char −128…127; unsigned char 0…255; `sizeof('A')` = sizeof(int) in C
- Format specifiers: %d %i int, %u unsigned, %ld long, %f float/double (printf), %lf double (scanf), %c char, %s string, %o octal, %x hex, %e, %p pointer
- Constants: `const int N = 10;` or `#define N 10`; `void` = no value
"""}],
    "C Instructions": [{"title": "C instructions and operators – revision sheet", "md": """## Instructions (Kanetkar)
- Type declaration, arithmetic, control instructions
- Arithmetic: variable on the left (`a + b = c` is invalid); `%` only for integers; no power operator – `pow()`
- int / int → int (5 / 2 = 2); one real operand → real (5.0 / 2 = 2.5); `float a = 5 / 2` → 2.0
- Assignment converts: `int k = 7.9 / 2` → 3; `char ch = 321` → 65
- Casts: `(float) a / b` = 3.5 but `(float)(a / b)` = 3.0 (a = 7, b = 2)
- C99: −7 / 2 = −3, −7 % 2 = −1 (sign of the dividend)

## Hierarchy of operators (high → low)
| Level | Operators | Assoc. |
|---|---|---|
| Postfix | `() [] -> .` `x++` | L→R |
| Unary | `! ~ ++ -- + - * & sizeof (type)` | R→L |
| Multiplicative | `* / %` | L→R |
| Additive | `+ -` | L→R |
| Shift | `<< >>` | L→R |
| Relational | `< <= > >=` | L→R |
| Equality | `== !=` | L→R |
| Bitwise | `&` then `^` then `|` | L→R |
| Logical | `&&` then `||` | L→R |
| Conditional | `?:` | R→L |
| Assignment | `= += -= …` | R→L |
| Comma | `,` | L→R |
- `&&` / `||` short-circuit; `5 > 3 > 1` = 0; `a & b == c` = `a & (b == c)`; `x = (1, 2, 3)` = 3
- Worked: `2*3/4 + 4/4 + 8 - 2 + 5/8` = 8; `10 + 20*3/4%5` = 10

## Input-output
- Formatted: `printf`, `scanf` (needs `&var`; returns the count read; `%s` stops at white space)
- Unformatted: `getchar putchar gets puts` (`getch getche` in conio.h)
- printf returns the number of characters printed (`printf("happy")` → 5); `%5.2f`, `%-5d`, `%%`
"""}],
}
