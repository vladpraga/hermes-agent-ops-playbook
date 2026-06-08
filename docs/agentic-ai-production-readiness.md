# Agentic AI production readiness checklist

This is a public-safe checklist for moving an AI agent workflow from a demo into a production-like operating environment.

It is intentionally vendor-neutral. It applies whether the agent is built with a local-first assistant, an enterprise agent framework, a support automation platform, or a custom LLM workflow.

## Core idea

The production question is no longer only:

> Can the agent complete the task?

The better question is:

> Can the agent complete the task safely, observably, and with a clear owner, rollback path, and audit trail?

## 12-point checklist

### 1. Workflow owner named

Every agent workflow should have a human owner.

The owner is responsible for scope, allowed actions, escalation, review cadence, and retirement when the workflow is no longer useful.

### 2. Data sources listed

Document every data source the agent can read.

Include:

- local files;
- SaaS tools;
- databases;
- email or messaging systems;
- CRM/support systems;
- web sources;
- memory stores.

### 3. Data boundaries defined

For each data source, define what is allowed and what is out of bounds.

Examples:

- read-only customer support knowledge base: allowed;
- raw private customer records: restricted;
- secrets, tokens, or credentials: never included in prompts or logs.

### 4. Agent actions classified by risk

Group actions into risk tiers.

Example tiers:

- **Low risk**: summarize, classify, draft, search, read-only lookup.
- **Medium risk**: create internal ticket, update non-critical metadata, generate report.
- **High risk**: send external message, change customer record, trigger payment/refund, delete data, modify production config.

### 5. Human approval rules defined

High-risk actions should require approval by default.

A useful default:

- drafts are allowed;
- external sends require approval;
- destructive changes require explicit confirmation;
- payments, account changes, and production changes require a separate policy.

### 6. Tool permissions scoped

Avoid giving an agent full tool access just because a tool server provides it.

Prefer:

- install-time allowlists;
- read-only tools first;
- separate credentials for agent workflows;
- separate environments for experiments;
- first-run smoke tests before real tasks.

### 7. Prompt and workflow versions tracked

If a prompt, skill, workflow, or tool contract matters, version it.

Minimum useful metadata:

- workflow name;
- owner;
- last updated date;
- model/provider assumptions;
- tool permissions;
- expected outputs;
- rollback or disable path.

### 8. Logs and audit trail retained

A production-like agent should leave enough evidence to reconstruct what happened.

Track:

- request/run ID;
- user or triggering system;
- tools called;
- external actions taken;
- output artifact path;
- approval state;
- errors and retries.

Do not log secrets or unnecessary private content.

### 9. Evaluation set exists

Do not rely only on live user feedback.

Maintain a small test set:

- common happy path;
- edge cases;
- known failure cases;
- unsafe action attempts;
- stale or missing data cases.

### 10. Metrics track outcomes, not only activity

Activity metrics are not enough.

Prefer:

- resolved cases;
- completed workflows;
- repeat-contact rate;
- escalation rate;
- correction rate;
- incident rate;
- time saved after review.

### 11. Incident and rollback process exists

Before shipping, define what happens when the agent is wrong.

Include:

- how to disable the workflow;
- who reviews the incident;
- how to notify affected users;
- how to correct records or messages;
- how to update the evaluation set afterward.

### 12. Compliance evidence can be exported

For regulated or customer-facing workflows, make evidence exportable.

Useful evidence:

- workflow policy;
- data source list;
- permission matrix;
- approval rules;
- eval results;
- incident log;
- retention policy;
- model/provider notes.

## Practical readiness levels

### Level 0 — Demo

- Works once.
- No owner.
- No explicit permissions.
- No logs beyond chat history.

### Level 1 — Controlled pilot

- Named owner.
- Limited users.
- Read-only or draft-first actions.
- Basic logs and manual review.

### Level 2 — Production-like workflow

- Explicit data boundaries.
- Tool allowlists.
- Human approval for high-risk actions.
- Evaluation set.
- Incident process.

### Level 3 — Governed production

- Audit trail.
- Compliance evidence.
- Regular reviews.
- Monitored cost/rate limits.
- Documented rollback path.
- Measured business outcomes.

## Safe default policy

If in doubt:

```text
read: allowed with scoped sources
draft: allowed
send externally: approval required
modify records: approval required
delete: blocked by default
payments/refunds: separate policy required
production config: separate policy required
```

## Maintainer note

Most failed agent deployments do not fail because the model cannot answer. They fail because nobody defined ownership, boundaries, approvals, logging, evaluation, and rollback.

Production readiness is the layer that turns an agent from a demo into infrastructure.
