# Codex Playbook · Full Version (EN)

> Author: a liberal-arts writer. Doesn't code. Gets things done with Codex.
> Every section here comes from real usage — not a translation of official docs.

---

## Chapter 1: What Codex is

Codex is OpenAI's coding agent. Think of it as:

**A programmer who lives in your computer and speaks human language.**

- You talk to it in a terminal
- It reads your project files, edits code, runs commands
- You watch it work and correct it anytime

It's not a toy that "auto-generates code." It's an **assistant that can complete a task end-to-end on its own.**

### A liberal-arts perspective

Programmers see Codex as a tool to "write code faster."
I see Codex as "**the hands that turn ideas into reality.**"

I can't code, but I know what I want. Codex handles the *how*; I handle the *what* and the *whether it's good*.

**That's a division of labor, not a replacement.** I'm the boss. It's the employee.

---

## Chapter 2: Getting started (3 minutes)

### 1. Install

- **Official App**: download the Codex app from OpenAI's site (macOS / Windows)
- **CLI**: install the `codex` command-line tool (officially supported)
- **Web**: Codex is also available inside ChatGPT (Pro users)

### 2. Log in

Use your OpenAI account. Requires a ChatGPT Plus or Pro subscription.

### 3. First conversation

Open a terminal, go to your project:

```bash
cd your-project
codex
```

Then just say it plainly:

```
Make this README more attractive
```

It starts working. **Say whatever comes naturally — plain language is fine.**

### 4. Common commands

| Command | What it does |
|---|---|
| `codex` | Interactive mode |
| `codex "task"` | Direct task |
| `codex --full-auto` | Fully automatic (runs to completion) |
| `codex --ask-for-approval` | Ask before every change (recommended for beginners) |

---

## Chapter 3: The secret to speaking plainly

Codex is not a search engine. The more specific your instruction, the better it works.

### Good instructions vs bad instructions

| Bad | Good |
|---|---|
| help me optimize | Make the homepage title more conversational, for an elementary school audience |
| fix a bug | Open login.js line 42, the login button does nothing when clicked, find the cause |
| write a README | Write an English README with a one-line intro, in three sections: Install, Usage, FAQ |

### The universal formula

```
Role + Task + Context + Acceptance criteria
```

Example:

> You're a senior frontend dev (role). Make this page mobile-responsive (task).
> Project is in src/, uses React + Tailwind (context).
> After the change, no buttons overflow at 375px width and everything is clickable (acceptance).

### Give context

Codex reads the files in your project, but it doesn't know what's in your head. **Say the background:**

- What this project is for
- What you tried before
- Why you want this effect

---

## Chapter 4: AGENTS.md — make Codex remember your rules

My favorite feature. Create `AGENTS.md` in the project root, write down the rules, and Codex reads them before every task.

### What my AGENTS.md looks like

```markdown
# Project rules

## Language
- All copy in Chinese
- README bilingual (Chinese + English)

## Style
- Conversational, no AI-sounding tone
- No corporate jargon

## Code
- Don't comment out errors to make it run
- Verify after changes

## Commits
- Commit messages in English, concise
```

### The effect

- No need to repeat yourself every time
- More projects, less effort
- Copy and adapt it for each new project

**This is the first milestone between "using it" and "using it well."**

---

## Chapter 5: Skills — package what you do often

Skills are Codex's "capability packs." Package a task you do often into a skill, then trigger it with one sentence.

### Skill ideas

| Skill | What it does |
|---|---|
| Writing polish | Drop a paragraph in, get it rewritten in my style |
| Repo scaffolding | Say an idea, get project structure + README automatically |
| Scheduled content | Daily tasks that auto-commit updates |
| Translation | Chinese ↔ English, keeping the tone |

### How to use

1. Create a folder in `.codex/skills/`
2. Write a `SKILL.md` describing what it does and how
3. Mention it in conversation to trigger

---

## Chapter 6: Real workflows

### Workflow 1: Writing → Repo

Every long essay I write eventually becomes an open-source repo:

```
1. I write the article (markdown)
2. Codex scaffolds the repo (README, directory structure)
3. Codex organizes the article into it
4. Auto-generate cover/navigation
5. Push to GitHub
```

### Workflow 2: Content automation

Scheduled tasks with GitHub Actions + Codex:

```
1. Write a workflow file (let Codex write it)
2. Set a schedule (e.g. 8am daily)
3. Task: generate/update content
4. Auto commit + push
```

I have a project that auto-updates a scientist-of-the-day calendar — running daily for a month now.

### Workflow 3: Batch processing

I have dozens of similar repos (travel, music, book lists). Let Codex process them in batches against one template:

```
1. Define a template
2. Apply it in batch
3. Spot-check the results
```

---

## Chapter 7: Common traps (lessons learned the hard way)

### Trap 1: Giving a task without context

**Symptom**: It makes things up, and the result is nothing like what you wanted.
**Fix**: Paste the background first, then give the task. More context = better results.

### Trap 2: Too many tasks at once

**Symptom**: It forgets the earlier parts, or starts strong and fades.
**Fix**: Break it down. One task per session; verify before moving on.

### Trap 3: Expecting mind-reading

**Symptom**: "Make it look nicer" — and you don't like what it makes.
**Fix**: Say what "nicer" means to you. Give references, examples, direction.

### Trap 4: Trusting without verifying

**Symptom**: It says "done" but it doesn't actually run.
**Fix**: Make it run its own checks; you spot-check key output. It's the assistant, you're the QA.

### Trap 5: Being afraid to correct it

**Symptom**: It made a mistake, you feel awkward correcting it, and you settle.
**Fix**: Just say "this doesn't work, do it that way." It won't hold a grudge. **The more specific the correction, the better next time.**

---

## Chapter 8: What a non-programmer actually uses it for

Finally, my real usage. **I'm not "learning to code" — I'm creating.**

- My travel stories became open-source travel guides
- My music essays became a music column repo
- My AI ideas became small runnable projects
- My daily writing became an auto-updating content site

Codex didn't turn me into a programmer. It gave me, **as a writer, the ability to make my ideas land.**

That's what I want this book to pass on:

> **The tool won't create for you — but it lets your creation land.**

---

*The manual keeps updating. New field experience gets added as it happens.*
