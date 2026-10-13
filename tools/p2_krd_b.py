"""KRIES Computer Teacher · Data Structures · P2-KRD-03 Arrays in Data Structures and P2-KRD-04 Linked Lists (2 topics × 3 sets × 30),
with NOTES. Set 1 of each topic PULLS the GPSTR Unit 8 set (tools/p2u8_a.py – repeats by design, see REUSE in check_packs.py); sets 2 and 3
mix REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final keys for
Legislative Council Secretariat 2024 (Sr/Jr Programmer P2 – A1) and GTTC 2024 (Lecturer CS – A1). KSET/KEA questions come from
packs/pyq-p2.json; PGCET answers were worked out by ExamSim (read from the page images). Addresses assume the stated base and element size;
every list trace was done by hand. References: Lipschutz, Data Structures (Schaum); Horowitz & Sahni, Fundamentals of Data Structures in C."""
from p2u8_a import ARRAYS, LINKED_LISTS
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

ARRAY_INS_DEL = [
    ("Arrange the following steps in the order for inserting data elements into an array-based list\n(a) Repeat till all elements are inserted\n(b) insert data\n"
     "(c) update counter\n(d) check capacity\n(e) initialise the list, and counter too", ["(a), (b), (d), (c), (e)", "(a), (b), (c), (d), (e)", "(e), (d), (b), (c), (a)",
                                                                                          "(b), (a), (c), (e), (d)"], 2,
     "Initialise; for each element check capacity, insert, update the count; repeat." + NOTE, "PGCET 2026 CS · Q3"),
    kset("KSET 2023 CS&A · Q41"),
    ("If an array is declared as int arr [50], then how many elements can it hold?", ["49", "51", "0", "50"], 3, "Indices 0 … 49." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q56"),
    ("In a array, all elements are stored in ____ memory locations.", ["Random", "Sequential", "Shared", "None of the above"], 1, "Contiguous storage." + NOTE,
     "PGCET 2024 M.Tech CS · Q82"),
    ("To insert a new element at index 2 of an array holding 6 elements (indices 0–5), how many elements must be shifted?", ["4", "2", "6", "3"], 0,
     PYQ + "Elements at indices 2, 3, 4 and 5 move one place right."),
    ("When inserting into an array, the elements are shifted", ["From the last element backwards, so that none is overwritten", "From the insertion point forwards",
                                                               "In random order", "Not at all"], 0, "for (i = n; i > pos; i--) a[i] = a[i − 1];"),
    ("Before inserting into an array, a program must check", ["That the array is not already full (overflow)", "That it is sorted", "That it is empty",
                                                              "The element's address"], 0, "A static array cannot grow."),
    ("Inserting 25 at index 1 of the array [10, 30, 40] gives", ["[10, 25, 30, 40]", "[25, 10, 30, 40]", "[10, 30, 25, 40]", "[10, 25, 40]"], 0, "30 and 40 move right."),
    ("Deleting the element at index 0 of [5, 8, 9, 12] (keeping the order) gives", ["[8, 9, 12]", "[5, 9, 12]", "[12, 8, 9]", "[0, 8, 9, 12]"], 0, "The rest move left."),
    ("Deleting the first element of an array of n elements (keeping the order) needs how many moves?", ["n − 1", "n", "1", "0"], 0, "Every other element moves left."),
    ("Deleting the last element of an array takes", ["O(1)", "O(n)", "O(log n)", "O(n²)"], 0, "Only the count changes."),
    ("The worst-case time to insert an element into an array of n elements (keeping the order) is", ["O(n)", "O(1)", "O(log n)", "O(n²)"], 0, "Inserting at the front."),
    ("Inserting 35 into the sorted array [10, 20, 30, 40, 50] (keeping it sorted) puts 35 at index", ["3", "2", "4", "5"], 0, "After 30, before 40."),
    ("If the order of elements does not matter, an element can be deleted from an array in O(1) by", ["Copying the last element into its place and reducing the count",
                                                                                                       "Shifting all the elements", "Sorting the array", "Setting it to zero"], 0,
     "No shifting is needed."),
    ("Which is an advantage of arrays?", ["Constant-time access to any element by its index", "Easy insertion in the middle", "Automatic growth in size",
                                          "No wasted memory in any case"], 0, "Address = base + index × size."),
    ("Which is a disadvantage of a static array?", ["Its size is fixed when it is declared", "Random access", "Contiguous storage helps the cache", "Simple indexing"], 0,
     "Too small overflows; too large wastes memory."),
    ("A very large array may fail to be allocated even when enough memory is free in total, because", ["It needs one contiguous block", "Arrays need a cache",
                                                                                                         "Arrays need a linked list", "Arrays cannot be large"], 0,
     "Linked lists can use scattered memory."),
    ("Declaring an array much larger than needed", ["Wastes the unused memory", "Makes access slower", "Causes overflow", "Is not allowed"], 0, "A dynamic structure avoids this."),
    ("Merging two sorted arrays of sizes m and n into a new sorted array takes", ["O(m + n)", "O(m × n)", "O(log(m + n))", "O(1)"], 0, "Each step moves one element."),
    ("Reversing an array of n elements in place needs how many swaps?", ["⌊n/2⌋", "n", "n − 1", "2n"], 0, "Swap a[i] and a[n − 1 − i]."),
    ("For the array [2, 7, 4, 9, 6], a loop that counts the even elements gives", ["3", "2", "5", "4"], 0, "2, 4 and 6."),
    ("Searching an unsorted array of n elements for a key takes, in the worst case,", ["O(n)", "O(log n)", "O(1)", "O(n²)"], 0, "Binary search needs a sorted array."),
    ("In an array-based list, the number of elements in use is kept in a separate variable because", ["The array may have more slots than elements in use",
                                                                                                        "Arrays store their own length", "C requires it", "It speeds up sorting"], 0,
     "Insertion and deletion update it."),
    ("Inserting at the beginning of an array of n elements shifts", ["All n elements", "No elements", "One element", "n/2 elements"], 0, "The worst case of insertion."),
    ("Deleting the element at index 3 of an array of 10 elements (keeping the order) moves how many elements?", ["6", "7", "3", "9"], 0, "Indices 4 … 9."),
    ("When a dynamic array is full, it is usually grown by", ["Allocating a bigger block (often double the size) and copying the elements", "Adding one slot in place",
                                                              "Linking a new node", "Sorting it"], 0, "realloc in C; amortised O(1) appends."),
    ("Keeping roll numbers in one array and marks in another, matched by index, is called using", ["Parallel arrays", "Sparse arrays", "Jagged arrays", "Linked arrays"], 0,
     "An array of structures is the alternative."),
    ("Compared with a linked list, an array uses less memory per element because", ["It needs no pointer fields", "It compresses data", "It stores fewer elements",
                                                                                     "It uses registers"], 0, "Each list node carries at least one pointer."),
    ("for (i = n; i > pos; i--) a[i] = a[i - 1];  a[pos] = x;  n++;", ["Inserts x at index pos", "Deletes the element at pos", "Reverses the array", "Searches for x"], 0,
     "Shift right, then place x."),
    ("for (i = pos; i < n - 1; i++) a[i] = a[i + 1];  n--;", ["Deletes the element at index pos", "Inserts at pos", "Sorts the array", "Copies the array"], 0,
     "Shift left over the deleted element."),
]

ARRAY_PRACTICE = [
    kset("KEA 2026 CS Paper-2 · Q82"),
    kset("KEA 2026 CS Paper-2 · Q84"),
    kset("KSET 2023 CS&A · Q3"),
    ("Consider the following declaration of a 2D array in C:\nChar a [100] [100];\nAssuming that the main memory is byte addressable and that the array is stored starting "
     "from memory address 0, the address of a [40] [50] is", ["4040", "4050", "5040", "5050"], 1, "Row-major: 40 × 100 + 50." + GTTC, "GTTC 2024 Lecturer CS · Q9"),
    ("What is the output of the following program ?\n#include<stdio.h>\nvoid main( )\n{\n  int a[3][2] = {1, 2, 3, 4, 5, 6};\n  printf(\"%d, %d\", a[0][0], a[2][1]);\n}",
     ["1, 5", "1, 6", "2, 5", "2, 6"], 1, "Row-major filling." + NOTE, "PGCET 2024 M.Tech CS · Q94"),
    ("An array A[10..30] has 2-byte elements and starts at address 2000. The address of A[15] is", ["2010", "2030", "2015", "2005"], 0,
     PYQ + "Base + (i − lower bound) × size = 2000 + 5 × 2."),
    ("A[5][4] (4-byte elements, 0-based) is stored row-major from address 100. The address of A[3][2] is", ["156", "152", "128", "140"], 0, "100 + (3 × 4 + 2) × 4."),
    ("The same A[5][4] stored column-major from address 100 has A[3][2] at", ["152", "156", "112", "160"], 0, "100 + (2 × 5 + 3) × 4."),
    ("How many elements does the array A[2..8][3..7] have?", ["35", "30", "42", "24"], 0, "(8 − 2 + 1) × (7 − 3 + 1) = 7 × 5."),
    ("What is printed?\nint a[2][3] = {1, 2, 3, 4, 5, 6}, i, s = 0;\nfor (i = 0; i < 2; i++) s += a[i][2];\nprintf(\"%d\", s);", ["9", "5", "7", "21"], 0,
     "The last column: 3 + 6."),
    ("With a = {{1, 2, 3}, {4, 5, 6}} and b[j][i] = a[i][j] for all i, j, the value of b[2][0] is", ["3", "5", "4", "6"], 0, "b is the transpose: b[2][0] = a[0][2]."),
    ("int a[6] = {1, 2, 4, 5}; n = 4. After inserting 3 at index 2 (shifting right), a[3] is", ["4", "3", "5", "2"], 0, "The array becomes 1 2 3 4 5."),
    ("int a[] = {9, 8, 7, 6}. After deleting the element at index 1 (shifting left), a[1] is", ["7", "8", "6", "9"], 0, "The array becomes 9 7 6."),
    ("For the array [2, 4, 6, 8], how many elements are greater than the average?", ["2", "1", "3", "4"], 0, "The average is 5."),
    ("After reversing [1, 2, 3, 4, 5] in place, a[1] is", ["4", "2", "3", "5"], 0, "5 4 3 2 1."),
    ("After rotating [1, 2, 3, 4] left by one place, a[3] is", ["1", "4", "3", "2"], 0, "2 3 4 1."),
    ("What is printed?\nint a[] = {1, 2, 3, 4}, i;\nfor (i = 1; i < 4; i++) a[i] += a[i - 1];\nprintf(\"%d\", a[3]);", ["10", "7", "4", "9"], 0,
     "Running (prefix) sums: 1 3 6 10."),
    ("For  int a[5];  the last valid index is", ["4", "5", "0", "6"], 0, "Indices start at 0."),
    ("With 4-byte int,  int a[10][20];  occupies", ["800 bytes", "200 bytes", "120 bytes", "80 bytes"], 0, "10 × 20 × 4."),
    ("char name[5][10];  occupies", ["50 bytes", "15 bytes", "5 bytes", "10 bytes"], 0, "5 strings of 10 bytes."),
    ("For an int array a, the value of  &a[4] − &a[1]  is", ["3", "12", "4", "1"], 0, "Pointer difference counts elements."),
    ("A 6 × 6 sparse matrix has 8 non-zero values. Its triplet form, with a header row, needs how many rows?", ["9", "8", "36", "6"], 0,
     "One header (rows, columns, count) + one row per non-zero value."),
    ("A lower triangular matrix is stored row by row (0-based, i ≥ j). Element a[3][1] is at position", ["7", "4", "10", "6"], 0, PYQ + "i(i + 1)/2 + j = 6 + 1."),
    ("An n × n diagonal matrix can be stored using how many locations?", ["n", "n²", "2n", "n(n + 1)/2"], 0, "Only the diagonal is non-zero."),
    ("The integer average of [10, 20, 30, 40] computed as sum / 4 is", ["25", "100", "20", "30"], 0, "100 / 4."),
    ("char A[2][3][4] (1 byte each) starts at address 0, row-major. The address of A[1][2][3] is", ["23", "24", "11", "17"], 0, "1 × 12 + 2 × 4 + 3."),
    ("A linear search for 7 in [4, 7, 7, 2] that stops at the first match returns index", ["1", "2", "0", "3"], 0, "The first 7."),
    ("A linear search finds the key at index 5. How many comparisons were made?", ["6", "5", "1", "4"], 0, "Indices 0 to 5."),
    ("for (i = 0; i < n / 2; i++) swap(a[i], a[n - 1 - i]);", ["Reverses the array", "Sorts it", "Rotates it by one", "Does nothing"], 0, "Ends move towards the middle."),
    ("Merging [1, 4, 7] and [2, 3, 8] into one sorted array, the third element is", ["3", "2", "4", "7"], 0, "1 2 3 4 7 8."),
]

LIST_DYNAMIC = [
    ("A variant of the linked list in which none of the node contains NULL pointer is", ["Singly-linked list", "Doubly-linked list", "Circular linked list", "None"], 2,
     "The last node points back to the first." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q57"),
    ("The minimum number of fields in each node of a doubly-linked list is ____", ["3", "2", "4", "5"], 0, "prev, data, next." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q59"),
    ("Which of the following is optimal to find an element at the K-th position in the linked list?", ["Single linked list", "Doubly linked list", "Circular linked list",
                                                                                                         "Array Implementation of linked list"], 3,
     "Arrays allow direct indexing." + GTTC, "GTTC 2024 Lecturer CS · Q21"),
    ("Which of the following applications uses circular linked list?", ["Recursive function call", "Undo operation in a text editor", "Implementation of hash table",
                                                                        "Allocating CPU to other resources"], 3, "Round-robin CPU allocation cycles through the list." + NOTE,
     "PGCET 2026 CS · Q4"),
    ("In simple chaining, what data structure is appropriate ?", ["Singly linked list", "Doubly linked list", "Circular linked list", "Binary trees"], 0,
     "Each hash bucket keeps a singly linked chain." + NOTE, "PGCET 2023 M.Tech CS · Q12"),
    ("The dynamic memory allocation functions in C language are defined in ____", ["<stdio.h>", "<stdlib.h>", "<string.h>", "<conio.h>"], 1,
     "malloc, calloc, realloc, free." + NOTE, "PGCET 2026 CS · Q91"),
    ("A new node is created in C with", ["(struct node *) malloc(sizeof(struct node))", "new node;", "malloc(node);", "alloc(struct node);"], 0,
     PYQ + "The cast is optional in C."),
    ("If malloc() returns NULL while creating a node, it means", ["No memory is available (overflow)", "The list is empty", "The node was freed", "The list is sorted"], 0,
     "Always check before using the node."),
    ("After a node is removed from a list, its memory should be released with", ["free(p)", "delete p", "remove(p)", "p = 0 alone"], 0, "Otherwise memory leaks."),
    ("To insert node t at the beginning of a singly linked list, the correct order is", ["t->next = head; head = t;", "head = t; t->next = head;", "head->next = t;", "t = head;"], 0,
     "The other order makes t point to itself."),
    ("To insert node t after node p, the statements are", ["t->next = p->next; p->next = t;", "p->next = t; t->next = p->next;", "t->next = p; p->next = t;",
                                                          "p = t;"], 0, "Link t to the rest first."),
    ("Deleting the first node of a singly linked list is done by", ["temp = head; head = head->next; free(temp);", "free(head); head = head->next;", "head = NULL;",
                                                                    "head->next = NULL;"], 0, "Using head after free is an error."),
    ("Deleting the last node of a singly linked list with only a head pointer takes", ["O(n) – the second-last node must be found", "O(1)", "O(log n)", "O(n²)"], 0,
     "A tail pointer does not help for deletion."),
    ("Inserting at the end of a singly linked list that keeps a tail pointer takes", ["O(1)", "O(n)", "O(log n)", "O(n²)"], 0, "tail->next = t; tail = t;"),
    ("A singly linked list is empty when", ["head == NULL", "head->next == NULL", "head->data == 0", "head == head->next"], 0, "head->next == NULL means one node."),
    ("Trying to delete from an empty linked list is called", ["Underflow", "Overflow", "A memory leak", "A collision"], 0, "Overflow = no memory for a new node."),
    ("In Lipschutz's notation, the list of free nodes from which new nodes are taken is the", ["AVAIL (free-storage) list", "Garbage list", "Header list", "Stack list"], 0,
     "Garbage collection returns unused nodes to it."),
    ("Deleting node p from the middle of a doubly linked list needs", ["p->prev->next = p->next; p->next->prev = p->prev;", "p->next = NULL;", "p = p->prev;", "head = p;"], 0,
     "Then free(p)."),
    ("A circular singly linked list is traversed once, starting at head, with", ["do { … p = p->next; } while (p != head);", "while (p != NULL)", "for (;;) with no test",
                                                                                 "while (p->next != NULL)"], 0, "There is no NULL to stop at."),
    ("A header list whose last node points back to the header node is a", ["Circular header list", "Grounded header list", "Doubly linked list", "Two-way list"], 0,
     "In a grounded header list the last node holds NULL."),
    ("In Lipschutz's book, a 'two-way list' is", ["A doubly linked list", "Two singly linked lists", "A circular list", "A stack and a queue"], 0, "Traversal in both directions."),
    ("In  struct node { int data; struct node *next; };  the member next holds", ["The address of the next node", "The next data value", "The size of the node", "An index"], 0,
     "A self-referential structure."),
    ("A function that inserts at the head of a list is declared  void push(struct node **head, int x)  because", ["It must change the caller's head pointer", "It is faster",
                                                                                                                  "It saves memory", "C requires two stars"], 0,
     "Or it can return the new head."),
    ("Linked lists are preferred over arrays when", ["Insertions and deletions are frequent and the size is not known in advance", "Random access is needed",
                                                     "Memory per element must be minimal", "Binary search is needed"], 0, "No shifting, no fixed size."),
    ("Inserting at the front of a circular singly linked list, given a pointer to its LAST node, takes", ["O(1)", "O(n)", "O(log n)", "O(n²)"], 0,
     "last->next is the first node."),
    ("Searching a linked list of n nodes for a key takes", ["O(n), even if the list is sorted", "O(log n) if sorted", "O(1)", "O(n²)"], 0, "No random access, so no binary search."),
    ("Inserting into a sorted linked list (keeping it sorted) takes", ["O(n) to find the position, then O(1) to link", "O(1)", "O(log n)", "O(n²)"], 0, "No shifting is needed."),
    ("Using a pointer after the node it points to has been freed is a", ["Dangling-pointer error", "Memory leak", "Underflow", "Collision"], 0, "Set it to NULL after free."),
    ("A loop that counts the nodes of a list is", ["for (c = 0, p = head; p != NULL; p = p->next) c++;", "for (c = 0; head; c++);", "c = sizeof(head);", "c = head->data;"], 0,
     "O(n)."),
    ("Not freeing nodes that are no longer reachable causes", ["A memory leak", "Underflow", "A stack overflow", "A segmentation fault always"], 0, "Memory is lost until the program ends."),
]

LIST_PRACTICE = [
    ("For the list 10 → 20 → 30, a traversal that adds the data gives", ["60", "30", "10", "3"], 0, "10 + 20 + 30."),
    ("A loop that counts the nodes of 5 → 3 → 8 → 1 gives", ["4", "3", "5", "17"], 0, "Four nodes."),
    ("Inserting 15 after the first node of 10 → 20 → 30 gives", ["10 → 15 → 20 → 30", "15 → 10 → 20 → 30", "10 → 20 → 15 → 30", "10 → 20 → 30 → 15"], 0,
     "t->next = p->next; p->next = t."),
    ("Deleting the first node of 10 → 20 → 30 leaves", ["20 → 30", "10 → 30", "10 → 20", "30"], 0, "head moves to the second node."),
    ("After reversing 1 → 2 → 3 → 4, head->data is", ["4", "1", "2", "3"], 0, "The old last node becomes the head."),
    ("A loop that finds the largest value in 7 → 19 → 3 gives", ["19", "7", "3", "29"], 0, "Compare as you traverse."),
    ("Searching for 8 in 5 → 8 → 2 returns position (1-based)", ["2", "1", "3", "8"], 0, "Second node."),
    ("For the list 1 → 2 → 3 → 4, after  p = head->next->next;  p->data is", ["3", "2", "4", "1"], 0, "Two steps from the head."),
    ("For the list A → B → C, head->next->next->data is", ["C", "B", "A", "NULL"], 0, "The third node."),
    ("What does cnt(head) return for a list of 6 nodes?\nint cnt(struct node *p) { return p ? 1 + cnt(p->next) : 0; }", ["6", "5", "7", "0"], 0, PYQ + "Recursive counting."),
    ("Deleting the last node of 4 → 5 → 6 leaves", ["4 → 5", "5 → 6", "4 → 6", "4"], 0, "The second-last node's next becomes NULL."),
    ("In the circular list 1 → 2 → 3 → (back to 1), printing 4 nodes starting at node 2 gives", ["2 3 1 2", "2 3 1", "1 2 3 1", "2 3 4 1"], 0, "It wraps around."),
    ("Traversing the doubly linked list 1 ⇄ 2 ⇄ 3 backwards from the tail prints", ["3 2 1", "1 2 3", "3 1 2", "2 1 3"], 0, "Follow the prev pointers."),
    ("In the doubly linked list 1 ⇄ 2 ⇄ 3, with p pointing to node 2, the value of  p->prev->data + p->next->data  is", ["4", "3", "5", "6"], 0, "1 + 3."),
    ("After inserting 3 at the end of 1 → 2, the number of nodes and the last value are", ["3 and 3", "2 and 3", "3 and 2", "3 and 1"], 0, "1 → 2 → 3."),
    ("Removing all even values from 1 → 2 → 3 → 4 leaves", ["1 → 3", "2 → 4", "1 → 2", "3 → 4"], 0, "Unlink each even node."),
    ("Adding the 1st, 3rd and 5th nodes of 1 → 2 → 3 → 4 → 5 gives", ["9", "6", "15", "8"], 0, "1 + 3 + 5."),
    ("Using slow and fast pointers on 1 → 2 → 3 → 4 → 5, the slow pointer ends at", ["3", "2", "4", "5"], 0, PYQ + "The fast pointer moves two steps per step of the slow one."),
    ("The number of NULL pointers in a (non-circular) singly linked list of n nodes is", ["1", "n", "0", "2"], 0, "Only the last node's next."),
    ("With 4-byte data and an 8-byte pointer (nodes padded to 16 bytes), 100 nodes take about", ["1,600 bytes", "400 bytes", "1,200 bytes", "800 bytes"], 0,
     "An int array of 100 takes 400 bytes."),
    ("Merging the sorted lists 1 → 4 and 2 → 3, the third node of the result holds", ["3", "2", "4", "1"], 0, "1 → 2 → 3 → 4."),
    ("Writing  head = head->next;  without freeing the old first node causes", ["A memory leak", "Underflow", "A dangling pointer", "Nothing harmful"], 0,
     "The old node can no longer be reached."),
    ("The polynomial 4x³ + 2x + 5, stored as a list of (coefficient, exponent) nodes, needs", ["3 nodes", "4 nodes", "6 nodes", "1 node"], 0, "Zero terms are not stored."),
    ("Adding the polynomials 3x² + 2x and 5x² + 1 as linked lists gives", ["8x² + 2x + 1", "8x² + 3x", "15x⁴ + 2x + 1", "8x⁴ + 2x + 1"], 0, "Add coefficients of equal exponents."),
    ("A stack built as a linked list (push at the head): push 1, 2, 3, then pop. The popped value is", ["3", "1", "2", "NULL"], 0, "Last in, first out."),
    ("A queue built as a linked list (insert at the tail, delete at the head): insert 1, 2, 3, then delete. The deleted value is", ["1", "3", "2", "NULL"], 0, "First in, first out."),
    ("In a circular singly linked list with only one node, that node's next points to", ["Itself", "NULL", "The header", "Garbage"], 0, "It is both first and last."),
    ("A doubly linked list of n nodes contains how many pointer fields in all?", ["2n", "n", "n + 1", "2n + 2"], 0, "prev and next in every node."),
    ("The Josephus problem (people in a circle, every k-th person removed) is naturally solved with a", ["Circular linked list", "Stack", "Binary tree", "Hash table"], 0,
     "Keep moving round the circle and unlink."),
    ("If head is NULL, the loop  for (p = head; p->next != NULL; p = p->next);", ["Crashes – p->next dereferences a NULL pointer", "Runs zero times safely", "Runs forever",
                                                                                  "Returns the last node"], 0, "Check head != NULL first."),
]

SET3 = "3 · Previous-Year Pattern Practice – Programs and Traces"
TOPICS = {
    "Arrays in Data Structures": [
        ("1 · Storage Representation of 1-D and 2-D Arrays, Sparse and Special Matrices", ARRAYS),
        ("2 · Insertion and Deletion on 1-D Arrays, Advantages and Disadvantages", ARRAY_INS_DEL),
        (SET3, ARRAY_PRACTICE),
    ],
    "Linked Lists": [
        ("1 · Singly, Circular and Doubly Linked Lists – Operations", LINKED_LISTS),
        ("2 · Pointers, Dynamic Memory Allocation, Insertion and Deletion of a Node", LIST_DYNAMIC),
        (SET3, LIST_PRACTICE),
    ],
}

NOTES = {
    "Arrays in Data Structures": [{"title": "Arrays – revision sheet", "md": """## Storage representation
- 1-D: Loc(A[i]) = Base + w × (i − LB); number of elements = UB − LB + 1
- 2-D (m × n): row-major Loc = Base + w × (n × (i − LB₁) + (j − LB₂)); column-major Base + w × (m × (j − LB₂) + (i − LB₁))
  - char a[100][100] at 0 → a[40][50] = 4050; A[5][4], w = 4, base 100 → A[3][2] = 156 (row) / 152 (column)
- 3-D: A[1][2][3] of A[2][3][4] = 1·12 + 2·4 + 3 = 23 elements from the base
- Special matrices: lower triangular n(n + 1)/2 (index i(i+1)/2 + j), tridiagonal 3n − 2, diagonal n; sparse → triplets (header + one row per non-zero)

## Insertion and deletion (n elements)
- Insert at pos: check overflow; shift a[n−1]…a[pos] right (from the end); place; n++ → O(n) (front worst, end O(1))
- Delete at pos: shift a[pos+1]…a[n−1] left; n−− → n − pos − 1 moves; unordered delete: copy last element in, O(1)
- Insert into a sorted array: find the position, then shift

## Advantages / disadvantages
| Advantages | Disadvantages |
|---|---|
| O(1) random access | fixed size (overflow or waste) |
| no pointer overhead | O(n) insert/delete in the middle |
| simple, cache-friendly | needs one contiguous block |
- Dynamic arrays grow by doubling (amortised O(1) append); parallel arrays
"""}],
    "Linked Lists": [{"title": "Linked lists – revision sheet", "md": """## Basics
- Node = data + pointer(s): `struct node { int data; struct node *next; };` (self-referential)
- Create: `t = (struct node *) malloc(sizeof(struct node));` (NULL → overflow); release: `free(t)`; AVAIL list (Lipschutz)
- Empty: head == NULL; deleting from empty = underflow; forgetting free = memory leak; using freed node = dangling pointer

## Operations (singly, head pointer only)
| Operation | Code | Time |
|---|---|---|
| insert at front | t->next = head; head = t | O(1) |
| insert after p | t->next = p->next; p->next = t | O(1) |
| insert at end | traverse (O(1) with tail) | O(n) |
| delete first | tmp = head; head = head->next; free(tmp) | O(1) |
| delete last | find second-last | O(n) |
| search / k-th element | traverse | O(n) |
- Reverse iteratively O(n); middle by slow/fast pointers; cycle by Floyd's method; merge sorted lists O(m + n)

## Variants
- Circular: last → first, no NULL; traverse with do … while (p != head); round-robin, Josephus; front insert O(1) with a last pointer
- Doubly (two-way): prev + data + next (3 fields, 2n pointers); delete p: p->prev->next = p->next; p->next->prev = p->prev
- Header lists: grounded (last → NULL) or circular (last → header)
- Uses: polynomials (coefficient, exponent nodes), stacks and queues, hash chaining, sparse matrices
- Prefer lists for frequent insert/delete and unknown size; arrays for random access
"""}],
}
