"""P2 · Unit 8 – Data Structures & Algorithms · detailed revision NOTES for all ten topics (no new questions).
Owner's request (19 Oct 2026): "continue CS notes, detailed". Every worked example (LCS, knapsack, matrix chain, Huffman,
activity selection, hashing, AVL, Floyd–Warshall, max-flow, N-queens, coin change, traversals, MST, Dijkstra, sorting passes)
was computed with a script on 19 Oct 2026. Facts follow Cormen et al. (CLRS) and Horowitz–Sahni."""

TOPICS = {}  # notes only – question sets come from p2u8_a … p2u8_f

NOTES = {
    "Linear Data Structures": [{"title": "Linear data structures – detailed notes", "md": """## Arrays
- Contiguous, O(1) access; row-major address Base + w × ((i − LR) × N + (j − LC)); column-major Base + w × ((j − LC) × M + (i − LR))
- Insertion/deletion O(n) (shifting)
- **Sparse matrix**: store non-zeros as (row, col, value) triplets – first row (rows, cols, count); transpose in O(cols + terms) with the fast-transpose method; linked representation with row/column header lists
- Special matrices: lower/upper triangular n(n + 1)/2 elements, tridiagonal 3n − 2, diagonal n
- Polynomials: arrays of coefficients or (coef, exp) pairs

## Stacks (LIFO)
- push/pop/peek O(1); array (top = −1 empty, MAX − 1 full) or linked (top = head)
- Applications: function calls/recursion, **infix → postfix/prefix**, postfix evaluation, bracket matching, backtracking, DFS, undo
- A + B * C − D → A B C * + D −; (A + B) * (C − D) → A B + C D − *; prefix of (A + B) * C = * + A B C
- Postfix 2 3 4 * + 5 − = 9; number of stack permutations of n = Catalan(n) (1, 2, 5, 14, 42)
- Two stacks in one array of size n grow from the ends – overflow only when the array is full

## Queues (FIFO)
- Linear array queue wastes space → **circular queue**: rear = (rear + 1) % N, full when (rear + 1) % N == front (one slot kept empty) → holds N − 1 items
- **Deque** (both ends; input-/output-restricted); **priority queue** – binary heap: insert and delete-max O(log n), build-heap O(n)
- Queue with two stacks: amortised O(1); stack with two queues: one operation O(n)
- Applications: BFS, scheduling, buffers, simulation

## Linked lists
| Operation | Singly | Doubly | Circular (tail pointer) |
|---|---|---|---|
| Insert at head | O(1) | O(1) | O(1) |
| Insert at tail | O(n) (O(1) with tail) | O(1) with tail | O(1) |
| Delete given node | O(n) | **O(1)** | O(n) |
| Search | O(n) | O(n) | O(n) |
- Reverse (three pointers), middle (slow/fast), cycle detection (**Floyd's tortoise and hare**), merge two sorted lists O(m + n), header nodes, XOR lists (memory-efficient doubly)
- Sentinel/header node removes special cases for the empty list
- Linked list vs array: no random access, no shifting, extra pointer memory, poor cache locality

## Traps
- A circular queue implemented with "one empty slot" holds N − 1 elements
- Deleting a node in a singly linked list needs its predecessor
- Binary search on a linked list is O(n)"""}],

    "Trees": [{"title": "Trees, BST and AVL – detailed notes", "md": """## Trees and forests
- Tree with n nodes has **n − 1 edges**; degree of a node = number of children; degree of a tree = max degree; leaf, internal node, level, height, depth
- **Forest** = set of disjoint trees; a forest ↔ binary tree conversion: **left child = first child, right child = next sibling** (left-child right-sibling representation)
- k-ary tree with n internal nodes has kn + 1 total nodes (full k-ary) → leaves = (k − 1)n + 1

## Binary trees
- Max nodes at level i (root level 0) = 2ⁱ; height h → max 2ʰ⁺¹ − 1 nodes; n nodes → min height ⌈log₂(n + 1)⌉ − 1
- **n₀ = n₂ + 1**; n + 1 NULL links; distinct binary trees with n nodes = Catalan(n) = (2n)!/((n + 1)! n!)
- Complete binary tree in an array: children of i at 2i and 2i + 1 (1-based)
- Traversals: preorder, inorder, postorder (stack/recursion, O(n)), level order (queue)
  - Tree A(B(D, E(G)), C(–, F)): pre A B D E G C F · in D B G E A C F · post D G E B F C A
- Inorder + preorder (or postorder) → unique tree; preorder + postorder only for full binary trees
- Expression trees: postorder = postfix

## Threaded binary trees
- NULL right pointers point to the **inorder successor**, NULL left pointers to the **inorder predecessor**; a flag bit distinguishes threads from child links
- Inorder traversal without stack or recursion; a header node avoids dangling end threads

## Binary search trees
- left < root < right; inorder = sorted
- Search/insert/delete **O(h)**: O(log n) balanced, **O(n) skewed** (sorted insertions)
- Insert 50, 30, 70, 20, 40, 60, 80, 35 → preorder 50 30 20 40 35 70 60 80; postorder 20 35 40 30 60 80 70 50; height 3
- Delete: leaf / one child / two children (replace with inorder successor – leftmost of right subtree)
- Number of BSTs with n distinct keys = Catalan(n) (3 keys → 5)
- Min = leftmost, max = rightmost; floor/ceil, k-th smallest by inorder

## AVL trees (Adelson-Velsky and Landis, 1962)
- Balance factor = h(left) − h(right) ∈ {−1, 0, +1} at every node → height ≤ 1.44 log₂ n → all operations O(log n)
- Rotations after insertion: **LL** → single right rotation; **RR** → single left; **LR** → left then right (double); **RL** → right then left
- Insert 10, 20, 30, 40, 50, 25:
  - 30 makes RR at 10 → left rotate → 20(10, 30)
  - 50 makes RR at 30 → 20(10, 40(30, 50))
  - 25 makes RL at 20 → final preorder **30 20 10 25 40 50**
- Minimum nodes in an AVL tree of height h: N(h) = N(h − 1) + N(h − 2) + 1 → 1, 2, 4, 7, 12, 20 (h = 0 … 5)
- Insertion needs at most one (single or double) rotation; deletion may need O(log n) rotations
- Other balanced trees: red-black (height ≤ 2 log₂(n + 1), fewer rotations), B-trees (order m: up to m children, used in databases/file systems; B+ trees keep data in linked leaves), splay trees, 2-3 trees

## Heaps
- Complete binary tree with heap order (max-heap: parent ≥ children); insert/delete O(log n); build O(n) by bottom-up heapify
- Build max-heap from [4, 10, 3, 5, 1] → [10, 5, 3, 4, 1]

## Traps
- A BST built from sorted input is a chain (height n − 1)
- AVL balance is checked from the inserted node upward; the **first** unbalanced ancestor is rotated
- Threaded trees remove the need for a stack in inorder traversal"""}],

    "Sets & Graph Representation": [{"title": "Sets (disjoint sets) and graph representation – detailed notes", "md": """## Data structures for sets
- Bit vector (universe small): union = OR, intersection = AND – O(n/w)
- Sorted list/array: union and intersection by merging O(m + n); hash set: average O(1) membership
- **Disjoint-set (union–find)**: Make-Set, **Find** (which set?), **Union** (merge sets)
  - Linked-list representation: union by appending the shorter list (weighted union) → O(m + n log n)
  - **Forest representation** with **union by rank (size)** and **path compression** → almost constant amortised time, O(m α(n)) – α is the inverse Ackermann function (≤ 4 in practice)
  - Union by rank alone keeps tree height ≤ log₂ n
  - Uses: **Kruskal's MST**, connected components, cycle detection in undirected graphs, equivalence of names

Worked union–find: sets {1} … {6}; Union(1, 2), Union(3, 4), Union(2, 4) → {1, 2, 3, 4}, {5}, {6}; Find(3) = Find(1) → same set

## Graph terminology
- Simple graph, multigraph (parallel edges), pseudograph (loops); directed/undirected; weighted
- Degree; Σ deg = 2|E|; in-degree/out-degree sums equal |E|
- Path, simple path, cycle; connected, strongly/weakly connected (digraphs); complete graph Kₙ has n(n − 1)/2 edges; DAG
- Tree = connected, acyclic, n − 1 edges; spanning tree; forest

## Graph representation
| | Adjacency matrix | Adjacency list | Incidence matrix |
|---|---|---|---|
| Space | O(V²) | O(V + E) | O(V × E) |
| Is (u, v) an edge? | O(1) | O(deg u) | O(E) |
| List neighbours of u | O(V) | O(deg u) | O(E) |
| Add edge | O(1) | O(1) | rebuild |
| Best for | dense graphs | sparse graphs | rarely used |
- Undirected adjacency matrix is symmetric; diagonal 0 for simple graphs; (A²)ᵢⱼ = number of walks of length 2 from i to j
- Adjacency list of an undirected graph has 2E entries; directed graph E entries
- Edge list (array of (u, v, w)) – handy for Kruskal and Bellman–Ford
- Orthogonal / multilist representation for sparse directed graphs

## Traps
- Union by rank + path compression makes Find nearly O(1), not exactly O(1)
- Matrix space does not depend on E
- For dense graphs (E ≈ V²) the matrix is as compact as lists"""}],

    "Sorting and Searching": [{"title": "Sorting and searching – detailed notes", "md": """## Searching
| Method | Needs | Time |
|---|---|---|
| Linear | nothing | O(n); average (n + 1)/2 comparisons for a successful search |
| **Binary** | sorted, random access | O(log n); ⌊log₂ n⌋ + 1 comparisons worst |
| Interpolation | sorted, uniform data | O(log log n) average, O(n) worst |
| Jump search | sorted | O(√n) |
| Exponential | sorted, unbounded | O(log n) |
| Hashing | hash table | O(1) average |
| BST / balanced tree | tree | O(h) / O(log n) |
- Binary search on [3, 8, 15, 23, 42, 56, 71, 89, 94]: 71 found in 2 comparisons (42, then 71); 10 not found after 3 (42, 8, 15)

## Elementary sorts (on 64 25 12 22 11)
- **Bubble**: 25 12 22 11 64 → 12 22 11 25 64 → 12 11 22 25 64 → 11 12 22 25 64
- **Selection**: 11 25 12 22 64 → 11 12 25 22 64 → 11 12 22 25 64 → 11 12 22 25 64
- **Insertion**: 25 64 12 22 11 → 12 25 64 22 11 → 12 22 25 64 11 → 11 12 22 25 64
- Shell sort: insertion sort on gaps (n/2, n/4 … 1) – about O(n^1.25 … n^1.5)

## Advanced sorts
- **Merge sort**: T(n) = 2T(n/2) + n → Θ(n log n) always; stable; O(n) extra space; good for linked lists and external sorting
- **Quick sort**: partition around a pivot; average Θ(n log n), worst Θ(n²) (already sorted with first/last pivot); randomised/median-of-three pivots avoid the worst case; not stable; in place
  - Lomuto partition of [10, 80, 30, 90, 40, 50, 70] with pivot 70 → [10, 30, 40, 50, 70, 90, 80]
- **Heap sort**: build max-heap O(n), n − 1 extract-max O(log n) → O(n log n) always; in place; not stable
- **Counting sort** O(n + k) (keys 0..k), stable; **radix sort** O(d(n + k)) – sorts digit by digit (least significant first) with a stable sort; **bucket sort** O(n) average for uniform data
- **Lower bound**: any comparison sort needs **Ω(n log n)** comparisons (decision-tree argument: log₂(n!) leaves)

| Sort | Best | Avg | Worst | Space | Stable | In place |
|---|---|---|---|---|---|---|
| Bubble (with flag) | n | n² | n² | 1 | ✓ | ✓ |
| Selection | n² | n² | n² | 1 | ✗ | ✓ |
| Insertion | n | n² | n² | 1 | ✓ | ✓ |
| Merge | n log n | n log n | n log n | n | ✓ | ✗ |
| Quick | n log n | n log n | n² | log n | ✗ | ✓ |
| Heap | n log n | n log n | n log n | 1 | ✗ | ✓ |
| Counting | n + k | n + k | n + k | n + k | ✓ | ✗ |
| Radix | d(n + k) | d(n + k) | d(n + k) | n + k | ✓ | ✗ |

## Traps
- Selection sort makes O(n) swaps – the fewest
- Insertion sort is O(n) on already sorted input and is used inside hybrid sorts (TimSort, introsort) for small parts
- Merge sort is the usual answer for "stable O(n log n)"; heap sort for "in-place O(n log n) worst case\""""}],

    "Hashing": [{"title": "Hashing – detailed notes with probing traces", "md": """## Hash functions
- Map a key to a table index 0 … m − 1; good hash = fast, uniform, uses all of the key
- **Division**: h(k) = k mod m (m a prime not close to a power of 2)
- **Multiplication**: h(k) = ⌊m (kA mod 1)⌋, A ≈ (√5 − 1)/2 = 0.618 (Knuth)
- **Mid-square** (square, take middle digits), **folding** (split key into parts and add), digit analysis; universal hashing (random function from a family)
- Load factor **α = n/m**

## Collision resolution
**Separate chaining**: each slot holds a linked list – average search 1 + α; α may exceed 1; deletion easy
**Open addressing** (all keys in the table, α ≤ 1):
| Probe | Sequence | Problem |
|---|---|---|
| Linear | h(k) + i | **primary clustering** |
| Quadratic | h(k) + c₁i + c₂i² | **secondary clustering**; may not reach every slot |
| Double hashing | h₁(k) + i·h₂(k) | best spread; h₂(k) ≠ 0 and coprime with m |
- Deletion needs a "deleted" marker (tombstone) so searches don't stop early
- Expected probes (uniform hashing): unsuccessful ≤ 1/(1 − α); successful ≤ (1/α) ln(1/(1 − α)) – at α = 0.5: 2 and ≈ 1.39

## Worked: m = 11, h(k) = k mod 11, insert 10, 22, 31, 4, 15, 28, 17, 88, 59
- **Linear probing** → slot: 0:22, 1:88, 4:4, 5:15, 6:28, 7:17, 8:59, 9:31, 10:10 (2 and 3 empty)
  - 15 → 4 taken → 5; 17 → 6 taken → 7; 88 → 0 taken → 1; 59 → 4, 5, 6, 7 taken → 8
- **Quadratic** (h + i²) gives the same table here (59: 4 → 5 → 8)
- **Double hashing** with h₂(k) = 1 + (k mod 10): 0:22, 2:59, 3:17, 4:4, 5:15, 6:28, 7:88, 9:31, 10:10
  - 17: h = 6 taken, h₂ = 8 → 14 mod 11 = 3; 88: h = 0 taken, h₂ = 9 → 9 taken (31) → 18 mod 11 = 7; 59: 4 taken, h₂ = 10 → 14 mod 11 = 3 taken → 24 mod 11 = 2

## Other ideas
- **Rehashing**: when α grows too large, build a bigger table (≈ 2m, prime) and reinsert – amortised O(1)
- **Perfect hashing** (static key sets, two-level), cuckoo hashing, extendible/linear hashing (databases)
- Applications: symbol tables in compilers, database indexes, caches, sets/dictionaries, password storage (cryptographic hashes – different purpose)

## Traps
- Chaining tolerates α > 1; open addressing needs α < 1
- Linear probing → primary clustering; quadratic → secondary clustering
- Worst-case search in any hash table is O(n)"""}],

    "Performance Analysis & Recurrences": [{"title": "Performance analysis and recurrences – detailed notes", "md": """## Measuring algorithms
- **A priori** analysis (count operations, machine independent) vs **a posteriori** testing (run and time)
- Time complexity counts basic steps as a function of n; space complexity = fixed part + variable part (incl. recursion stack)
- Best, worst, average case; **amortised** analysis (aggregate, accounting, potential methods) – e.g. dynamic array append amortised O(1)

## Asymptotic notation
| Notation | Meaning | Definition |
|---|---|---|
| O(g) | upper bound | f ≤ c·g for n ≥ n₀ |
| Ω(g) | lower bound | f ≥ c·g |
| Θ(g) | tight bound | both |
| o(g) | strictly smaller | f/g → 0 |
| ω(g) | strictly larger | f/g → ∞ |
- Order: 1 < log log n < log n < (log n)² < √n < n < n log n < n² < n³ < 2ⁿ < 3ⁿ < n! < nⁿ
- 2ⁿ⁺¹ = O(2ⁿ) but 2²ⁿ ≠ O(2ⁿ); log(n!) = Θ(n log n); Σ1/i = Θ(log n); Σi = Θ(n²); Σi² = Θ(n³)
- Polynomial: degree decides (5n³ + 2n = Θ(n³))

## Loop analysis
- `for (i = 1; i <= n; i *= 2)` → log n; `for (i = 1; i <= n; i++) for (j = 1; j <= n; j += i)` → n(1 + 1/2 + … ) = **n log n**
- `for (i = 1; i <= n; i++) for (j = 1; j <= i * i; j++)` → Σi² = Θ(n³)
- `while (n > 1) n = n / 2;` → Θ(log n); `while (n > 1) n = √n;` → Θ(log log n)

## Recurrence relations – methods
1. **Substitution** – guess and prove by induction
2. **Recursion tree** – sum the cost of each level
3. **Master theorem** – T(n) = aT(n/b) + f(n), a ≥ 1, b > 1; compare f(n) with n^(log_b a):
   - Case 1: f = O(n^(log_b a − ε)) → Θ(n^(log_b a))
   - Case 2: f = Θ(n^(log_b a)) → Θ(n^(log_b a) log n)
   - Case 3: f = Ω(n^(log_b a + ε)) and regularity → Θ(f(n))
4. Characteristic equation for linear recurrences (Fibonacci: r² = r + 1 → φⁿ)

## Worked recurrences
| Recurrence | Answer | Reason |
|---|---|---|
| T(n) = T(n/2) + 1 | Θ(log n) | binary search, case 2 |
| T(n) = 2T(n/2) + n | Θ(n log n) | merge sort, case 2 |
| T(n) = 2T(n/2) + 1 | Θ(n) | case 1 |
| T(n) = 4T(n/2) + n | Θ(n²) | case 1 (n^log₂4 = n²) |
| T(n) = 4T(n/2) + n² | Θ(n² log n) | case 2 |
| T(n) = 4T(n/2) + n³ | Θ(n³) | case 3 |
| T(n) = 7T(n/2) + n² | Θ(n^2.81) | Strassen, case 1 |
| T(n) = 3T(n/4) + n log n | Θ(n log n) | case 3 |
| T(n) = T(n − 1) + n | Θ(n²) | sum 1 … n |
| T(n) = T(n − 1) + 1 | Θ(n) | |
| T(n) = 2T(n − 1) + 1 | Θ(2ⁿ) | Tower of Hanoi |
| T(n) = T(n − 1) + T(n − 2) | Θ(φⁿ) ≈ 1.618ⁿ | naive Fibonacci |
| T(n) = T(√n) + 1 | Θ(log log n) | substitution m = log n |
| T(n) = 2T(n/2) + n log n | Θ(n log² n) | extended case 2 (not the basic master theorem) |

## Traps
- The master theorem does not apply to T(n) = T(n − 1) + n (not of the form n/b)
- O gives an upper bound only; "the algorithm is O(n²)" is true even if it is Θ(n)
- Average case ≠ amortised cost"""}],

    "Design Techniques – Divide & Conquer, Greedy": [{"title": "Divide and conquer, greedy – detailed notes", "md": """## Divide and conquer
**Divide** into smaller subproblems → **conquer** recursively → **combine**.
| Algorithm | Recurrence | Time |
|---|---|---|
| Binary search | T(n/2) + 1 | O(log n) |
| Merge sort | 2T(n/2) + n | O(n log n) |
| Quick sort | T(k) + T(n − k − 1) + n | O(n log n) avg, O(n²) worst |
| Max–min of an array | 2T(n/2) + 2 | **3n/2 − 2** comparisons |
| Strassen matrix multiplication | 7T(n/2) + n² | O(n^2.81) (naive 8 multiplications → n³) |
| Karatsuba multiplication | 3T(n/2) + n | O(n^1.585) |
| Closest pair of points | 2T(n/2) + n log n / n | O(n log n) |
| Power xⁿ | T(n/2) + 1 | O(log n) |

## Greedy method
Make the **locally best** choice at each step, never reconsider; works when the problem has the **greedy-choice property** and **optimal substructure** (proof by exchange argument or matroids).

**Fractional knapsack** – sort by value/weight, take greedily: W = 50, items (60, 10), (100, 20), (120, 30) → ratios 6, 5, 4 → take 10 + 20 fully and 20/30 of the last → **240**. (Greedy fails for 0/1 knapsack: best there is 220.)

**Activity selection** – sort by finish time, pick each activity starting after the last finish:
(1, 4) (3, 5) (0, 6) (5, 7) (3, 9) (5, 9) (6, 10) (8, 11) (8, 12) (2, 14) (12, 16) → **(1, 4), (5, 7), (8, 11), (12, 16)** = 4 activities

**Huffman coding** – merge the two least frequent nodes repeatedly:
a 5, b 9, c 12, d 13, e 16, f 45 → codes f 0, c 100, d 101, a 1100, b 1101, e 111 → **224 bits** for 100 characters (fixed 3-bit code needs 300); prefix-free; O(n log n) with a heap

Other greedy algorithms: **Kruskal** and **Prim** (MST), **Dijkstra** (shortest paths, non-negative weights), job sequencing with deadlines, optimal merge pattern, coin change for canonical systems (₹1, 2, 5, 10 …)
- Greedy coin change fails for coins {1, 3, 4}, amount 6: greedy 4 + 1 + 1 (3 coins) vs optimal 3 + 3 (2 coins)

## Divide and conquer vs greedy vs DP
| | Subproblems | Choice |
|---|---|---|
| Divide & conquer | independent | solve all |
| Dynamic programming | **overlapping** | try all, store results |
| Greedy | one at a time | best-looking, never revisit |

## Traps
- Greedy works for fractional knapsack, not 0/1
- Strassen uses 7 multiplications of half-size matrices
- Huffman codes are optimal prefix codes; the most frequent symbol gets the shortest code"""}],

    "Design Techniques – DP, Backtracking, Branch & Bound": [{"title": "Dynamic programming, backtracking, branch and bound – detailed notes", "md": """## Dynamic programming (Richard Bellman, 1950s)
Needs **optimal substructure** + **overlapping subproblems**; store answers (memoisation top-down, or tabulation bottom-up).
| Problem | Recurrence | Time |
|---|---|---|
| Fibonacci | F(n) = F(n − 1) + F(n − 2) | O(n) instead of O(2ⁿ) |
| **0/1 knapsack** | K[i][w] = max(K[i−1][w], vᵢ + K[i−1][w − wᵢ]) | O(nW) (pseudo-polynomial) |
| **LCS** | equal chars → L[i−1][j−1] + 1, else max(L[i−1][j], L[i][j−1]) | O(mn) |
| **Matrix chain** | m[i][j] = min over k (m[i][k] + m[k+1][j] + pᵢ₋₁pₖpⱼ) | O(n³) |
| Floyd–Warshall | D[i][j] = min(D[i][j], D[i][k] + D[k][j]) | O(V³) |
| Bellman–Ford | relax all edges V − 1 times | O(VE) |
| Coin change (min coins) | C[a] = 1 + min C[a − c] | O(amount × coins) |
| Optimal BST, edit distance, TSP (Held–Karp O(n²2ⁿ)), longest increasing subsequence | | |

Worked
- **0/1 knapsack** W = 50, (60, 10), (100, 20), (120, 30) → **220** (items 2 and 3)
- **LCS**("ABCBDAB", "BDCABA") = **4** (e.g. BCBA)
- **Matrix chain** 10×30, 30×5, 5×60 → (A₁A₂)A₃ = 10·30·5 + 10·5·60 = **4500** (other order 27,000); dims 40, 20, 30, 10, 30 → **26,000**
- **Coin change** coins {1, 2, 5}, amount 11 → **3** coins (5 + 5 + 1)
- **Floyd–Warshall** on 4 vertices with edges 1→2 (3), 1→4 (7), 2→1 (8), 2→3 (2), 3→1 (5), 3→4 (1), 4→1 (2) → shortest from 1: to 2 = 3, to 3 = 5, to 4 = 6

## Backtracking
Build a solution step by step; abandon (**prune**) a partial solution as soon as it can't succeed; explores the **state-space tree** depth-first.
- **N-queens**: 4-queens has **2** solutions, 8-queens **92**
- Sum of subsets, graph colouring (m-colouring), Hamiltonian cycle, Sudoku, maze solving
- Bounding function decides pruning; worst case still exponential

## Branch and bound
Explores the state-space tree (often breadth-first / **least-cost** first with a priority queue), using **bounds** to discard nodes that cannot beat the best solution found so far.
- Used for optimisation: 0/1 knapsack, **travelling salesman** (reduced cost matrix), job assignment, 15-puzzle (LC search)
- FIFO B&B, LIFO B&B, least-cost (LC) B&B

| | Backtracking | Branch and bound |
|---|---|---|
| Goal | any/all feasible solutions | optimal solution |
| Search | DFS | BFS / best-first |
| Pruning | feasibility | bounds (cost) |

## Traps
- DP needs overlapping subproblems; merge sort has none → divide and conquer
- 0/1 knapsack DP is pseudo-polynomial (depends on W's value)
- Matrix-chain DP finds the order, not the product itself"""}],

    "Graph Algorithms": [{"title": "Graph algorithms – detailed notes", "md": """## BFS and DFS
- **BFS** (queue): O(V + E); shortest path in edges for unweighted graphs; BFS tree; bipartiteness test
- **DFS** (stack/recursion): O(V + E); discovery/finish times; edge types – **tree, back, forward, cross**; a **back edge ⇔ cycle**
- Graph with edges A–B, A–C, B–D, B–E, C–F, E–F from A: BFS A B C D E F; DFS A B D E F C
- Applications of DFS: **topological sort** (decreasing finish time; DAG only), **strongly connected components** (Kosaraju – two DFS passes; Tarjan), articulation points and bridges, cycle detection

## Single-source shortest paths
| Algorithm | Weights | Time |
|---|---|---|
| BFS | unweighted | O(V + E) |
| **Dijkstra** (greedy) | **non-negative** | O((V + E) log V) with a binary heap, O(V²) with an array |
| **Bellman–Ford** (DP) | negative allowed; detects negative cycles | O(VE) |
| DAG shortest path | any, no cycles | O(V + E) (topological order) |
- Relaxation: if d[u] + w(u, v) < d[v] then d[v] = d[u] + w(u, v)
- Dijkstra example (edges A–B 4, A–C 2, B–C 1, B–D 5, C–D 8, C–E 10, D–E 2, D–F 6, E–F 3) from A: C 2, B 3, D 8, E 10, F 13

## All-pairs shortest paths
**Floyd–Warshall** O(V³) (DP over intermediate vertices); Johnson's algorithm (reweighting + Dijkstra) O(V² log V + VE) for sparse graphs; **Warshall** – transitive closure

## Minimum spanning trees
- **Kruskal** (sort edges, union–find): O(E log E); **Prim** (grow from a vertex, priority queue): O(E log V)
- Same graph: Kruskal picks B–C 1, A–C 2, D–E 2, E–F 3, B–D 5 → **13**; Prim from A gets the same total
- **Cut property**: the lightest edge crossing any cut belongs to some MST; **cycle property**: the heaviest edge on a cycle is in no MST
- Borůvka's algorithm; MST is unique when all weights are distinct

## Maximum flow
- Flow network: capacities, source s, sink t; flow conservation; capacity constraint
- **Ford–Fulkerson**: repeatedly find an **augmenting path** in the residual graph; **Edmonds–Karp** uses BFS → O(VE²)
- **Max-flow min-cut theorem**: maximum flow value = capacity of the minimum s–t cut
- Example: s→a 10, s→b 5, a→b 15, a→t 10, b→t 10 → max flow **15** (min cut {s→a, s→b} = 15)
- Applications: bipartite matching, network routing, project selection

## Traps
- Dijkstra can fail with a negative edge even without negative cycles
- Topological order exists only for DAGs (there may be several)
- Prim needs a connected graph; Kruskal on a disconnected graph gives a spanning forest"""}],

    "Complexity Theory": [{"title": "P, NP and NP-completeness – detailed notes", "md": """## Decision problems and classes
- **Decision problem**: yes/no answer (optimisation problems have decision versions – "is there a tour of cost ≤ k?")
- **P**: solvable in **polynomial time** by a deterministic algorithm (sorting, shortest paths, MST, matching, 2-SAT, primality – AKS 2002, linear programming)
- **NP**: a "yes" answer can be **verified** in polynomial time given a certificate (equivalently, solvable in polynomial time by a non-deterministic machine)
- P ⊆ NP; whether **P = NP** is the biggest open question (Clay Millennium Prize)
- co-NP: "no" answers verifiable; EXP ⊇ NP; undecidable problems (halting problem) lie outside all of these

## Reductions
- A ≤ₚ B: transform any instance of A into an instance of B in polynomial time so the answers match
- If A ≤ₚ B and B ∈ P then A ∈ P; if A is hard and A ≤ₚ B then **B is at least as hard**
- To prove X NP-complete: (1) X ∈ NP, (2) reduce a **known** NP-complete problem **to X**

## NP-hard and NP-complete
- **NP-hard**: every NP problem reduces to it (may not be in NP – e.g. halting problem, optimisation TSP)
- **NP-complete** = NP-hard **and** in NP
- **Cook–Levin theorem (1971)**: **SAT** is NP-complete (the first one); Karp (1972) listed 21 NP-complete problems
- Classic NP-complete problems: SAT, **3-SAT**, CNF-SAT, clique, independent set, **vertex cover**, **Hamiltonian cycle**, **TSP (decision)**, subset sum, 0/1 knapsack (decision), **graph colouring (k ≥ 3)**, set cover, partition, bin packing
- In P: **2-SAT**, 2-colouring (bipartiteness), Euler circuit, shortest path, MST
- If any NP-complete problem has a polynomial algorithm then **P = NP**

## Coping with hardness
Approximation algorithms (vertex cover 2-approximation; metric TSP 2- or 1.5-approximation – Christofides), heuristics, branch and bound, DP for small parameters, randomised algorithms, special cases

## Traps
- NP stands for **non-deterministic polynomial**, not "non-polynomial"
- Every P problem is in NP
- An NP-hard problem need not be in NP
- Reduce **from** the known hard problem **to** the new one"""}],
}
