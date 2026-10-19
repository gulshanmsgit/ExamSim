"""P2 · Unit 5 – Database Management Systems · revision NOTES for every topic (no new questions).
Owner's request (19 Oct 2026): more notes for KRIES (DBMS is named in the KRIES Paper 2 syllabus). The closure / key /
serializability examples were checked with a script on 19 Oct 2026. Facts follow Elmasri & Navathe and Silberschatz.
'DBMS Concepts and Architecture' is built by pack_p2_u5_01_concepts.py, which imports its note from here."""

TOPICS = {}  # notes only – question sets come from p2u5_b … p2u5_f

NOTES = {
    "DBMS Concepts and Architecture": [{"title": "DBMS concepts and architecture – revision sheet", "md": """## Why a DBMS (vs file system)
File systems suffer **redundancy and inconsistency**, difficult access, isolation of data, integrity problems, atomicity problems, concurrent-access anomalies and security problems. A DBMS gives controlled redundancy, sharing, security, integrity constraints, backup/recovery, multiple views.
- Database = related data; DBMS = software (MySQL, Oracle, PostgreSQL, SQL Server); database system = DB + DBMS
- Actors: **DBA** (schema, access, backup, tuning), designers, end users (naive, casual, sophisticated), application programmers

## Data models
| Model | Structure | Example |
|---|---|---|
| Hierarchical | tree (1 : N) | IBM IMS |
| Network | graph (records + sets, M : N) | IDMS, CODASYL |
| **Relational** | tables (E. F. **Codd, 1970**) | Oracle, MySQL |
| Object-oriented / object-relational | objects, classes | PostgreSQL |
| ER model | conceptual design | – |
| NoSQL | key-value, document, column, graph | Redis, MongoDB, Cassandra, Neo4j |
Levels: conceptual (high-level), representational/logical, physical (low-level).

## Schema vs instance
- **Schema** (intension) – the design, changes rarely; **instance / state** (extension) – the data at a moment, changes often
- **Data dictionary / catalog** stores metadata (data about data)

## Three-schema (ANSI/SPARC) architecture
| Level | Describes |
|---|---|
| **External** (view) | what each user group sees – many views |
| **Conceptual** (logical) | whole database: entities, relationships, constraints – one |
| **Internal** (physical) | storage structures, indexes, file organisation – one |
Mappings between levels give **data independence**:
- **Logical** independence – change the conceptual schema without changing external views/programs (harder to achieve)
- **Physical** independence – change the internal schema (indexes, files) without changing the conceptual schema

## Database languages
| Language | Commands |
|---|---|
| **DDL** | CREATE, ALTER, DROP, TRUNCATE, RENAME |
| **DML** | SELECT, INSERT, UPDATE, DELETE (procedural vs declarative/non-procedural – SQL is declarative) |
| **DCL** | GRANT, REVOKE |
| **TCL** | COMMIT, ROLLBACK, SAVEPOINT |
| SDL / VDL | storage / view definition |
Interfaces: menu-based, forms, GUI, natural language, parametric (bank teller), DBA interfaces

## Architectures
- Centralized (one machine); **client/server**: **two-tier** (client app ↔ DB server, ODBC/JDBC) and **three-tier** (client ↔ application/web server ↔ DB server – better security and scalability); distributed and cloud databases
- DBMS components: query processor (DDL interpreter, DML compiler, query optimiser), storage manager (buffer, file, transaction, authorization managers), disk storage

## Traps
- Codd gave the relational model (and 12 rules); Peter **Chen** gave the ER model (1976)
- TRUNCATE is DDL (no rollback in most systems); DELETE is DML
- Physical independence is easier than logical independence"""}],

    "ER Model & Relational Model": [{"title": "ER model and relational model – revision sheet", "md": """## ER model (Peter Chen, 1976) – notation
| Concept | Symbol |
|---|---|
| Entity set | rectangle; **weak entity** – double rectangle |
| Attribute | ellipse; key attribute underlined; multivalued – double ellipse; derived – dashed ellipse; composite – ellipse with sub-ellipses |
| Relationship | diamond; identifying relationship (for a weak entity) – double diamond |
| Total participation | double line; partial – single line |
- Attribute types: simple/composite (name → first, last), single/multivalued (phone numbers), stored/derived (age from DOB), key, NULL
- **Weak entity**: no key of its own → partial key (discriminator, dashed underline) + owner's key; always total participation
- Degree: unary (recursive), binary, ternary
- **Cardinality**: 1 : 1, 1 : N, M : N; (min, max) notation
- Extended ER: specialisation / generalisation (ISA triangle), disjoint vs overlapping, total vs partial; aggregation; categories (union types)

## ER → tables
| ER construct | Table |
|---|---|
| Strong entity | own table, its key = primary key |
| Weak entity | table with owner's key + partial key as primary key |
| 1 : 1 | foreign key on either side (prefer the total-participation side) |
| 1 : N | foreign key on the **N** side |
| **M : N** | **separate table** with both keys (+ relationship attributes) |
| Multivalued attribute | separate table (key + value) |
| Composite attribute | only the simple components |
- Minimum tables: entity sets A, B with M : N → 3; with 1 : N → 2

## Relational model terms
Relation = table; tuple = row; attribute = column; **domain** = allowed values; **degree** = number of attributes; **cardinality** = number of tuples; relation schema R(A1 … An)

## Keys
- **Super key** – any set that identifies tuples uniquely
- **Candidate key** – minimal super key; **primary key** – the chosen one (NOT NULL + UNIQUE); alternate keys – the rest
- **Foreign key** – refers to the primary key of another (or the same) table
- Composite key – more than one attribute; surrogate key – artificial ID
- n attributes → maximum super keys 2ⁿ − 1

## Constraints
Domain, key, **entity integrity** (primary key not NULL), **referential integrity** (foreign key matches an existing primary key or is NULL), semantic constraints (CHECK)
- Update operations and violations: INSERT may break all four; DELETE may break referential integrity → **restrict, cascade, set null, set default**; UPDATE of a key → like delete + insert

## Traps
- M : N always needs a separate relation
- A primary key cannot be NULL; a foreign key can (unless declared NOT NULL)
- Degree = columns, cardinality = rows"""}],

    "Relational Algebra and Relational Calculus": [{"title": "Relational algebra and calculus – revision sheet", "md": """## Operators
| Operator | Symbol | Result |
|---|---|---|
| Select | σ condition (R) | rows satisfying the condition (horizontal) |
| Project | π attributes (R) | chosen columns, **duplicates removed** (vertical) |
| Union | R ∪ S | union-compatible relations |
| Set difference | R − S | in R not in S |
| Cartesian product | R × S | every pair: degree n + m, cardinality p × q |
| Rename | ρ | |
| Intersection | R ∩ S = R − (R − S) | derived |
| **Join** ⋈ | σ on R × S | theta join, equijoin, **natural join** (equal common attributes, one copy kept) |
| Division | R ÷ S | values of R related to **all** tuples of S ("for all" queries) |
| Outer joins | ⟕ ⟖ ⟗ | keep unmatched tuples with NULLs |
- **Fundamental** set: σ, π, ∪, −, ×, ρ (the rest can be derived)
- Union compatibility: same number of attributes and matching domains

## Worked sizes
- R has 3 attributes, 10 tuples; S has 2 attributes, 5 tuples → R × S: degree **5**, cardinality **50**
- R(A, B) ⋈ S(B, C): result tuples between 0 and |R| × |S|; if B is a key of S and a foreign key in R → exactly |R| (when no NULLs)
- σ never changes the degree; π never increases cardinality

## Writing queries (EMP(eno, name, dno, sal), DEPT(dno, dname))
- Names of employees with salary > 50000: **π name (σ sal > 50000 (EMP))**
- Employees with their department names: π name, dname (EMP ⋈ DEPT)
- Departments with no employee: π dno (DEPT) − π dno (EMP)
- Students who took **all** courses: π sid, cid (ENROLL) ÷ π cid (COURSE)

## Relational calculus (non-procedural)
- **Tuple relational calculus (TRC)**: { t | P(t) } → { t | t ∈ EMP ∧ t.sal > 50000 }
- **Domain relational calculus (DRC)**: { ⟨n⟩ | ∃e, d, s (⟨e, n, d, s⟩ ∈ EMP ∧ s > 50000) } (basis of QBE)
- Quantifiers ∃ (exists), ∀ (for all); **safe** expressions return finite results
- Codd's theorem: relational algebra and safe relational calculus have the same expressive power (**relationally complete**); SQL is based on both
- Algebra is **procedural** (says how); calculus is **declarative** (says what)

## Traps
- π removes duplicates (SQL SELECT does not, unless DISTINCT)
- Natural join on relations with no common attribute = Cartesian product
- Division answers "for all" questions"""}],

    "SQL – Part 1": [{"title": "SQL part 1 – DDL, queries and aggregates – revision sheet", "md": """## DDL
```sql
CREATE TABLE emp (
  eno     INT PRIMARY KEY,
  name    VARCHAR(30) NOT NULL,
  dno     INT REFERENCES dept(dno) ON DELETE SET NULL,
  sal     DECIMAL(10,2) CHECK (sal > 0),
  email   VARCHAR(50) UNIQUE,
  joined  DATE DEFAULT CURRENT_DATE
);
ALTER TABLE emp ADD phone VARCHAR(15);
ALTER TABLE emp DROP COLUMN phone;
DROP TABLE emp;          -- structure + data gone
TRUNCATE TABLE emp;      -- all rows gone, structure stays
```
- Data types: CHAR(n) (fixed, padded) vs **VARCHAR(n)** (variable), INT, DECIMAL/NUMERIC(p, s), FLOAT, DATE, TIME, TIMESTAMP, BOOLEAN, BLOB/CLOB
- Constraints: NOT NULL, UNIQUE (allows NULLs), PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT

## SELECT – clause order and execution order
Written: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
Executed: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**
```sql
SELECT dno, COUNT(*) AS n, AVG(sal)
FROM emp
WHERE sal > 20000
GROUP BY dno
HAVING COUNT(*) >= 3
ORDER BY n DESC;
```
- WHERE filters **rows** (no aggregates allowed); HAVING filters **groups**
- Every non-aggregated column in SELECT must appear in GROUP BY

## Operators
- `BETWEEN 10 AND 20` (inclusive), `IN ('A', 'B')`, `LIKE 'S%'` (% any string, _ one char: `'_a%'` = second letter a), `IS NULL` (never `= NULL`), `DISTINCT`, `AND OR NOT`
- Set operations: UNION (removes duplicates), **UNION ALL** (keeps), INTERSECT, EXCEPT/MINUS

## Aggregates and NULL
- COUNT, SUM, AVG, MIN, MAX; **all ignore NULLs except COUNT(*)**
- Salaries 10, 20, NULL, 30 → COUNT(*) = 4, COUNT(sal) = 3, SUM = 60, **AVG = 20** (60/3, not 60/4)
- Any arithmetic or comparison with NULL gives NULL/unknown

## Joins
```sql
SELECT e.name, d.dname FROM emp e JOIN dept d ON e.dno = d.dno;          -- inner
SELECT e.name, d.dname FROM emp e LEFT JOIN dept d ON e.dno = d.dno;     -- all employees
```
INNER, LEFT/RIGHT/FULL OUTER, CROSS (Cartesian), NATURAL, SELF join

## Subqueries
- Second highest salary: `SELECT MAX(sal) FROM emp WHERE sal < (SELECT MAX(sal) FROM emp);`
- `IN`, `EXISTS`, `ANY`, `ALL`; correlated subquery runs once per outer row:
  `SELECT name FROM emp e WHERE sal > (SELECT AVG(sal) FROM emp WHERE dno = e.dno);`

## DML
```sql
INSERT INTO emp (eno, name, sal) VALUES (1, 'Asha', 45000);
UPDATE emp SET sal = sal * 1.10 WHERE dno = 5;
DELETE FROM emp WHERE sal < 10000;      -- without WHERE: every row
```

## Traps
- `= NULL` is never true – use IS NULL
- COUNT(*) counts rows with NULLs; COUNT(col) does not
- ORDER BY is ascending by default; it is the last clause
- DELETE can be rolled back; DROP/TRUNCATE usually cannot"""}],

    "SQL – Part 2": [{"title": "SQL part 2 – views, procedures, triggers, security – revision sheet", "md": """## Views
```sql
CREATE VIEW high_paid AS SELECT eno, name, sal FROM emp WHERE sal > 50000;
SELECT * FROM high_paid;
DROP VIEW high_paid;
```
- A view is a **virtual table** (stored query); simplifies queries, hides columns (security), gives logical independence
- Updatable only if simple (one table, no aggregates/GROUP BY/DISTINCT); `WITH CHECK OPTION` stops updates that would leave the view
- **Materialized view** stores the result (refreshed periodically) – data warehouses

## Stored procedures and functions
```sql
CREATE PROCEDURE raise_sal(IN d INT, IN pct DECIMAL(5,2))
BEGIN
  UPDATE emp SET sal = sal * (1 + pct/100) WHERE dno = d;
END;
CALL raise_sal(5, 10);
```
- Stored in the database, pre-compiled, less network traffic, reusable; parameters IN, OUT, INOUT
- A **function** returns a value and can be used inside SELECT; a procedure is CALLed and may return through OUT parameters
- PL/SQL (Oracle), T-SQL (SQL Server), PL/pgSQL

## Triggers
```sql
CREATE TRIGGER log_sal BEFORE UPDATE ON emp
FOR EACH ROW
BEGIN
  INSERT INTO sal_log VALUES (OLD.eno, OLD.sal, NEW.sal, NOW());
END;
```
- Event–Condition–Action (ECA) rule; BEFORE/AFTER/INSTEAD OF; INSERT/UPDATE/DELETE; row-level vs statement-level; OLD and NEW values
- Uses: auditing, derived values, complex integrity rules; cannot be called directly

## Cursors
Process a query result **row by row** in procedural code: DECLARE → OPEN → FETCH (loop) → CLOSE. Implicit (automatic for single statements) vs explicit cursors; attributes %FOUND, %NOTFOUND, %ROWCOUNT (Oracle)

## Privileges (DCL)
```sql
GRANT SELECT, UPDATE (sal) ON emp TO clerk WITH GRANT OPTION;
REVOKE UPDATE ON emp FROM clerk;     -- CASCADE removes privileges clerk granted onward
```
- Roles group privileges (`CREATE ROLE`); principle of least privilege

## Transactions in SQL
`COMMIT` (make permanent), `ROLLBACK` (undo), `SAVEPOINT s1` / `ROLLBACK TO s1`; DDL usually auto-commits

## SQL injection
- Attack: user input changes the query: `' OR '1'='1` turns `WHERE user = '...' AND pwd = '...'` always true; `'; DROP TABLE users; --`
- Defences: **parameterised queries / prepared statements**, input validation, stored procedures, least privilege, escaping, WAF

## Embedded and dynamic SQL
SQL inside a host language (EXEC SQL in C – precompiler), APIs **ODBC / JDBC**; dynamic SQL builds statements at run time

## Traps
- A view does not store data (unless materialized)
- Triggers fire automatically; procedures are called
- Prepared statements, not string concatenation, stop SQL injection"""}],

    "Normalization": [{"title": "Normalization – revision sheet with worked keys", "md": """## Functional dependencies
- X → Y: equal X values imply equal Y values
- **Armstrong's axioms**: reflexivity (Y ⊆ X ⇒ X → Y), **augmentation** (X → Y ⇒ XZ → YZ), **transitivity** (X → Y, Y → Z ⇒ X → Z) – sound and complete
- Derived: union, decomposition, pseudo-transitivity
- Trivial FD: Y ⊆ X

## Attribute closure and keys – worked
R(A, B, C, D, E), F = {A → B, B → C, CD → E}
- A⁺ = {A, B, C}; **AD⁺ = {A, B, C, D, E}** → AD is a super key; neither A nor D alone → **AD is the only candidate key**
- Tip: attributes never on any right side (A, D) must be in every key

R(A, B, C, D), F = {AB → C, C → D, D → A}
- Candidate keys: **AB, BC, BD** → every attribute is prime → in **3NF** but **not BCNF** (C → D with C not a super key)

- **Canonical (minimal) cover**: single attribute on the right, no extraneous left attributes, no redundant FDs

## Anomalies (why normalise)
Insertion (can't add data without other data), deletion (losing unrelated facts), update (changing many copies) – caused by redundancy

## Normal forms
| NF | Condition |
|---|---|
| **1NF** | atomic values, no repeating groups |
| **2NF** | 1NF + no **partial dependency** (non-prime attribute depending on part of a candidate key) – only an issue with composite keys |
| **3NF** | 2NF + no **transitive dependency**; for every X → A: X is a super key **or** A is prime |
| **BCNF** | for every non-trivial X → A: **X is a super key** |
| 4NF | BCNF + no non-trivial **multivalued dependency** (X →→ Y) |
| 5NF (PJNF) | no non-trivial **join dependency** |
- Every BCNF relation is 3NF; every 3NF is 2NF; a 2-attribute relation is always BCNF

## Decomposition properties
- **Lossless join**: R₁ ∩ R₂ → R₁ or R₁ ∩ R₂ → R₂ (the common attributes are a key of one part)
- **Dependency preserving**: (F₁ ∪ F₂)⁺ = F⁺
- 3NF decomposition can always achieve **both**; BCNF is always lossless but **not always dependency-preserving**

## Worked normalisation
STUDENT(roll, course, name, fee) with roll → name, course → fee, key (roll, course)
- Partial dependencies → not 2NF → split into S(roll, name), C(course, fee), ENROL(roll, course) → all BCNF

## Traps
- 2NF is about **partial** dependency; 3NF about **transitive** dependency
- BCNF is stricter than 3NF
- Denormalisation is sometimes done deliberately for read speed (data warehouses)"""}],

    "Query Processing and Optimization": [{"title": "Query processing and optimization – revision sheet", "md": """## Steps
SQL query → **parsing and translation** (syntax check, relational algebra) → **optimisation** (choose the cheapest evaluation plan) → **evaluation** (query execution engine) → result
- Query tree / evaluation plan = algebra expression + algorithm for each operator

## Cost measures
Mostly **number of disk block transfers and seeks**; also CPU and network. Statistics in the catalog: number of tuples nᵣ, blocks bᵣ, distinct values V(A, r), index height

## Selection algorithms
- Linear scan – bᵣ block transfers (any condition)
- Binary search on a sorted file – ⌈log₂ bᵣ⌉
- Index scans: primary B⁺-tree index (height + 1), secondary index (one block per matching record – can be worse than a scan)

## Join algorithms (r outer, s inner)
| Algorithm | Cost idea | Note |
|---|---|---|
| Nested-loop | nᵣ × bₛ + bᵣ | always works |
| **Block nested-loop** | bᵣ × bₛ + bᵣ | use the smaller relation as outer |
| Indexed nested-loop | bᵣ + nᵣ × c | index on the inner join attribute |
| **Sort-merge** | sort both + bᵣ + bₛ | equijoins, sorted inputs |
| **Hash join** | ≈ 3(bᵣ + bₛ) | equijoins; build + probe phases |
- External sort-merge for relations larger than memory

## Heuristic (rule-based) optimisation
1. Perform **selections as early as possible** (push σ down)
2. Perform projections early (fewer columns)
3. Replace × followed by σ with a **join**
4. Do the most restrictive selections and joins first (smallest intermediate results)
5. Choose join order wisely (left-deep trees)
- Equivalence rules: σ cascades and commutes; joins are commutative and associative; σ distributes over ⋈ when its condition involves one relation

## Cost-based optimisation
Estimate result sizes from statistics (e.g. σ A = v gives nᵣ / V(A, r) tuples), enumerate plans with dynamic programming (System R), choose the cheapest. Materialisation (store temporaries) vs **pipelining** (pass tuples on directly).

## Indexes help
B⁺-tree (range queries, balanced, leaves linked), hash index (equality only), clustered vs non-clustered, dense vs sparse

## Traps
- Optimisation chooses a plan; it does not change the result
- Pushing selections down is the most important heuristic
- Hash join suits only equality joins"""}],

    "Transactions & Concurrency Control": [{"title": "Transactions and concurrency control – revision sheet", "md": """## ACID
| Property | Meaning | Ensured by |
|---|---|---|
| **Atomicity** | all or nothing | recovery manager (undo log) |
| **Consistency** | valid state → valid state | programmer + integrity constraints |
| **Isolation** | concurrent ≈ some serial order | concurrency control |
| **Durability** | committed changes survive failures | recovery manager (redo log) |
States: active → partially committed → **committed**; active → failed → **aborted** (rolled back) → restart or kill

## Problems without control
Lost update, **dirty read** (uncommitted data), unrepeatable read, phantom read, incorrect summary

## Schedules
- Serial vs concurrent; **conflicting operations**: same item, different transactions, at least one **write**
- **Conflict serializable** ⇔ the **precedence graph has no cycle**
  - r1(A) r2(A) w1(A) w2(A) → edges T2 → T1 (r2 before w1) and T1 → T2 (r1 before w2) → **cycle → not conflict serializable**
- View serializable is wider (includes blind writes); every conflict-serializable schedule is view serializable
- **Recoverable**: T commits only after the transactions it read from commit; **cascadeless**: read only committed data; **strict**: no read/write of uncommitted writes
- Number of serial schedules of n transactions = n!

## Locking
- Shared (S, read) and exclusive (X, write) locks; S–S compatible, anything with X conflicts
- **Two-phase locking (2PL)**: growing phase (only acquire) then shrinking phase (only release) → guarantees **conflict serializability**, but deadlocks are possible
- **Strict 2PL**: hold X locks until commit → cascadeless; **rigorous 2PL**: hold all locks until commit
- Lock granularity: database, table, page, row; intention locks (IS, IX, SIX)

## Timestamp ordering
Each transaction gets TS(T); each item keeps read_TS and write_TS
- T reads X: if TS(T) < write_TS(X) → **rollback T**
- T writes X: if TS(T) < read_TS(X) or < write_TS(X) → rollback (**Thomas' write rule**: ignore an obsolete write instead)
- No deadlocks (no waiting), but starvation/cascading rollback possible
- Optimistic (validation) protocol: read → validate → write; MVCC keeps several versions

## Deadlock handling in databases
- Prevention with timestamps: **wait-die** (older waits, younger dies) and **wound-wait** (older wounds/aborts younger, younger waits)
- Detection with a **wait-for graph** (cycle = deadlock) + choose a victim; timeouts

## Isolation levels (SQL)
Read uncommitted (dirty reads possible) < read committed < repeatable read < **serializable** (none of the anomalies)

## Traps
- 2PL ensures serializability, **not** freedom from deadlock
- Consistency is the programmer's job; the others are the DBMS's
- In wait-die only older transactions wait"""}],

    "Database Recovery Techniques": [{"title": "Database recovery – revision sheet", "md": """## Failures
Transaction failure (logical error, deadlock victim), **system crash** (memory lost, disk fine), **disk failure** (media), catastrophes
- Storage: volatile (RAM), non-volatile (disk), **stable** storage (replicated – survives everything in theory)

## Log-based recovery
- Log record: ⟨T start⟩, ⟨T, X, old value, new value⟩, ⟨T commit⟩, ⟨T abort⟩
- **Write-ahead logging (WAL)**: the log record must reach stable storage **before** the data page is written; all log records of T before T commits
- **Deferred update** (NO-UNDO/REDO): changes written to the DB only after commit → after a crash **redo** committed transactions, nothing to undo
- **Immediate update** (UNDO/REDO): changes may reach the DB before commit → **undo** uncommitted, **redo** committed
- Undo goes backwards through the log; redo goes forwards; both are **idempotent**

## Checkpoints
Periodically: write all log records and dirty buffers to disk, write ⟨checkpoint⟩. After a crash only transactions active at or after the last checkpoint need attention.
Worked: log has ⟨checkpoint⟩, T1 committed after it, T2 started after it but never committed, T0 committed before it → **redo T1, undo T2, ignore T0**

## Shadow paging
Keep a shadow page table (old) and a current page table (new); commit = switch the pointer to the current table atomically. No log needed for undo; drawbacks – data fragmentation, garbage collection, hard with concurrency.

## ARIES (IBM)
- Uses WAL, **log sequence numbers (LSN)**, page LSN, dirty page table, transaction table, compensation log records (CLRs)
- Three passes: **Analysis** (find dirty pages and active transactions) → **Redo** (repeat history from the earliest needed point) → **Undo** (roll back losers)
- Steal / no-force buffer policy (most flexible)

## Buffer policies
| | Undo needed? | Redo needed? |
|---|---|---|
| Steal (uncommitted pages may be written) | yes | |
| No-steal | no | |
| Force (write all pages at commit) | | no |
| No-force | | yes |

## Backup
Full, incremental, differential backups; archive logs; remote backup / replication for catastrophes

## Traps
- WAL: log first, data later
- Deferred update needs only REDO; immediate update needs UNDO and REDO
- Checkpoints shorten recovery; they don't replace the log"""}],

    "Data Warehousing and Data Mining": [{"title": "Data warehousing and mining – revision sheet", "md": """## Data warehouse
Bill **Inmon**: a **subject-oriented, integrated, time-variant, non-volatile** collection of data supporting management decisions
| OLTP (operational DB) | OLAP (warehouse) |
|---|---|
| day-to-day transactions | analysis, decisions |
| current, detailed | historical, summarised |
| many short read/write queries | few complex read-mostly queries |
| normalised | denormalised (star schema) |
| clerks, many users | managers, analysts |
- **ETL**: Extract → Transform (clean, integrate) → Load; data marts (department-level, dependent or independent); metadata; Kimball's bottom-up vs Inmon's top-down approach

## Schemas
- **Star**: one central **fact table** (measures + foreign keys) + denormalised **dimension tables**
- **Snowflake**: dimension tables normalised into sub-dimensions
- **Fact constellation (galaxy)**: several fact tables share dimensions

## OLAP operations on a data cube
**Roll-up** (aggregate up a hierarchy – city → state), **drill-down** (reverse), **slice** (fix one dimension), **dice** (sub-cube on several dimensions), **pivot** (rotate)
- MOLAP (multidimensional arrays), ROLAP (relational), HOLAP (hybrid)

## Data mining (KDD process)
Data cleaning → integration → selection → transformation → **mining** → pattern evaluation → knowledge presentation

## Association rules – worked
Transactions: {bread, milk}, {bread, butter}, {bread, milk, butter}, {milk}
- Rule bread → milk: **support** = transactions with both / all = 2/4 = **50%**; **confidence** = 2 / transactions with bread (3) = **66.7%**
- **Apriori**: every subset of a frequent itemset is frequent; generate candidates level by level; FP-growth avoids candidate generation

## Other tasks
| Task | Learning | Algorithms |
|---|---|---|
| **Classification** | supervised (labels known) | decision tree (ID3 uses information gain, C4.5), Naive Bayes, k-NN, SVM, neural networks |
| **Clustering** | unsupervised | **k-means**, hierarchical (agglomerative), DBSCAN |
| **Regression** | supervised, numeric output | linear, logistic (for classification) |
| Outlier detection | | fraud detection |
- Evaluation: accuracy, precision, recall, confusion matrix; overfitting vs underfitting; train/test split, cross-validation

## Traps
- A warehouse is non-volatile (data is not updated in place)
- Classification is supervised; clustering is unsupervised
- Confidence of A → B = support(A ∪ B) / support(A)"""}],
}
