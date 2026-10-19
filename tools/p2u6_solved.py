"""P2 · Unit 6 – Operating Systems · SOLVED EXAM PROBLEMS as an extra note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed" – OS is a KRIES 'in detail' area and its
questions are mostly numericals. Every answer below (scheduling with arrival times, Banker's algorithm with three resource
types, paging, semaphores, fork, page replacement, memory placement) was computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

S = "Solved exam problems – "

NOTES = {
    "CPU Scheduling": [{"title": S + "CPU scheduling with arrival times", "md": """**Data** (times in ms): P1 arrives 0, burst 8 · P2 arrives 1, burst 4 · P3 arrives 2, burst 9 · P4 arrives 3, burst 5
Formulas: **TAT = completion − arrival**, **WT = TAT − burst** (= time spent in the ready queue)

### 1. FCFS
Order P1 (0–8), P2 (8–12), P3 (12–21), P4 (21–26)
WT: P1 0, P2 8 − 1 = 7, P3 12 − 2 = 10, P4 21 − 3 = 18 → **average 8.75**

### 2. SJF (non-preemptive)
At 0 only P1 → runs 0–8. At 8: P2 (4), P3 (9), P4 (5) → P2 8–12, P4 12–17, P3 17–26
WT: P1 0, P2 7, P4 9, P3 15 → **average 7.75**

### 3. SRTF (preemptive SJF)
- 0–1 P1 (remaining 7); at 1 P2 arrives with 4 < 7 → **preempt**
- 1–5 P2 (done at 5); then P4 (5) < P1 (7) < P3 (9) → 5–10 P4; 10–17 P1; 17–26 P3
- Completion: P2 5, P4 10, P1 17, P3 26 → WT: P1 17 − 0 − 8 = 9, P2 0, P3 15, P4 2 → **average 6.5** (the smallest)

### 4. Round robin, quantum 4
Gantt: P1 0–4 · P2 4–8 · P3 8–12 · P4 12–16 · P1 16–20 · P3 20–24 · P4 24–25 · P3 25–26
WT: P1 12, P2 3, P3 15, P4 17 → **average 11.75** (convention: processes arriving during a slice join the queue before the preempted process)

### 5. Priority (non-preemptive, all arrive at 0, smaller number = higher priority)
P1 burst 10 pri 3 · P2 1 pri 1 · P3 2 pri 4 · P4 1 pri 5 · P5 5 pri 2
Order P2, P5, P1, P3, P4 → WT 0, 1, 6, 16, 18 → **average 8.2**

### Quick checks
- Average TAT = average WT + average burst
- SRTF/SJF always give the least average waiting time for the same data
- Throughput = processes completed / total time (4 in 26 ms here)"""}],

    "Deadlocks": [{"title": S + "Banker's algorithm with three resource types", "md": """**System**: 5 processes, resources A = 10, B = 5, C = 7 instances
| Process | Allocation (A B C) | Max (A B C) | **Need = Max − Allocation** |
|---|---|---|---|
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |
Available = total − Σ allocation = (10 − 7, 5 − 2, 7 − 5) = **(3, 3, 2)**

### Q1. Is the state safe?
Work = (3, 3, 2)
- P1 needs (1, 2, 2) ≤ work → finishes → work = (5, 3, 2)
- P3 (0, 1, 1) ≤ → work = (7, 4, 3)
- P4 (4, 3, 1) ≤ → work = (7, 4, 5)
- P2 (6, 0, 0) ≤ → work = (10, 4, 7)
- P0 (7, 4, 3) ≤ → work = (10, 5, 7)
**Safe**, sequence ⟨P1, P3, P4, P2, P0⟩ (⟨P1, P3, P0, P2, P4⟩ also works – safe sequences need not be unique)

### Q2. P1 requests (1, 0, 2). Grant it?
1. Request ≤ Need(P1) = (1, 2, 2) ✓ 2. Request ≤ Available (3, 3, 2) ✓
3. Pretend: Available = (2, 3, 0), Allocation(P1) = (3, 0, 2), Need(P1) = (0, 2, 0)
4. Safety check finds ⟨P1, P3, P0, P2, P4⟩ → **grant**

