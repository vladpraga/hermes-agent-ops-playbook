# No-agent watchdogs

A no-agent watchdog is a deterministic scheduled script that checks system health and prints a human-readable alert only when attention is needed.

For local-first AI agent systems, this is usually safer and cheaper than running a full LLM agent on every monitoring tick.

## Core pattern

- Put the script under a known local scripts directory.
- Schedule it as a no-agent cron job.
- Exit `0` both for healthy and attention-needed states.
- Healthy state prints **empty stdout**.
- Attention-needed state prints a compact report.
- Non-zero exit is reserved for broken watchdog infrastructure.

## Why this matters

Agent-based recurring jobs can fail for reasons unrelated to the thing being monitored: model rate limits, provider outages, approval prompts, context length, or tool-call loops.

For routine health checks, deterministic scripts are more reliable.

## Alert format

```text
System Watchdog

Status: attention needed

Issues:
- ...

Recommended action:
- ...
```

## De-duplication

Frequent watchdogs should avoid repeating the same alert every run.

Recommended approach:

1. Normalize issue text.
2. Hash the issue list and recommendations.
3. Store the last fingerprint and timestamp in a local state file.
4. Suppress identical alerts for a cooldown window, for example 6 hours.
5. Still alert immediately when the fingerprint changes.

## Log freshness

When scanning logs, do not count raw tail content as "fresh".

A robust log scanner should:

- parse timestamps from log records;
- only count records inside a lookback window;
- keep continuation lines only when attached to a fresh timestamped record;
- ignore stale traceback fragments;
- suppress known non-actionable historical noise.

## Verification

Before scheduling a watchdog:

```bash
python3 -m py_compile scripts/my-watchdog.py
scripts/my-watchdog.py | wc -c
```

A healthy no-agent watchdog should return `0` bytes of stdout.
