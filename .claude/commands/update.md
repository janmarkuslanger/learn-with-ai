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
- `templates/concept.md`
- `templates/deep-dive.md`
- `templates/kata.md`
- `templates/quiz.md`
- `templates/review.md`
- `templates/drill.md`
- `.claude/commands/learn.md`
- `.claude/commands/review.md`

## Steps

1. Use the GitHub MCP tool `mcp__github__get_file_contents` to fetch each framework
   file listed above from the repository `janmarkuslanger/learn-with-ai` on the
   `main` branch.
2. For each file: compare the fetched content to the local file. If different,
   overwrite the local file with the fetched content using the Write or Edit tool.
3. After all files are processed, report a summary:
   - Which files were updated (with a one-line description of what changed)
   - Which files were already up to date
   - Remind the learner that `CURRICULUM.md` and `PROGRESS.md` were not touched.
4. Do NOT commit or push automatically — leave that to the learner.
