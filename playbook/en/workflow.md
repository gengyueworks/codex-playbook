# The Standard Codex Workflow: Six Steps from Request to Delivery

> Most Codex failures happen not because Codex can't code, but because the request wasn't clear and the process wasn't controlled.
> This six-step method comes from the Codex Orange Book, battle-tested in real projects.
> Core idea: **a request doesn't become a deliverable directly — it passes through understand, plan, change, verify, review, accept.**

---

## The Six Steps at a Glance

| # | Step | What you do | Why |
|---|---|---|---|
| 1 | Break down the request | Make Codex understand what the task is | Avoid changing things without knowing the structure |
| 2 | Make a plan | List what to do, confirm before acting | Avoid doing too much at once or going off track |
| 3 | Small steps | Change one small piece at a time | Lower error rate, easy to roll back |
| 4 | Test | Run checks + manual verification | Confirm nothing is obviously broken |
| 5 | Review | Look at the diff, check if changes are right | Prevent Codex from touching things it shouldn't |
| 6 | Commit & reflect | Commit code and save the experience | AI executes, you decide |

**Remember it in one sentence: AI executes, you decide.**

---

## Step 1: Break Down the Request (most critical)

Most Codex failures come from unclear requests.

Say only "optimize the homepage" and Codex might delete code it thinks is "useless." Before it touches anything, break the request into questions:

### 1. What's the background?
- Why is this task needed?
- What stage is the project at?
- Why now?

### 2. What problem to solve (be specific)

| Vague | Clear |
|---|---|
| Optimize homepage | Optimize the homepage hero title, subtitle, and CTA button |
| Page looks bad | Adjust card spacing, typography hierarchy, and button styles |
| Login is broken | Fix the issue where clicking login doesn't navigate |
| Build an admin panel | Add a user list page with search, filter, and pagination |

### 3. Which files are relevant?
Tell Codex where files live to reduce blind searching.

### 4. What must NOT be touched (draw the boundary)
This is the most important part. Tell it in advance:
- Don't change which logic
- Don't touch which APIs
- Don't change existing page paths
- Don't upgrade dependencies casually
- Don't do large refactors unless necessary

### 5. What counts as done
Don't just say "when it's done." Tell it what done looks like:

> Acceptance criteria:
> 1. Homepage hero clearly communicates the product
> 2. CTA button is more visible
> 3. Mobile view renders correctly
> 4. No impact on other pages
> 5. Project builds and runs

### 6. What tests are needed
Don't just trust "it's done." Specify how to verify: page preview, console check, build test, manual flow test.

---

## Request Breakdown Prompt Template (copy-paste)

```
Please help me break down this request first. Do NOT modify code yet.

Request: 【write your request here】

Analyze using this structure:

1. Background
- What is the project roughly
- Why is this request needed
- Is this new feature, bug fix, UI polish, or refactor

2. What problem to solve
- What is the specific problem
- To what extent should this be solved
- What is out of scope this time

3. Which files are likely relevant
- Judge which files might be involved from the project structure
- List them, don't modify anything

4. What must NOT be touched
- Which logic should not change
- Which APIs should not be touched
- Which pages or components should not be affected

5. What counts as done
- Give verifiable acceptance criteria

6. What tests are needed
- How to verify after changes

Output the breakdown and wait for my confirmation before starting.
```

---

## Task Template Library

No need to rewrite prompts every time. Copy the right one and fill in your request.

### 📖 Read Project Template (first contact with a new project)

```
Please do NOT modify any code.
Read the current project and output a project understanding report:

1. Tech stack
- Main technologies used
- Frontend/backend/database/build tools

2. Directory structure
- What each main directory does
- Which are core directories, which should not be casually changed

3. How to run
- How to install dependencies, how to start locally
- Whether environment variables are needed

4. Test commands
- Whether test / lint / typecheck / build commands exist

5. Core modules
- Main feature modules and what each does

6. Modification risks
- Which files are high-risk to change
- Which logic should not be touched

Output only the report. Do not modify code.
```

### 🐛 Fix Bug Template

```
I have a bug:
【Symptom】
【Repro steps】
【Expected result】
【Actual result】
【Related files/pages】

Please find the cause first. Do NOT modify directly.
Give me:
1. Possible causes
2. Files to examine
3. Fix plan
4. Risks

Wait for my confirmation before changing code.
```

### ✨ Add Feature Template

```
I want to add a feature:
【Description】
【Entry point】
【Interaction flow】
【Visual requirements】
【Data source】
【Acceptance criteria】

Please read the relevant code and give an implementation plan.
Don't touch unrelated files.
After implementing, run tests and summarize the diff.
```

### 🖥 Frontend Page Template

```
Please build a page with these requirements:
【Purpose】
【Target users】
【Visual style】
【Module structure】
【Chinese copy】
【Responsive requirements】
【Things to avoid】

Give a component breakdown plan first, then implement.
```

### 🔍 Code Review Template

```
Please review the current branch's diff against main.
Focus on:
1. Potential bugs
2. Edge cases
3. Security risks
4. Type issues
5. Performance issues
6. Unrelated changes
7. Test coverage

Do NOT modify code. Output a review report first.
```

### 🔧 Refactor Template

```
Please refactor this module:
【Module path】

Goals:
1. Improve readability
2. Reduce duplicate code
3. Keep behavior unchanged
4. Don't change public API
5. Don't introduce new dependencies

Write a refactor plan first, and explain how to verify behavior is unchanged.
```

### ✅ Write Tests Template

```
Please add tests for:
【Feature description】
【Related files】
【Edge cases】

Requirements:
1. Don't change business logic
2. Cover normal paths
3. Cover error paths
4. Cover edge cases
5. Run tests and report results.
```

### 📄 Write Docs Template

```
Please generate documentation for this project:
1. Project intro
2. Installation
3. How to run
4. Environment variables
5. Common commands
6. Directory structure
7. Development notes
8. FAQ

Don't invent commands that don't exist. Base everything on the actual project files.
```

---

## A Non-Programmer's Addition

This six-step method grew out of developer projects, but the underlying logic applies to anyone using Codex:

- **Break down the request** → it's just "say it clearly." Same as outlining before writing an essay
- **Draw boundaries** → it's "what must not change." For content work, it's "don't touch my core ideas and voice"
- **Acceptance criteria** → it's "what counts as done." Without criteria, AI always delivers "good enough"
- **Commit & reflect** → it's "save the experience." Use it once, save the template, turn AI into your workflow

**Tools are universal. So is the way of working.**
