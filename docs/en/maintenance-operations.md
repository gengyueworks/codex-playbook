# Maintenance Operations

This file is shared by the author and scheduled agents. It defines ownership, output locations, and human approval points.

## Ownership

### GitHub Actions

Only mechanical checks:

- Run `scripts/quality_gate.py`.
- Check Markdown links, chapter counts, bilingual files, example JSON, and table spacing.
- Run on Pull Requests and updates to `main`.

It does not generate chapters or merge content.

### Weekly maintenance agent

Finds problems and writes a maintenance report:

- Review GitHub Issues, recent commits, and the roadmap.
- Run the quality gate.
- Choose one issue worth handling next.
- Write the investigation in the current monthly report folder.
- Produce a next-step task brief.

By default it creates reports and drafts only. It does not edit the main book, commit, or push.

### Monthly case agent

Turns one real experience into a bilingual case and exercise:

- Handle one case only.
- Confirm facts and public-safe scope first.
- Write the Chinese case, matching English version, and sanitized exercise.
- Run the quality gate.
- Wait for editorial review before linking it from the main book.

### Author

Makes the final decisions about truth, voice, numbers, links, publication, and pushing to GitHub.

## Directory convention

```text
docs/maintenance/
├── weekly-agent-prompt.en.md
├── monthly-case-agent-prompt.en.md
├── reports/
│   └── YYYY-MM/
└── drafts/
    └── YYYY-MM/
```

Reports and drafts are grouped by month.

## Maintenance push rule

For pure maintenance output, agents may commit and push without waiting for the author, provided ALL of the following hold:

- The quality gate passes (`scripts/quality_gate.py` and `git diff --check`);
- No personal information: accounts, keys, personal email addresses, local paths, or unpublished material;
- No edits to main chapters in `playbook/zh/` or `playbook/en/`;
- No deletion or renaming of public files;
- No change to GitHub Actions permissions.

Applicable output: maintenance reports, drafts, contributing guides, roadmap checkboxes, and small fixes to README and docs.

Anything touching main-book text, case facts, personal information, or unverified facts must stay at draft stage until the author confirms. Once pushed, content is public and cannot be retracted; that is the main exposure risk.

## Human approval points

Stop at draft stage before editing main chapters, deleting public files, exposing private information, pushing to GitHub, or changing workflow permissions.

