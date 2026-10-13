"""KRIES Computer Teacher · C Programming · P2-KRC-03 Control Structures and P2-KRC-04 Arrays (2 topics × 2 sets × 30), with NOTES.
Pulls the matching GPSTR questions of 'Programming in C – Part 1' (tools/p2u4_b.py), adds REAL previous-year questions (exact wording,
printed option order, `source`) and new ones. Official answers: KEA final keys for Legislative Council Secretariat 2024 (Sr/Jr Programmer
P2 – A1) and GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1). KSET/KEA questions come from packs/pyq-p2.json; PGCET answers were
worked out by ExamSim (code read from the page images). Every output, bubble-sort pass and address was traced by hand."""
from p2u4_b import SEQUENCE as S, ARRAYS_STRINGS as A
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

DECISION = [
    ("What is the output of the following program ?\n#include<stdio.h>\nvoid main( )\n{\n  int x = 1;\n  if (x > 0)\n    printf(\"inside if\\t\");\n  else if (x > 0)\n"
     "    printf(\"inside else if\\t\");\n}", ["inside if", "inside else if", "inside if inside else if", "error"], 0,
     "Only the first true branch of an if-else-if chain runs." + NOTE, "PGCET 2024 M.Tech CS · Q90"),
    ("What is printed?\nint x = 0;\nif (x = 5) printf(\"yes\"); else printf(\"no\");", ["yes", "no", "Compile error", "Nothing"], 0,
     PYQ + "x = 5 assigns 5; the condition's value is 5, which is true."),
    ("What is printed?\nint a = 0, b = 1;\nif (a)\n  if (b) printf(\"X\");\n  else printf(\"Y\");", ["Nothing", "X", "Y", "XY"], 0,
     PYQ + "Dangling else: else pairs with the nearest if (if (b)), which is never reached because a is 0."),
    ("What is printed?\nint a = 1, b = 5;\nif (a > b);\n  printf(\"Hello\");", ["Hello – the ; ends the if, so printf always runs", "Nothing", "Compile error", "Hello twice"], 0,
     "if (a > b); has an empty statement as its body."),
    ("The value of  (5 > 3) + (2 == 2)  is", ["2", "1", "0", "true"], 0, "Each relational expression gives 1 (true) or 0 (false)."),
    ("The value of  !(4 < 3) && (2 != 2)  is", ["0", "1", "−1", "2"], 0, "!(0) = 1; (2 != 2) = 0; 1 && 0 = 0."),
    ("abs = n < 0 ? -n : n;  with n = −8 gives abs =", ["8", "−8", "0", "1"], 0, "The conditional operator picks −n when n is negative."),
    ("What is printed?\nint n = 0;\nprintf(\"%s\", n > 0 ? \"pos\" : n < 0 ? \"neg\" : \"zero\");", ["zero", "pos", "neg", "Compile error"], 0,
     "?: is right-associative: n > 0 ? \"pos\" : (n < 0 ? \"neg\" : \"zero\")."),
    ("What is printed?\nfloat f = 0.1;\nif (f == 0.1) printf(\"Equal\"); else printf(\"Not equal\");", ["Not equal", "Equal", "Compile error", "Nothing"], 0,
     PYQ + "0.1 is a double constant; the float copy is less precise, so they differ. Compare reals with a tolerance."),
    ("What is printed?\nint m = 72;\nif (m >= 80) printf(\"A\");\nelse if (m >= 60) printf(\"B\");\nelse if (m >= 40) printf(\"C\");\nelse printf(\"F\");",
     ["B", "A", "C", "BC"], 0, "The first true condition (m >= 60) is taken and the rest are skipped."),
    ("Which expression checks that x lies between 10 and 20 (both inclusive)?", ["x >= 10 && x <= 20", "10 <= x <= 20", "x >= 10 || x <= 20", "x > 10 & x < 20"], 0,
     "10 <= x <= 20 is (10 <= x) <= 20, which is always true."),
    ("What is printed?\nint i = 0, j = 0;\nif (i++ || j++) ;\nprintf(\"%d %d\", i, j);", ["1 1", "1 0", "0 1", "0 0"], 0,
     "i++ gives 0 (false), so || must evaluate j++ too; both become 1."),
    ("What is printed?\nint i = 1, j = 0;\nif (i++ && j++) ;\nprintf(\"%d %d\", i, j);", ["2 1", "2 0", "1 1", "1 0"], 0,
     "i++ gives 1 (true), so && evaluates j++ as well."),
    ("What is printed?\nif (-1) printf(\"T\"); else printf(\"F\");", ["T", "F", "Compile error", "Nothing"], 0, "Any non-zero value, even negative, is true."),
    ("The conditional operator ?: takes how many operands?", ["Three", "Two", "One", "Four"], 0, "It is C's only ternary operator."),
    ("Which operator tests two values for equality in C?", ["==", "=", "===", "eq"], 0, "= is assignment."),
    ("What is printed?\nint x = 5;\nif (x > 10)\n  printf(\"A\");\n  printf(\"B\");", ["B", "AB", "A", "Nothing"], 0,
     PYQ + "Without braces, only the first statement belongs to the if."),
    ("The expression  !a == b  is evaluated as", ["(!a) == b", "!(a == b)", "a != b", "A compile-time error"], 0, "Unary ! has higher precedence than ==."),
    ("!(a > 5 && b < 3) is equivalent to", ["a <= 5 || b >= 3", "a <= 5 && b >= 3", "a > 5 || b < 3", "a < 5 || b > 3"], 0, "De Morgan's law."),
    ("The condition  ch >= 'a' && ch <= 'z'  is true when ch is", ["A lowercase letter", "An uppercase letter", "A digit", "Any letter"], 0,
     "Lowercase letters have consecutive ASCII codes 97–122."),
    ("Which condition is true exactly when n is even?", ["n % 2 == 0", "n / 2 == 0", "n % 2 == 1", "n & 2 == 0"], 0, "n & 1 == 0 also works ((n & 1) == 0)."),
    ("Which condition correctly tests whether year y is a leap year?", ["(y % 4 == 0 && y % 100 != 0) || y % 400 == 0", "y % 4 == 0",
                                                                         "y % 100 == 0 && y % 400 != 0", "y % 4 == 0 || y % 100 == 0"], 0,
     PYQ + "1900 is not a leap year; 2000 is."),
    ("In C, the value of a relational expression such as a < b is", ["1 for true or 0 for false, of type int", "true or false of type bool", "−1 for true",
                                                                       "Any non-zero value"], 0, "C99's _Bool came later; relational results are still int."),
    ("An if-else ladder is preferred over switch when", ["The conditions involve ranges or non-integer comparisons", "One int variable is compared with constants",
                                                         "Menu choices are numbered", "There are more than two cases"], 0, "switch tests equality with integer constants only."),
    ("What is printed?\nint a = 10, b = 20, c = 15;\nif (a > b) { if (a > c) printf(\"a\"); else printf(\"c\"); }\nelse { if (b > c) printf(\"b\"); else printf(\"c\"); }",
     ["b", "a", "c", "bc"], 0, "a > b is false; in the else part b > c is true."),
    ("What is printed?\nprintf(\"%d\", 'A' < 'a');", ["1", "0", "65", "97"], 0, "'A' = 65 and 'a' = 97."),
    ("What is printed?\nint x = 0, y = 5;\nif (x = y == 5) printf(\"%d\", x);", ["1", "5", "0", "Nothing"], 0,
     PYQ + "== binds tighter than =: x = (y == 5) = 1, which is true."),
    ("What is printed?\nint a = 5, b = 5;\nif (a == b) printf(\"same\"); else printf(\"diff\");\nprintf(\"%d\", a != b);", ["same0", "same1", "diff0", "diff1"], 0,
     "a == b is true; a != b is 0."),
    ("C's logical operators are", ["&&, || and !", "&, | and ^", "and, or and not", "&&, || and ^^"], 0, "&, | and ^ are bitwise operators."),
    ("Which is a valid C if statement?", ["if (a > b) max = a;", "if a > b then max = a;", "if (a > b) then max = a;", "if a > b: max = a"], 0,
     "The condition must be in parentheses; there is no 'then'."),
]

