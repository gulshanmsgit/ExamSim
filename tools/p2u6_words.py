"""P2 · Unit 6 – Operating Systems · the KRIES Operating System syllabus broken down WORD BY WORD (no new questions).
Owner's request (19 Oct 2026): "breakdown each word as notes" for the KRIES CS syllabus. KRIES lists OS 'in detail'; each term
of its syllabus line (tools/make_kries_plan.py) gets a heading in syllabus order with meaning, key facts, example and exam angle.
Numericals match the script-checked ones in p2u6_notes.py."""

TOPICS = {}  # notes only

W = "KRIES syllabus word by word – "

NOTES = {
    "OS Basics": [{"title": W + "OS basics", "md": """> **Syllabus:** History; batch, multiprogrammed, time-sharing, personal, distributed and real-time systems; OS structures – command interpreter, services, system calls, system programs

### History (of operating systems)
- **Means:** how OSs evolved with hardware.
- **Key facts:** 1940s no OS (plugboards) → 1950s **batch** (IBM, punched cards, resident monitor) → 1960s **multiprogramming & time-sharing** (IBM OS/360, CTSS, MULTICS) → 1969 **UNIX** → 1980s personal computers (MS-DOS 1981, Mac OS 1984, Windows 1985) → 1990s Linux (1991), Windows NT → mobile (Android 2008, iOS 2007).
- **Exam point:** MULTICS inspired UNIX; MS-DOS was single-user, single-tasking.

### Batch systems
- **Means:** similar jobs grouped and run one after another without user interaction.
- **Key facts:** operator collects jobs; **spooling** overlaps I/O and computation; CPU idle during I/O; long turnaround.
- **Example:** payroll, bank statements run overnight.
- **Exam point:** no interaction between user and job while it runs.

### Multiprogrammed systems
- **Means:** several jobs kept in memory; when one waits for I/O the CPU runs another.
- **Key facts:** goal = **maximise CPU utilisation**; needs job scheduling, memory management, protection.
- **Example:** while job 1 reads the disk, job 2 computes.
- **Exam point:** degree of multiprogramming = number of processes in memory.

### Time-sharing systems
- **Means:** multitasking – the CPU switches among users so fast that each feels it has its own computer.
- **Key facts:** **time slice/quantum**, round-robin scheduling; goal = **minimise response time**; interactive; virtual memory.
- **Example:** many terminals on one UNIX server.
- **Exam point:** time-sharing = multiprogramming + time slices + interaction.

### Personal (desktop) systems
- **Means:** OS for a single user's PC.
- **Key facts:** focus on convenience and responsiveness (GUI), not utilisation; MS-DOS, Windows, macOS, Linux desktops.
- **Exam point:** personal systems later adopted multitasking and protection from mainframes.

### Distributed systems
- **Means:** many computers connected by a network appear as one system.
- **Key facts:** resource sharing, computation speed-up, **reliability** (one fails, others continue), communication; loosely coupled (own memory and clock); client–server and peer-to-peer.
- **Example:** cloud clusters, Google file system.
- **Exam point:** tightly coupled = multiprocessor (shared memory); loosely coupled = distributed.

### Real-time systems
- **Means:** correctness depends on meeting **deadlines**.
- **Key facts:** **hard** real-time (missing a deadline = failure – airbag, pacemaker, missile) vs **soft** real-time (late is tolerable – video streaming, VoIP); RTOS examples VxWorks, QNX, FreeRTOS.
- **Exam point:** hard real-time systems usually avoid virtual memory (unpredictable delays).

### OS structures
- **Means:** how the OS is organised internally.
- **Key facts:** simple/monolithic (MS-DOS, UNIX), **layered** (THE OS), **microkernel** (Mach, QNX), modular (Linux loadable modules), hybrid (Windows, macOS), virtual machines.
- **Exam point:** a microkernel keeps only minimal services in kernel mode.

### Command interpreter
- **Means:** the program that reads and runs user commands – the **shell**.
- **Key facts:** CLI (bash, cmd, PowerShell) or GUI (Windows Explorer); may run commands itself or start programs (`ls` is a separate program in UNIX).
- **Exam point:** in UNIX the shell is a user program, not part of the kernel.

### Services (of an OS)
- **Means:** functions the OS provides to users and programs.
- **Key facts:** user interface, **program execution**, **I/O operations**, **file-system manipulation**, **communication**, **error detection**; for efficiency: resource allocation, accounting, protection and security.
- **Exam point:** these services are reached through system calls.

### System calls
- **Means:** the programming interface to OS services – a **trap** from user mode into kernel mode.
- **Key facts:** categories: process control (fork, exec, exit, wait), file management (open, read, write, close), device management (ioctl), information (getpid, time), communication (pipe, socket, shmget), protection (chmod); parameters via registers, a table in memory or the stack; APIs: POSIX, Win32.
- **Example:** `printf` → library → `write()` system call.
- **Exam point:** a system call switches the **mode bit** to kernel (0).

### System programs
- **Means:** utilities shipped with the OS that make it usable (not part of the kernel).
- **Key facts:** file management (cp, ls), status information (date, df, top), file modification (editors), programming-language support (compilers, assemblers, debuggers), program loading and execution (loaders, linkers), communication (ssh, ftp, mail), background services (daemons).
- **Exam point:** most users see the OS through system programs, not system calls."""}],

    "Process Management & IPC": [{"title": W + "Process concept, PCB and scheduling", "md": """> **Syllabus:** Process concept, process control block, process scheduling

### Process concept
- **Means:** a **program in execution** – the unit of work in a system.
- **Key facts:** a program is passive (file); a process is active (has a program counter, registers, stack, data section, heap, text); **states**: new, ready, running, waiting (blocked), terminated; one program can create many processes.
- **Example:** two open Notepad windows = two processes of one program.
- **Exam point:** only **one** process can be running on a CPU core at a time.

### Process control block (PCB)
- **Means:** the kernel's record for each process (task control block).
- **Key facts:** contains **process state, PID, program counter, CPU registers, CPU-scheduling information (priority, queue pointers), memory-management information (base/limit, page table), accounting information, I/O status (open files, devices)**.
- **Example:** Linux `task_struct`.
- **Exam point:** a **context switch** saves the old PCB and loads the new one; it is pure overhead.

### Process scheduling
- **Means:** choosing which process runs next and moving processes between queues.
- **Key facts:** queues – **job queue** (all processes), **ready queue**, **device (I/O) queues**; schedulers – **long-term** (admits jobs, controls the degree of multiprogramming), **short-term / CPU scheduler** (picks from the ready queue, runs very often), **medium-term** (swapping); dispatcher does the switch; good mix of I/O-bound and CPU-bound processes.
- **Example:** queueing diagram: ready → CPU → (I/O request → I/O queue → ready) / (time slice expired → ready) / (fork child) / (wait for interrupt).
- **Exam point:** short-term scheduler must be fast; long-term scheduler may be absent in time-sharing systems."""}],

    "CPU Scheduling": [{"title": W + "CPU scheduling", "md": """> **Syllabus:** Basic concepts; FIFO, RR, SJF, multilevel and multilevel feedback queue scheduling

### Basic concepts
- **Means:** deciding which ready process gets the CPU.
- **Key facts:** CPU burst / I/O burst cycle; **preemptive** vs **non-preemptive** scheduling; dispatcher and dispatch latency; criteria – CPU utilisation, throughput (↑), **turnaround time = completion − arrival**, **waiting time = turnaround − burst**, response time (↓).
- **Exam point:** waiting time is the time spent in the **ready queue** only.

### FIFO (first in, first out = FCFS)
- **Means:** the process that arrives first runs first, to completion.
- **Key facts:** non-preemptive; simple queue; **convoy effect** (short jobs stuck behind a long one); poor for time-sharing.
- **Example:** P1 = 24, P2 = 3, P3 = 3 (arrive at 0 in that order) → waiting 0, 24, 27 → average **17**.
- **Exam point:** average waiting time depends heavily on arrival order (order P2, P3, P1 → 3).

### RR (round robin)
- **Means:** each process gets a fixed **time quantum** in turn; unfinished ones go to the back of the ready queue.
- **Key facts:** preemptive; designed for **time-sharing**; quantum too large → FCFS; too small → too many context switches; good response time; no starvation.
- **Example:** P1 = 24, P2 = 3, P3 = 3, q = 4 → P1 0–4, P2 4–7, P3 7–10, P1 10–30 → average waiting **5.67**.
- **Exam point:** with n processes and quantum q, each waits at most (n − 1) × q for its next turn.

### SJF (shortest job first)
- **Means:** run the process with the **smallest next CPU burst**.
- **Key facts:** gives the **minimum average waiting time** (optimal); non-preemptive SJF or preemptive **SRTF** (shortest remaining time first); needs burst prediction (exponential averaging); long jobs may **starve**.
- **Example:** same three processes → order P2, P3, P1 → waiting 0, 3, 6 → average **3**.
- **Exam point:** SJF is a special case of priority scheduling (priority = 1/burst).

### Multilevel queue scheduling
- **Means:** the ready queue is split into **separate fixed queues** (e.g. system, interactive/foreground, batch/background), each with its own algorithm.
- **Key facts:** a process stays in its queue permanently; scheduling between queues by fixed priority (foreground first – risk of starvation) or time slicing (e.g. 80% foreground RR, 20% background FCFS).
- **Exam point:** no movement between queues → inflexible.

### Multilevel feedback queue scheduling
- **Means:** like multilevel queues, but processes **move between queues** according to their behaviour.
- **Key facts:** a process that uses its full quantum moves to a lower-priority queue (CPU-bound sinks); one that waits long moves up (**aging** prevents starvation); defined by number of queues, algorithm per queue, upgrade/demote rules, entry queue.
- **Example:** Q0 RR q = 8, Q1 RR q = 16, Q2 FCFS; new jobs enter Q0.
- **Exam point:** the most **general and complex** CPU-scheduling algorithm."""}],

    "Memory Management": [{"title": W + "Memory management", "md": """> **Syllabus:** Logical and physical address space, swapping, contiguous allocation, paging, segmentation

### Logical address space
- **Means:** the set of addresses a program generates (virtual addresses), starting at 0.
- **Key facts:** generated by the CPU; the program sees only logical addresses; same as physical in compile/load-time binding, different in execution-time binding.
- **Exam point:** logical address = **virtual** address.

### Physical address space
- **Means:** the real addresses in RAM.
- **Key facts:** the **MMU** maps logical → physical at run time; simple scheme: physical = logical + **relocation (base) register**, checked against the **limit register**.
- **Example:** base 14000, logical 346 → physical **14346**.
- **Exam point:** logical address ≥ limit → trap (addressing error).

### Swapping
- **Means:** moving a whole process out of memory to the **backing store** (disk) and back later.
- **Key facts:** lets more processes run than fit in RAM; swap time mostly transfer time (proportional to size); roll out, roll in (priority-based); medium-term scheduler.
- **Example:** a 100 MB process at 50 MB/s → 2 s out + 2 s in.
- **Exam point:** a process waiting for I/O into its buffer should not be swapped out.

### Contiguous allocation
- **Means:** each process gets **one continuous block** of memory.
- **Key facts:** fixed partitions (**internal fragmentation**) or variable partitions with holes (**external fragmentation**); placement – **first fit** (first hole big enough), **best fit** (smallest adequate hole), **worst fit** (largest hole); compaction removes external fragmentation.
- **Example:** holes 100, 500, 200, 300, 600 KB; request 212 KB → first fit 500, best fit 300, worst fit 600.
- **Exam point:** first fit and best fit beat worst fit in practice.

### Paging
- **Means:** physical memory split into fixed **frames**, logical memory into **pages** of the same size; any page can go into any free frame.
- **Key facts:** no external fragmentation (some internal in the last page); address = page number p + offset d; **page table** maps p → frame; **TLB** caches entries (EAT = h(t + m) + (1 − h)(t + 2m)); page size a power of 2 (4 KB).
- **Example:** 32-bit addresses, 4 KB pages → 12-bit offset, 20-bit page number; TLB 20 ns, memory 100 ns, hit 80% → EAT **140 ns**.
- **Exam point:** paging is invisible to the programmer.

### Segmentation
- **Means:** memory divided into variable-size **segments** that match the program's logical parts (main, functions, stack, arrays).
- **Key facts:** address = (segment number, offset); **segment table** has base + limit; offset ≥ limit → trap; supports sharing and protection per segment; causes external fragmentation.
- **Example:** segment 2 base 4300 limit 400 → (2, 53) → **4353**; (2, 450) → trap.
- **Exam point:** segmentation is visible to the programmer; paging is not."""}],

    "Virtual Memory": [{"title": W + "Virtual memory", "md": """> **Syllabus:** Demand paging, page replacement and its algorithms, allocation of frames, thrashing, demand segmentation

### Demand paging
- **Means:** a page is loaded into memory only when it is first referenced (lazy swapper / pager).
- **Key facts:** valid–invalid bit in the page table; access to an invalid page → **page fault** → OS finds a free frame, reads the page from disk, updates the table, restarts the instruction; pure demand paging starts with no pages; EAT = (1 − p) × ma + p × page-fault time.
- **Example:** ma 200 ns, fault 8 ms, p = 0.001 → ≈ 8.2 µs.
- **Exam point:** programs can be larger than physical memory.

### Page replacement
- **Means:** when no frame is free, choose a **victim** page to remove.
- **Key facts:** write it back only if the **dirty (modify) bit** is set; goal = lowest page-fault rate.
- **Exam point:** page replacement completes the separation of logical and physical memory.

### Page-replacement algorithms
- **Means:** rules for picking the victim.
- **Key facts:** **FIFO** (oldest page – suffers **Belady's anomaly**), **Optimal/OPT** (page not used for the longest time in future – lowest faults, not implementable), **LRU** (least recently used – counters or stack), LRU approximations (reference bit, **second chance / clock**), counting (LFU, MFU).
- **Example:** string 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1 with 3 frames → FIFO **15**, OPT **9**, LRU **12** faults.
- **Exam point:** 1 2 3 4 1 2 5 1 2 3 4 5 with FIFO: 3 frames 9 faults, 4 frames 10 (Belady).

### Allocation of frames
- **Means:** how many frames each process gets.
- **Key facts:** minimum set by the architecture; **equal** allocation (m/n each) vs **proportional** (by size: aᵢ = sᵢ/S × m) vs priority; **global** replacement (take from any process) vs **local** (only own frames).
- **Example:** 62 frames, processes of 10 and 127 pages → ≈ 4 and 57 frames proportionally.
- **Exam point:** global replacement gives better throughput but less predictable performance.

### Thrashing
- **Means:** a process spends more time **paging** than executing.
- **Key facts:** cause – too little memory per process (high multiprogramming) → CPU utilisation drops → OS adds more processes → worse; cures – **working-set model** (keep each process's working set in memory; suspend if Σ WSS > frames), **page-fault frequency** control, more RAM.
- **Exam point:** graph of CPU utilisation vs degree of multiprogramming rises, then falls sharply at thrashing.

### Demand segmentation
- **Means:** virtual memory with **segments** instead of pages – a segment is loaded when needed.
- **Key facts:** segment descriptor has a valid bit; missing segment → segment fault; used where paging hardware is lacking (e.g. OS/2 on Intel 80286); segments vary in size, so replacement is harder.
- **Exam point:** less efficient than demand paging because of variable segment sizes."""}],

    "File Systems": [{"title": W + "File systems", "md": """> **Syllabus:** File concept, access methods, directory structure, protection, file-system structure, allocation methods, free-space management

### File concept
- **Means:** a named collection of related information on secondary storage – the smallest unit of logical storage.
- **Key facts:** attributes – name, identifier, type, location, size, protection, time/date, owner; operations – create, write, read, reposition (seek), delete, truncate, open, close; file types by extension (.exe, .c, .txt); open-file table and file pointer.
- **Exam point:** the **FCB** (inode in UNIX) stores the attributes, not the name.

### Access methods
- **Means:** how the records of a file are read.
- **Key facts:** **sequential** (in order – tapes, logs), **direct/relative** (any block by number – databases), **indexed** (an index points to blocks; ISAM, multi-level index).
- **Exam point:** direct access is built on disks; sequential access can be simulated on direct access easily, not the reverse.

### Directory structure
- **Means:** how files are organised into directories.
- **Key facts:** **single-level** (one directory, name clashes) → **two-level** (one per user) → **tree-structured** (subdirectories, absolute/relative paths) → **acyclic graph** (shared files via links) → **general graph** (cycles; garbage collection needed).
- **Example:** `/home/asha/notes.txt` absolute; `../ravi/a.c` relative.
- **Exam point:** links (hard/soft) make the acyclic-graph directory.

### Protection
- **Means:** controlling who can access a file and how.
- **Key facts:** access types read, write, execute, append, delete, list; **access-control lists**; UNIX **owner / group / others** with rwx bits (chmod 754 = rwxr-xr--); passwords on files (old systems).
- **Exam point:** 3 classes × 3 bits = 9 permission bits in UNIX.

### File-system structure
- **Means:** the layers that implement a file system.
- **Key facts:** application programs → **logical file system** (directories, FCBs, protection) → **file-organisation module** (logical → physical blocks, free space) → **basic file system** (generic block read/write, buffers) → **I/O control** (device drivers, interrupts) → devices; on disk: boot block, superblock/volume control block, directory structure, FCBs.
- **Exam point:** the disk is read/written in **blocks**.

### Allocation methods
- **Means:** how disk blocks are given to files.
- **Key facts:** **contiguous** (start + length; fast, external fragmentation, hard to grow), **linked** (each block points to the next; no fragmentation, sequential only; FAT keeps links in a table), **indexed** (index block lists all blocks; direct access; UNIX inode = 12 direct + single, double, triple indirect).
- **Exam point:** linked allocation cannot support direct access efficiently.

### Free-space management
- **Means:** tracking which blocks are free.
- **Key facts:** **bit vector/bitmap** (1 bit per block; 1 TB with 4 KB blocks → 32 MB map), **linked list** of free blocks, **grouping** (first free block stores addresses of n free blocks), **counting** (start address + count of contiguous free blocks).
- **Exam point:** a bitmap makes finding contiguous free blocks easy."""}],

    "Storage Management": [{"title": W + "Secondary storage and disk scheduling", "md": """> **Syllabus:** Secondary storage – disk structure, disk scheduling

### Secondary storage
- **Means:** non-volatile storage that holds programs and data permanently (HDD, SSD, tape, optical).
- **Key facts:** larger, cheaper and slower than RAM; magnetic disks give direct access; tape is sequential (backups); SSDs have no seek time.
- **Exam point:** secondary storage is the backing store for virtual memory and swapping.

### Disk structure
- **Means:** physical and logical layout of a disk.
- **Key facts:** platters → surfaces → **tracks** (circles) → **sectors** (512 B or 4 KB); the same track on all surfaces = **cylinder**; read–write heads on an arm; disk = 1-D array of **logical blocks** mapped sector by sector, track by track, cylinder by cylinder; **access time = seek time + rotational latency + transfer time**.
- **Example:** 7200 rpm → 8.33 ms per rotation → average latency ≈ 4.17 ms.
- **Exam point:** seek time is usually the largest part, so disk scheduling minimises head movement.

### Disk scheduling
- **Means:** ordering pending disk requests to reduce total head movement.
- **Key facts:** **FCFS** (fair, slow), **SSTF** (nearest first – may starve far requests), **SCAN** (elevator – end to end), **C-SCAN** (one direction, jump back – uniform wait), **LOOK / C-LOOK** (turn at the last request).
- **Example:** queue 98, 183, 37, 122, 14, 124, 65, 67, head 53 → FCFS **640**, SSTF **236**, SCAN towards 0 **236**, LOOK towards 0 **208** cylinders.
- **Exam point:** SCAN is called the **elevator** algorithm; read the starting direction before computing."""}],

    "I/O Systems": [{"title": W + "I/O systems", "md": """> **Syllabus:** Overview of I/O systems and I/O interfaces

### Overview of I/O systems
- **Means:** the OS part that controls devices – the **I/O subsystem**.
- **Key facts:** device → **port/bus** (PCIe, USB, SATA) → **controller** (registers: data-in, data-out, status, control) → **device driver** (uniform interface to the kernel); techniques – **polling** (busy-wait on the status bit), **interrupts** (device signals the CPU; interrupt vector, maskable/non-maskable), **DMA** (controller moves blocks to memory, one interrupt at the end); port-mapped vs **memory-mapped I/O**.
- **Example:** keyboard uses interrupts; disk uses DMA.
- **Exam point:** DMA frees the CPU from moving each byte.

### I/O interfaces (application I/O interface)
- **Means:** the standard way programs talk to very different devices.
- **Key facts:** devices grouped by type: **block** (disk – read, write, seek), **character-stream** (keyboard – get, put), **network** (sockets), clocks and timers; differences: sequential/random, synchronous/asynchronous, sharable/dedicated, read-only/write-only/read–write; **blocking**, **non-blocking** and **asynchronous** I/O; escape call `ioctl()`; kernel services – I/O scheduling, **buffering**, **caching**, **spooling** (printers), error handling, protection.
- **Example:** `read()` on a socket blocks until data arrives unless the socket is non-blocking.
- **Exam point:** device drivers hide hardware differences; spooling serves devices that take one job at a time."""}],
}
