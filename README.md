# learn-with-ai

A personal daily learning system powered by AI agents.
15–20 minutes per day. Structured sessions. Real progress.

Works for any topic — software architecture, distributed systems, product management, languages, anything.

---

## Setup

1. **Clone or download this repo**
2. **Open `CURRICULUM.md`** — fill in your background, goal, real projects, and what you want to learn
3. **Open this repo in your AI agent** (e.g. Claude Code, Cursor, or any agent that reads `AGENTS.md`)
4. **Start your first session** by typing `lernen` or `learn`

That's it. The agent reads your curriculum and guides everything from there.

---

## How to use

Type one of these in your agent:

```
lernen / learn  → auto-select the next session type
concept         → new concept session  (15–20 min)
quiz            → quiz on the last concept  (5 questions)
kata            → focused design or coding task
deep dive       → trade-off discussion
review          → spaced repetition over past concepts
wildcard        → free scenario on any topic
```

The agent reads `PROGRESS.md` and `CURRICULUM.md` automatically.
It knows exactly where you are and what comes next.

---

## Structure

```
CURRICULUM.md   ← Your personal file: background, projects, curriculum  ← EDIT THIS
AGENTS.md       ← Instructions for the AI agent (generic, no changes needed)
PROGRESS.md     ← Current status, gaps, session log (agent maintains this)

/concepts       ← Concept session notes
/quizzes        ← Quiz results
/katas          ← Design tasks and solutions
/deep-dives     ← Trade-off discussion notes
/review         ← Spaced review logs
/templates      ← Markdown templates for each session type
```

---

## Tips

- **One session = 15–20 minutes.** No need to do more at once.
- **Be honest in quizzes.** The agent tracks your gaps and revisits them.
- **Use `lernen` / `learn` each time.** The agent picks the right next session automatically.
- **Reviews happen naturally.** After every 4 completed topics, the agent inserts a review.
- **Gap weeks are fine.** Come back after a break and the agent picks up exactly where you left off.
- **Real projects make it stick.** Add your actual projects to `CURRICULUM.md`.

---

## Customizing

Everything is driven by `CURRICULUM.md`. To change your learning path:
- Edit the phases and topics in `CURRICULUM.md`

No need to touch `AGENTS.md` or templates unless you want to change how sessions work.
