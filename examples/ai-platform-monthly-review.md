# Monthly AI Platform Review

Use this template for a recurring review of an AI/API organization workspace.

Keep the completed review private if it contains real users, projects, usage, billing, provider names, endpoints, tickets, logs, or incidents. Publish only sanitized patterns and lessons learned.

## Metadata

Date:
Reviewer:
Organization/workspace:
Review period:
Decision: `healthy / needs attention / freeze changes`

## 1. Access review

People reviewed: `yes / no`

Changes:

- Added:
- Removed:
- Role changes:
- Admin access exceptions:

Questions:

- Does every active user still need access?
- Are there temporary users or contractors to remove?
- Is admin access still limited to the right people?

## 2. Project and environment review

Projects reviewed: `yes / no`

Active projects:

- Production:
- Evaluations:
- Sandbox:
- Demos:

Actions:

- Archive unused projects:
- Rename unclear projects:
- Separate mixed-use projects:

## 3. API key review

Keys reviewed: `yes / no`

Actions:

- Rotate:
- Revoke:
- Move to project-scoped key:
- Move out of local files/chat/docs:

Questions:

- Are any keys unused?
- Are any keys too broad for their workflow?
- Were keys exposed in demos, screenshots, logs, or debugging sessions?

## 4. Usage, billing, and limits

Usage reviewed: `yes / no`

Summary:

- Expected usage:
- Actual usage:
- Anomalies:
- Limit changes:
- Spend/cost notes:

Questions:

- Did any job retry too aggressively?
- Did any workflow hit rate limits?
- Are new automations still running with conservative concurrency?

## 5. Model and provider governance

Provider/model allowlist reviewed: `yes / no`

Changes:

- Added:
- Removed:
- Pilot-only:
- Production-approved:

Questions:

- Are third-party providers allowed for this workflow?
- Are evaluation providers separated from production providers?
- Are protected-model requirements understood?

## 6. Verification and capability status

Verification status reviewed: `yes / no`

Status:

- Individual verification:
- Business verification:
- Protected-model access:
- App submission readiness:

Actions:

- Prepare documents:
- Update public business profile:
- Review data handling statement:

## 7. Data controls and security

Data-control settings reviewed: `yes / no`

Checks:

- Public docs use placeholders.
- Screenshots are redacted or avoided.
- Logs do not contain secrets or private identifiers.
- Evaluation datasets do not contain production/customer data unless explicitly approved.
- Provider policy changes were reviewed.

Risks found:

-

Actions:

-

## 8. Incidents and lessons learned

Incidents this period:

- Incident:
  - Impact:
  - Root cause:
  - Action taken:
  - Follow-up:

Reusable lessons:

-

Public-safe notes worth publishing:

-

## 9. Next actions

Top 3 actions:

1.
2.
3.

Owner:
Due date:
Next review date:

## Final decision

Decision: `healthy / needs attention / freeze changes`

Reason:

-
