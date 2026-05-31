# Server-side AI agent operations

Local-first AI agent workflows often start on a laptop, but many practical maintenance tasks eventually touch virtual servers, databases, scheduled jobs, and remote services. This note collects patterns for running those workflows without turning them into fragile black boxes.

## Scope

This playbook is for small, practical automation systems such as:

- cron jobs running on a virtual server;
- Python scripts that enrich or clean operational data;
- PostgreSQL-backed data-enrichment workflows;
- remote log checks and health summaries;
- agent-assisted maintenance where the final action is still explicit and reviewable.

## Principles

1. **Keep routine checks deterministic.** Use Python or shell scripts for repeatable server checks. Bring an LLM in only when summarization, classification, or remediation drafting is actually useful.
2. **Separate data collection from reasoning.** A script can collect logs, counts, statuses, and database metrics. The agent can then summarize a sanitized result.
3. **Stay quiet when healthy.** Watchdogs should produce no output when nothing needs attention. Alerts should be rare and actionable.
4. **Avoid private data in prompts.** Summarize or redact database rows, user content, tokens, chat IDs, and file paths before sending anything to a model.
5. **Make recovery steps explicit.** Every alert should point to the likely cause, the evidence, and the safe next command or manual check.

## PostgreSQL-backed workflows

When an AI-assisted workflow enriches tables in PostgreSQL, prefer a staged pipeline:

1. Select a small batch of pending rows.
2. Export only the fields needed for classification or enrichment.
3. Redact or hash sensitive identifiers where possible.
4. Run enrichment with clear status transitions such as `pending`, `processing`, `done`, and `failed`.
5. Store model output separately from source data.
6. Keep retries bounded and idempotent.
7. Log enough metadata to debug failures without exposing private content.

Example operational checks:

- count rows stuck in `processing`;
- count failed rows by error type;
- detect repeated API failures or rate limits;
- verify that recent batches completed within the expected time window;
- alert only when a threshold is crossed.

## Virtual server maintenance checklist

Before trusting a server-side agent workflow, check:

- cron/systemd timer is installed and enabled;
- logs rotate and do not expose secrets;
- credentials are stored outside the repository;
- network failures and rate limits use backoff;
- database writes are idempotent;
- dry-run mode exists for destructive or bulk actions;
- alert delivery has been tested;
- there is a documented manual fallback.

## Where AI helps

AI coding and agent tools are useful for:

- drafting Python diagnostics;
- explaining unfamiliar logs;
- turning incidents into reusable playbooks;
- reviewing scripts for unsafe assumptions;
- generating test cases for edge conditions;
- summarizing server health for a maintainer.

They should not silently perform destructive actions, rotate secrets, delete data, or change infrastructure without explicit approval.

## Minimal alert format

A good server-side alert should include:

```text
Status: attention needed
System: <service or workflow name>
Evidence:
- <metric/log finding>
- <time window>
Likely cause:
- <short explanation>
Recommended next step:
- <safe command or manual check>
```

This keeps automation useful without requiring the maintainer to inspect raw logs every time.
