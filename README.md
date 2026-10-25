# learn-with-ai

A personal daily learning system powered by AI agents.
10–60 minutes a day — short days consolidate, long days extend. Real progress either way.

Works for any topic — software architecture, distributed systems, product management, languages, anything.

---

## Setup

1. **Clone or download this repo**
2. **Open `CURRICULUM.md`** — fill in your background, goal, real projects, and what you want to learn
3. **Open this repo in your AI agent** (e.g. Claude Code, Cursor, or any agent that reads `AGENTS.md`)
4. **Start your first session** by typing `learn`

The agent reads your curriculum and progress and guides everything from there.

---

## How to use

```
learn        → auto-select the next session — asks how much time you have: S (~10) / M (~25) / L (45+ min)
learn 15     → auto-select with a fixed time budget (also: learn s / m / l)
drill        → ~10 min pure retrieval across due topics (the daily anchor)
quiz         → quiz on the last concept (earliest the day after)
concept      → new concept session  (~20–30 min)
kata         → focused design or coding task  (45+ min, splittable)
deep dive    → trade-off discussion  (45+ min, splittable)
review       → spaced repetition over past concepts  (~20–30 min)
```

In Claude Code, `/learn 15`, `/drill` and `/review` work as slash commands — same behavior, guaranteed trigger.
`/update` pulls framework improvements; `CURRICULUM.md` and `PROGRESS.md` are never touched.

---

## Structure

```
CURRICULUM.md   ← Your personal file: background, projects, curriculum  ← EDIT THIS
PROGRESS.md     ← Current status, gaps, session log (agent maintains this)
AGENTS.md       ← Agent instructions: rotation, SRS, tracking
/protocol       ← Step-by-step spec per session type
/templates      ← Markdown templates for each session output
/scripts        ← check_progress.py — validates PROGRESS.md after every session

/concepts  /quizzes  /katas  /deep-dives  /review   ← your session notes
```

`scripts/check_progress.py` catches broken tables and miscalculated review dates. It needs only
Python 3; run its tests with `python3 -m unittest discover -s scripts`.

---

## Tips

- **Short days count.** New material enters on M/L days; S days strengthen what's there. A daily 10-minute drill beats a weekly 60-minute marathon for retention.
- **The quiz comes the day after the concept.** It tests what you kept, not what you just heard.
- **Be honest about confidence.** A confident wrong answer is the most valuable thing the agent can find.
- **Topics are right-sized automatically.** Default: concept + quiz + one application session. The agent expands load-bearing topics and trims small ones — one word from you overrides it.
- **Breaks are handled.** After 2+ weeks away, the agent checks what stuck before moving on.
- **Real projects make it stick.** Add your actual projects to `CURRICULUM.md`.

To change your learning path, edit `CURRICULUM.md`. `AGENTS.md`, `protocol/` and the templates only need changes if you want sessions to work differently.