LOOPS = [
    S[12], S[13], S[14], S[15], S[16], S[19], S[20], S[23], S[28], S[29],
    kset("KSET 2024 CS&A · Q21"),
    kset("KEA 2026 CS Paper-2 · Q85"),
    ("What is the output of the following program ?\n#include<stdio.h>\nvoid main( )\n{\n  int i;\n  for (i = 1; i <= 5; i++)\n  {\n    if (i == 3)\n      continue;\n"
     "    printf(\"%d\\t\", i);\n  }\n}", ["1 2", "1 2 3 4 5", "3 4 5", "1 2 4 5"], 3, "continue skips the printf only when i is 3." + NOTE,
     "PGCET 2024 M.Tech CS · Q97"),
    ("In the given loop construct, which one is executed only once ?\nfor (exp1; exp2; exp3)", ["exp1", "exp1 and exp3", "exp3", "exp2"], 0,
     "exp1 initialises once; exp2 is tested before every iteration; exp3 runs after every iteration." + NOTE, "PGCET 2024 M.Tech CS · Q100"),
    ("What is the output of the following code?\nint main() {\n  for (; ;) {\n    printf(\"Hello\");\n  }\n  return 0;\n}",
     ["Compilation error", "Prints Hello 100 times", "Prints Hello infinitely", "Does not print Hello"], 2,
     "for (;;) has no condition, which counts as always true." + NOTE, "PGCET 2026 CS · Q92"),
    ("What is printed?\nint i = 5;\nwhile (i < 5) { printf(\"%d\", i); i++; }", ["Nothing", "5", "56789", "An infinite loop"], 0,
     "while tests first; the condition is false at the start."),
    ("What is printed?\nint i = 5;\ndo { printf(\"%d \", i); i++; } while (i < 5);", ["5", "Nothing", "5 6", "An infinite loop"], 0,
     "A do-while body runs once before the test."),
    ("What is printed?\nint s = 0, i;\nfor (i = 1; i <= 5; i++) s += i;\nprintf(\"%d\", s);", ["15", "10", "5", "21"], 0, "1 + 2 + 3 + 4 + 5."),
    ("What is printed?\nint i;\nfor (i = 0; i < 5; i++);\nprintf(\"%d\", i);", ["5", "01234", "0", "4"], 0,
     PYQ + "The ; after for( ) is an empty body; printf runs once after the loop, when i is 5."),
    ("What is printed?\nint i;\nfor (i = 10; i > 0; i -= 3) printf(\"%d \", i);", ["10 7 4 1", "10 7 4 1 -2", "10 7 4", "7 4 1"], 0, "i becomes −2, which stops the loop."),
    ("What is printed?\nint i;\nfor (i = 1; i <= 10; i++) { if (i == 4) break; printf(\"%d\", i); }", ["123", "1234", "12345678910", "4"], 0,
     "break leaves the loop when i reaches 4."),
    ("How many stars are printed?\nfor (i = 1; i <= 3; i++)\n  for (j = 1; j <= i; j++)\n    printf(\"*\");", ["6", "9", "3", "4"], 0, "1 + 2 + 3."),
    ("The goto statement is used to", ["Transfer control unconditionally to a labelled statement in the same function", "Call a function",
                                       "Exit the program", "Jump to another source file"], 0, "Its overuse makes code hard to follow."),
    ("What is printed?\nint i = 0;\nwhile (i < 5) { i++; if (i == 2) continue; printf(\"%d\", i); }", ["1345", "12345", "1", "2345"], 0,
     "i is incremented before continue, so the loop does not get stuck."),
    ("What is printed?\nswitch (5) {\n  default: printf(\"D\");\n  case 1: printf(\"1\"); break;\n  case 2: printf(\"2\");\n}", ["D1", "D", "D12", "Nothing"], 0,
     PYQ + "No case matches, so control goes to default and falls through into case 1 until break."),
    ("Which type is NOT allowed for the controlling expression of a switch?", ["float", "int", "char", "enum"], 0,
     PYQ + "switch needs an integer expression; case labels must be integer constants."),
    ("Two case labels with the same value in one switch cause", ["A compile-time error", "Only the first one to run", "Both to run", "A runtime error"], 0,
     "Case values must be distinct."),
    ("exit(0) called inside a loop", ["Terminates the whole program", "Leaves only the loop", "Skips one iteration", "Restarts the loop"], 0,
     "break leaves the loop; continue skips to the next iteration."),
    ("Which of these is an infinite loop?", ["while (1) { }", "for (i = 0; i < 1; i++) { }", "do { } while (0);", "while (0) { }"], 0,
     "for (;;) is another common form."),
    ("What is printed?\nint i = 0, c = 0;\nwhile (i++ < 5) c++;\nprintf(\"%d %d\", c, i);", ["5 6", "5 5", "6 6", "4 5"], 0,
     PYQ + "The test runs 6 times (i = 0…5); the last test fails but still increments i to 6."),
]

