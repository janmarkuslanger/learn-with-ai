# Drill session

Part of the coaching protocol — `AGENTS.md` is the entry point and its general rules
(retrieval loop, SRS rules, tracking) apply on top of this file. No warm-up — the drill is the retrieval.

**Output:** one row appended to `review/drills.md` (create it from `templates/drill.md` if missing). No standalone file per drill.

Pure retrieval, ~10 minutes, 4–6 questions. This is the default S-day session and the backbone of retention — a full session type, not a consolation prize.

- **Selection:** overdue SRS topics first (oldest first), then gaps with `Reviews since last seen ≥ 1`, then earlier topics at random. Interleave — never take all questions from one topic if more than one is available.
- Every question runs through the retrieval loop (`AGENTS.md` § Retrieval loop), with **condensed** error analysis: name the flawed mental model and the correct one in 1–2 sentences, log the gap.
- **SRS:** apply the SRS rules to every topic touched.
- **Gap tracker:** gaps addressed → update `Consecutive correct`, reset `Reviews since last seen` to 0. Gaps not touched keep their counters — drills never increment `Reviews since last seen`; only full review sessions do.
- **`Consecutive reviews` is neither incremented nor reset by a drill.**
- A drill is a full session for tracking: it updates `Last session` and gets a row in the session log (`AGENTS.md` § After each session). `review/drills.md` holds the per-drill detail.
- Never split a drill — it is short by design.
