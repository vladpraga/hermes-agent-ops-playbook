# Hermes Agent Ops Playbook

A sanitized public showcase of practical patterns for running local-first AI-agent systems reliably.

This repository documents reusable workflows for Hermes Agent-style personal automation systems: Telegram gateways, scheduled digests, no-agent watchdogs, Obsidian/LLM research wikis, safe media delivery, memory hygiene, and public-safe operational playbooks.

The examples are intentionally sanitized. They use placeholders instead of private paths, client names, chat IDs, tokens, logs, banking data, or personal context.

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

## Showcase workflows

- **Telegram-first personal AI agent OS** — a messaging interface for agent work, approvals, reports, and operational alerts.
- **Obsidian LLM research wiki** — raw sources compiled into linked Markdown concepts, entities, comparisons, and query outputs.
- **Scheduled AI digests** — recurring reports with explicit delivery contracts and local artifacts.
- **Agent radar and governance loop** — watch adjacent frameworks, MCP changes, security issues, and workflow patterns without turning every trend into an install.
- **Agentic AI production readiness** — practical governance checklist for moving agent workflows from demo to auditable production-like operation.
- **No-agent watchdogs** — deterministic scripts that stay silent when healthy and alert only when action is needed.
- **Gateway diagnostics** — log-first triage for delivery, timeouts, stale sessions, and restart behavior.
- **Public-safe showcase pattern** — how to document private automation work without leaking sensitive details.

## Contents

### Docs

- [`docs/no-agent-watchdogs.md`](docs/no-agent-watchdogs.md) — deterministic watchdog pattern for scheduled checks.
- [`docs/cron-reliability.md`](docs/cron-reliability.md) — cron hygiene for AI-agent systems.
- [`docs/telegram-gateway-diagnostics.md`](docs/telegram-gateway-diagnostics.md) — gateway and delivery troubleshooting checklist.
- [`docs/gateway-runtime-contracts.md`](docs/gateway-runtime-contracts.md) — runtime contracts for routing, delivery, renderer behavior, structured metadata, and transport modes.
- [`docs/azure-openai-gpt5-transport-routing.md`](docs/azure-openai-gpt5-transport-routing.md) — explicit Chat Completions vs Responses routing for Azure OpenAI GPT-5.x agent deployments.
- [`docs/agent-radar-and-governance-loop.md`](docs/agent-radar-and-governance-loop.md) — recurring radar loop for agent-framework, MCP, security, and workflow signals.
- [`docs/agentic-ai-production-readiness.md`](docs/agentic-ai-production-readiness.md) — vendor-neutral checklist for governed agent workflows.
- [`docs/server-side-agent-ops.md`](docs/server-side-agent-ops.md) — virtual server and PostgreSQL-backed operations patterns.
- [`docs/obsidian-llm-wiki-workflows.md`](docs/obsidian-llm-wiki-workflows.md) — durable research/wiki workflow for agents.
- [`docs/memory-hygiene.md`](docs/memory-hygiene.md) — memory routing and cleanup principles.
- [`docs/privacy-safe-showcase.md`](docs/privacy-safe-showcase.md) — publishing sanitized examples without leaking private context.
- [`docs/architecture.md`](docs/architecture.md) — reference architecture for a local-first personal agent OS.

### Examples

- [`examples/cron-doctor-summary.py`](examples/cron-doctor-summary.py) — example read-only no-agent cron doctor.
- [`examples/telegram-agent-workflow.md`](examples/telegram-agent-workflow.md) — example Telegram-first agent flow.
- [`examples/llm-wiki-workflow.md`](examples/llm-wiki-workflow.md) — example Obsidian/Markdown wiki workflow.
- [`examples/daily-ai-digest-workflow.md`](examples/daily-ai-digest-workflow.md) — example scheduled digest flow.

### Templates

- [`templates/research-briefing.md`](templates/research-briefing.md) — Markdown research briefing template.
- [`templates/research-briefing.html`](templates/research-briefing.html) — self-contained visual HTML briefing template.
- [`templates/ops-log.md`](templates/ops-log.md) — operational history note template.

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
