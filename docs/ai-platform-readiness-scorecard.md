# AI Platform Readiness Scorecard

A lightweight scorecard for checking whether an AI/API organization workspace is ready for production automation.

Use this before connecting scheduled jobs, customer-facing workflows, evaluation pipelines, or high-volume agent systems to an AI provider account.

This template is public-safe. Replace placeholders with private details only in an internal copy.

## Scoring

For each area, mark one status:

- `0 - missing`: not defined or not reviewed
- `1 - partial`: exists, but has gaps or unclear ownership
- `2 - ready`: documented, verified, and owned

Suggested threshold:

- **0-7:** not ready for production automation
- **8-13:** limited pilot only
- **14-18:** production-ready with normal monitoring

## 1. Ownership and organization identity

Score: `0 / 1 / 2`

Ready means:

- organization owner/admin is known
- billing owner is known
- technical owner is known
- organization/project names are human-readable
- internal organization identifiers are kept private

Evidence to keep privately:

- owner/admin list
- billing contact
- internal escalation path

## 2. People and role access

Score: `0 / 1 / 2`

Ready means:

- every user has a clear reason for access
- admin access is limited
- inactive users are removed
- contractor or temporary access has an expiry path
- emergency access is documented

Review questions:

- Who can create keys?
- Who can change billing or limits?
- Who can access verification, admin keys, or security pages?

## 3. Project and environment isolation

Score: `0 / 1 / 2`

Ready means:

- production, experiments, evaluations, and demos are separated
- each automation maps to one project or environment
- project names do not expose private client details in public screenshots
- abandoned projects are archived or disabled

Example public-safe project names:

- `project-production`
- `project-evals`
- `project-sandbox`
- `project-demo`

## 4. API key governance

Score: `0 / 1 / 2`

Ready means:

- project-scoped keys are preferred where supported
- user-level keys are avoided for shared automation
- keys are stored outside repositories and chat logs
- key rotation is documented
- leaked, demo, or unused keys are revoked quickly

Minimum private inventory:

- key purpose
- project/environment
- owner
- creation date
- rotation date
- revocation criteria

## 5. Data controls and provider policy

Score: `0 / 1 / 2`

Ready means:

- allowed data classes are documented
- prohibited data classes are documented
- third-party provider usage requires explicit review
- evaluation datasets are separated from production/customer data
- logs and prompts are treated as sensitive artifacts

Public-safe statement:

> The system uses a provider allowlist and keeps private data, credentials, and operational logs out of public examples.

## 6. Models, providers, and verification readiness

Score: `0 / 1 / 2`

Ready means:

- approved models/providers are listed internally
- protected-model verification status is known
- individual/business verification requirements are understood
- new providers are tested with read-only smoke checks before production use
- eval providers and production providers are not confused

Review questions:

- Which models are approved for production?
- Which models are allowed only for experiments?
- Which workflows may use third-party providers?

## 7. Billing, limits, retries, and failure modes

Score: `0 / 1 / 2`

Ready means:

- expected daily usage is known for each automation
- rate limits and spend limits are reviewed
- retry behavior honors `Retry-After` and uses backoff
- new automations start with conservative concurrency
- runaway jobs have an owner and stop procedure

Safe default for new workflows:

```text
concurrency: 1
retry: exponential backoff
on_429: honor Retry-After
on_provider_outage: pause queue and alert owner
```

## 8. Monitoring and incident response

Score: `0 / 1 / 2`

Ready means:

- normal usage patterns are known
- abnormal usage thresholds are defined
- service health is checked before local debugging
- incidents produce a short ops note
- rollback or disable steps are documented

Minimum incident note:

```md
# AI Platform Incident Note

Date:
Owner:
Workflow:
Impact:
Provider status checked:
Root cause:
Action taken:
Follow-up:
```

## 9. Public-safe documentation

Score: `0 / 1 / 2`

Ready means:

- public docs use placeholders
- screenshots are avoided or redacted
- organization IDs, keys, user lists, billing data, and endpoints are not published
- repository checks search for obvious private identifiers
- private operational history stays in private systems

Before publishing, scan for:

```text
org-
sk-
secret
token
chat_id
/Users/
invoice
client
admin key
```

## Summary

```md
# AI Platform Readiness Summary

Date:
Reviewer:
Scope:

1. Ownership and identity: 0 / 1 / 2
2. People and roles: 0 / 1 / 2
3. Project isolation: 0 / 1 / 2
4. API key governance: 0 / 1 / 2
5. Data controls: 0 / 1 / 2
6. Models/providers/verification: 0 / 1 / 2
7. Billing/limits/retries: 0 / 1 / 2
8. Monitoring/incident response: 0 / 1 / 2
9. Public-safe documentation: 0 / 1 / 2

Total:
Decision: not ready / pilot only / production-ready
Top risks:
Next actions:
```
