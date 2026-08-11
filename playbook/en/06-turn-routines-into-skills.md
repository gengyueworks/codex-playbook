# 06 Turn Routines into Skills

If you ask Codex to do the same kind of work every week, save the method.

A Skill is a small folder containing instructions, references, and sometimes helper scripts. It turns “how I usually do this” into something you can call again.

## Run it before you save it

A useful sequence from the course material is: complete the work in plain language, ask Codex to extract the reusable method, then test it with a second input.

For turning an article into a public release, the five steps are:

1. input: notes, source links, and the writer’s additions;
2. processing: structure, headline, and missing information;
3. review rules: facts, voice, format, and privacy;
4. deliverables: article, README, and source note;
5. filing: the correct folder, date, and version.

Run the sequence several times before writing the Skill. A file created too early usually describes an imagined process.

## A minimal folder

```text
article-publishing/
├── SKILL.md
├── references/
│   └── writing-checklist.md
└── scripts/
    └── check-links.sh
```

`SKILL.md` needs to answer four questions: when to use it, what inputs it needs, what steps to follow, and how to check the result.

## A minimal SKILL.md

```markdown
# Article editing and publishing

## Use when

Use this Skill when one or more raw notes need to become a publishable Markdown article.

## Inputs

- Raw material path.
- Topic and reader.
- Facts and sources that must remain.
- Destination folder.

## Steps

1. Read the material and list facts and gaps.
2. Propose the structure and wait for review.
3. Draft under the project rules.
4. Check facts, links, and sensitive information.
5. Deliver the article, source note, and change report.

## Do not

- Turn missing facts into certain claims.
- Overwrite original material.
- Publish or push without confirmation.
```

## AGENTS.md and Skills

Use a simple distinction:

- `AGENTS.md` says what the project always follows.
- A Skill says how to handle one recurring kind of work.

A project can have one rule file and several Skills. Templates and Skills make work across many repositories easier to repeat, while each project still keeps its own facts and exceptions.

## Test the Skill

Use a new input and record:

- whether it found the input;
- whether it proposed a structure before drafting;
- whether it ran the checks;
- where you still had to make a decision.

Write the result back into the Skill. An instruction becomes useful when a new input can test it.

## Practice

Choose a task you have done at least three times: meeting cleanup, README maintenance, article preparation, or batch formatting. Ask Codex to draft a Skill, then test it on a second input. Keep the first and tested versions together.

The next chapter puts a daily project on GitHub Actions with visible checks and a way to pause it.
