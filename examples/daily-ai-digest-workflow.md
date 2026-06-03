# Example: scheduled AI digest workflow

A recurring digest should have a clear delivery contract.

## Contract

- Schedule: daily at a fixed local time.
- Sources: explicit list of feeds, websites, or APIs.
- Output: Markdown summary plus optional HTML/PDF artifact.
- Delivery: Telegram DM or configured home channel.
- Failure behavior: report only actionable failures.

## Recommended sections

1. Executive verdict.
2. Top 5 items.
3. Tools worth testing.
4. Market or ecosystem signal.
5. Recommended next action.
6. Source links.

## Reliability checks

- Artifact exists locally.
- Delivery path is allowed for media attachments.
- Gateway log does not show skipped media delivery.
- Duplicate reports use timestamped filenames.
