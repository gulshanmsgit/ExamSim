"""P2 · KRIES – Data Structures · SOLVED EXAM PROBLEMS as an extra note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". Every answer (expression conversions, tree
reconstruction, heaps, queue states, complexity counts, search/sort counts) was computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

S = "Solved exam problems – "

NOTES = {
    "Stacks": [{"title": S + "expression conversion and evaluation", "md": """### Infix → postfix
| Infix | Postfix |
|---|---|
| A + B * C − D / E | **A B C * + D E / −** |
| (A + B) * (C − D) / E | **A B + C D − * E /** |
| A * (B + C * D) + E | **A B C D * + * E +** |
| A ^ B ^ C * D | **A B C ^ ^ D *** (^ is right-associative) |
| K + L − M * N + (O ^ P) * W / U / V * T + Q | **K L + M N * − O P ^ W * U / V / T * + Q +** |

### Infix → prefix
| Infix | Prefix |
|---|---|
| A + B * C − D / E | **− + A * B C / D E** |
| (A + B) * (C − D) / E | **/ * + A B − C D E** |
| A * (B + C * D) + E | **+ * A + B * C D E** |

### Evaluation
- Postfix **5 3 + 8 2 − *** → (5 + 3) × (8 − 2) = **48**
- Prefix **− + 7 * 4 5 + 2 0** (scan right to left) → (7 + 4 × 5) − (2 + 0) = **25**
- Postfix 6 2 3 + − 3 8 2 / + * 2 ^ 3 + → 6 − 5 = 1; 8/2 = 4; 3 + 4 = 7; 1 × 7 = 7; 7² = 49; 49 + 3 = **52**

### Stack states
Push 10, 20, 30; pop; push 40; pop; pop → output **30, 40, 20**; stack holds 10.

### Maximum stack size during conversion
For A + B * C − D the operator stack reaches size **2** (+ and *).

### Tower of Hanoi
5 discs → 2⁵ − 1 = **31** moves; the largest disc moves exactly once; the smallest disc moves 2ⁿ⁻¹ = 16 times."""}],

    "Trees – Binary Trees": [{"title": S + "traversals, reconstruction, BST and heaps", "md": """### Q1. Rebuild from preorder ABDHEICFG and inorder HDBIEAFCG
- Preorder's first letter A is the root; inorder splits into HDBIE (left) and FCG (right)
- Left: preorder B D H E I → root B; inorder HD | IE → D has left child H; E has left child I
- Right: preorder C F G → root C, left F, right G
→ **Postorder H D I E B F G C A**, level order **A B C D E F G H I**, height **3**

### Q2. Rebuild from postorder DEBFCA and inorder DBEAFC
Root A (last of postorder) → left DBE (root B with D, E), right FC (root C with left F) → **preorder A B D E C F**

### Q3. BST from 50, 30, 70, 20, 40, 60, 80
- Inorder 20 30 40 50 60 70 80 (sorted); search 60 → 50 → 70 → 60 (3 comparisons)
- Delete 50 (two children) → replace with the inorder successor **60** → root 60
- Delete 30 → successor 40 replaces it

### Q4. Max-heap by inserting 15, 10, 20, 8, 25, 5 one by one
15 → [15]; 10 → [15, 10]; 20 → swaps with 15 → [20, 10, 15]; 8 → [20, 10, 15, 8]; 25 → up past 10 and 20 → [25, 20, 15, 8, 10]; 5 → **[25, 20, 15, 8, 10, 5]**
Delete max → move 5 to the root and sift down → **[20, 10, 15, 8, 5]**

### Q5. Counts
- Binary tree with 20 leaves → nodes with two children = **19**
- Complete binary tree with 100 nodes → height ⌊log₂ 100⌋ = **6**, leaves = ⌈100/2⌉ = **50**
- Distinct binary trees with 4 nodes = Catalan(4) = **14**
- Array storage (1-based): parent of node 13 = 6, children of 6 = 12 and 13"""}],

    "Queues": [{"title": S + "queue states", "md": """### Q1. Circular queue of size 5 (front = rear = −1 initially)
| Operation | front | rear | Contents |
|---|---|---|---|
| enqueue 10, 20, 30, 40, 50 | 0 | 4 | 10 20 30 40 50 – full |
| dequeue × 2 | 2 | 4 | 30 40 50 |
| enqueue 60 | 2 | **0** | 30 40 50 60 |
| enqueue 70 | 2 | 1 | 30 40 50 60 70 – full ((1 + 1) % 5 = 2 = front) |
| enqueue 80 | – | – | **overflow** |
Count = (rear − front + 5) % 5 + 1 = (1 − 2 + 5) % 5 + 1 = 5

