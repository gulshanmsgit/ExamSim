"""Paper 2 · Unit 3 · P2-U3-09 Memory Hierarchy (2 sets × 30), with revision NOTES.
References: M. Morris Mano, Computer System Architecture (3rd ed., ch. 12); Hamacher, Computer Organization (cache mapping); Hennessy &
Patterson (AMAT). Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers:
KEA final keys for Legislative Council Secretariat 2024 (Sr/Jr Programmer P2, Computer Operator P2, Junior Console Operator P2 – A1) and
GTTC 2024 Lecturer CS (A1). KSET 2023/2025 and KEA 2026 questions come from packs/pyq-p2.json; GFGC 2021 and PGCET answers were worked out by
ExamSim (options read from the page images). Every chip count, address split, hit-ratio and access-time answer was computed."""
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

MAIN_AUX_ASSOC = [
    kset("KEA 2026 CS Paper-2 · Q26"),
    kset("KEA 2026 CS Paper-2 · Q29"),
    ("Match the following in relation to Memory\nList-1\n(a) ROM\n(b) Cache memory\n(c) Virtual memory\n(d) Flash memory\nList-2\ni) Retains data even when power is turned off\n"
     "ii) Reads only memory\niii) Small, fast memory\niv) Provides an illusion of more memory than physically available",
     ["a – i, b – iv, c – iii, d – ii", "a – ii, b – iii, c – iv, d – i", "a – ii, b – i, c – iii, d – iv", "a – iv, b – ii, c – i, d – iii"], 1,
     "ROM – read only; cache – small and fast; virtual memory – illusion of a larger memory; flash – non-volatile." + KLC, "Legislative Council 2024 Computer Operator P2 · Q3"),
    ("What is the correct sequence of storage hierarchy with respect to faster access time?", ["Main Memory → Secondary Memory → Cache Memory",
                                                                                              "Cache Memory → Secondary Memory → Main Memory",
                                                                                              "Cache Memory → Main Memory → Secondary Memory",
                                                                                              "Main Memory → Cache Memory → Secondary Memory"], 2,
     "Fastest first: cache, then main memory, then secondary storage." + KLC, "Legislative Council 2024 Computer Operator P2 · Q12"),
    ("Which memory has the lowest access time ?", ["Cache memory", "Main memory", "Registers", "Optical disk"], 2, "Registers are inside the CPU." + NOTE, "GFGC 2021 CS · Q19"),
    ("Pick the correct sequence which is in the decreasing order of storage capacity.", ["Primary Memory, Magnetic Disk, CPU Registers, Cache",
                                                                                         "CPU Registers, Cache, Primary Memory, Magnetic Disk",
                                                                                         "Magnetic Disk, Primary Memory, Cache, CPU Registers",
                                                                                         "CPU Registers, Primary Memory, Cache, Magnetic Disk"], 2,
     "Largest first: disk, main memory, cache, registers." + NOTE, "PGCET 2024 MCA · Q4"),
    ("What is the meaning of 16 x 8 organizations with respect to memory chip?", ["8 words of 16 bits each", "16 bits × 8 bits", "16 words of 8 bits each",
                                                                                 "16 words of 8 bytes each"], 2, "Words × bits per word." + NOTE, "PGCET 2026 MCA · Q37"),
    ("Arrange the given list of memories as per the size.\n(a) Cache memory\n(b) Registers\n(c) Secondary memory\n(d) Primary memory",
     ["(b), (a), (d), (c)", "(b), (a), (c), (d)", "(a), (b), (c), (d)", "(d), (b), (a), (c)"], 0, "Smallest to largest: registers, cache, primary, secondary." + NOTE,
     "PGCET 2026 MCA · Q41"),
    ("Main memory is built mainly from", ["RAM chips, plus some ROM for the bootstrap loader", "Magnetic tape", "Optical disks", "Registers"], 0,
     PYQ + "Mano, ch. 12."),
    ("The memory hierarchy is used to", ["Give a large, fast memory at a low average cost per bit", "Remove the need for main memory", "Make every memory equally fast",
                                         "Raise the cost"], 0, "It works because of locality of reference."),
    ("Moving down the hierarchy from registers to magnetic tape", ["Capacity increases, cost per bit falls and access time increases", "Capacity falls",
                                                                  "Speed increases", "Cost per bit rises"], 0, "Registers are the fastest and most costly."),
    ("A 128 × 8 RAM chip needs how many address lines?", ["7", "8", "128", "10"], 0, PYQ + "2⁷ = 128 words; 8 data lines."),
    ("How many 128 × 8 RAM chips are needed for 512 bytes of RAM?", ["4", "2", "8", "16"], 0, "512 / 128."),
    ("Selecting one of 4 RAM chips needs a decoder of size", ["2 × 4", "3 × 8", "4 × 16", "1 × 2"], 0, "Two high-order address bits choose the chip."),
    ("A table showing the address range that each RAM and ROM chip occupies is the", ["Memory address map", "Page table", "Symbol table", "Truth table"], 0,
     "Mano's example: RAM 0000–01FF, ROM 0200–03FF."),
    ("The most common auxiliary memory devices are", ["Magnetic disks and magnetic tapes", "Registers", "Cache memories", "ROM chips"], 0, "Plus optical disks and SSDs today."),
    ("Disk access time is", ["Seek time + rotational latency + transfer time", "Seek time alone", "CPU time + seek time", "Twice the transfer time"], 0,
     "Seek usually dominates."),
    ("A disk spins at 6000 rpm. Its average rotational latency is", ["5 ms", "10 ms", "6 ms", "1 ms"], 0, PYQ + "One turn takes 60 / 6000 s = 10 ms; on average half a turn."),
    ("Magnetic tape is mainly suited for", ["Sequential access and backup", "Random access to records", "Cache memory", "Main memory"], 0, "Records are read in order."),
    ("Associative memory is also called", ["Content addressable memory (CAM)", "Read-only memory", "Virtual memory", "Auxiliary memory"], 0, "It is searched by content."),
    ("Associative memory finds a word by", ["Comparing its content with all stored words in parallel", "Its address", "A sequential search", "Hashing"], 0,
     "Much faster than a software search."),
    ("In associative memory, the key register K", ["Masks the argument so that only selected bits are compared", "Holds the address", "Holds the number of matches",
                                                   "Stores data permanently"], 0, "A holds the argument."),
    ("The match register M of an associative memory", ["Has one bit per word, set when that word matches the masked argument", "Holds the key", "Holds addresses",
                                                       "Counts hits"], 0, "Matching words can then be read."),
    ("Associative memory is used only for small, speed-critical tables such as TLBs because", ["Each cell needs comparison logic, which makes it costly", "It is slow",
                                                                                               "It is volatile", "It cannot be written"], 0, "Cost grows with size."),
    ("Cache memories are usually built from", ["SRAM", "DRAM", "EPROM", "Flash"], 0, "SRAM is fast and needs no refresh."),
    ("DRAM must be refreshed periodically because", ["Its capacitors leak charge", "It is non-volatile", "It uses flip-flops", "Its data is compressed"], 0,
     "SRAM uses flip-flops."),
    ("The bootstrap loader is stored in", ["ROM (non-volatile memory)", "RAM", "Cache", "Registers"], 0, "It loads the operating system at power-on."),
    ("Memory interleaving (consecutive addresses in different modules) is used to", ["Overlap accesses and raise the memory bandwidth", "Reduce the memory size", "Add parity",
                                                                                     "Store programs twice"], 0, "Low-order interleaving."),
    ("A solid-state drive (SSD) stores data in", ["Flash memory, with no moving parts", "Magnetic platters", "Optical layers", "DRAM without power"], 0,
     "Faster and more robust than a hard disk."),
    ("CD-ROM and DVD are examples of", ["Optical auxiliary storage", "Magnetic storage", "Primary memory", "Cache memory"], 0, "Read with a laser."),
]

