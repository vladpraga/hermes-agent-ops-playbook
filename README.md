# Hermes Agent Ops Playbook

Practical operational patterns for running local-first AI agent systems reliably.

This repository collects reusable notes, scripts, and playbooks for Hermes Agent-style personal automation systems: Telegram gateways, cron jobs, no-agent watchdogs, Obsidian/LLM wiki workflows, local logs, safe media delivery, and memory hygiene.

## Why this exists

Open-source AI agent frameworks are powerful, but real-world users often struggle with reliability:

- cron jobs that silently fail
- noisy logs and stale alerts
- broken Telegram or gateway delivery
- unsafe file and media artifact handling
- unclear recovery steps
- memory and context hygiene problems
- difficulty turning agent demos into dependable daily infrastructure

This project focuses on the operational and maintainer layer that helps local-first agent systems run safely over time.

## Focus areas

- Reliable cron automation for AI agents
- No-agent watchdog scripts that stay silent when healthy
- Gateway and Telegram delivery diagnostics
- Safe handling of logs, media artifacts, and local files
- Obsidian-based research wiki workflows
- Skill authoring and operational playbooks
- Local-first, privacy-conscious automation patterns

## Intended audience

- open-source AI agent users
- maintainers of local-first agent tooling
- developers running personal automation systems
- people building Hermes Agent / MCP / Obsidian-based workflows

## Contents

- [`docs/no-agent-watchdogs.md`](docs/no-agent-watchdogs.md) — deterministic watchdog pattern for scheduled checks.
- [`docs/cron-reliability.md`](docs/cron-reliability.md) — cron hygiene for AI-agent systems.
- [`docs/telegram-gateway-diagnostics.md`](docs/telegram-gateway-diagnostics.md) — gateway and delivery troubleshooting checklist.
- [`docs/obsidian-llm-wiki-workflows.md`](docs/obsidian-llm-wiki-workflows.md) — durable research/wiki workflow for agents.
- [`docs/memory-hygiene.md`](docs/memory-hygiene.md) — memory routing and cleanup principles.
- [`examples/cron-doctor-summary.py`](examples/cron-doctor-summary.py) — example read-only no-agent cron doctor.

## Status

Early public playbook. The content is based on real operational experience running a local-first AI agent setup and is being cleaned up into reusable documentation and examples.

## Principles

- Local-first by default.
- Silent when healthy; noisy only when action is needed.
- Prefer deterministic scripts over agent calls for routine maintenance.
- Keep secrets out of logs, reports, and examples.
- Treat files, credentials, and messaging gateways as security-sensitive boundaries.
- Document rollback and verification steps for infrastructure changes.

## License

MIT
