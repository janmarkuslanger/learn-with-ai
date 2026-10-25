# Quiz session

Part of the coaching protocol — `AGENTS.md` is the entry point and its general rules
(warm-up, retrieval loop, SRS rules, tracking) apply on top of this file.

**Output:** `quizzes/YYYY-MM-DD-quiz.md` from `templates/quiz.md`.

- **Timing (hard default):** a quiz runs earliest on the day **after** its concept session — never in the same session. Same-day retrieval only measures short-term memory, not learning. If the learner explicitly insists on a same-day quiz after being told this, run it, note **same-day** in the quiz file, and start the topic's first SRS interval at 3 days instead of 7.
- **Before writing questions**, read the concept file for this topic (`concepts/YYYY-MM-DD-<slug>.md`). Only test what was explicitly covered there. Do not introduce details, edge cases, or sub-concepts that weren't part of that session. If no concept file exists, say so and do not run the quiz.
- **Cross-topic check (mandatory):** before finalizing the question list, check every question against `PROGRESS.md`. If a question touches a concept from a topic not yet marked ✅ (Concept column), remove or replace it — this applies even if the concept appears only as a contrast or delineation in the current topic's concept file. If it is unclear whether the learner has covered a concept (adjacent topic, ambiguous entry), **ask before including the question** — in the session language from `CURRICULUM.md`: "Have you already had a session on [topic]?" Wait for the answer before finalizing that question.
- Run every question through the **retrieval loop** (`AGENTS.md` § Retrieval loop), with full error analysis on wrong or partial answers.
- Record correctness, confidence, and — for wrong answers — the error cause in the output file, not just "wrong".
- Flag answers that were correct but with low confidence as **"lucky"** — these need review just as much as wrong answers.
- At the end, summarize which items go into the gap tracker: wrong answers AND low-confidence correct answers.
- **After the quiz:** add the topic to `## Review schedule` in `PROGRESS.md` — starting interval 7 days (3 days for a same-day quiz), `Next review` = today + interval. This is how topics enter the SRS cycle.
