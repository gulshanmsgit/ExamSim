"""KRIES Computer Teacher · C Programming · P2-KRC-05 Functions and P2-KRC-06 Pointers (2 topics × 2 sets × 30), with NOTES.
Pulls the matching GPSTR questions of 'Programming in C – Part 1 / Part 2' (tools/p2u4_b.py), adds REAL previous-year questions (exact
wording, printed option order, `source`) and new ones. Official answers: KEA final keys for Legislative Council Secretariat 2024
(Computer Operator P2, Sr/Jr Programmer P2 – A1) and GTTC 2024 Technician Gr-III CS (C1). KSET questions come from packs/pyq-p2.json;
GFGC 2021 and PGCET answers were worked out by ExamSim (read from the page images). Every recursion and pointer trace was done by hand."""
from p2u4_b import SUBPROGRAMS as U, POINTERS as P
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

FUNC_BASICS = [
    U[2], U[3], U[16], U[25], U[28], U[29],
    ("Identify the structure/structures used in the syntax of function in C.\n(a) Function declaration\n(b) Function definition\n(c) Function call",
     ["a and b only", "a, b and c", "b only", "a and c only"], 1, "A function is declared (prototype), defined and called." + KLC,
     "Legislative Council 2024 Computer Operator P2 · Q10"),
    ("Given a factorial function in C\nint fact(int n) {\n  int fact = 1;\n  for (int i = 1; i <= n; i++) fact *= i;\n  return fact;\n}\n"
     "Which is the correct C function from the given options which finds the binomial coefficient ⁿCᵣ?",
     ["int ⁿCᵣ (int r, int n) {\n  return fact(n)/(fact (n − r) * fact(r));}", "int ⁿCᵣ (int n, int r) {\n  return fact(n)/(fact (r) * fact(n − r));}",
      "int ⁿCᵣ (int r, int n) {\n  return fact(n)/(fact (r) * fact(n − r));}", "int ⁿCᵣ (int n, int r) {\n  return fact(n)/(fact (r − n) * fact(r));}"], 1,
     "ⁿCᵣ = n! / (r! (n − r)!). Options 1–3 all use this formula; option 2 also takes the arguments in the usual order (n, r), so it is the intended answer."
     + NOTE, "PGCET 2026 CS · Q94"),
    ("A function definition in C consists of", ["A return type, a name, a parameter list and a body", "A name and a body alone", "A prototype and a call",
                                                "A header file"], 0, "int add(int a, int b) { return a + b; }"),
    ("Which is a correct prototype of a function that takes two ints and returns a float?", ["float avg(int, int);", "avg(int a, int b) float;",
                                                                                             "float avg(int a; int b);", "float avg[int, int];"], 0,
     PYQ + "Parameter names are optional in a prototype."),
    ("Based on arguments and return values, user-defined functions are classified into", ["Four categories: no arguments/no return, arguments/no return, "
                                                                                          "no arguments/return, arguments/return", "Two categories",
                                                                                          "Library and user-defined", "Recursive and iterative"], 0, "Balagurusamy, ch. 9."),
    ("printf() and sqrt() are examples of", ["Library (built-in) functions", "User-defined functions", "Recursive functions", "Macros"], 0,
     "sqrt needs <math.h> (and -lm on Linux)."),
    ("In the call  sum(a, b)  made from main, a and b are", ["Actual arguments", "Formal parameters", "Local variables of sum", "Global variables"], 0,
     "The variables in sum's definition are the formal parameters."),
    ("Through its return statement, a C function can send back", ["At most one value", "Any number of values", "Exactly two values", "Integers alone"], 0,
     "Use pointers or a structure to return several values."),
    ("A function declared as  void show(void)", ["Takes no arguments and returns no value", "Returns a void pointer", "Takes any number of arguments", "Returns 0"], 0,
     "In C, an empty list () means 'unspecified arguments'; (void) means none."),
    ("What is printed?\nint sq(int x) { return x * x; }\n…\nprintf(\"%d\", sq(3) + sq(2));", ["13", "25", "10", "36"], 0, "9 + 4."),
    ("What is printed?\nvoid swap(int a, int b) { int t = a; a = b; b = t; }\nint main() { int x = 1, y = 2; swap(x, y); printf(\"%d %d\", x, y); }",
     ["1 2", "2 1", "2 2", "1 1"], 0, PYQ + "Call by value: swap works on copies."),
    ("What is printed?\nint f(int x) { return x + 1; }\nint g(int x) { return 2 * x; }\n…\nprintf(\"%d\", f(g(3)));", ["7", "8", "6", "4"], 0, "g(3) = 6, f(6) = 7."),
    ("With  int f(int n) { if (n > 0) return 1; return -1; },  f(0) returns", ["−1", "1", "0", "Nothing"], 0, "The first return is skipped because 0 > 0 is false."),
    ("If a prototype says  int f(int);  the call  f(1, 2)  gives", ["A compile-time error", "2", "1", "A runtime error"], 0, "The prototype lets the compiler check calls."),
    ("C passes arguments to functions", ["By value – passing a pointer lets the function change the caller's variable", "By reference always", "By name",
                                         "By value-result"], 0, PYQ + "Arrays decay to pointers, so array elements can be changed."),
    ("A variable declared inside a function is visible", ["Inside that function (block) alone", "In all functions", "In the whole file after it", "In main as well"], 0,
     "Its scope is local."),
    ("Which is NOT an advantage of using functions?", ["Programs always run faster", "Code reuse", "Easier debugging", "Modularity"], 0,
     "Calls add a little overhead."),
    ("A function's return value", ["May be ignored by the caller", "Must always be stored", "Must be printed", "Must be a pointer"], 0,
     "printf's return value is usually ignored."),
    ("What is printed?\nint f(int a, int b) { return a - b; }\n…\nprintf(\"%d\", f(10, f(4, 1)));", ["7", "5", "3", "−7"], 0, "f(4, 1) = 3; f(10, 3) = 7."),
    ("The keyword that sends a value back from a function to its caller is", ["return", "break", "exit", "back"], 0, "exit ends the whole program."),
    ("C does not allow two functions with the same name in one program because", ["C has no function overloading", "Names are case-insensitive",
                                                                                  "Prototypes are optional", "main must be unique"], 0, "C++ allows overloading."),
    ("What is printed?\nint max(int a, int b) { return a > b ? a : b; }\n…\nprintf(\"%d\", max(max(3, 9), 5));", ["9", "5", "3", "17"], 0, "max(3, 9) = 9; max(9, 5) = 9."),
    ("A function declared static at file level", ["Is visible in its own source file alone", "Keeps its local variables between calls", "Runs once",
                                                  "Cannot return a value"], 0, "static limits linkage to the file."),
    ("A function prototype is also called a", ["Function declaration", "Function definition", "Function call", "Function body"], 0,
     "It ends with a semicolon and has no body."),
]

