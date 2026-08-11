# 07 Let the Project Run Itself

When a project repeats the same job every day, manual work becomes a burden. In my “One Scientist A Day” project, GitHub Actions handles the daily pick, archive, and site rebuild.

The repository contains 52 scientist profiles across 17 fields. Each morning, the workflow updates the README and archive, then rebuilds the GitHub Pages site.

## Understand the manual process first

```text
Read the project README, data/pool.json, scripts/, and existing workflows.
Write the manual steps for updating the project once a day.
For each step, state the input, output, and visible failure signal.
Do not modify files yet.
```

If the manual process is unclear, automation will only run the confusion faster.

## A readable workflow

```yaml
name: Daily Update

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Run daily update
        run: python3 scripts/daily_pick.py
      - name: Rebuild site
        run: python3 scripts/build_site.py
      - name: Commit changes when needed
        run: |
          git config user.name "content-bot"
          git config user.email "content-bot@users.noreply.github.com"
          git add -A
          if git diff --cached --quiet; then
            echo "No changes to commit"
          else
            git commit -m "Daily update $(date +%F)"
            git push
          fi
```

Each section has a visible purpose: schedule, permissions, scripts, and the no-change exit. Ask Codex to explain it line by line, then run it once with `workflow_dispatch` before relying on the schedule.

## Codex Automations and GitHub Actions

Both can involve recurring work, but they live in different places:

- Codex Automations are personal scheduled tasks that bring Codex back to a recurring piece of work.
- GitHub Actions live in the repository and are useful for checks, file updates, builds, and GitHub Pages publishing.

Choose based on where the result belongs. A public repository update belongs in the repository workflow. A private reminder can start as a Codex scheduled task.

## Add safeguards

For a daily project, I want three safeguards:

- a manual mode and a test date for backfills;
- no empty commit when there is no change;
- a visible warning when the input has not changed for several days.

Check the Actions log daily during the first week. Keep occasional spot checks after the workflow becomes stable.

## Common failures

- A schedule does not run at the exact minute: inspect the Actions page and its queue time.
- The script succeeds but the site does not change: check the written files and the Pages workflow.
- The same content is committed every day: add a “skip existing archive” check.
- A previously working task fails: inspect the latest log, input timestamp, and permissions before rewriting the pipeline.

The next chapter follows a full material-gathering and filtering job.

