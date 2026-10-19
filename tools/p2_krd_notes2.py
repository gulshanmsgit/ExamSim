"""P2 · KRIES – Data Structures · second, DETAILED notes per topic (no new questions).
Owner's request (19 Oct 2026): much more detailed notes with worked examples, step-by-step traces and exam traps. Added as a
second note per topic (own title), so learners who already imported the pack receive them on re-import. Every trace below
(traversals, BFS/DFS, Kruskal/Prim/Dijkstra, sorting passes, binary search, partition, hashing, heap, address formulas,
IEEE-754 patterns) was re-computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

T = " – detailed notes with worked examples"

NOTES = {
    "Introduction to Data Structures": [{"title": "Introduction to data structures" + T, "md": """## Key terms
- **Data structure** – a way to organise data in memory so the needed operations are efficient
- **Abstract data type (ADT)** – what the operations do (interface), not how (implementation). Stack ADT: push, pop, peek, isEmpty
- **Algorithm** – finite, definite, effective steps with input and output (Knuth's five properties: finiteness, definiteness, input, output, effectiveness)

## Classification
| | Examples |
|---|---|
| Primitive | int, char, float, double, pointer, boolean |
| Linear (non-primitive) | array, linked list, stack, queue |
| Non-linear | tree, graph |
| Static | array (size fixed at compile time) |
| Dynamic | linked list, tree (grow at run time) |
| Homogeneous / heterogeneous | array / structure (record) |

## Counting steps – worked examples
| Code | Count | Order |
|---|---|---|
| `for (i = 0; i < n; i++) s++;` | n | O(n) |
| `for (i = 0; i < n; i++) for (j = 0; j < n; j++) s++;` | n² | O(n²) |
| `for (i = 0; i < n; i++) for (j = 0; j < i; j++) s++;` | n(n − 1)/2 | O(n²) |
| `for (i = 1; i < n; i *= 2) s++;` | ⌈log₂ n⌉ | O(log n) |
| `for (i = n; i > 0; i /= 2) for (j = 0; j < n; j++) s++;` | n log n | O(n log n) |
| `for (i = 1; i < n; i *= 2) for (j = 0; j < i; j++) s++;` | 1 + 2 + 4 + … < 2n | **O(n)** |
| `for (i = 1; i * i <= n; i++) s++;` | √n | O(√n) |
| `for (i = 2; i < n; i = i * i) s++;` | log log n | O(log log n) |
| Two separate (not nested) loops of n | 2n | O(n) |

## Asymptotic notation
- **O** upper bound (worst case usually), **Ω** lower bound, **Θ** tight bound; little-o / little-ω strict
- Drop constants and lower terms: 3n² + 10n log n + 500 = **O(n²)**
- Growth order: 1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n! < nⁿ
- log bases do not matter in O (log₂ n and log₁₀ n differ by a constant)

## Recurrences (divide and conquer)
| Recurrence | Solution | Algorithm |
|---|---|---|
| T(n) = T(n/2) + 1 | O(log n) | binary search |
| T(n) = T(n − 1) + 1 | O(n) | linear recursion, factorial |
| T(n) = T(n − 1) + n | O(n²) | selection sort recursion, quicksort worst |
| T(n) = 2T(n/2) + n | O(n log n) | merge sort, quicksort best |
| T(n) = 2T(n/2) + 1 | O(n) | tree traversal |
| T(n) = 2T(n − 1) + 1 | O(2ⁿ) | Tower of Hanoi (2ⁿ − 1 moves) |
**Master theorem** for T(n) = aT(n/b) + f(n), compare f(n) with n^(log_b a):
1. f smaller → Θ(n^(log_b a)) — e.g. 8T(n/2) + n² → n³
2. equal → Θ(n^(log_b a) · log n) — e.g. 2T(n/2) + n → n log n
3. f larger → Θ(f(n)) — e.g. 2T(n/2) + n² → n²

## Space complexity
- Fixed part (code, constants) + variable part (input-dependent, recursion stack)
- Recursive factorial uses O(n) stack; iterative O(1); merge sort needs O(n) extra; quicksort O(log n) stack on average
- **Time–space trade-off**: e.g. a lookup table (more memory, less time)

## Operations on any data structure
Traversing, searching, inserting, deleting, sorting, merging

## Traps
- O(n) "is also" O(n²) (upper bound) – exams ask for the tightest
- Best case of linear search is O(1), not O(n)
- Amortised O(1) (dynamic array append) ≠ worst-case O(1)"""}],

    "Primitive Data Structures": [{"title": "Primitive data structures" + T, "md": """## What "primitive" means
Basic types operated on directly by machine instructions: **integer, real (float/double), character, boolean, pointer**. Non-primitive structures (arrays, lists, trees) are built from them.

## Integers
- Unsigned n bits: 0 … 2ⁿ − 1 (8 bits: 0 … 255)
- **Two's complement** signed n bits: −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 (8 bits: −128 … 127; 16 bits: −32,768 … 32,767)
- Negate: invert all bits and add 1 → −5 in 8 bits: 00000101 → 11111010 → **11111011**
- Other forms: sign-magnitude and one's complement (both have two zeros, +0 and −0)
- Overflow: 127 + 1 in 8-bit signed wraps to −128

## Number-system conversions (worked)
- 156 → binary: 156 = 128 + 16 + 8 + 4 → **10011100** → octal (groups of 3 from right: 010 011 100) **234** → hex (groups of 4: 1001 1100) **9C**
- 0x2F = 2 × 16 + 15 = **47**; 0o17 = 15; 1011.101₂ = 11.625
- Decimal fraction 0.375 → ×2: 0.75 (0), 1.5 (1), 1.0 (1) → **0.011₂**

## Real numbers – IEEE 754
| Format | Sign | Exponent | Mantissa | Bias |
|---|---|---|---|---|
| Single (float, 32-bit) | 1 | 8 | 23 | **127** |
| Double (64-bit) | 1 | 11 | 52 | 1023 |
Worked: **5.75** = 101.11₂ = 1.0111 × 2² → sign 0, exponent 2 + 127 = 129 = 10000001, mantissa 0111000… → **0x40B80000**
Worked: **−13.25** = −1101.01₂ = −1.10101 × 2³ → sign 1, exponent 130 = 10000010 → **0xC1540000**
- Value = (−1)ˢ × 1.mantissa × 2^(exponent − bias); exponent all 1s = infinity/NaN; all 0s = zero/denormal
- 0.1 cannot be stored exactly → never compare floats with ==

## Characters
- ASCII 7-bit (128 codes); 'A' = 65, 'a' = 97, '0' = 48, space = 32, '\\n' = 10; upper ↔ lower differ by 32
- Digit value: `c − '0'`; EBCDIC (IBM), **Unicode** (UTF-8 1–4 bytes, UTF-16) for all scripts including Kannada

## Boolean and pointer
- Boolean: true/false; in C any non-zero is true (`_Bool` / `<stdbool.h>` since C99)
- Pointer: stores an address; size depends on the machine (4 bytes on 32-bit, 8 on 64-bit), not on the type pointed to

## Operations on primitive types
Create (declare), select (access), update (assign), destroy (go out of scope); arithmetic, logical, relational, bitwise

## Traps
- Range of a signed 8-bit number is −128 … **127** (not 128)
- Hex digit = 4 bits, octal digit = 3 bits
- IEEE single bias is 127, double bias is 1023
- sizeof(char) is always 1 in C"""}],

    "Arrays in Data Structures": [{"title": "Arrays in data structures" + T, "md": """## Properties
- Contiguous memory, same type, random access by index in **O(1)**
- Fixed size; insertion/deletion in the middle needs shifting → O(n)

## Address formulas (w = bytes per element)
- 1-D, lower bound LB: **base + (i − LB) × w**
- 2-D row-major: **base + ((i − LR) × N + (j − LC)) × w** (N = number of columns)
- 2-D column-major: **base + ((j − LC) × M + (i − LR)) × w** (M = number of rows)
- Number of elements in A[l₁..u₁][l₂..u₂] = (u₁ − l₁ + 1)(u₂ − l₂ + 1)

Worked examples
1. A[1..10], base 2000, w = 4 → A[7] = 2000 + (7 − 1) × 4 = **2024**
2. `int a[3][4]`, base 1000, w = 4 → a[2][1] = 1000 + (2 × 4 + 1) × 4 = **1036**
3. A[−2..5][3..8], base 500, w = 2 → 8 × 6 = 48 elements; A[1][5]: row-major 500 + (3 × 6 + 2) × 2 = **540**; column-major 500 + (2 × 8 + 3) × 2 = **538**
4. 3-D A[L][M][N] row-major: base + ((i × M + j) × N + k) × w

## Operations with cost
| Operation | Cost | Note |
|---|---|---|
| Access a[i] | O(1) | address formula |
| Search (unsorted) | O(n) | linear search |
| Search (sorted) | O(log n) | binary search |
| Insert at position k | O(n) | shift a[k … n−1] right, from the **end** backwards |
| Delete at position k | O(n) | shift a[k+1 … n−1] left |
| Insert at end | O(1) | if space |

Insert 25 at index 2 of [10, 20, 30, 40]: move 40 → a[4], 30 → a[3], put 25 → **[10, 20, 25, 30, 40]** (2 shifts)

## Special matrices
- **Sparse matrix**: mostly zeros → store (row, col, value) **triplets**; first row of the triplet table often holds (rows, cols, count)
  - 4 × 5 matrix with 3 non-zero values → triplet table of 4 rows × 3 columns
- **Lower triangular** n × n: n(n + 1)/2 non-zero elements; row-major index of (i, j), 1-based, i ≥ j: **i(i − 1)/2 + (j − 1)**
- Upper triangular: also n(n + 1)/2; **tridiagonal**: 3n − 2 elements; diagonal: n
- Symmetric matrix: store only one triangle

## Array vs linked list
| | Array | Linked list |
|---|---|---|
| Memory | contiguous | scattered nodes |
| Size | fixed | dynamic |
| Access i-th | O(1) | O(n) |
| Insert/delete at front | O(n) | O(1) |
| Extra memory | none | a pointer per node |
| Cache friendly | yes | no |

## Uses
Lookup tables, matrices, implementing stacks/queues/heaps/hash tables, strings, polynomials (coefficient arrays)

## Traps
- C arrays are row-major; Fortran/MATLAB column-major
- For row-major the **column count** appears in the formula; for column-major the **row count**
- Upper bound minus lower bound **plus one** = number of elements"""}],

    "Linked Lists": [{"title": "Linked lists" + T, "md": """## Node and kinds
```c
struct node { int data; struct node *next; };
```
| Kind | Links | Note |
|---|---|---|
| Singly | next | one direction |
| **Doubly** | prev + next | both directions; delete a given node in O(1) |
| **Circular** | last → first | no NULL; any node can be the start; round-robin |
| Circular doubly | both ways, closed | |
| Header list | dummy first node | simplifies insert/delete |

## Core operations (singly)
```c
/* insert at beginning – O(1) */
t = malloc(sizeof *t); t->data = x; t->next = head; head = t;

/* insert at end – O(n) without a tail pointer */
t->next = NULL; if (!head) head = t; else { p = head; while (p->next) p = p->next; p->next = t; }

/* insert after node p */
t->next = p->next; p->next = t;          /* order matters – reversing these loses the rest */

/* delete first */
t = head; head = head->next; free(t);

/* delete the node after p */
t = p->next; p->next = t->next; free(t);

/* traverse / count */
for (p = head, n = 0; p; p = p->next) n++;
```

## Reverse a list (three pointers) – trace on 1 → 2 → 3
```c
prev = NULL; cur = head;
while (cur) { nxt = cur->next; cur->next = prev; prev = cur; cur = nxt; }
head = prev;
```
| Step | prev | cur | list so far |
|---|---|---|---|
| start | NULL | 1 | |
| 1 | 1 | 2 | 1 → NULL |
| 2 | 2 | 3 | 2 → 1 → NULL |
| 3 | 3 | NULL | 3 → 2 → 1 → NULL |

## Two-pointer tricks
- **Middle**: slow moves 1, fast moves 2; when fast reaches the end, slow is in the middle
- **Loop detection (Floyd)**: if slow and fast ever meet there is a cycle; O(n) time, O(1) space
- **k-th from end**: move one pointer k ahead, then move both
- Merge two sorted lists in O(m + n)

## Doubly linked insertion (after p)
```c
t->next = p->next; t->prev = p;
if (p->next) p->next->prev = t;
p->next = t;
```
Deleting node q: `q->prev->next = q->next; q->next->prev = q->prev; free(q);` (check the ends)

## Costs
| Operation | Singly | Doubly |
|---|---|---|
| Insert/delete at head | O(1) | O(1) |
| Insert at tail | O(n) (O(1) with tail pointer) | O(1) with tail |
| Delete a given node | O(n) (need previous) | **O(1)** |
| Search / access k-th | O(n) | O(n) |
- Binary search is not efficient on a linked list (no random access)

## Applications
Polynomials (coefficient, exponent, next) – adding two polynomials merges by exponent; sparse matrices; stacks and queues; adjacency lists of graphs; undo history; music playlists (circular); memory free lists

## Traps
- Always check for an empty list (head == NULL)
- Losing the head pointer loses the whole list (memory leak)
- In a circular list the loop condition is `p->next != head`, not `p != NULL`
- A doubly linked node needs **two** pointer fields → more memory"""}],

    "Stacks": [{"title": "Stacks" + T, "md": """## Infix → postfix, step by step: A + B * C − D
| Symbol | Action | Stack | Output |
|---|---|---|---|
| A | output | | A |
| + | push | + | A |
| B | output | + | A B |
| * | higher than + → push | + * | A B |
| C | output | + * | A B C |
| − | pop * and + (≥ precedence), push − | − | A B C * + |
| D | output | − | A B C * + D |
| end | pop all | | **A B C * + D −** |
Rules: operand → output; `(` → push; `)` → pop until `(`; operator → pop while the top has **higher or equal** precedence (for right-associative `^` only higher), then push. Precedence: `^` > `* / %` > `+ −`.

More: (A + B) * (C − D) → **A B + C D − ***; A * (B + C) / D → **A B C + * D /**; A ^ B ^ C → **A B C ^ ^** (right-associative)

## Infix → prefix
Reverse the infix (swap brackets), convert to postfix, reverse the result.
(A + B) * C → **\\* + A B C**; A + B * C → **+ A * B C**

## Evaluate postfix: 2 3 4 * + 5 −
| Symbol | Stack |
|---|---|
| 2 | 2 |
| 3 | 2 3 |
| 4 | 2 3 4 |
| * | 2 12 |
| + | 14 |
| 5 | 14 5 |
| − | **9** |
Pop the **right** operand first: for `a b −` the result is a − b. Prefix is evaluated from **right to left**.

## Stack permutations
- With push/pop of 1, 2, 3 in order, 5 output orders are possible; **3 1 2** is impossible (3 out first means 1 and 2 are stacked with 2 on top)
- Count for n = **Catalan number** C(2n, n)/(n + 1): 1, 2, 5, 14, 42, 132

## Array implementation (MAX = 5)
```c
int s[MAX], top = -1;
void push(int x) { if (top == MAX - 1) puts("Overflow"); else s[++top] = x; }
int pop(void)    { if (top == -1) { puts("Underflow"); return -1; } return s[top--]; }
```
Trace: push 10, 20, 30, pop, push 40 → stack 10 20 40, top = 2

## Recursion uses a stack
- Each call pushes an activation record (parameters, locals, return address)
- fact(3) → push fact(3), fact(2), fact(1) → pop with results 1, 2, 6
- Converting recursion to iteration = using an explicit stack

## Applications
Function calls, undo, browser back, balanced brackets `{[()]}`, expression conversion/evaluation, **DFS**, backtracking (maze, N-queens), decimal → binary (push remainders, pop to print: 13 → 1101), reversing a string, Tower of Hanoi (2ⁿ − 1 moves)

## Variants
- Two stacks in one array: grow from both ends; overflow when top1 + 1 == top2
- Stack with two queues; **min-stack** (extra stack of minimums) gives getMin in O(1)
- Linked stack: push/pop at the head, no overflow (until memory runs out)

## Traps
- Underflow = pop from an empty stack; overflow = push onto a full stack
- In postfix there are no brackets and no precedence rules are needed
- Stack is LIFO; recursion depth = maximum stack size"""}],

    "Queues": [{"title": "Queues" + T, "md": """## Linear queue (array)
- FIFO; insert at **rear**, delete at **front**
- Start front = rear = −1; enqueue: `if (rear == MAX − 1) overflow; if (front == −1) front = 0; q[++rear] = x;`
- Dequeue: `x = q[front]; if (front == rear) front = rear = −1; else front++;`
- Problem: after deletions the freed front cells cannot be reused → "full" even with space → **circular queue**

## Circular queue (size N = 5) – trace
- Enqueue: `rear = (rear + 1) % N`; dequeue: `front = (front + 1) % N`
- **Full**: `(rear + 1) % N == front`; **empty**: front == −1 (or with the "one empty slot" method: front == rear)
- Elements = (rear − front + N) % N + 1 (when not empty)
| Operation | front | rear | Contents |
|---|---|---|---|
| enqueue 10, 20, 30, 40, 50 | 0 | 4 | 10 20 30 40 50 (full) |
| dequeue, dequeue | 2 | 4 | 30 40 50 |
| enqueue 60 | 2 | **0** | 30 40 50 60 |
| enqueue 70 | 2 | 1 | 30 40 50 60 70 → (1 + 1) % 5 = 2 = front → **full** |

## Linked queue
- front = head, rear = tail; enqueue at tail O(1), dequeue at head O(1); no overflow until memory ends

## Deque (double-ended queue)
- Insert and delete at **both** ends
- **Input-restricted**: insert at one end only, delete at both; **output-restricted**: delete at one end only, insert at both
- Can act as both a stack and a queue

## Priority queue
- Each element has a priority; the highest (or lowest) priority leaves first
| Implementation | Insert | Delete-max |
|---|---|---|
| Unsorted array/list | O(1) | O(n) |
| Sorted array/list | O(n) | O(1) |
| **Binary heap** | **O(log n)** | **O(log n)** |
- Max-heap from [4, 10, 3, 5, 1] (heapify from the last internal node) → **[10, 5, 3, 4, 1]**

## Queue using two stacks
- Enqueue: push on S1. Dequeue: if S2 empty, pop everything from S1 into S2; pop S2 → amortised O(1)

## Applications
CPU scheduling (ready queue, round robin = circular queue), printer spooling, keyboard and I/O buffers, **BFS**, call-centre/ticket systems, Josephus problem (circular)

## Comparison
| | Stack | Queue |
|---|---|---|
| Order | LIFO | FIFO |
| Ends used | one (top) | two (front, rear) |
| Insert / delete | push / pop | enqueue / dequeue |
| Graph search | DFS | BFS |

## Traps
- Circular queue of size N stores N elements with a separate count/flag, or **N − 1** with the "one empty slot" rule – check the question
- Priority queue is not FIFO for different priorities (FIFO only among equal priorities)
- Rear pointer moves on insertion, front on deletion"""}],

    "Trees – Binary Trees": [{"title": "Binary trees" + T, "md": """## Terms
Root, parent, child, siblings, leaf (degree 0), internal node, **degree** (number of children), **level** (root = 0), **depth** (edges from root), **height** (edges on the longest root-to-leaf path; one-node tree = 0), subtree, ancestor/descendant, forest

## Properties of binary trees
- Maximum nodes at level l = **2ˡ**; in a tree of height h = **2ʰ⁺¹ − 1**
- Minimum height with n nodes = ⌈log₂(n + 1)⌉ − 1
- **n₀ = n₂ + 1** (leaves = nodes with two children + 1)
- A binary tree with n nodes has **n + 1 NULL links** and n − 1 edges
- Number of distinct binary tree shapes with n nodes = Catalan: 1, 2, **5**, 14, 42
- **Full/strict**: every node has 0 or 2 children; **complete**: all levels full except possibly the last, filled left to right; **perfect**: all leaves at the same level
- Array storage (0-based): children of i at **2i + 1** and **2i + 2**, parent at ⌊(i − 1)/2⌋ (1-based: 2i, 2i + 1, ⌊i/2⌋)

## Traversals – worked example
```
            A
          /   \\
         B     C
        / \\     \\
       D   E     F
          /
         G
```
| Traversal | Rule | Result |
|---|---|---|
| Preorder | root, left, right | **A B D E G C F** |
| Inorder | left, root, right | **D B G E A C F** |
| Postorder | left, right, root | **D G E B F C A** |
| Level order (BFS, queue) | level by level | **A B C D E F G** |
- Inorder + preorder (or inorder + postorder) determines a unique tree; preorder + postorder does not (unless the tree is full)
- Rebuild: the first preorder (last postorder) symbol is the root; split the inorder at it

## Binary search tree (BST)
Left subtree < node < right subtree; **inorder gives sorted order**.
Insert 50, 30, 70, 20, 40, 60, 80, 35:
```
             50
          /      \\
        30        70
       /  \\      /  \\
      20   40   60   80
          /
         35
```
- Preorder 50 30 20 40 35 70 60 80 · Postorder 20 35 40 30 60 80 70 50 · height 3
- Search/insert/delete O(h): O(log n) when balanced, **O(n) when skewed** (sorted input makes a chain)
- Delete: leaf → remove; one child → link the child up; two children → replace with the **inorder successor** (smallest in the right subtree) or predecessor, then delete that node
- Delete 30 above → successor 35 takes its place

## Expression trees
Leaves are operands, internal nodes operators: (a + b) * c → root *, left +(a, b), right c. Preorder = prefix, inorder = infix, postorder = postfix.

## Balanced trees
- **AVL**: balance factor = height(left) − height(right) ∈ {−1, 0, 1}; fix with LL, RR (single) or LR, RL (double) rotations
- Inserting 10, 20, 30 into an AVL tree → RR case → rotate left → 20 is the root
- Others: red-black tree, B-tree / B+ tree (databases, multi-way), splay tree; **heap** = complete binary tree with the heap property
- **Threaded binary tree**: NULL links point to inorder predecessor/successor → traversal without a stack

## Traps
- Height vs depth vs level: read whether the root is counted as 0 or 1
- Inorder of a BST is sorted; preorder is not
- A complete binary tree is not necessarily full, and vice versa
- Level order needs a **queue**; recursive DFS traversals use a **stack**"""}],

    "Graphs": [{"title": "Graphs" + T, "md": """## Terms
- G = (V, E); directed/undirected; weighted; **degree** (in-degree, out-degree); path, cycle, connected, strongly connected (directed), complete graph, tree (connected, acyclic, n − 1 edges), spanning tree, DAG
- **Σ degrees = 2|E|** (handshake lemma) → the number of odd-degree vertices is even
- Maximum edges: undirected n(n − 1)/2, directed n(n − 1)
- Complete graph Kₙ has **nⁿ⁻²** spanning trees (Cayley): K₄ → 16

## Representations
| | Adjacency matrix | Adjacency list |
|---|---|---|
| Space | O(V²) | O(V + E) |
| Edge (u, v)? | O(1) | O(degree) |
| All neighbours | O(V) | O(degree) |
| Best for | dense graphs | sparse graphs |
- Undirected matrix is symmetric; row sum = degree; incidence matrix is V × E

## BFS and DFS – worked example
Edges: A–B, A–C, B–D, B–E, C–F, E–F (neighbours in alphabetical order, start at A)
- **BFS** (queue): **A B C D E F** – visits level by level; gives shortest paths in an unweighted graph
- **DFS** (stack / recursion): **A B D E F C** – goes deep first, backtracks
- Both O(V + E) with lists, O(V²) with a matrix
- Uses: BFS – shortest path (unweighted), level order, broadcasting; DFS – cycle detection, topological sort, connected components, maze solving

## Minimum spanning tree – worked example
Edges (weight): A–B 4, A–C 2, B–C 1, B–D 5, C–D 8, C–E 10, D–E 2, D–F 6, E–F 3
- **Kruskal** (sort edges, add if no cycle – union–find): B–C 1, A–C 2, D–E 2, E–F 3, B–D 5 → **total 13** (A–B 4 rejected: cycle)
- **Prim** from A (grow one tree, cheapest edge leaving it): A–C 2, C–B 1, B–D 5, D–E 2, E–F 3 → **total 13**
- Same total; Kruskal O(E log E) good for sparse; Prim O(E log V) with a heap, O(V²) with a matrix, good for dense
- MST has V − 1 edges; unique if all weights are distinct

## Shortest paths
- **Dijkstra** (non-negative weights, greedy): from A on the graph above, final order A 0, C 2, B 3 (via C), D 8, E 10, F 13
- Bellman–Ford: negative weights allowed, detects negative cycles, O(VE)
- Floyd–Warshall: all pairs, O(V³), dynamic programming; Warshall: transitive closure

## Topological sort (DAG only)
Linear order with every edge u → v having u before v: repeatedly remove a vertex of in-degree 0 (Kahn), or reverse DFS finishing order. Used for task scheduling, course prerequisites, build systems. A graph with a cycle has none.

## Traps
- BFS uses a queue, DFS a stack
- Dijkstra fails with negative edge weights
- A tree with n vertices has exactly n − 1 edges; adding any edge makes a cycle
- Adjacency matrix of an undirected graph is symmetric, of a directed graph usually not"""}],

    "Searching and Sorting": [{"title": "Searching and sorting" + T, "md": """## Linear vs binary search
- Linear: any order; best 1, worst n, average (n + 1)/2 comparisons → O(n)
- **Binary**: sorted array only; O(log n); max comparisons ⌊log₂ n⌋ + 1 (1000 items → 10)

Binary search on [3, 8, 15, 23, 42, 56, 71, 89, 94] (indices 0–8):
| Find 71 | low | high | mid | a[mid] |
|---|---|---|---|---|
| 1 | 0 | 8 | 4 | 42 < 71 → low = 5 |
| 2 | 5 | 8 | 6 | **71 found** (2 comparisons) |
| Find 10 | 0 → 0 → 2 | 8 → 3 → 3 | 4, 1, 2 | 42, 8, 15 → low 2 > high 1: **not found** |

## Sorting passes on [64, 25, 12, 22, 11]
**Bubble** (largest sinks to the end each pass):
1. 25 12 22 11 **64** 2. 12 22 11 **25 64** 3. 12 11 **22 25 64** 4. **11 12 22 25 64**

**Selection** (find the minimum, swap into place):
1. **11** 25 12 22 64 2. 11 **12** 25 22 64 3. 11 12 **22** 25 64 4. 11 12 22 25 64

**Insertion** (insert the next item into the sorted left part):
1. 25 64 | 12 22 11 2. 12 25 64 | 22 11 3. 12 22 25 64 | 11 4. 11 12 22 25 64

## Quick sort – Lomuto partition, pivot = last
[10, 80, 30, 90, 40, 50, 70], pivot 70 → elements < 70 move left → **[10, 30, 40, 50, 70, 90, 80]**, pivot at index 4; recurse on both sides
- Best/average O(n log n); **worst O(n²)** when the pivot is always the smallest/largest (already sorted input with first/last pivot); not stable; in-place

## Merge sort
Split in halves until size 1, merge sorted halves: [38, 27, 43, 3] → [27, 38] [3, 43] → [3, 27, 38, 43]. Always O(n log n), stable, needs O(n) extra space.

## Heap sort
Build a max-heap, swap the root with the last element, shrink, heapify. Max-heap of [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17] → [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]. O(n log n) always, in-place, not stable.

## Summary table
| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble | O(n)* | O(n²) | O(n²) | O(1) | yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | no |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | no |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | no |
| Counting / Radix | O(n + k) / O(d(n + k)) | | | O(n + k) | yes |
\\* bubble sort with a "no swaps → stop" flag. Selection sort makes the **fewest swaps** (n − 1). Insertion sort is best for nearly sorted data. Comparison sorts cannot beat **Ω(n log n)**.

## Hashing
- h(k) = k mod m (division method); collisions resolved by **chaining** (lists) or **open addressing**: linear probing (h + i), quadratic probing (h + i²), double hashing
- Insert 23, 43, 13, 27, 37, 50 into a table of 10 with linear probing:
  23 → 3; 43 → 3 taken → **4**; 13 → 3, 4 taken → **5**; 27 → 7; 37 → 7 taken → **8**; 50 → 0
  Final: [50, –, –, 23, 43, 13, –, 27, 37, –]
- Load factor α = n/m; linear probing suffers **primary clustering**, quadratic **secondary clustering**
- Average search O(1); worst O(n)

## Traps
- Binary search needs a **sorted** array and random access
- Number of passes for bubble/selection = n − 1
- Quick sort's worst case is O(n²) even though it is "quick"
- Stable = equal keys keep their original order"""}],
}
