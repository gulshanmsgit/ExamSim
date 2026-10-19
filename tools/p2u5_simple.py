"""P2 · Unit 5 – DBMS · "In simple words" note for every topic (no new questions).
Owner's request (19 Oct 2026): DBMS notes in layman language. Everyday examples (a college office, a bank, a library) explain
each idea before the technical word is used. 'DBMS Concepts and Architecture' lives in packs/p2-u5-01-dbms-concepts.json and
is added by add_concepts_note() (rebuilding that pack would reshuffle its options)."""
import json
from pathlib import Path

TOPICS = {}  # notes only

T = "DBMS in simple words – "

NOTES = {
    "DBMS Concepts and Architecture": [{"title": T + "what a database is", "md": """## The idea
Think of a **college office**. Earlier, every section kept its own register: admissions had one book, the fees counter another, the exam section a third. The same student's name and address were written three times. When the student moved house, one register got the new address and the others didn't. Finding "all girls from Mysuru who paid fees late" meant turning hundreds of pages.

A **database** is one well-organised store of all this information. A **DBMS** (Database Management System – MySQL, Oracle, PostgreSQL) is the software "office clerk" that keeps it, finds things quickly, stops wrong entries, lets many people use it at once and keeps backups.

## Why not just files?
| Problem with separate files | How a DBMS helps |
|---|---|
| Same data written many times (**redundancy**) | stored once, shared |
| Copies disagree (**inconsistency**) | one copy, so no disagreement |
| Hard to search | ask a question in SQL |
| Anyone can change anything | passwords and permissions |
| Two clerks editing together spoil data | it controls who writes when |
| A power cut leaves half-done work | it undoes half-done work |

## Words you must know
- **Data model** – the "shape" in which data is kept. Today almost everyone uses the **relational model** – data in **tables** (E. F. Codd, 1970)
- **Schema** – the plan of the database (what tables, what columns). Like the printed column headings of a register – rarely changes
- **Instance** – the actual data at this moment. Like the entries written in the register today – changes all the time
- **Metadata / data dictionary** – "data about data" (which tables exist, column types)

## Three-level view (ANSI/SPARC)
Think of a **hotel**:
- **External level** – what each guest sees (the room). A student sees only their marks; the accounts clerk sees only fees. Many views
- **Conceptual level** – the manager's full plan of the hotel (all tables and links). One
- **Internal level** – the plumbing and wiring (how data sits on disk, indexes). One
**Data independence**: you can change the wiring without disturbing the rooms (**physical independence**), and change the plan a little without disturbing what guests see (**logical independence** – harder).

## Languages
- **DDL** – builds the shelves: CREATE, ALTER, DROP
- **DML** – puts things on and takes them off: SELECT, INSERT, UPDATE, DELETE
- **DCL** – hands out keys: GRANT, REVOKE
- **TCL** – "save" or "undo": COMMIT, ROLLBACK

## Who's who
**DBA** (database administrator) – the head clerk: designs, gives permissions, takes backups, tunes speed. End users – people who just use the screens. Programmers – write the apps.

## Two-tier vs three-tier
- Two-tier: your app talks **directly** to the database
- Three-tier: your browser → a **web/application server** → the database (like online exam portals) – safer and handles more users"""}],

    "ER Model & Relational Model": [{"title": T + "ER diagrams and tables", "md": """## ER diagram = a drawing before building
Before building a house you draw a plan. Before making tables you draw an **ER (Entity–Relationship) diagram** (Peter Chen, 1976).
- **Entity** – a "thing" we keep data about: Student, Course, Teacher → **rectangle**
- **Attribute** – a detail of the thing: roll number, name → **oval**; the key detail (roll number) is **underlined**
- **Relationship** – how things are linked: Student *enrols in* Course → **diamond**

## Special kinds of attributes
- **Composite** – can be split: Name → first name + last name
- **Multivalued** – can have many values: phone numbers → **double oval**
- **Derived** – can be calculated: age from date of birth → **dashed oval**

## How many? (cardinality)
- **One-to-one (1 : 1)** – one principal heads one college
- **One-to-many (1 : N)** – one department has many teachers
- **Many-to-many (M : N)** – many students take many courses
- Double line = **total participation** (every teacher *must* belong to a department)

## Weak entity
Something that can't be identified on its own. "Dependent" (family member) of an employee – "Ravi's son, age 10" makes sense only with Ravi. Drawn as a **double rectangle**.

## From drawing to tables (simple rules)
1. Each entity → a table; its key → the **primary key**
2. 1 : N → put the "one" side's key into the "many" side's table (**foreign key**) – each teacher row carries its dept number
3. M : N → make a **new table** holding both keys – ENROLS(roll, course_id)
4. Multivalued attribute → its own small table – PHONE(roll, phone)

## Relational model words
| Everyday word | Database word |
|---|---|
| table | **relation** |
| row | **tuple** |
| column | **attribute** |
| allowed values (e.g. marks 0–100) | **domain** |
| number of columns | **degree** |
| number of rows | **cardinality** |

## Keys, simply
- **Super key** – anything that can tell rows apart (roll; roll + name …)
- **Candidate key** – the *smallest* such sets (roll; or Aadhaar number)
- **Primary key** – the one we choose (roll). Can't be empty (NULL) and can't repeat
- **Foreign key** – a column that points to another table's primary key (EMP.dno → DEPT.dno), like a cross-reference in a register

## Rules the database protects (integrity)
- **Entity integrity** – primary key can never be blank
- **Referential integrity** – a foreign key must point to something that exists (you can't put an employee in department 99 if there is no department 99)
- If a department is deleted: refuse (RESTRICT), delete its employees too (CASCADE) or blank their dept (SET NULL)"""}],

    "Relational Algebra and Relational Calculus": [{"title": T + "relational algebra", "md": """## What it is
A small set of **operations on tables** that produce new tables – the maths behind SQL. Imagine a big register of students and a few "tools" to cut and combine pages.

| Tool | Symbol | Think of it as | SQL |
|---|---|---|---|
| **Select** | σ | pick some **rows** (students of CS) | WHERE |
| **Project** | π | pick some **columns** (only names) | SELECT columns |
| **Union** | ∪ | combine two lists | UNION |
| **Difference** | − | in list A but not in B | EXCEPT / NOT IN |
| **Intersection** | ∩ | in both lists | INTERSECT |
| **Cartesian product** | × | pair every row of A with every row of B | FROM A, B |
| **Join** | ⋈ | pair only matching rows (student with their own course) | JOIN |
| **Division** | ÷ | who has done **all** of something (students who took **every** course) | NOT EXISTS twice |
| **Rename** | ρ | give a new name | AS |

## Examples in words
- "Names of CS students" → first **select** CS rows, then **project** the name column: π name (σ dept = 'CS' (STUDENT))
- "Students who took no course" → all students **minus** students in ENROLL
- "Students who took both C1 and C2" → list for C1 **intersect** list for C2

## Easy facts
- Select keeps all columns, fewer rows; project keeps all rows (duplicates removed), fewer columns
- Product of a 3-row table and a 4-row table → **12 rows**
- Union/difference/intersection need **matching columns** (same number and type)
- Natural join = product + keep matching rows + drop the repeated column

## Relational calculus
Instead of saying *how* to get the answer (algebra), you describe *what* you want: "give me every student t such that t is in CS". Tuple calculus uses rows (t), domain calculus uses column values. Both are as powerful as the algebra. SQL mixes both ideas."""}],

    "SQL – Part 1": [{"title": T + "SQL basics", "md": """## SQL = asking the database in near-English
**SQL** (Structured Query Language) is how you talk to a relational database.

## Making the table (DDL)
```sql
CREATE TABLE student (
  roll  INT PRIMARY KEY,      -- unique, never blank
  name  VARCHAR(30) NOT NULL, -- must be filled
  dept  CHAR(3),
  marks INT CHECK (marks BETWEEN 0 AND 100)
);
```
- `VARCHAR(30)` – text up to 30 letters (uses only what it needs); `CHAR(3)` – always exactly 3 (padded)
- `ALTER TABLE` – change the table; `DROP TABLE` – throw away table and data; `TRUNCATE` – empty it but keep the table

## Putting data in and changing it (DML)
```sql
INSERT INTO student VALUES (1, 'Asha', 'CS', 92);
UPDATE student SET marks = 95 WHERE roll = 1;
DELETE FROM student WHERE roll = 1;      -- forget WHERE and every row goes!
```

## Asking questions (SELECT)
```sql
SELECT name, marks          -- which columns
FROM student                -- which table
WHERE dept = 'CS'           -- which rows
ORDER BY marks DESC;        -- in what order
```
- `LIKE 'A%'` – names starting with A; `'_s%'` – second letter s
- `BETWEEN 40 AND 60` – includes 40 and 60; `IN ('CS', 'EC')` – any of these
- `IS NULL` – blank values (never write `= NULL`)
- `DISTINCT` – remove repeats

## Counting and totals
- `COUNT(*)` – how many rows; `SUM`, `AVG`, `MAX`, `MIN`
- **Blanks (NULL) are ignored** by SUM/AVG/COUNT(column): marks 80, 60, blank → AVG = 70, not 46.7
- **GROUP BY** – make piles: `SELECT dept, AVG(marks) FROM student GROUP BY dept;` → one line per department
- **HAVING** – filter the piles: `… HAVING AVG(marks) > 60` (WHERE filters rows *before* piling, HAVING filters piles *after*)

## Joining two tables
`SELECT s.name, d.dname FROM student s JOIN dept d ON s.dept = d.code;` – like matching a roll list with the department list. **LEFT JOIN** keeps all students even if their department is missing (shows blank).

## Order the database follows
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY (that's why you can't use a SELECT nickname inside WHERE)"""}],

    "SQL – Part 2": [{"title": T + "views, procedures, triggers, security", "md": """## View – a saved question
A **view** is a stored SELECT that behaves like a table. Like a "toppers list" notice that always shows the current toppers from the register:
```sql
CREATE VIEW toppers AS SELECT name, marks FROM student WHERE marks > 90;
SELECT * FROM toppers;
```
- It stores no data of its own (unless it is a *materialized* view)
- Used to hide columns (the clerk sees names but not phone numbers) and to make long queries short

## Stored procedure – a saved routine
A set of SQL steps saved inside the database and run by name, like a macro: `CALL give_grace_marks(5);`. Faster and safer than sending the steps every time. A **function** is similar but returns one value and can be used inside SELECT.

## Trigger – an automatic alarm
Runs **by itself** when something happens: "whenever marks are updated, write the old and new marks into a log table". Events: INSERT, UPDATE, DELETE; timing BEFORE or AFTER. You never call a trigger yourself.

## Cursor – reading one row at a time
Normally SQL works on all rows at once. A **cursor** lets a program walk through the result like reading a register line by line: open → fetch → fetch … → close.

## Permissions
- `GRANT SELECT ON student TO clerk;` – the clerk may read
- `REVOKE …` – take it back
- Give each person only what they need (least privilege)

## Saving and undoing
- `COMMIT` – make the changes permanent ("save")
- `ROLLBACK` – cancel the changes since the last commit ("undo")
- `SAVEPOINT s1` – a bookmark you can roll back to

## SQL injection – the classic attack
A login form builds: `SELECT * FROM users WHERE name = '…' AND pass = '…'`. A hacker types the password `' OR '1'='1` → the condition is always true → logged in without a password.
**Defence**: never glue user text into SQL; use **prepared statements / parameterised queries**, check inputs, give the app account few rights."""}],

    "Normalization": [{"title": T + "normalization", "md": """## The problem
One big table: STUDENT_COURSE(roll, name, course, teacher, teacher_phone). If a teacher's phone changes you must fix it in 60 rows (**update problem**). You can't record a new teacher until some student takes the course (**insertion problem**). If the last student drops the course, the teacher's phone is lost too (**deletion problem**). **Normalization** = splitting tables smartly so each fact is stored **once**.

## Functional dependency (FD)
"A → B" means **if you know A, you know B**. Roll → name (a roll number gives exactly one name). Course → teacher. Teacher → phone.

## Key, in this language
A **candidate key** is the smallest set of columns that tells you *everything* in the row. Trick: columns that never appear on the right side of any FD must be in the key.

## Normal forms as a staircase
| Step | Rule in plain words | Fix |
|---|---|---|
| **1NF** | one value per cell – no lists like "Maths, Physics" in one cell | one row per value |
| **2NF** | nothing should depend on **only part** of a combined key | move such columns to their own table |
| **3NF** | non-key columns shouldn't depend on **other non-key** columns (no chains) | move the chain to its own table |
| **BCNF** | the left side of every FD must be a key | split again |
| 4NF / 5NF | no "independent lists" mixed in one table / no hidden join problems | rarely asked beyond definitions |

## Worked example
ENROL(roll, course, name, fee) with roll → name and course → fee; key = (roll, course)
- name depends only on roll (part of the key) → **not 2NF**
- Split: STUDENT(roll, name), COURSE(course, fee), ENROL(roll, course) → each fact once ✓

Chain example: EMP(eno, dno, dname) with eno → dno → dname → dname depends on eno *through* dno → **not 3NF** → split into EMP(eno, dno) and DEPT(dno, dname).

## Good splitting
- **Lossless** – joining the pieces gives back exactly the original (the common column must be a key of one piece)
- **Dependency-preserving** – every rule can still be checked inside one piece
- 3NF can always keep both; BCNF sometimes loses dependency preservation

## Memory line
"The key, the whole key, and nothing but the key" – 1NF (the key), 2NF (the whole key), 3NF (nothing but the key)."""}],

    "Query Processing and Optimization": [{"title": T + "how a query runs", "md": """## What happens after you press Enter
1. **Parsing** – the database checks your SQL spelling and grammar and turns it into an internal form (relational algebra)
2. **Optimisation** – it thinks of many ways to get the same answer and picks the **cheapest** (fewest disk reads)
3. **Execution** – it runs that plan and gives you the rows

Like Google Maps: many routes reach the same place; it picks the fastest.

## Why order matters
"Names of CS students who scored above 90" on 10 lakh students and 50 departments:
- Bad plan: pair every student with every department (crores of pairs), then filter
- Good plan: first keep only CS students with marks > 90 (a few hundred), then join
**Rule 1: filter (select) as early as possible.** Rule 2: keep only needed columns early. Rule 3: join smaller results first.

## How joins are done
- **Nested loop** – for each row of A, scan all of B (simple, slow)
- **Block nested loop** – same, but page by page (fewer disk reads)
- **Index nested loop** – use an index on B (like using a book's index instead of reading every page)
- **Sort-merge** – sort both lists, walk through them together
- **Hash join** – put one table into buckets, look up the other – fast for "=" joins

## Indexes
An **index** is like the index at the back of a textbook: find "Normalization" without reading the whole book. B⁺-trees (good for ranges like marks 60–80) and hash indexes (good for exact matches). Indexes speed up reading but slow down inserts a little.

## Cost
Mostly counted as **disk blocks read** (disk is far slower than memory). The optimiser uses statistics (how many rows, how many distinct values) to guess sizes."""}],

    "Transactions & Concurrency Control": [{"title": T + "transactions and locking", "md": """## Transaction = one complete piece of work
Sending ₹500 from Asha to Ravi = take ₹500 from Asha **and** add ₹500 to Ravi. Both must happen, or neither. That bundle is a **transaction**.

## ACID – four promises
| Letter | Promise | Bank example |
|---|---|---|
| **A**tomicity | all or nothing | if power fails after the debit, the debit is undone |
| **C**onsistency | rules stay true | total money in the bank stays the same |
| **I**solation | others don't see half-done work | Ravi's balance enquiry doesn't see the money "in the air" |
| **D**urability | once done, it stays done | after "Transfer successful", even a crash can't lose it |

## What goes wrong without control
- **Lost update** – two clerks read balance 1000, one adds 100, the other subtracts 50; the last one to save wins (950 instead of 1050)
- **Dirty read** – reading a change that is later cancelled
- **Unrepeatable read** – reading the same value twice gets different answers

## Schedules and serializability
When many transactions run together, their steps interleave. The result is OK if it equals **some one-after-another order** → **serializable**. Check: draw arrows between transactions for each conflicting pair (same item, at least one write); **no circle = OK**.

## Locks – "I'm using this, wait"
- **Shared lock** – many can read together
- **Exclusive lock** – only one can write; nobody else reads or writes
- **Two-phase locking (2PL)**: first a *growing* phase (only take locks), then a *shrinking* phase (only release) → guarantees serializability. Strict 2PL keeps write locks until commit
- **Deadlock**: A waits for B's lock, B waits for A's → both stuck. The DBMS detects it and cancels one (the "victim")

## Timestamps instead of locks
Each transaction gets a token number by arrival time. Older ones go first; a younger one that comes "too late" is rolled back and restarted.

## Isolation levels
From loose to strict: read uncommitted → read committed → repeatable read → **serializable** (safest, slowest)."""}],

    "Database Recovery Techniques": [{"title": T + "recovery after a crash", "md": """## The worry
The power goes off in the middle of fee entry. Some changes reached the disk, some didn't. How does the database come back correct?

## The log – the database's diary
Before changing anything, the DBMS writes in a **log**: "T1 started", "T1 changed fee of roll 7 from 0 to 5000", "T1 committed". **Rule (write-ahead logging): diary first, data later.**

## After a crash
- Transactions that had **committed** → **REDO** them (replay from the diary so nothing is lost)
- Transactions that had **not committed** → **UNDO** them (put back the old values)

## Two styles
- **Deferred update** – don't touch the real data until commit → after a crash only REDO is needed
- **Immediate update** – change data as you go → need both UNDO and REDO

## Checkpoints – bookmarks in the diary
Every few minutes the DBMS saves everything to disk and writes "checkpoint". After a crash it only needs to look at the diary **after the last checkpoint** – much faster.
Example: T0 committed before the checkpoint → ignore; T1 committed after it → redo; T2 never committed → undo.

## Shadow paging
Keep the old copy of the page table (shadow) and work on a new copy. To commit, just switch the pointer to the new copy in one step. If a crash happens before the switch, the old copy is still perfect. No log needed for undo, but it scatters data and is hard with many users.

## ARIES
The method real systems (IBM DB2, SQL Server) use: three passes after a crash – **analysis** (what was going on?), **redo** (repeat history), **undo** (cancel the unfinished).

## Backups
For a disk failure the log is not enough – you need **backups** (full, incremental) and sometimes a remote copy."""}],

    "Data Warehousing and Data Mining": [{"title": T + "data warehouse and data mining", "md": """## Data warehouse – the history room
Your daily database (OLTP) handles today's work: admissions, fee payments – many small, fast updates. Management wants big-picture answers: "How did pass percentages change district-wise over 10 years?" Running that on the busy daily system would slow everyone down.
So data is copied every night into a separate **data warehouse** – a big, read-mostly store of **historical, cleaned, combined** data.
- Bill Inmon's definition: **subject-oriented** (by topic, e.g. "students"), **integrated** (from many sources), **time-variant** (history kept), **non-volatile** (not edited, only added)
- **ETL** = Extract (copy from sources) → Transform (clean, fix formats) → Load (into the warehouse)
- **Data mart** = a small department-level warehouse

## Star schema
A **fact table** in the middle (numbers: marks, fees paid) surrounded by **dimension tables** (who, what, when, where: student, subject, year, district) – looks like a star. **Snowflake** = the dimensions split further.

## OLAP – slicing the data cube
Think of a cube: districts × years × subjects.
- **Roll-up** – zoom out (taluk → district → state)
- **Drill-down** – zoom in (year → month)
- **Slice** – fix one thing (only 2025)
- **Dice** – a smaller cube (2024–25, Mysuru and Mandya, Maths and Science)
- **Pivot** – turn the table around

## Data mining – finding hidden patterns
- **Association rules** – "students who take Computer Science also take Maths" (market basket: bread → butter). **Support** = how often both appear; **confidence** = when the first appears, how often the second also does
- **Classification** – sort into known groups with labelled examples (pass/fail prediction, spam/not spam) – supervised
- **Clustering** – find natural groups without labels (group schools by performance) – unsupervised; k-means
- **Regression** – predict a number (next year's admissions)
- **Outlier detection** – spot unusual cases (fraud)

## OLTP vs OLAP in one line
OLTP runs the office today; OLAP helps plan for tomorrow."""}],
}


def add_concepts_note():
    """Put the DBMS Concepts note into packs/p2-u5-01-dbms-concepts.json without touching the questions (re-run safe)."""
    path = Path(__file__).resolve().parent.parent / "packs" / "p2-u5-01-dbms-concepts.json"
    raw = path.read_text(encoding="utf-8")
    pack = json.loads(raw)
    t = pack["subjects"][0]["topics"][0]
    mine = {n["title"] for n in NOTES[t["name"]]}
    t["notes"] = [n for n in t.get("notes", []) if n["title"] not in mine] + NOTES[t["name"]]
    path.write_text(json.dumps(pack, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")


if __name__ == "__main__":
    add_concepts_note()