ARRAYS_1D_2D = [
    A[0], A[1], A[2], A[3], A[4], A[5], A[27], A[29],
    kset("KSET 2023 CS&A · Q3"),
    kset("KEA 2026 CS Paper-2 · Q82"),
    kset("KEA 2026 CS Paper-2 · Q84"),
    ("If an array is declared as int arr [50], then how many elements can it hold?", ["49", "51", "0", "50"], 3, "Indices 0 … 49." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q56"),
    ("Consider the following declaration of a 2D array in C:\nChar a [100] [100];\nAssuming that the main memory is byte addressable and that the array is stored starting "
     "from memory address 0, the address of a [40] [50] is", ["4040", "4050", "5040", "5050"], 1,
     "Row-major: 40 × 100 + 50 = 4050 (1 byte per char)." + GTTC, "GTTC 2024 Lecturer CS · Q9"),
    ("In many programming langauges what is the index of the first element in an array?", ["0", "1", "−1", "Size of the array"], 0, "C arrays start at index 0." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q87"),
    ("What is the output of the following program ?\n#include<stdio.h>\nvoid main( )\n{\n  int a[3][2] = {1, 2, 3, 4, 5, 6};\n  printf(\"%d, %d\", a[0][0], a[2][1]);\n}",
     ["1, 5", "1, 6", "2, 5", "2, 6"], 1, "Rows are filled in order: {1, 2}, {3, 4}, {5, 6}; a[2][1] = 6." + NOTE, "PGCET 2024 M.Tech CS · Q94"),
    ("Given the array [4, 3, 2, 1, 8, 7, 6, 5]. After two passes of Bubble Sort, what is the status of array while sorting in ascending order?",
     ["[3, 2, 1, 4, 7, 6, 5, 8]", "[4, 3, 2, 1, 8, 7, 6, 5]", "[1, 2, 3, 4, 5, 6, 7, 8]", "[2, 1, 3, 4, 6, 5, 7, 8]"], 3,
     "Pass 1 → 3 2 1 4 7 6 5 8; pass 2 → 2 1 3 4 6 5 7 8." + NOTE, "PGCET 2026 CS · Q95"),
    ("In a array, all elements are stored in ____ memory locations.", ["Random", "Sequential", "Shared", "None of the above"], 1,
     "Array elements are contiguous." + NOTE, "PGCET 2024 M.Tech CS · Q82"),
    ("Bubble sort of n elements needs at most how many passes?", ["n − 1", "n", "n/2", "log₂ n"], 0, "Each pass places one more element at the end."),
    ("For 6 elements, basic bubble sort makes how many comparisons in total?", ["15", "36", "30", "6"], 0, PYQ + "5 + 4 + 3 + 2 + 1 = n(n − 1)/2 = 15."),
    ("After the first pass of bubble sort in ascending order", ["The largest element is in the last position", "The smallest element is first",
                                                               "The array is sorted", "The middle element is in place"], 0, "It 'bubbles' to the end."),
    ("The array {5, 1, 4, 2, 8} after the first pass of bubble sort (ascending) is", ["1 4 2 5 8", "1 2 4 5 8", "5 1 4 2 8", "1 4 5 2 8"], 0,
     PYQ + "Swaps: (5,1), (5,4), (5,2); 5 and 8 stay."),
    ("Bubble sort with a 'swapped' flag on an already sorted array takes", ["O(n) – one pass with no swaps", "O(n²)", "O(log n)", "O(1)"], 0, "Worst and average case: O(n²)."),
    ("int a[3][4] starts at address 1000 with 4-byte int, stored row-major. The address of a[2][1] is", ["1036", "1024", "1032", "1044"], 0,
     PYQ + "1000 + (2 × 4 + 1) × 4 = 1036."),
    ("After  int a[2][3] = {{1}, {4, 5}};  the value of a[1][2] is", ["0", "5", "Garbage", "4"], 0, "Missing initialisers are set to 0."),
    ("For  int a[10];  the valid indices are", ["0 to 9", "1 to 10", "0 to 10", "1 to 9"], 0, "C does not check bounds."),
    ("Which array declaration is INVALID in C89 (but allowed as a variable-length array in C99)?", ["int n = 5; int a[n];", "int a[5];", "int a[] = {1, 2, 3};",
                                                                                                    "#define N 5 … int a[N];"], 0, "C89 needs a constant size."),
    ("For a 3 × 3 matrix a, the loop  for (i = 0; i < 3; i++) s += a[i][i];  computes", ["The sum of the main diagonal (trace)", "The sum of the first row",
                                                                                         "The sum of all elements", "The sum of the last column"], 0, "Elements with row = column."),
    ("The assignment  b[j][i] = a[i][j];  inside two nested loops stores in b", ["The transpose of a", "A copy of a", "The inverse of a", "The square of a"], 0,
     "Rows become columns."),
    ("How many elements does  int a[2][3][4];  have?", ["24", "9", "12", "234"], 0, "2 × 3 × 4."),
    ("In an expression, the name a of  int a[5];  stands for", ["&a[0], the address of the first element", "A copy of the whole array", "The value of a[0]",
                                                                 "The size of the array"], 0, "Except with sizeof and &."),
]

STRINGS = [
    A[6], A[7], A[8], A[9], A[10], A[19], A[20], A[21], A[22], A[23], A[28],
    kset("KEA 2026 CS Paper-2 · Q83"),
    ("What is the output of the following program ?\n#include<stdio.h>\n#include<string.h>\nvoid main()\n{\n  printf(\"%d%d\", sizeof (\"bengaluru\"),\n    strlen(\"bengaluru\"));\n}",
     ["9 9", "10 9", "10 10", "9 10"], 1, "sizeof counts the terminating '\\0' (10 bytes); strlen does not (9)." + NOTE, "PGCET 2024 M.Tech CS · Q86"),
    ("What is printed?\nchar s[10] = \"abc\";\nprintf(\"%d %d\", (int)sizeof(s), (int)strlen(s));", ["10 3", "3 3", "4 3", "10 10"], 0,
     PYQ + "sizeof gives the array size; strlen counts characters before '\\0'."),
    ("strcpy(s1, s2) copies", ["s2 into s1", "s1 into s2", "s2 to the end of s1", "Nothing – it compares them"], 0, "Destination first, like assignment s1 = s2."),
    ("strcmp(s1, s2) returns 0 when", ["The two strings are equal", "s1 is longer", "s1 is empty", "They differ"], 0,
     "A negative value if s1 < s2, positive if s1 > s2 (dictionary order)."),
    ("What is printed?\nchar s[20] = \"Good\";\nstrcat(s, \"Day\");\nputs(s);", ["GoodDay", "Good Day", "Good", "DayGood"], 0, "strcat appends without adding a space."),
    ("toupper() and isdigit() are declared in", ["<ctype.h>", "<string.h>", "<stdlib.h>", "<math.h>"], 0, "Character classification and conversion."),
    ("gets() was removed from C11 because it", ["Cannot limit the input size, so it can overflow the buffer", "Is too slow", "Reads only one character",
                                                "Needs a file pointer"], 0, "fgets(s, n, stdin) is the safe replacement."),
    ("strncpy(d, \"computer\", 3) copies", ["The first 3 characters \"com\" – no '\\0' is added automatically", "The string 3 times", "The last 3 characters", "Nothing"], 0,
     "The programmer must add d[3] = '\\0'."),
    ("What is printed?\nchar s[] = \"hello\";\nint n = 0;\nwhile (s[n] != '\\0') n++;\nprintf(\"%d\", n);", ["5", "6", "4", "0"], 0, "This loop is how strlen works."),
    ("For  char s[] = \"hi\";  sizeof(s) is", ["3", "2", "4", "1"], 0, "'h', 'i' and '\\0'."),
    ("char s[] = {'h', 'i'};  declares", ["A char array that is not a proper string (no '\\0')", "A string of length 2", "A string of length 3", "An error"], 0,
     "Passing it to printf(\"%s\") is unsafe."),
    ("What is printed?\nchar s[] = \"KARNATAKA\";\nprintf(\"%c%c\", s[0], s[4]);", ["KA", "KT", "KN", "AA"], 0, "K(0) A(1) R(2) N(3) A(4)."),
    ("For two char arrays s1 and s2,  if (s1 == s2)  compares", ["Their addresses, not their contents", "Their contents", "Their lengths", "Their first characters"], 0,
     PYQ + "Use strcmp(s1, s2) == 0 to compare contents."),
    ("sprintf(buf, \"%d\", 25);", ["Writes the characters \"25\" into buf", "Prints 25 on the screen", "Reads 25 from buf", "Writes 25 to a file"], 0,
     "sscanf reads from a string."),
    ("The value of  atoi(\"123\") + 1  is", ["124", "1231", "\"1231\"", "An error"], 0, "atoi (in <stdlib.h>) converts a string to int."),
    ("To check whether a string of length n is a palindrome, s[i] is compared with", ["s[n − 1 − i]", "s[n − i]", "s[i + 1]", "s[n / 2]"], 0,
     PYQ + "Compare from both ends towards the middle."),
    ("If ch holds a lowercase letter, ch − 32 gives", ["The same letter in uppercase", "The next letter", "A digit", "A space"], 0, "'a' (97) − 32 = 'A' (65)."),
    ("char names[5][20];  can store", ["5 strings of up to 19 characters each", "20 strings of 5 characters", "100 strings", "5 characters"], 0,
     "One byte of each row is needed for '\\0'."),
]

TOPICS = {
    "Control Structures": [
        ("1 · Decision Control – if, else, Logical, Relational and Conditional Operators", DECISION),
        ("2 · Loops – while, do-while, for, break, continue, switch-case and goto", LOOPS),
    ],
    "Arrays": [
        ("1 · One- and Multi-dimensional Arrays, Initialisation and Bubble Sort", ARRAYS_1D_2D),
        ("2 · Strings and String Library Functions", STRINGS),
    ],
}

NOTES = {
    "Control Structures": [{"title": "Control structures – revision sheet", "md": """## Decisions
- `if`, `if-else`, nested if, `else if` ladder; non-zero = true, 0 = false; relational results are 1/0 (int)
- Traps: `if (x = 5)` is always true; `if (a > b);` has an empty body; without braces only one statement belongs to the if
- **Dangling else** pairs with the nearest unmatched `if`
- `10 <= x <= 20` is always true – write `x >= 10 && x <= 20`
- `&&`, `||` short-circuit (right side may not run: `i++ || j++`)
- `?:` – three operands, right-associative; `max = a > b ? a : b`
- Never compare floats with `==` (`0.1f != 0.1`)
- Leap year: `(y % 4 == 0 && y % 100 != 0) || y % 400 == 0`

## Loops
| Loop | Test | Runs at least |
|---|---|---|
| while | before body | 0 times |
| for (init; test; update) | before body | 0 times (init once) |
| do … while( ); | after body | 1 time |
- `for (;;)` and `while (1)` are infinite; `for (i = 0; i < 5; i++);` – the `;` is the body (i ends at 5)
- `break` – leaves the innermost loop/switch; `continue` – next iteration; `goto label;` – jump within a function; `exit()` – ends the program
- Counting: `for (i = 1; i <= 100; i *= 2)` runs 7 times; `while (i++ < 5)` tests 6 times and leaves i = 6

## switch
- Expression and case labels must be integer types (int, char, enum) – no float, no ranges, no duplicates
- Without `break` control falls through to the next case; `default` may be anywhere
"""}],
    "Arrays": [{"title": "Arrays and strings – revision sheet", "md": """## Arrays
- `int a[5];` indices 0–4; no bounds checking (a[5] or a[-1] → garbage / undefined)
- `int a[5] = {1, 2};` → rest 0; `int a[] = {…}` size from initialisers; count = `sizeof(a) / sizeof(a[0])`
- 2-D row-major: address of a[i][j] = base + (i × cols + j) × size; `char a[100][100]` → a[40][50] at 4050
- `int a[3][2] = {1,2,3,4,5,6}` → a[2][1] = 6; `int a[2][3][4]` = 24 elements
- Array name = `&a[0]` (cannot be assigned: `a = b` is an error); `2[a]` = `a[2]`
- Bubble sort: n − 1 passes, n(n − 1)/2 comparisons, O(n²) (O(n) best with a swap flag); largest element moves to the end after each pass
  - [4,3,2,1,8,7,6,5] → pass 1: 3 2 1 4 7 6 5 8 → pass 2: 2 1 3 4 6 5 7 8

## Strings
- char array ending in `'\\0'`; `"hi"` takes 3 bytes; `sizeof("bengaluru")` = 10, `strlen` = 9
- `char s[10]; s = "hi";` is an error – use `strcpy(s, "hi")`
- `<string.h>`: strlen, strcpy(dest, src), strncpy, strcat(dest, src), strncmp, strcmp (0 when equal), strchr (char), strstr (substring), strrev (Turbo C)
- `<ctype.h>`: toupper, tolower, isdigit, isalpha; `<stdlib.h>`: atoi, atof
- `scanf("%s")` stops at a space; `gets` removed (use `fgets`); compare contents with strcmp, not ==
- `'a' − 32 = 'A'`; palindrome: s[i] vs s[n − 1 − i]
"""}],
}
