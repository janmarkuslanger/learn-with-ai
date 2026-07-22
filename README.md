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

That's it. The agent reads your curriculum and guides everything from there.

---

## How to use

Type one of these in your agent:

```
learn        → auto-select the next session — asks how much time you have
learn 15     → auto-select with a fixed time budget (also: learn s / m / l)
drill        → ~10 min pure retrieval across due topics (the daily anchor)
quiz         → quiz on the last concept (earliest the day after)
concept      → new concept session  (~20–30 min)
kata         → focused design or coding task  (45+ min, splittable)
deep dive    → trade-off discussion  (45+ min, splittable)
review       → spaced repetition over past concepts  (~20–30 min)
```

In Claude Code you can also use slash commands: `/learn 15`, `/review` — same behavior, guaranteed trigger.

The agent reads `PROGRESS.md` and `CURRICULUM.md` automatically.
It knows exactly where you are and what comes next.

**Every session starts with the time question: S (~10 min) / M (~25 min) / L (45+ min).**
Ten minutes is a real session — a drill or a quiz — not a skipped day.

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
/review         ← Spaced review logs + drills.md (compact drill log)
/templates      ← Markdown templates for each session type
```



---

## Tips

- **Short days consolidate, long days extend.** New material enters on M/L days; S days strengthen what's there. Both count — a daily 10-minute drill beats a weekly 60-minute marathon for retention.
- **The quiz comes the day after the concept.** That's deliberate: it tests what you kept, not what you just heard.
- **Big sessions can be split.** If time runs out mid-kata, the agent pauses and resumes next time.
- **Be honest in quizzes.** The agent tracks your gaps and revisits them.
- **Use `learn` each time.** The agent picks the right next session automatically.
- **Topics are right-sized automatically.** Default per topic: concept + quiz + one application session. The agent expands load-bearing topics to the full cycle and trims small ones — it announces each call, and one word from you overrides it.
- **Reviews happen naturally.** After every 4 completed topics, the agent inserts a review.
- **Gap weeks are fine.** Come back after a break and the agent picks up exactly where you left off.
- **Real projects make it stick.** Add your actual projects to `CURRICULUM.md`.

---

## Customizing

Everything is driven by `CURRICULUM.md`. To change your learning path:
- Edit the phases and topics in `CURRICULUM.md`

No need to touch `AGENTS.md` or templates unless you want to change how sessions work.
