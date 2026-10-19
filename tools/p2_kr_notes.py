"""P2 · KRIES – Additional Topics · revision NOTES for Basic Java and Computer Graphics (no new questions).
Owner's request (19 Oct 2026): notes for the remaining KRIES Paper 2 areas. Graphics numericals (DDA, Bresenham, midpoint
circle, frame-buffer size, outcodes, window–viewport mapping) were computed with a script on 19 Oct 2026; they match the
worked examples in Hearn & Baker (Computer Graphics, C version). Java outputs follow the Java Language Specification
(Java's evaluation order is defined left to right, unlike C)."""

TOPICS = {}  # notes only – question sets come from p2_kr_a

NOTES = {
    "Basic Java Programming": [{"title": "Basic Java – revision sheet with output tracing", "md": """## Java facts
- **James Gosling**, Sun Microsystems, 1995 (first called **Oak**); owned by **Oracle** since 2010
- "Write once, run anywhere": `javac Hello.java` → **bytecode** `Hello.class` → `java Hello` runs it on the **JVM** (interpreter + **JIT** compiler)
- **JDK** (tools: javac, java, javadoc, jar, jdb) ⊃ **JRE** (libraries + JVM) ⊃ **JVM**
- Features: simple, **object-oriented**, platform-independent, secure (no pointers, bytecode verifier, sandbox), robust (strong typing, exceptions, **garbage collection**), multithreaded, distributed, portable
- No pointers, no multiple inheritance of classes, no operator overloading, no global variables, no `goto` (reserved word)

## Program structure
```java
public class Hello {                          // file must be Hello.java
    public static void main(String[] args) {  // entry point
        System.out.println("Hello, KRIES");
    }
}
```

## Data types (sizes are fixed on every platform)
| Type | Size | Default (fields) |
|---|---|---|
| byte | 1 byte (−128 … 127) | 0 |
| short | 2 | 0 |
| int | 4 | 0 |
| long | 8 (`10L`) | 0L |
| float | 4 (`2.5f`) | 0.0f |
| double | 8 | 0.0 |
| **char** | **2 (Unicode)** | '\\u0000' |
| boolean | true/false (not 0/1) | false |
- Reference types default to **null**; **local variables have no default** – using one uninitialised is a compile error
- Widening is automatic (int → long → float → double); narrowing needs a cast: `(byte) 130` = **−126**

## Output tracing
| Code | Output | Why |
|---|---|---|
| `System.out.println(10 / 3 + " " + 10 % 3);` | 3 1 | integer division |
| `System.out.println(-10 % 3);` | -1 | sign of the left operand |
| `System.out.println(1 + 2 + "3");` | 33 | 1 + 2 = 3, then "3" + "3" |
| `System.out.println("1" + 2 + 3);` | 123 | string concatenation from the left |
| `System.out.println('A' + 1);` | 66 | char promoted to int |
| `System.out.println("" + 'A' + 1);` | A1 | |
| `char c = 'A'; c += 1; System.out.println(c);` | B | compound assignment casts back (`c = c + 1` is a compile error) |
| `int i = 5; int j = i++ + ++i;` | j = **12**, i = 7 | defined in Java: 5 + 7 (in C it is undefined) |
| `System.out.println(5.0 / 0);` | Infinity | `5 / 0` throws ArithmeticException |
| `System.out.println(Math.round(2.5) + " " + Math.round(-2.5));` | 3 -2 | floor(x + 0.5) |
| `String a = "hi", b = "hi"; a == b` | true | string pool (same literal) |
| `new String("hi") == "hi"` | false | different objects – use `.equals()` |
| `Integer x = 127, y = 127; x == y` | true | cached −128 … 127 (128 → false) |

## Classes and objects
- Access: **private** (class only) < **default** (package) < **protected** (package + subclasses) < **public**
- Constructor: same name, no return type; default constructor added only if none written; `this(...)` / `super(...)` must be the **first** statement
- `static` members belong to the class; a **static block** runs once when the class loads (before main); static methods can't use `this`
- `final` variable = constant; final method can't be overridden; final class can't be extended (String)
```java
class A { A() { System.out.print("A"); } }
class B extends A { B() { System.out.print("B"); } }
new B();                                   // AB  – superclass constructor first
class T { static int c = 0; T() { c++; } }
new T(); new T(); System.out.print(T.c);   // 2
```
- **Inheritance**: `class B extends A` (single only); **interfaces**: `class C implements I1, I2` (multiple); `abstract` classes can't be instantiated
- **Overriding** + dynamic dispatch: `A obj = new B(); obj.show();` calls B's show (methods are polymorphic, **fields are not**)
- Overloading = same name, different parameters (compile time)
- Packages: `java.lang` (imported automatically – String, Math, System, Thread), java.util (Scanner, ArrayList, HashMap), java.io, java.awt, javax.swing, java.sql, java.net

## Arrays and strings
- `int[] a = new int[5];` → all 0; `a.length` (field) vs `s.length()` (method); index out of range → ArrayIndexOutOfBoundsException
- String is **immutable**; **StringBuilder** (fast, not thread-safe) and **StringBuffer** (synchronized) are mutable
- Methods: length, charAt, substring(1, 3) (end excluded), indexOf, equals, equalsIgnoreCase, compareTo, toUpperCase, trim, split, replace, concat
- `"KRIES".substring(1, 3)` → "RI"; `"abc".compareTo("abd")` → −1

## Exceptions
- `Throwable` → **Error** (OutOfMemoryError – don't catch) and **Exception** → checked (IOException, SQLException, ClassNotFoundException – must be caught or declared with `throws`) and **unchecked** RuntimeException (ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException)
- `try` / `catch` (specific before general) / `finally` (always runs, except System.exit); `throw` an object, `throws` in a method header; custom exceptions extend Exception
```java
static int f() { try { return 1; } finally { System.out.print("F"); } }
System.out.print(f());                    // F1
```

## Multithreading
- Create: **extend Thread** or **implement Runnable** (preferred – the class can still extend another); call **start()** (calling run() directly runs in the same thread)
- States: new → runnable → running → blocked/waiting/timed-waiting → terminated
- `sleep(ms)`, `join()`, `yield()`, priorities 1–10 (NORM 5); `synchronized` methods/blocks for mutual exclusion; `wait()`, `notify()`, `notifyAll()` are methods of **Object**; deadlock possible

## Applets and JDBC
- Applet life cycle: **init() → start() → paint(Graphics g) → stop() → destroy()**; ran in browsers/appletviewer; no main(); **deprecated** (removed in modern JDKs) – still asked in exams
- **JDBC** steps: load driver (`Class.forName(...)`) → `DriverManager.getConnection(url, user, pwd)` → `createStatement()` / `prepareStatement()` → `executeQuery()` (SELECT → **ResultSet**) or `executeUpdate()` (INSERT/UPDATE/DELETE → row count) → close
- Driver types: **1** JDBC-ODBC bridge, **2** native-API, **3** network protocol (middleware), **4** thin / pure Java (most used)

## Traps
- `main` must be `public static void main(String[] args)`
- `==` compares references for objects; `.equals()` compares contents
- Java has `>>>` (unsigned right shift) – C does not
- `char` is 2 bytes in Java (1 in C)"""}],

    "Computer Graphics": [{"title": "Computer graphics – revision sheet with worked algorithms", "md": """## Display devices
- **CRT**: electron gun → deflection → phosphor screen; persistence; refresh rate (60 Hz+)
- **Raster scan**: beam sweeps every line; picture in a **frame buffer** (refresh buffer); interlaced/non-interlaced; TV, monitors; jagged lines (aliasing)
- **Random scan (vector)**: draws lines directly; smooth lines; display file; no realistic shading
- Flat panels: LCD, LED, plasma; colour CRT – **shadow mask** (RGB dots) or beam penetration
- **Resolution** = pixels (1024 × 768); **aspect ratio** = width/height (4 : 3, 16 : 9)
- **Frame buffer size** = width × height × bits per pixel / 8
  - 1024 × 768 × 24-bit = 2,359,296 bytes = **2.25 MB**; 640 × 480 × 8-bit = **307,200 bytes**; 24 bits → 2²⁴ ≈ 16.7 million colours
- Input: light pen, digitiser, joystick, touch panel; graphics software: OpenGL, DirectX

## Line drawing
**DDA** (digital differential analyser): steps = max(|Δx|, |Δy|); add Δx/steps and Δy/steps each step, round
- (2, 3) → (10, 8): steps 8, x += 1, y += 0.625 → (2, 3) (3, 4) (4, 4) (5, 5) (6, 6) (7, 6) (8, 7) (9, 7) (10, 8)
- Uses floating point and rounding → slower

**Bresenham** (integers only), for 0 < slope < 1: p₀ = 2Δy − Δx; if p < 0 → (x + 1, y), p += 2Δy; else → (x + 1, y + 1), p += 2Δy − 2Δx
- (20, 10) → (30, 18): Δx = 10, Δy = 8, **p₀ = 6**; pixels (21, 11) (22, 12) (23, 12) (24, 13) (25, 14) (26, 15) (27, 16) (28, 16) (29, 17) (30, 18)

## Circles, ellipses, curves
- **Midpoint circle**: start (0, r), p₀ = 1 − r; if p < 0 → (x + 1, y), p += 2x + 1; else → (x + 1, y − 1), p += 2(x − y) + 1 (with the new x, y); compute one **octant**, mirror to 8 (8-way symmetry)
  - r = 10: (0, 10) (1, 10) (2, 10) (3, 10) (4, 9) (5, 9) (6, 8) (7, 7)
- Ellipse: midpoint algorithm with 4-way symmetry, two regions
- **Bezier curve**: n + 1 control points → degree n; passes through the **first and last** points; inside the **convex hull**; global control (moving one point changes the whole curve); Bernstein polynomials
- **B-spline**: **local control**, degree independent of the number of points

## Filling
- **Scan-line** polygon fill (edge table, active edge list, fill between pairs of intersections)
- **Boundary fill** – fill until the boundary colour; **flood fill** – replace one interior colour; **4-connected** (up/down/left/right) vs **8-connected** (+ diagonals); recursive versions use a stack
- Inside test: odd–even (crossing) rule, non-zero winding rule

## 2-D transformations (homogeneous coordinates, 3 × 3 matrices)
| Transform | Result for (x, y) |
|---|---|
| Translation (tx, ty) | (x + tx, y + ty) |
| Scaling (sx, sy) about origin | (sx·x, sy·y) → (2, 3) with sx = 2, sy = 0.5 → (4, 1.5) |
| Rotation θ (anticlockwise) about origin | (x cos θ − y sin θ, x sin θ + y cos θ) → (4, 3) by 90° → **(−3, 4)** |
| Reflection about x-axis / y-axis / origin / y = x | (x, −y) / (−x, y) / (−x, −y) / (y, x) |
| Shear in x | (x + shx·y, y) |
- **Composite** transforms multiply matrices (order matters – not commutative); rotation/scaling about a fixed point (xp, yp) = T(xp, yp) · R(θ) · T(−xp, −yp)
- Homogeneous coordinates let translation be a matrix multiplication too

## Windowing and clipping
- **Window** = area of the world selected (world coordinates); **viewport** = area on the screen (device coordinates)
- Mapping: xv = xvmin + (xw − xwmin) · sx, sx = (xvmax − xvmin)/(xwmax − xwmin) (same for y)
  - Window (10, 10)–(110, 60) → viewport (0, 0)–(200, 100): sx = sy = 2 → point (60, 35) maps to **(100, 50)**
- **Cohen–Sutherland** line clipping: 4-bit **outcode TBRL** (top, bottom, right, left); window (0, 0)–(10, 10): (12, −3) → **0110**, (−2, 15) → **1001**; both codes 0000 → accept; codes AND ≠ 0 → reject; else clip
- **Liang–Barsky** (parametric, faster), Cyrus–Beck; **Sutherland–Hodgman** polygon clipping (clip against each edge in turn), Weiler–Atherton (concave polygons)

## Colour models
| Model | Type | Use |
|---|---|---|
| **RGB** | additive (light): R + G + B = white | monitors |
| **CMY(K)** | subtractive (ink): C = 1 − R … | printers |
| **HSV / HSB** | hue, saturation, value | user colour pickers |
| YIQ | luminance + chrominance | NTSC TV |

## Projections (3-D → 2-D)
- **Parallel**: projectors parallel; **orthographic** (perpendicular to the plane – front/top/side views, isometric) and **oblique** (cavalier, cabinet); preserves relative proportions
- **Perspective**: projectors meet at the centre of projection; distant objects look smaller (**foreshortening**); 1-, 2-, 3-point perspective by **vanishing points**
- 3-D: back-face removal, **z-buffer (depth buffer)** hidden-surface method, ray tracing; shading – flat, Gouraud (interpolate intensities), Phong (interpolate normals)

## Traps
- Bresenham uses only **integer** arithmetic; DDA uses floating point
- Circle has **8**-way symmetry, ellipse **4**-way
- Bezier curves pass through only the end control points
- RGB is additive, CMY subtractive"""}],
}
