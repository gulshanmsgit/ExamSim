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
- **Explanation for every question**: 1–3 sentences saying why the answer is right (and for numericals, the worked steps).
- **Accuracy first.** If unsure about a fact, write a different question. No questions on things that differ between textbooks
  unless the question names the convention (e.g. "according to Morris Mano…").
- **No duplicates** across the whole bank (the builder rejects exact duplicates in one pack; do not reword the same question).
- Sources: Paper 2 → Mano (COA), Sebesta / Kernighan-Ritchie / Balaguruswamy (languages), Elmasri & Navathe, Silberschatz,
  Galvin, Forouzan, Tanenbaum, Pressman, Cormen, Rosen, Russell & Norvig, Sinha (fundamentals). Paper 1 → KTBS textbooks, NCERT, standard psychology texts.

## 4. File layout and naming

- Content modules: `tools/p2u<N>_<a,b,c…>.py` (Paper 2) or `tools/p1_<subj>_<a,b…>.py` (Paper 1). Each exports
  `TOPICS = {"<planner topic name>": [("1 · <Sub-topic>", QUESTIONS), ("2 · <Sub-topic>", QUESTIONS), …]}`.
  Question tuple: `(question, [4 options], correct_index, explanation)`. Keep each module under ~60 KB (about 2–3 topics).
- Assembler: `tools/pack_p2_u<N>.py` / `tools/pack_p1_<subj>.py`, modelled on `tools/pack_p2_u2.py`
  (asserts topic names against the structure pack, asserts set size, sets `tag` = sub-topic name, calls `packlib.build_pack`).
- Output: `packs/p2-u<N>-complete.json` or `packs/p1-<subj>-complete.json`. Partial units: `packs/p2-u<N>-<NN>-<slug>.json`.
- Set names: `"<n> · <Sub-topic>"` numbered from 1 inside each topic; `tag` = the text after `· ` (results break down by it).
- Mock-test sets (full-length practice) go in topic `Mock tests` (Kannada: `ಮಾದರಿ ಪರೀಕ್ಷೆಗಳು (Mock tests)`) and are not in the syllabus map.

## 5. Step-by-step workflow for one unit / subject

1. Read the unit's topics in the structure pack (names, `plan.coverage`) and the matching section of the syllabus PDF.
2. Write the split into `tools/syllabus_map.json`: `"<subject>": {"<topic>": ["Sub-topic 1", "Sub-topic 2", …]}`.
3. Write the questions in content modules, set by set, following section 3.
4. Build: `python tools/pack_p2_u<N>.py packs/p2-u<N>-complete.json` (fix anything it reports; check the printed A–D spread).
5. Add the pack to `packs/index.json` (hand fields: `group`, `file`, `name`, `description`), then `python tools/make_index.py`.
6. `python tools/check_packs.py` must print no ERROR lines.
7. Test in the browser in demo mode: import from Question bank, open a topic, run a set, check the study-plan day shows it.
8. Bump `CACHE` in `sw.js`, update the status table in `CLAUDE.md`, commit, and tell the owner to run `git push origin main`.
