"""P2 · Unit 4 – Programming Languages & Web · revision NOTES for the six topics that had none (no new questions).
Owner's request (19 Oct 2026): "continue CS notes, detailed". Web Programming is in the KRIES syllabus (Internet Technology);
language design, data types and C are GPSTR Unit 4. Facts follow Pratt & Zelkowitz (Programming Languages – Design and
Implementation), the HTML Living Standard / CSS specs and ECMAScript."""

TOPICS = {}  # notes only – question sets come from p2u4_a … p2u4_e

NOTES = {
    "Web Programming – HTML, DHTML, CSS": [{"title": "HTML, DHTML and CSS – detailed notes", "md": """## HTML basics
- **HyperText Markup Language** – Tim Berners-Lee (1991); current standard = **HTML5 / HTML Living Standard** (WHATWG); a **markup** language, not a programming language; tags are case-insensitive
- Element = start tag + content + end tag: `<p>Hello</p>`; **empty (void) elements** have no end tag: `<br>`, `<hr>`, `<img>`, `<input>`, `<meta>`, `<link>`
- Attributes go in the start tag: `<a href="x.html" title="Go">`; global attributes: id (unique), class, style, title, lang, hidden

## Document structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KRIES notes</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Heading</h1>
  <p>Paragraph</p>
</body>
</html>
```
- `<head>` = information about the page (title shown on the tab, meta, links, scripts); `<body>` = visible content
- HTML5 semantic elements: `<header> <nav> <main> <section> <article> <aside> <footer> <figure>`; media: `<audio> <video> <canvas> <svg>`

## Text formatting
| Tag | Effect |
|---|---|
| `<h1>` … `<h6>` | headings (h1 largest) |
| `<p>`, `<br>`, `<hr>` | paragraph, line break, horizontal rule |
| `<b>` / `<strong>` | bold / important |
| `<i>` / `<em>` | italic / emphasis |
| `<u>`, `<s>`, `<mark>` | underline, strike, highlight |
| `<sub>`, `<sup>` | H<sub>2</sub>O, x<sup>2</sup> |
| `<pre>` | preformatted (keeps spaces) |
| `<blockquote>`, `<q>`, `<code>`, `<abbr>` | quotations, code, abbreviation |
| `<font>`, `<center>` | **obsolete** (use CSS) |
- Entities: `&lt;` <, `&gt;` >, `&amp;` &, `&nbsp;` non-breaking space, `&copy;` ©

## Links and images
- `<a href="https://kea.kar.nic.in" target="_blank">KEA</a>`; `target="_blank"` opens a new tab; `href="#top"` jumps to `id="top"`; `mailto:` and `tel:` links
- `<img src="logo.png" alt="KEA logo" width="100" height="80">` – **alt** text is shown if the image fails and is read by screen readers
- Absolute URL (full address) vs relative URL (`images/a.png`)

## Lists
- **Ordered** `<ol>` (type="1", "A", "a", "I", "i"; start="5"), **unordered** `<ul>` (disc, circle, square), items `<li>`
- **Description/definition list** `<dl>` with `<dt>` (term) and `<dd>` (description)
- Lists can be nested

## Tables
```html
<table border="1">
  <caption>Marks</caption>
  <tr><th>Name</th><th>Marks</th></tr>
  <tr><td>Asha</td><td>92</td></tr>
  <tr><td colspan="2">Total: 1 student</td></tr>
</table>
```
- `<tr>` row, `<th>` header cell (bold, centred), `<td>` data cell; **colspan** merges columns, **rowspan** merges rows; `<thead> <tbody> <tfoot>`; old attributes cellpadding, cellspacing

## Forms
```html
<form action="/submit" method="post">
  <label for="n">Name</label> <input type="text" id="n" name="name" required>
  <input type="password" name="pwd">
  <input type="radio" name="g" value="M"> <input type="checkbox" name="agree">
  <select name="city"><option>Mysuru</option><option>Kalaburagi</option></select>
  <textarea name="addr" rows="3" cols="30"></textarea>
  <input type="submit" value="Send"> <input type="reset">
</form>
```
- **GET** – data in the URL (visible, limited length, bookmarkable); **POST** – data in the request body (for passwords, large data)
- Input types: text, password, email, number, date, range, color, file, hidden, radio (one of a group – same name), checkbox (many), submit, reset, button
- Attributes: name (key sent to the server), value, placeholder, required, maxlength, readonly, disabled, pattern

## DHTML (Dynamic HTML)
Not a language – the **combination of HTML + CSS + JavaScript + DOM** to change a page after it loads without reloading (hover effects, show/hide menus, moving elements, form validation). Microsoft and Netscape versions in the late 1990s; now just "modern web pages".

## CSS (Cascading Style Sheets)
- Håkon Wium Lie (1994), W3C; separates **presentation from content**
- Syntax: `selector { property: value; }` → `p { color: blue; font-size: 16px; }`
- Three ways: **inline** (`style="color:red"`), **internal** (`<style>` in head), **external** (`<link rel="stylesheet" href="a.css">` – best for many pages)
- **Cascade priority**: inline > internal/external (the later rule wins when equally specific) > browser default; `!important` overrides
- **Specificity**: inline (1000) > id `#x` (100) > class `.x` / attribute / pseudo-class (10) > element `p` (1)
- Selectors: `*`, `p`, `.note`, `#main`, `div p` (descendant), `div > p` (child), `h1, h2` (group), `a:hover`, `li:first-child`, `p::first-line`, `[type="text"]`
- **Box model**: content → padding → border → margin; width excludes padding/border unless `box-sizing: border-box`
  - width 200 + padding 10 each side + border 2 each side → total **224 px** wide (content-box)
- Units: px, %, **em** (relative to parent font size), **rem** (root font size), vh/vw
- Common properties: color, background-color, font-family, font-size, font-weight, text-align, margin, padding, border, width, height, display (block, inline, inline-block, none, flex, grid), position (static, relative, absolute, fixed, sticky), float, z-index, visibility
- `display: none` removes the element; `visibility: hidden` hides it but keeps its space
- Responsive design: media queries `@media (max-width: 600px) { … }`, flexbox, grid

## Traps
- `<br>` and `<img>` have no closing tag
- `id` must be unique; `class` can repeat
- Inline CSS has the highest priority (except `!important`)
- `<th>` is a header cell, `<thead>` a header row group"""}],

    "Web Programming – XML, Scripting, JavaScript": [{"title": "XML and JavaScript – detailed notes", "md": """## XML (eXtensible Markup Language)
- W3C 1998; designed to **store and transport data** (HTML displays data); tags are **user-defined**; self-descriptive; platform independent
- **Well-formed** rules: one root element; every start tag closed; properly nested; **case-sensitive**; attribute values in quotes; special characters escaped (`&lt;`)
- **Valid** = well-formed + follows a **DTD** or **XML Schema (XSD)**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<students>
  <student roll="1"><name>Asha</name><marks>92</marks></student>
</students>
```
- DTD: `<!ELEMENT student (name, marks)>`, `<!ATTLIST student roll CDATA #REQUIRED>`; XSD is written in XML and supports data types
- Related: **XSLT** (transform XML to HTML), **XPath** (navigate: `/students/student[1]/name`), XQuery, namespaces, CDATA sections; parsers – **DOM** (whole tree in memory) and **SAX** (event-based, streaming)
- Uses: config files, RSS feeds, SOAP web services, Office files (.docx is zipped XML), SVG; JSON is the lighter alternative

| HTML | XML |
|---|---|
| predefined tags | user-defined tags |
| displays data | carries data |
| not case-sensitive | case-sensitive |
| some tags may stay unclosed | every tag must close |

## Scripting
- **Client-side** scripts run in the browser (JavaScript) – validation, interactivity; **server-side** scripts run on the server (PHP, JSP, ASP.NET, Python, Node.js) – database access, generating pages
- Scripting languages are usually interpreted and dynamically typed (JavaScript, Python, Perl, VBScript – old IE)

## JavaScript fundamentals
- **Brendan Eich**, Netscape, **1995** (written in 10 days); standard **ECMAScript** (ES6 = 2015); not related to Java; runs in browsers and in Node.js
- Include: `<script> … </script>` inline or `<script src="app.js"></script>` (usually at the end of body or with `defer`)
- Output: `document.write()`, `alert()`, `console.log()`, `innerHTML`; input: `prompt()`, `confirm()` (returns true/false)
- Variables: `var` (function scope, hoisted), `let` (block scope), `const` (block scope, cannot be reassigned)
- Types: **number** (one type for int and float), string, boolean, **undefined**, **null**, object, symbol, bigint; `typeof null` = "object" (a famous bug); `typeof NaN` = "number"
- Operators: `==` (loose, converts types) vs **`===`** (strict, no conversion); `5 == "5"` true, `5 === "5"` false
- Type coercion traces: `"5" + 2` → "52"; `"5" - 2` → 3; `"5" * "2"` → 10; `true + 1` → 2; `1 + 2 + "3"` → "33"; `"3" + 1 + 2` → "312"; `0.1 + 0.2 === 0.3` → false
- Control: if/else, switch, for, while, do-while, `for…in` (keys), `for…of` (values), break, continue

## Functions
```javascript
function add(a, b) { return a + b; }          // declaration (hoisted)
const mul = function (a, b) { return a * b; }; // expression
const sq = x => x * x;                         // arrow function (ES6)
add(2, 3);   // 5
add(2);      // NaN (b is undefined)
```
- Functions are first-class objects (can be passed, returned); closures remember outer variables; callbacks; default parameters `function f(a, b = 1)`

## Objects and arrays
```javascript
let s = { name: "Asha", marks: 92, show() { return this.name; } };
s.marks;  s["name"];  s.show();
let a = [10, 20, 30];
a.length;          // 3
a.push(40);        // add at end
a.pop();           // remove from end
a.map(x => x * 2); // [20, 40, 60]
a.filter(x => x > 15); // [20, 30]
a.join("-");       // "10-20-30"
```
- Built-in objects: String (length, toUpperCase, substring, indexOf, split), Math (random, round, floor, max), Date, Array, JSON (`JSON.stringify`, `JSON.parse`), RegExp
- Classes (ES6): `class A { constructor(x) { this.x = x; } }`, `extends`; prototype-based inheritance underneath

## DOM (Document Object Model)
- The page as a **tree of objects**; root = `document`
- Find: `document.getElementById("id")`, `getElementsByClassName`, `getElementsByTagName`, `querySelector(".c")`, `querySelectorAll("p")`
- Change: `el.innerHTML = "<b>Hi</b>"`, `el.textContent`, `el.style.color = "red"`, `el.setAttribute("src", "a.png")`, `el.classList.add("on")`
- Create/remove: `document.createElement("li")`, `parent.appendChild(li)`, `el.remove()`
- BOM (browser object model): `window`, `location`, `history`, `navigator`, `screen`

## Events
- `onclick`, `ondblclick`, `onmouseover`, `onmouseout`, `onkeydown`, `onkeyup`, `onchange`, `onsubmit`, `onload`, `onfocus`, `onblur`, `oninput`
```html
<button onclick="greet()">Hi</button>
<script>
  function greet() { alert("Welcome to KRIES"); }
  document.getElementById("f").addEventListener("submit", e => {
    if (document.getElementById("age").value < 18) { e.preventDefault(); alert("Too young"); }
  });
</script>
```
- `addEventListener` allows several handlers; event bubbling (inner → outer) and capturing; `event.preventDefault()`, `event.stopPropagation()`
- Form validation before submit is a classic client-side task
- AJAX / `fetch()` loads data without reloading the page; timers `setTimeout`, `setInterval`

## Traps
- JavaScript ≠ Java
- `===` checks value **and** type
- XML is case-sensitive and every tag must close
- `getElementById` returns one element; `getElementsByClassName` returns a collection"""}],

    "Language Design and Translation Issues": [{"title": "Language design and translation – detailed notes", "md": """## Why study language concepts
Better choice of language, easier learning of new ones, better use of features, understanding implementation costs.

## Qualities of a good language
**Readability**, **writability**, **reliability** (type checking, exception handling, no aliasing surprises), cost (training, compiling, execution, maintenance), **orthogonality** (a small set of features combine freely), simplicity, abstraction support, portability, efficiency.

## Paradigms
| Paradigm | Idea | Languages |
|---|---|---|
| **Imperative / procedural** | statements change state, step by step | C, Pascal, FORTRAN, COBOL |
| **Object-oriented** | objects, classes, inheritance | C++, Java, Smalltalk, C# |
| **Functional (applicative)** | functions and expressions, no side effects, recursion | LISP, Haskell, ML, Scheme |
| **Logic (declarative)** | facts and rules, the system infers | **Prolog** |
| Scripting | glue, interpreted | Perl, Python, JavaScript |
| Concurrent / parallel | processes, threads | Ada, Go, Erlang |
- Declarative = say **what**, not how (SQL, Prolog, HTML)

## History milestones
FORTRAN (1957, Backus – scientific) · LISP (1958, McCarthy – AI) · ALGOL 60 (block structure, BNF) · COBOL (1959, Grace Hopper – business) · BASIC (1964) · Pascal (1970, Wirth – teaching) · C (1972) · Smalltalk (1972–80) · Prolog (1972) · Ada (1983, US DoD) · C++ (1983) · Python (1991) · Java (1995) · JavaScript (1995) · C# (2000)

## Models of computation / implementation
- **Compilation** (translate whole program to machine code – fast execution), **pure interpretation** (execute source directly – easy debugging, slow), **hybrid** (compile to intermediate code then interpret – Java bytecode, Python .pyc), **JIT** compilation
- Virtual computer: the language implementation builds a "virtual machine" on top of the real one
- Binding times: language design time (meaning of `*`), language implementation time (size of int), **compile time** (type of a variable in C), link time, load time, **run time** (value of a variable; type in Python). Early binding = efficiency; late binding = flexibility

## Programming environments
Editors, compilers, debuggers, IDEs (Eclipse, Visual Studio, VS Code), version control, test frameworks, profilers

## Syntax and semantics
- **Syntax** = form (grammar); **semantics** = meaning; pragmatics = use
- Lexemes (lowest units, e.g. `sum`, `=`) grouped into **tokens** (identifier, assignment operator)
- **BNF** (Backus–Naur Form) and **EBNF** describe syntax: `<expr> ::= <expr> + <term> | <term>`; `[ ]` optional, `{ }` repetition in EBNF; syntax diagrams
- **Parse tree**; a grammar is **ambiguous** if a sentence has two parse trees (classic: dangling else, `a + b * c` without precedence)
- Precedence and associativity are encoded in the grammar (left recursion → left associativity)
- Semantics: operational, denotational, axiomatic; attribute grammars add static semantics (type rules)

## Stages in translation
**Lexical analysis** (scanner, tokens, removes comments/white space) → **syntax analysis** (parser, parse tree; top-down LL / recursive descent, bottom-up LR / shift-reduce) → **semantic analysis** (type checking, symbol table) → **intermediate code** (three-address code, postfix, syntax trees) → **optimisation** → **code generation**; plus linking and loading
- Example three-address code for `a = b * c + d`: `t1 = b * c; t2 = t1 + d; a = t2`

## Formal transition models
- **Finite automata** (DFA/NFA) recognise **regular languages** → used by **lexical analysers**; regular expressions describe tokens (identifier = letter (letter | digit)*)
- **Pushdown automata** (FA + stack) recognise **context-free languages** → used by **parsers**
- **Chomsky hierarchy**: type 3 regular (FA) ⊂ type 2 context-free (PDA) ⊂ type 1 context-sensitive (linear bounded automaton) ⊂ type 0 recursively enumerable (**Turing machine**)
- Every NFA has an equivalent DFA (subset construction, up to 2ⁿ states)

## Traps
- Prolog = logic paradigm; LISP = functional; SQL = declarative
- Lexical analysis uses finite automata; parsing uses pushdown automata
- Type of a variable in C is bound at compile time; in Python at run time
- An ambiguous grammar has more than one parse tree (or leftmost derivation) for some sentence"""}],

    "Elementary Data Types": [{"title": "Elementary data types – detailed notes", "md": """## Data objects, variables, constants
- **Data object** = a run-time container of data values (a location); attributes – type, value, name, lifetime, location
- **Variable** – a data object whose value can change; **constant** – fixed value (literal or named, e.g. `const`)
- **Lifetime** (when it exists in memory) vs **scope** (where its name can be used)
- **l-value** (address/location) vs **r-value** (stored value): in `x = x + 1`, the left x is used as an l-value, the right x as an r-value

## Data types
- A **type** = a set of values + a set of operations on them
- **Specification** (attributes, values, operations – what the user sees) vs **implementation** (storage representation, how operations are carried out)
- Operations described by a **signature**: `+ : integer × integer → integer`
- Type checking: **static** (compile time – C, Java) vs **dynamic** (run time – Python, JavaScript); **strongly typed** (all type errors detected – Java, Ada) vs weakly typed (C allows many implicit conversions)
- **Type conversion**: implicit (**coercion** – int to float in `2 + 3.5`) vs explicit (**cast** `(int) 3.9`); widening (safe) vs narrowing (may lose data)
- Type equivalence: **name** equivalence (same type name) vs **structural** equivalence (same structure)

## Properties of types and objects
- Initialisation, assignment, storage representation (fixed size, descriptors for complex objects at run time)
- Declarations give the translator information: type, storage, names; they allow static checking and efficient storage

## Scalar (elementary) data types
| Type | Notes |
|---|---|
| **Integer** | fixed range (two's complement), exact; operations + − × ÷ mod; overflow possible |
| **Real / floating point** | IEEE 754 (sign, exponent, mantissa); approximate – avoid equality tests |
| **Fixed-point** | fixed number of decimal places (money, COBOL) |
| **Boolean** | true/false; 1 bit in theory, often 1 byte; and, or, not |
| **Character** | ASCII (7/8-bit), Unicode (UTF-8/16/32) |
| **Enumeration** | named values `enum colour {RED, GREEN}` – readable, type-safe |
| Subrange | `1..100` (Pascal, Ada) |
| Pointer | address; null; dangling/garbage problems |
- Scalar = a single value with no internal structure visible

## Composite (structured) data types
| Type | Notes |
|---|---|
| **Character strings** | fixed length, variable length with a maximum, unbounded (dynamic); operations – concatenation, comparison, substring, pattern matching |
| **Arrays** | homogeneous, indexed; static/dynamic; row-major (C) or column-major (Fortran) |
| **Records / structures** | heterogeneous fields accessed by name |
| **Unions / variant records** | one storage area, different interpretations |
| **Lists** | sequences (LISP), dynamic |
| **Sets** | membership, union, intersection (Pascal bit sets) |
| Files | persistent sequences |
| Pointers and programmer-constructed objects | linked structures on the heap |
- Composite objects usually need a **descriptor** (dope vector) holding type, bounds, size and location

## Traps
- Coercion is implicit conversion; casting is explicit
- Strings are composite, not scalar (in C they are char arrays)
- Strong typing is about detecting all type errors, not about declaring types"""}],

    "Programming in C – Part 1": [{"title": "Programming in C, part 1 – exam digest", "md": """The KRIES C topics carry full worked notes (P2 · KRIES – C Programming). This digest gathers the GPSTR Unit 4 points in one place.

## Tokens, identifiers and data types
- Tokens: keywords (32 in C89), identifiers, constants, string literals, operators, special symbols
- Identifiers: letters, digits, `_`; not starting with a digit; case-sensitive; not a keyword; first 31 characters significant (C89 external: 6)
- Basic types and sizes (64-bit GCC): char 1, short 2, int 4, long 8, float 4, double 8; modifiers signed, unsigned, short, long; void
- Qualifiers: `const` (read-only), `volatile` (may change outside the program – don't optimise away)
- Constants: integer (decimal, **octal** with leading 0, hex 0x), floating (3.0, 1e-3), character ('a', '\\n'), string ("abc")

## Sequence control – operators, expressions, statements
- Precedence (high → low): postfix, unary, `* / %`, `+ -`, shifts, relational, equality, `&`, `^`, `|`, `&&`, `||`, `?:`, assignment, comma
- Integer division truncates; `%` only on integers; mixed expressions promote to the wider type
- Short-circuit `&&` / `||`; relational/logical results are 1 or 0
- Statements: expression, compound `{ }`, selection (if, switch), iteration (while, do-while, for), jump (break, continue, goto, return)
- **Sequence points**: `;`, `&&`, `||`, `?:`, comma operator – modifying a variable twice between two sequence points (`i = i++`) is **undefined**
- Worked: `int a = 10, b = 3; printf("%d %d %.2f", a / b, a % b, (float) a / b);` → `3 1 3.33`

## Subprogram control and functions
- Function = return type, name, parameters, body; prototypes let the compiler check calls
- Parameter passing: by value only (addresses passed by value give "reference" behaviour)
- **Activation record** (stack frame): parameters, return address, saved registers, local variables; created on call, removed on return → recursion works
- Scope rules: block scope, file scope, function prototype scope; **static scoping** (C) – a name refers to the nearest enclosing declaration in the program text
- Storage classes: auto (stack, garbage), register (no &), static (keeps value, default 0), extern (global across files)
- Recursion trace: `int f(int n) { return n < 2 ? n : f(n - 1) + f(n - 2); }` → f(6) = 8

## Arrays, structures, unions and strings
- Arrays: contiguous; `a[i]` = `*(a + i)`; 2-D row-major; passed to functions as pointers
- Structures: heterogeneous; `.` and `->`; padding makes `sizeof` ≥ sum of members; structures can be assigned, not compared
- Unions: shared memory, size = largest member; one active member
- Strings: char arrays ending in `'\\0'`; `<string.h>` – strlen, strcpy, strcat, strcmp, strchr, strstr
- Worked: `char s[] = "GPSTR"; printf("%zu %zu %c", sizeof s, strlen(s), s[strlen(s) - 1]);` → `6 5 R`

## Traps
- `sizeof` is evaluated at compile time (except for VLAs) and does not evaluate its operand
- An array name is not a modifiable lvalue
- `char c = 'A' + 2;` → 'C'"""}],

    "Programming in C – Part 2": [{"title": "Programming in C, part 2 – exam digest", "md": """## Pointers
- `&` address-of, `*` dereference; pointer arithmetic scales by the pointed type size
- Pointers and arrays: `a[i]` = `*(a + i)`; difference of pointers = number of elements
- `int *p[5]` array of pointers · `int (*p)[5]` pointer to array · `int *f()` function returning pointer · `int (*f)()` pointer to function · `int **pp` pointer to pointer
- `const int *p` (data const) vs `int *const p` (pointer const)
- Dynamic memory: malloc (garbage), calloc (zeroed), realloc, free; leaks and dangling pointers
- `void *` is generic (cast before use); NULL pointer; wild pointer (uninitialised)
- Worked: `int a[] = {1, 2, 3, 4}, *p = a + 1; printf("%d %d %ld", *p, p[2], (a + 3) - p);` → `2 4 2`

## File handling
- `FILE *fp = fopen(name, mode)`; modes r, w, a, r+, w+, a+ (+ b for binary); NULL on failure
- Character: fgetc/fputc; line: fgets/fputs; formatted: fscanf/fprintf; block: fread/fwrite
- Random access: fseek(fp, offset, SEEK_SET | SEEK_CUR | SEEK_END), ftell, rewind
- feof becomes true only after a read fails; fclose flushes buffers
- Standard streams stdin, stdout, stderr; low-level I/O: open/read/write/close with file descriptors (UNIX)

## Command-line arguments
- `int main(int argc, char *argv[])`; argc counts the program name; argv[0] = program name; convert with atoi/atof
- Worked: `./prog 10 20` → argc 3; `atoi(argv[1]) * atoi(argv[2])` = 200

## Preprocessor
- `#include <…>` (system) vs `"…"` (local first); `#define` object-like and function-like macros (bracket everything); `#undef`
- Conditional compilation: `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`; include guards
- `#` stringising, `##` token pasting; predefined `__FILE__`, `__LINE__`, `__DATE__`, `__TIME__`, `__STDC__`
- Worked: `#define MUL(a, b) a * b` → `MUL(2 + 3, 4)` = 2 + 3 * 4 = **14**; with brackets `((a) * (b))` = 20

## Traps
- `fopen` with "w" erases an existing file
- Macros are expanded before compilation – no type checking
- `free(p)` does not set p to NULL"""}],
}
