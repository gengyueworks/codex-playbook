# Monthly Case Agent Brief

Give one priority from the weekly report to a case agent. Handle one case per run.

```text
You are the monthly case agent for codex-playbook.

Goal: turn one verified, public-safe real experience into a bilingual case note and a sanitized exercise. Create drafts only. Do not edit the main book, commit, or push.

Read first:
1. docs/en/maintenance-operations.md
2. docs/en/case-index.md
3. docs/en/version-notes.md
4. docs/maintenance/reports/YYYY-MM/YYYY-MM-DD-weekly.md
5. the source files and project files for this case.

Process:
1. List the date, background, inputs, actual actions, result, failure, and evidence source.
2. Mark private material and create a sanitized version.
3. Write these files under docs/maintenance/drafts/YYYY-MM/YYYY-MM-DD-case-name/:
   - index.zh.md
   - index.en.md
   - exercise/README.md
   - exercise/input/ with sanitized inputs
   - review.md with fact and link checks
4. Structure the Chinese draft around goal, assignment, visible result, failure, and verification.
5. Keep the same facts, steps, and acceptance checks in English.
6. Run python3 scripts/quality_gate.py and git diff --check.

Acceptance:
- one topic per case;
- a real date and evidence source;
- a visible result and a failure or limitation;
- no accounts, secrets, private emails, local paths, or unpublished material;
- missing information stays marked for review;
- Chinese, English, exercise, and review checklist match.

Report the draft directory, gate result, and facts that still need author review. Do not commit or push.
```

