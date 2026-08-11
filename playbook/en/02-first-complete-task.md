# 02 Let Codex Finish One Small Task

The three sentences from the previous chapter are still an idea. Now turn them into a real assignment.

This exercise uses public-safe material in `examples/01-first-task/input/`: a product idea, a meeting note, and an old memo. Your goal is to turn them into a work list you can use.

## Open the right working folder

Open `examples/01-first-task/` in Codex. On a first task, let it read the situation before asking it to change anything.

```text
Read the three Markdown notes in examples/01-first-task/input/.

My goal is to turn them into a usable work list.

First tell me:
1. which files you found;
2. where you plan to write the result;
3. how you will keep the original material unchanged;
4. what information is still missing.

Do not create or modify files yet. Give me the plan only.
```

You should see a list of files and an approach before any output is created. If Codex starts writing immediately, say: “Stop at the plan. Wait for my confirmation before changing files.”

## Describe the result

After reviewing the plan, continue with:

```text
Continue with the plan.

1. Extract confirmed facts, action items, and open questions from each note.
2. Merge repeated information and keep the source filename.
3. Create examples/01-first-task/output/整理结果.md.
4. Include four sections: confirmed information, action items, open questions, and source index.
5. Each action item must include the item, owner, due date, and source. If the material has no value, write “Not provided”.
6. Do not modify the original files under input/. Do not invent names, dates, or conclusions.
7. Report the files created, the checks you ran, and the decisions that still need me.
```

The useful shift is that you are describing the result you want to keep, rather than asking for a vague cleanup.

## Check three things

Open `examples/01-first-task/output/整理结果.md` and verify:

1. all three input files appear in the source index;
2. missing owners and dates are marked “Not provided”;
3. the original files under `input/` are unchanged.

You can ask for an evidence report:

```text
List every file you created or modified and explain why.
Compare input/ and output/ and confirm that the original material was not changed.
```

“Done” has meaning only when you can open the result, see its sources, and confirm that the originals are still there.

## If the result is wrong

- Empty output: ask Codex to reread the input folder and report the character count of each file.
- Invented names or dates: require a source for every claim; remove anything without one.
- Modified originals: stop, restore from Git or a backup, and make “input/ is read-only” part of the next assignment.
- Messy structure: ask for the four headings first, then fill them after you approve the shape.

## Chapter checkpoint

You have completed this chapter when you have opened a folder, given an assignment, reviewed a plan, opened the output, and checked the original material.

The next chapter uses a real application-writing case to show how a vague draft becomes a submission under a hard character limit.

