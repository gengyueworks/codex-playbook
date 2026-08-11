# Quality Gate

Run these checks from the repository root before delivery:

```bash
git diff --check
python3 scripts/quality_gate.py
```

Also run the project maintainer’s sensitive-word check and confirm that the finished guide contains no language that frames reuse as a shortcut or insult.

## Chapter requirements

- [ ] All 10 Chinese chapters exist.
- [ ] All 10 English chapters have matching coverage.
- [ ] Every chapter has an action, visible result, troubleshooting note, or checkpoint.
- [ ] Cases come from the author’s experience or are clearly marked as sanitized exercises.
- [ ] No accounts, secrets, private email addresses, or local private paths appear in finished examples.
- [ ] The README contents are in chapters 1 through 10 order.
- [ ] Markdown table rows have no blank lines between them.
- [ ] Chinese prose uses Chinese punctuation.
- [ ] Link targets exist and encoded Chinese filenames resolve correctly.

## Delivery evidence

The final handoff should report:

1. changed file count;
2. Chinese and English chapter counts;
3. exercise and template counts;
4. `git diff --check` result;
5. link-check result;
6. the local state, including whether anything was pushed to GitHub.
