# Local-first personal AI agent OS architecture

This is a sanitized reference architecture for a practical personal AI-agent setup.

## Components

```text
Telegram / chat UI
        |
        v
Hermes-style gateway
        |
        +--> Agent runtime with tools, skills, memory, and approvals
        |
        +--> Cron scheduler for recurring jobs
        |
        +--> API server for programmatic runs
        |
        +--> Local filesystem / Obsidian vault / reports
        |
        +--> Logs, watchdogs, and operational state
```

## Design goals

- Use chat for fast instructions and approvals.
- Keep durable knowledge in Markdown files, not only in chat history.
- Use scheduled jobs for repeated work.
- Use deterministic no-agent scripts for health checks.
- Keep sensitive data local unless explicitly approved.
- Make every automation observable and recoverable.

## Typical workflow

1. User sends a task through Telegram.
2. Gateway routes the task to the agent.
3. Agent reads local context, uses tools, and produces an answer or artifact.
4. Important research is saved as Markdown and optionally rendered as HTML.
5. Cron jobs run recurring digests or health checks.
6. Watchdogs alert only when a concrete action is needed.

## Safety boundaries

- Secrets stay in environment files or credential stores, never in examples.
- Public docs use placeholders for people, companies, paths, and chat IDs.
- Destructive actions require explicit confirmation.
- Scheduled watchdogs should be read-only by default.
