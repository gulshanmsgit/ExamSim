"""P2 · KRIES – Data Structures · third note per topic: the KRIES syllabus line broken down WORD BY WORD (no new questions).
Owner's request (19 Oct 2026): "breakdown each word as notes" – every term of the official KRIES syllabus line (as in
tools/make_kries_plan.py), in syllabus order: what it means, key facts, a small example and the exam angle. Traces match the
script-checked ones in p2_krd_notes2.py."""

TOPICS = {}  # notes only

W = "KRIES syllabus word by word – "

NOTES = {
    "Introduction to Data Structures": [{"title": W + "Introduction to data structures", "md": """> **Syllabus:** Definition, classification of data structures, operations on data structures, introduction to time and space complexity

### Definition (of a data structure)
- **Means:** a way of organising and storing data in memory so that it can be used efficiently.
- **Key facts:** data structure + algorithm = program (Niklaus Wirth); choice depends on the operations needed; an **ADT** states the operations, the data structure implements them.
- **Example:** a phone contact list kept sorted (array) for binary search, or as a linked list for easy insertion.
- **Exam point:** a data structure is about **organisation**, an algorithm about **steps**.

### Classification of data structures
- **Means:** grouping by nature.
- **Key facts:** **primitive** (int, char, float, pointer) vs **non-primitive**; non-primitive → **linear** (array, stack, queue, linked list – elements in sequence) and **non-linear** (tree, graph – hierarchy/network); **static** (fixed size – array) vs **dynamic** (grows – linked list); homogeneous vs heterogeneous.
- **Example:** family tree → tree; road map → graph; plates pile → stack; ticket line → queue.
- **Exam point:** stack and queue are **linear**; tree and graph are **non-linear**.

### Operations on data structures
- **Means:** what we do with the stored data.
- **Key facts:** **traversing** (visit each element once), **searching** (find an element), **inserting**, **deleting**, **sorting** (arrange in order), **merging** (combine two sorted lists); also create, update, destroy.
- **Example:** printing every student's marks = traversal.
- **Exam point:** "visiting every element exactly once" = **traversal**.

### Introduction to time complexity
- **Means:** how the running time grows with input size n.
- **Key facts:** counted in basic operations, expressed with **Big-O** (upper bound), Ω (lower), Θ (tight); best, average, worst case; order: 1 < log n < n < n log n < n² < 2ⁿ < n!
- **Example:** one loop over n → O(n); two nested loops → O(n²); halving each step → O(log n).
- **Exam point:** linear search worst case O(n), binary search O(log n).

### Introduction to space complexity
- **Means:** how much memory an algorithm needs as n grows.
- **Key facts:** fixed part (code, constants, simple variables) + variable part (arrays sized by n, **recursion stack**); auxiliary space = extra space beyond the input.
- **Example:** iterative factorial O(1) space; recursive factorial O(n) (n stack frames); merge sort O(n) extra.
- **Exam point:** time–space trade-off – using more memory (e.g. a lookup table) to save time."""}],

    "Primitive Data Structures": [{"title": W + "Primitive data structures", "md": """> **Syllabus:** Integer, character, float, strings – memory representation and primitive operations; string manipulation using pointers

### Integer
- **Means:** whole numbers, stored in binary.
- **Key facts:** n bits unsigned 0 … 2ⁿ − 1; signed uses **two's complement**: −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 (int 32-bit: −2,147,483,648 … 2,147,483,647); −5 in 8 bits = 11111011.
- **Example:** 13 = 00001101.
- **Exam point:** overflow wraps around (unsigned); signed overflow is undefined in C.

### Character
- **Means:** a single symbol stored as a small integer code.
- **Key facts:** **ASCII** 7-bit (128 codes, stored in 1 byte): 'A' 65, 'a' 97, '0' 48, space 32; **Unicode** for all scripts (UTF-8, UTF-16; Java char = 2 bytes).
- **Example:** `'a' - 'A'` = 32; `'7' - '0'` = 7.
- **Exam point:** upper ↔ lower case differ by 32 (bit 5).

### Float
- **Means:** real numbers in **IEEE 754** floating point.
- **Key facts:** single (32-bit): 1 sign + 8 exponent (bias 127) + 23 mantissa; double (64-bit): 1 + 11 (bias 1023) + 52; value = (−1)ˢ × 1.m × 2^(e − bias).
- **Example:** 5.75 = 1.0111 × 2² → 0 10000001 0111000… = 0x40B80000.
- **Exam point:** 0.1 can't be stored exactly – never compare floats with `==`.

### Strings
- **Means:** a sequence of characters; in C a char array ending with `'\\0'`.
- **Key facts:** length n needs n + 1 bytes; stored in contiguous memory; literals are read-only.
- **Example:** "DATA" → 'D' 'A' 'T' 'A' '\\0' (5 bytes).
- **Exam point:** `strlen` excludes `'\\0'`, `sizeof` of the array includes it.

### Memory representation
- **Means:** how each type is laid out in bytes.
- **Key facts:** int 4 bytes (little-endian on x86: lowest byte at the lowest address), char 1, float 4, double 8, pointer 8 (64-bit); arrays/strings contiguous.
- **Example:** int 0x12345678 at address 100 on little-endian: 100 → 78, 101 → 56, 102 → 34, 103 → 12.
- **Exam point:** big-endian stores the **most** significant byte first (network byte order).

### Primitive operations
- **Means:** basic operations directly supported on primitive types.
- **Key facts:** create (declare), select/access, update (assign), destroy; arithmetic, relational, logical, bitwise operations; type conversion.
- **Example:** `int x = 5; x = x * 2;` → create, access, update.
- **Exam point:** primitive types are operated on by **machine instructions** directly.

### String manipulation using pointers
- **Means:** walking through a string with a `char *` instead of indexes.
- **Key facts:** loop `while (*p) p++;` stops at `'\\0'`; length = p − s; copy `while ((*d++ = *s++));`; compare character by character.
- **Example:** `int len(char *s) { char *p = s; while (*p) p++; return p - s; }` → len("KRIES") = 5.
- **Exam point:** `*p++` reads then moves; reverse a string with two pointers swapping from both ends."""}],

    "Arrays in Data Structures": [{"title": W + "Arrays", "md": """> **Syllabus:** Storage representation of 1-D and 2-D arrays, insertion and deletion on 1-D arrays, advantages and disadvantages of arrays

### Storage representation of 1-D arrays
- **Means:** how a 1-D array sits in memory – one block of consecutive cells.
- **Key facts:** Loc(A[i]) = Base + w × (i − LB); number of elements = UB − LB + 1.
- **Example:** A[1..20], base 500, w = 2 → A[12] = 500 + 2 × 11 = **522**.
- **Exam point:** random access in **O(1)** because of this formula.

### Storage representation of 2-D arrays
- **Means:** mapping rows × columns onto linear memory.
- **Key facts:** **row-major** (C): Base + w × [(i − LR) × N + (j − LC)]; **column-major** (Fortran): Base + w × [(j − LC) × M + (i − LR)]; M rows, N columns.
- **Example:** A[3][4], base 1000, w = 4, A[2][1]: row-major 1000 + 4 × 9 = **1036**; column-major 1000 + 4 × (1 × 3 + 2) = **1020**.
- **Exam point:** row-major uses the column count, column-major the row count.

### Insertion on 1-D arrays
- **Means:** adding an element at position k.
- **Key facts:** check space; shift A[n−1] … A[k] one place right (start from the **end**); put the item; n++. Cost O(n) (worst at the front), O(1) at the end.
- **Example:** [10, 20, 30, 40], insert 25 at index 2 → [10, 20, 25, 30, 40] (2 shifts).
- **Exam point:** shifting from the front would overwrite data.

### Deletion on 1-D arrays
- **Means:** removing the element at position k.
- **Key facts:** save A[k]; shift A[k+1] … A[n−1] one place left; n−−. Cost O(n).
- **Example:** [10, 20, 30, 40] delete index 1 → [10, 30, 40].
- **Exam point:** average shifts ≈ n/2 for insertion or deletion.

### Advantages of arrays
- **Means:** why arrays are used.
- **Key facts:** O(1) random access by index; simple; no pointer overhead; cache-friendly (contiguous); easy to implement stacks, queues, heaps, matrices.
- **Example:** marks of 60 students in `int m[60]`.
- **Exam point:** best when size is known and access is by position.

### Disadvantages of arrays
- **Means:** limits of arrays.
- **Key facts:** fixed size (waste or overflow); insertion/deletion costly (shifting); needs one contiguous block; homogeneous only.
- **Example:** declaring 1000 cells for 10 values wastes memory.
- **Exam point:** these are solved by **linked lists**."""}],

    "Linked Lists": [{"title": W + "Linked lists", "md": """> **Syllabus:** Pointers, dynamic memory allocation, singly linked lists and their operations, insertion and deletion of a node; circular and doubly linked lists

### Pointers
- **Means:** variables holding addresses – the "links" of a linked list.
- **Key facts:** each node holds data + pointer to the next node; `head` points to the first node; last node's next = NULL.
- **Example:** `struct node { int data; struct node *next; };`
- **Exam point:** losing `head` loses the whole list.

### Dynamic memory allocation
- **Means:** getting memory at run time from the **heap**.
- **Key facts:** `malloc(size)` (garbage), `calloc(n, size)` (zeroed), `realloc`, `free`; returns NULL on failure; forgetting free → memory leak.
- **Example:** `struct node *t = malloc(sizeof(struct node));`
- **Exam point:** this is what lets a linked list grow and shrink.

### Singly linked lists
- **Means:** nodes linked in one direction (next only).
- **Key facts:** access only from head; traversal O(n); no random access; extra memory per node for one pointer.
- **Example:** head → 10 → 20 → 30 → NULL.
- **Exam point:** to delete a node you need its **previous** node.

### Operations (on singly linked lists)
- **Means:** creation, traversal, search, count, insertion, deletion, reversal, concatenation.
- **Key facts:** traverse `for (p = head; p != NULL; p = p->next)`; search O(n); reverse with three pointers (prev, cur, next).
- **Example:** counting nodes of the list above → 3.
- **Exam point:** middle node = slow/fast pointer method.

### Insertion of a node
- **Means:** adding a node at the beginning, end or after a given node.
- **Key facts:** beginning: `t->next = head; head = t;` (O(1)); end: walk to last, `last->next = t; t->next = NULL;` (O(n)); after p: `t->next = p->next; p->next = t;` (this order!).
- **Example:** insert 15 after 10 in 10 → 20 → 10 → 15 → 20.
- **Exam point:** swapping the two lines of "insert after" breaks the list.

### Deletion of a node
- **Means:** unlinking and freeing a node.
- **Key facts:** first: `t = head; head = head->next; free(t);`; after p: `t = p->next; p->next = t->next; free(t);`; check empty list (underflow).
- **Example:** delete 20 from 10 → 20 → 30 → 10 → 30.
- **Exam point:** free the node **after** relinking.

### Circular linked lists
- **Means:** the last node points back to the first (no NULL).
- **Key facts:** any node can start a traversal; stop when you come back to the start (`p->next != head`); often a tail pointer is kept (tail->next = head) → insert at both ends in O(1).
- **Example:** round-robin CPU scheduling, multiplayer turns.
- **Exam point:** using `p != NULL` as the stop test loops forever.

### Doubly linked lists
- **Means:** each node has **prev** and **next** pointers.
- **Key facts:** traverse both ways; delete a given node in O(1); more memory (two pointers); insertion updates four links.
- **Example:** browser back/forward history, music playlist.
- **Exam point:** a node of a doubly linked list of ints on 64-bit: 4 + 8 + 8 = 20 → 24 bytes with padding."""}],

    "Stacks": [{"title": W + "Stacks", "md": """> **Syllabus:** Concepts, operations, sequential and linked implementation; applications – recursion, Tower of Hanoi, infix to postfix, evaluation of postfix

### Concepts
- **Means:** a linear list where insertion and deletion happen at **one end (top)** – **LIFO** (last in, first out).
- **Key facts:** top points to the last inserted element; empty when top = −1 (array).
- **Example:** pile of plates; undo in an editor.
- **Exam point:** push A, B, C → pop gives C first.

### Operations
- **Means:** push (insert), pop (remove), peek/top (look), isEmpty, isFull.
- **Key facts:** all O(1); **overflow** = push on full, **underflow** = pop on empty.
- **Example:** push 1, push 2, pop, push 3 → stack 1 3 (top 3).
- **Exam point:** possible pop orders of 1, 2, 3 (pushed in order) = 5; 3 1 2 is impossible.

### Sequential implementation
- **Means:** stack in an array.
- **Key facts:** `push: if (top == MAX-1) overflow; else s[++top] = x;` · `pop: if (top == -1) underflow; else x = s[top--];` – fixed size.
- **Example:** MAX = 3, push 4 items → 4th causes overflow.
- **Exam point:** full when top = MAX − 1.

### Linked implementation
- **Means:** stack as a linked list with top = head.
- **Key facts:** push = insert at head, pop = delete head, both O(1); no overflow until memory ends; extra pointer per node.
- **Example:** push 5: `t->data = 5; t->next = top; top = t;`
- **Exam point:** empty when top == NULL.

### Applications – recursion
- **Means:** every function call pushes an **activation record** (parameters, locals, return address) on the call stack.
- **Key facts:** return pops it; too deep → stack overflow; any recursion can be rewritten with an explicit stack.
- **Example:** fact(3) → frames fact(3), fact(2), fact(1) pushed, then popped with 1, 2, 6.
- **Exam point:** depth of recursion = maximum stack size used.

### Applications – Tower of Hanoi
- **Means:** move n discs from A to C using B; one disc at a time; never a bigger disc on a smaller one.
- **Key facts:** move n − 1 to B, largest to C, n − 1 to C; moves = **2ⁿ − 1** (3 discs = 7, 4 = 15, 64 = 2⁶⁴ − 1).
- **Example:** n = 2: A→B, A→C, B→C.
- **Exam point:** T(n) = 2T(n − 1) + 1 → O(2ⁿ).

### Applications – infix to postfix
- **Means:** converting `A + B * C` (operator between) to `A B C * +` (operator after).
- **Key facts:** operands go to output; `(` pushed; `)` pops until `(`; an operator pops operators of higher or equal precedence first (except right-associative `^`); end: pop all.
- **Example:** (A + B) * C → A B + C *; A + B * C − D → A B C * + D −.
- **Exam point:** postfix needs no brackets and no precedence rules.

### Applications – evaluation of postfix
- **Means:** computing a postfix expression with an operand stack.
- **Key facts:** operand → push; operator → pop **right** (first pop) and **left** (second pop), push left op right; answer = the last value.
- **Example:** 6 2 / 3 − 4 2 * + → 6/2 = 3, 3 − 3 = 0, 4 × 2 = 8, 0 + 8 = **8**.
- **Exam point:** for `a b −` the result is a − b, not b − a."""}],

    "Queues": [{"title": W + "Queues", "md": """> **Syllabus:** Concepts, operations, sequential and linked implementation; circular queues, priority queues and deques; applications of queues

### Concepts
- **Means:** a linear list with insertion at the **rear** and deletion at the **front** – **FIFO** (first in, first out).
- **Key facts:** two pointers front and rear; empty when front = −1 (or front > rear).
- **Example:** people at a bus stop; print jobs.
- **Exam point:** enqueue A, B, C → dequeue gives A first.

### Operations
- **Means:** enqueue (insert at rear), dequeue (remove from front), peek/front, isEmpty, isFull.
- **Key facts:** all O(1); overflow on a full queue, underflow on an empty one.
- **Example:** enqueue 1, 2, 3; dequeue → 1 leaves; queue 2 3.
- **Exam point:** rear moves on insertion, front on deletion.

### Sequential implementation
- **Means:** queue in an array.
- **Key facts:** enqueue `if (rear == MAX-1) overflow; if (front == -1) front = 0; q[++rear] = x;`; dequeue `x = q[front++]` (reset both to −1 when it becomes empty).
- **Example:** MAX 5: insert 5 items, delete 2 → rear = 4 → "full" though 2 cells are free.
- **Exam point:** this wasted space is why **circular queues** exist.

### Linked implementation
- **Means:** queue as a linked list – front = head, rear = tail.
- **Key facts:** enqueue at tail, dequeue at head, both O(1); no fixed size.
- **Example:** enqueue: `rear->next = t; rear = t;`
- **Exam point:** when the last node is removed set rear = NULL too.

### Circular queues
- **Means:** array queue whose end wraps to the start.
- **Key facts:** rear = (rear + 1) % N; front = (front + 1) % N; full when (rear + 1) % N == front; count = (rear − front + N) % N + 1.
- **Example:** N = 5, front 2, rear 4 → enqueue goes to index 0.
- **Exam point:** reuses freed cells, so no false "full".

### Priority queues
- **Means:** each element has a priority; the highest priority is removed first (FIFO among equals).
- **Key facts:** ascending (smallest first) or descending; best implemented with a **heap** (insert and delete O(log n)); sorted list gives O(n) insert, O(1) delete.
- **Example:** hospital emergency room; CPU scheduling by priority.
- **Exam point:** a priority queue is not strictly FIFO.

### Deques
- **Means:** double-ended queue – insert and delete at **both** ends.
- **Key facts:** **input-restricted** (insert at one end, delete at both) and **output-restricted** (delete at one end, insert at both); can act as stack or queue.
- **Example:** browser history with limited size; sliding-window maximum.
- **Exam point:** pronounced "deck"; not the same as dequeue (the operation).

### Applications of queues
- **Means:** where FIFO order is needed.
- **Key facts:** CPU/printer scheduling, **BFS** of graphs, level-order tree traversal, keyboard and I/O buffers, call centres, round robin (circular), simulation of waiting lines, Josephus problem.
- **Example:** BFS from A visits neighbours in the order they were queued.
- **Exam point:** BFS uses a queue, DFS uses a stack."""}],

    "Trees – Binary Trees": [{"title": W + "Binary trees", "md": """> **Syllabus:** Binary trees, sequential and linked representation, insertion and deletion on binary trees, binary tree traversal

### Binary trees
- **Means:** a tree in which every node has **at most two** children (left and right).
- **Key facts:** max nodes at level l = 2ˡ; max nodes with height h = 2ʰ⁺¹ − 1; leaves n₀ = n₂ + 1; n nodes → n + 1 NULL links; full, complete, perfect, skewed binary trees; distinct shapes with 3 nodes = 5.
- **Example:** expression (a + b) × c as a tree with × at the root.
- **Exam point:** a binary tree of height 3 has at most 15 nodes.

### Sequential representation
- **Means:** storing a binary tree in an **array**.
- **Key facts:** root at index 1 → children of i at **2i** and **2i + 1**, parent at ⌊i/2⌋ (0-based: 2i + 1, 2i + 2, ⌊(i − 1)/2⌋); efficient for complete trees (heaps); wasteful for skewed trees (height h needs 2ʰ⁺¹ − 1 cells).
- **Example:** A(1), B(2), C(3), D(4), E(5) → children of B are D and E.
- **Exam point:** a right-skewed tree of 4 nodes needs 15 array cells.

### Linked representation
- **Means:** each node = data + left pointer + right pointer.
- **Key facts:** `struct tnode { int data; struct tnode *left, *right; };`; no wasted cells; root pointer; parent pointer optional.
- **Example:** leaf: left = right = NULL.
- **Exam point:** n nodes have 2n pointers, of which n − 1 are used and n + 1 are NULL.

### Insertion on binary trees
- **Means:** adding a node.
- **Key facts:** general binary tree: insert at the first free position in level order (keeps it complete); **binary search tree**: compare with root, go left if smaller, right if larger, attach at a NULL link – O(h).
- **Example:** BST insert 50, 30, 70, 20, 40 → 30 and 70 children of 50; 20, 40 under 30.
- **Exam point:** inserting sorted data into a BST makes a skewed tree (O(n)).

### Deletion on binary trees
- **Means:** removing a node while keeping the tree valid.
- **Key facts:** BST: **leaf** → remove; **one child** → link the child to the parent; **two children** → replace with the **inorder successor** (smallest in right subtree) or predecessor, then delete that one. General tree: replace with the deepest-rightmost node, delete that.
- **Example:** delete 30 (children 20, 40) → 40 replaces 30 (if 40 has no left child).
- **Exam point:** the inorder successor has no left child.

### Binary tree traversal
- **Means:** visiting every node exactly once.
- **Key facts:** **preorder** (root, left, right), **inorder** (left, root, right), **postorder** (left, right, root), **level order** (queue); recursive ones use a stack; each O(n).
- **Example:** tree A(B(D, E(G)), C(–, F)): pre A B D E G C F · in D B G E A C F · post D G E B F C A · level A B C D E F G.
- **Exam point:** inorder of a BST is **sorted**; inorder + preorder rebuilds a unique tree."""}],

    "Graphs": [{"title": W + "Graphs", "md": """> **Syllabus:** Concepts, sequential and linked representation of graphs, BFS and DFS traversal

### Concepts
- **Means:** G = (V, E) – vertices joined by edges; models networks.
- **Key facts:** directed/undirected, weighted, degree (in/out), path, cycle, connected graph, complete graph (n(n − 1)/2 edges), tree = connected acyclic graph with n − 1 edges; Σ degree = 2|E|.
- **Example:** cities (vertices) and roads (edges).
- **Exam point:** an undirected graph with 6 vertices has at most 15 edges.

### Sequential representation (adjacency matrix)
- **Means:** an n × n matrix with A[i][j] = 1 (or the weight) if edge i–j exists.
- **Key facts:** space **O(V²)**; edge check O(1); symmetric for undirected graphs; row sum = degree (out-degree for directed); good for **dense** graphs.
- **Example:** edges A–B, A–C → row A: 0 1 1.
- **Exam point:** a graph with V vertices always needs V² cells, however few edges.

### Linked representation (adjacency list)
- **Means:** an array of lists – each vertex lists its neighbours.
- **Key facts:** space **O(V + E)**; listing neighbours is fast; edge check O(degree); good for **sparse** graphs; undirected edge appears in two lists.
- **Example:** A → B → C; B → A → D → E.
- **Exam point:** total list nodes = 2E (undirected) or E (directed).

### BFS traversal
- **Means:** breadth-first search – visit a vertex, then all its neighbours, then their neighbours (level by level).
- **Key facts:** uses a **queue** and a visited array; O(V + E) with lists; finds shortest paths (fewest edges) in unweighted graphs; gives a BFS tree.
- **Example:** edges A–B, A–C, B–D, B–E, C–F, E–F, start A → **A B C D E F**.
- **Exam point:** BFS ↔ level-order traversal of a tree.

### DFS traversal
- **Means:** depth-first search – go as deep as possible along one path, then backtrack.
- **Key facts:** uses a **stack** (or recursion); O(V + E); used for cycle detection, topological sort, connected components, maze solving.
- **Example:** same graph from A (neighbours in alphabetical order) → **A B D E F C**.
- **Exam point:** DFS ↔ preorder traversal of a tree."""}],

    "Searching and Sorting": [{"title": W + "Searching and sorting", "md": """> **Syllabus:** Linear and binary search; selection, insertion, quick and merge sort

### Linear search
- **Means:** check elements one by one from the start until found.
- **Key facts:** works on unsorted data and linked lists; best 1 comparison, worst n, average (n + 1)/2 → O(n).
- **Example:** find 7 in [4, 9, 7, 1] → found at the 3rd comparison.
- **Exam point:** the only choice for unsorted, unindexed data.

### Binary search
- **Means:** on a **sorted** array, compare with the middle and discard half each time.
- **Key facts:** mid = (low + high)/2; O(log n); max comparisons ⌊log₂ n⌋ + 1 (1024 items → 11); needs random access (not linked lists).
- **Example:** [3, 8, 15, 23, 42, 56, 71, 89, 94], find 71 → mid 42 → right half → mid 71 found (2 comparisons).
- **Exam point:** `low + (high − low)/2` avoids integer overflow.

### Selection sort
- **Means:** repeatedly select the **minimum** of the unsorted part and swap it to the front.
- **Key facts:** n − 1 passes; n(n − 1)/2 comparisons always → O(n²) in every case; at most n − 1 swaps (fewest swaps); not stable; in-place.
- **Example:** 64 25 12 22 11 → 11 25 12 22 64 → 11 12 25 22 64 → 11 12 22 25 64.
- **Exam point:** best when swaps (writes) are expensive.

### Insertion sort
- **Means:** take the next element and insert it into its place in the sorted left part (like arranging cards).
- **Key facts:** best O(n) (already sorted), worst O(n²) (reverse sorted); stable; in-place; online (works as data arrives); good for small or nearly sorted lists.
- **Example:** 64 25 12 22 11 → 25 64 | … → 12 25 64 | … → 12 22 25 64 | 11 → 11 12 22 25 64.
- **Exam point:** number of shifts = number of inversions.

### Quick sort
- **Means:** divide and conquer – choose a **pivot**, partition into smaller-than and larger-than parts, sort each part recursively (C. A. R. Hoare, 1960).
- **Key facts:** average/best O(n log n); **worst O(n²)** (sorted input with first/last pivot); not stable; in-place; O(log n) stack on average; Lomuto and Hoare partition schemes.
- **Example:** [10, 80, 30, 90, 40, 50, 70], pivot 70 → [10, 30, 40, 50, **70**, 90, 80].
- **Exam point:** after one partition the pivot is in its **final** position.

### Merge sort
- **Means:** divide and conquer – split into halves, sort each, **merge** the sorted halves (John von Neumann, 1945).
- **Key facts:** O(n log n) in every case; T(n) = 2T(n/2) + n; **stable**; needs O(n) extra space; best for linked lists and external sorting.
- **Example:** [38, 27, 43, 3] → [27, 38] + [3, 43] → [3, 27, 38, 43].
- **Exam point:** merging two sorted lists of sizes m and n takes at most m + n − 1 comparisons."""}],
}
