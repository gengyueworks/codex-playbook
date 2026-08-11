# Contributing

Thanks for helping the Codex field guide stay current and useful. This project keeps a small set of rules so that new content stays real, verifiable, and safe to publish.

## What you can contribute

- Report outdated content (product changes, broken links, changed steps).
- Propose a real, public-safe Codex case.
- Report an exercise that cannot be completed.
- Fix a translation so Chinese and English match.
- Fix a broken link or a small factual error with a source.

Use a GitHub Issue for reports and proposals. Templates exist at:

- [内容过时 / Outdated content](.github/ISSUE_TEMPLATE/内容过时.md)
- [案例建议 / Case idea](.github/ISSUE_TEMPLATE/案例建议.md)
- [练习失效 / Broken exercise](.github/ISSUE_TEMPLATE/练习失效.md)

## Case notes

A case note must record a real operation you did, with:

- background and date;
- inputs and the actual task brief;
- visible results;
- a failure point or limitation;
- how to verify the result;
- a verifiable source.

Private details stay out: no accounts, keys, personal email addresses, local paths, or unpublished materials. Write a sanitized version before opening a pull request.

## Translations

The Chinese chapters are the primary experience narrative; English pages mirror the same facts, steps, and acceptance checks. Do not merge one language without the other. If you change a Chinese chapter, update the matching English page in the same pull request (and vice versa).

## Quality gate

Before submitting, run from the repository root:

```bash
python3 scripts/quality_gate.py
git diff --check
```

Both must pass. The same checks run automatically on every pull request and push to `main`.

## Review

Content only enters `main` after the author reviews facts, privacy, links, and voice. Drafts and new cases may be kept in `docs/maintenance/drafts/` until then.
