"""P2 · KRIES – C Programming · second, DETAILED notes per topic (no new questions).
Owner's request (19 Oct 2026): make the KRIES C notes much more detailed – worked examples, output-tracing tips and exam traps.
The first, short revision sheets stay in p2_krc_a … e; these are added as a second note with its own title, so learners who
already imported the pack get them on re-import. Assumptions everywhere: 64-bit GCC, int = 4 bytes, char = 1, double = 8,
pointers = 8, ASCII, little-endian. Every traced output avoids undefined behaviour; where a common exam question IS
undefined, the note says so (the expected answer is then 'compiler dependent / undefined')."""

TOPICS = {}  # notes only

T = " – detailed notes with worked examples"

NOTES = {
    "Introduction to C Programming": [{"title": "Introduction to C" + T, "md": """## History in one line
BCPL (Martin Richards, 1967) → B (Ken Thompson, 1970) → **C (Dennis Ritchie, Bell Labs, 1972)**, written to re-implement **UNIX**.
Standards: K&R C (1978 book) → **ANSI C / C89** (= ISO C90) → C99 → C11 → C17 → C23. C is a **middle-level, procedural, structured** language.

## Structure of a C program
```c
/* 1. documentation section */
#include <stdio.h>        /* 2. link section            */
#define PI 3.14159        /* 3. definition section      */
int count = 0;            /* 4. global declarations     */
int area(int r);          /*    function prototypes     */
int main(void)            /* 5. main() – execution starts here */
{
    printf("%d\\n", area(2));
    return 0;             /* 0 = success to the OS      */
}
int area(int r) { return PI * r * r; }   /* 6. sub-programs */
```
Output: `12` – 3.14159 × 4 = 12.566…, converted to int on return (truncated, not rounded).

## From source to running program
`prog.c` → **preprocessor** (`prog.i`: includes pasted, macros expanded, comments removed) → **compiler** (`prog.s`, assembly) → **assembler** (`prog.o` / `.obj`, object code) → **linker** (+ library code → `a.out` / `prog.exe`) → **loader** puts it in memory.
- Syntax errors come from the compiler; "undefined reference to …" comes from the **linker**; division by zero shows up only at **run time**.

## Character set, tokens, keywords, identifiers
- Tokens: keywords, identifiers, constants, string literals, operators, punctuators (`; , { } ( ) [ ]`)
- **32 keywords in C89**: auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while. C99 added inline, restrict, _Bool, _Complex, _Imaginary.
- Identifier rules: letters, digits, `_`; must not start with a digit; case-sensitive; not a keyword
  - Valid: `_sum`, `total1`, `Int`, `__x` · Invalid: `1total`, `int`, `my-var`, `my var`, `rate%`
- `main`, `printf`, `scanf` are **not** keywords (they are identifiers).

## Constants and data types
| Constant | Example | Value |
|---|---|---|
| Decimal / octal / hex integer | `25`, `031`, `0x19` | all = 25 |
| Real | `3.14`, `2.5e3` | 2500.0 |
| Character | `'A'` | 65 (type int in C) |
| String | `"A"` | 2 bytes: 'A' and '\\0' |

| Type | Size | Range / precision | printf |
|---|---|---|---|
| char | 1 | −128 … 127 (signed) | %c, %d |
| unsigned char | 1 | 0 … 255 | %u |
| short | 2 | −32,768 … 32,767 | %hd |
| int | 4 | −2,147,483,648 … 2,147,483,647 | %d |
| unsigned int | 4 | 0 … 4,294,967,295 | %u |
| long | 8 (Linux) / 4 (Windows) | | %ld |
| long long | 8 | | %lld |
| float | 4 | ~6–7 digits | %f, %e |
| double | 8 | ~15–16 digits | %lf in scanf, %f in printf |
- Old 16-bit Turbo C: int = 2 bytes (−32,768 … 32,767) – some old questions assume this; read the question.
- Escape sequences: `\\n` newline, `\\t` tab, `\\0` null, `\\\\` backslash, `\\'`, `\\"`, `\\a` bell, `\\b` backspace, `\\r` carriage return.

## Output tracing – worked examples
| Statement | Output | Why |
|---|---|---|
| `printf("%d", 'A' + 1);` | 66 | 'A' is 65 |
| `printf("%c", 'a' - 32);` | A | 97 − 32 = 65 |
| `printf("%d", 010 + 0x10);` | 24 | octal 8 + hex 16 |
| `printf("%o %x %X", 65, 255, 255);` | 101 ff FF | octal / hex |
| `printf("%5.2f|", 3.14159);` | ` 3.14\\|` | width 5, 2 decimals |
| `printf("%-5d|", 42);` | `42   \\|` | `-` = left-justify |
| `printf("%zu", sizeof('A'));` | 4 | a char constant is an int in C (1 in C++) |
| `printf("%zu", sizeof("abc"));` | 4 | 3 chars + '\\0' |
| `unsigned char c = 300; printf("%d", c);` | 44 | 300 − 256 |
| `printf("%d", 7 / 2);` | 3 | integer division truncates |
| `printf("%.1f", 7 / 2.0);` | 3.5 | one operand is double |
| `printf("%d %d", 7 % -3, -7 % 3);` | 1 -1 | the remainder takes the sign of the **left** operand |
| `printf("%d", printf("Hi"));` | Hi2 | printf returns the number of characters printed |

## Traps
- A program can have only **one** `main()`; execution always starts there, whatever the order of functions.
- `void main()` is non-standard; `int main(void)` is correct.
- `%f` for an int (or `%d` for a float) prints garbage – undefined behaviour.
- Comments do not nest: `/* a /* b */ c */` ends at the first `*/`.
- C is case-sensitive: `Printf` is an unknown function."""}],

    "C Instructions": [{"title": "C instructions and operators" + T, "md": """## Three kinds of instructions
1. **Type declaration** – `int a = 5, b = a * 2;` (a variable must be declared before use; `int b = a, a = 5;` is an error)
2. **Arithmetic** – `left = expression;` the left side must be a variable (`a + b = c;` is an error – "lvalue required")
3. **Control** – sequence, decision (if, switch), repetition (loops), case control (goto)

## Operator precedence (high → low) and associativity
| Level | Operators | Assoc. |
|---|---|---|
| 1 | `()` `[]` `->` `.` postfix `++ --` | L → R |
| 2 | unary `! ~ + -` prefix `++ --` `*` `&` `(type)` `sizeof` | **R → L** |
| 3 | `* / %` | L → R |
| 4 | `+ -` | L → R |
| 5 | `<< >>` | L → R |
| 6 | `< <= > >=` | L → R |
| 7 | `== !=` | L → R |
| 8–10 | `&` then `^` then `\\|` | L → R |
| 11–12 | `&&` then `\\|\\|` | L → R |
| 13 | `?:` | **R → L** |
| 14 | `= += -= *= /= %= &= ^= \\|= <<= >>=` | **R → L** |
| 15 | `,` | L → R |
Memory aid: **unary > arithmetic > shift > relational > equality > bitwise > logical > ternary > assignment > comma**.

## Evaluating expressions – worked examples
- `int a = 2 + 3 * 4 % 5 - 6 / 4;` → 3 * 4 = 12, 12 % 5 = 2, 6 / 4 = 1 → 2 + 2 − 1 = **3**
- `int k = 5 / 2 * 2.0;` → 5 / 2 = 2 (int), 2 × 2.0 = 4.0 → k = **4**
- `float f = 5 / 2;` → **2.000000** (the division happens in int first)
- `float g = (float)5 / 2;` → **2.500000** (cast binds tighter than /)
- `int x = 10 > 5 > 2;` → (10 > 5) = 1, then 1 > 2 = **0**
- `printf("%d", -1 < 1u);` → **0**: −1 is converted to unsigned (4,294,967,295)
- `int a = 5; a += a *= 2;` – modifies a twice without a sequence point → **undefined**
- `int x = (1, 2, 3);` → **3** (comma operator gives the last value). But `x = 1, 2;` sets x to **1** (= binds tighter than ,)
- `int m = a > b ? a : b;` → the larger; nested `a > b ? (a > c ? a : c) : (b > c ? b : c)` → largest of three
- `printf("%d", 5 == 5.0);` → 1 (5 is converted to double)

## Increment / decrement
| Code (i starts at 5 each time) | Result |
|---|---|
| `j = i++;` | j = 5, i = 6 (use, then increment) |
| `j = ++i;` | j = 6, i = 6 (increment, then use) |
| `j = i++ + 10;` | j = 15, i = 6 |
| `j = --i * 2;` | j = 8, i = 4 |
| `j = i++ + ++i;` | **undefined** (i changed twice) – answer "compiler dependent" |
| `printf("%d %d", i, i++);` | **undefined** (order of argument evaluation is unspecified) |

## Short-circuit evaluation (tracing favourite)
```c
int i = 0, j = 5, k;
k = i && ++j;     /* i is 0 → right side skipped: k = 0, j = 5 */
k = i || ++j;     /* right side runs: j = 6, k = 1 */
k = ++i || j++;   /* i = 1 is true → j++ skipped: k = 1, j = 6 */
```

## Type conversion
- Implicit (promotion): char, short → int → unsigned → long → long long → float → double → long double
- In assignment the value is converted to the **left** type: `int n = 3.99;` → 3; `char c = 65.7;` → 'A'
- Explicit cast: `(double)a / b`

## I/O instructions
- `printf` returns characters printed; `scanf` returns **number of items read** (EOF at end of input)
- `scanf("%d", &n);` needs `&`; strings don't: `scanf("%s", name);` (stops at a space – use `fgets` for a line)
- `scanf("%d %d", &a, &b)` – a space in the format skips any white space
- `getchar()` / `putchar()` one character; `puts(s)` prints and **adds a newline**; `gets` was removed in C11 (buffer overflow)
- `sizeof` does not evaluate its operand: `int i = 5; sizeof(i++);` → i is still **5**

## Traps
- `if (x = 0)` assigns 0 → condition is always false; `if (x == 0)` compares
- `a = b = c = 10;` works (right-to-left)
- `%` works only on integers (`5.5 % 2` is an error; use `fmod`)
- `x & 1 == 0` parses as `x & (1 == 0)` → always 0 (see Bitwise notes)"""}],

    "Control Structures": [{"title": "Control structures" + T, "md": """## Decisions
- `if`, `if-else`, `else if` ladder, nested if; any non-zero value is true
- **Dangling else**: an `else` pairs with the **nearest unmatched if** (indentation does not matter)
```c
int a = 5, b = 10;
if (a > 10)
    if (b > 5) printf("X");
else printf("Y");      /* belongs to if (b > 5) → nothing printed */
```

## switch
- Case labels must be **integer or character constants** (no float, no string, no variables, no ranges in standard C)
- Without `break` execution **falls through** to the next cases; `default` can be anywhere and is optional
```c
int x = 2;
switch (x) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C"); break;
    default: printf("D");
}                                   /* output: BC */
```
- `switch (x) { default: printf("D"); case 1: printf("A"); }` with x = 5 → **DA** (default falls through too)
- Duplicate case values are a compile error; `case 'a': case 'A':` share one block

## Loops
| Loop | Test | Runs at least once? |
|---|---|---|
| `while (cond)` | entry-controlled | no |
| `for (init; cond; update)` | entry-controlled | no |
| `do { } while (cond);` | **exit-controlled** | **yes** (note the `;` at the end) |

## Tracing loops – worked examples
| Code | Output / result |
|---|---|
| `for (i = 0; i < 5; i++); printf("%d", i);` | **5** – the `;` is an empty body |
| `i = 0; while (i < 10) i += 3; printf("%d", i);` | **12** |
| `for (i = 1; i <= 10; i *= 2) n++;` | i = 1, 2, 4, 8 → n = **4** |
| `for (i = 10; i > 0; i -= 3) printf("%d ", i);` | 10 7 4 1 |
| `i = 0; do printf("%d", i); while (i++ < 3);` | **0123** |
| `i = 5; while (i--) printf("%d", i);` | **43210** (test uses 5…1, prints after decrement) |
| `for (i = 0, j = 10; i < j; i++, j--) n++;` | n = **5** |
| `for (i = 1; i <= 3; i++) for (j = 1; j <= i; j++) n++;` | 1 + 2 + 3 = **6** |

Counting rule: a loop `for (i = a; i <= b; i += s)` runs ⌊(b − a)/s⌋ + 1 times when a ≤ b.

## break, continue, goto
- `break` leaves the **innermost** loop or switch only
- `continue` skips to the next iteration (in a `for`, the update part still runs)
```c
for (i = 1; i <= 5; i++) {
    if (i == 3) continue;
    if (i == 5) break;
    printf("%d ", i);
}                                   /* 1 2 4 */
```
- `goto label;` jumps anywhere in the same function (avoid; used to leave deep nesting)

## Classic loop programs (know the logic)
- **Sum of digits** of 1234: `while (n) { s += n % 10; n /= 10; }` → 10
- **Reverse** 1234: `r = r * 10 + n % 10;` → 4321; palindrome if reverse == original
- **Armstrong** (3 digits): 153 = 1³ + 5³ + 3³; 370, 371, 407 are the others
- **Prime**: test divisors 2 … √n; **factorial** 5! = 120; **Fibonacci** 0 1 1 2 3 5 8 13
- **GCD** (Euclid): `while (b) { t = b; b = a % b; a = t; }` → gcd(48, 18) = 6; lcm = a × b / gcd = 144
- Patterns: outer loop = rows, inner loop = columns (`for (j = 1; j <= i; j++) printf("*");`)

## Traps
- `for (unsigned i = 5; i >= 0; i--)` never ends (unsigned is never negative)
- `while (x != 10) x += 3;` with x = 0 never ends (0, 3, 6, 9, 12 … skips 10)
- `if (a = 5)` is always true; `while (0)` body never runs; `for (;;)` is an infinite loop
- A `case` without `break` is not an error – it is fall-through"""}],

    "Arrays": [{"title": "Arrays and strings" + T, "md": """## Declaring and initialising
- `int a[5] = {1, 2};` → {1, 2, 0, 0, 0} (missing elements become 0); `int a[5];` (local) holds garbage
- `int a[] = {4, 5, 6};` → size 3; number of elements = `sizeof(a) / sizeof(a[0])`
- Index runs 0 … n − 1; **no bounds checking** – `a[5]` on a 5-element array is undefined, not an error
- Size must be a constant in C89 (C99 allows variable-length arrays)
- An array name is a constant address: `a++` and `a = b` are errors; copy element by element (or memcpy)

## Address calculation (formula questions)
- 1-D: **addr(a[i]) = base + (i − LB) × w**
- 2-D, **row-major** (C): **addr(a[i][j]) = base + ((i − LR) × columns + (j − LC)) × w**
- 2-D, column-major (Fortran): base + ((j − LC) × rows + (i − LR)) × w
- Example: `int a[3][4]`, base 1000, w = 4 → a[2][1] = 1000 + (2 × 4 + 1) × 4 = **1036**
- Example: A[−2..5][3..8], base 500, w = 2 → 8 rows, 6 columns → A[1][5] row-major = 500 + ((1 + 2) × 6 + (5 − 3)) × 2 = **540**; column-major = 500 + ((5 − 3) × 8 + (1 + 2)) × 2 = **538**

## 2-D arrays
- `int m[2][3] = {{1, 2, 3}, {4, 5, 6}};` – the first dimension may be omitted: `int m[][3] = {...}`; the column size never
- Matrix multiplication A(m × n) · B(n × p) is possible only when columns of A = rows of B → result m × p, needs m·n·p multiplications
- Transpose: `t[j][i] = m[i][j]`; sum of the diagonal: `m[i][i]`

## Strings
- A string is a char array ending in `'\\0'`
- `char s[] = "hello";` → sizeof 6, strlen 5; `char s[5] = "hello";` is legal in C but has **no '\\0'** (printing it is undefined)
- `char *p = "hello";` points to a read-only literal – `p[0] = 'H'` is undefined; `char s[] = "hello"; s[0] = 'H';` is fine

| `<string.h>` | Does | Example |
|---|---|---|
| strlen(s) | length without '\\0' | strlen("abc\\0de") = **3** |
| strcpy(d, s) | copy s into d | d must be big enough |
| strncpy(d, s, n) | copy at most n | may leave no '\\0' |
| strcat(d, s) | append | "Exam" + "Sim" → "ExamSim" |
| strcmp(a, b) | < 0, 0, > 0 | strcmp("abc", "abd") < 0; strcmp("b", "a") > 0 |
| strchr(s, c) / strstr(s, t) | first char / substring | return a pointer or NULL |
| strrev, strupr, strlwr | non-standard (Turbo C) | |
- Comparing with `==` compares **addresses**, not contents – use strcmp

## Output tracing
```c
char s[] = "ExamSim";
printf("%c", s[3]);        /* m      */
printf("%s", s + 4);       /* Sim    */
printf("%c", *s + 1);      /* F  ('E' + 1) */
printf("%c", *(s + 1));    /* x      */
printf("%zu %zu", sizeof(s), strlen(s));   /* 8 7 */
int a[] = {10, 20, 30, 40};
printf("%d", a[1] + a[3]);   /* 60 */
printf("%d", 2[a]);          /* 30 – a[i] == *(a+i) == i[a] */
```

## Arrays and functions
- An array is passed as a **pointer** to its first element: changes inside the function affect the caller
- Inside the function `sizeof(arr)` gives the pointer size (8), so pass the length separately
- `void f(int a[])`, `void f(int *a)` and `void f(int a[10])` are identical; 2-D: `void g(int m[][4])`

## Sorting and searching on arrays
- **Bubble sort** on 5 1 4 2 8 – pass 1: 1 4 2 5 8 (the largest bubbles to the end); n − 1 passes, n(n − 1)/2 comparisons
- **Linear search** O(n); **binary search** O(log n) – only on a sorted array (see Searching and Sorting notes)

## Traps
- `int a[3] = {1, 2, 3, 4};` → compile error/warning (too many initialisers)
- Array index can be an expression: `a[i++]`
- `char c[] = {'a', 'b'};` is not a string (no '\\0')"""}],

    "Functions": [{"title": "Functions" + T, "md": """## Parts of a function
```c
int add(int, int);              /* declaration / prototype */
int main(void) {
    printf("%d", add(2, 3));    /* call: 2, 3 are actual arguments */
    return 0;
}
int add(int x, int y) {         /* definition: x, y are formal parameters */
    return x + y;               /* returns ONE value */
}
```
- A function can return only one value (return a struct or use pointers for more)
- Types of functions: library (printf, sqrt) vs user-defined; by arguments/return value – no args no return, args no return, no args return, args and return

## Call by value vs call by reference
| By value | By reference (address) |
|---|---|
| a **copy** is passed | the **address** is passed (`&x`) |
| changes stay inside the function | changes reach the caller |
| `void swap(int a, int b)` – does **not** swap | `void swap(int *a, int *b)` – swaps |
```c
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
int x = 1, y = 2; swap(&x, &y);      /* x = 2, y = 1 */
```
C itself passes everything by value; "call by reference" means passing an address by value.

## Storage classes
| Class | Stored in | Default | Scope | Lifetime |
|---|---|---|---|---|
| auto (default for locals) | stack | garbage | block | block |
| register | CPU register (request) | garbage | block | block – `&` not allowed |
| **static** (local) | data segment | **0** | block | **whole program – keeps its value** |
| static (global) | data segment | 0 | **this file only** | whole program |
| extern | data segment | 0 | all files | whole program – declares, doesn't allocate |
```c
void count(void) { static int c = 0; c++; printf("%d ", c); }
count(); count(); count();          /* 1 2 3  (with auto: 1 1 1) */
```
- A static local is initialised **once**, and only with a constant.

## Recursion – trace the calls
- Needs a **base case**; each call gets its own stack frame; too deep → stack overflow
```c
int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }   /* fact(5) = 120 */
int sum(int n)  { return n == 0 ? 0 : n % 10 + sum(n / 10); } /* sum(1234) = 10 */
int pw(int b, int e) { return e == 0 ? 1 : b * pw(b, e - 1); } /* pw(2, 5) = 32 */
void up(int n)   { if (n > 0) { up(n - 1); printf("%d ", n); } }   /* up(3): 1 2 3 */
void down(int n) { if (n > 0) { printf("%d ", n); down(n - 1); } } /* down(3): 3 2 1 */
```
- Statement **after** the recursive call runs on the way back (reverse order)
- `fib(n) = fib(n−1) + fib(n−2)`: fib(5) = 5 (0 1 1 2 3 5); the naive version makes **15 calls** for fib(5) → O(2ⁿ)
- `int f(int n) { if (n <= 0) return 0; return n + f(n - 2); }` → f(7) = 7 + 5 + 3 + 1 = **16**
- Tower of Hanoi: 2ⁿ − 1 moves; Ackermann grows extremely fast (not primitive recursive)

## main and command-line arguments
- `int main(int argc, char *argv[])`: `./prog in.txt 5` → argc = 3, argv[0] = "./prog", argv[1] = "in.txt", argv[2] = "5" (a string – use atoi)
- `return 0` = success; `exit(1)` ends the program from anywhere (`<stdlib.h>`)

## Library functions to remember
- `<math.h>`: sqrt, pow, fabs, ceil(2.1) = 3.0, floor(2.9) = 2.0, round, log, exp, sin – link with `-lm`
- `<stdlib.h>`: abs, atoi("42") = 42, rand, srand, malloc, free, exit, qsort
- `<ctype.h>`: isdigit, isalpha, isupper, toupper('a') = 'A'

## Traps
- Calling a function before its prototype assumes it returns int (old C) – in C99 it is an error
- A function's arguments are evaluated in **unspecified order**
- Returning the address of a local variable → dangling pointer
- `return` with no value in an int function returns garbage
- Nested function **definitions** are not allowed in standard C (calls inside calls are fine)"""}],

    "Pointers": [{"title": "Pointers" + T, "md": """## Reading declarations (right–left rule)
| Declaration | Meaning |
|---|---|
| `int *p;` | p is a pointer to int |
| `int **q;` | pointer to pointer to int |
| `int *a[5];` | array of 5 pointers to int |
| `int (*b)[5];` | pointer to an array of 5 ints |
| `int *f(void);` | function returning a pointer to int |
| `int (*fp)(int, int);` | pointer to a function taking two ints and returning int |
| `const int *p;` / `int const *p;` | pointer to a constant int (value read-only) |
| `int *const p = &x;` | constant pointer (cannot point elsewhere) |
| `void *v;` | generic pointer – cast before dereferencing; no arithmetic in standard C |

## Pointer arithmetic (addresses)
p holds 1000:
| Type of p | p + 1 | p + 3 |
|---|---|---|
| char * | 1001 | 1003 |
| int * | 1004 | 1012 |
| double * | 1008 | 1024 |
- Subtracting two pointers into the same array gives the **number of elements** between them: `&a[3] − &a[0]` = 3
- Allowed: pointer ± integer, pointer − pointer, comparison. Not allowed: pointer + pointer, × , ÷
- `sizeof(p)` = 8 for every pointer type on a 64-bit system

## Trace – pointers and arrays
```c
int a[] = {10, 20, 30, 40};
int *p = a;
printf("%d ", *(p + 2));   /* 30                       */
p++;                        /* p → a[1]                 */
printf("%d ", *p);          /* 20                       */
printf("%d ", *p++);        /* 20, then p → a[2]        */
printf("%d ", ++*p);        /* a[2] becomes 31 → 31     */
printf("%d ", (*p)++);      /* prints 31, a[2] = 32     */
printf("%d", *p);           /* 32                       */
```
Output: `30 20 20 31 31 32`
- `*p++` = `*(p++)` (postfix binds tighter) – use the value, move the pointer
- `++*p` and `(*p)++` change the **value**; `*++p` moves first, then reads

## 2-D arrays and pointers
`int m[2][3] = {{1, 2, 3}, {4, 5, 6}};`
- `m[i][j]` = `*(*(m + i) + j)`; `**m` = 1; `*m[1]` = 4; `*(*(m + 1) + 2)` = 6
- `m + 1` moves a whole row (12 bytes); `*m + 1` moves one int (4 bytes)

## Strings and pointers
```c
char *s = "hello";
printf("%c", *(s + 1));   /* e     */
printf("%s", s + 2);      /* llo   */
printf("%c", *s + 2);     /* j  ('h' + 2) */
```
- `sizeof(s)` = 8 (pointer) but `char t[] = "hello"; sizeof(t)` = 6
- String length with pointers: `char *q = s; while (*q) q++; len = q − s;`

## Pointer to pointer
```c
int x = 10, *p = &x, **q = &p;
**q = 20;                       /* x is now 20 */
printf("%d %d %d", x, *p, **q); /* 20 20 20    */
```

## Dynamic memory (`<stdlib.h>`)
| Function | Does | Memory content |
|---|---|---|
| `malloc(n)` | n bytes | garbage |
| `calloc(k, size)` | k × size bytes | **zeroed** |
| `realloc(p, n)` | resize (may move) | old data kept |
| `free(p)` | release | p becomes dangling – set `p = NULL` |
```c
int *arr = malloc(5 * sizeof(int));
if (arr == NULL) { /* out of memory */ }
for (int i = 0; i < 5; i++) arr[i] = i * i;   /* 0 1 4 9 16 */
free(arr); arr = NULL;
```
- Heap memory lives until free(); forgetting free → **memory leak**; using after free → **dangling pointer**; freeing twice → undefined

## Function pointers
```c
int add(int a, int b) { return a + b; }
int (*fp)(int, int) = add;     /* or &add */
printf("%d", fp(2, 3));        /* 5 */
```
Used for callbacks (qsort's compare function), menus, tables of operations.

## Traps
- Uninitialised pointer = **wild** pointer; `int *p; *p = 5;` is undefined
- `int *p, q;` declares p as a pointer but q as a plain int
- Array name is a constant pointer (`a++` illegal) but a pointer parameter can be incremented
- NULL pointer dereference crashes (segmentation fault)"""}],

    "Structures and Unions": [{"title": "Structures and unions" + T, "md": """## Structure basics
```c
struct student {
    int roll;
    char name[20];
    float marks;
};
struct student s1 = {1, "Asha", 92.5f}, *ps = &s1;
printf("%d %s", s1.roll, ps->name);     /* 1 Asha */
```
- `ps->name` = `(*ps).name` (the brackets matter: `*ps.name` means `*(ps.name)`)
- Structures can be **assigned** (`s2 = s1;` copies every member, even arrays) but **not compared** with `==`
- `typedef struct student Student;` then `Student s;`
- Array of structures: `struct student cls[60];` → `cls[i].marks`
- Nested structures: `s.dob.year`; self-referential: `struct node { int data; struct node *next; };` (a member may be a pointer to its own type, not the type itself)

## Size and padding (64-bit GCC)
Each member is aligned to its own size; the total is rounded up to the largest alignment.
| Structure | sizeof | Layout |
|---|---|---|
| `{char c; int i; char d;}` | **12** | c + 3 pad, i, d + 3 pad |
| `{int i; char c; char d;}` | **8** | i, c, d + 2 pad |
| `{char a; char b; int c;}` | **8** | a, b + 2 pad, c |
| `{char c; double d;}` | **16** | c + 7 pad, d |
| `{char c; short s; int i;}` | **8** | c + 1 pad, s, i |
| `{int a[3]; char c;}` | **16** | 12 + 1 + 3 pad |
- Order members from largest to smallest to save space; `#pragma pack(1)` removes padding
- Exam questions without padding simply **add** member sizes – read the options

## Unions
- All members share **the same memory**; size = largest member rounded to the alignment
- Only one member holds a valid value at a time; writing one overwrites the others
| Union | sizeof |
|---|---|
| `{int i; char c;}` | 4 |
| `{int i; double d; char s[10];}` | **16** (10 rounded up to a multiple of 8) |
| `{char a[5]; int b;}` | 8 |
```c
union { int i; char c; } u;
u.i = 65;
printf("%c", u.c);            /* A – on a little-endian machine the low byte comes first */
union { int i; float f; } v;
v.f = 1.0f;                    /* v.i now holds the bit pattern 1065353216 (0x3F800000) */
```

| Structure | Union |
|---|---|
| separate memory for each member | shared memory |
| size ≥ sum of members | size = largest member |
| all members usable together | one at a time |
| keyword `struct` | keyword `union` |

## Bit fields
```c
struct flags { unsigned a : 1; unsigned b : 3; unsigned c : 4; };   /* sizeof = 4 */
```
- Width ≤ the type's bits; `&` cannot be applied to a bit field; `unsigned a : 1` holds 0 or 1

## enum
```c
enum color { RED, GREEN = 5, BLUE, WHITE = 2, BLACK };
/* RED = 0, GREEN = 5, BLUE = 6, WHITE = 2, BLACK = 3 */
```
- Each enumerator is the previous + 1 unless given; values may repeat; the type is int

## Passing structures to functions
- By value copies the whole structure (slow for large ones); pass a pointer (`void show(const struct student *p)`)
- A function may **return** a structure

## Traps
- A `;` is required after the closing `}` of a structure definition
- Members cannot be initialised inside the declaration in C (`struct s { int x = 5; };` is an error)
- `struct a { struct a x; };` is an error (infinite size); a pointer to `struct a` is fine
- Union size is **not** the sum of its members"""}],

    "Bitwise Operators": [{"title": "Bitwise operators" + T, "md": """## The six operators
| Op | Name | 12 op 10 (1100, 1010) |
|---|---|---|
| `&` | AND | 1000 = **8** |
| `\\|` | OR | 1110 = **14** |
| `^` | XOR | 0110 = **6** |
| `~` | NOT (one's complement) | ~12 = **−13** (rule: ~x = −x − 1) |
| `<<` | left shift | 5 << 2 = **20** (× 2²) |
| `>>` | right shift | 20 >> 2 = **5** (÷ 2², truncating) |
- Work only on integer types (char, int, long …), not float/double
- `>>` on a negative number is implementation-defined (GCC does an arithmetic shift: −8 >> 1 = −4); on **unsigned** it fills with 0s
- Shifting by ≥ the width of the type, or a negative amount, is undefined

## Two's complement (how negatives are stored)
- −x = ~x + 1. In 8 bits: 5 = 00000101 → −5 = **11111011**
- Range of n-bit signed: −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 (8 bits: −128 … 127)
- `printf("%d", ~0);` → −1; `printf("%u", ~0u);` → 4294967295

## Tricks every exam uses
| Task | Expression |
|---|---|
| Is x odd? | `x & 1` |
| Is x a power of 2? | `x && !(x & (x − 1))` |
| Set bit n | `x \\| (1 << n)` |
| Clear bit n | `x & ~(1 << n)` |
| Toggle bit n | `x ^ (1 << n)` |
| Test bit n | `(x >> n) & 1` |
| Multiply / divide by 2ⁿ | `x << n`, `x >> n` |
| Swap without a temp | `a ^= b; b ^= a; a ^= b;` (fails if a and b are the same variable) |
| Turn off the lowest set bit | `x & (x − 1)` |
| Keep only the lowest set bit | `x & −x` |
| Count set bits (Kernighan) | `while (x) { x &= x − 1; c++; }` |
| Lower 4 bits | `x & 0x0F` |

## Output tracing
```c
int a = 7, b = 5;
printf("%d %d %d\\n", a & b, a | b, a ^ b);   /* 5 7 2   (111 & 101, 111 | 101, 111 ^ 101) */
printf("%d %d\\n", a << 1, a >> 1);            /* 14 3 */
printf("%d\\n", ~a);                           /* -8  */
int x = 10;                                    /* 1010 */
x = x | (1 << 0);                              /* 1011 = 11 */
x = x & ~(1 << 3);                             /* 0011 = 3  */
printf("%d\\n", x);                            /* 3 */
unsigned char c = 0xF0;
printf("%X\\n", c >> 4);                       /* F */
printf("%d\\n", 1 << 10);                      /* 1024 */
```

## XOR facts
- x ^ x = 0, x ^ 0 = x, XOR is commutative and associative
- The number that appears once among pairs: XOR all elements (2 ^ 3 ^ 2 = 3)
- Simple XOR encryption: c = m ^ k; m = c ^ k

## Logical vs bitwise
| | `&&` / `\\|\\|` | `&` / `\\|` |
|---|---|---|
| Result | 0 or 1 | bit pattern |
| Short-circuit | yes | no (both sides evaluated) |
| 5 op 2 | 5 && 2 = 1 | 5 & 2 = 0 |

## Traps
- **Precedence**: `==` binds tighter than `&`, `^`, `|` → `if (x & 1 == 0)` means `x & (1 == 0)` = 0 → always false. Write `if ((x & 1) == 0)`
- `<<` binds looser than `+`: `1 << 2 + 1` = 1 << 3 = 8
- `~` on an unsigned char promotes to int first: `~(unsigned char)0` = −1 as int"""}],

    "C Preprocessor": [{"title": "C preprocessor" + T, "md": """## What it is
- Runs **before** compilation; lines start with `#`; no `;` at the end; `gcc -E file.c` shows its output
- Directives: `#include`, `#define`, `#undef`, `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`, `#error`, `#pragma`, `#line`

## #include
- `#include <stdio.h>` – searches the system/include directories
- `#include "myhdr.h"` – searches the current directory first, then system directories
- Header files hold declarations (prototypes, macros, typedefs), not normally function bodies
- **Include guard** to stop double inclusion:
```c
#ifndef MYHDR_H
#define MYHDR_H
/* declarations */
#endif
```
(or `#pragma once`, non-standard but widely supported)

## Object-like and function-like macros
```c
#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```
Macros are **text substitution** – no type checking, no evaluation.

## Macro tracing – the most asked questions
| Macro | Use | Expands to | Result |
|---|---|---|---|
| `#define SQ(x) x * x` | `SQ(3 + 2)` | `3 + 2 * 3 + 2` | **11** |
| `#define SQ(x) ((x) * (x))` | `SQ(3 + 2)` | `((3 + 2) * (3 + 2))` | **25** |
| `#define DBL(x) x + x` | `10 * DBL(2)` | `10 * 2 + 2` | **22** |
| `#define DBL(x) ((x) + (x))` | `10 * DBL(2)` | | **40** |
| `#define SQ(x) ((x) * (x))` | `100 / SQ(5)` | `100 / ((5) * (5))` | **4** |
| `#define SQ(x) x * x` | `100 / SQ(5)` | `100 / 5 * 5` | **100** |
| `#define CUBE(x) (x * x * x)` | `CUBE(1 + 1)` | `(1 + 1 * 1 + 1 * 1 + 1)` | **4** |
| `#define SQ(x) ((x) * (x))` | `SQ(i++)` | `((i++) * (i++))` | **undefined** (i changed twice) |
Rule: put brackets around **every parameter and the whole body**.

## # and ## operators
- `#` stringises: `#define STR(x) #x` → `STR(hello)` becomes `"hello"`
- `##` pastes tokens: `#define CAT(a, b) a##b` → `CAT(var, 1)` becomes `var1`
- Multi-line macro: end each line with `\\`

## Predefined macros
`__FILE__` (file name), `__LINE__` (line number), `__DATE__`, `__TIME__`, `__STDC__` (1 if standard C), `__STDC_VERSION__`; C99's `__func__` is the current function name (an identifier, not a macro)
```c
printf("%s line %d", __FILE__, __LINE__);
```

## Conditional compilation
```c
#define DEBUG 1
#if DEBUG
    printf("x = %d\\n", x);
#endif

#ifdef _WIN32
    /* Windows-only code */
#else
    /* other systems */
#endif
```
- Used for debugging switches, portability, include guards; `#undef PI` removes a definition

## Macro vs function
| Macro | Function |
|---|---|
| expanded inline – no call overhead (faster) | one copy of code – call overhead |
| code grows with each use | smaller code |
| no type checking | arguments type-checked |
| arguments may be evaluated twice | evaluated once |
| hard to debug | easy to debug |
| C99 alternative: `inline` functions | |
- `#define` vs `const`: a const variable has a type and scope and is visible to the debugger; a macro is just text

## Traps
- `#define PI 3.14;` (with a `;`) puts the `;` into every use → errors such as `area = PI * r * r;` becoming `3.14; * r * r`
- Macro names are not replaced inside string literals: `printf("PI")` prints PI
- A macro can be redefined only after `#undef` (or with an identical body)
- `#include` can include any file, even a .c file (bad practice)"""}],

    "Files": [{"title": "File handling" + T, "md": """## Opening and closing
```c
FILE *fp = fopen("marks.txt", "r");
if (fp == NULL) { perror("marks.txt"); return 1; }
/* … use the file … */
fclose(fp);
```
| Mode | Meaning | If the file does not exist | If it exists |
|---|---|---|---|
| "r" | read | returns **NULL** | read from start |
| "w" | write | creates | **erases** (truncates) |
| "a" | append | creates | writes at the end |
| "r+" | read + write | NULL | keeps content |
| "w+" | write + read | creates | erases |
| "a+" | read + append | creates | reads anywhere, writes at end |
Add `b` for binary files: "rb", "wb", "ab+". On Windows text mode turns "\\r\\n" into "\\n" when reading.

## Reading and writing functions
| Level | Read | Write |
|---|---|---|
| character | `fgetc(fp)` / `getc` → int, EOF at end | `fputc(c, fp)` / `putc` |
| line / string | `fgets(buf, n, fp)` (keeps the '\\n'; NULL at end) | `fputs(s, fp)` (no newline added) |
| formatted | `fscanf(fp, "%d", &x)` | `fprintf(fp, "%d\\n", x)` |
| block / binary | `fread(ptr, size, count, fp)` | `fwrite(ptr, size, count, fp)` – both return items done |

## Moving around
- `fseek(fp, offset, origin)` – origin `SEEK_SET` (start), `SEEK_CUR` (current), `SEEK_END` (end)
- `ftell(fp)` – current position in bytes; `rewind(fp)` = `fseek(fp, 0, SEEK_SET)`
- File size: `fseek(fp, 0, SEEK_END); long n = ftell(fp);`
- `fseek(fp, -10, SEEK_END)` – 10 bytes before the end; `fseek(fp, sizeof(struct rec) * 2, SEEK_SET)` – third record

## Standard programs
```c
/* copy a file character by character */
int ch;                                   /* int, not char – EOF is -1 */
while ((ch = fgetc(src)) != EOF)
    fputc(ch, dst);

/* count characters, words and lines */
int c, chars = 0, lines = 0;
while ((c = fgetc(fp)) != EOF) { chars++; if (c == '\\n') lines++; }

/* write and read a structure */
struct rec { int id; float m; } r = {1, 88.5f};
fwrite(&r, sizeof r, 1, fp);
rewind(fp);
fread(&r, sizeof r, 1, fp);
```

## Other functions
- `feof(fp)` – true only **after** a read has hit the end; `ferror(fp)` – error flag; `clearerr(fp)`
- `fflush(fp)` – write out the buffer; `fclose` flushes too (data may be lost if a program crashes before closing)
- `remove("a.txt")`, `rename("a.txt", "b.txt")`, `tmpfile()`
- Standard streams opened automatically: **stdin, stdout, stderr** (`fprintf(stderr, "error\\n")`)
- EOF is a macro (usually −1) in `<stdio.h>`; from the keyboard: Ctrl+Z (Windows) / Ctrl+D (Linux)

## Text vs binary files
| Text | Binary |
|---|---|
| human-readable characters | raw bytes as in memory |
| numbers stored as digits ("12345" = 5 bytes) | an int is 4 bytes |
| fprintf / fscanf / fgets | fwrite / fread |
| newline translation (Windows) | none |

## Traps
- `while (!feof(fp)) { fgets(...); print }` prints the **last line twice** – test the return value of the read instead
- `char ch = fgetc(fp)` may never equal EOF if char is unsigned → infinite loop; use `int`
- Opening with "w" destroys the old content
- Always check `fopen` for NULL; always `fclose`
- `FILE` is a structure type defined in `<stdio.h>`; `fopen` returns `FILE *`"""}],
}
