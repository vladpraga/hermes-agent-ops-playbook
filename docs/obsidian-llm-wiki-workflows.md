# Obsidian and LLM wiki workflows

Obsidian can act as the durable knowledge layer for local-first AI agent systems. The goal is not to dump transcripts into notes, but to maintain a structured, searchable, reviewable knowledge base.

## Layering model

Recommended separation:

- Chat/session history: raw working context.
- Agent memory: compact durable preferences and facts.
- Fact store: structured recall and relationships.
- Obsidian wiki: canonical concepts, decisions, and research.
- Ops Log: operational history for one-off infrastructure changes.

## Research workflow

A practical wiki workflow:

1. Capture raw sources.
2. Create review candidates.
3. Promote only reviewed concepts to canonical notes.
4. Link concepts with wiki links.
5. Keep an overview or ecosystem map as the navigation hub.
6. Run read-only lint checks for broken links, orphan pages, and stale candidates.

## Ops Log pattern

For infrastructure changes, write an Ops Log note instead of saving temporary task progress in memory.

Include:

- timestamp;
- system/component;
- previous state;
- exact change;
- verification result;
- rollback path;
- what was intentionally not changed.

## Safety rules

- Never delete notes as part of automated cleanup.
- Do not upload private notes to third-party services without explicit approval.
- Keep secrets out of notes and generated reports.
- Prefer local linting and local backups.

## Why this matters

Agent systems become more useful when they can accumulate durable knowledge without polluting their always-on prompt. Obsidian provides the human-readable canonical layer while memory remains compact and operational.