### Q2. Linear queue of size 5
enqueue 5 items, dequeue 3 → front = 3, rear = 4 → enqueue reports **overflow** though 3 cells are free → the reason for circular queues.

### Q3. Queue using two stacks
enqueue 1, 2, 3 (push on S1) → dequeue: move 3, 2, 1 to S2 → pop **1** → enqueue 4 (S1) → dequeue pops **2** from S2.

### Q4. Priority queue (smaller number = higher priority)
Insert (A, 3), (B, 1), (C, 2), (D, 1) → delete order **B, D, C, A** (B before D – FIFO among equal priorities).

### Q5. Restricted deques (input 1, 2, 3, 4 in that order)
- **Input-restricted** (insert at the rear only, delete at both ends): 4 1 3 2 is **possible** (insert all, delete rear 4, front 1, rear 3, then 2); the only impossible orders are **4 2 1 3** and **4 2 3 1**
- **Output-restricted** (insert at both ends, delete at the front only): 3 1 2 4 is **possible** (insert 1, 2 at the rear, 3 at the front, delete 3, 1, 2, then insert and delete 4); the only impossible orders are **4 1 3 2** and **4 2 3 1**
- A plain stack allows 14 of the 24 orders; a plain queue only 1 (1 2 3 4)"""}],

    "Searching and Sorting": [{"title": S + "counting comparisons and passes", "md": """### Q1. Binary search on 1000 sorted items
Maximum comparisons = ⌊log₂ 1000⌋ + 1 = **10**; for 1024 items → 11; linear search worst case 1000, average ≈ 500.

### Q2. Binary search trace
[3, 8, 15, 23, 42, 56, 71, 89, 94]: search 23 → mid index 4 (42) → left half 0–3, mid 1 (8) → right 2–3, mid 2 (15) → right 3–3, mid 3 (23) found → **4 comparisons**

### Q3. Bubble sort counts
n = 6 → passes 5, comparisons 15 (n(n − 1)/2); already sorted with the swap flag → 1 pass, 5 comparisons. Reverse-sorted 5 elements → 10 swaps.

### Q4. Insertion sort shifts = number of inversions
[3, 1, 2] has inversions (3,1), (3,2) → **2 shifts**; [5, 4, 3, 2, 1] → 10.

### Q5. Selection sort swaps
At most n − 1 = 4 swaps for 5 elements – the fewest of the simple sorts.

### Q6. Quick sort partition
[10, 80, 30, 90, 40, 50, 70], pivot 70 (last) → [10, 30, 40, 50, **70**, 90, 80]; worst case on sorted input: n(n − 1)/2 = 21 comparisons for 7 items.

### Q7. Merge sort
Merging [3, 27, 38] and [9, 43, 82] → 3, 9, 27, 38, 43, 82 with at most 3 + 3 − 1 = **5** comparisons; merge sort on 8 items needs 3 levels (log₂ 8).

### Q8. Which sort?
Nearly sorted data → insertion; stable O(n log n) → merge; in-place O(n log n) worst case → heap; fastest on average in practice → quick; fewest writes → selection."""}],

    "Introduction to Data Structures": [{"title": S + "time complexity of code", "md": """| Code | Count | Order |
|---|---|---|
| `for (i = 0; i < n; i++) for (j = 0; j < n; j++) x++;` | n² | O(n²) |
| `for (i = 0; i < n; i++) for (j = i; j < n; j++) x++;` | n(n + 1)/2 | O(n²) |
| `for (i = 1; i < n; i = i * 2) x++;` | ⌈log₂ n⌉ | O(log n) |
| `for (i = n; i > 0; i = i / 2) for (j = 0; j < i; j++) x++;` | n + n/2 + … < 2n | **O(n)** |
| `for (i = 0; i < n; i++) for (j = 1; j < n; j *= 2) x++;` | n log n | O(n log n) |
| `for (i = 1; i * i <= n; i++) x++;` | √n | O(√n) |
| `for (i = 0; i < n; i++); for (j = 0; j < n; j++) x++;` | 2n (two separate loops) | O(n) |
| `int f(int n) { return n <= 1 ? 1 : f(n - 1) + f(n - 1); }` | 2ⁿ calls | O(2ⁿ) |
| `int g(int n) { return n <= 1 ? 1 : g(n / 2) + 1; }` | log n calls | O(log n) |

### Q. Which grows fastest?
n log n, n¹·⁵, 2ⁿ, n! → order n log n < n¹·⁵ < 2ⁿ < n!; log n² = 2 log n = O(log n); 2ⁿ⁺¹ = O(2ⁿ) but 4ⁿ ≠ O(2ⁿ).

### Q. Space
Recursive sum of an array of n elements uses O(n) stack; iterative O(1); merge sort O(n) extra; quick sort O(log n) average stack."""}],
}
