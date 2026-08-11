# 08 Gather and Organize Material

When a collection grows, the hard part is often finding, deduplicating, filtering, and preserving sources.

When I organized my Zhihu AI collection, I had 681 saved items across 32 pages. The final shortlist contained 22 items about using Codex. The process shows why material work should happen in stages with evidence at each stage.

## Confirm the scope first

```text
Inspect the structure of this collection and report:
1. the total number of records;
2. the fields available on each record;
3. pagination, duplicate URLs, missing titles, and missing dates;
4. keyword groups for Codex tutorials, practice, workflows, Skills, and automation.

Read only. Do not modify the original data. Write a short inspection report.
```

If the data comes from a logged-in site, confirm that you have permission to process it. Keep private collections, account details, and credentials out of a public repository.

## Process it in three passes

### Pass one: preserve the source

Keep the raw export separate. You should be able to answer where the 22 selected items came from.

### Pass two: mechanical filtering

Use keywords, categories, URLs, and titles to reduce the set. A script or Codex can handle this pass. It narrows the set; it does not make the final editorial decision.

### Pass three: human review

Open the candidates and confirm that they really cover Codex tutorials, practice, or workflows. Keep news and general discussion in a separate observation list.

## What the output should preserve

```markdown
# Codex Reading List

| Title | Link | Category | Why it stayed | Checked on |
|---|---|---|---|---|
| Example title | https://example.com | Beginner | Has complete steps | 2026-08-11 |
```

Every item needs a title, original link, category, reason for keeping it, and check date. Numbers change, so record the date they describe.

## Ask Codex to work in stages

```text
Process this collection in three stages:

Stage one: inspect count, fields, duplicates, and missing values. Report only.
Stage two: create candidates using the categories “Codex tutorial, practice, workflow, Skill, automation”. Keep the original URLs.
Stage three: after I review the candidates, create the final reading list.

Keep raw data read-only. Write all outputs to a separate directory. Every conclusion must trace back to a source record or source page.
```

The dangerous version is “fetch, filter, and publish everything” in one request. Without checks in between, you cannot tell whether the problem came from pagination, filtering, or broken links.

## Common problems

- Fewer items than expected: compare the pagination total before checking the filter.
- Duplicate articles: deduplicate normalized URLs while retaining the original record.
- A title exists but the page is unavailable: mark it for link review; do not invent a summary.
- Too many candidates: add a reason-for-keeping field and review the candidates before selecting the final list.

The next chapter explains how to narrow down failures without starting over.

