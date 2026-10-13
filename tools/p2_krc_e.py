"""KRIES Computer Teacher · C Programming · P2-KRC-09 C Preprocessor and P2-KRC-10 Files (2 topics × 2 sets × 30), with NOTES.
Pulls the matching GPSTR questions of 'Programming in C – Part 2' (tools/p2u4_b.py), adds REAL previous-year questions (exact wording,
printed option order, `source`) and new ones. Official answers: KEA final keys for Legislative Council Secretariat 2024 Computer Operator
P2 (A1) and GTTC 2024 Technician Gr-III CS (C1). KSET 2025 Q41 comes from packs/pyq-p2.json; GFGC 2021 and PGCET answers were worked out by
ExamSim. Low-level I/O refers to the UNIX/POSIX calls open, read, write, lseek and close (<fcntl.h>, <unistd.h>). Every macro expansion
was done by hand."""
from p2u4_b import FILES_PREPROC as F
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

DIRECTIVES = [
    F[14], F[15], F[16], F[19], F[20], F[26],
    ("The C preprocessor are specified with ____ symbol.", ["#", "$", "\" \"", "&"], 0, "Every directive starts with #." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q89"),
    ("The C-preprocessors are specified with ____ symbol.", ["#", "$", "“ ”", "&"], 0, "#include, #define, #if …" + NOTE, "GFGC 2021 CS · Q27"),
    ("What is the correct sequence for the types of preprocessor directives?", ["Macro definition → Conditional compilation → File inclusion directive",
                                                                                "Macro definition → File inclusion directive → Conditional compilation",
                                                                                "File inclusion directive → Macro definition → Conditional compilation",
                                                                                "Conditional compilation → File inclusion directive → Macro definition"], 1,
     "The official key lists macro definition, file inclusion, then conditional compilation (the usual textbook order)." + KLC,
     "Legislative Council 2024 Computer Operator P2 · Q70"),
    ("The object code of the header files are linked to programs whenever required by using ____ software.", ["Loader", "Linker", "Assembler", "Compiler"], 1,
     "The linker joins the program's object code with the library code behind the header declarations." + NOTE, "PGCET 2023 M.Tech CS · Q27"),
    ("The three main kinds of preprocessor directives are", ["Macro substitution, file inclusion and conditional compilation", "Input, output and process",
                                                            "Declaration, definition and call", "Loop, branch and jump"], 0,
     PYQ + "Others: #undef, #pragma, #error, #line."),
    ("A preprocessor directive", ["Begins with # and is not ended by a semicolon", "Ends with a semicolon", "Must be inside main()", "Is executed at run time"], 0,
     "It is one line (continued with \\ if needed)."),
    ("#include <stdio.h> makes the preprocessor", ["Insert the text of stdio.h at that point", "Link the stdio library", "Call the stdio functions",
                                                  "Compile stdio.h separately"], 0, "File inclusion is textual."),
    ("User-defined header files are usually saved with the extension", [".h", ".c", ".hdr", ".lib"], 0, "Included with #include \"myfile.h\"."),
    ("#pragma is used to", ["Give compiler-specific instructions (e.g. #pragma once)", "Define a macro", "Include a file", "End the program"], 0,
     "Unknown pragmas are ignored."),
    ("#error \"message\" makes the", ["Preprocessor stop compilation and show the message", "Program print the message at run time", "Linker skip the file",
                                     "Compiler ignore the next line"], 0, "Used inside #if blocks to catch bad configurations."),
    ("__LINE__ expands to", ["The current source line number", "The number of lines in the file", "The line of the last error", "A newline character"], 0,
     "__FILE__, __DATE__, __TIME__ and __STDC__ are also predefined."),
    ("Which predefined macro gives the name of the current source file?", ["__FILE__", "__NAME__", "__SOURCE__", "__MAIN__"], 0, "printf(\"%s\", __FILE__);"),
    ("#pragma once at the top of a header file", ["Prevents it from being included more than once", "Runs the header once at run time", "Makes the header read-only",
                                                 "Is required in every C file"], 0, "A common alternative to #ifndef include guards."),
    ("The output of the preprocessor (e.g. gcc -E) is", ["Source code with macros replaced and headers inserted", "Object code", "Assembly code", "An executable"], 0,
     PYQ + "Saved as a .i file."),
    ("Comments in C source code are removed by the", ["Preprocessor", "Linker", "Loader", "Assembler"], 0, "Each comment becomes a space."),
    ("Can a .c file be included with #include?", ["Yes – any text file can be included, though headers are normal", "No, .h files alone", "System files alone",
                                                  "C++ files alone"], 0, "Including .c files is legal but poor style."),
    ("A header file normally contains", ["Function prototypes, macro definitions, type declarations and extern declarations", "The main() function",
                                         "Compiled object code", "Comments alone"], 0, "Definitions go in .c files."),
    ("Which header must be included to use sqrt()?", ["<math.h>", "<stdlib.h>", "<stdio.h>", "<ctype.h>"], 0, "Also pow(), sin(), ceil(), floor()."),
    ("The #include directive can appear", ["Anywhere in the file, though usually at the top", "As the first line alone", "Inside functions alone", "Once per file at most"], 0,
     "The text is inserted wherever the directive is."),
    ("The C preprocessor works on", ["The program text, before compilation, without knowing C types", "Machine code", "Object files", "The running program"], 0,
     "It does textual substitution."),
    ("#include <conio.h> is", ["A non-standard header used by Turbo C for getch() and clrscr()", "An ANSI standard header", "The maths library", "Needed for printf"], 0,
     "It is not available with gcc on Linux."),
    ("Which header declares exit(), malloc() and atoi()?", ["<stdlib.h>", "<stdio.h>", "<string.h>", "<ctype.h>"], 0, "stdlib = standard library utilities."),
    ("strlen() and strcpy() are declared in", ["<string.h>", "<stdio.h>", "<ctype.h>", "<stdlib.h>"], 0, "Also strcat, strcmp, memcpy."),
    ("Which of these is NOT a preprocessor directive?", ["#start", "#ifdef", "#undef", "#pragma"], 0, PYQ + "There is no #start."),
]

MACROS = [
    F[11], F[12], F[13], F[17], F[18], F[21], F[27],
    kset("KSET 2025 CS&A · Q41"),
    ("In  #define PI 3.14,  PI is a", ["Symbolic constant (object-like macro)", "Variable", "Function", "Keyword"], 0, "Every PI is replaced by 3.14 before compilation."),
    ("#define N 10;\nint a[N];", ["A compile-time error – the ; becomes part of the replacement", "An array of 10 ints", "An array of 11 ints", "A warning only"], 0,
     PYQ + "a[N] becomes a[10;]."),
    ("#define SQR(x) ((x)*(x))\nint i = 3;\nprintf(\"%d\", SQR(i++));", ["Undefined behaviour – i++ appears twice in one expression", "9", "16", "12"], 0,
     "Avoid side effects in macro arguments."),
    ("What is printed?\n#define DOUBLE(x) x + x\nprintf(\"%d\", 3 * DOUBLE(2));", ["8", "12", "10", "6"], 0, PYQ + "3 * 2 + 2 = 8 – the body needs parentheses."),
    ("Compared with a function, a macro", ["Has no call overhead and no type checking, but makes the code larger", "Is type-checked", "Is always slower",
                                           "Can call itself recursively"], 0, "Each use is expanded in place."),
    ("A long macro definition is continued on the next line with", ["A backslash (\\) at the end of the line", "A semicolon", "A comma", "#continue"], 0,
     "The newline after \\ is removed."),
    ("#ifdef DEBUG … #endif  compiles the enclosed code only if", ["DEBUG has been defined as a macro", "A variable DEBUG equals 1", "The program runs in debug mode",
                                                                   "DEBUG is a function"], 0, "#ifndef does the opposite."),
    ("#if needs an expression that is", ["An integer constant expression the preprocessor can evaluate", "Any C expression, variables included", "A string",
                                         "A floating-point value"], 0, "Variables do not exist yet at preprocessing time."),
    ("Which directive is NOT used for conditional compilation?", ["#include", "#elif", "#else", "#endif"], 0, "#if, #ifdef, #ifndef, #elif, #else, #endif."),
    ("Inside #if, defined(NAME) is", ["1 if NAME is a defined macro, otherwise 0", "The value of NAME", "An error", "A function call"], 0,
     "#if defined(A) || defined(B)."),
    ("What is printed?\n#define X 5\n#if X > 3\n  printf(\"big\");\n#else\n  printf(\"small\");\n#endif", ["big", "small", "bigsmall", "Compile error"], 0,
     "Only the #if branch is compiled."),
    ("#define A 10\n#undef A\nprintf(\"%d\", A);", ["A compile-time error – A is no longer defined", "10", "0", "Garbage"], 0, "#undef removes the macro."),
    ("What is printed?\n#define NAME KEA\nprintf(\"NAME\");", ["NAME", "KEA", "Nothing", "Compile error"], 0, PYQ + "Macros are not replaced inside string literals."),
    ("What is printed?\n#define A 2\n#define B A * 3\nprintf(\"%d\", B + 1);", ["7", "8", "9", "6"], 0, "B + 1 → 2 * 3 + 1."),
    ("With  #define SWAP(a, b) { int t = a; a = b; b = t; },  after  x = 1, y = 2;  SWAP(x, y);", ["x = 2, y = 1", "x = 1, y = 2", "x = 2, y = 2", "A compile-time error"], 0,
     "The block is expanded in place and works directly on x and y."),
    ("What is printed?\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\nprintf(\"%d\", MIN(4, 2 + 1));", ["3", "4", "2", "1"], 0, "((4) < (2 + 1) ? … ) → 3."),
    ("Conditional compilation is mainly used to", ["Build different versions (debug, platform-specific) from one source", "Speed up loops", "Allocate memory",
                                                   "Handle run-time errors"], 0, "E.g. #ifdef _WIN32."),
    ("Compiling with  gcc -DDEBUG prog.c", ["Defines the macro DEBUG, as if #define DEBUG were at the top", "Deletes DEBUG", "Runs the debugger", "Turns off warnings"], 0,
     "-D defines a macro from the command line."),
    ("By convention, macro names are written in", ["Upper case", "Lower case", "camelCase", "With a leading #"], 0, "So they stand out from variables."),
    ("What is printed?\n#define AREA(r) 3.14 * r * r\nprintf(\"%.2f\", AREA(1 + 1));", ["5.14", "12.56", "6.28", "4.14"], 0,
     PYQ + "3.14 * 1 + 1 * 1 + 1 = 5.14; write ((r) * (r))."),
    ("C99's alternative to function-like macros that keeps type checking is", ["inline functions", "typedef", "enum", "register"], 0, "static inline int sq(int x)."),
    ("Macro expansion happens", ["Before compilation, by textual substitution", "At run time", "During linking", "When the function is called"], 0,
     "The compiler never sees the macro names."),
]

FILE_MODES = [
    F[0], F[1], F[2], F[3], F[7], F[23], F[25], F[29],
    ("A file pointer is declared as", ["FILE *fp;", "file *fp;", "FILE fp[];", "pointer FILE fp;"], 0, "FILE (upper case) is a structure type from <stdio.h>."),
    ("The correct call to open data.txt for reading is", ["fp = fopen(\"data.txt\", \"r\");", "fp = fopen(\"r\", \"data.txt\");", "fp = open(\"data.txt\");",
                                                         "fopen(fp, \"data.txt\", \"r\");"], 0, "File name first, then mode."),
    ("Opening a file that does not exist in \"r\" mode", ["Returns NULL", "Creates an empty file", "Creates the file and writes to it", "Deletes the directory"], 0,
     "\"w\" and \"a\" create the file."),
    ("The mode \"a\" opens a file for", ["Writing at its end, creating it if needed", "Reading from the start", "Writing after erasing it", "Reading and writing from the start"], 0,
     "Existing contents are kept."),
    ("The mode \"w+\" opens a file for", ["Reading and writing, after truncating it (or creating it)", "Appending", "Reading", "Writing without truncating"], 0,
     "\"r+\" reads and writes without truncating."),
    ("The mode \"a+\" opens a file for", ["Reading and appending", "Appending without reading", "Reading only from the end", "Writing after erasing it"], 0,
     "Writes always go to the end."),
    ("A binary file is opened by adding which letter to the mode?", ["b, e.g. \"rb\" or \"wb\"", "t", "x", "bin"], 0, "Without b the file is opened in text mode."),
    ("The int 12345 written with fprintf (text) takes ___ bytes; written with fwrite (binary, 4-byte int) it takes ___", ["5 and 4", "4 and 5", "2 and 4", "5 and 5"], 0,
     PYQ + "Text stores each digit as a character; binary stores the raw bytes."),
    ("EOF is a macro whose value is usually", ["−1", "0", "26", "'\\0'"], 0, "That is why getc's result is stored in an int."),
    ("Which pair reads and writes one character at a time?", ["fgetc() / fputc()", "fread() / fwrite()", "fscanf() / fprintf()", "fgets() / fputs()"], 0,
     "getc/putc are the macro versions."),
    ("fgets(buf, 80, fp) reads", ["At most 79 characters, stopping after a newline, and adds '\\0'", "Exactly 80 characters", "One word", "The whole file"], 0,
     "It returns NULL at end of file."),
    ("fprintf(fp, \"%d %s\\n\", roll, name);", ["Writes formatted text to the file fp", "Prints on the screen", "Reads from the file", "Writes binary data"], 0,
     "fscanf reads formatted text."),
    ("fwrite(&s, sizeof(s), 1, fp) writes", ["One structure s as raw bytes", "sizeof(s) structures", "The address of s", "One character"], 0,
     "fread(&s, sizeof(s), 1, fp) reads it back."),
    ("fwrite() returns", ["The number of items (not bytes) written", "The number of bytes written", "0 on success", "The file pointer"], 0,
     "Less than requested means an error."),
    ("The loop  while ((ch = fgetc(src)) != EOF) fputc(ch, dst);", ["Copies src to dst character by character", "Deletes src", "Counts lines", "Reads one line"], 0,
     "ch must be an int."),
    ("To count the lines of a text file read with fgetc, a program counts", ["The '\\n' characters", "The spaces", "The EOF markers", "The '\\0' characters"], 0,
     "Add one if the last line has no newline."),
    ("The standard C function that deletes a file is", ["remove()", "delete()", "erase()", "destroy()"], 0, "rename(old, new) renames a file."),
    ("fopen(name, \"r+\") returns NULL when", ["The file does not exist", "The file is empty", "The file is small", "The file contains text"], 0, "\"r+\" never creates a file."),
    ("Why do programs check  if (fp == NULL)  after fopen?", ["The file may not have opened – missing file, no permission, etc.", "To close it", "To rewind it", "To flush it"], 0,
     PYQ + "Using a NULL FILE pointer crashes the program."),
    ("A binary file written with fwrite is", ["Not human-readable in a text editor, but compact and exact", "Plain text", "Always smaller than 1 KB",
                                              "Readable by fscanf alone"], 0, "Floats keep their exact bits."),
    ("Which function writes formatted output to a file?", ["fprintf()", "printf()", "sprintf()", "fputc()"], 0, "sprintf writes to a string."),
    ("fflush(fp) on an output stream", ["Writes any buffered data to the file immediately", "Erases the file", "Closes the file", "Moves to the start"], 0,
     "fclose also flushes."),
]

FILE_OPS_ARGS = [
    F[4], F[5], F[6], F[8], F[9], F[10], F[22], F[24], F[28],
    ("Low-level file I/O in C (UNIX) uses", ["open(), read(), write() and close() with integer file descriptors", "fopen() and fclose() with FILE pointers",
                                             "printf() and scanf()", "Buffered streams"], 0, PYQ + "These are system calls (<fcntl.h>, <unistd.h>)."),
    ("In low-level I/O, file descriptors 0, 1 and 2 are", ["Standard input, standard output and standard error", "Three files opened by the program",
                                                            "Reserved for the printer", "Invalid descriptors"], 0, "open() returns the lowest free descriptor (3, 4, …)."),
    ("Compared with low-level I/O, high-level (stream) I/O", ["Is buffered and portable, using FILE pointers", "Is unbuffered", "Works on UNIX alone",
                                                              "Uses file descriptors"], 0, "fopen, fread, fprintf … are standard C."),
    ("In  open(\"a.txt\", O_WRONLY | O_CREAT, 0644),  O_CREAT means", ["Create the file if it does not exist", "Close the file", "Open for reading", "Append"], 0,
     "0644 sets the permissions of a new file."),
    ("read(fd, buf, 100) returns 0 when", ["The end of file has been reached", "An error occurred", "100 bytes were read", "The file was created"], 0,
     "It returns −1 on error, otherwise the number of bytes read."),
    ("The low-level counterpart of fseek() is", ["lseek()", "seek()", "ftell()", "rewind()"], 0, "lseek(fd, offset, SEEK_SET)."),
    ("fseek(fp, 10, SEEK_CUR) moves the file position", ["10 bytes forward from the current position", "To byte 10 from the start", "10 bytes before the end",
                                                         "To the end"], 0, "SEEK_SET = start, SEEK_END = end."),
    ("fseek(fp, -5, SEEK_END) moves to", ["5 bytes before the end of the file", "Byte 5", "5 bytes after the current position", "The start"], 0, "Negative offsets move backwards."),
    ("To read the 4th record (each of size sizeof(rec)) of a binary file, seek to", ["3 * sizeof(rec) from SEEK_SET", "4 * sizeof(rec) from SEEK_SET",
                                                                                     "4 from SEEK_CUR", "sizeof(rec) from SEEK_END"], 0,
     PYQ + "Records are numbered from 0 in byte offsets: record k starts at (k − 1) × size."),
    ("ferror(fp) returns non-zero when", ["An error has occurred on the stream", "End of file is reached", "The file is empty", "The file is closed"], 0,
     "feof(fp) reports end of file."),
    ("The standard way for main to receive command line arguments is", ["int main(int argc, char *argv[])", "int main(char argv, int argc)", "void main(string args[])",
                                                                        "int main(int argc, int argv[])"], 0, "char **argv is equivalent."),
    ("For the command  copy a.txt b.txt,  argc and argv[1] are", ["3 and \"a.txt\"", "2 and \"a.txt\"", "3 and \"copy\"", "2 and \"b.txt\""], 0,
     PYQ + "argv[0] is the program name."),
    ("Run as  ./p red green,  the loop  for (i = 1; i < argc; i++) printf(\"%s \", argv[i]);  prints", ["red green", "./p red green", "red", "3"], 0,
     "i starts at 1 to skip the program name."),
    ("A program tests  if (argc != 3)  to make sure that", ["The user gave exactly two arguments after the program name", "Three files are open",
                                                           "The file has 3 lines", "main returns 3"], 0, "Then it prints a usage message and exits."),
    ("If the first argument is \"hello\", then *argv[1] is", ["'h'", "\"hello\"", "The program name", "1"], 0, "argv[1] points to the string; * gives its first character."),
    ("Command line arguments are supplied", ["When the program is started, by the user through the shell or IDE", "While the program runs, through scanf",
                                             "By the compiler", "By #define"], 0, "They are always strings."),
    ("argv[argc − 1] is", ["The last argument", "The program name", "NULL", "The first argument"], 0, "argv[argc] is NULL."),
    ("Running  ./p \"New Delhi\" 5  gives argc =", ["3", "4", "2", "5"], 0, "Quotes keep New Delhi as one argument."),
    ("Which sequence gives the size of a file in bytes?", ["fseek(fp, 0, SEEK_END); then ftell(fp)", "rewind(fp); then feof(fp)", "fgetc(fp) once",
                                                          "fclose(fp); then ftell(fp)"], 0, "ftell returns the current byte offset."),
    ("The low-level (UNIX) call that closes a file descriptor is", ["close(fd)", "fclose(fd)", "end(fd)", "free(fd)"], 0, "fclose takes a FILE *."),
    ("fopen, fread, fwrite, fprintf and fclose are called ___ file functions", ["High-level (stream, buffered)", "Low-level (system call)", "Kernel", "Assembly"], 0,
     "They are built on top of the low-level calls."),
]

TOPICS = {
    "C Preprocessor": [
        ("1 · Types of Preprocessor Directives and File Inclusion", DIRECTIVES),
        ("2 · Macros and Conditional Compilation", MACROS),
    ],
    "Files": [
        ("1 · File Operating Modes, Text and Binary Files", FILE_MODES),
        ("2 · High-level and Low-level File Operations and Command Line Arguments", FILE_OPS_ARGS),
    ],
}

NOTES = {
    "C Preprocessor": [{"title": "C preprocessor – revision sheet", "md": """## Directives (start with #, no semicolon, processed before compilation)
| Type | Directives |
|---|---|
| Macro substitution | `#define`, `#undef` |
| File inclusion | `#include <file.h>` (system dirs), `#include "file.h"` (current dir first) |
| Conditional compilation | `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`, `defined()` |
| Others | `#pragma`, `#error`, `#line` |
- Predefined: `__LINE__`, `__FILE__`, `__DATE__`, `__TIME__`, `__STDC__`
- Output of the preprocessor: .i file (gcc -E); comments removed; include guards `#ifndef X_H #define X_H … #endif` or `#pragma once`
- Headers: stdio.h (printf, FILE), stdlib.h (malloc, exit, atoi), string.h, math.h (sqrt, pow), ctype.h, conio.h (Turbo C only)

## Macros
- Object-like `#define PI 3.14`; function-like `#define SQ(x) ((x) * (x))`
- Pitfalls: `#define SQUARE(x) x * x` → SQUARE(2 + 3) = 11; `3 * DOUBLE(2)` with `x + x` = 8; `AREA(1 + 1)` with `3.14 * r * r` = 5.14
- `#define N 10;` puts the ; into the code; side effects (`SQR(i++)`) are evaluated twice
- `#x` stringizes, `a##b` pastes tokens; not replaced inside "strings"; continue lines with `\\`
- Macro vs function: no call overhead, no type checking, bigger code; C99 `inline` functions are the safe alternative
- `gcc -DDEBUG` defines DEBUG on the command line
"""}],
    "Files": [{"title": "Files – revision sheet", "md": """## Opening and modes
- `FILE *fp = fopen("data.txt", "r");` – check `fp == NULL`; `fclose(fp)` flushes and frees
| Mode | Meaning |
|---|---|
| "r" | read; NULL if missing |
| "w" | write; erase or create |
| "a" | append; create if missing |
| "r+" | read + write; must exist |
| "w+" | read + write; erase or create |
| "a+" | read + append |
- Add **b** for binary ("rb", "wb"); text mode may translate newlines (\\n ↔ \\r\\n on Windows)
- Text vs binary: 12345 → 5 characters vs 4 raw bytes
- Standard streams: stdin, stdout, stderr

## High-level (stream) functions – <stdio.h>
- Character: fgetc/getc, fputc/putc (store in int; EOF = −1); strings: fgets(buf, n, fp), fputs
- Formatted: fprintf, fscanf; blocks: fread/fwrite(&rec, sizeof rec, 1, fp) (return the item count)
- Position: fseek(fp, offset, SEEK_SET/SEEK_CUR/SEEK_END), ftell, rewind (= fseek(fp, 0, SEEK_SET)); feof, ferror, fflush, remove, rename
- Record k (1-based) starts at (k − 1) × sizeof(rec); file size: fseek to end, then ftell

## Low-level (UNIX system calls)
- open(name, O_RDONLY / O_WRONLY / O_RDWR | O_CREAT | O_APPEND, 0644) → int fd; read(fd, buf, n) (0 at EOF, −1 error); write; lseek; close
- fd 0, 1, 2 = stdin, stdout, stderr; unbuffered

## Command line arguments
- `int main(int argc, char *argv[])`; argv[0] = program name; argv[argc] = NULL
- `./prog one two` → argc = 3; quoted text is one argument; convert numbers with atoi/atof
"""}],
}