CACHE_VIRTUAL = [
    kset("KSET 2023 CS&A · Q58"),
    kset("KSET 2023 CS&A · Q100"),
    kset("KSET 2025 CS&A · Q16"),
    kset("KSET 2025 CS&A · Q17"),
    ("In a single cache block, the multiple words are put for", ["Exploring references temporal locality in a program", "Reducing the miss penalty",
                                                                 "Exploiting the reference's spatial locality in a program", "None of the above"], 2,
     "Neighbouring words are likely to be used soon." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q19"),
    ("The effectiveness of cache memory is based on the property of", ["Locality of reference", "Memory localisation", "Memory size", "None of the mentioned"], 0,
     "Temporal and spatial locality." + KLC, "Legislative Council 2024 Computer Operator P2 · Q15"),
    ("Given\nL1 Cache: Hit time = 2 cycles, Miss rate = 10%, Miss penalty = 50 cycles\nL2 Cache: Hit time = 10 cycles, Miss rate = 5%, Miss Penalty = 100 cycles\n"
     "What is the average memory access time for the system?", ["3.5 cycles", "2.5 cycles", "4.5 cycles", "1.5 cycles"], 0,
     "AMAT = 2 + 0.10 × (10 + 0.05 × 100) = 2 + 1.5 = 3.5 cycles." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q23"),
    ("Which of the following techniques are used to improve cache hit rates?\na) Increasing cache size\nb) Reducing associativity\nc) Implementing cache prefetching\n"
     "d) Using a victim cache\ne) Increasing the block size", ["a, b, c and d", "a, c, d and e", "a, b and d", "a, b, d and e"], 1,
     "Reducing associativity raises conflict misses." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q26"),
    ("If memory access takes 20 ns with cache and 110 ns without it, then the ratio that the cache uses as 10 ns memory is", ["0.93", "0.9", "0.88", "0.87"], 1,
     "Hit ratio h: 20 = 10h + 110(1 − h) → h = 0.9." + GTTC, "GTTC 2024 Lecturer CS · Q42"),
    ("Which of the following property allows the processor to execute a number of clustered locations ?", ["Coherence", "Spatial", "Temporal", "Inclusion"], 1,
     "Spatial locality: nearby addresses are used together." + NOTE, "GFGC 2021 CS · Q23"),
    ("Which memory is employed to compensate for the speed differential between main memory access time and processor logic in computer systems ?",
     ["Secondary", "Primary", "Cache", "Auxiliary"], 2, "Cache sits between the CPU and main memory." + NOTE, "PGCET 2023 M.Tech CS · Q60"),
    ("A computer with cache access time of 100 ns, a main memory access time of 1000 ns, and a hit ratio of ____ produces an average access time of 200 ns.",
     ["0·9", "0·7", "0·5", "0"], 0, "200 = 100h + 1100(1 − h) (a miss costs cache + memory) → h = 0.9." + NOTE, "PGCET 2023 M.Tech CS · Q61"),
    ("Consider a computer system with a byte addressable memory of size 2³² bytes. Assume the computer system has a direct mapped cache of size 32 KB (1 KB = 2¹⁰ bytes) "
     "and each cache block is of size 64 bytes. The size of the tag field is ____ bits.", ["17", "13", "21", "45"], 0,
     "Offset 6 bits (64 B), index 9 bits (512 lines), tag 32 − 15 = 17." + NOTE, "PGCET 2023 M.Tech CS · Q67"),
    ("The concept of ____ is that the combined size of the program, data, and stack may exceed the amount of physical memory available for it.",
     ["Primary memory", "Virtual memory", "Cache memory", "Logical memory"], 1, "Only the parts in use are kept in main memory." + NOTE, "PGCET 2023 M.Tech CS · Q29"),
    ("Which is the most expensive memory?", ["Pen drive", "DVD", "Cache", "Hard disk"], 2, "Cost per bit is highest near the CPU." + NOTE, "PGCET 2024 M.Tech CS · Q46"),
    ("The fastest memory in a computer system is", ["ROM", "RAM", "Cache memory", "Pen drive"], 2, "Of the options given (registers are faster still)." + NOTE, "PGCET 2024 MCA · Q3"),
    ("The (a) memory is used to (b) the performance mismatch between the (c) memory and the (d).\nThe correct order of words in the above statement is",
     ["(a) Main, (b) Increase, (c) Cache, (d) CPU Registers", "(a) Secondary, (b) Increase, (c) CPU Registers, (d) Main memory",
      "(a) Cache, (b) Decrease, (c) Main, (d) CPU Register", "(a) Cache, (b) Decrease, (c) Main, (d) Secondary memory"], 2,
     "Cache reduces the gap between main memory and the CPU registers." + NOTE, "PGCET 2025 MCA · Q30"),
    ("Select the correct statement(s) from below given statements.\n(i) Cache memory is an extremely fast and small memory between CPU and main memory.\n"
     "(ii) Main memory is an extremely fast and larger memory between CPU and cache memory.", ["Only (ii) is correct", "Only (i) is correct", "Both (i) and (ii) are correct",
                                                                                              "Both (i) and (ii) are wrong"], 1, "Main memory is behind the cache, not between." + NOTE,
     "PGCET 2026 MCA · Q31"),
    ("Consider the following memory access times\nL1 cache hit is equal to 1 cycle.\nL2 cache hit = 5 cycles\nMain memory access = 050 cycles\nDisk access = 10,000 cycles\n"
     "A program has the following probabilities\nL1 hit = 80%, L2 hit = 15% (if L1 missed)\nMain memory hit = 4.85% (if L2 missed)\nDisk access = 0.15 % (if main memory missed)\n"
     "Order the following events from fastest to slowest access time.\ndisk, L1 cache, main memory, L2 cache",
     ["L1 cache, disk, main memory, L2 cache", "L2 cache, disk, main memory, L1 cache", "disk, L2 cache, L1 cache, main memory", "L1 cache, L2 cache, main memory, disk"], 3,
     "1 < 5 < 50 < 10,000 cycles." + NOTE, "PGCET 2026 CS · Q17"),
    ("In direct mapping, main-memory block j goes to cache line", ["j mod (number of cache lines)", "Any free line", "j div (number of lines)", "The least recently used line"], 0,
     PYQ + "Simple, but blocks with the same index conflict."),
    ("In a 4-way set-associative cache, a block can be placed", ["In any of the 4 lines of one particular set", "In any line of the cache", "In exactly one line",
                                                                 "In 4 different sets"], 0, "Set = block number mod number of sets."),
    ("In a write-back cache, main memory is updated", ["When a modified (dirty) block is replaced", "On every write", "Never", "Before every read"], 0,
     "Write-through updates memory on every write."),
    ("The replacement policy that evicts the block unused for the longest time is", ["LRU", "FIFO", "Random", "LFU"], 0, "Least recently used."),
    ("With hit ratio 0.9, cache access 10 ns and memory access 100 ns (Tavg = h·Tc + (1 − h)·Tm), the average access time is", ["19 ns", "10 ns", "28 ns", "100 ns"], 0,
     PYQ + "0.9 × 10 + 0.1 × 100."),
    ("The hardware that translates virtual addresses into physical addresses is the", ["Memory management unit (MMU)", "ALU", "DMA controller", "Cache controller"], 0,
     "It uses the page table and the TLB."),
    ("With an address space of 1M words and a memory space of 32K words, virtual and physical addresses have", ["20 and 15 bits", "15 and 20 bits", "32 and 20 bits",
                                                                                                                "20 and 32 bits"], 0, PYQ + "2²⁰ = 1M; 2¹⁵ = 32K (Mano's example)."),
    ("A page fault occurs when", ["The referenced page is not in main memory", "The cache misses", "The TLB is full", "The page has been modified"], 0,
     "The OS loads the page from disk."),
    ("The translation lookaside buffer (TLB) is", ["A small associative memory holding recent page-table entries", "Part of the disk", "The page table itself",
                                                   "The register file"], 0, "A TLB hit avoids reading the page table in memory."),
    ("Memory management hardware protects memory by", ["Checking access rights (read/write/execute) and bounds stored with each page or segment", "Encrypting memory",
                                                       "Doubling memory", "Using parity bits"], 0, "Violations cause a trap to the OS."),
    ("A direct-mapped 64 KB cache has 16-byte blocks and 32-bit addresses. The tag has", ["16 bits", "12 bits", "4 bits", "20 bits"], 0,
     "Offset 4, index 12 (4096 lines), tag 32 − 16 = 16."),
]

TOPICS = {
    "Memory Hierarchy": [
        ("1 · Main Memory, Auxiliary Memory and Associative Memory", MAIN_AUX_ASSOC),
        ("2 · Cache Memory, Virtual Memory and Memory Management Hardware", CACHE_VIRTUAL),
    ],
}

NOTES = {
    "Memory Hierarchy": [{"title": "Memory hierarchy – revision sheet", "md": """## The hierarchy
Registers → cache (SRAM) → main memory (DRAM) → disk/SSD → tape: capacity and access time increase, cost per bit falls. Works because of
**locality of reference** – temporal (used again soon), spatial (neighbours used soon; why a cache block holds several words), sequential.

## Main memory
- RAM (SRAM: flip-flops, fast, cache; DRAM: capacitors, refresh, main memory); ROM holds the bootstrap loader
- A chip of w × b has log₂ w address lines (128 × 8 → 7); chips = total / chip size (512 B / 128 → 4); 2 × 4 decoder selects 4 chips; memory address map
- k-bit address → 2ᵏ locations (16-bit → 64K); interleaving raises bandwidth

## Auxiliary memory
- Disk: access = seek + rotational latency (half a turn: 6000 rpm → 5 ms) + transfer; tape: sequential, backup; optical (CD/DVD); SSD (flash)

## Associative memory (CAM)
- Searched by content in parallel; argument register A, key (mask) register K, match register M; costly – used for TLBs

## Cache
- Hit ratio h = hits / (hits + misses); Tavg = h·Tc + (1 − h)·Tm (or Tc + (1 − h)·Tm if a miss also spends Tc)
  - 20 ns with cache, 110 without, 10 ns cache → h = 0.9; 100/1000 ns with average 200 → h = 0.9
- AMAT = hit time + miss rate × miss penalty (L1/L2: 2 + 0.1 × (10 + 0.05 × 100) = 3.5)
- Mapping: direct (block mod lines), fully associative (anywhere), k-way set associative
  - Address = tag | index | offset: 2³² bytes, 32 KB cache, 64 B blocks → 17 | 9 | 6; 64 KB, 16 B → 16 | 12 | 4
  - KSET: 128 blocks × 16 words, 4096 memory blocks: direct 5 | 7 | 4, associative 12 | 4, 64 sets 6 | 6 | 4
- Write-through vs write-back (dirty bit); replacement LRU, FIFO, random
- Better hit rate: larger cache, more associativity, prefetching, victim cache, larger blocks (up to a point)

## Virtual memory and memory management hardware
- Address space (virtual) vs memory space (physical): 1M / 32K → 20 / 15 bits
- MMU translates with the page table; TLB caches entries; page fault = page not in memory
- Protection bits and bounds (segments/pages) checked by hardware
"""}],
}
