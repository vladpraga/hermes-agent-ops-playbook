# Example: Telegram-first agent workflow

This example shows the operating pattern without exposing a real bot, chat, or user ID.

## Flow

1. User sends a task in Telegram.
2. Gateway validates that the user or chat is allowed.
3. Agent receives the request with tool access.
4. If a risky action is needed, the gateway asks for approval.
5. Agent returns a concise answer or a file attachment.
6. Important operational changes are recorded in an Ops Log note.

## Example request

```text
Check whether the scheduled AI digest ran today. If the report file exists, summarize the result and verify delivery logs.
```

## Good response contract

- Verdict first.
- Mention exact artifact paths only if safe.
- Separate local generation from delivery success.
- Do not expose secrets or raw logs.

## Common failure modes

- Gateway is running but Telegram delivery failed.
- Cron marked a job as `ok`, but media attachment was skipped.
- Long web extraction caused an agent idle timeout.
- Restart interrupted an active session and triggered auto-resume.
