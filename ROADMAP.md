# Roadmap

This project is an early public playbook for reliable local-first AI agent operations. The roadmap is intentionally practical: small documents, scripts, and checks that can help developers run agent systems safely over time.

## Near term

- Add more no-agent watchdog examples that are silent when healthy and explicit when action is needed.
- Add Python diagnostics for cron logs, gateway delivery, media artifact paths, and stale/broken API calls.
- Add server-side agent operations notes for virtual servers, process supervisors, PostgreSQL-backed workflows, and remote maintenance.
- Add lightweight GitHub Actions checks for example scripts and documentation hygiene.
- Expand security notes around credentials, private logs, chat IDs, local files, and public examples.

## Later

- Turn recurring operational incidents into reusable troubleshooting checklists.
- Add templates for cron job definitions, watchdog scripts, incident summaries, and recovery notes.
- Document maintainer automation patterns for issue triage, pull request review, release checks, and public documentation updates.
- Collect examples that work across local machines, virtual servers, and self-hosted agent setups.

## Non-goals

- This repository does not publish private user data, private logs, secrets, chat IDs, or proprietary workflow details.
- It is not a replacement for Hermes Agent documentation; it is an operations-focused companion playbook.
- It avoids pretending that early experiments are mature infrastructure. Patterns should be documented with clear status and verification steps.
