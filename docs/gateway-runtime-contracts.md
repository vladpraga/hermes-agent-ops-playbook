# Gateway Runtime Contracts for Local-First AI Agents

Messaging gateways are not just chat adapters. In a local-first AI agent setup, the gateway is the runtime boundary where user context, routing, delivery, media, and safety decisions become real.

This note collects practical contracts for Hermes-style gateways and adjacent agent systems.

## Why this matters

Gateway bugs are often hard to diagnose because the prompt looks correct while the runtime state is wrong:

- a message goes to the wrong channel or session;
- a thread or room name is lost;
- a delivery failure is swallowed;
- Markdown renders badly in one platform;
- a native attachment is flattened into incomplete text;
- webhook and long-polling modes conflict;
- benign adapter acknowledgements create noisy warnings.

The fix is to treat gateway behavior as a set of explicit runtime contracts.

## Contract 1: log routing at dispatch time

Log route resolution not only when a message is received, but immediately before dispatch.

A useful dispatch log should include safe, structured fields such as:

```json
{
  "event": "gateway.dispatch.resolve",
  "platform": "telegram",
  "adapter": "telegram",
  "session_id": "session_abc123",
  "source": "telegram:project-space:example-thread",
  "target_kind": "thread",
  "target_id_hash": "sha256:...",
  "thread_name": "Example Project",
  "delivery_mode": "message",
  "fallback_used": false
}
```

Do not log raw tokens, full phone numbers, private chat IDs, or secrets. Hash or redact identifiers when needed.

## Contract 2: visible delivery failure

A send failure should not disappear into logs only.

The gateway should distinguish:

- user-visible delivery failure: the agent could not send the result;
- recoverable retry: the platform/API is temporarily unavailable;
- benign acknowledgement/no-op: expected adapter noise;
- fatal configuration problem: wrong target, missing permission, bad token.

For scheduled reports and cron jobs, save undelivered content as a forensic artifact and include its local path in diagnostics.

## Contract 3: transport modes are mutually exclusive

For Telegram-like platforms, webhook and long-polling are separate runtime modes.

If webhook mode is configured:

- do not continue long-polling with `getUpdates`;
- do not silently reset or delete the webhook;
- log the active transport mode during startup;
- fail fast if both modes are configured in a conflicting way.

This avoids the class of bugs where a polling loop erases webhook state.

## Contract 4: preserve channel context

The session source should contain human-readable context when available:

- room name;
- thread/topic title;
- channel name;
- project-space label;
- reply/forward context when safe.

Stable IDs are still needed for routing, but human-readable names help operators and agents understand where a request came from.

Example:

```text
matrix:room:agent-ops
telegram:Hermes Project Spaces:Gateway Runtime
slack:team-ops:#agent-infra
```

## Contract 5: normalize native metadata into structured context

Native platform objects should not be reduced to incomplete prose.

Examples:

- location pin → latitude, longitude, label, address, accuracy;
- image/file → filename, MIME type, size, caption, local cached path;
- contact card → display name, safe redacted fields;
- replied message → safe excerpt plus message/thread reference;
- forwarded message → provenance when available and safe.

If a platform adapter cannot access some metadata, make the limitation explicit in diagnostics.

## Contract 6: renderer contracts are platform-specific

Markdown is not a universal delivery format.

A gateway should define renderer behavior per channel:

- Telegram: Markdown subset, file/document delivery, media captions;
- Slack: blocks or plain text, depending on target;
- Feishu/Lark: native post/card format where possible;
- Discord: message length and embed constraints;
- email: HTML/plain multipart when appropriate.

Tables, long reports, code blocks, and media attachments need explicit formatting decisions rather than relying on fallback Markdown.

## Contract 7: suppress benign acknowledgement noise

Some platforms emit events that need acknowledgement but should not become warnings.

Use catch-all acknowledgement handlers for known benign cases, and keep counters for observability. Do not train operators to ignore warning logs by filling them with expected 404/no-op noise.

## Contract 8: provider/client config survives async wrappers

Gateway-driven multimodal tasks often pass through async wrappers. Provider-specific configuration must survive that path.

Regression tests should cover:

- custom vision client config;
- model/provider override preservation;
- credential pool context;
- no hidden fallback when a provider policy forbids it.

## Minimal gateway diagnostics checklist

When debugging a gateway incident:

1. Identify inbound platform, room/thread, and user-visible source.
2. Find the session id created or resumed for the message.
3. Inspect dispatch-time route resolution.
4. Check whether a fallback target was used.
5. Check delivery result and retry/error classification.
6. Verify renderer path and media/document handling.
7. Confirm transport mode: webhook or polling, not both.
8. If tools/MCP were involved, check whether tool schema loading degraded safely.

## Related patterns

- No-agent watchdogs should stay silent when healthy.
- Cron jobs should preserve failed delivery artifacts.
- MCP/tool onboarding should use quarantine profiles and smoke tests.
- Obsidian or Markdown research wikis are useful for preserving operational lessons without putting everything into always-on memory.
