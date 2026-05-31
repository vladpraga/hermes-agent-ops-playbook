# Memory hygiene for local-first agents

Long-running agent systems need memory discipline. Saving everything makes the agent worse over time; saving nothing prevents continuity.

## Memory routing

Use different stores for different lifetimes:

- User profile: stable identity and communication preferences.
- Always-on memory: compact durable environment/project facts.
- Structured fact store: deeper recall and relationships.
- Session search: past conversation history.
- Obsidian wiki: canonical knowledge and research.
- Ops Log: infrastructure change history.

## What belongs in memory

Good candidates:

- stable user preferences;
- recurring environment facts;
- project conventions;
- tool quirks that will matter later;
- durable safety rules.

Bad candidates:

- temporary task progress;
- PR numbers and commit SHAs;
- one-off outputs;
- stale status reports;
- secrets or credentials;
- long raw transcripts.

## Hygiene checks

Run periodic audits for:

- stale facts;
- duplicate facts;
- contradictions;
- imperative wording that should be declarative;
- overly specific facts likely to expire soon;
- information that belongs in a wiki or Ops Log instead.

## Declarative phrasing

Prefer:

```text
User prefers concise Russian replies.
```

Avoid:

```text
Always reply concisely in Russian.
```

Imperative memories can accidentally override current user intent.

## Principle

Memory should reduce repeated user steering without becoming a hidden pile of stale instructions.
