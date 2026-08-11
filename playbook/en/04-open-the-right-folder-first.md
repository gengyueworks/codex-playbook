# 04 Open the Right Folder First

Codex can work with many files. The first question should be where it is looking and what it is allowed to change.

When I synchronized my GitHub profile data, the task was small but easy to overshoot: the profile had reached 102 repositories, while the README badges still said 84. Only three lines needed updating, and the rest of the introduction needed to stay intact.

## Read the situation first

```text
Read the project README and related configuration first. Tell me:
1. the current repository counts shown in the files;
2. where each number appears;
3. the smallest change needed to sync the GitHub profile;
4. how you will verify the live page afterward.

Read only. Do not modify files yet.
```

Numbers should be checked against their source before their wording is changed.

## Limit the change

```text
Update only the three repository-count badge lines in the README.
Keep the personal introduction, links, layout, and other badges unchanged.
Show the proposed change before editing and show the diff afterward.
Do not commit or push. Wait for my review.
```

“Only these three lines” is a useful boundary. A named block or file works too.

## Review the diff, not the promise

```text
Show the complete diff for this task.
Confirm that no other files or sections changed.
Run the checks that fit this project, but do not commit or push.
```

After reviewing the diff, decide whether to commit. After pushing, open the real GitHub page and verify the result there.

## A simple permission rule

For a first task, let Codex work inside the current project folder and keep human confirmation for consequential actions. When the task involves files outside the project, deletion, publishing, account access, or network actions, ask for an explanation before allowing it.

The wider the scope and the harder the action is to undo, the earlier your review should happen.

## Common mistakes

- Opening the wrong folder and assuming Codex can see the files you meant.
- Saying “update the data” without naming the source or allowed location.
- Skipping the diff because the visible text looks correct.
- Checking the local result but never checking the published page.

## Checklist

- [ ] I know which project folder the conversation opened.
- [ ] Codex read the files before editing.
- [ ] I named the file or section it may change.
- [ ] I reviewed the diff.
- [ ] I checked the real page after publishing.

The next chapter turns these habits into a project rule file.

