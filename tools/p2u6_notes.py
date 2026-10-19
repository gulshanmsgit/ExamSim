"""P2 · Unit 6 – System Software & Operating Systems · revision NOTES for every topic (no new questions).
Owner's request (19 Oct 2026): more notes for KRIES – the KRIES Computer Teacher Paper 2 syllabus asks for Operating System 'in detail',
and the Unit 6 topics had questions but no notes. Same style as the KRIES C / Data Structures notes: definitions, comparison tables,
worked numericals and exam traps. Facts follow Silberschatz (Operating System Concepts, 10th ed.) and Dhamdhere (Systems Programming)."""

TOPICS = {}  # notes only – the question sets come from p2u6_a … p2u6_i

NOTES = {
    "System Software": [{"title": "System software – revision sheet", "md": """## Software types
| Type | Purpose | Examples |
|---|---|---|
| System software | Runs and manages the hardware, supports other programs | OS, assembler, compiler, linker, loader, device drivers |
| Utility software | Maintenance tasks | Antivirus, disk defragmenter, backup, compression |
| Application software | End-user tasks | Word processor, browser, Tally |
| Firmware | Software in ROM/flash | BIOS/UEFI |

## Language levels
- **Machine language** (binary, 1st gen) → **assembly** (mnemonics, 2nd gen) → **high-level** (C, Java, 3rd gen) → **4GL** (SQL) → 5GL (Prolog, AI)
- Low-level = machine dependent, fast; high-level = portable, needs translation

## Translators
| Translator | Input → output | Works | Note |
|---|---|---|---|
| **Assembler** | assembly → machine code | whole program | one-pass / **two-pass** (pass 1 builds the symbol table, pass 2 generates code) |
| **Compiler** | HLL → object code | whole program at once | errors listed after compiling; faster execution (C, C++) |
| **Interpreter** | HLL → executes line by line | statement by statement | stops at first error; slower (Python, BASIC) |
| Cross-compiler | code for another machine | | embedded systems |
| Decompiler / disassembler | reverse direction | | |
- Java: compiler → **bytecode** → **JVM** interprets / JIT-compiles

## Phases of a compiler
1. **Lexical analysis** (scanner) – characters → **tokens**; removes white space/comments (tool: **LEX**)
2. **Syntax analysis** (parser) – tokens → **parse tree**; checks grammar (CFG; tool: **YACC**)
3. **Semantic analysis** – type checking
4. **Intermediate code** – three-address code
5. **Code optimisation** – removes redundancy
6. **Code generation** – target code
- **Symbol table** and **error handler** are used by all phases
- Front end = phases 1–4 (machine independent); back end = 5–6

## Linker, loader, macros
- **Linker** combines object modules + library routines → one executable; resolves **external references**
  - Static linking (copied in at link time) vs **dynamic linking** (DLL / .so loaded at run time)
- **Loader** places the program in memory and starts it: allocation, linking, **relocation**, loading
  - Absolute loader (no relocation), relocating loader, **bootstrap loader** (loads the OS at power-on)
- **Macro** = named block of code expanded in place by the **macro processor** (no call overhead, bigger code); a **subroutine/function** is called (smaller code, call overhead)
- **Debugger** – breakpoints, stepping, watching variables; **editor** – writes source; **profiler** – measures time

## Exam traps
- Compiler finds **all** errors after the whole program; interpreter stops at the **first**
- Lexical analysis output = tokens; parser output = parse tree
- Relocation is done by the **loader** (linker can also relocate in linking loaders)
- Two-pass assembler is needed because of **forward references**"""}],

    "OS Basics": [{"title": "Operating system basics – revision sheet", "md": """## What an OS does
- Interface between user and hardware; **resource manager** (CPU, memory, I/O, files) and **control program**
- Functions: process management, memory management, file management, device (I/O) management, security & protection, networking, user interface (CLI/GUI), error detection, accounting
- **Kernel** = core that stays in memory; **shell** = command interpreter (bash, cmd)

## Types of OS
| Type | Idea | Example |
|---|---|---|
| Batch | Similar jobs grouped, no interaction | early IBM |
| **Multiprogramming** | Several jobs in memory; CPU switches when a job waits for I/O → better CPU use | |
| **Time-sharing / multitasking** | Short time slice per user → fast response | UNIX |
| Multiprocessing | 2+ CPUs share memory (symmetric SMP / asymmetric) | |
| Distributed | Many computers appear as one | Amoeba |
| Network OS | Shares files/printers over a LAN | Windows Server, Novell NetWare |
| **Real-time** | Deadline-bound; **hard** (missile, pacemaker) vs **soft** (video streaming) | VxWorks, RTLinux |
| Embedded / mobile | Device-specific | Android, iOS |

## Structures
- **Simple / monolithic** – everything in one kernel (MS-DOS, early UNIX, Linux is monolithic + modules)
- **Layered** – layer n uses only n−1 (THE OS)
- **Microkernel** – only IPC, scheduling, basic memory in kernel; rest in user space (Mach, QNX, MINIX) → reliable, slower
- **Modular** – loadable kernel modules (Linux, Solaris); **hybrid** – macOS, Windows NT

## Dual mode and system calls
- **Mode bit**: kernel (0) / user (1); privileged instructions only in kernel mode
- **System call** = program's request to the kernel (trap / software interrupt); parameters passed in registers, a memory block or the stack
| Category | UNIX examples |
|---|---|
| Process control | fork(), exec(), exit(), wait() |
| File management | open(), read(), write(), close() |
| Device management | ioctl(), read(), write() |
| Information | getpid(), alarm(), sleep() |
| Communication | pipe(), shmget(), mmap(), socket() |
| Protection | chmod(), umask(), chown() |
- APIs: POSIX (UNIX/Linux/macOS), Win32 (Windows)

## Booting
Power on → **BIOS/UEFI** in ROM runs **POST** → finds boot device → **bootstrap loader** (MBR / GRUB) → loads kernel → init/systemd → login
- Cold boot (power on) vs warm boot (restart)

## Exam traps
- Multiprogramming aims at **CPU utilisation**; time-sharing aims at **response time**
- Interrupt = hardware signal; **trap** = software-generated (system call or error)
- Linux = monolithic with loadable modules, not microkernel"""}],

    "Process Management & IPC": [{"title": "Processes and IPC – revision sheet", "md": """## Process
- Process = program **in execution** (active); program = passive file
- Memory layout: **text** (code), **data** (globals), **heap** (dynamic, grows up), **stack** (locals, calls, grows down)

## Process states (5-state model)
New → **Ready** → (dispatch) → **Running** → (I/O wait) → **Waiting/Blocked** → (I/O done) → Ready; Running → (time-out/interrupt) → Ready; Running → (exit) → **Terminated**
- 7-state model adds **suspended ready** and **suspended blocked** (swapped out)

## PCB (Process Control Block)
Process ID, state, program counter, CPU registers, scheduling info (priority, queue pointers), memory info (base/limit, page table), accounting, I/O status (open files)
- **Context switch** = save PCB of old process + load PCB of new one; pure overhead

## Schedulers
| Scheduler | Chooses | Frequency |
|---|---|---|
| **Long-term** (job) | which jobs enter memory → controls **degree of multiprogramming** | rare |
| **Short-term** (CPU) | which ready process gets the CPU | very often (ms) |
| **Medium-term** | swapping out/in | in between |
- **Dispatcher** gives the CPU to the chosen process; its delay = **dispatch latency**
- I/O-bound vs CPU-bound processes – a good mix keeps devices busy

## Process creation
- UNIX: **fork()** creates a child (copy of parent); returns **0 in child**, child's PID in parent, −1 on error
- **exec()** replaces the memory image; **wait()** parent waits; **exit()** ends
- n fork() calls in sequence → **2ⁿ processes** (2ⁿ − 1 children)
- **Zombie** = finished child whose parent has not called wait(); **orphan** = parent died first (adopted by init/systemd)

## Inter-process communication
| Model | How | Note |
|---|---|---|
| **Shared memory** | common memory region | fast; processes must synchronise |
| **Message passing** | send()/receive() via kernel | easier, good for distributed |
- Direct (name the process) vs indirect (mailbox/port); blocking (synchronous) vs non-blocking (asynchronous)
- **Pipes**: ordinary (unidirectional, parent–child) vs **named pipes / FIFO** (any processes)
- Others: signals, message queues, **sockets** (IP + port), **RPC**, RMI (Java)
- Producer–consumer with a bounded buffer is the classic shared-memory example

## Exam traps
- fork() return value in child = **0**
- 3 fork() → 8 processes
- Long-term scheduler controls the degree of multiprogramming"""}],

    "Process Synchronization": [{"title": "Process synchronization – revision sheet", "md": """## Race condition and critical section
- **Race condition**: result depends on the order of access to shared data
- Critical-section solution must give **mutual exclusion**, **progress**, **bounded waiting**
- Structure: entry section → critical section → exit section → remainder

## Software solutions
- **Peterson's solution** (2 processes): `flag[i] = true; turn = j; while (flag[j] && turn == j);` → satisfies all three
- Strict alternation (turn only) violates **progress**

## Hardware support
- Disable interrupts (only uniprocessor)
- Atomic **test_and_set()** and **compare_and_swap()**; **mutex lock** (acquire/release)
- **Spinlock** = busy waiting; fine for short waits on multiprocessors

## Semaphores (Dijkstra)
- Integer S with atomic **wait(P)**: `S--; if S < 0 block` and **signal(V)**: `S++; if S <= 0 wake one`
- **Binary** (0/1, like mutex) vs **counting** (number of resources)
- Count after operations: S = initial − (number of P) + (number of V); negative value = number of waiting processes
- Problems: deadlock, starvation, **priority inversion** (fix: priority inheritance)

## Classical problems
| Problem | Semaphores |
|---|---|
| **Bounded buffer** (producer–consumer) | mutex = 1, **empty = n**, **full = 0** |
| **Readers–writers** | rw_mutex = 1, mutex = 1, read_count = 0 – many readers or one writer |
| **Dining philosophers** (5) | chopstick[5] = 1; deadlock if all pick left; fixes: max 4 at table, pick both at once, odd/even order |
| Sleeping barber | customers, barbers, mutex |

## Monitors
- High-level construct: only **one process active inside** at a time; **condition variables** with wait() / signal()
- Java `synchronized`, C# lock

## Exam traps
- Peterson's = 2 processes, software only
- Producer: wait(empty) → wait(mutex) → add → signal(mutex) → signal(full); swapping the two waits can deadlock
- Semaphore value −3 → 3 processes blocked"""}],

    "Threads": [{"title": "Threads – revision sheet", "md": """## Thread basics
- Thread = **lightweight process**, basic unit of CPU use: thread ID, program counter, registers, **stack** (own)
- Threads of one process **share** code, data, open files, heap
- Benefits: responsiveness, resource sharing, economy (creating/switching is cheaper), scalability on multicore

| Process | Thread |
|---|---|
| Heavyweight, own address space | Lightweight, shared address space |
| Costly creation and context switch | Cheap |
| Isolated – one crash doesn't kill others | One thread can crash the whole process |
| IPC needed to communicate | Share memory directly |

## Concurrency vs parallelism
- **Concurrency**: tasks make progress by interleaving (possible on one core)
- **Parallelism**: tasks run at the same instant (needs multiple cores); data vs task parallelism
- **Amdahl's law**: speed-up ≤ 1 / (S + (1 − S)/N), S = serial part. Example: S = 25%, N = 2 → 1.6; N → ∞ → 4

## User vs kernel threads
- **User threads**: managed by a library, kernel unaware; fast, but one blocking call blocks all
- **Kernel threads**: managed by the OS; true parallelism

## Multithreading models
| Model | Mapping | Note |
|---|---|---|
| **Many-to-one** | many user → 1 kernel | no parallelism; blocking call blocks all (Green threads) |
| **One-to-one** | each user → 1 kernel | parallel; overhead of many kernel threads (**Linux, Windows**) |
| **Many-to-many** | many user → ≤ kernel threads | flexible; two-level variant also allows 1:1 binding |

## Libraries and implicit threading
- **Pthreads** (POSIX, `pthread_create`, `pthread_join`), **Windows threads** (`CreateThread`), **Java threads** (extend Thread / implement Runnable)
- Implicit: **thread pools**, fork–join, **OpenMP** (`#pragma omp parallel`), Grand Central Dispatch, Intel TBB

## Threading issues
- fork() in a threaded program: copy all threads or only the caller; exec() replaces all
- Signal handling – deliver to the right thread
- **Thread cancellation**: asynchronous (immediate) vs **deferred** (at cancellation points)
- Thread-local storage; scheduler activations (LWP between user and kernel threads)

## Exam traps
- Threads share data/heap/code but **not stack and registers**
- Many-to-one cannot use multiple cores
- Java thread starts with **start()**, not run()"""}],

    "CPU Scheduling": [{"title": "CPU scheduling – revision sheet with worked example", "md": """## Criteria
- Maximise **CPU utilisation**, **throughput**; minimise **turnaround**, **waiting**, **response** time
- **Turnaround time (TAT) = completion − arrival**; **waiting time (WT) = TAT − burst**; **response = first run − arrival**
- Preemptive (CPU can be taken away) vs non-preemptive

## Algorithms
| Algorithm | Preemptive? | Key point |
|---|---|---|
| **FCFS** | No | Simple; **convoy effect** (short jobs wait behind a long one) |
| **SJF** | No | **Optimal average waiting time**; needs burst prediction; starvation of long jobs |
| **SRTF** (preemptive SJF) | Yes | Shortest remaining time first |
| **Priority** | Either | Starvation → fix with **aging**; usually small number = high priority |
| **Round Robin** | Yes | Time quantum q; large q → FCFS; very small q → too many context switches; good response for time-sharing |
| **Multilevel queue** | | Fixed queues (system, interactive, batch), each with its own algorithm |
| **Multilevel feedback queue** | Yes | Processes move between queues → most general/complex |
- Burst prediction: τₙ₊₁ = α·tₙ + (1 − α)·τₙ (exponential averaging)

## Worked example (all arrive at 0)
P1 = 24, P2 = 3, P3 = 3
- **FCFS** (P1, P2, P3): WT = 0, 24, 27 → **avg 17**
- **SJF** (P2, P3, P1): WT = 0, 3, 6 → **avg 3**
- **RR, q = 4**: P1 0–4, P2 4–7, P3 7–10, P1 10–30 → WT P1 = 6, P2 = 4, P3 = 7 → **avg 5.67**

Gantt chart tip: write each slice, then completion times; TAT = CT − AT; WT = TAT − BT.

## Multiprocessor and real-time
- Asymmetric vs **symmetric (SMP)**; **processor affinity** (soft/hard); load balancing (push/pull migration)
- Real-time: **Rate-monotonic** (static priority, shorter period = higher priority; schedulable if U ≤ n(2^(1/n) − 1), ≈ 69% as n → ∞) and **EDF** (earliest deadline first, up to 100%)
- Linux uses **CFS** (Completely Fair Scheduler, red-black tree, vruntime)

## Exam traps
- SJF gives minimum **average waiting time** (provably optimal)
- RR with a very large quantum behaves like **FCFS**
- Starvation in priority scheduling is solved by **aging**"""}],

    "Deadlocks": [{"title": "Deadlocks – revision sheet with Banker's example", "md": """## Four necessary conditions (Coffman) – all must hold
1. **Mutual exclusion** 2. **Hold and wait** 3. **No preemption** 4. **Circular wait**

## Resource-allocation graph (RAG)
- Request edge P → R, assignment edge R → P
- No cycle → no deadlock. Cycle + **single instance** per resource → deadlock. Cycle + multiple instances → **maybe**
- Wait-for graph (single instances): cycle ⇔ deadlock

## Handling methods
| Method | Idea |
|---|---|
| **Prevention** | Break one condition: spool (mutual exclusion), request all at once (hold & wait), allow preemption, **number resources and request in increasing order** (circular wait) |
| **Avoidance** | Grant only if the state stays **safe** – Banker's algorithm |
| **Detection + recovery** | Let it happen, detect cycles, then abort processes or preempt resources (rollback) |
| **Ignore** (ostrich) | Used by most OS (UNIX, Windows) |

## Banker's algorithm
- **Need = Max − Allocation**; Available = total − sum of allocations
- Safety: find a process with Need ≤ Available → it finishes → Available += its Allocation → repeat; if all finish → **safe sequence**
- Example (one resource, 12 units): P0 max 10 alloc 5, P1 max 4 alloc 2, P2 max 9 alloc 2 → available 3; needs 5, 2, 7 → P1 (avail 5) → P0 (avail 10) → P2 → safe ⟨P1, P0, P2⟩

## Formulas
- Minimum resources so that n processes, each needing k, never deadlock: **n(k − 1) + 1**
- Example: 3 processes each need 2 → 4 units guarantee no deadlock

## Exam traps
- Safe state ⇒ no deadlock; **unsafe ≠ deadlock** (only possible)
- Deadlock ≠ starvation (starvation = indefinite waiting while others progress)
- Banker's is for **multiple instances**; RAG cycle check for single instance"""}],

    "Memory Management": [{"title": "Memory management – revision sheet with numericals", "md": """## Address binding
- At **compile** time (absolute code), **load** time (relocatable), **execution** time (needs **MMU**; most OS)
- **Logical (virtual) address** – generated by CPU; **physical address** – seen by memory; MMU maps them
- Base (relocation) register + limit register protect each process

## Contiguous allocation
- Fixed partitions → **internal fragmentation**; variable partitions → **external fragmentation**
- Placement: **first fit** (fast), **best fit** (smallest hole that fits), **worst fit** (largest hole)
- External fragmentation fix: **compaction** or paging; 50-percent rule (first fit loses ~⅓ of memory)
- **Swapping**: move a process to the backing store and back

## Paging
- Physical memory → **frames**; logical → **pages** (same size, power of 2); no external fragmentation, only internal (last page)
- Logical address = page number p + offset d; with 2ᵐ address space and 2ⁿ page size → **p = m − n bits, d = n bits**
- Example: 32-bit address, 4 KB pages → offset 12 bits, page number 20 bits → 2²⁰ entries; at 4 B each → **4 MB page table**
- **TLB** (associative cache of page-table entries); **EAT = h(t + m) + (1 − h)(t + 2m)**
  - Example: TLB 20 ns, memory 100 ns, hit 80% → 0.8×120 + 0.2×220 = **140 ns**
- Large tables: **hierarchical (two-level)**, **hashed**, **inverted** page table (one entry per frame)
- Valid–invalid bit; shared pages (reentrant code)

## Segmentation
- User view: segments (main, stack, symbol table) of different size; address = (segment, offset)
- Segment table: **base + limit**; offset ≥ limit → trap
- External fragmentation possible; **segmented paging** combines both (Intel x86)

| | Paging | Segmentation |
|---|---|---|
| Unit size | fixed | variable |
| Fragmentation | internal | external |
| Visible to programmer | no | yes |

## Exam traps
- Paging removes **external** fragmentation, not internal
- Best fit leaves the smallest leftover holes; worst fit leaves the largest
- Page-table size = number of pages × entry size"""}],

    "Virtual Memory": [{"title": "Virtual memory – revision sheet with page-replacement example", "md": """## Demand paging
- Load a page only when needed; **lazy swapper (pager)**
- **Page fault**: trap → find free frame → read page from disk → update table → restart instruction
- **EAT = (1 − p) × memory access + p × page-fault service time**
  - Example: 200 ns access, 8 ms service, p = 0.001 → ≈ 8.2 µs (40× slower) → keep p tiny
- **Copy-on-write** after fork(); dirty (modify) bit avoids writing clean pages back

## Page replacement (frames = 3, string 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1)
| Algorithm | Rule | Faults |
|---|---|---|
| **FIFO** | Oldest page out | 15 |
| **Optimal (OPT/MIN)** | Page used farthest in future | **9** (lowest possible) |
| **LRU** | Least recently used | 12 |
- **Belady's anomaly**: more frames → more faults; happens in **FIFO**, never in stack algorithms (LRU, OPT)
  - Classic string 1 2 3 4 1 2 5 1 2 3 4 5: FIFO 3 frames = 9 faults, 4 frames = 10 faults
- LRU approximations: reference bit, **second-chance (clock)**, enhanced second chance (ref, modify), LFU/MFU counting

## Frame allocation
- Equal vs proportional allocation; global vs local replacement
- **Thrashing**: process spends more time paging than executing; cause = too many processes / too few frames → CPU use drops → long-term scheduler adds more → worse
- Fixes: **working-set model** (pages used in the last Δ references; if Σ WSS > frames → suspend a process), **page-fault frequency** control
- Locality of reference (temporal, spatial) makes virtual memory work

## Exam traps
- Optimal is not implementable (needs the future); used as a benchmark
- Belady's anomaly → FIFO
- Count the first loads of each page as faults too"""}],

    "Storage Management": [{"title": "Disk storage and scheduling – revision sheet with worked example", "md": """## Disk structure
- Platter → tracks → **sectors**; same track on all platters = **cylinder**
- **Access time = seek time + rotational latency + transfer time**; average latency = ½ rotation
  - 7200 rpm → 8.33 ms per rotation → average latency ≈ **4.17 ms**
- Disk capacity = surfaces × tracks × sectors × bytes per sector
- SSD: no moving parts, no seek; wear levelling; TRIM
- Low-level formatting (sectors), partitioning, logical formatting (file system); boot block; bad-block handling (sector sparing)

## Disk scheduling (queue 98, 183, 37, 122, 14, 124, 65, 67; head at 53; cylinders 0–199)
| Algorithm | Order / idea | Head movement |
|---|---|---|
| **FCFS** | in arrival order | **640** |
| **SSTF** | nearest request first (may starve) | **236** |
| **SCAN** (elevator), towards 0 | 37, 14, **0**, then 65 … 183 | **236** (towards 199: 331) |
| **C-SCAN**, towards 199 | 65 … 183, **199 → 0** jump, 14, 37 | 382 counting the return (183 without it) |
| **LOOK** | like SCAN but turns at the last request | towards 0: **208**; towards 199: 299 |
| **C-LOOK**, towards 199 | like C-SCAN but jumps from the last request (183) to the first (14) | 322 counting the jump (153 without it) |
- SSTF is not optimal and can starve far requests; SCAN/C-SCAN suit heavy load; C-SCAN gives more uniform waiting

## RAID
| Level | Method | Note |
|---|---|---|
| 0 | Striping | Fast, **no redundancy** |
| 1 | **Mirroring** | 50% capacity, high reliability |
| 2 | Bit-level, Hamming code | rare |
| 3 | Byte-level, dedicated parity | |
| 4 | Block-level, dedicated parity disk | parity disk bottleneck |
| **5** | Block-level, **distributed parity** | survives 1 failure, common |
| 6 | Double distributed parity (P + Q) | survives 2 failures |
| 10 (1+0) | Mirror + stripe | fast and safe |

## Exam traps
- RAID 0 has no fault tolerance
- SCAN = elevator algorithm
- Always check the direction given before computing SCAN/LOOK totals"""}],

    "File Systems": [{"title": "File systems – revision sheet", "md": """## File concept
- Attributes: name, identifier, type, location, size, protection, time stamps; kept in the **FCB** (inode in UNIX)
- Operations: create, write, read, reposition (seek), delete, truncate; open-file table + file pointer
- Access methods: **sequential** (tape-like), **direct/relative** (any block by number), **indexed** (index → block, ISAM)

## Directory structures
Single-level → two-level (per user) → **tree** (absolute/relative path names) → **acyclic graph** (sharing via links) → general graph (cycles; needs garbage collection)
- **Hard link** – another name for the same inode; **soft (symbolic) link** – a file holding a path
- **Mounting**: attach a file system at a mount point (`mount /dev/sdb1 /mnt`)
- Protection: UNIX **rwx** for owner/group/others (chmod 754 = rwx r-x r--); access-control lists

## Allocation methods
| Method | How | Pros | Cons |
|---|---|---|---|
| **Contiguous** | start + length | fast sequential & direct access | external fragmentation, file can't grow |
| **Linked** | each block points to next | no external fragmentation | **no direct access**, pointer space, reliability; **FAT** keeps links in a table |
| **Indexed** | index block lists all blocks | direct access, no fragmentation | index overhead; linked / multilevel / **combined (UNIX inode)** |
- UNIX inode: 12 direct + single + double + triple indirect pointers
  - Example: 4 KB blocks, 4 B pointers → 1024 pointers per block → max ≈ 48 KB + 4 MB + 4 GB + 4 TB

## Free-space management
- **Bit vector** (1 bit per block; simple, fast to find runs), **linked list**, **grouping**, **counting** (start + count)
- Example: 1 TB disk, 4 KB blocks → 2²⁸ blocks → bitmap of 32 MB

## Efficiency and recovery
- Unified buffer cache, read-ahead, free-behind
- **Consistency checking** (fsck, chkdsk); **journaling / log-structured** file systems (ext4, NTFS) replay the log after a crash; backups (full, incremental)
- Virtual File System (VFS) layer lets one OS use many file systems; NFS = network file system (RPC based)

## Exam traps
- Linked allocation cannot do direct access efficiently
- FAT = linked allocation with the links kept in a table
- Hard links cannot cross file systems; soft links can"""}],

    "I/O Systems": [{"title": "I/O systems – revision sheet", "md": """## I/O hardware
- Device ↔ **controller** (has data-in, data-out, status, control registers) ↔ bus (PCIe, USB, SATA) ↔ CPU
- **Port-mapped I/O** (special IN/OUT instructions) vs **memory-mapped I/O** (device registers share the address space; ordinary load/store)

## Ways to do I/O
| Method | How | CPU cost |
|---|---|---|
| **Programmed I/O / polling** | CPU keeps checking the busy bit | busy-waiting wastes CPU |
| **Interrupt-driven** | device raises an interrupt when ready | CPU free meanwhile; overhead per word |
| **DMA** | DMA controller moves a whole block between device and memory, interrupts once at the end | best for large transfers; **cycle stealing** |
- Interrupts: maskable vs **non-maskable**; **interrupt vector** table; priority levels; interrupt service routine (ISR)

## Application I/O interface
- Block devices (disk – read/write/seek), character devices (keyboard – get/put), network devices (sockets)
- Blocking, non-blocking and **asynchronous** I/O; device drivers hide hardware details (uniform interface)
- Clocks and timers; `ioctl()` for device-specific commands

## Kernel I/O subsystem
- **I/O scheduling** (queue order)
- **Buffering**: cope with speed mismatch / transfer-size mismatch; single, **double buffering**, circular buffer
- **Caching**: keep a copy of data for speed (a buffer may hold the only copy; a cache holds a copy)
- **Spooling**: queue output for a device that can serve one job at a time (**printer**) – Simultaneous Peripheral Operations On-Line
- Device reservation, error handling, I/O protection (I/O instructions are privileged)
- Life cycle of a request: system call → kernel I/O subsystem → driver → controller → interrupt → back to process

## Exam traps
- DMA interrupts the CPU **once per block**, interrupt-driven I/O once per word/byte
- Spooling is used for **printers**
- Memory-mapped I/O uses normal memory instructions"""}],

    "OS Security": [{"title": "Protection and security – revision sheet", "md": """## Protection vs security
- **Protection** = internal mechanism controlling access of processes/users to resources
- **Security** = defending the system against external and internal attacks; goals **CIA**: confidentiality, integrity, availability
- **Principle of least privilege**; need-to-know; domain of protection = set of (object, rights)

## Access matrix
- Rows = domains, columns = objects, entries = rights (read, write, execute, owner, copy, control, switch)
- Implementations: global table; **access-control list (ACL)** per object (column); **capability list** per domain (row); lock–key
- **Role-based access control (RBAC)**; mandatory (MAC, SELinux) vs discretionary (DAC) access control

## Authentication
- Something you **know** (password, PIN), **have** (OTP token, smart card), **are** (biometrics) → multi-factor
- Passwords stored as **salted hashes**; one-time passwords

## Threats
| Threat | What it is |
|---|---|
| **Trojan horse** | looks useful, does harm |
| **Trap door / back door** | hidden entry left by the programmer |
| **Logic bomb** | runs when a condition is met |
| **Virus** | attaches to programs, needs a host and user action |
| **Worm** | self-replicates over the network, no host needed (Morris worm 1988) |
| Buffer/stack overflow | overwrites return address |
| **DoS / DDoS** | floods a system to deny service |
| Phishing, spoofing, man-in-the-middle, sniffing, ransomware | |

## Cryptography and defences
- **Symmetric** (same key; DES 56-bit, 3DES, **AES** 128/192/256) vs **asymmetric / public-key** (**RSA**, ECC; public key encrypts, private decrypts)
- **Digital signature** = hash signed with the sender's **private** key; verified with the public key
- Hash functions: MD5 (broken), SHA-1, **SHA-256**; certificates from a CA; SSL/TLS
- Defences: firewalls (packet filter, proxy), IDS/IPS (signature vs anomaly), antivirus, patching, auditing/logging, sandboxing

## Exam traps
- Worm needs no host program; virus does
- Digital signature uses the sender's private key
- ACL is per object; capability list is per domain/user"""}],

    "Linux Operating System": [{"title": "Linux – revision sheet with commands", "md": """## Design
- UNIX-like, **open source** (GPL); kernel by **Linus Torvalds, 1991**; GNU tools by Richard Stallman
- **Monolithic kernel with loadable kernel modules** (insmod, rmmod, lsmod, modprobe)
- Components: kernel, system libraries (glibc), system utilities; distributions – Ubuntu, Fedora, Debian, Red Hat
- Everything is a file; multi-user, multitasking

## Basic commands
| Task | Command |
|---|---|
| List / change / print directory | `ls -l`, `cd`, `pwd` |
| Create / remove directory | `mkdir`, `rmdir`, `rm -r` |
| Copy / move / delete | `cp`, `mv`, `rm` |
| Show file | `cat`, `more`, `less`, `head`, `tail` |
| Search text / files | `grep`, `find` |
| Permissions / owner | `chmod 755 f`, `chown` |
| Processes | `ps`, `top`, `kill -9 PID`, `nice`, `&` (background), `jobs`, `fg` |
| Disk | `df` (free space), `du` (usage), `mount` |
| Users | `whoami`, `who`, `passwd`, `su`, `sudo` |
| Others | `wc` (count), `sort`, `man` (help), `echo`, `tar`, `chmod +x` |
- Pipes `|` and redirection `>` (overwrite), `>>` (append), `<` (input)
- chmod digits: r = 4, w = 2, x = 1 → **755 = rwxr-xr-x**, 644 = rw-r--r--

## Internals
- Processes: fork()/exec(); **task_struct** describes a process; threads via clone()
- Scheduling: **CFS** (Completely Fair Scheduler) for normal tasks; real-time FIFO and RR classes; nice values −20 (high) … 19
- Memory: paging, buddy system + slab allocator; swap space; page cache
- File systems: **ext4** (journaling), XFS, Btrfs; **VFS** layer; inode-based
- Directories: `/bin`, `/etc` (config), `/home`, `/root`, `/var` (logs), `/tmp`, `/dev` (devices), `/proc` (process info), `/boot`
- I/O: block, character and network devices; IPC – pipes, FIFOs, signals, shared memory, message queues, semaphores, sockets
- Boot: BIOS/UEFI → GRUB → kernel → **init / systemd** (PID 1) → runlevels / targets

## Exam traps
- Linux is monolithic (modular), not a microkernel
- `kill -9` sends SIGKILL (cannot be caught)
- `/etc` holds configuration files; `/proc` is a virtual file system"""},
        {"title": "UNIX shell, vi and scripting – revision sheet (KRIES: Basic UNIX)", "md": """## UNIX in brief
- **Ken Thompson and Dennis Ritchie**, Bell Labs, **1969**; rewritten in **C in 1973** (hence portable); BSD (Berkeley), System V (AT&T); POSIX standard; Linux and macOS are UNIX-like
- Architecture: **hardware → kernel → shell → utilities/applications**; the **shell** is the command interpreter
- Shells: **sh** (Bourne – Stephen Bourne), **bash** (Bourne Again – default on Linux), **csh** (C shell – Bill Joy), ksh (Korn), zsh; prompt `$` for users, `#` for root
- Multi-user, multitasking, hierarchical file system starting at **/** (root), everything is a file

## Files and permissions
- `ls -l` first character: **-** regular, **d** directory, **l** symbolic link, **c** character device, **b** block device, **p** named pipe, **s** socket
- `-rwxr-x---` → owner rwx (7), group r-x (5), others --- (0) → **750**
- `chmod 644 f` (rw-r--r--), `chmod u+x f`, `chmod go-w f`, `chmod -R 755 dir`; `chown user f`, `chgrp group f`
- **umask** removes permissions from the defaults (files 666, directories 777): umask **022** → files **644**, directories **755**
- Links: `ln a b` (hard link – same inode, same file system), `ln -s a b` (soft/symbolic link – can cross file systems, breaks if the target is deleted)
- Every file has an **inode** (owner, permissions, size, timestamps, block addresses – but **not the name**; names live in directories); `ls -i` shows inode numbers

## Commands by task
| Task | Commands |
|---|---|
| Navigation | `pwd`, `cd ~`, `cd ..`, `ls -la` |
| Files | `cat`, `touch`, `cp -r`, `mv`, `rm -rf`, `mkdir -p`, `rmdir`, `file` |
| View | `more`, `less`, `head -n 5`, `tail -f log` |
| Search | `grep -i "word" f`, `grep -c` (count), `grep -v` (invert), `find / -name "*.c"` |
| **Filters** | `sort` (`-n` numeric, `-r` reverse), `uniq` (adjacent duplicates), `wc -l/-w/-c`, `cut -d: -f1 /etc/passwd`, `tr 'a-z' 'A-Z'`, `sed 's/old/new/g'`, `awk '{print $1}'`, `tee`, `paste`, `diff`, `cmp`, `comm` |
| Processes | `ps -ef`, `top`, `kill -9 PID`, `jobs`, `bg`, `fg`, `nohup cmd &`, `nice -n 10 cmd` |
| Disk/system | `df -h`, `du -sh`, `free`, `uname -a`, `date`, `cal`, `who`, `whoami`, `uptime` |
| Archives | `tar -cvf a.tar dir`, `tar -xvf a.tar`, `gzip`, `zip` |
| Network | `ping`, `ssh`, `scp`, `ftp`, `wget`, `curl`, `ifconfig` / `ip addr` |
| Help | `man ls`, `info`, `whatis`, `which` |
| Scheduling | `cron` / `crontab -e` (min hour day month weekday), `at` |

## Redirection and pipes
- `>` overwrite output, `>>` append, `<` input, **`2>`** errors, `2>&1` errors with output, `/dev/null` discards
- **Pipe** `|` sends one command's output to another: `ls -l | grep "^d" | wc -l` counts directories; `cat f | sort | uniq -c | sort -nr` counts repeated lines
- Wildcards: `*` any string, `?` one character, `[abc]` one of the set

## vi / vim editor
| Mode | Enter with | Use |
|---|---|---|
| **Command (normal)** | Esc (default on start) | move, delete, copy |
| **Insert** | `i` (before cursor), `a` (after), `o` (new line below), `I`, `A`, `O` | type text |
| **Last-line (ex)** | `:` | save, quit, search–replace |
- `:w` save, `:q` quit, **`:wq`** or `:x` or `ZZ` save and quit, **`:q!`** quit without saving
- `dd` delete line, `5dd` five lines, `x` delete character, `yy` copy (yank) line, `p` paste, `u` undo, `/word` search forward, `n` next match, `:%s/old/new/g` replace everywhere, `:set nu` line numbers, `G` last line, `gg` first line, `h j k l` move
- Other editors: ed, ex, emacs, nano

## Shell scripting
```bash
#!/bin/bash
# sum of numbers given as arguments
sum=0
for n in "$@"; do
    sum=$((sum + n))
done
echo "Total of $# numbers: $sum"
```
`bash sum.sh 4 5 6` → **Total of 3 numbers: 15**
- Special variables: **$0** script name, **$1 … $9** arguments, **$#** number of arguments, **$@ / $\\*** all arguments, **$?** exit status of the last command (0 = success), **$$** process ID
- Variables: `name=KRIES` (no spaces around =), use `$name`; `read x` reads input; command substitution `` `date` `` or `$(date)`; arithmetic `$((a + b))` or `expr $a + $b`
- Tests: `if [ $a -gt $b ]; then … elif …; else …; fi`; numeric `-eq -ne -lt -le -gt -ge`; strings `=`, `!=`, `-z` (empty); files `-f` (file exists), `-d` (directory), `-r -w -x`
- Loops: `for i in 1 2 3; do …; done`, `while [ $i -le 5 ]; do …; done`; `case $x in a) … ;; *) … ;; esac`
- Make executable: `chmod +x script.sh`, run `./script.sh`

## Traps
- `rm -r` removes directories recursively; `rmdir` only empty ones
- `$?` = 0 means success in UNIX (opposite of C's true/false habit)
- `uniq` removes only **adjacent** duplicates – sort first
- `>` truncates the file before writing"""}],

    "Windows Operating System": [{"title": "Windows – revision sheet", "md": """## Design principles (Windows NT family → 10/11)
- Goals: security, reliability, compatibility, performance, extensibility, **portability**, international support
- **Hybrid kernel** design: layered + microkernel ideas; written mostly in C/C++
- Layers: **HAL** (Hardware Abstraction Layer) → **kernel** (scheduling, interrupts, synchronisation) → **executive** (object manager, virtual memory manager, process manager, I/O manager, security reference monitor, cache manager, PnP and power manager, ALPC for local IPC)
- Environmental subsystems (Win32, earlier POSIX); WoW64 runs 32-bit apps on 64-bit

## Processes, threads, memory
- Threads are the unit of scheduling; **32 priority levels** (16–31 real-time, 1–15 variable, 0 zero-page thread); preemptive priority scheduling with quantum boosts
- Virtual memory with demand paging, page file (pagefile.sys); working-set manager

## File system – NTFS
- **Master File Table (MFT)**; journaling (log file) for recovery; security descriptors / **ACLs**; compression; **EFS** encryption; hard links, junctions; large volumes; **BitLocker** for full-volume encryption
- FAT32 (max file 4 GB) and exFAT (flash drives) also supported
- Volume management: dynamic disks, RAID 0/1/5 in software; Volume Shadow Copy (snapshots)

## Features and tools
- **Terminal Services / Remote Desktop (RDP)** – many remote sessions on one machine
- **Fast user switching** – several users logged in, switch without logging off
- Registry (hierarchical configuration database: HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER …)
- Tools: Task Manager (Ctrl+Shift+Esc), Control Panel / Settings, Device Manager, Disk Management, Event Viewer, Command Prompt and **PowerShell**, Windows Defender, System Restore
- Networking: SMB file sharing, TCP/IP stack, Active Directory (domains), named pipes, RPC

## Exam traps
- HAL hides hardware differences → portability
- NTFS supports permissions, journaling and encryption; FAT32 has no security
- Fast user switching keeps the other users' sessions running"""}],
}
