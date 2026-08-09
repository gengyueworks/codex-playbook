# Codex Playbook · One-Page Version

> Full version: [full.md](full.md). This page distills what matters most.

---

## 1. What Codex is

A programmer who lives in your computer and speaks human language.
I decide *what* I want, it decides *how*. **I'm the boss, it's the employee.**

## 2. Get started (3 minutes)

```bash
cd your-project
codex
```

Say it in plain language: "Make this README more attractive."

| Command | What it does |
|---|---|
| `codex` | Interactive mode |
| `codex "task"` | Direct task |
| `--full-auto` | Fully automatic |
| `--ask-for-approval` | Ask before every step (recommended for beginners) |

## 3. The plain-language formula

```
Role + Task + Context + Acceptance criteria
```

Bad: "optimize this"
Good: "You're a senior frontend dev. Make this page mobile-responsive. Project is in src/ using React. After the change, buttons must not overflow at 375px."

## 4. AGENTS.md — the most important habit

Create `AGENTS.md` in your project root and write down your rules (language, style, commit conventions). Codex reads it before every task — no need to repeat yourself.

## 5. Skills

Package frequently-used capabilities into skills (writing polish, repo scaffolding, scheduled tasks) and trigger them with one sentence.

## 6. Three workflows in brief

1. **Writing → Repo**: hand your article to Codex, turn it into a project
2. **Content automation**: scheduled updates via GitHub Actions
3. **Batch processing**: apply one template to dozens of repos

## 7. Five traps

1. No context → give background first
2. Too many tasks at once → break it down
3. Expecting mind-reading → describe what "good" looks like
4. Trusting without verification → make it run its own checks, you spot-check
5. Afraid to correct → say "this doesn't work, do it that way"

## 8. Core belief

> The tool won't create for you — but it lets your creation land.