### Q3. Then P0 requests (0, 2, 0)?
Request ≤ Need (7, 4, 3) ✓ and ≤ Available (2, 3, 0) ✓, but after pretending Available = (2, 1, 0) no process's need fits → **unsafe → P0 must wait**

### Q4. Then P4 requests (3, 3, 0)?
Available (2, 3, 0) < request → **cannot be granted** (not enough resources)

### Formula problems
- n processes each needing at most k units of one resource: deadlock impossible if units ≥ **n(k − 1) + 1** (3 processes × 3 units → 7)
- With m units and n processes: deadlock-free if Σ maxᵢ < m + n
- Resource-allocation graph with single instances: cycle ⇔ deadlock"""}],

    "Process Synchronization": [{"title": S + "semaphores and critical sections", "md": """### Q1. Counting semaphore S = 10; 6 P (wait) and 4 V (signal) operations run. Final value?
S = 10 − 6 + 4 = **8**. (If S = 7 and 20 P, 15 V → 2.)

### Q2. S = 1 (binary). Processes P1 and P2 each run `wait(S); CS; signal(S);`
Mutual exclusion holds. If P2 forgets `wait(S)` → both may be in the CS together; if a process forgets `signal(S)` → others block forever (deadlock-like).

### Q3. Bounded buffer with N = 5 slots – initial values?
mutex = 1, **empty = 5**, **full = 0**. After 3 items produced and 1 consumed: empty = 3, full = 2.

### Q4. Two processes, shared x = 0
P1: `x = x + 1;` P2: `x = x − 1;` (each as load–modify–store, no locking)
Possible final values: **−1, 0, +1** (race condition).

### Q5. Count = 5; P1: `count++` and P2: `count--` interleaved at machine level
r1 = count (5); r1 = r1 + 1 (6); r2 = count (5); r2 = r2 − 1 (4); count = r1 (6); count = r2 (**4**) → wrong result (should be 5).

### Q6. Peterson's solution check
`flag[i] = true; turn = j; while (flag[j] && turn == j);` – if you swap the first two lines, mutual exclusion can fail. It gives mutual exclusion, progress and bounded waiting for 2 processes.

### Q7. Deadlock with two semaphores S = Q = 1
P0: wait(S); wait(Q); … P1: wait(Q); wait(S); … → if P0 holds S and P1 holds Q, both wait forever → **deadlock**. Fix: same order of waits in every process.

### Q8. Dining philosophers (5 philosophers, 5 chopsticks)
All pick the left chopstick first → deadlock. Fixes: allow at most 4 at the table, pick both chopsticks atomically, or odd philosophers pick left first and even ones right first.

### Q9. Readers–writers
Readers share (read_count protected by mutex); the first reader waits on rw_mutex, the last reader signals it → writers may **starve** in the first readers–writers problem."""}],

    "Memory Management": [{"title": S + "paging, segmentation and placement", "md": """### Q1. Logical address split
Logical address space 2¹⁶ (64 KB), page size 1 KB (2¹⁰) → **page number 6 bits, offset 10 bits**, 64 pages.
Logical address 3000 → page = 3000 ÷ 1024 = **2**, offset = 3000 mod 1024 = **952**. If page 2 is in frame 5 → physical = 5 × 1024 + 952 = **6072**.

### Q2. Page-table size
32-bit logical addresses, 4 KB pages → 2²⁰ pages; 4-byte entries → **4 MB** per process. With 2-level paging (10 + 10 + 12 bits) each inner table is 4 KB.

### Q3. Physical memory bits
Physical memory 256 MB (2²⁸) with 4 KB frames → 2¹⁶ frames → **16-bit frame number**.

### Q4. Effective access time with TLB
TLB 20 ns, memory 100 ns, hit ratio 80% → 0.8 × (20 + 100) + 0.2 × (20 + 200) = **140 ns**; at 98% → 0.98 × 120 + 0.02 × 220 = **122 ns**.

### Q5. Segmentation
Segment table: seg 0 base 219 limit 600; seg 1 base 2300 limit 14; seg 2 base 90 limit 100; seg 3 base 1327 limit 580; seg 4 base 1952 limit 96
- (0, 430) → 219 + 430 = **649** · (1, 10) → **2310** · (2, 500) → 500 ≥ 100 → **trap** · (3, 400) → **1727** · (4, 112) → 112 ≥ 96 → **trap**

