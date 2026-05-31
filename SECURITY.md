# Security Policy

This project documents local automation patterns for AI agents. Some examples may interact with files, logs, cron jobs, messaging gateways, or local services.

## Reporting a vulnerability

Please open a GitHub issue with a minimal description that does not include secrets, tokens, private logs, private chat IDs, or credentials.

## Safety expectations

Examples should:

- avoid printing secrets;
- avoid destructive file operations by default;
- keep healthy watchdog runs silent;
- document rollback and verification steps;
- prefer localhost bindings for local services;
- avoid uploading private local data to third-party services without explicit approval.
