"""P2 · Unit 2 – Discrete Structures & Optimization · detailed revision NOTES for all nine topics (no new questions).
Owner's request (19 Oct 2026): "continue CS notes, detailed". The Unit 2 pack is built by pack_p2_u2.py (with answer
balancing), so add_u2_notes() puts these notes straight into packs/p2-u2-complete.json without touching the questions.
Counting, probability and Boolean examples were checked with a script on 19 Oct 2026. Facts follow Rosen (Discrete
Mathematics and Its Applications)."""
import json
from pathlib import Path

NOTES = {
    "Propositional Logic": [{"title": "Propositional logic – detailed notes", "md": """## Propositions and connectives
- **Proposition** = declarative sentence that is either true or false ("5 > 3"); questions, commands and "x + 1 = 2" are not
| Connective | Symbol | False only when … / rule |
|---|---|---|
| Negation | ¬p | flips |
| Conjunction (AND) | p ∧ q | true only if both true |
| Disjunction (OR) | p ∨ q | false only if both false |
| Exclusive OR | p ⊕ q | true if exactly one true |
| **Implication** | p → q | **false only when p is T and q is F** |
| Biconditional | p ↔ q | true when both have the same value |
- p → q reads "if p then q", "p only if q", "q is necessary for p", "p is sufficient for q", "q unless ¬p"
- **Converse** q → p, **inverse** ¬p → ¬q, **contrapositive** ¬q → ¬p (contrapositive ≡ original; converse ≡ inverse)
- Precedence: ¬, ∧, ∨, →, ↔
- n variables → truth table of 2ⁿ rows; number of distinct Boolean functions of n variables = 2^(2ⁿ) (n = 2 → 16)

## Tautology, contradiction, contingency
- **Tautology** – always true (p ∨ ¬p, (p ∧ q) → p); **contradiction** – always false (p ∧ ¬p); **contingency** – neither
- **Satisfiable** = true for at least one assignment

## Logical equivalences (p ≡ q when p ↔ q is a tautology)
| Law | Form |
|---|---|
| Identity | p ∧ T ≡ p, p ∨ F ≡ p |
| Domination | p ∨ T ≡ T, p ∧ F ≡ F |
| Idempotent | p ∨ p ≡ p |
| Double negation | ¬¬p ≡ p |
| Commutative, associative, distributive | p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) |
| **De Morgan** | ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q |
| Absorption | p ∨ (p ∧ q) ≡ p; p ∧ (p ∨ q) ≡ p |
| Negation | p ∨ ¬p ≡ T; p ∧ ¬p ≡ F |
| **Implication** | **p → q ≡ ¬p ∨ q** |
| Biconditional | p ↔ q ≡ (p → q) ∧ (q → p) |
| Exportation | (p ∧ q) → r ≡ p → (q → r) |
- ¬(p → q) ≡ p ∧ ¬q

## Normal forms
- **DNF** (disjunctive) = OR of AND-terms; **CNF** (conjunctive) = AND of OR-clauses
- **Principal (canonical)** DNF = sum of **minterms** (rows where the formula is true); PCNF = product of **maxterms** (rows where false)
- Example p → q = ¬p ∨ q (already CNF and DNF); PDNF = (¬p ∧ ¬q) ∨ (¬p ∧ q) ∨ (p ∧ q)
- Functionally complete sets: {¬, ∧}, {¬, ∨}, **{NAND}**, **{NOR}**

## Traps
- An implication with a false hypothesis is **true** ("If 2 + 2 = 5 then I am the PM" is true)
- The contrapositive, not the converse, is equivalent
- XOR is the negation of the biconditional"""}],

    "Predicate Logic & Rules of Inference": [{"title": "Predicates, quantifiers and inference – detailed notes", "md": """## Predicates and quantifiers
- **Predicate** P(x) becomes a proposition when x gets a value or is quantified; domain (universe of discourse) matters
- **Universal** ∀x P(x) – true if P is true for **every** x (one counterexample makes it false)
- **Existential** ∃x P(x) – true if **at least one** x works
- ∃! "there exists exactly one"
- **Negation (De Morgan for quantifiers)**: ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x)
- Translation patterns: "All students study" → ∀x (S(x) → T(x)) (use **→** with ∀); "Some students study" → ∃x (S(x) ∧ T(x)) (use **∧** with ∃)
- ∀ distributes over ∧, ∃ over ∨ (not the other way round)
- Bound vs free variables; scope of a quantifier

## Nested quantifiers
- Order matters when quantifiers differ: ∀x ∃y (x + y = 0) is **true** over integers (y = −x), but ∃y ∀x (x + y = 0) is **false**
- Same quantifiers commute: ∀x ∀y ≡ ∀y ∀x
- ∃y ∀x P(x, y) → ∀x ∃y P(x, y) is valid; the converse is not
- Negate step by step: ¬∀x ∃y P(x, y) ≡ ∃x ∀y ¬P(x, y)
- "Every student has a friend" → ∀x ∃y F(x, y); "Someone is everyone's friend" → ∃y ∀x F(x, y)

## Rules of inference (propositional)
| Rule | Form |
|---|---|
| **Modus ponens** | p, p → q ∴ q |
| **Modus tollens** | ¬q, p → q ∴ ¬p |
| **Hypothetical syllogism** | p → q, q → r ∴ p → r |
| **Disjunctive syllogism** | p ∨ q, ¬p ∴ q |
| Addition | p ∴ p ∨ q |
| Simplification | p ∧ q ∴ p |
| Conjunction | p, q ∴ p ∧ q |
| **Resolution** | p ∨ q, ¬p ∨ r ∴ q ∨ r |
- Fallacies: **affirming the consequent** (q, p → q ∴ p) and **denying the antecedent** (¬p, p → q ∴ ¬q)

## Rules for quantifiers
Universal instantiation (∀x P(x) ∴ P(c)), universal generalisation (P(c) for arbitrary c ∴ ∀x P(x)), existential instantiation (∃x P(x) ∴ P(c) for some c), existential generalisation (P(c) ∴ ∃x P(x)); universal modus ponens: ∀x (P(x) → Q(x)), P(a) ∴ Q(a) ("All men are mortal; Socrates is a man ∴ Socrates is mortal")

## Proof methods
Direct proof, **contrapositive**, **contradiction** (assume ¬p, derive F – e.g. √2 is irrational, infinitely many primes), cases, existence (constructive / non-constructive), counterexample (to disprove ∀), induction

## Traps
- Use → with ∀ and ∧ with ∃ when translating
- ∀x ∃y and ∃y ∀x are different statements
- Affirming the consequent is a fallacy"""}],

    "Sets and Relations": [{"title": "Sets and relations – detailed notes", "md": """## Sets
- Roster {1, 2, 3} or set-builder {x | x > 0}; ∅ empty; U universal; |A| cardinality
- **Power set** P(A): all subsets → |P(A)| = **2ⁿ**; P(∅) = {∅}
- A ⊆ B (subset), A ⊂ B (proper); A = B iff A ⊆ B and B ⊆ A
- Operations: A ∪ B, A ∩ B, A − B, complement A′, **symmetric difference** A ⊕ B = (A − B) ∪ (B − A); **Cartesian product** |A × B| = |A|·|B|
- Identities: De Morgan (A ∪ B)′ = A′ ∩ B′; distributive; absorption
- |A ∪ B| = |A| + |B| − |A ∩ B|
- Countable (ℕ, ℤ, ℚ) vs uncountable (ℝ – Cantor's diagonal argument)

## Relations
- A relation R from A to B is a subset of A × B; on a set A with n elements there are **2^(n²)** relations (n = 3 → 512)
- Representations: ordered pairs, **0–1 matrix**, **digraph**
| Property | Meaning | Matrix / digraph | Count on n elements |
|---|---|---|---|
| **Reflexive** | (a, a) ∈ R for all a | all 1s on the diagonal / loop at every vertex | 2^(n² − n) (n = 3 → 64) |
| Irreflexive | no (a, a) | diagonal all 0 | 2^(n² − n) |
| **Symmetric** | (a, b) → (b, a) | matrix symmetric | 2^(n(n + 1)/2) (n = 3 → 64) |
| **Antisymmetric** | (a, b) and (b, a) → a = b | no 1s in mirror positions off the diagonal | 2ⁿ · 3^(n(n − 1)/2) (n = 3 → 216) |
| Asymmetric | (a, b) → not (b, a) | antisymmetric + irreflexive | 3^(n(n − 1)/2) |
| **Transitive** | (a, b), (b, c) → (a, c) | | no simple formula |
- Composition R∘S; inverse R⁻¹; closures: reflexive (add the diagonal), symmetric (add R⁻¹), **transitive** (Warshall's algorithm)
- Example on {1, 2, 3}: R = {(1, 1), (2, 2), (3, 3), (1, 2)} is reflexive, antisymmetric, transitive → a partial order

## Equivalence relations
- **Reflexive + symmetric + transitive** (e.g. congruence mod n, "same age", equality)
- **Equivalence class** [a] = {x | x R a}; the classes **partition** the set (disjoint, cover everything) – and every partition gives an equivalence relation
- Congruence mod 3 on ℤ has 3 classes: [0], [1], [2]
- Number of equivalence relations on an n-set = **Bell number** (1, 2, 5, 15, 52 …; n = 4 → 15)

## Partial orders
- **Reflexive + antisymmetric + transitive** – poset (A, ≤); examples ⊆ on sets, | (divides) on positive integers, ≤ on ℝ
- **Total (linear) order**: every two elements are comparable; **Hasse diagram** drops loops, transitive edges and arrow heads
- Maximal/minimal, greatest/least elements; upper/lower bounds; **lub (join)**, **glb (meet)**
- **Lattice**: every pair has a lub and a glb (e.g. divisors of 30 under divisibility; P(A) under ⊆)
- Topological sorting gives a total order compatible with a partial order
- Divisors of 12 under |: Hasse diagram 1 → 2, 3 → 4, 6 → 12; minimal 1, maximal 12

## Functions (quick)
- Injective (one-to-one), surjective (onto), bijective; |A| = m, |B| = n → nᵐ functions (3 → 4: 64), onto functions 4 → 3 = **36**, injective functions m ≤ n: n!/(n − m)!

## Traps
- A relation can be both symmetric and antisymmetric (e.g. equality)
- The empty relation on a non-empty set is symmetric and transitive but **not** reflexive
- Partial order = reflexive, antisymmetric, transitive (not symmetric)"""}],

    "Counting": [{"title": "Counting – detailed notes", "md": """## Basic rules
- **Product rule**: tasks done in sequence → multiply (4-digit PINs: 10⁴ = 10,000; car plates 3 letters + 3 digits: 26³ × 10³)
- **Sum rule**: either/or (disjoint) → add
- **Subtraction (inclusion–exclusion for two sets)**: |A ∪ B| = |A| + |B| − |A ∩ B|
- **Division rule**: n ways counted d times each → n/d (circular arrangements of n people = (n − 1)!)
- Bit strings of length n: 2ⁿ; subsets of an n-set: 2ⁿ

## Pigeonhole principle
- n + 1 objects into n boxes → some box has ≥ 2
- **Generalised**: N objects into k boxes → some box has ≥ ⌈N/k⌉
- 13 people → two share a birth month; 367 people → two share a birthday (with 29 Feb)
- Minimum people to guarantee 3 with the same blood group (4 groups): 2 × 4 + 1 = 9
- Among any n + 1 integers from 1 … 2n, one divides another

## Permutations and combinations
| Situation | Formula | Example |
|---|---|---|
| Arrange r of n distinct (order matters) | P(n, r) = n!/(n − r)! | P(10, 3) = 720 |
| Choose r of n (order doesn't) | C(n, r) = n!/(r!(n − r)!) | C(10, 3) = 120 |
| Arrange with repeats n₁, n₂ … | n!/(n₁! n₂! …) | MISSISSIPPI = 11!/(4! 4! 2!) = **34,650** |
| r-permutations with repetition | nʳ | |
| r-combinations with repetition | C(n + r − 1, r) | x₁ + x₂ + x₃ = 10, xᵢ ≥ 0 → C(12, 2) = **66** |
| Circular arrangements | (n − 1)! | 5 people → 24 |
- C(n, r) = C(n, n − r); **Pascal's identity** C(n, r) = C(n − 1, r − 1) + C(n − 1, r); Σ C(n, r) = 2ⁿ
- **Binomial theorem**: (x + y)ⁿ = Σ C(n, k) xⁿ⁻ᵏ yᵏ; coefficient of x³y² in (x + y)⁵ = C(5, 2) = 10

## Inclusion–exclusion
- |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|
- Integers 1 … 100 divisible by 2, 3 or 5: 50 + 33 + 20 − 16 − 10 − 6 + 3 = **74**
- **Derangements** (nobody in their own place): Dₙ = n! Σ (−1)ᵏ/k! → D₃ = 2, **D₄ = 9**, D₅ = 44; Dₙ ≈ n!/e
- Onto functions from m to n elements: Σ (−1)ᵏ C(n, k)(n − k)ᵐ → 4 → 3: 81 − 48 + 3 = **36**

## Recurrences and generating functions (overview)
- Fibonacci, Tower of Hanoi Hₙ = 2Hₙ₋₁ + 1, bit strings without two consecutive 0s: aₙ = aₙ₋₁ + aₙ₋₂
- Catalan numbers C(2n, n)/(n + 1): 1, 1, 2, 5, 14, 42 (bracketings, binary trees, stack permutations)
- Stirling numbers of the 2nd kind (partitions into k non-empty subsets), Bell numbers

## Traps
- Order matters → permutation; doesn't → combination
- "At least one" problems: total − none
- Committee of 3 from 6 men and 4 women with at least 1 woman: C(10, 3) − C(6, 3) = 120 − 20 = 100"""}],

    "Mathematical Induction & Discrete Probability": [{"title": "Induction and discrete probability – detailed notes", "md": """## Mathematical induction
1. **Basis step**: prove P(1) (or P(n₀))
2. **Inductive step**: assume P(k) (**inductive hypothesis**) and prove P(k + 1)
→ P(n) holds for all n ≥ n₀ (like dominoes)
- Example: 1 + 2 + … + n = n(n + 1)/2. Basis 1 = 1. Step: k(k + 1)/2 + (k + 1) = (k + 1)(k + 2)/2 ✓
- Other classics: Σ 2ⁱ (i = 0..n) = 2ⁿ⁺¹ − 1; 2ⁿ > n²  for n ≥ 5; n³ − n divisible by 3; Σ i² = n(n + 1)(2n + 1)/6
- **Strong induction**: assume P(1) … P(k) to prove P(k + 1) (e.g. every n ≥ 2 is a product of primes; postage with 4p and 5p stamps for n ≥ 12)
- **Well-ordering principle**: every non-empty set of positive integers has a least element (equivalent to induction)
- **Structural induction** for recursively defined sets/trees

## Discrete probability
- Sample space S of equally likely outcomes; P(E) = |E|/|S|; 0 ≤ P(E) ≤ 1; P(E′) = 1 − P(E)
- P(A ∪ B) = P(A) + P(B) − P(A ∩ B); mutually exclusive → P(A ∩ B) = 0
- **Conditional**: P(A | B) = P(A ∩ B)/P(B); **independent** ⇔ P(A ∩ B) = P(A)P(B)
- Two dice: P(sum = 7) = 6/36 = **1/6**; P(at least one six) = 1 − (5/6)² = 11/36
- Coin tossed 3 times: P(exactly 2 heads) = C(3, 2)/8 = 3/8
- **Bernoulli trials / binomial**: P(k successes in n) = C(n, k) pᵏ (1 − p)ⁿ⁻ᵏ
- **Expected value** E(X) = Σ x P(x); fair die E = 3.5; linearity E(X + Y) = E(X) + E(Y); binomial E = np, variance np(1 − p)
- **Birthday problem**: with 23 people P(shared birthday) ≈ **0.507**
- Random variables, geometric distribution (E = 1/p), variance V(X) = E(X²) − E(X)²

## Bayes' theorem
**P(A | B) = P(B | A) P(A) / [P(B | A) P(A) + P(B | A′) P(A′)]**
- Worked: a disease affects 1%; the test detects it 99% of the time; false-positive rate 5%. P(disease | positive) = 0.01 × 0.99 / (0.01 × 0.99 + 0.99 × 0.05) = **0.1667** (only about 17%)
- Prior P(A), likelihood P(B | A), posterior P(A | B); basis of **naive Bayes** spam filters
- Total probability: P(B) = Σ P(B | Aᵢ) P(Aᵢ) over a partition

## Traps
- Independent ≠ mutually exclusive (exclusive events with non-zero probability are dependent)
- In induction you must use the hypothesis P(k) in proving P(k + 1)
- Base-rate fallacy: a positive test for a rare disease is usually a false positive"""}],

    "Graph Theory – Basics & Paths": [{"title": "Graph theory basics and paths – detailed notes", "md": """## Kinds of graphs
| Graph | Feature |
|---|---|
| Simple | no loops, no parallel edges |
| Multigraph | parallel edges allowed |
| Pseudograph | loops and parallel edges |
| Directed (digraph) | edges are ordered pairs |
| Weighted | numbers on edges |
| Complete Kₙ | every pair joined – n(n − 1)/2 edges (K₅: 10) |
| Cycle Cₙ, wheel Wₙ, n-cube Qₙ (2ⁿ vertices, n·2ⁿ⁻¹ edges) | |
| Complete bipartite K_{m,n} | m·n edges (K₃,₃: 9) |
| Regular | all vertices same degree (k-regular → kn/2 edges) |

## Degree facts
- **Handshaking theorem**: Σ deg(v) = **2|E|** → number of odd-degree vertices is even
- Digraph: Σ in-degrees = Σ out-degrees = |E|
- A loop adds 2 to the degree; isolated vertex has degree 0, pendant vertex degree 1
- Degree sequence must have an even sum (3, 3, 2, 1 is impossible)
- Isomorphic graphs: same vertices, edges, degree sequence (necessary, not sufficient)
- Subgraph, induced subgraph, complement (Ḡ of Kₙ is empty), union

## Paths and connectivity
- Walk (any), trail (no repeated edge), path (no repeated vertex), circuit/cycle
- Connected graph; components; cut vertex (articulation point), cut edge (bridge); vertex/edge connectivity κ ≤ λ ≤ δ (min degree)
- Strongly vs weakly connected digraphs
- Number of walks of length r from i to j = (Aʳ)ᵢⱼ
- A connected graph with n vertices needs ≥ n − 1 edges; a simple graph with n vertices and more than (n − 1)(n − 2)/2 edges is connected

## Shortest paths
- **Dijkstra** (non-negative weights): repeatedly fix the closest unvisited vertex and relax its edges; O(V²) or O((V + E) log V)
- Example edges A–B 4, A–C 2, B–C 1, B–D 5, C–D 8, C–E 10, D–E 2, D–F 6, E–F 3 → from A: C 2, B 3, D 8, E 10, F 13
- Floyd–Warshall for all pairs; Bellman–Ford for negative weights

## Euler and Hamilton
| | Euler | Hamilton |
|---|---|---|
| Visits | every **edge** once | every **vertex** once |
| Circuit exists iff | connected and **all degrees even** | no simple test (NP-complete) |
| Path exists iff | connected and **exactly 0 or 2 odd-degree vertices** (start/end at the odd ones) | – |
- Königsberg bridges (Euler, 1736): 4 land masses all with odd degree → no Euler path – birth of graph theory
- Digraph Euler circuit: in-degree = out-degree at every vertex
- Hamilton sufficient conditions: **Dirac** (every degree ≥ n/2), **Ore** (deg u + deg v ≥ n for non-adjacent u, v); Kₙ (n ≥ 3) is Hamiltonian
- Kₙ has an Euler circuit iff n is odd
- Travelling salesman = cheapest Hamilton circuit

## Traps
- Euler = edges, Hamilton = vertices
- An Euler path (not circuit) needs exactly two odd vertices
- Handshaking: edges = half the degree sum"""}],

    "Graph Theory – Planar, Colouring, Bipartite": [{"title": "Planar graphs, colouring and bipartite graphs – detailed notes", "md": """## Planar graphs
- Can be drawn in the plane with no edges crossing; the drawing splits the plane into **regions (faces)**, including the unbounded one
- **Euler's formula** (connected planar): **v − e + f = 2** (e.g. cube: 8 − 12 + 6 = 2); with k components: v − e + f = k + 1
- Simple connected planar graph with v ≥ 3: **e ≤ 3v − 6**; if no triangles (e.g. bipartite): **e ≤ 2v − 4**
  - K₅: 10 > 3·5 − 6 = 9 → **not planar**; K₃,₃: 9 > 2·6 − 4 = 8 → **not planar**
- Every simple planar graph has a vertex of degree ≤ 5
- **Kuratowski's theorem**: a graph is planar iff it has no subgraph homeomorphic to **K₅ or K₃,₃** (Wagner: no K₅/K₃,₃ minor)
- K₄ and all trees and cycles are planar; Q₃ is planar
- Dual graph: a vertex per face, an edge per shared boundary

## Graph colouring
- Proper vertex colouring: adjacent vertices get different colours; **chromatic number χ(G)** = fewest colours
| Graph | χ |
|---|---|
| Kₙ | n |
| Cycle Cₙ | 2 if n even, 3 if n odd |
| Bipartite (with an edge) | 2 |
| Tree (n ≥ 2) | 2 |
| Wheel Wₙ | 3 if n even, 4 if n odd |
| Planar | ≤ **4** (Four Colour Theorem, Appel & Haken 1976 – computer-assisted) |
- χ(G) ≥ clique size ω(G); χ(G) ≤ Δ + 1 (greedy); Brooks: ≤ Δ unless complete or odd cycle
- Deciding χ ≤ k is NP-complete for k ≥ 3 (2-colouring is easy – bipartite test)
- **Edge colouring**: chromatic index χ′ is Δ or Δ + 1 (Vizing)
- **Chromatic polynomial** P(G, k): Kₙ → k(k − 1)…(k − n + 1); tree with n vertices → k(k − 1)ⁿ⁻¹
- Applications: exam timetabling (subjects = vertices, common students = edges), register allocation, frequency assignment, map colouring

## Bipartite graphs
- Vertices split into two sets V₁, V₂ with every edge going between them
- **Bipartite ⇔ 2-colourable ⇔ no odd cycle**; test with BFS colouring in O(V + E)
- K_{m,n}: m·n edges; a tree is bipartite; Cₙ is bipartite iff n is even; Qₙ is bipartite
- **Matching**: set of edges without common vertices; maximum matching; perfect matching (covers all vertices)
- **Hall's marriage theorem**: a bipartite graph has a matching saturating V₁ iff |N(S)| ≥ |S| for every S ⊆ V₁
- König's theorem: in bipartite graphs max matching = min vertex cover
- Applications: job assignment, stable marriage (Gale–Shapley), scheduling

## Traps
- K₅ and K₃,₃ are the two minimal non-planar graphs
- Four colours suffice for planar graphs; some need four (K₄)
- An odd cycle makes a graph non-bipartite"""}],

    "Trees, Prefix Codes, Spanning Trees": [{"title": "Trees, prefix codes and spanning trees – detailed notes", "md": """## Trees
- **Tree** = connected graph with **no cycles**; equivalently: exactly one simple path between any two vertices; connected with n − 1 edges; acyclic with n − 1 edges
- A tree with n vertices has **n − 1 edges**; every tree with n ≥ 2 has at least 2 leaves
- Forest = acyclic graph (k trees → n − k edges)
- **Rooted tree**: parent, child, siblings, ancestors, descendants, leaf, internal vertex, subtree, level, **height**
- **m-ary tree**: each internal vertex has ≤ m children; **full** m-ary: exactly m
  - Full m-ary with i internal vertices: n = mi + 1 vertices, leaves l = (m − 1)i + 1
  - Full binary tree with 10 internal nodes → 21 nodes, 11 leaves
  - An m-ary tree of height h has at most mʰ leaves → h ≥ ⌈log_m l⌉
- **Cayley's formula**: number of labelled trees on n vertices = **nⁿ⁻²** (n = 4 → 16)
- Applications: decision trees (sorting needs ≥ ⌈log₂ n!⌉ comparisons), game trees, file systems, BSTs

## Prefix codes and Huffman coding
- **Prefix code**: no codeword is a prefix of another → decoding is unambiguous; represented by a binary tree with symbols at leaves (left 0, right 1)
- Example: {e: 0, a: 10, t: 110, s: 111} is prefix-free; {a: 0, b: 01} is not
- **Huffman algorithm**: repeatedly merge the two lowest-frequency trees → optimal prefix code
  - a 5, b 9, c 12, d 13, e 16, f 45 → f 0, c 100, d 101, a 1100, b 1101, e 111 → 224 bits vs 300 fixed-length
- Average code length = Σ (frequency × code length)/Σ frequency

## Tree traversals
- **Preorder** (root, left, right), **inorder** (left, root, right – binary trees), **postorder** (left, right, root), level order
- Expression tree of (a + b) * (c − d): preorder * + a b − c d (prefix / **Polish** notation); postorder a b + c d − * (postfix / reverse Polish); inorder gives infix (needs brackets)
- Evaluate prefix right to left, postfix left to right with a stack

## Spanning trees
- A spanning tree of a connected graph G includes all vertices and is a tree; found by DFS or BFS
- Every connected graph has one; Kₙ has nⁿ⁻² spanning trees; a cycle Cₙ has n
- **Minimum spanning tree**: **Prim** (grow from a vertex) and **Kruskal** (add the cheapest edge that makes no cycle); on edges A–B 4, A–C 2, B–C 1, B–D 5, C–D 8, C–E 10, D–E 2, D–F 6, E–F 3 both give weight **13**
- **Fundamental circuits**: adding a non-tree edge (a **chord**) creates exactly one cycle → e − n + 1 fundamental circuits (cyclomatic number)

## Cut-sets
- A **cut-set** is a minimal set of edges whose removal disconnects the graph (increases the number of components)
- Every cut-set shares at least one edge with every spanning tree; each tree edge (**branch**) defines a **fundamental cut-set** → n − 1 fundamental cut-sets
- Edge connectivity λ = size of the smallest cut-set; a bridge is a cut-set of size 1

## Traps
- Trees: n vertices, n − 1 edges, no cycles – any two of (connected, acyclic, n − 1 edges) imply the third
- Prefix code ≠ "shortest" code; Huffman gives the optimal prefix code
- Fundamental circuits = e − n + 1; fundamental cut-sets = n − 1"""}],

    "Boolean Algebra": [{"title": "Boolean algebra – detailed notes", "md": """## Boolean algebra
- Set {0, 1} with + (OR), · (AND), ′ (NOT) – George **Boole** (1854); Claude **Shannon** applied it to switching circuits (1938)
- **Huntington postulates**: closure, identity (x + 0 = x, x·1 = x), commutative, distributive (both ways: x + yz = (x + y)(x + z)), complement (x + x′ = 1, x·x′ = 0)
- **Duality**: swap + ↔ · and 0 ↔ 1 → the dual of a valid identity is valid

## Laws
| Law | OR form | AND form |
|---|---|---|
| Identity | x + 0 = x | x · 1 = x |
| Domination (null) | x + 1 = 1 | x · 0 = 0 |
| Idempotent | x + x = x | x · x = x |
| Complement | x + x′ = 1 | x · x′ = 0 |
| Involution | (x′)′ = x | |
| **Absorption** | x + xy = x | x(x + y) = x |
| **De Morgan** | (x + y)′ = x′y′ | (xy)′ = x′ + y′ |
| Redundancy | x + x′y = x + y | x(x′ + y) = xy |
| **Consensus** | xy + x′z + yz = xy + x′z | |

## Boolean functions and representation
- n variables → 2ⁿ rows, **2^(2ⁿ)** functions
- **Minterm** (product with every variable, value 1 for one row) → **sum of products (SOP)**, canonical form Σm(…)
- **Maxterm** (sum with every variable, value 0 for one row) → **product of sums (POS)**, Πᴹ(…)
- Example F(A, B, C) = Σm(1, 3, 5, 7) → F = **C**
- Functionally complete: {AND, OR, NOT}, {NAND} alone, {NOR} alone
- Self-dual functions, symmetric functions; logic gates realise functions (AND, OR, NOT, NAND, NOR, XOR, XNOR)

## Simplification
**Algebraic**: AB + AB′ = A(B + B′) = A; A + A′B = A + B; (A + B)(A + C) = A + BC

**Karnaugh map** (up to 4–5 variables): Gray-code order (00, 01, 11, 10); group 1s in rectangles of size 1, 2, 4, 8 (powers of 2), as large as possible, wrapping around edges; each group eliminates the variables that change
- F(A, B, C) = Σm(0, 2, 4, 5, 6) → **C′ + AB′**
- Prime implicant = largest possible group; essential prime implicant covers a 1 no other group covers
- **Don't-care** conditions (X) may be used as 1 or 0 to make groups bigger (e.g. BCD inputs 10–15)
- For POS, group the 0s
**Quine–McCluskey** (tabular) method for more variables; algorithmic, suitable for computers

## Traps
- x + yz = (x + y)(x + z) holds in Boolean algebra (not in ordinary algebra)
- A K-map group must have 1, 2, 4, 8 … cells, never 3 or 6
- De Morgan: break the bar, change the sign"""}],
}


def add_u2_notes():
    """Put the notes into packs/p2-u2-complete.json without touching the questions (re-run safe)."""
    path = Path(__file__).resolve().parent.parent / "packs" / "p2-u2-complete.json"
    raw = path.read_text(encoding="utf-8")
    pack = json.loads(raw)
    for t in pack["subjects"][0]["topics"]:
        if t["name"] in NOTES:
            mine = {n["title"] for n in NOTES[t["name"]]}
            t["notes"] = [n for n in t.get("notes", []) if n["title"] not in mine] + NOTES[t["name"]]
    path.write_text(json.dumps(pack, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")


if __name__ == "__main__":
    add_u2_notes()
