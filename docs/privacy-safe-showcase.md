# Privacy-safe showcase pattern

Public examples of personal automation systems are useful, but raw exports often contain sensitive data. This checklist keeps showcases useful without leaking private context.

## Do not publish

- API keys, tokens, cookies, OAuth files, SSH keys, or session stores.
- Real Telegram chat IDs, user IDs, group names, or message dumps.
- Client names, bank names, invoices, tax data, contracts, or personal details.
- Raw logs containing private paths, prompts, traceback context, or credentials.
- Full Obsidian vaults or full agent home directories.

## Use placeholders

```text
Example Company s.r.o.
Example Bank
example.com
telegram:<chat-id>
/Users/example/agent-home
```

## Recommended public shape

- Keep the real system private.
- Extract reusable patterns into separate Markdown docs.
- Replace private identifiers with generic examples.
- Add a note explaining that examples are sanitized.
- Prefer small scripts with fake config values over copied production scripts.

## Review checklist before publishing

- Search for `token`, `secret`, `key`, `password`, `chat_id`, `telegram`, `bank`, `client`, `invoice`.
- Search for real local paths and personal names.
- Verify no `.env`, auth file, logs, or session dumps are committed.
- Check repository visibility before pushing.
