# Review session

Part of the coaching protocol — `AGENTS.md` is the entry point and its general rules
(retrieval loop, SRS rules, tracking) apply on top of this file. No warm-up.

**Output:** `review/YYYY-MM-DD-review.md` from `templates/review.md`.

Review sessions are not random — they are targeted. Before starting:

1. **Review schedule in `PROGRESS.md`:** prioritize topics where `Next review ≤ today`. Among those, oldest first.
2. **Gap tracker in `PROGRESS.md`:** include any open gap where `Reviews since last seen ≥ 2`, plus any gap that has never been addressed. These are mandatory regardless of topic priority.
3. Mix 3–5 retrieval questions across these prioritized topics. Do not re-ask quiz questions verbatim — rephrase or change the scenario. Tag each question with difficulty: `[easy]`, `[medium]`, or `[hard]`. Run every question through the retrieval loop (`AGENTS.md` § Retrieval loop) with full error analysis.

After the review, update `PROGRESS.md`:

- **SRS schedule:** recalculate `Next review` for every topic covered (`AGENTS.md` § SRS rules).
- **Gap tracker:** increment `Reviews since last seen` by 1 for every open gap **not** addressed; reset to 0 for gaps that were addressed. Update `Consecutive correct` per `AGENTS.md` § Gap tracker rules.
- `Consecutive reviews` is incremented (`AGENTS.md` § After each session).

The **Phase Exit Review** (`AGENTS.md` § Phase exit gate) is a review session with its own coverage and pass criteria.
