# Cron reliability for AI-agent systems

Scheduled AI-agent workflows are useful, but they need different reliability rules than ordinary chat sessions.

## Recommended defaults

- Use no-agent scripts for deterministic maintenance jobs.
- Keep routine checks silent when healthy.
- Keep concurrency low, often `1`, when using a single model/provider quota.
- Honor `Retry-After` and use backoff instead of provider hopping.
- Avoid commands that require interactive approval in unattended cron jobs.
- Make every generated artifact verifiable on disk before delivery.

## Agent cron vs no-agent cron

Use an agent cron job when the task genuinely requires reasoning:

- summarizing fresh research;
- ranking findings;
- drafting a report;
- comparing sources;
- making a judgment call.

Use a no-agent cron script when the task is deterministic:

- checking gateway status;
- checking disk usage;
- linting a wiki;
- verifying backups;
- scanning recent logs;
- probing an API health endpoint.

## Common failure modes

### Approval prompts

Unattended cron jobs should not run commands that trigger manual approval. Convert those workflows to deterministic scripts or reduce the tool scope.

### Stale log alerts

A cron doctor that scans log tails without timestamp filtering may report old errors forever. Always filter by time window.

### Provider credits and rate limits

Do not solve rate limits by silently switching providers. For local-first setups with one intended provider, prefer:

- queueing;
- concurrency `1`;
- retry-after aware sleeps;
- smaller prompts/output limits;
- no-agent scripts for routine work.

### Media delivery

A report job can succeed locally while the attachment silently fails if `MEDIA:` points outside allowed roots. Verify both:

- artifact exists locally;
- delivery path is allowed by the gateway.

## Completion checklist

For each scheduled job, document:

- schedule;
- delivery target;
- script or prompt path;
- expected healthy stdout behavior;
- state file path;
- verification command;
- rollback/pause command.
