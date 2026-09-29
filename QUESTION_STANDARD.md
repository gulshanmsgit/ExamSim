# Question-set standard (every agent must follow this)

This is the fixed recipe for creating question packs for ExamSim. Follow it exactly; `python tools/check_packs.py`
enforces the checkable parts and must pass before any commit.

## 1. Where the organisation comes from: planner = skeleton, syllabus = detail

| Level in the app | Comes from | Example |
|---|---|---|
| **Subject** | Study planner (one per Paper 1 subject / Paper 2 unit) | `P2 · Unit 3 – Computer System Architecture` |
| **Topic** | Study planner row (has a plan ID and dates) | `Memory Hierarchy` (`P2-U3-09`, 27–28 Oct) |
| **Set** (one per sub-topic) | Official syllabus PDF (`GPT_P1.pdf` / `GPT_P2.pdf`), guided by the planner's *coverage* column | `3 · Cache Memory` |
| **Question** | Standard reference books for that syllabus item | — |

- Never invent subjects or topics. Subject and topic names are copied **exactly** from `packs/gpstr-cst-2026-00-structure.json`
  (generated from the planner, en dash `–`). That exact match is what links questions to the study plan.
- The syllabus PDF decides **how a planner topic is split into sets**: take the syllabus items that the planner topic covers
  (its `plan.coverage` text lists them), group closely related items, and give each group one set.
  Usually 2–6 sets per topic. Every syllabus item must land in exactly one set; nothing from the PDF may be dropped.
- Record the split in `tools/syllabus_map.json` **before writing questions** (see section 5). That file is the contract;
  the checker verifies the built pack against it.

## 2. How a pack reaches the study plan (why the names matter)

1. The structure pack gives every topic a `plan.id` (e.g. `P2-U3-09`) and dates.
2. A question pack uses the same subject + topic names, so import merges its sets into those topics.
3. `python tools/make_index.py` finds each pack topic's plan ID and writes it into `packs/index.json` → `planIds`.
4. In the app, 📅 Study plan → Today shows the day's tasks by plan ID. "Import questions for this day" imports every bank pack whose
   `planIds` cover those tasks, and "Practise this day" / the weekly mock draw from those topics. Subject and topic pages show
   "📦 ready in the bank".

If a topic name differs by even one character, the questions land in a new orphan topic and never show on the plan day.

## 3. Content rules

| Rule | Paper 2 (Computer Science) | Paper 1 (General) |
|---|---|---|
| Language | English only | General Kannada in Kannada; other subjects in English |
| Questions per set | **30** | **20** |
| Level | UGC-NET CS / GPSTR-CST level | GPSTR-CST level (KTBS textbooks 6–10 for Kannada) |
| Current affairs | not applicable | **excluded** (also GK-16/17) |

Every set, both papers:
- **Mix of formats** (per 30-question set, roughly): ≥ 8 direct concept, ≥ 5 multi-statement ("Which of the following are correct / INCORRECT"),
  ≥ 3 assertion–reason, ≥ 2 match-the-following, ≥ 4 numerical or scenario/code-trace (where the topic has numbers), rest application.
  Scale down proportionally for 20-question sets. No trivial "What is the full form of…" filler beyond 2 per set.
- **Answers spread across A–D.** `packlib` shuffles normal options. Ordered option sets (assertion–reason `AR`, `I_II`, "All of the above")
  are *not* shuffled, so choose their correct index deliberately: across a set, AR answers must use at least 3 of the 4 options
  and I/II answers must not all be "Only I". No letter above 40% of a set.
- **Four distinct, plausible options.** Distractors are real mistakes (common misconception, wrong formula, off-by-one), never joke options.
  Use "All of the above" / "None of the above" at most twice per set.
- **Previous-year pattern (PYQ) questions: about 20–30% of every set** (≥ 5 of 20, ≥ 7 of 30 where the topic has them). These are the
  classic questions that recur in KPSC / KEA (GPSTR, KARTET, FDA/SDA) / SSC papers for Paper 1 and UGC-NET CS / GATE / KEA papers
  for Paper 2 (standard facts, named theorists, textbook numericals). Mark each by starting its explanation with
  `PYQ pattern (<exams>). ` via a `PYQ` constant in the module. Never claim a specific paper or year ("KPSC 2019") unless it was
  verified from an official or credible source, and never copy a question from a copyrighted guide word for word – write it fresh.
- **Explanation for every question**: 1–3 sentences saying why the answer is right (and for numericals, the worked steps).
- **Accuracy first.** If unsure about a fact, write a different question. No questions on things that differ between textbooks
  unless the question names the convention (e.g. "according to Morris Mano…").
- **No duplicates** across the whole bank. The app identifies a question by its text + options, ignoring only spacing and case
  (`qKey` in index.html); `check_packs.py` uses the same rule. Two different questions must not share the same stem *and* options.
- **Layout**: use `
` for line breaks (the app keeps them): code snippets, 'I. … II. …' statements, AR's 'Assertion (A): …
Reason (R): …'.
- **Match-the-following** format: `"<stem>
a. X  b. Y  c. Z  d. W
1. P  2. Q  3. R  4. S"` with options like `"a-4, b-3, c-2, d-1"`
  (two spaces between items). Write the columns in any convenient order: `packlib` renumbers the right column (so the correct code
  varies), rewrites every option code to match, and lays each item on its own line.
- Sources: Paper 2 → Mano (COA), Sebesta / Kernighan-Ritchie / Balaguruswamy (languages), Elmasri & Navathe, Silberschatz,
  Galvin, Forouzan, Tanenbaum, Pressman, Cormen, Rosen, Russell & Norvig, Sinha (fundamentals). Paper 1 → KTBS textbooks, NCERT, standard psychology texts.

