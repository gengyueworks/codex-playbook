# 09 How to Debug a Bad Result

The deeper you use Codex, the more failures you will see. The waste comes from restarting everything before finding which step failed.

When I processed 35 course videos, the web transcription route stopped producing usable text. I checked the account and task state, tested a local Whisper route, used a model mirror, and only then expanded to the full batch. Each decision had evidence behind it.

## Describe the symptom

```text
I intended to complete:
What I actually saw:
The last point that worked:
What I already tried:
```

Then ask for diagnosis only:

```text
Do not modify files or retry the entire process yet.
List the three most likely causes from this symptom, with one minimal check for each.
Mark which checks are read-only.
```

## Six common situations

| Symptom | Check first | Direction |
|---|---|---|
| File not found | Open folder and actual path | Reopen the right project and list files |
| Output looks invented | Sources for dates and numbers | Require a source for every claim |
| Too many files changed | Diff and latest assignment | Restore extras and narrow the scope |
| Automation stopped | Latest log, permissions, input time | Reproduce one date before editing |
| Batch missed items | Expected count and failure list | Add counters and rerun only failures |
| Inconsistent format | Rule file and latest good output | Put the repeated standard in a rule or Skill |

## Switching a transcription route

For a batch failure:

1. Confirm that the original files are complete.
2. Test the current tool with one small file.
3. Identify whether the failure is account, network, format, or model related.
4. Save successful outputs and a failure list before changing tools.
5. Test the replacement with one file before expanding the batch.

After a 35-file run, “finished” is weak evidence. Record total, success count, failure count, and filenames.

## When to stop

Pause and preserve the current state when continuing would require deleting originals, sending private data to an external service, widening account permissions, publishing publicly, or making a decision you cannot evaluate.

Write down the symptom, log, current files, and next check. A paused task can resume from evidence.

## A small incident note

```markdown
# 2026-08-11 transcription batch

Symptom: the web transcription task produced no downloadable text.
Confirmed: source videos were complete; one-file upload also failed.
Tried: checked account state and saved a failure list.
Next: test a local route with one file before batching.
```

Write the solution back into the rule file or Skill when the same failure could happen again.

## Chapter checkpoint

- [ ] I can describe a failure as a concrete symptom.
- [ ] I can test one small input before rerunning a batch.
- [ ] I can preserve logs, originals, and a failure list.

The final chapter collects the templates and the shortest path to building your own system.
