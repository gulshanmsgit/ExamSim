"""P2 · Unit 5 – DBMS · SOLVED EXAM PROBLEMS as an extra note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". SQL outputs were produced by running the queries
in SQLite; candidate keys, normal forms and precedence graphs were computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

S = "Solved exam problems – "

NOTES = {
    "SQL – Part 1": [{"title": S + "SQL query outputs", "md": """**Tables**
EMP(eno, name, dno, sal): (1, Asha, 10, 50000) · (2, Ravi, 20, 40000) · (3, Meena, 10, 60000) · (4, Kiran, 30, NULL) · (5, John, 20, 40000) · (6, Leela, NULL, 30000)
DEPT(dno, dname): (10, CS) · (20, EC) · (40, ME)

| # | Query | Result |
|---|---|---|
| 1 | `SELECT COUNT(*), COUNT(sal), COUNT(DISTINCT sal), SUM(sal), AVG(sal) FROM emp;` | 6, 5, 4, 220000, **44000** (NULL ignored: 220000/5) |
| 2 | `SELECT dno, COUNT(*), MAX(sal) FROM emp GROUP BY dno;` | NULL 1 30000 · 10 2 60000 · 20 2 40000 · 30 1 NULL – NULLs form one group |
| 3 | `… GROUP BY dno HAVING COUNT(*) > 1;` with AVG(sal) | 10 → 55000 · 20 → 40000 |
| 4 | `SELECT e.name, d.dname FROM emp e JOIN dept d ON e.dno = d.dno;` | Asha CS · Ravi EC · Meena CS · John EC (4 rows – Kiran, Leela and ME drop out) |
| 5 | same with `LEFT JOIN` | 6 rows; Kiran and Leela get NULL dname |
| 6 | `SELECT COUNT(*) FROM emp, dept;` | **18** (Cartesian product 6 × 3) |
| 7 | Second highest: `SELECT MAX(sal) FROM emp WHERE sal < (SELECT MAX(sal) FROM emp);` | **50000** |
| 8 | `SELECT name FROM emp WHERE sal > (SELECT AVG(sal) FROM emp);` | Asha, Meena (> 44000) |
| 9 | `SELECT name FROM emp WHERE name LIKE '_e%';` | Meena, Leela (2nd letter e) |
| 10 | `SELECT name FROM emp WHERE sal BETWEEN 40000 AND 50000;` | Asha, Ravi, John (inclusive) |
| 11 | `SELECT name FROM emp WHERE dno NOT IN (10, 20);` | **Kiran only** – Leela's NULL dno makes the test unknown, so she is excluded |
| 12 | `SELECT dname FROM dept WHERE dno NOT IN (SELECT dno FROM emp WHERE dno IS NOT NULL);` | ME |

**NULL traps**
- Without `WHERE dno IS NOT NULL`, query 12 returns **no rows**: `x NOT IN (…, NULL)` is never true
- `WHERE sal = NULL` matches nothing – use `IS NULL` (here: Kiran)
- `COUNT(*)` counts rows; `COUNT(col)` skips NULLs; `AVG` divides by the non-NULL count

