# 05 Make It Remember Your Rules

Repeating “use Chinese punctuation, keep the README bilingual, check the result” in every conversation gets tiring. Put long-lived project rules in an `AGENTS.md` file.

It is not magical memory. Think of it as a note beside the workbench: when Codex enters the folder, it can read the note before starting.

## Write rules that will last

A content project may need rules about:

- what the project is and who reads it;
- language, tone, and punctuation;
- bilingual README requirements;
- directories containing original material;
- checks required before delivery;
- actions that need approval, such as publishing, deletion, or batch edits.

Rules work best when they describe real habits. A long list of every possible preference becomes a document no one reads.

## A small content-project example

```markdown
# How this project works

## Project

- This is a Chinese content project for general readers.
- Every article needs a clear title, source, and publication date.

## Writing

- Use natural, direct Chinese.
- Use Chinese punctuation in Chinese prose.
- Prefer concrete facts and actions to broad slogans.
- Verify important numbers, dates, and links against their sources.

## Files

- Keep original material under input/ and do not edit it in place.
- Put finished work under output/ with clear filenames.
- Provide Chinese and English entry points in the README.

## Before delivery

- List created and modified files.
- Check links.
- Confirm original material is unchanged.
- Show the diff.
- Ask before publishing, deleting, or making batch changes.
```

Keep the first version short. Add a rule after a real repeated problem, not before.

## Where it lives

At the project root, it can describe the whole project. Deeper files can describe a narrower area. The exact files Codex reads depend on the current project entry and structure, so ask: “Which AGENTS.md files did you find, and which rules will you follow?”

## Ask Codex for a first draft

```text
Based on the last three reasons this project needed rework, draft a short AGENTS.md.

Include only long-lived rules that can be checked. Do not include one-off task instructions.
Group the rules under project, writing, files, and delivery checks.
Show the draft first. Do not overwrite an existing file.
```

Once you review it, ask Codex to write it. When the same error appears again, improve the rule or the Skill instead of repeating the reminder forever.

## When a rule fails

- Codex did not find it: check the filename, location, and project opened.
- The rule is too broad: say what to do, where to do it, and how to check it.
- Two rules conflict: keep one clear version and remove the old wording.
- The file keeps growing: move details into a Skill or project guide.

The next chapter saves a repeatable process as a Skill.

