"""P2 · KRIES – C Programming · third note per topic: the KRIES syllabus line broken down WORD BY WORD (no new questions).
Owner's request (19 Oct 2026): "breakdown each word as notes" – every term of the official KRIES Computer Teacher syllabus line
(as in tools/make_kries_plan.py) gets its own heading, in syllabus order, with what it means, key facts, a small example and the
exam angle. Assumptions: 64-bit GCC, int 4 bytes, ASCII."""

TOPICS = {}  # notes only

W = "KRIES syllabus word by word – "

NOTES = {
    "Introduction to C Programming": [{"title": W + "Introduction to C", "md": """> **Syllabus:** History of C, structure of a C programme, the C character set, constants, variables and keywords, types of constants and variables

### History of C
- **Means:** how C came about.
- **Key facts:** ALGOL 60 → CPL → BCPL (Martin Richards, 1967) → B (Ken Thompson, 1970) → **C by Dennis Ritchie at AT&T Bell Labs, 1972**, to rewrite UNIX. K&R book 1978; ANSI C 1989 (C89/C90); C99, C11, C17, C23.
- **Example:** UNIX, Linux kernel, Windows kernel parts, embedded firmware are written in C.
- **Exam point:** C is called a **middle-level** language (high-level syntax + low-level access via pointers and bit operations).

### Structure of a C programme
- **Means:** the sections a C program is arranged in.
- **Key facts:** documentation (comments) → link (`#include`) → definition (`#define`) → global declarations → `main()` → user-defined functions. Every statement ends with `;`; blocks use `{ }`.
- **Example:** `#include <stdio.h>` · `int main(void) { printf("Hi"); return 0; }`
- **Exam point:** execution always starts at **main()**; only one main per program.

### The C character set
- **Means:** characters allowed in C source code.
- **Key facts:** letters A–Z, a–z; digits 0–9; special symbols `~ ! # % ^ & * ( ) - + = | \\ { } [ ] : ; " ' < > , . ? /`; white space (blank, tab, newline). Characters form **tokens**: keywords, identifiers, constants, strings, operators, special symbols.
- **Example:** `sum = a + 5;` has tokens `sum`, `=`, `a`, `+`, `5`, `;` → 6 tokens.
- **Exam point:** count tokens: `printf("%d", x);` → `printf`, `(`, `"%d"`, `,`, `x`, `)`, `;` = **7**.

### Constants
- **Means:** fixed values that do not change while the program runs.
- **Key facts:** literal constants (`25`, `3.14`, `'A'`, `"KEA"`), symbolic constants (`#define PI 3.14`), `const` variables (`const int MAX = 100;`).
- **Example:** `const int n = 5; n = 6;` → compile error (assignment of read-only variable).
- **Exam point:** `#define` has no type and no memory; `const` has a type.

### Variables
- **Means:** named memory locations whose value can change.
- **Key facts:** must be **declared** before use with a type; declaration reserves memory; initialise to avoid garbage; naming rules = identifier rules.
- **Example:** `int age = 30; age = age + 1;` → 31.
- **Exam point:** an uninitialised local (auto) variable holds **garbage**; global/static start at 0.

### Keywords
- **Means:** reserved words with a fixed meaning; cannot be used as names.
- **Key facts:** **32 keywords in C89**: auto, break, case, char, const, continue, default, do, double, else, enum, extern, float, for, goto, if, int, long, register, return, short, signed, sizeof, static, struct, switch, typedef, union, unsigned, void, volatile, while. All lowercase.
- **Example:** `int int = 5;` → error. `int Int = 5;` → valid (C is case-sensitive).
- **Exam point:** `main`, `printf`, `include`, `define` are **not** keywords.

### Types of constants
- **Means:** classes of constant values.
- **Key facts:** **Primary** – integer (decimal `25`, octal `031`, hex `0x19`), real/floating (`3.5`, exponent form `2.5e-3`), character (`'a'`, escape `'\\n'`). **Secondary** – string, array, pointer, structure, union, enum.
- **Example:** `printf("%d", 031);` → 25.
- **Exam point:** `'A'` (char, 1 character) ≠ `"A"` (string, 2 bytes with `'\\0'`); a leading 0 makes an integer **octal** (`08` is an error).

### Types of variables
- **Means:** classified by data type (and by scope/storage).
- **Key facts:** by type: `char` (1 byte), `int` (4), `float` (4), `double` (8), with modifiers `short`, `long`, `signed`, `unsigned`; by scope: **local** (inside a block) and **global** (outside all functions); by storage: auto, register, static, extern.
- **Example:** `unsigned int u = -1;` → stored as 4294967295.
- **Exam point:** `%d` int, `%f` float, `%lf` double (scanf), `%c` char, `%u` unsigned, `%ld` long."""}],

    "C Instructions": [{"title": W + "C instructions", "md": """> **Syllabus:** Type declaration and arithmetic instructions, integer and float conversions, type conversion in assignment, operators in C, hierarchy of operators, control instructions, formatted and unformatted input-output statements

### Type declaration instruction
- **Means:** the statement that declares variables and their types.
- **Key facts:** written at the start of a block (C89); can initialise; can use earlier variables: `int a = 5, b = a * 2;`
- **Example:** `float r = 2.5, area;`
- **Exam point:** `int b = a, a = 5;` is wrong – a is used before it is declared.

### Arithmetic instruction
- **Means:** `variable = expression;` using arithmetic operators.
- **Key facts:** left side must be a single variable (lvalue); operators `+ - * / %`; `%` only for integers; no implicit multiplication (`a = bc` is not b × c).
- **Example:** `k = 3 * 4 + 6 / 4;` → 12 + 1 = **13**.
- **Exam point:** `a + b = c;` → error "lvalue required"; `x = 5 % 2.0` → error.

### Integer and float conversions
- **Means:** what type the result of an arithmetic operation has.
- **Key facts:** int op int → **int**; float op float → float; int op float → **float** (the int is promoted).
- **Example:** `5 / 2` = 2 · `5.0 / 2` = 2.5 · `5 / 2.0` = 2.5 · `2 / 5` = 0 · `2.0 / 5` = 0.4.
- **Exam point:** integer division **truncates** toward zero: `-7 / 2` = −3.

### Type conversion in assignment
- **Means:** when the right-side type differs from the left variable's type, the value is converted to the **left** type.
- **Key facts:** float → int drops the fraction; int → float adds `.0`; large int → char keeps the low byte.
- **Example:** `int i = 3.99;` → 3 · `float f = 7 / 2;` → 3.000000 · `char c = 321;` → 65 ('A').
- **Exam point:** in `float a = 9 / 2 * 2;` the right side is done in int: 4 × 2 = 8 → a = 8.0.

### Operators in C
- **Means:** symbols that perform operations.
- **Key facts:** arithmetic `+ - * / %`; relational `< > <= >= == !=`; logical `&& || !`; bitwise `& | ^ ~ << >>`; assignment `= += -= …`; increment/decrement `++ --`; conditional `?:`; comma `,`; `sizeof`; address `&`, indirection `*`; member `.` and `->`.
- **Example:** `x = 10; y = x++ * 2;` → y = 20, x = 11.
- **Exam point:** `?:` is the only **ternary** operator; `sizeof` is an operator, not a function.

### Hierarchy of operators
- **Means:** order (precedence) and direction (associativity) of evaluation.
- **Key facts:** `()` → unary (`! ~ ++ -- - sizeof (type)`, right-to-left) → `* / %` → `+ -` → `<< >>` → `< <= > >=` → `== !=` → `&` → `^` → `|` → `&&` → `||` → `?:` → assignment (right-to-left) → `,`.
- **Example:** `i = 2 * 3 / 4 + 4 / 4 + 8 - 2 + 5 / 8;` → 1 + 1 + 8 − 2 + 0 = **8** (2 × 3 = 6, 6 / 4 = 1).
- **Exam point:** `*` and `/` have equal precedence → evaluate **left to right**; `a = b = c` goes right to left.

### Control instructions
- **Means:** instructions that decide the order in which statements run.
- **Key facts:** four kinds – **sequence** (one after another), **selection/decision** (if, if-else, switch), **repetition/loop** (while, do-while, for), **case control** (switch; goto).
- **Example:** `if (marks >= 35) puts("Pass"); else puts("Fail");`
- **Exam point:** without control instructions, statements run in sequence.

### Formatted input-output statements
- **Means:** I/O functions that use format specifiers.
- **Key facts:** `printf()` and `scanf()` (`<stdio.h>`); specifiers `%d %i %u %ld %f %lf %e %c %s %x %o %p %%`; width/precision `%6.2f`, left-align `%-5d`, leading zeros `%05d`.
- **Example:** `printf("%05d|%-4d|%.3f", 42, 7, 3.14159);` → `00042|7   |3.142`
- **Exam point:** `scanf` needs addresses (`&x`); it returns the number of values read; `printf` returns the number of characters printed.

### Unformatted input-output statements
- **Means:** I/O without format specifiers – character and string functions.
- **Key facts:** `getchar()` / `putchar()` (one char, stdio.h); `getch()` / `getche()` (conio.h, no Enter needed – non-standard); `gets()` / `puts()` (strings; puts adds a newline; gets removed in C11 → use `fgets`).
- **Example:** `char c = getchar(); putchar(c + 1);` → typing `a` prints `b`.
- **Exam point:** `getch()` does not echo; `getche()` echoes; `scanf("%s")` stops at a space, `gets/fgets` read the whole line."""}],

    "Control Structures": [{"title": W + "Control structures", "md": """> **Syllabus:** Decision control structures, logical, conditional and relational operators; loops – while, do-while, for; break, continue, switch-case, goto

### Decision control structures
- **Means:** statements that choose which code runs.
- **Key facts:** `if`, `if-else`, nested if, `else-if` ladder, `switch`; condition is true when **non-zero**.
- **Example:** `if (n % 2 == 0) puts("even"); else puts("odd");`
- **Exam point:** an `else` pairs with the **nearest** unmatched `if`; `if (x = 5)` is always true.

### Logical operators
- **Means:** combine conditions: `&&` (AND), `||` (OR), `!` (NOT); result is 1 or 0.
- **Key facts:** **short-circuit**: in `a && b`, b is skipped if a is 0; in `a || b`, b is skipped if a is non-zero. `!` has the highest precedence of the three, then `&&`, then `||`.
- **Example:** `int i = 0, j = 2; if (i && j++) ; printf("%d", j);` → 2.
- **Exam point:** `!5` = 0, `!0` = 1; `5 && 3` = 1.

### Conditional operator
- **Means:** `condition ? value1 : value2` – a compact if-else that gives a value.
- **Key facts:** the only ternary operator; right-to-left associative; can be nested.
- **Example:** `big = (a > b) ? a : b;` · `printf("%s", n % 2 ? "odd" : "even");`
- **Exam point:** `x = 5 > 3 ? 10 : 20;` → 10.

### Relational operators
- **Means:** compare values: `< > <= >= == !=`; result 1 (true) or 0 (false).
- **Key facts:** `==` compares, `=` assigns; relational ops are higher in precedence than `==` and `!=`.
- **Example:** `printf("%d", 3 < 2 < 1);` → (0 < 1) = **1**.
- **Exam point:** compare floats with a tolerance, not `==` (0.1 + 0.2 != 0.3 in binary).

### Loops – while
- **Means:** entry-controlled loop: test first, then body.
- **Key facts:** `while (cond) { … }` – may run zero times; update the variable inside or it never ends.
- **Example:** `i = 1; while (i <= 5) { s += i; i++; }` → s = 15.
- **Exam point:** `while (i < 5);` (semicolon) → empty body → infinite loop if i < 5.

### Loops – do-while
- **Means:** exit-controlled loop: body first, then test.
- **Key facts:** runs **at least once**; syntax ends with `while (cond);`
- **Example:** `i = 10; do { printf("%d", i); } while (i < 5);` → prints 10 once.
- **Exam point:** best for menus that must appear at least once.

### Loops – for
- **Means:** `for (initialisation; condition; update)` – compact counting loop.
- **Key facts:** any part may be empty: `for (;;)` = infinite; comma for several variables: `for (i = 0, j = 9; i < j; i++, j--)`.
- **Example:** `for (i = 1; i <= 10; i += 3) printf("%d ", i);` → 1 4 7 10.
- **Exam point:** the update runs **after** the body, before the next test; after the loop i holds the first failing value.

### break
- **Means:** leave the nearest enclosing loop or switch immediately.
- **Key facts:** only one level; in nested loops the outer loop continues.
- **Example:** `for (i = 1; i <= 10; i++) { if (i == 4) break; printf("%d", i); }` → 123.
- **Exam point:** `break` outside a loop/switch → compile error.

### continue
- **Means:** skip the rest of the current iteration and go to the next one.
- **Key facts:** in a `for`, control goes to the **update** part; in while/do-while, to the test.
- **Example:** `for (i = 1; i <= 5; i++) { if (i % 2 == 0) continue; printf("%d", i); }` → 135.
- **Exam point:** `continue` cannot be used in a switch on its own (only inside a loop).

### switch-case
- **Means:** multi-way selection on an integer/char value.
- **Key facts:** `case` labels must be **constant integer/char** expressions, unique; `default` optional and can be anywhere; no `break` → **fall-through**.
- **Example:** `switch (2) { case 1: printf("A"); case 2: printf("B"); case 3: printf("C"); }` → BC.
- **Exam point:** `switch` cannot test float, string or ranges (`case 1 ... 5` is a GCC extension only).

### goto
- **Means:** unconditional jump to a **label** in the same function.
- **Key facts:** `goto end; … end: statement;` – makes code hard to read ("spaghetti code"); acceptable to escape deeply nested loops.
- **Example:** `i = 1; loop: printf("%d", i++); if (i <= 3) goto loop;` → 123.
- **Exam point:** cannot jump into another function; structured programming avoids goto."""}],

    "Arrays": [{"title": W + "Arrays", "md": """> **Syllabus:** One- and multi-dimensional arrays – declaration, initialisation, manipulation; bubble sort; strings – basic concepts and library functions

### One-dimensional array
- **Means:** a list of same-type elements in contiguous memory, accessed by one index.
- **Key facts:** index 0 … n−1; address of a[i] = base + i × size; size = n × sizeof(element).
- **Example:** `int a[5]` with base 1000 → a[3] at 1012; total 20 bytes.
- **Exam point:** C does no bounds checking.

### Multi-dimensional array
- **Means:** array of arrays – e.g. a matrix `int m[3][4]` (3 rows, 4 columns).
- **Key facts:** stored **row-major**; a[i][j] at base + (i × columns + j) × size; 3-D: `int c[2][3][4]` = 24 elements.
- **Example:** `int m[3][4]`, base 2000 → m[1][2] = 2000 + (1 × 4 + 2) × 4 = **2024**.
- **Exam point:** total elements = product of dimensions.

### Declaration
- **Means:** telling the compiler the type, name and size.
- **Key facts:** `type name[size];` size must be a positive constant in C89 (VLA allowed in C99); `int a[0]`, `int a[-3]` are errors.
- **Example:** `float marks[60]; char name[30]; int m[2][3];`
- **Exam point:** in a 2-D declaration with initialiser, only the **first** dimension may be omitted.

### Initialisation
- **Means:** giving values at declaration.
- **Key facts:** `int a[5] = {1, 2, 3};` → remaining are 0; `int a[] = {1, 2, 3};` → size 3; `int a[5] = {0};` → all zeros; `int m[2][3] = {{1, 2, 3}, {4, 5, 6}};` or `{1, 2, 3, 4, 5, 6}`.
- **Example:** `int a[4] = {5}; printf("%d", a[0] + a[3]);` → 5.
- **Exam point:** more initialisers than the size → error; uninitialised local array → garbage.

### Manipulation
- **Means:** reading, printing, updating, searching, summing, copying arrays with loops.
- **Key facts:** traverse `for (i = 0; i < n; i++)`; copy element by element (`b = a` is illegal); find max: start with a[0].
- **Example:** reverse in place: `for (i = 0; i < n / 2; i++) { t = a[i]; a[i] = a[n-1-i]; a[n-1-i] = t; }`
- **Exam point:** inserting at position k needs shifting elements right from the end.

### Bubble sort
- **Means:** repeatedly swap adjacent elements that are out of order; the largest "bubbles" to the end each pass.
- **Key facts:** n − 1 passes; n(n − 1)/2 comparisons; O(n²) worst/average, O(n) best with a swap flag; stable.
- **Example:** 5 1 4 2 8 → pass 1: 1 4 2 5 8 → pass 2: 1 2 4 5 8 (sorted).
- **Exam point:** after pass k the last k elements are in final position.

### Strings – basic concepts
- **Means:** a character array terminated by the null character `'\\0'`.
- **Key facts:** `char s[] = "KEA";` → 4 bytes; `%s` prints till `'\\0'`; `scanf("%s", s)` (no &) stops at space; string literal is read-only when used through a pointer.
- **Example:** `char s[10] = "Hi"; printf("%zu %zu", sizeof(s), strlen(s));` → 10 2.
- **Exam point:** `"A"` takes 2 bytes, `'A'` 1 byte.

### Library functions (string.h)
- **Means:** ready functions for strings.
- **Key facts:** `strlen` (length without '\\0'), `strcpy(d, s)`, `strncpy`, `strcat(d, s)`, `strcmp(a, b)` (0 if equal, <0 / >0 by first differing character), `strncmp`, `strchr`, `strstr`, `strrev`/`strupr`/`strlwr` (Turbo C only); ctype.h: `toupper`, `isalpha`, `isdigit`.
- **Example:** `char a[20] = "Com"; strcat(a, "puter"); printf("%s %zu", a, strlen(a));` → Computer 8.
- **Exam point:** compare strings with **strcmp**, not `==`."""}],

    "Functions": [{"title": W + "Functions", "md": """> **Syllabus:** Definition, function definition and prototyping, types of functions and arguments, recursion, passing arrays to functions; storage classes – automatic, register, external, static

### Definition (of a function)
- **Means:** a self-contained block of statements that performs a task and may return a value.
- **Key facts:** benefits – reuse, modularity, easier testing; `main()` is itself a function; library vs user-defined.
- **Example:** `int sq(int x) { return x * x; }`
- **Exam point:** a function returns at most **one** value with `return`.

### Function definition
- **Means:** the actual body: `return_type name(parameter list) { body }`.
- **Key facts:** parameters in the definition are **formal**; values in the call are **actual** arguments; `void` return = nothing returned.
- **Example:** `float avg(int a, int b) { return (a + b) / 2.0; }` → avg(3, 4) = 3.5.
- **Exam point:** definitions cannot be nested inside other functions.

### Prototyping
- **Means:** declaring a function before use: `return_type name(parameter types);`
- **Key facts:** lets the compiler check argument number and types; parameter names optional: `int add(int, int);`; usually in header files.
- **Example:** prototype at top, `main()` calls `add(2, 3)`, definition below main.
- **Exam point:** missing prototype → implicit int (C89) or error (C99).

### Types of functions
- **Means:** grouped by arguments and return value.
- **Key facts:** (1) no arguments, no return; (2) arguments, no return; (3) no arguments, return; (4) arguments and return. Also library (printf, sqrt) vs user-defined; recursive.
- **Example:** `void line(void)` (type 1); `int getNum(void)` (type 3).
- **Exam point:** a `void` function used in an expression → error.

### Arguments
- **Means:** values passed to a function.
- **Key facts:** **call by value** – a copy is passed (changes don't affect the caller); **call by reference** – the address is passed (pointer), changes affect the caller; order of argument evaluation is unspecified.
- **Example:** `void inc(int *p) { (*p)++; }` → `inc(&x);` increases x.
- **Exam point:** C itself is call by value; reference is simulated with pointers.

### Recursion
- **Means:** a function calling itself (directly or indirectly).
- **Key facts:** needs a **base case**; uses the stack (one frame per call); can overflow; examples – factorial, Fibonacci, GCD, Tower of Hanoi, binary search.
- **Example:** `int f(int n) { return n == 0 ? 0 : n + f(n - 1); }` → f(4) = 10.
- **Exam point:** statements after the recursive call run in **reverse** order of calls.

### Passing arrays to functions
- **Means:** sending an array to a function – the **address of the first element** is passed.
- **Key facts:** changes inside affect the original; pass the size separately; `void f(int a[], int n)` = `void f(int *a, int n)`; 2-D: column size required `void g(int m[][4], int r)`.
- **Example:** `void zero(int a[], int n) { for (int i = 0; i < n; i++) a[i] = 0; }`
- **Exam point:** `sizeof(a)` inside the function = pointer size (8), not the array size.

### Storage classes – automatic
- **Means:** `auto` – default for local variables.
- **Key facts:** stored on the **stack**; default value **garbage**; scope – the block; lifetime – until the block ends.
- **Example:** `void f() { auto int x = 0; x++; printf("%d", x); }` → prints 1 every call.
- **Exam point:** writing `auto` is optional.

### Storage classes – register
- **Means:** request to keep the variable in a **CPU register** for speed.
- **Key facts:** default garbage; block scope and lifetime; the compiler may ignore it; **`&` not allowed**; used for loop counters.
- **Example:** `register int i; for (i = 0; i < 1000; i++) …`
- **Exam point:** `&i` on a register variable → compile error.

### Storage classes – external
- **Means:** `extern` – a global variable defined elsewhere (another file or later in the same file).
- **Key facts:** stored in the data segment; default **0**; scope – whole program; lifetime – whole run; `extern int x;` declares, does not allocate.
- **Example:** file1.c `int count = 5;` · file2.c `extern int count;`
- **Exam point:** global variables are extern by default.

### Storage classes – static
- **Means:** variable that keeps its value between calls (local static) or is private to the file (global static).
- **Key facts:** data segment; default **0**; initialised **once**; lifetime – whole program.
- **Example:** `void f() { static int c; c++; printf("%d ", c); }` called 3 times → 1 2 3.
- **Exam point:** static local = block scope but program lifetime."""}],

    "Pointers": [{"title": W + "Pointers", "md": """> **Syllabus:** Definition, notation, pointers and arrays, arrays of pointers, pointers and functions – call by value and call by reference, pointers to pointers

### Definition (of a pointer)
- **Means:** a variable that stores the **address** of another variable.
- **Key facts:** size is the same for every type (8 bytes on 64-bit, 4 on 32-bit, 2 in old 16-bit Turbo C); uses – call by reference, dynamic memory, arrays/strings, data structures (linked lists, trees).
- **Example:** `int x = 7; int *p = &x;` → p holds x's address.
- **Exam point:** an uninitialised pointer is a **wild** pointer; `NULL` points nowhere.

### Notation
- **Means:** the symbols used: `&` (address-of) and `*` (value-at / indirection; also used in declarations).
- **Key facts:** `*p` = value at p; `&*p` = p; `*&x` = x; `%p` prints an address; `p++` moves by sizeof(type).
- **Example:** `int x = 7, *p = &x; *p = 9; printf("%d", x);` → 9.
- **Exam point:** `int *p, q;` → only p is a pointer.

### Pointers and arrays
- **Means:** an array name acts as a constant pointer to its first element.
- **Key facts:** `a[i]` ≡ `*(a + i)` ≡ `*(i + a)` ≡ `i[a]`; `p = a;` allowed, `a = p;` / `a++` not; pointer difference gives element count.
- **Example:** `int a[] = {2, 4, 6}, *p = a; printf("%d %d", *(p + 1), *p + 1);` → 4 3.
- **Exam point:** `sizeof(a)` = whole array; `sizeof(p)` = 8.

### Arrays of pointers
- **Means:** an array whose elements are pointers: `int *ap[3];`
- **Key facts:** common for lists of strings: `char *days[] = {"Mon", "Tue", "Wed"};` (each element points to a string); differs from a pointer to an array `int (*pa)[3];`.
- **Example:** `printf("%s %c", days[1], *days[2]);` → Tue W
- **Exam point:** `argv` in `main(int argc, char *argv[])` is an array of pointers.

### Pointers and functions
- **Means:** passing pointers to functions, returning pointers, and pointers to functions.
- **Key facts:** passing `&x` lets the function change x; never return the address of a local variable; function pointer `int (*fp)(int, int) = add; fp(2, 3);`
- **Example:** `void reset(int *p) { *p = 0; }`
- **Exam point:** `int *f();` = function returning pointer; `int (*f)();` = pointer to function.

### Call by value
- **Means:** the function gets a **copy** of the argument.
- **Key facts:** changes to parameters are lost on return; safe; default in C.
- **Example:** `void sw(int a, int b) { int t = a; a = b; b = t; }` → `sw(x, y)` leaves x and y unchanged.
- **Exam point:** the classic "swap doesn't work" question.

### Call by reference
- **Means:** the function gets the **address**, so it changes the original.
- **Key facts:** declare pointer parameters, call with `&`; used to "return" several values.
- **Example:** `void sw(int *a, int *b) { int t = *a; *a = *b; *b = t; }` → `sw(&x, &y)` swaps.
- **Exam point:** scanf uses call by reference (`&x`).

### Pointers to pointers
- **Means:** a pointer that stores the address of another pointer: `int **pp`.
- **Key facts:** `**pp` reaches the original value; used for 2-D dynamic arrays, changing a pointer inside a function, `char **argv`.
- **Example:** `int x = 5, *p = &x, **pp = &p; **pp += 1; printf("%d", x);` → 6.
- **Exam point:** levels: `*pp` = p (an address), `**pp` = x (a value)."""}],

    "Structures and Unions": [{"title": W + "Structures and unions", "md": """> **Syllabus:** Structures – definition, declaration, accessing elements, arrays of structures, structure in a structure, pointers and structures; unions – definition, declaration, accessing elements; typedef, enum, bit fields

### Structures – definition
- **Means:** a user-defined type grouping variables of **different types** under one name.
- **Key facts:** keyword `struct`; members get separate memory; size ≥ sum of members (padding).
- **Example:** `struct book { char title[40]; float price; int pages; };`
- **Exam point:** definition ends with `};` and allocates **no memory** until a variable is declared.

### Declaration (of structure variables)
- **Means:** creating variables of the structure type.
- **Key facts:** `struct book b1, b2;` or together with the definition `struct book {…} b1;`; initialise `struct book b = {"C", 250.0, 300};`
- **Example:** `struct point { int x, y; } p = {3, 4};`
- **Exam point:** members cannot be initialised inside the definition.

### Accessing elements
- **Means:** reading/writing members with the dot operator `.`
- **Key facts:** `b1.price = 300;` ; `scanf("%d", &b1.pages);` ; strings: `strcpy(b1.title, "DS");` (not `b1.title = "DS"`).
- **Example:** `printf("%d", p.x + p.y);` → 7.
- **Exam point:** whole structures can be assigned (`b2 = b1`) but not compared (`b1 == b2` is an error).

### Arrays of structures
- **Means:** an array whose elements are structures – a table of records.
- **Key facts:** `struct student s[60];` → `s[i].marks`; loop over records.
- **Example:** `struct emp e[3]; for (i = 0; i < 3; i++) total += e[i].sal;`
- **Exam point:** `sizeof(s)` = 60 × sizeof(struct student).

### Structure in a structure (nested)
- **Means:** a member that is itself a structure.
- **Key facts:** access with two dots: `e.dob.year`; inner type defined before or inside.
- **Example:** `struct date { int d, m, y; }; struct emp { char name[20]; struct date dob; } e; e.dob.y = 1990;`
- **Exam point:** a structure cannot contain itself, only a pointer to itself.

### Pointers and structures
- **Means:** pointer variables that point to structures.
- **Key facts:** `struct book *pb = &b1;` access with arrow `pb->price` = `(*pb).price`; basis of linked lists (`struct node *next`); pass pointers to functions to avoid copying.
- **Example:** `pb->pages += 10;`
- **Exam point:** `*pb.price` is wrong (`.` binds tighter than `*`).

### Unions – definition
- **Means:** like a structure, but **all members share one memory location**.
- **Key facts:** keyword `union`; size = largest member (rounded for alignment); saves memory when only one member is needed at a time.
- **Example:** `union data { int i; float f; char s[8]; };` → sizeof = 8.
- **Exam point:** union size = max, structure size = sum (+ padding).

### Unions – declaration
- **Means:** creating union variables.
- **Key facts:** `union data d1;` ; only the **first member** can be initialised in C89: `union data d = {10};` (C99 designated: `{.f = 2.5}`).
- **Example:** `union data d = {65};`
- **Exam point:** declaring a union allocates memory for its largest member only.

### Unions – accessing elements
- **Means:** using `.` (or `->`) just like structures.
- **Key facts:** writing one member overwrites the others; read only the member last written.
- **Example:** `d.i = 65; d.f = 1.5; printf("%d", d.i);` → not 65 (the float overwrote it).
- **Exam point:** a union holds **one** valid value at a time.

### typedef
- **Means:** creates a new name (alias) for an existing type.
- **Key facts:** `typedef unsigned int uint;` · `typedef struct book Book;` · `typedef struct { int x, y; } Point;` – does not create a new type, just a name.
- **Example:** `Point p = {1, 2};`
- **Exam point:** typedef is handled by the compiler; `#define` by the preprocessor.

### enum
- **Means:** user-defined type of named integer constants.
- **Key facts:** starts at 0, each next +1 unless assigned; values may repeat.
- **Example:** `enum day { MON = 1, TUE, WED }; printf("%d", WED);` → 3.
- **Exam point:** `enum {A, B = 5, C};` → A 0, B 5, C 6.

### Bit fields
- **Means:** structure members with a specified number of **bits**.
- **Key facts:** `struct { unsigned on : 1; unsigned mode : 3; } f;` saves memory (flags, hardware registers); range of a 3-bit unsigned field 0–7; no `&` on a bit field; no arrays of bit fields.
- **Example:** `f.mode = 9;` stores 9 mod 8 = 1.
- **Exam point:** width cannot exceed the bits of the base type."""}],

    "Bitwise Operators": [{"title": W + "Bitwise operators", "md": """> **Syllabus:** Bitwise AND, OR, exclusive OR, complement, right shift and left shift operators

### Bitwise AND (`&`)
- **Means:** result bit is 1 only if **both** bits are 1.
- **Key facts:** used for **masking** (keep chosen bits), testing a bit, checking odd/even (`n & 1`).
- **Example:** 12 & 10 → 1100 & 1010 = 1000 = **8**; `0x2F & 0x0F` = 0x0F.
- **Exam point:** `&` (bitwise) ≠ `&&` (logical): 4 & 2 = 0 but 4 && 2 = 1.

### Bitwise OR (`|`)
- **Means:** result bit is 1 if **either** bit is 1.
- **Key facts:** used to **set** bits: `flags | (1 << n)`.
- **Example:** 12 | 10 → 1110 = **14**; 5 | 2 = 7.
- **Exam point:** x | 0 = x; x | x = x.

### Exclusive OR (`^`)
- **Means:** result bit is 1 if the bits are **different**.
- **Key facts:** x ^ x = 0, x ^ 0 = x; used to **toggle** bits, swap without a temporary, simple encryption, find the odd-one-out.
- **Example:** 12 ^ 10 → 0110 = **6**; a = 5, b = 9: a ^= b; b ^= a; a ^= b → a = 9, b = 5.
- **Exam point:** `^` is XOR, **not** power in C (use `pow`).

### Complement (`~`)
- **Means:** one's complement – flips every bit (unary).
- **Key facts:** for signed int, **~x = −(x + 1)**; for unsigned 8-bit, ~x = 255 − x.
- **Example:** ~5 = **−6**; ~0 = −1; `(unsigned char)~5` = 250.
- **Exam point:** two's complement = one's complement + 1 (that is how −x is stored).

### Right shift (`>>`)
- **Means:** moves bits right by n places.
- **Key facts:** x >> n = x ÷ 2ⁿ (integer); unsigned → zeros come in on the left; signed negative → implementation-defined (usually sign bit copied).
- **Example:** 40 >> 3 = **5**; 7 >> 1 = 3.
- **Exam point:** shifting by a negative count or ≥ the width is undefined.

### Left shift (`<<`)
- **Means:** moves bits left by n places, zeros fill on the right.
- **Key facts:** x << n = x × 2ⁿ (if no overflow); `1 << n` makes a mask with bit n set.
- **Example:** 5 << 2 = **20**; 1 << 4 = 16.
- **Exam point:** `<<`/`>>` have **lower** precedence than `+`/`-`: `1 << 2 + 1` = 1 << 3 = 8."""}],

    "C Preprocessor": [{"title": W + "C preprocessor", "md": """> **Syllabus:** Types of C preprocessor directives, macros, file inclusion

### C preprocessor
- **Means:** a program that processes the source **before compilation** – handles lines starting with `#`.
- **Key facts:** removes comments, expands macros, includes files, compiles conditionally; directives end at the line end (no `;`); `gcc -E` shows its output.
- **Exam point:** preprocessing is the **first** stage of the build.

### Types of preprocessor directives
- **Means:** the kinds of `#` commands.
- **Key facts:** (1) **macro substitution** – `#define`, `#undef`; (2) **file inclusion** – `#include`; (3) **conditional compilation** – `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`; (4) **miscellaneous** – `#pragma`, `#error`, `#line`.
- **Example:** `#ifdef DEBUG printf("x=%d", x); #endif` – compiled only when DEBUG is defined.
- **Exam point:** `#pragma` gives compiler-specific instructions (`#pragma once`, `#pragma pack(1)`).

### Macros
- **Means:** names replaced by text before compiling – object-like (`#define PI 3.14`) and function-like (`#define SQ(x) ((x) * (x))`).
- **Key facts:** pure text substitution – no type checking; faster (no call) but bigger code; bracket every argument and the whole body; `#` stringises, `##` joins tokens; `#undef` removes.
- **Example:** `#define SQ(x) x * x` → `SQ(2 + 3)` = 2 + 3 * 2 + 3 = **11**; with brackets = 25.
- **Exam point:** `#define MAX 10;` (with `;`) breaks expressions where MAX is used.

### File inclusion
- **Means:** `#include` copies another file's contents into the program.
- **Key facts:** `#include <file.h>` searches standard directories; `#include "file.h"` searches the current directory first; header files hold prototypes, macros, typedefs; guard against double inclusion with `#ifndef X_H #define X_H … #endif`.
- **Example:** `#include <math.h>` gives `sqrt()`, `pow()`; `#include "myfuns.h"`.
- **Exam point:** including a header gives declarations; the library code itself is added by the **linker**."""}],

    "Files": [{"title": W + "Files", "md": """> **Syllabus:** File operating modes, text and binary files, high-level and low-level operations on files, command line arguments

### File operating modes
- **Means:** the second argument of `fopen` that says how the file is used.
- **Key facts:** `"r"` read (file must exist, else NULL), `"w"` write (creates or **erases**), `"a"` append (creates, writes at end), `"r+"` read/write (must exist), `"w+"` read/write (erases), `"a+"` read/append; add `b` for binary (`"rb"`, `"wb+"`).
- **Example:** `FILE *fp = fopen("data.txt", "a");`
- **Exam point:** opening an existing file with `"w"` deletes its contents.

### Text files
- **Means:** files of readable characters arranged in lines.
- **Key facts:** numbers stored as digit characters (12345 → 5 bytes); newline may be translated (`\\r\\n` on Windows); functions `fprintf`, `fscanf`, `fgets`, `fputs`, `fgetc`, `fputc`.
- **Example:** `fprintf(fp, "%d %s\\n", roll, name);`
- **Exam point:** text files are portable but larger and slower to parse.

### Binary files
- **Means:** files storing data exactly as in memory (bytes).
- **Key facts:** int always 4 bytes; no newline translation; `fread`, `fwrite`; good for records/structures, images.
- **Example:** `fwrite(&rec, sizeof rec, 1, fp);` · `fread(&rec, sizeof rec, 1, fp);`
- **Exam point:** fread/fwrite return the number of **items** (not bytes) transferred.

### High-level operations on files
- **Means:** buffered, stream-based I/O through `FILE *` (stdio.h) – portable.
- **Key facts:** `fopen`, `fclose`, `fgetc/fputc`, `fgets/fputs`, `fprintf/fscanf`, `fread/fwrite`, `fseek` (SEEK_SET/CUR/END), `ftell`, `rewind`, `feof`, `ferror`, `remove`, `rename`.
- **Example:** `fseek(fp, 0, SEEK_END); long size = ftell(fp);`
- **Exam point:** always check `fp == NULL`; `fclose` flushes the buffer.

### Low-level operations on files
- **Means:** unbuffered, system-call I/O using integer **file descriptors** (UNIX `<fcntl.h>`, `<unistd.h>`).
- **Key facts:** `open(name, O_RDONLY | O_WRONLY | O_CREAT …, mode)` returns an int fd; `read(fd, buf, n)`, `write(fd, buf, n)`, `lseek(fd, off, whence)`, `close(fd)`; standard fds 0 (stdin), 1 (stdout), 2 (stderr).
- **Example:** `int fd = open("a.txt", O_RDONLY); n = read(fd, buf, 100); close(fd);`
- **Exam point:** high-level = `FILE *` + buffering; low-level = `int` descriptor, no buffering, faster for big blocks, less portable.

### Command line arguments
- **Means:** values typed after the program name, received by `main(int argc, char *argv[])`.
- **Key facts:** `argc` = count **including** the program name; `argv[0]` = program name; `argv[argc]` = NULL; all arguments are strings → convert with `atoi`, `atof`.
- **Example:** `./copy a.txt b.txt` → argc = 3, argv[1] = "a.txt", argv[2] = "b.txt".
- **Exam point:** `./sum 4 5` → `atoi(argv[1]) + atoi(argv[2])` = 9."""}],
}
