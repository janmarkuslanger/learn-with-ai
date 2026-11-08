# /update — Sync framework files from the upstream template

Fetch the latest versions of all framework files from the upstream repository
`janmarkuslanger/learn-with-ai` and overwrite them locally.

## Protected files (never touch)

- `CURRICULUM.md` — learner-specific curriculum
- `PROGRESS.md` — learner-specific progress tracking

Only files explicitly listed in the allowlist below will be updated. All other files in the repository (including learner-generated session outputs in `concepts/`, `quizzes/`, `katas/`, `deep-dives/`, and `review/`) must never be touched automatically — handle any changes to unlisted files manually.

## Framework files to update

- `AGENTS.md`
- `README.md`
- `LICENSE`
- `.gitignore`
- `protocol/concept.md`
- `protocol/quiz.md`
- `protocol/kata.md`
- `protocol/deep-dive.md`
- `protocol/review.md`
- `protocol/drill.md`
- `protocol/mixed.md`
- `templates/concept.md`
- `templates/deep-dive.md`
- `templates/kata.md`
- `templates/quiz.md`
- `templates/review.md`
- `templates/drill.md`
- `scripts/check_progress.py`
- `scripts/test_check_progress.py`
- `.claude/commands/learn.md`
- `.claude/commands/drill.md`
- `.claude/commands/review.md`
- `.claude/commands/update.md` — always processed **last**, so this run finishes with the instructions it started with

## Steps

1. Fetch each framework file listed above from `janmarkuslanger/learn-with-ai` on the `main` branch.
   Use the first method that works, and keep using it for the rest of the run:
   1. GitHub MCP tool `mcp__github__get_file_contents`
   2. GitHub CLI: `gh api "repos/janmarkuslanger/learn-with-ai/contents/<path>?ref=main" -H "Accept: application/vnd.github.raw"`
   3. curl: `curl -fsSL "https://raw.githubusercontent.com/janmarkuslanger/learn-with-ai/main/<path>"`

   If a single file cannot be fetched (e.g. 404 because it does not exist upstream yet), skip it and report it — never overwrite or delete a local file based on a failed fetch. If no method works at all, stop and report why.
2. For each fetched file: compare it to the local file. If different — or missing locally — write the fetched content with the Write or Edit tool.
3. If `PROGRESS.md` exists and `scripts/check_progress.py` was fetched, run `python3 scripts/check_progress.py`. If it reports errors, the learner's `PROGRESS.md` predates a format change: list the errors and propose the fixes, but do not edit `PROGRESS.md` without the learner's go-ahead.
4. Report a summary:
   - Which files were updated or created (with a one-line description of what changed)
   - Which files were already up to date
   - Which files could not be fetched, and why
   - Remind the learner that `CURRICULUM.md` and `PROGRESS.md` were not touched.
5. Do NOT commit or push automatically — leave that to the learner.