## 4. File layout and naming

- Content modules: `tools/p2u<N>_<a,b,c…>.py` (Paper 2) or `tools/p1_<subj>_<a,b…>.py` (Paper 1). Each exports
  `TOPICS = {"<planner topic name>": [("1 · <Sub-topic>", QUESTIONS), ("2 · <Sub-topic>", QUESTIONS), …]}`.
  Question tuple: `(question, [4 options], correct_index, explanation)`. Keep each module under ~60 KB (about 2–3 topics).
- Builder: **`python tools/build_subject.py <key>`** (keys and their modules are listed in `PACKS` at the top of that file; add a new
  subject or module there). It checks topic names against the planner, set names against `tools/syllabus_map.json` and set sizes,
  writes `packs/<key>.json`, adds/updates its entry in `packs/index.json` and runs `make_index.py`. `build_subject.py all` rebuilds everything.
- Output: one pack per subject/unit that grows topic by topic: `packs/p2-u<N>.json`, `packs/p1-<subj>.json`
  (older packs keep their names: `p2-u1-complete`, `p2-u2-complete`, `p2-u5-01-dbms-concepts`, `p1-kannada-complete`).
- Set names: `"<n> · <Sub-topic>"` numbered from 1 inside each topic; `tag` = the text after `· ` (results break down by it).
- Mock-test sets (full-length practice) go in topic `Mock tests` (Kannada: `ಮಾದರಿ ಪರೀಕ್ಷೆಗಳು (Mock tests)`) and are not in the syllabus map.

## 5. Step-by-step workflow for one unit / subject

1. Read the unit's topics in the structure pack (names, `plan.coverage`) and the matching section of the syllabus PDF.
2. Write the split into `tools/syllabus_map.json`: `"<subject>": {"<topic>": ["Sub-topic 1", "Sub-topic 2", …]}`.
3. Write the questions in content modules, set by set, following section 3.
4. Build: `python tools/build_subject.py <key>` (fix anything it reports; check the printed A–D spread). This also lists the pack
   in the Question bank (`packs/index.json`) and refreshes plan IDs.
5. Re-read a sample of the built questions as a student would (code outputs, numericals, 'which is INCORRECT' options).
6. `python tools/check_packs.py` must print no ERROR lines.
7. Test in the browser in demo mode: import from Question bank, open a topic, run a set, check the study-plan day shows it.
8. Bump `CACHE` in `sw.js`, update the status table in `CLAUDE.md`, commit, and tell the owner to run `git push origin main`.

## 6. How the owner asks, and what each request means

The unit of work is always a **whole planner topic** (all of its sub-topic sets), whichever way it is requested.
A topic "has questions" when its sets exist in a pack listed in `packs/index.json`. Skip such topics unless the owner says "redo".

| Owner types | Agent does |
|---|---|
| `Generate: next` | Take planner topics **in calendar order** (earliest `plan.start` first, Paper 1 and Paper 2 together) that have no questions yet, up to the batch limit. This is the default way to keep the bank ahead of the study plan. |
| `Generate: <subject or unit>` (e.g. `Generate: P2 Unit 3`, `Generate: Educational Psychology`) | All topics of that subject without questions, in planner order, up to the batch limit. |
| `Generate: day <date>` / `Generate: days <date> to <date>` | Read the `calendar` rows for those dates in `packs/gpstr-cst-2026-plan.json`, take their task IDs (`P2-U3-01`, `P1-GK-05`…; current-affairs `P1-CA-*` ignored), map them to topics, and do those. |
| `Generate: <topic name>` | Just that topic. |
| Any of the above + `redo` | Rewrite those topics' sets (new set content under the same names; tell the owner to delete the old sets in the app before re-importing). |

- **Batch limit per request: about 10 topics (≈ 300–450 questions).** If more remain, finish the batch, commit, and say
  exactly what is left and the command to continue (e.g. "next: `Generate: P2 Unit 3` again for the last 3 topics").
- **Files stay per subject, never per day**: questions for a day are added to that subject's pack
  (`packs/p2-u<N>.json` / `packs/p1-<subj>.json`; the Unit 1/2 and Kannada packs keep their `-complete` names). The pack grows
  topic by topic; its assembler builds whatever topics exist, and its index description says which topics are covered.
  Re-importing a grown pack in the app only adds the new sets, and the study plan finds it by plan ID, so day-wise requests
  still show up under "Import questions for this day".
- Start every request by printing the chosen topics with their plan IDs, dates and planned sub-topic sets, then do the work
  without waiting (unless something is ambiguous). End with: topics done, question count, what is left, `git push origin main`.

## 7. Current affairs (monthly, from January 2026)

- Subject **P1 · Current Affairs** (not a planner subject; declared in `EXTRA_SUBJECTS` in `tools/build_subject.py`). One topic per month
  named `January 2026`, `February 2026`, … with exactly two sets: `1 · Karnataka` (30 Q) and `2 · National` (10 Q) = the owner's
  **75% Karnataka / 25% national** rule. Important schemes (Karnataka guarantees, central schemes) are included.
- Content module `tools/p1_ca_2026.py` (`JAN26_KARNATAKA`, `JAN26_NATIONAL`, …); build with `python tools/build_subject.py p1-ca`.
- **Never write current-affairs facts from memory.** Research each month on the web (PIB, All India Radio News, Deccan Herald, The Hindu,
  Drishti IAS/GKToday monthly pages, Wikipedia "2026 in India"), keep only facts that are dated in that month (older decisions only as
  scheme questions), cross-check anything that looks odd with a second source, and name the source in every explanation.
- Watch for anachronisms: use the office-holders of that month (e.g. Karnataka CM in January 2026 = Siddaramaiah).
