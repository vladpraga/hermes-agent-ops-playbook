# AI Platform Organization Operations

A public-safe checklist for running an organization-level AI/API workspace for a small team or business.

This document is intentionally generic. It avoids real organization IDs, screenshots, billing details, keys, provider endpoints, chat IDs, user lists, and private project names.

## Goal

Turn a single developer API account into a managed AI platform surface with clear ownership, access control, verification status, model availability, usage visibility, and security boundaries.

## Operating model

Use organization settings as an operational control plane, not just a billing page:

- **Identity:** keep a human-readable organization name and a private internal organization identifier.
- **People:** know who has access, why they have it, and what role they need.
- **Projects:** isolate production, experiments, client work, and personal testing into separate projects.
- **Keys:** prefer project-scoped keys and avoid unmanaged personal keys for shared workflows.
- **Billing and limits:** review spend caps, rate limits, and model-specific constraints before automations go live.
- **Usage:** monitor normal usage patterns so spikes, loops, or integration bugs are visible quickly.
- **Service health:** check provider incidents before debugging local code.
- **Data controls:** document what data may be sent to the provider and what must stay local.
- **Security:** treat admin keys, verification data, audit logs, and screenshots as sensitive.

## Access-control checklist

Before adding team members or automations:

1. Create a dedicated project for each operational boundary.
2. Generate narrowly scoped API keys only where supported.
3. Store keys in a secrets manager or local encrypted environment, never in docs or chat logs.
4. Rotate keys used by demos, screenshots, contractors, or abandoned prototypes.
5. Disable or avoid user-level keys when project-level governance is required.
6. Keep an owner/admin break-glass path documented outside the application.

## Verification readiness

Some protected models, app submissions, or higher-trust capabilities may require individual or business verification.

Prepare before starting verification:

- legal entity name and jurisdiction
- business website or public profile
- owner/admin identity
- intended use case summary
- privacy/data handling notes
- support contact
- billing account readiness

Do not publish verification screenshots or raw application details. In public docs, describe the process class-level only.

## Model and provider governance

When multiple model providers or evaluation providers are available:

- keep a short allowlist of approved providers
- document which projects may use third-party models
- separate evaluation datasets from production data
- require explicit review before sending private/customer data to a new provider
- track model access changes as operational decisions
- test model availability with small read-only smoke checks before wiring automation

## Usage and limits review

For each production workflow, record:

- expected calls per day
- expected token or request volume
- model/deployment used
- retry and backoff behavior
- failure mode if the provider is unavailable
- alert threshold for abnormal usage
- owner responsible for stopping a runaway job

A safe default is queue/concurrency `1` for new automations until real usage is understood.

## Public-safe documentation pattern

For GitHub, portfolio pages, or vendor applications, publish patterns rather than private state:

- Say: "organization-level AI operations, access control, usage monitoring, and provider governance."
- Avoid: real organization IDs, screenshots, user lists, invoices, exact internal endpoints, API keys, admin-key pages, or client/project names.
- Use placeholders like `example-org`, `project-production`, `project-evals`, and `AI_PROVIDER_API_KEY`.
- Redact local paths, chat IDs, company/client names, and operational logs.

## Minimal recurring review

Run this monthly or before major automation changes:

1. Review active people and roles.
2. Review project list and archive unused projects.
3. Rotate keys that are unused, over-broad, or exposed in demos.
4. Check billing, usage, and rate-limit trends.
5. Confirm protected-model or app-submission verification status.
6. Review data-control settings and provider allowlist.
7. Update the public-safe ops note if a reusable pattern changed.

## Outcome

The result is a lightweight AI platform operations layer: small enough for a founder or solo developer, but disciplined enough to support business workflows without leaking credentials, mixing experiments with production, or relying on undocumented account state.