### Q6. Placement (holes 100, 500, 200, 300, 600 KB; requests 212, 417, 112, 426 KB in order)
- **First fit**: 212 → 500 (left 288), 417 → 600 (left 183), 112 → 288, 426 → **must wait**
- **Best fit**: 212 → 300, 417 → 500, 112 → 200, 426 → 600 – **all placed** (best here)
- **Worst fit**: 212 → 600 (388), 417 → 500, 112 → 388, 426 → **must wait**

### Q7. Internal fragmentation
Process of 72,766 bytes with 2,048-byte pages → 35 pages + 1,086 bytes → 36 frames; internal fragmentation = 2,048 − 1,086 = **962 bytes**."""}],

    "Virtual Memory": [{"title": S + "page replacement and EAT", "md": """### Q1. Reference string 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1, 3 frames
| Algorithm | Page faults |
|---|---|
| FIFO | **15** |
| Optimal | **9** |
| LRU | **12** |
Count the first loads as faults. Hit ratio for LRU = (20 − 12)/20 = 40%.

FIFO trace (frames after each fault): 7 · 7 0 · 7 0 1 · 2 0 1 · (0 hit) · 2 3 1 · 2 3 0 · 4 3 0 · 4 2 0 · 4 2 3 · 0 2 3 · (3, 2 hits) · 0 1 3 · 0 1 2 · (0, 1 hits) · 7 1 2 · 7 0 2 · 7 0 1 → 15 faults in all

### Q2. Belady's anomaly
String 1 2 3 4 1 2 5 1 2 3 4 5 with FIFO: 3 frames → **9** faults, 4 frames → **10** faults. LRU/Optimal never show this (stack algorithms).

### Q3. Effective access time with page faults
Memory access 200 ns, fault service 8 ms, p = 1/1000 → EAT = 0.999 × 200 + 0.001 × 8,000,000 ≈ **8.2 µs** (40 × slower). To keep slowdown below 10%: 220 > 200 + 7,999,800 p → **p < 0.0000025** (1 fault in 400,000 accesses).

### Q4. Frame allocation
62 free frames, two processes of 10 and 127 pages → proportional: 10/137 × 62 ≈ **4**, 127/137 × 62 ≈ **57**; equal: 31 each.

### Q5. Working set
Δ = 10, references … 2 6 1 5 7 7 7 7 5 1 | at this point WS = {1, 2, 5, 6, 7} (size 5). If Σ WSS of all processes > available frames → suspend a process to stop thrashing.

### Q6. Second-chance (clock)
Pages with reference bit 1 get a second chance (bit cleared, pointer moves on); the first page found with bit 0 is replaced; if all bits are 1 it degenerates to FIFO."""}],

    "Process Management & IPC": [{"title": S + "fork() and process states", "md": """### Q1. How many processes?
```c
fork(); fork(); fork();
```
Each fork doubles the count → 2³ = **8 processes** (7 new children). n forks in sequence → 2ⁿ.

### Q2. How many times is "Hi" printed?
```c
for (int i = 0; i < 3; i++) fork();
printf("Hi\\n");
```
**8** times (every one of the 8 processes prints once).

### Q3. Conditional fork
```c
if (fork() && fork()) fork();
```
fork #1: child gets 0 → short-circuit, stops. Parent continues: fork #2 – its child gets 0 → stops; the parent (both forks non-zero) runs fork #3. Total processes = **4**.

### Q4. Value seen by parent and child
```c
int x = 5;
if (fork() == 0) { x++; printf("%d ", x); }
else { wait(NULL); printf("%d ", x); }
```
Output: **6 5** – the child has its own copy of x (copy-on-write), so the parent's x stays 5.

### Q5. State transitions
Running → Ready: interrupt / time slice over · Running → Waiting: I/O request or wait() · Waiting → Ready: I/O done · Ready → Running: dispatched · New → Ready: admitted (long-term scheduler)
A process **cannot** go from Waiting directly to Running, or from Ready to Waiting.

### Q6. Context-switch overhead
Time slice 10 ms, switch 1 ms → CPU efficiency = 10/(10 + 1) ≈ **91%**; with a 1 ms slice → 50%."""}],
}
