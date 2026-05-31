# Telegram gateway diagnostics

Messaging gateways are the operational boundary between an AI agent and the user. A gateway can be healthy while a specific delivery path is broken, so diagnostics should separate runtime health from delivery health.

## First checks

Check the live service first:

```bash
hermes gateway status
hermes cron status
```

Separate the answers:

- Is the gateway process running?
- Is the scheduler running?
- Are jobs firing?
- Are messages being delivered?
- Are media attachments being delivered?

## Logs to inspect

Typical logs:

```text
~/.hermes/logs/gateway.log
~/.hermes/logs/gateway.error.log
~/.hermes/logs/errors.log
```

Search recent logs by timestamp, not just raw tail content.

Useful patterns:

- `Traceback`
- `failed to send`
- `NetworkError`
- `ConnectError`
- `Skipping unsafe MEDIA directive path outside allowed roots`
- `runtime lock`
- `pending_approval`

## Delivery checks

A cron job marked `ok` may still have partial delivery issues.

Verify:

1. The job produced the artifact.
2. The artifact path exists.
3. The path is inside allowed media roots.
4. The gateway did not log an unsafe media warning.
5. The message was delivered to the intended chat/thread.

## Network failures

Telegram network failures should not be confused with model failures. DNS/connectivity errors around `api.telegram.org` or fallback IPs usually indicate network path trouble, not an agent prompt problem.

## Safe reporting

A useful gateway report should include:

- process status;
- scheduler status;
- fresh log errors only;
- affected delivery paths;
- recommended action;
- what was intentionally not changed.
