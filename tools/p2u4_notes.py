"""P2 · Unit 4 – Programming Languages & Web · revision NOTES for Object Oriented Programming and C++ (no new questions).
Owner's request (19 Oct 2026): more notes for KRIES – 'OOPS using C++' is named in the KRIES Paper 2 syllabus. Output traces use
standard C++ (g++, 64-bit: int 4 bytes, pointer 8 bytes)."""

TOPICS = {}  # notes only – question sets come from p2u4_a … p2u4_e

NOTES = {
    "Object Oriented Programming": [{"title": "Object-oriented programming – revision sheet", "md": """## Procedural vs object-oriented
| Procedure-oriented (C) | Object-oriented (C++, Java) |
|---|---|
| program = functions | program = objects |
| top-down design | **bottom-up** design |
| data moves freely between functions (global data) | data hidden inside objects |
| hard to extend | reuse through inheritance |

## Core concepts
- **Class** – blueprint/user-defined type (data members + member functions); **object** – an instance (memory is allocated per object); **instantiation** – creating an object
- **Encapsulation** – binding data and functions together; **data hiding** with access specifiers (private, protected, public)
- **Abstraction** – showing essentials, hiding details (abstract classes, interfaces)
- **Inheritance** – a new class reuses an existing one ("is-a"): single, multiple, multilevel, hierarchical, hybrid
- **Polymorphism** – one name, many forms
  - **Compile-time / static**: function overloading, operator overloading, templates (early binding)
  - **Run-time / dynamic**: virtual functions + overriding (late binding through a base pointer/reference)
- **Dynamic binding** – the code to call is chosen at run time; **message passing** – objects call each other's methods
- Composition / aggregation = "has-a" (a Car has an Engine); association; **coupling** (low is good) and **cohesion** (high is good)

## History
**Simula 67** – first OO language (classes, objects); **Smalltalk** (Alan Kay) – pure OO; **C++** – Bjarne Stroustrup, Bell Labs, "C with Classes" (1979), renamed C++ in 1983; Java – James Gosling, Sun (1995); Python, C# also OO

## Abstract classes and interfaces
- Abstract class: cannot be instantiated; has at least one abstract (pure virtual) method; may hold data and concrete methods
- Interface (Java): only method signatures (plus default/static methods since Java 8); a class can implement many interfaces → Java's answer to multiple inheritance

## Overloading vs overriding
| Overloading | Overriding |
|---|---|
| same name, **different parameters** | same signature in **derived** class |
| same class (or scope) | base and derived classes |
| compile-time | run-time (needs virtual in C++) |
| return type alone can't differ | return type same (or covariant) |

## SOLID principles (design)
Single responsibility, Open/closed (open for extension, closed for modification), Liskov substitution, Interface segregation, Dependency inversion

## Traps
- Encapsulation ≠ abstraction (bundling vs hiding complexity)
- Overloading is static polymorphism; overriding with virtual is dynamic
- Abstract classes can have constructors (called by derived classes) but no objects of their own
- C++ is not purely object-oriented (main and global functions exist); Smalltalk is"""}],

    "Programming in C++ – Part 1": [{"title": "C++ basics, functions, classes and constructors – revision sheet", "md": """## C++ additions over C
`cin >>` / `cout <<` (iostream), `//` comments, **references**, `new`/`delete`, `bool`, function overloading, default arguments, inline functions, namespaces (`using namespace std;`), `::` scope resolution, classes, templates, exceptions, `const` everywhere, `string` class

## Tokens and types
- Keywords added: class, public, private, protected, new, delete, this, virtual, friend, inline, namespace, template, throw, try, catch, operator, bool, true, false …
- `sizeof('a')` = **1** in C++ (it is 4 in C – the literal is an int there)
- Reference: `int x = 10; int &r = x; r++;` → x = **11**; a reference must be initialised and cannot be re-seated
- `::` gives access to a global variable hidden by a local: `int a = 5; int main() { int a = 3; cout << ::a; }` → **5**

## Functions
- **Default arguments** go from the right: `int add(int a, int b = 5, int c = 10);` → add(1) = **16**, add(1, 2) = **13**, add(1, 2, 3) = 6
- **Inline**: `inline int sq(int x) { return x * x; }` – a request to expand at the call site
- **Overloading**: same name, different number/type/order of parameters; `void f(int)`, `void f(double)` → `f('a')` calls **f(int)** (char → int promotion), `f(2.5f)` calls **f(double)**; differing only in return type is an error
- Parameter passing: by value, by **reference** (`void swap(int &a, int &b)` – no pointers needed), by pointer; `const T&` for big objects

## Classes and objects
```cpp
class Account {
    int balance;                 // private by default in a class
public:
    static int count;            // one copy shared by all objects
    Account(int b = 0) : balance(b) { count++; }
    int get() const { return balance; }
};
int Account::count = 0;          // static member defined outside
```
- `class` members are **private** by default; `struct` members **public**
- Member functions defined inside the class are implicitly inline; outside: `int Account::get() const { … }`
- **this** pointer points to the calling object (not available in static functions)
- **Static member function** can access only static members; called as `Account::count`
- `const` member function cannot change data members
- **Friend function**: not a member, but can access private members (declared with `friend` inside the class); friendship is not inherited or mutual
- Empty class: `sizeof` = **1**; size of an object = its non-static data (+ padding, + 8 for a vptr if it has virtual functions)

## Constructors and destructors
- Same name as the class, no return type; called automatically on creation; can be overloaded; can't be virtual
- Kinds: default, parameterised, **copy** (`X(const X &o)` – parameter **must** be a reference, else infinite recursion), move (C++11), conversion
- **Copy constructor runs** when: an object is initialised from another (`X b = a;` or `X b(a);`), passed **by value**, returned by value. `c = a;` (both already exist) calls the **assignment operator**, not the copy constructor
- Shallow copy (default, copies pointers) vs deep copy (allocates new memory)
- Initialiser list required for const members, references and base classes
- **Destructor** `~X()`: one per class, no arguments, no overloading, called in **reverse order of construction**
```cpp
class T { int id; public:
  T(int i) : id(i) { cout << "C" << id << " "; }
  ~T() { cout << "D" << id << " "; } };
int main() { T a(1), b(2); { T c(3); } }
```
Output: **C1 C2 C3 D3 D2 D1** (c dies at its closing brace; then b, then a)

## Dynamic memory
`int *p = new int(5); delete p;` · `int *a = new int[10]; delete[] a;` – new calls constructors, delete calls destructors (malloc/free don't)

## Traps
- `cout << 5 / 2;` → 2; `cout << 5 / 2.0;` → 2.5
- A constructor with all default arguments is also the default constructor
- Static data members must be defined outside the class (before C++17 inline variables)
- A friend function is called like a normal function (no object.)"""}],

    "Programming in C++ – Part 2": [{"title": "C++ overloading, inheritance, virtual functions, templates, exceptions, files – revision sheet", "md": """## Operator overloading
```cpp
class Complex { public: double re, im;
  Complex(double r = 0, double i = 0) : re(r), im(i) {}
  Complex operator+(const Complex &o) const { return Complex(re + o.re, im + o.im); }
  friend ostream& operator<<(ostream &os, const Complex &c) { return os << c.re << "+" << c.im << "i"; }
};
```
- **Cannot be overloaded**: `::`, `.`, `.*`, `?:`, `sizeof`, `typeid` (and the preprocessor # ##)
- Must be member functions: `=`, `()`, `[]`, `->`; `<<` and `>>` for streams are usually friends
- Unary ++: prefix `T& operator++()`, postfix `T operator++(int)` (dummy int)
- Cannot change precedence, associativity or the number of operands; at least one operand must be a user type

## Inheritance
| Base member → | public inheritance | protected inheritance | private inheritance |
|---|---|---|---|
| public | public | protected | private |
| protected | protected | protected | private |
| private | **not accessible** | not accessible | not accessible |
- Default: `class D : B` is **private** inheritance; `struct D : B` is public
- Types: single, multiple (`class C : public A, public B`), multilevel, hierarchical, hybrid
- **Diamond problem** (D from B and C, both from A → two copies of A) → solve with **virtual base classes**: `class B : virtual public A`
- Constructors run **base first, then derived**; destructors run **derived first, then base**; with multiple inheritance, bases in the order listed in the class head
```cpp
class A { public: A() { cout << "A"; } ~A() { cout << "~A"; } };
class B : public A { public: B() { cout << "B"; } ~B() { cout << "~B"; } };
int main() { B b; }        // output: AB~B~A
```
- Constructors, destructors, friend functions and the assignment operator are **not inherited**

## Virtual functions (run-time polymorphism)
```cpp
class Base { public:
  virtual void show() { cout << "Base "; }
  void f() { cout << "Bf "; } };
class Der : public Base { public:
  void show() override { cout << "Der "; }
  void f() { cout << "Df "; } };
Base *p = new Der;
p->show();   // Der  – virtual: decided by the OBJECT type
p->f();      // Bf   – not virtual: decided by the POINTER type
```
- Implemented with a **vtable** per class and a **vptr** per object
- **Pure virtual**: `virtual void draw() = 0;` → the class is **abstract** (no objects); derived classes must override or stay abstract
- **Virtual destructor**: needed when deleting a derived object through a base pointer, otherwise only the base destructor runs
- Constructors cannot be virtual; calling a virtual function inside a constructor uses the class being constructed
- `final` stops further overriding/inheritance; `override` asks the compiler to check

## Templates (generic programming)
```cpp
template <typename T> T maxOf(T a, T b) { return a > b ? a : b; }
maxOf(3, 7);        // 7  (T = int)
maxOf(2.5, 1.5);    // 2.5 (T = double)
template <class T> class Stack { T a[50]; int top = -1; public: void push(T x) { a[++top] = x; } };
Stack<int> s;
```
- Function and class templates; explicit specialisation `template<> …`; non-type parameters `template <int N>`
- **STL**: containers (vector, list, deque, set, map, stack, queue), iterators, algorithms (sort, find, count)

## Exception handling
```cpp
try {
    if (d == 0) throw "Divide by zero";
    cout << n / d;
} catch (const char *msg) { cout << msg; }
  catch (...) { cout << "Unknown"; }   // catch-all must be LAST
```
- `throw` any type; the first matching catch runs (put derived-class catches before base-class ones); unhandled → `std::terminate()`
- Standard: `std::exception` → runtime_error, logic_error, out_of_range, bad_alloc (failed new); rethrow with `throw;`; `noexcept`
- Stack unwinding calls destructors of local objects

## Streams and files
- Classes: `ios` → `istream` (cin), `ostream` (cout, cerr, clog), `iostream`; files: `ifstream`, `ofstream`, `fstream` (`<fstream>`)
- Manipulators (`<iomanip>`): `endl` (newline + flush), `setw(5)`, `setprecision(2)`, `fixed`, `setfill('*')`
```cpp
ofstream out("marks.txt", ios::app);   out << "Asha 92\\n";  out.close();
ifstream in("marks.txt");  string name; int m;
while (in >> name >> m) cout << name << " " << m << endl;
```
- Open modes: `ios::in`, `ios::out`, `ios::app` (append), `ios::ate` (start at end), `ios::trunc`, `ios::binary`; combine with `|`
- `read()`/`write()` for binary data, `seekg/seekp` (get/put pointer), `tellg/tellp`, `eof()`, `fail()`, `getline(in, line)`
- **Event handling**: GUI frameworks (Qt signals and slots, MFC message maps, callbacks/function objects) call handler functions when events (click, key press) occur

## Traps
- Without `virtual`, a base pointer calls the base version
- An abstract class can still have a pointer/reference of its type
- `catch(...)` placed first hides all later handlers (compile error/warning)
- `endl` flushes the buffer; `"\\n"` does not"""}],
}
