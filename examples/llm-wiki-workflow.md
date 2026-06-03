# Example: Obsidian LLM wiki workflow

Inspired by the LLM-maintained Markdown wiki pattern: raw sources are collected first, then compiled into linked notes.

## Folder shape

```text
AI Agents Research Wiki/
  overview.md
  raw/
    articles/
    papers/
    videos/
  concepts/
  entities/
  comparisons/
  queries/
  review/candidates/
  state/manifest.json
```

## Workflow

1. Save source material under `raw/`.
2. Create a review candidate note with source metadata and summary.
3. Promote stable knowledge into canonical concept/entity/comparison pages.
4. Add backlinks and update the overview/index.
5. Run a read-only lint check for broken links and manifest issues.
6. Save important query outputs back into the wiki.

## Why Markdown first

- Easy to inspect in Obsidian.
- Easy for agents to read and patch.
- Works without a vector database at small/medium scale.
- Git-friendly and backup-friendly.
