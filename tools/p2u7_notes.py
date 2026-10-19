"""P2 · Unit 7 – Software Engineering · revision NOTES for all five topics (no new questions).
Owner's request (19 Oct 2026): notes for the remaining KRIES Paper 2 areas (Software Engineering is named in the KRIES syllabus).
COCOMO and function-point figures were computed with a script on 19 Oct 2026. Facts follow Pressman (Software Engineering:
A Practitioner's Approach) and Sommerville."""

TOPICS = {}  # notes only – question sets come from p2u7_a, p2u7_b

NOTES = {
    "Software Process Models": [{"title": "Software process models and project management – revision sheet", "md": """## Basics
- Software = programs + documentation + data; it is **developed, not manufactured**, and does not wear out (but deteriorates through changes)
- Software crisis (1960s) → software engineering (term from the **NATO conference, 1968**)
- Layers (Pressman): **quality focus** (bedrock) → process → methods → tools
- **Generic process framework**: communication, planning, modeling, construction, deployment + umbrella activities (project tracking, risk management, QA, configuration management, reviews, measurement)
- **SDLC** phases: feasibility → requirements → design → coding → testing → deployment → maintenance

## Prescriptive models
| Model | Idea | Best when | Weakness |
|---|---|---|---|
| **Waterfall** (classic, linear sequential – Royce 1970) | phases in strict order | requirements fixed and clear | no working software until late; changes costly |
| **V-model** | each development phase paired with a testing phase | safety-critical | rigid |
| **Incremental** | deliver in increments, core product first | early partial delivery | needs good architecture |
| **RAD** | very short cycle (60–90 days), component reuse, teams in parallel | modular, well-understood | needs many skilled people |
| **Prototyping** | throwaway or evolutionary prototype to clarify requirements | **unclear requirements** | customer may mistake prototype for product |
| **Spiral** (Boehm, 1988) | loops of planning, **risk analysis**, engineering, evaluation | large, **high-risk** projects | needs risk expertise; costly |
| Concurrent | activities in states (awaiting changes, under development …) | | |
| **Specialised**: component-based (COTS), formal methods (cleanroom – mathematical proof), aspect-oriented | | | |
| **Unified Process (RUP)** | phases inception, elaboration, construction, transition; use-case driven, architecture-centric, iterative | | |

## Estimation – worked
**Basic COCOMO** (Boehm 1981), E = a(KLOC)ᵇ person-months, D = 2.5 Eᵈ months
| Mode | a | b | d |
|---|---|---|---|
| Organic (small, familiar) | 2.4 | 1.05 | 0.38 |
| Semi-detached | 3.0 | 1.12 | 0.35 |
| Embedded (tight constraints) | 3.6 | 1.20 | 0.32 |
32 KLOC organic → E ≈ **91.3 PM**, D ≈ **13.9 months**, staff ≈ E/D ≈ **6.6 people**. Intermediate COCOMO multiplies by an effort adjustment factor (15 cost drivers); COCOMO II uses object/function points.

**Function points** (Albrecht): count external inputs, outputs, inquiries, internal logical files, external interface files × weights → UFP; **FP = UFP × (0.65 + 0.01 × ΣFᵢ)** (14 factors rated 0–5)
- Example: 20 EI×4 + 30 EO×5 + 15 EQ×4 + 5 ILF×10 + 3 EIF×7 = **361 UFP**; ΣF = 42 → CAF 1.07 → **FP ≈ 386**
- LOC is language-dependent; FP is language-independent

## Project management
- The **4 Ps**: people, product, process, project; W⁵HH principle (Boehm)
- Scheduling: work breakdown structure, **Gantt chart** (bars on a timeline), **PERT / CPM** (network; **critical path** = longest path, zero slack); PERT time = (O + 4M + P)/6
- Risk management: identify → analyse (probability × impact = **risk exposure**) → plan (avoid, monitor, manage – RMMM) → monitor
- Brooks' law: adding people to a late project makes it later

## Traps
- Spiral model = **risk-driven**; prototyping = unclear requirements; waterfall = stable requirements
- COCOMO is an **algorithmic** cost model by Barry Boehm
- Critical-path activities have zero slack"""}],

    "Agile Process Models": [{"title": "Agile process models – revision sheet", "md": """## Agile Manifesto (2001, 17 developers at Snowbird, Utah)
We value:
1. **Individuals and interactions** over processes and tools
2. **Working software** over comprehensive documentation
3. **Customer collaboration** over contract negotiation
4. **Responding to change** over following a plan
Plus **12 principles**: early and continuous delivery, welcome changing requirements, deliver frequently (weeks), business people and developers work together daily, face-to-face conversation, working software is the measure of progress, sustainable pace, technical excellence, simplicity, self-organising teams, regular reflection.

## Extreme Programming (XP – Kent Beck)
- Values: communication, simplicity, feedback, courage, respect
- Activities: planning (**user stories**, story points, velocity), design (**KISS**, CRC cards, spike solutions, **refactoring**), coding (**pair programming**, unit tests written **before** code), testing (continuous integration, acceptance tests)
- Small releases, collective code ownership, 40-hour week, on-site customer

## Scrum
| Element | Meaning |
|---|---|
| **Product owner** | owns and prioritises the product backlog |
| **Scrum master** | facilitator, removes impediments (not a manager) |
| Development team | self-organising, cross-functional (3–9) |
| **Product backlog** | prioritised list of features |
| **Sprint** | time-box of 1–4 weeks (often 2 or 30 days) producing a shippable increment |
| Sprint backlog | items chosen for the sprint |
| **Daily scrum** | 15-minute stand-up: what did I do, what will I do, what blocks me |
| Sprint review / retrospective | demo to stakeholders / improve the process |
- Burn-down chart shows remaining work

## Other agile methods
| Method | Key idea |
|---|---|
| **ASD** (Adaptive Software Development, Highsmith) | speculation → collaboration → learning |
| **DSDM** | **80/20 rule** (Pareto), time-boxing, MoSCoW prioritisation (Must, Should, Could, Won't) |
| **FDD** (Feature-Driven Development, Coad) | features small (≤ 2 weeks), "action result object" naming |
| Crystal (Cockburn) | family of methods by team size and criticality |
| Lean | eliminate waste, deliver fast |
| Kanban | visual board, limit work in progress |
| Agile Unified Process | RUP made lighter |

## Agile vs plan-driven
| Agile | Plan-driven |
|---|---|
| changing requirements welcome | fixed up front |
| short iterations, frequent delivery | one big delivery |
| light documentation | heavy documentation |
| customer involved throughout | customer at start and end |

## Traps
- "Working software over documentation" doesn't mean **no** documentation
- Pair programming and test-first are **XP** practices
- The Scrum master is a servant-leader, not the project manager
- DSDM's 80/20 rule: 80% of the value comes from 20% of the functionality"""}],

    "Software Requirements": [{"title": "Software requirements and SRS – revision sheet", "md": """## Kinds of requirements
| Functional | Non-functional (quality attributes) |
|---|---|
| **what** the system does: services, inputs, outputs, behaviour | **how well**: performance, reliability, usability, security, availability, portability, maintainability |
| "The system shall generate a hall ticket" | "Pages shall load within 2 seconds" |
- Also: user vs system requirements; domain requirements; product, organisational, external (legal) constraints

## Requirements engineering tasks (Pressman)
Inception → **elicitation** → elaboration → negotiation → **specification** → **validation** → requirements management

## Elicitation techniques
Interviews (structured/unstructured), questionnaires, **brainstorming**, observation (ethnography), **JAD / facilitated application specification technique (FAST)**, **QFD** (quality function deployment – normal, expected, exciting requirements), prototyping, scenarios and **use cases**, document study
- Problems: scope, understanding, volatility

## Use cases
- **Actor** (external role – person, device, system) + **use case** (goal-oriented interaction); use case diagram: stick figures, ovals, system boundary
- Relationships: `<<include>>` (always uses – common behaviour), `<<extend>>` (optional/conditional), generalisation
- Text template: name, actors, preconditions, main flow, alternative flows, postconditions

## Analysis modelling
| Approach | Models |
|---|---|
| Structured analysis | **DFD** (process, data flow, data store, external entity; level 0 = **context diagram**, levelled DFDs with balancing), **data dictionary**, ERD, state transition diagram, process specifications (structured English, decision table/tree) |
| Object-oriented analysis | class diagrams, CRC cards, use cases, activity, sequence and state diagrams |
- DFD shows **data flow, not control flow**; flowcharts show control flow

## SRS (Software Requirements Specification)
- Standard **IEEE 830** (now ISO/IEC/IEEE 29148): introduction (purpose, scope, definitions), overall description (product perspective, functions, users, constraints, assumptions), specific requirements
- A good SRS is: **correct, unambiguous, complete, consistent, ranked for importance, verifiable, modifiable, traceable**
- SRS says **what**, not **how** (no design decisions); it is the basis for contract, design, testing and acceptance

## Validation and management
- Reviews/inspections, prototyping, test-case generation, requirements **traceability matrix** (requirement ↔ design ↔ test)
- Feasibility study: technical, economic (cost–benefit), operational, schedule, legal

## Traps
- Context diagram = level-0 DFD with a single process
- Non-functional requirements often decide the architecture
- `<<include>>` is mandatory, `<<extend>>` is optional"""}],

    "Software Design": [{"title": "Software design – revision sheet", "md": """## Design concepts (Pressman)
- **Abstraction** – procedural and data abstraction
- **Architecture** – overall structure of components and their interactions
- **Patterns** – proven solutions to recurring problems (Gang of Four, 23 patterns): creational (**Singleton**, Factory, Builder, Prototype), structural (Adapter, Facade, Decorator, Composite, Proxy), behavioural (**Observer**, Strategy, Command, Iterator, State); MVC
- **Separation of concerns**, **modularity** (divide into modules – too many modules raise integration cost)
- **Information hiding** (Parnas, 1972) – a module hides its internals; access only via its interface
- **Functional independence** – measured by cohesion and coupling
- Refinement (stepwise, top-down – Wirth), refactoring, aspects, OO design concepts

## Cohesion (inside one module) – best to worst
**Functional** > sequential > communicational > procedural > temporal > logical > **coincidental**
- Functional: does one well-defined task; coincidental: unrelated parts thrown together

## Coupling (between modules) – best to worst
**Data** (pass only needed data) > stamp (pass a whole structure) > control (pass a flag that controls logic) > external > **common** (shared global data) > **content** (one module changes another's internals)
**Aim: high cohesion, low coupling**

## Architectural styles
Data-centred (repository/blackboard), **data-flow (pipe and filter)**, call-and-return (main program/subprogram), **layered**, object-oriented, client–server, **MVC**, event-driven, microservices

## Component-level and UI design
- Component design: detailed algorithms (flowcharts, pseudocode, decision tables), interfaces
- **Structure chart** (structured design): modules as boxes, data couples/control flags; transform and transaction analysis convert DFDs to structure charts
- UI golden rules (Mandel): place the **user in control**, **reduce memory load**, make the interface **consistent**; usability heuristics (Nielsen)

## UML diagrams (14 in UML 2.x)
| Structural | Behavioural |
|---|---|
| **Class**, object, component, **deployment**, package, composite structure, profile | **Use case**, **activity**, **sequence**, communication (collaboration), **state machine**, timing, interaction overview |
- Class diagram relationships: association, **aggregation** (hollow diamond – "has-a", parts can live alone), **composition** (filled diamond – parts die with the whole), **generalisation** (hollow triangle – inheritance), dependency (dashed arrow), realisation (dashed triangle – interface)
- Visibility: + public, − private, # protected, ~ package
- Sequence diagram = objects over **time** (lifelines, messages); collaboration diagram = object links; sequence and communication diagrams are **interaction diagrams**
- UML created by the "three amigos": Booch, Rumbaugh, Jacobson (OMG standard)

## Traps
- Content coupling is the **worst**; data coupling the best
- Coincidental cohesion is the worst; functional the best
- Filled diamond = composition, hollow = aggregation
- Design patterns are not code libraries but templates"""}],

    "Software Testing": [{"title": "Software testing and quality – revision sheet", "md": """## Verification vs validation (Boehm)
- **Verification**: "Are we building the product **right**?" – reviews, inspections, walkthroughs (static, no execution)
- **Validation**: "Are we building the **right** product?" – testing against user needs (dynamic)
- Error (human mistake) → **fault/defect/bug** (in code) → **failure** (wrong behaviour seen)
- Testing shows the **presence** of bugs, never their absence (Dijkstra); exhaustive testing is impossible

## Testing strategy (levels)
**Unit** (module – drivers and stubs) → **integration** (top-down with stubs, bottom-up with drivers, sandwich, **big-bang**; regression and smoke testing) → **validation** (against SRS: **alpha** at developer's site, **beta** at customer's site) → **system** (recovery, security, **stress**, performance, deployment) → **acceptance**
- Stub = dummy **called** module (top-down); driver = dummy **calling** module (bottom-up)

## White-box (structural, glass-box) testing
- Uses the code: statement, branch/decision, condition, path coverage; loop testing; data-flow testing
- **Basis path testing / cyclomatic complexity (McCabe)**: **V(G) = E − N + 2** = **D + 1** (D = number of decision/predicate nodes) = number of regions in the flow graph = number of independent paths
  - Flow graph with 9 edges and 7 nodes → V(G) = 9 − 7 + 2 = **4**; code with 3 `if`s → V(G) = 4
  - V(G) > 10 suggests the module is too complex

## Black-box (functional, behavioural) testing
- Uses only the specification
- **Equivalence partitioning**: input range 1–100 → classes < 1 (invalid), 1–100 (valid), > 100 (invalid) → one test each
- **Boundary value analysis**: test at and around the edges → 0, 1, 2, 99, 100, 101 (for n inputs the basic BVA gives 4n + 1 cases)
- Decision tables, cause–effect graphs, state-transition testing, orthogonal array testing, error guessing
- Grey-box = mix of both

## Other kinds
**Regression** (re-run old tests after changes), smoke (build verification), sanity, usability, compatibility, **mutation testing** (insert small faults to judge the test suite), static analysis

## Debugging
Brute force (memory dumps, print statements), **backtracking** (trace back from the symptom), **cause elimination** (binary partitioning / induction–deduction); automated debuggers

## Quality assurance and configuration management
- **SQA**: standards, reviews (formal technical review, inspections – Fagan), audits, metrics; quality factors (McCall: product operation, revision, transition)
- Cost of quality: prevention, appraisal, failure (internal, external)
- **CMMI / CMM** levels: 1 Initial, 2 Repeatable/Managed, 3 Defined, 4 Quantitatively managed, 5 **Optimizing**; ISO 9001; Six Sigma (DMAIC, 3.4 defects per million)
- **Software configuration management (SCM)**: identification, **version control**, **change control** (change request → CCB approves), configuration audit, status reporting; **baseline** = reviewed, agreed work product
- Maintenance types: **corrective** (fix bugs), **adaptive** (new environment), **perfective** (new features/improvements – largest share), **preventive** (re-engineering)

## Traps
- Alpha test at the **developer's** site; beta at the **customer's**
- Cyclomatic complexity = E − N + 2P for P connected components (P = 1 normally)
- Stubs for top-down, drivers for bottom-up
- Perfective maintenance takes the most effort"""}],
}
