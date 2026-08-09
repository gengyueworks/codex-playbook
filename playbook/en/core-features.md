# Codex Core Features: Threads, Sandbox, Plugins, Skills, MCP

> This chapter comes from the Codex Orange Book's core features section + my real usage.
> The key goal: clarify the three most-confused concepts — Plugin, Skill, MCP — plus the Thread and Sandbox you should understand from day one.

---

## 1. Thread: one task, one conversation

A Thread is a "task conversation" in Codex.

**Project = a code folder; Thread = one specific task within that project.**

For example, if the project is "Xiaohongshu Cover Generator":
- Thread 1: build the homepage
- Thread 2: fix image upload failure
- Thread 3: optimize mobile layout
- Thread 4: write project docs

**Why threads matter?**
Different tasks should be done separately. If you cram "build homepage, fix bug, change styles, write docs" into one conversation, Codex gets confused about context, and you can't tell what it actually changed.

**In one sentence: one clear task = one thread.**

### How I use it

- Before each job, ask: is this one task or many?
- One task, one thread. Archive it when done — the project list stays clean.
- Found a new problem? Open a new thread. Don't continue the old conversation.

---

## 2. Sandbox: Codex's safety fence

Codex isn't a normal chat tool — it reads files, edits files, runs commands. So there must be a "fence" limiting what it can touch.

**The sandbox decides whether Codex can:**
- Read files
- Edit files
- Access directories outside the project
- Go online
- Run high-risk commands

**Three permission levels:**

| Option | What it does | Risk |
|---|---|---|
| Request approval | Ask you before crossing boundaries | Safe, recommended for beginners |
| Auto-approve | Let the system judge some approvals | Medium |
| Full access | Open the sandbox, do anything | Highest, not for beginners |

**My advice: beginners use "Request approval."** Let Codex work inside the project, but stop and ask you when it hits boundaries, networking, or high-risk commands. Don't enable full access from day one.

---

## 3. Plugin vs Skill vs MCP: the relationship (the most important table)

These three are the easiest to confuse. They don't replace each other — each handles a different layer:

| Concept | One sentence | What problem it solves | Analogy |
|---|---|---|---|
| Plugin | Capability package | Install, package, distribute abilities | Toolbox |
| Skill | A fixed working method | "How" to do a type of task | Manual inside the toolbox |
| MCP | Interface to external tools | "Which tool or data" to connect | Power outlet for the toolbox |

**Remember it in one sentence: plugins package Skills and MCP into easily installable capability packs; Skills handle "how", MCP handles "which tool to connect."**

---

## 4. Skills in detail

A Skill is a **fixed working method** you prepare for Codex.

Codex already reads code, edits code, runs commands. But if you often ask it to do the same type of task — write READMEs, do code review, generate web pages, organize documents — you can turn that process into a Skill.

**What a Skill consists of:**

| Component | What it is |
|---|---|
| Prompt | The prompt for this task |
| Workflow | The process |
| Template | A fixed template |
| Instruction | Long-term rules for Codex |
| Resource | Reference materials included in the Skill |
| Script | Optional automation scripts |

**Example: a README Skill**

You always want Codex's READMEs to include: project intro, install steps, run commands, file structure, FAQ.

Make a README Skill. From then on, no need to explain the rules every time — just invoke the Skill and Codex follows that process.

**A non-programmer's take: a Skill is the instruction manual where you teach AI "how to work."** I can't code, but I can write my writing standards, my process, my templates into a Skill, so Codex works to my standards.

---

## 5. MCP in brief

MCP (Model Context Protocol) is the interface for connecting external tools.

**It solves "how Codex connects to your tools and data."**

- Database MCP: let Codex query databases directly
- Document MCP: let Codex read/write your document system
- Browser MCP: let Codex operate a browser

**My take: MCP is the power outlet for Codex.** Plug in whichever tool you want it to use. This leans developer-side; casual users can ignore it until needed.

---

## 6. Common plugins and capability directions

| Type | Plugins | Main use |
|---|---|---|
| Browser & computer | Chrome, Computer Use | Operate the browser, see the screen and click like a human |
| Code & project | GitHub | Manage repos, fix bugs, create PRs |
| Frontend & design | Build Web Apps, Figma | Generate web pages from one sentence, design-to-code |
| Office delivery | Documents, Presentations, Spreadsheets | Formal docs, quality PPT, data analysis |
| Video generation | HyperFrames, Remotion | HTML to video, code-based professional video |

> Plugin catalogs change with versions. Check your current Codex plugin page.

---

## My core takeaway

These features look developer-oriented, but the underlying logic applies to anyone using Codex:

- **Thread** → "do one thing at a time", same as writing in sections
- **Sandbox** → "safety boundary", keeps AI obedient without overstepping
- **Skill** → "teach AI your standards", my writing standards are my Skills
- **MCP** → ignore for now, learn when needed

**Tools are built by engineers, but the way you use them belongs to everyone.**