RECURSION_STORAGE = [
    U[8], U[9], U[10], U[11], U[12], U[13], U[14], U[15], U[17], U[20], U[22], U[23], U[24], U[27],
    ("Predict the output of the following program\n#include<stdio.h>\nint fun(int n)\n{\n  if (n == 4)\n    return n;\n  else\n    return 2*fun(n+1);\n}\nint main ()\n{\n"
     "  printf (\"%d\", fun(2));\n  return(0);\n}", ["4", "8", "16", "runtime error"], 2, "fun(2) = 2·fun(3) = 2·2·fun(4) = 4·4 = 16." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q54"),
    ("What is the output of the following code?\n#include <stdio.h>\nvoid main ()\n{\n  static int x = 3;\n  x++;\n  if (x <= 6)\n  {\n    printf (\"World\");\n    main ();\n  }\n}",
     ["World", "World World World", "Infinite loop", "World World"], 1,
     "x is static, so it keeps counting: 4, 5, 6 print World, 7 stops the recursion." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q90"),
    ("Static variable means ____", ["It is same as an automatic variable but is placed at the head of a program.", "It cannot be initialized.",
                                    "It retains its value throughout the file of the program.",
                                    "It is initialized once at the commencement of execution and cannot be changed at run time."], 2,
     "A static variable lives for the whole run and keeps its value between calls (it can be changed)." + NOTE, "GFGC 2021 CS · Q29"),
    ("A recursive function must have", ["A base (terminating) condition", "A loop", "A global variable", "A pointer argument"], 0, "Without it the recursion never stops."),
    ("A recursive function without a base case usually ends with", ["A stack overflow at run time", "A compile-time error", "The correct answer", "An infinite loop with no memory use"], 0,
     "Each call pushes a new activation record."),
    ("What does p(2, 5) return?\nint p(int b, int e) { return e == 0 ? 1 : b * p(b, e - 1); }", ["32", "10", "25", "16"], 0, "2⁵."),
    ("What is printed by f(3)?\nvoid f(int n) { if (n == 0) return; f(n - 1); printf(\"%d\", n); }", ["123", "321", "3", "0123"], 0,
     PYQ + "The printf runs while the calls return, so the smallest value prints first."),
    ("What is printed by f(3)?\nvoid f(int n) { if (n == 0) return; printf(\"%d\", n); f(n - 1); }", ["321", "123", "3210", "1"], 0, "Here printf runs before the recursive call."),
    ("What does gcd(48, 18) return?\nint gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }", ["6", "18", "3", "2"], 0, "(48, 18) → (18, 12) → (12, 6) → (6, 0)."),
    ("What is printed?\nvoid f(int a[]) { a[0] = 99; }\nint main() { int x[3] = {1, 2, 3}; f(x); printf(\"%d\", x[0]); }", ["99", "1", "0", "Garbage"], 0,
     PYQ + "The array's address is passed, so the function changes the caller's array."),
    ("Inside  void f(int a[10]),  sizeof(a) gives", ["The size of a pointer", "40", "10", "0"], 0, "The parameter is really int *a; pass the length separately."),
    ("The four storage classes in C are", ["auto, register, static and extern", "int, float, char and double", "local, global, public and private",
                                           "const, volatile, signed and unsigned"], 0, "They decide storage place, default value, scope and lifetime."),
    ("The default initial value of a static or global (extern) variable is", ["0", "Garbage", "1", "−1"], 0, PYQ + "auto and register variables start with garbage."),
    ("A local variable declared without any storage class specifier is", ["auto", "static", "register", "extern"], 0, "Stored on the stack."),
    ("The lifetime of an auto variable is", ["Until control leaves the block in which it is defined", "The whole program run", "Until the program is recompiled",
                                            "Until free() is called"], 0, "static variables live for the whole run."),
    ("What is printed?\nint x = 10;\nint main() { int x = 20; printf(\"%d\", x); }", ["20", "10", "30", "Compile error"], 0, "The local x hides the global x."),
]

PTR_BASICS = [
    P[0], P[1], P[2], P[9], P[12], P[13], P[14], P[15], P[16], P[17], P[21], P[23], P[24], P[28], P[29],
    kset("KSET 2024 CS&A · Q23"),
    ("The dynamic memory allocation functions in C language are defined in ____", ["<stdio.h>", "<stdlib.h>", "<string.h>", "<conio.h>"], 1,
     "malloc, calloc, realloc and free." + NOTE, "PGCET 2026 CS · Q91"),
    ("With pointers, the operators & and * are the", ["Address-of and indirection (dereference) operators", "Bitwise AND and multiplication operators",
                                                      "Logical operators", "Assignment operators"], 0, "&x gives x's address; *p gives the value at p."),
    ("int *p;  declares p as", ["A pointer to an int", "An int", "A pointer to a pointer", "An array"], 0, "The * belongs to p: int *p, q; makes q a plain int."),
    ("Which printf format specifier prints a pointer value (address)?", ["%p", "%d", "%a", "%s"], 0, "Cast to (void *) for portability."),
    ("A NULL pointer", ["Points to no valid object", "Points to address 1", "Is an uninitialised pointer", "Points to itself"], 0,
     "Dereferencing it is an error (usually a crash)."),
    ("If  double *d  holds 2000 (8-byte double), then d + 3 is", ["2024", "2003", "2006", "2012"], 0, PYQ + "Pointer arithmetic scales by the size of the type."),
    ("Which pointer operation is allowed in C?", ["Subtracting two pointers into the same array", "Adding two pointers", "Multiplying a pointer by 2",
                                                  "Dividing two pointers"], 0, "The difference is the number of elements between them."),
    ("What is printed?\nint x = 7, *p = &x;\nprintf(\"%d %d\", *p, *&x);", ["7 7", "7 and an address", "Two addresses", "Compile error"], 0, "*&x is x."),
    ("What is printed?\nint a = 5;\nint *p = &a;\n*p = *p * 2;\nprintf(\"%d\", a);", ["10", "5", "25", "An address"], 0, "a is changed through p."),
    ("What is printed?\nvoid *vp;\nint i = 3;\nvp = &i;\nprintf(\"%d\", *(int *)vp);", ["3", "Garbage", "Compile error", "0"], 0,
     "A void pointer must be cast before it is dereferenced."),
    ("A pointer that still holds the address of memory that has been freed is a", ["Dangling pointer", "NULL pointer", "Void pointer", "Near pointer"], 0,
     "Set it to NULL after free()."),
    ("int *p = (int *) malloc(5 * sizeof(int));  allocates", ["Space for 5 ints on the heap", "5 bytes", "One int with the value 5", "Space on the stack"], 0,
     PYQ + "Check for NULL and free() it later."),
    ("What is printed?\nint x = 4, *p = &x;\nprintf(\"%d\", *p * *p);", ["16", "8", "An address", "Compile error"], 0,
     "* in front of p dereferences; the middle * multiplies: 4 × 4."),
    ("Which statement stores the address of x in the pointer p?", ["p = &x;", "p = *x;", "*p = &x;", "&p = x;"], 0, "Then *p refers to x."),
]

PTR_ARRAYS = [
    P[3], P[4], P[5], P[6], P[7], P[8], P[10], P[11], P[18], P[19], P[20], P[22], P[25], P[26], P[27],
    kset("KSET 2024 CS&A · Q22"),
    ("For an array a, a[i] is equivalent to", ["*(a + i)", "*a + i", "&a + i", "a + *i"], 0, "That is why i[a] also works."),
    ("What is printed?\nchar *names[] = {\"Ram\", \"Sita\", \"Gita\"};\nprintf(\"%s %c\", names[1], *names[2]);", ["Sita G", "Ram S", "Sita Gita", "Gita S"], 0,
     PYQ + "names is an array of pointers to strings; *names[2] is the first character of \"Gita\"."),
    ("int **pp;  declares pp as", ["A pointer to a pointer to int", "A pointer to an int", "A 2-D array", "An int"], 0, "It can hold the address of an int * variable."),
    ("What is printed?\nvoid inc(int *p) { (*p)++; }\nint main() { int n = 5; inc(&n); inc(&n); printf(\"%d\", n); }", ["7", "5", "6", "Garbage"], 0,
     "Call by reference through a pointer."),
    ("A C function can give several results back to its caller by", ["Taking pointer parameters and storing the results through them", "Several return statements",
                                                                     "Returning an array by value", "Using goto"], 0, "E.g. void divmod(int a, int b, int *q, int *r)."),
    ("What is printed?\nint a[] = {2, 4, 6, 8}, *p = a + 3;\nprintf(\"%d\", *p - *(p - 2));", ["4", "2", "6", "8"], 0, "*p = 8, *(p − 2) = a[1] = 4."),
    ("What is printed?\nchar s[] = \"ABC\", *p = s;\nwhile (*p) putchar(*p++);", ["ABC", "BC", "A", "An infinite loop"], 0,
     "*p++ uses the character, then moves p; the loop stops at '\\0'."),
    ("What is printed?\nint x = 3, *p = &x, **q = &p;\n**q = **q + *p;\nprintf(\"%d\", x);", ["6", "3", "9", "An address"], 0, PYQ + "**q and *p are both x: x = 3 + 3."),
    ("In  int main(int argc, char *argv[]),  argv is", ["An array of pointers to char (the argument strings)", "A 2-D int array", "A pointer to int", "A single string"], 0,
     "argv[0] is the program name."),
    ("What is printed?\nint add(int a, int b) { return a + b; }\n…\nint (*fp)(int, int) = add;\nprintf(\"%d\", fp(2, 3));", ["5", "Address of add", "23", "Compile error"], 0,
     "A function pointer can be called like the function."),
    ("For a 2-D array a, a[i][j] is equivalent to", ["*(*(a + i) + j)", "*(a + i + j)", "**a + i + j", "*(a[i] + i)"], 0, "a + i points to row i."),
    ("char *p = \"hello\";  p[0] = 'H';", ["Undefined behaviour – string literals must not be modified", "Changes the string to Hello", "Always a compile-time error",
                                          "Prints H"], 0, PYQ + "Use char p[] = \"hello\"; for a modifiable copy."),
    ("What is printed?\nint a = 10, b = 20, *p = &a, *q = &b;\n*p = *q;\nprintf(\"%d %d\", a, b);", ["20 20", "10 20", "20 10", "10 10"], 0, "a gets the value of b."),
    ("What is printed?\nint a[5] = {1, 2, 3, 4, 5}, *p = a;\np += 3;\nprintf(\"%d\", p[-1]);", ["3", "4", "2", "Garbage"], 0, "p points to a[3]; p[−1] = a[2]."),
]

TOPICS = {
    "Functions": [
        ("1 · Function Definition, Prototypes, Types of Functions and Arguments", FUNC_BASICS),
        ("2 · Recursion, Passing Arrays and Storage Classes", RECURSION_STORAGE),
    ],
    "Pointers": [
        ("1 · Pointer Basics, Notation and Pointer Arithmetic", PTR_BASICS),
        ("2 · Pointers and Arrays, Arrays of Pointers, Call by Reference and Pointers to Pointers", PTR_ARRAYS),
    ],
}

NOTES = {
    "Functions": [{"title": "Functions – revision sheet", "md": """## Definition and prototypes
- Declaration (prototype) `float avg(int, int);` → definition `float avg(int a, int b) { … }` → call `avg(x, y)`
- Actual arguments (in the call) vs formal parameters (in the definition)
- One return value at most; `void f(void)` = no arguments, no value; C89 default return type int
- Categories: no args/no return, args/no return, no args/return, args/return; library vs user-defined
- C passes **by value**; pass an address (`&x`) to let a function change the caller's variable (call by reference)
- No overloading; no nested function definitions; a file-level `static` function is private to its file

## Recursion
- Needs a base case, else stack overflow; one activation record per active call
- fact(5) → 6 calls; fib(n) is exponential; `fun(2)` with `n == 4 ? n : 2*fun(n+1)` = 16
- Print before the call → 3 2 1; print after the call → 1 2 3
- gcd(a, b) = b == 0 ? a : gcd(b, a % b)

## Passing arrays
- `f(int a[])` = `f(int *a)` – the address is passed; changes affect the caller; `sizeof(a)` inside = pointer size

## Storage classes
| Class | Storage | Default | Scope | Lifetime |
|---|---|---|---|---|
| auto | stack | garbage | block | block |
| register | CPU register | garbage | block | block (no `&`) |
| static | data segment | 0 | block / file | whole run (keeps value) |
| extern | data segment | 0 | global (other files) | whole run |
- `static int x = 3; x++; if (x <= 6) { printf("World"); main(); }` → World ×3
"""}],
    "Pointers": [{"title": "Pointers – revision sheet", "md": """## Basics
- `int *p = &x;` → `*p` is x; `&` address-of, `*` indirection; `%p` prints addresses
- NULL pointer (points nowhere), wild pointer (uninitialised), dangling pointer (memory freed), void pointer (generic – cast before `*`)
- Pointer size does not depend on the type (8 bytes on 64-bit)
- Arithmetic scales by the type size: int* + 1 → +4; double* + 3 → +24; difference of two pointers = number of elements
- Not allowed: adding, multiplying or dividing pointers
- `const int *p` – value read-only; `int * const q` – pointer fixed
- `<stdlib.h>`: malloc(bytes) (garbage), calloc(n, size) (zeroed), realloc, free; memory leak = never freed

## Pointers and arrays
- `a[i]` = `*(a + i)` = `i[a]`; `a[i][j]` = `*(*(a + i) + j)`; array name is a constant pointer (`a++` illegal)
- `*p++` – use then move; `(*p)++` – increment the value; `++*p` – increment the value first
- `int *a[10]` – array of 10 pointers; `int (*b)[10]` – pointer to an array of 10 ints; `int (*fp)(int, int)` – function pointer
- `char *names[] = {"Ram", "Sita"}` – array of pointers to strings; `argv` is `char *argv[]`
- String literals are read-only (`char *p = "hello"; p[0] = 'H';` is undefined)

## Call by reference and pointers to pointers
- `void swap(int *x, int *y)`; call `swap(&a, &b)`
- `int **q = &p;` → `**q` is the int; `**q + *p` = 2x
- Never return the address of a local variable
"""}],
}
