"""KRIES Computer Teacher · Data Structures · P2-KRD-05 Stacks and P2-KRD-06 Queues (2 topics × 3 sets × 30), with NOTES.
Set 1 of each topic PULLS the GPSTR Unit 8 set (tools/p2u8_a.py – repeats by design, see REUSE in check_packs.py); sets 2 and 3 mix REAL
previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final keys for Legislative
Council Secretariat 2024 (Sr/Jr Programmer P2 – A1) and GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1). KSET/KEA questions come
from packs/pyq-p2.json; GFGC 2021 and PGCET answers were worked out by ExamSim (read from the page images). Every conversion, evaluation and
queue trace was done by hand. Operator precedence for conversions: ^ (right-associative) > * / > + −."""
from p2u8_a import STACKS, QUEUES
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

STACK_APPS = [
    ("A single array A [1..MAXSIZE] is used to implement two stacks. The two stacks grow from opposite ends of the array. Variables top1 and top2 (top1 < top2) point to the "
     "location of the topmost element in each of the stacks. If the space is to be used efficiently, then the condition for \"stack full\" is ____",
     ["(top1 = MAXSIZE/2) and (top2 = MAXSIZE/2 + 1)", "top1 + top2 = MAXSIZE", "(top1 = MAXSIZE/2) or (top2 = MAXSIZE/2)", "top1 = top2 − 1"], 3,
     "Full only when the two tops meet." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q60"),
    ("Which data structure is used for implementing recursion?", ["Stack", "Queue", "List", "Array"], 0, "Activation records are pushed and popped." + GTTC,
     "GTTC 2024 Lecturer CS · Q3"),
    ("The Prefix form of A − B / (C * D ^ E) is", ["−A/B*C^DE", "−A/BC*^DE", "−ABCD*^DE", "−/*^ACBDE"], 0,
     "A − (B / (C * (D ^ E))) → − A / B * C ^ D E." + GTTC, "GTTC 2024 Lecturer CS · Q4"),
    ("The optimal data structure used to solve Tower of Hanoi is", ["Tree", "Heap", "Queue", "Stack"], 3, "Recursion (or an explicit stack) holds the sub-problems." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q94"),
    ("Consider the following operations performed on stack of size 5.\npush(11);\npop();\npush(21);\npush(33);\npop();\npush(44);\npop();\npop();\npush(55);\n"
     "After the completion of all operations, the number of elements present in stack is", ["1", "2", "3", "4"], 0,
     "The stack ends holding only 55." + NOTE, "GFGC 2021 CS · Q76"),
    ("A parenthesis checker program would be best implemented using", ["Array", "List", "Queue", "Stack"], 3, "The last opened bracket must close first." + NOTE,
     "GFGC 2021 CS · Q87"),
    ("Let A = 2, B = 3, C = 4 and D = 5. What is the final value of the prefix expression :\n+ * A B − C D ?", ["5", "−5", "10", "−10"], 0,
     "(2 × 3) + (4 − 5) = 6 − 1." + NOTE, "GFGC 2021 CS · Q99"),
    ("Which of the following data structures find its use in recursion?", ["Arrays", "Stacks", "Queues", "Linked list"], 1, "The call stack." + NOTE,
     "PGCET 2024 M.Tech CS · Q17"),
    kset("KEA 2026 CS Paper-2 · Q1"),
    kset("KEA 2026 CS Paper-2 · Q2"),
    kset("KEA 2026 CS Paper-2 · Q8"),
    kset("KSET 2025 CS&A · Q61"),
    ("The postfix form of  (A + B) * C − D / E  is", ["A B + C * D E / −", "A B C + * D E / −", "A B + C D E / * −", "+ A B * C − / D E"], 0,
     PYQ + "Convert each sub-expression, keeping operands in order."),
    ("The postfix form of  A * (B + C) / D  is", ["A B C + * D /", "A B * C + D /", "A B C + D / *", "* A + B C / D"], 0, "Parentheses first, then left to right."),
    ("The postfix form of  A + B * C ^ D  is", ["A B C D ^ * +", "A B C * D ^ +", "A B + C D ^ *", "A B C D + * ^"], 0, "^ binds tightest."),
    ("Since ^ is right-associative, the postfix form of  A ^ B ^ C  is", ["A B C ^ ^", "A B ^ C ^", "^ ^ A B C", "A ^ B C ^"], 0, "A ^ (B ^ C)."),
    ("The prefix form of  (A + B) * C  is", ["* + A B C", "+ A * B C", "A B + C *", "* A + B C"], 0, "Each operator comes before its operands."),
    ("The value of the postfix expression  8 2 / 3 * 4 +  is", ["16", "10", "28", "7"], 0, "8 / 2 = 4; 4 × 3 = 12; 12 + 4."),
    ("The value of the postfix expression  2 3 ^ 1 −  is", ["7", "5", "8", "1"], 0, "2³ − 1."),
    ("While converting  A + B * C  to postfix, the largest number of operators on the stack at one time is", ["2", "1", "3", "0"], 0,
     PYQ + "+ is still on the stack when * is pushed."),
    ("With  fact(n) = n == 0 ? 1 : n * fact(n − 1),  computing fact(4) puts at most how many activation records of fact on the stack?", ["5", "4", "1", "24"], 0,
     "fact(4), fact(3), fact(2), fact(1), fact(0)."),
    ("The Tower of Hanoi with 6 discs needs a minimum of how many moves?", ["63", "64", "36", "32"], 0, "2ⁿ − 1."),
    ("In the 3-disc Tower of Hanoi (move all discs from A to C using B), the first move of the optimal solution is", ["Smallest disc from A to C", "Smallest disc from A to B",
                                                                                                                     "Largest disc from A to C", "Middle disc from A to B"], 0,
     "For an odd number of discs the smallest disc goes first to the target peg."),
    ("The recursive Tower of Hanoi solution moves n discs from A to C by", ["Moving n − 1 discs to B, the largest disc to C, then the n − 1 discs from B to C",
                                                                           "Moving one disc at a time from A to C", "Moving the largest disc first", "Sorting the discs"], 0,
     "T(n) = 2T(n − 1) + 1."),
    ("Postfix (Reverse Polish) expressions are convenient because", ["They need no parentheses and can be evaluated in one left-to-right scan with a stack",
                                                                     "They are shorter than infix in every case", "They need no stack", "They are easier for people to read"], 0,
     "Compilers convert infix to postfix."),
    ("In postfix evaluation, when an operator is read", ["The top two operands are popped, the operation applied (the second one popped is the left operand) and the result pushed",
                                                         "The operator is pushed", "One operand is popped", "The stack is cleared"], 0, "For '8 2 /' the result is 8 / 2."),
    ("During infix-to-postfix conversion of left-associative operators, an incoming operator first pops from the stack every operator of", ["Higher or equal precedence",
                                                                                                                                          "Lower precedence", "Any precedence",
                                                                                                                                          "No operator"], 0,
     "'(' stays until its ')' arrives."),
    ("Undo and redo in an editor are commonly implemented with", ["Two stacks", "One queue", "A binary tree", "A hash table"], 0, "Undo pops from one and pushes to the other."),
    ("When a function is called, its return address and local variables are kept on the", ["System (call) stack", "Heap", "Disk", "Queue"], 0, "Popped when it returns."),
    ("Pushing the letters of \"KEA\" onto a stack and popping them all gives", ["AEK", "KEA", "EAK", "AKE"], 0, "A stack reverses order."),
]

STACK_PRACTICE = [
    ("After  push(5), push(3), pop(), push(7),  the top of the stack is", ["7", "3", "5", "Empty"], 0, "3 was popped."),
    ("An array stack starts with top = −1. After 4 pushes and 1 pop, top is", ["2", "3", "4", "1"], 0, "−1 + 4 − 1."),
    ("An array stack of size MAX (0-based, top = −1 when empty) is full when", ["top == MAX − 1", "top == MAX", "top == 0", "top == −1"], 0, "The last index is MAX − 1."),
    ("Pushing node t onto a stack kept as a linked list (top = head) is", ["t->next = top; top = t;", "top->next = t;", "top = t->next;", "t = top;"], 0, "O(1)."),
    ("Popping from a linked stack is", ["temp = top; top = top->next; x = temp->data; free(temp);", "top = NULL;", "top->next = NULL;", "free(top); top = top->next;"], 0,
     "Check top != NULL first (underflow)."),
    ("The value of the postfix expression  9 3 − 2 *  is", ["12", "3", "15", "6"], 0, "(9 − 3) × 2."),
    ("The value of the prefix expression  + * 2 3 4  is", ["10", "14", "20", "9"], 0, "(2 × 3) + 4."),
    ("The infix form of the postfix expression  A B C − *  is", ["A * (B − C)", "(A − B) * C", "A − B * C", "A * B − C"], 0, "− applies to B and C first."),
    ("Which bracket string is NOT balanced?", ["( [ ) ]", "{ [ ( ) ] }", "( ) [ ] { }", "( ( ) )"], 0, "] arrives while ( is on top."),
    ("Reversing a 5-letter word with a stack needs how many pushes and pops?", ["5 pushes and 5 pops", "5 pushes and 1 pop", "10 pushes", "1 push and 5 pops"], 0, "One each per letter."),
    ("Pushing 1, 2, 3 in this order (pops allowed at any time), which output sequence is impossible?", ["3 1 2", "1 2 3", "3 2 1", "2 3 1"], 0,
     PYQ + "After 3 is popped, 2 is above 1, so 1 cannot come next."),
    ("Converting 13 to binary by pushing remainders of division by 2 and then popping them gives", ["1101", "1011", "0111", "1110"], 0, "Remainders 1, 0, 1, 1 come out reversed."),
    ("What does f(2) print?\nvoid f(int n) { if (n == 0) return; printf(\"%d\", n); f(n - 1); printf(\"%d\", n); }", ["2112", "21", "1221", "2121"], 0,
     "Before the call on the way down, after it on the way back."),
    ("Which of these needs a stack?", ["Reversing a string", "Breadth-first search", "Round-robin scheduling", "Printer spooling"], 0, "The others use queues."),
    ("The value of the postfix expression  5 6 2 + * 12 4 / −  is", ["37", "40", "3", "29"], 0, PYQ + "5 × (6 + 2) − 12 / 4 = 40 − 3."),
    ("The infix form of the postfix expression  a b + c d − *  is", ["(a + b) * (c − d)", "a + b * c − d", "a + (b * c) − d", "(a + b * c) − d"], 0, "Two sub-expressions, then *."),
    ("The postfix form of  a + b − c  is", ["a b + c −", "a b c − +", "a b c + −", "+ a − b c"], 0, "Left-associative: (a + b) − c."),
    ("The postfix form of  (a + b) * (c + d) * e  is", ["a b + c d + * e *", "a b + c d + e * *", "a b c d + + * e *", "a b + * c d + e *"], 0, "Left-associative *."),
    ("A stack of size 3 receives push 1, push 2, push 3, push 4. What happens at push 4?", ["Overflow", "Underflow", "4 replaces 3", "1 is removed"], 0, "The stack is already full."),
    ("Popping from an empty stack (top = −1) causes", ["Underflow", "Overflow", "A memory leak", "Nothing"], 0, "Check isEmpty() first."),
    ("The peek (top) operation", ["Returns the top element without removing it", "Removes the top element", "Adds an element", "Empties the stack"], 0, "O(1)."),
    ("Two stacks share an array of 10 cells, growing towards each other. A push fails when", ["top1 + 1 == top2", "top1 == 5", "top2 == 5", "top1 == top2 + 5"], 0,
     "Every cell is then in use."),
    ("If top = 4 in a 0-based array stack, the stack holds how many elements?", ["5", "4", "3", "6"], 0, "top + 1."),
    ("Infinite recursion in C usually ends with", ["A stack overflow (the program crashes)", "A compile-time error", "The correct answer", "A queue overflow"], 0,
     "Each call takes stack space."),
    ("The value of the prefix expression  − + 7 3 * 2 2  is", ["6", "14", "2", "−6"], 0, "(7 + 3) − (2 × 2)."),
    ("The postfix form of  A − (B + C) * D  is", ["A B C + D * −", "A B C D + * −", "A B − C + D *", "A B C + − D *"], 0, "(B + C) * D first."),
    ("push a, push b, pop, push c, push d, pop, pop. How many elements remain?", ["1", "2", "3", "0"], 0, "Only a."),
    ("Checking that HTML tags such as <b> … </b> are properly nested is done with a", ["Stack", "Queue", "Heap", "Graph"], 0, "Like bracket matching."),
    ("With a = 2, b = 3 and c = 4, the postfix expression  a b c * +  equals", ["14", "20", "24", "9"], 0, "2 + 3 × 4."),
    ("A stack is called a LIFO structure because", ["The last element pushed is the first one popped", "The first element is popped first", "Elements are popped at random",
                                                    "Elements are sorted"], 0, "Push and pop happen at the same end (the top)."),
]

QUEUE_TYPES = [
    ("The MAX_SIZE is the size of the array used in the implementation of circular queue. How is rear manipulated while inserting an element in the queue?",
     ["rear = (rear%1) + MAX_SIZE", "rear = rear%(MAX_SIZE + 1)", "rear = (rear + 1)% MAX_SIZE", "rear = rear + (1% MAX_SIZE)"], 2, "It wraps round to 0." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q61"),
    ("The seven elements A, B, C, D, E, F and G are pushed onto a stack in reverse order i.e. starting from G. The stack is popped 5 times and each element is inserted into a "
     "queue. Two elements are deleted from the queue and pushed back onto the stack. Now, one element is popped from the stack. The popped item is", ["A", "B", "F", "G"], 1,
     "A, B, C, D, E go to the queue; A and B come out and are pushed (B on top); B is popped." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q53"),
    ("Which of the following property/properties hold true for a heap data structure?\na) It is a complete binary tree\nb) The root node always contains the maximum or minimum "
     "value\nc) It allows efficient O(1) time access to the largest (or smallest) element", ["(a) and (b) are correct", "(b) and (c) are correct", "Only (c) is correct",
                                                                                              "(a), (b) and (c) are correct"], 3,
     "A heap is how priority queues are usually built." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q65"),
    ("Identify the data structure which allow deletions at both ends of the list but insertion at only one end.", ["Input restricted dequeue", "Output restricted dequeue",
                                                                                                                   "Priority queues", "Stack"], 0,
     "Input is restricted to one end." + NOTE, "GFGC 2021 CS · Q77"),
    kset("KSET 2025 CS&A · Q62"),
    ("Which of the following is the most commonly used data structure for implementing Dijkstra's Algorithm ?", ["Max priority queue", "Stack", "Circular queue",
                                                                                                                 "Min priority queue"], 3,
     "The vertex with the smallest distance is taken next." + NOTE, "PGCET 2023 M.Tech CS · Q9"),
    ("How many stacks are needed to implement a queue? Consider the situation where no other data structure like arrays, linked list is available to you.", ["1", "2", "3", "4"], 1,
     "One for enqueue, one for dequeue." + NOTE, "PGCET 2024 M.Tech CS · Q69"),
    ("In a queue, insertion (enqueue) and deletion (dequeue) take place", ["At the rear and at the front respectively", "Both at the front", "Both at the rear",
                                                                           "At the front and at the rear respectively"], 0, PYQ + "First in, first out."),
    ("In a linear array queue with front = rear = −1 at the start, the queue is full when", ["rear == MAX − 1", "front == MAX − 1", "rear == front", "front == 0"], 0,
     "Even if deletions have freed cells at the front – the weakness of a linear queue."),
    ("In a circular queue of size N, front is advanced on deletion by", ["front = (front + 1) % N", "front = front − 1", "front = 0", "front = N"], 0, "Like rear."),
    ("In a circular queue of size N where rear points just after the last element, the number of elements is", ["(rear − front + N) % N", "rear − front", "N − rear",
                                                                                                                "front + rear"], 0, "The % handles wrap-around."),
    ("In a circular queue that keeps one slot empty, the queue is empty when", ["front == rear", "(rear + 1) % N == front", "rear == N − 1", "front == 0"], 0,
     "(rear + 1) % N == front means full."),
    ("Keeping a separate count of elements lets a circular queue of size n hold", ["n elements", "n − 1 elements", "n + 1 elements", "n/2 elements"], 0,
     "Then empty and full are told apart by the count."),
    ("In an ascending priority queue", ["The element with the smallest key is removed first", "The largest key is removed first", "Elements leave in arrival order",
                                        "The last element inserted leaves first"], 0, "A descending priority queue removes the largest first."),
    ("A priority queue with a few fixed priority levels can be built as", ["One ordinary queue per priority level", "A single stack", "A binary search tree alone",
                                                                           "A circular list of stacks"], 0, "Serve the highest non-empty level first."),
    ("Elements with the same priority in a priority queue are usually served", ["In the order they arrived", "In random order", "Last arrived first", "Alphabetically"], 0,
     "FIFO within a priority."),
    ("An output-restricted deque allows", ["Insertion at both ends but deletion at one end only", "Deletion at both ends but insertion at one end only",
                                           "Insertion and deletion at one end only", "No deletion"], 0, "Input-restricted is the reverse."),
    ("A deque supports", ["Insertion and deletion at both the front and the rear", "Insertion at the rear only", "Deletion at the front only", "Access in the middle"], 0,
     "Four basic operations."),
    ("Which is an application of queues?", ["CPU scheduling and printer spooling", "Evaluating postfix expressions", "Undo in an editor", "Checking brackets"], 0,
     "Also BFS, buffers, call centres."),
    ("A bank simulation with customers waiting for a teller is modelled with a", ["Queue", "Stack", "Tree", "Graph"], 0, "First come, first served."),
    ("In a queue built as a linked list", ["Insertion is at the tail (rear) and deletion at the head (front) – both O(1)", "Both are at the head", "Deletion is at the tail",
                                           "Both need O(n)"], 0, "Keep front and rear pointers."),
    ("Dequeue from a linked queue is", ["t = front; front = front->next; if (front == NULL) rear = NULL; free(t);", "rear = rear->next;", "front = NULL;", "free(rear);"], 0,
     "rear must be reset when the queue becomes empty."),
    ("A linked queue overflows only when", ["Memory for a new node cannot be allocated", "rear == MAX − 1", "front == rear", "It has 100 nodes"], 0, "There is no fixed size."),
    ("Huffman coding repeatedly removes the two smallest weights using a", ["Min priority queue", "Stack", "Circular queue", "Deque"], 0, "A min-heap."),
    ("A priority queue kept as a sorted linked list has", ["O(n) insertion and O(1) removal of the top element", "O(1) insertion and O(1) removal", "O(log n) for both",
                                                           "O(n) for both"], 0, "A heap gives O(log n) for both."),
    ("A circular queue of size 5 (one slot kept empty) starts with front = rear = 0. After enqueue A, B, C, D, then dequeue twice, then enqueue E and F, rear is",
     ["1", "0", "2", "4"], 0, "rear goes 4 after D; E is stored at 4 (rear → 0) and F at 0 (rear → 1)."),
    ("To reverse the order of the elements of a queue, one uses a", ["Stack", "Second queue", "Heap", "Hash table"], 0, "Dequeue all into a stack, then pop all back."),
    ("Inserting and removing only at the front of a deque makes it behave like a", ["Stack", "Queue", "Priority queue", "Heap"], 0, "One end only = LIFO."),
    ("The basic queue ADT operations are", ["enqueue, dequeue, front (peek), isEmpty and isFull", "push and pop", "insert and search", "union and find"], 0, "Push and pop are stack operations."),
    ("A keyboard buffer that stores typed keys until the program reads them is usually a", ["Circular queue", "Stack", "Binary tree", "Graph"], 0, "Keys are read in typing order."),
]

QUEUE_PRACTICE = [
    ("After  enqueue 4, enqueue 7, enqueue 9, dequeue,  the front element is", ["7", "4", "9", "Empty"], 0, "4 left first."),
    ("A linear array queue of size 5 is filled (front = 0, rear = 4), then two elements are dequeued. Can a new element be inserted at the rear?",
     ["No – rear is at MAX − 1, although two cells at the front are free", "Yes, at index 5", "Yes, at index 0", "Only after sorting"], 0,
     PYQ + "This waste is why circular queues are used."),
    ("A circular queue of size 6 has front = 4 and rear = 1 (rear points after the last element). It holds", ["3 elements", "2 elements", "4 elements", "5 elements"], 0,
     "(1 − 4 + 6) % 6."),
    ("In a circular queue of size 6, after rear = 5, the next rear is", ["0", "6", "1", "5"], 0, "(5 + 1) % 6."),
    ("A deque receives insertRear(1), insertFront(2), insertRear(3), deleteFront(). The deque now holds (front to rear)", ["1 3", "2 1", "2 3", "1 2"], 0,
     "It was 2 1 3; 2 is removed."),
    ("A min priority queue receives 5, 1, 4. deleteMin() returns", ["1", "5", "4", "Error"], 0, "The smallest key."),
    ("A max priority queue receives 3, 9, 6. The first two deletions return", ["9, then 6", "3, then 9", "9, then 3", "6, then 3"], 0, "Largest first."),
    ("A queue built from two stacks receives enqueue 1, 2, 3, then one dequeue. The value returned is", ["1", "3", "2", "Error"], 0, "The order is reversed twice."),
    ("In an empty linked queue (front = rear = NULL), after one enqueue", ["front and rear both point to the new node", "front is NULL", "rear is NULL",
                                                                           "front points to NULL and rear to the node"], 0, "The only node is both first and last."),
    ("In round-robin scheduling, P1, P2 and P3 wait in the ready queue. P1 uses its time slice but is not finished. The queue is now", ["P2 P3 P1", "P1 P2 P3", "P3 P2 P1", "P2 P1 P3"], 0,
     "An unfinished process goes to the rear."),
    ("Josephus problem with 5 people in a circle (1 to 5), every 2nd person removed starting from 1. Who survives?", ["3", "5", "1", "4"], 0,
     PYQ + "Removed in order 2, 4, 1, 5."),
    ("After 5 enqueues, 2 dequeues and 1 more enqueue, a queue holds", ["4 elements", "3 elements", "5 elements", "6 elements"], 0, "5 − 2 + 1."),
    ("A circular queue with a count (size 4) receives enqueue a, b, c, d, dequeue, enqueue e. The front element is", ["b", "a", "e", "c"], 0, "b c d e."),
    ("Inserting 1, 2, 3 into a queue and then removing all of them gives", ["1 2 3", "3 2 1", "2 1 3", "1 3 2"], 0, "First in, first out."),
    ("Inserting 1, 2, 3 into a stack and then popping all of them gives", ["3 2 1", "1 2 3", "2 3 1", "3 1 2"], 0, "Last in, first out."),
    ("A circular queue of size 8 (one slot kept empty) has rear = 3 and front = 4. The queue is", ["Full", "Empty", "Holding one element", "Holding 4 elements"], 0,
     "(rear + 1) % 8 == front."),
    ("A circular queue has front = rear = 2. It is", ["Empty", "Full", "Holding 2 elements", "Holding one element"], 0, "With the one-empty-slot convention."),
    ("A circular queue of size 10 has front = 2 and rear = 6 (rear after the last element). It holds", ["4 elements", "5 elements", "6 elements", "8 elements"], 0, "6 − 2."),
    ("Inserting 1 into the min-heap [2, 5, 8] gives a root of", ["1", "2", "5", "8"], 0, "1 bubbles up past 2."),
    ("A deque is convenient for checking palindromes because", ["Characters can be removed from both ends and compared", "It sorts the characters", "It stores only vowels",
                                                                "It reverses in O(1)"], 0, "Compare front and rear until they meet."),
    ("A printer queue holds J1 (3 pages), J2 (1 page) and J3 (2 pages) in this order, one page per minute. J2 finishes after", ["4 minutes", "1 minute", "3 minutes", "6 minutes"], 0,
     "J1 takes 3, then J2 takes 1."),
    ("The queue 1 2 3 (front first) is emptied into a stack, and the stack is then popped completely. The output is", ["3 2 1", "1 2 3", "2 1 3", "3 1 2"], 0,
     "Queue order goes in; the stack reverses it."),
    ("BFS of the tree with root 1, children 2 and 3, and node 4 as the child of 2, using a queue, visits", ["1 2 3 4", "1 2 4 3", "1 3 2 4", "4 2 3 1"], 0, "Level by level."),
    ("A full 4-slot circular keyboard buffer receives a fifth key before any key is read. The fifth key is", ["Rejected (or an old key overwritten), because the buffer is full",
                                                                                                             "Stored in slot 5", "Placed on a stack", "Sorted into place"], 0,
     "Usually the computer beeps."),
    ("In a linear array queue, each dequeue", ["Advances front by one", "Moves every element left", "Moves rear back", "Resets front to 0"], 0, "front++."),
    ("Enqueue and dequeue in a circular array queue take", ["O(1)", "O(n)", "O(log n)", "O(n²)"], 0, "Only index arithmetic."),
    ("If a linear array queue shifts all elements left on every dequeue, dequeue takes", ["O(n)", "O(1)", "O(log n)", "O(n²)"], 0, "Front indexing avoids the shift."),
    ("A priority queue receives A (priority 2), B (priority 1), C (priority 2), where 1 is the highest priority. The service order is", ["B A C", "A B C", "B C A", "A C B"], 0,
     "B first; A and C in arrival order."),
    ("A deque receives insertRear 1, 2, 3. deleteRear() returns", ["3", "1", "2", "Error"], 0, "The rear end behaves like a stack top."),
    ("People join a line at the back and are served at the front. This is a", ["Queue (FIFO)", "Stack (LIFO)", "Tree", "Graph"], 0, "The real-world model of a queue."),
]

SET3 = "3 · Previous-Year Pattern Practice – Programs and Traces"
TOPICS = {
    "Stacks": [
        ("1 · Concepts, Operations and Sequential/Linked Implementation", STACKS),
        ("2 · Applications – Recursion, Tower of Hanoi, Infix to Postfix and Postfix Evaluation", STACK_APPS),
        (SET3, STACK_PRACTICE),
    ],
    "Queues": [
        ("1 · Concepts, Operations and Sequential/Linked Implementation", QUEUES),
        ("2 · Circular Queues, Priority Queues, Deques and Applications", QUEUE_TYPES),
        (SET3, QUEUE_PRACTICE),
    ],
}

NOTES = {
    "Stacks": [{"title": "Stacks – revision sheet", "md": """## Concept and implementation
- LIFO; push, pop, peek/top, isEmpty, isFull – all O(1)
- Array: top = −1 empty, top == MAX − 1 full; push: a[++top] = x; pop: x = a[top--]; overflow / underflow
- Linked (top = head): push t->next = top; top = t; pop temp = top; top = top->next; free(temp)
- Two stacks in one array grow from opposite ends: full when top1 = top2 − 1
- Stack permutations of 1, 2, 3: 5 possible (3 1 2 impossible); of n: Catalan number

## Applications
- Recursion / function calls (activation records); stack overflow on infinite recursion
- Tower of Hanoi: n − 1 to spare, largest to target, n − 1 to target; 2ⁿ − 1 moves (6 discs = 63); odd n → first move smallest disc to target
- Bracket matching, HTML tags, reversing strings, decimal → binary, undo/redo (two stacks), DFS, browser back
- Infix → postfix: operands to output; '(' push; ')' pop to '('; operator: pop ops of ≥ precedence (not for right-associative ^), then push
  - (A + B) * C − D / E → A B + C * D E / −; A + B * C ^ D → A B C D ^ * +; A − B / (C * D ^ E) prefix → − A / B * C ^ D E
- Postfix evaluation: push operands; on operator pop right then left, push result
  - 5 6 2 + * 12 4 / − = 37; 8 2 / 3 * 4 + = 16; prefix + * A B − C D (2, 3, 4, 5) = 5
"""}],
    "Queues": [{"title": "Queues – revision sheet", "md": """## Concept and implementation
- FIFO; enqueue at rear, dequeue at front; also front/peek, isEmpty, isFull
- Linear array: full when rear == MAX − 1 even if front cells are free (wasted space)
- Circular array: rear = (rear + 1) % N, front = (front + 1) % N; one empty slot → empty: front == rear, full: (rear + 1) % N == front, capacity N − 1 (or keep a count to use all N); count = (rear − front + N) % N
- Linked queue: front = head, rear = tail, both O(1); reset rear to NULL when empty
- Queue from two stacks (amortised O(1)); stack from two queues

## Variants
- Priority queue: ascending (min first) / descending (max first); same priority → FIFO; heap → O(log n) insert and delete (sorted list: O(n) insert, O(1) delete); one queue per level
- Deque: insert/delete at both ends; input-restricted (insert at one end, delete at both); output-restricted (insert at both, delete at one)

## Applications
CPU round-robin scheduling, printer spooling, keyboard buffers (circular), BFS, simulations (bank queue), Josephus problem, Dijkstra / Prim / Huffman (min priority queue), palindromes with a deque
"""}],
}