**Writing queries**
- Employees earning the maximum in their department: `SELECT name FROM emp e WHERE sal = (SELECT MAX(sal) FROM emp WHERE dno = e.dno);` → Ravi, Meena, John (Kiran's NULL salary never equals; for Leela `dno = NULL` finds no rows, so the MAX is NULL)
- Departments with no employees: `SELECT dname FROM dept d WHERE NOT EXISTS (SELECT * FROM emp e WHERE e.dno = d.dno);` → ME
- Raise CS salaries by 10%: `UPDATE emp SET sal = sal * 1.1 WHERE dno = (SELECT dno FROM dept WHERE dname = 'CS');`"""}],

    "Normalization": [{"title": S + "keys and normal forms", "md": """**Method**: (1) find attributes on no right side – they are in every key; (2) compute closures to find **candidate keys**; (3) prime attributes = those in some key; (4) test BCNF (every determinant a super key) → 3NF (or RHS prime) → 2NF (no partial dependency of a non-prime attribute on part of a key).

| # | R and F | Candidate keys | Highest NF | Why |
|---|---|---|---|---|
| 1 | R(A, B, C, D, E): A → BC, CD → E, B → D, E → A | **A, E, BC, CD** | **3NF** | B → D: B not a super key, but D is prime |
| 2 | R(A, B, C, D): AB → C, C → D, D → A | **AB, BC, BD** | **3NF** | all attributes prime; C → D violates BCNF |
| 3 | R(A, B, C, D, E): AB → C, B → D, D → E | **AB** | **1NF** | B → D is a partial dependency |
| 4 | R(A, B, C, D): A → B, B → C, C → D | **A** | **2NF** | single-attribute key (no partial dependency) but B → C is transitive |
| 5 | R(A, B, C): A → B, B → A | **AC, BC** | **3NF** | A → B: A not a super key, B prime |
| 6 | R(A … F): AB → C, C → D, D → E, E → F | **AB** | **2NF** | transitive chain C → D → E → F |
| 7 | R(A, B, C, D): AB → CD, C → A | **AB, BC** | **3NF** | C → A: A is prime |

**Closure practice** (example 1): B⁺ = {B, D}; CD⁺ = {A, B, C, D, E} → CD is a key; A⁺ = {A, B, C, D, E}

**Decomposition checks**
- R(A, B, C), F = {A → B}: decomposition R1(A, B), R2(A, C) – common attribute A, and A → AB → **lossless**
- R(A, B, C), F = {A → B, B → C}: R1(A, B), R2(A, C) is lossless (A is a key of R1) but **not dependency-preserving** (B → C lost)
- Example 4 to 3NF: R1(A, B), R2(B, C), R3(C, D) – lossless and dependency-preserving

**Quick rules**
- If every candidate key is a single attribute → automatically 2NF
- If all attributes are prime → automatically 3NF
- Any relation with two attributes is in BCNF"""}],

    "Transactions & Concurrency Control": [{"title": S + "serializability and recoverability", "md": """**Conflict test**: draw an edge Tᵢ → Tⱼ when an operation of Tᵢ comes before a **conflicting** operation of Tⱼ (same item, at least one write). No cycle ⇔ conflict serializable; a topological order gives the equivalent serial schedule.

### Q1. S1: r1(A) w1(A) r2(A) w2(A) r1(B) w1(B) r2(B) w2(B)
Edges: T1 → T2 only → **conflict serializable**, equivalent to ⟨T1, T2⟩

### Q2. S2: r1(A) r2(A) w1(A) w2(A)
r1(A) before w2(A) → T1 → T2; r2(A) before w1(A) → T2 → T1 → **cycle → not conflict serializable** (lost update)

### Q3. S3: r1(A) w2(A) w1(A) w3(A)
Edges T1 → T2, T2 → T1 (and → T3) → cycle → not conflict serializable; but it is **view serializable** (equivalent to ⟨T1, T2, T3⟩: T1 reads the initial A, T3 does the final write; w2 and w1 are **blind writes**) – every view-serializable but not conflict-serializable schedule contains blind writes

### Q4. Recoverability
- r1(A) w1(A) r2(A) w2(A) **c2** c1 → T2 read T1's uncommitted write and committed first → **not recoverable**
- Same with c1 before c2 → recoverable but **cascading** rollback possible (T2 read dirty data)
- If T2 reads A only after c1 → **cascadeless**; if nobody reads or writes an item until the writer commits → **strict**
- Hierarchy: strict ⊂ cascadeless ⊂ recoverable

### Q5. Two-phase locking
T1: lock-X(A), read A, A = A − 50, write A, lock-X(B), unlock(A), read B, B = B + 50, write B, unlock(B) → all locks acquired before the first unlock → **follows 2PL**. Moving unlock(A) before lock-X(B) breaks 2PL.

### Q6. Timestamp ordering
TS(T1) = 5, TS(T2) = 10; item X has read_TS = 10, write_TS = 0. T1 issues write(X): TS(T1) = 5 < read_TS 10 → **T1 rolls back**. If instead write_TS(X) = 10 and read_TS(X) = 0, Thomas' write rule **ignores** T1's obsolete write.

### Q7. Deadlock prevention
T1 (older, TS 5) requests an item held by T2 (TS 10):
- **Wait-die**: older waits → T1 waits; if T2 requested T1's item, T2 (younger) dies
- **Wound-wait**: older wounds younger → T2 is rolled back; a younger requester waits

### Q8. Number of schedules
Two transactions with 2 and 3 operations: interleavings = (2 + 3)!/(2! 3!) = **10**; serial schedules = 2! = 2"""}],

    "Relational Algebra and Relational Calculus": [{"title": S + "relational algebra", "md": """**Relations**: STUDENT(sid, name, dept), COURSE(cid, title), ENROLL(sid, cid, grade)

| Question | Algebra |
|---|---|
| Names of CS students | π name (σ dept = 'CS' (STUDENT)) |
| Students with their course titles | π name, title (STUDENT ⋈ ENROLL ⋈ COURSE) |
| sid of students enrolled in C1 **or** C2 | π sid (σ cid = 'C1' ∨ cid = 'C2' (ENROLL)) |
| sid of students enrolled in **both** C1 and C2 | π sid (σ cid = 'C1' (ENROLL)) ∩ π sid (σ cid = 'C2' (ENROLL)) |
| Students enrolled in **no** course | π sid (STUDENT) − π sid (ENROLL) |
| Students enrolled in **all** courses | π sid, cid (ENROLL) ÷ π cid (COURSE) |
| Highest grade (no aggregation) | π grade (ENROLL) − π E1.grade (σ E1.grade < E2.grade (ρ E1 (ENROLL) × ρ E2 (ENROLL))) |

**Size questions** (R: 5 attributes, 100 tuples; S: 3 attributes, 20 tuples)
- R × S → 8 attributes, **2000** tuples
- R ⋈ S on a common attribute that is the key of S and a foreign key of R (no NULLs) → exactly **100** tuples
- σ (R) → 0 … 100 tuples; π (R) → 1 … 100 (duplicates removed)
- R ∪ S, R ∩ S, R − S need union-compatible relations (same degree and domains)

**Division by hand**: A(x, y) = {(1, a), (1, b), (2, a), (3, a), (3, b)}, B(y) = {a, b} → A ÷ B = **{1, 3}**

**Tuple calculus**: { t.name | t ∈ STUDENT ∧ ∃e (e ∈ ENROLL ∧ e.sid = t.sid ∧ e.cid = 'C1') }

**SQL equivalents**: σ → WHERE, π → SELECT (DISTINCT), ⋈ → JOIN, ∪ → UNION, − → EXCEPT/NOT IN, ÷ → double NOT EXISTS"""}],

    "ER Model & Relational Model": [{"title": S + "ER to tables", "md": """### Q1. Minimum number of tables
- Entities A and B with a **1 : N** relationship (no attributes on the relationship) → **2** tables (foreign key on the N side)
- **M : N** → **3** tables (A, B and a relationship table with both keys)
- **1 : 1** with total participation on one side → **1** table can be enough (merge); otherwise 2
- Weak entity W owned by E (identifying 1 : N) → 2 tables; W's key = E's key + partial key
- Multivalued attribute → its own table

### Q2. Map this ER diagram
STUDENT(roll, name, {phone}) – ENROLS (M : N, attribute grade) – COURSE(cid, title); COURSE – TAUGHT_BY (N : 1) – FACULTY(fid, fname)
Tables: STUDENT(**roll**, name) · STUDENT_PHONE(**roll, phone**) · COURSE(**cid**, title, fid → FACULTY) · FACULTY(**fid**, fname) · ENROLS(**roll, cid**, grade) → **5 tables**

### Q3. Keys
R(A, B, C, D) where {A, B} is the only candidate key → super keys = all supersets of AB = AB, ABC, ABD, ABCD → **4**
n attributes with a single-attribute key → 2ⁿ⁻¹ super keys (4 attributes → 8)

### Q4. Referential integrity actions
DEPT(10, 20); EMP rows refer to dno 10 and 20. Deleting DEPT 20:
- ON DELETE RESTRICT/NO ACTION → rejected
- ON DELETE CASCADE → EMP rows with dno 20 deleted too
- ON DELETE SET NULL → their dno becomes NULL"""}],
}
