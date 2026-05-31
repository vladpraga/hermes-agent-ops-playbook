#!/usr/bin/env python3
"""Example read-only cron doctor for local-first AI-agent systems.

No-agent semantics:
- healthy state prints nothing and exits 0;
- attention-needed state prints a compact report and exits 0;
- non-zero exit means the doctor itself is broken.

This is a generic sanitized example. Adapt paths and patterns for your setup.
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

HOME = Path(os.environ.get("AGENT_HOME", str(Path.home() / ".agent"))).expanduser()
LOG_DIR = HOME / "logs"
STATE_DIR = HOME / "state"
LAST_ALERT = STATE_DIR / "cron-doctor-last-alert.tsv"
LOOKBACK_HOURS = int(os.environ.get("CRON_DOCTOR_LOOKBACK_HOURS", "6"))
COOLDOWN_HOURS = int(os.environ.get("CRON_DOCTOR_COOLDOWN_HOURS", "6"))
NOW = datetime.now().astimezone()

PATTERNS = {
    "approval pending": r"pending_approval",
    "traceback": r"Traceback",
    "media delivery issue": r"Skipping unsafe MEDIA|MEDIA file not found|failed to send",
    "stale api call": r"Broken pipe|stale for \d+s",
}


def read_tail(path: Path, max_bytes: int = 250_000) -> str:
    if not path.exists():
        return ""
    with path.open("rb") as f:
        try:
            f.seek(-max_bytes, os.SEEK_END)
        except OSError:
            pass
        return f.read().decode("utf-8", errors="replace")


def parse_log_dt(line: str):
    match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(?:,\d+)?\b", line)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=NOW.tzinfo)
    except ValueError:
        return None


def recent_log_lines(text: str) -> list[str]:
    cutoff = NOW - timedelta(hours=LOOKBACK_HOURS)
    kept: list[str] = []
    keep_current_record = False
    for line in text.splitlines():
        dt = parse_log_dt(line)
        if dt is not None:
            keep_current_record = dt >= cutoff
        if keep_current_record:
            kept.append(line)
    return kept


def suppress_duplicate(report: str) -> bool:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    fingerprint = hashlib.sha256(report.encode()).hexdigest()
    if LAST_ALERT.exists():
        try:
            old_fp, old_ts = LAST_ALERT.read_text().split("\t", 1)
            old_dt = datetime.fromisoformat(old_ts.strip())
            if old_fp == fingerprint and NOW - old_dt < timedelta(hours=COOLDOWN_HOURS):
                return True
        except Exception:
            pass
    LAST_ALERT.write_text(f"{fingerprint}\t{NOW.isoformat()}\n")
    return False


def main() -> int:
    raw_logs = "\n".join(read_tail(LOG_DIR / name) for name in ["gateway.log", "errors.log"])
    logs = "\n".join(recent_log_lines(raw_logs))

    issues: list[str] = []
    for label, pattern in PATTERNS.items():
        count = len(re.findall(pattern, logs, flags=re.IGNORECASE))
        if count:
            issues.append(f"In the last {LOOKBACK_HOURS}h: {label}: {count} match(es).")

    if not issues:
        return 0

    report = "Cron Doctor\n\nStatus: attention needed\n\nIssues:\n" + "\n".join(f"- {x}" for x in issues)
    report += "\n\nRecommended action:\n- Inspect fresh logs around the affected timestamps."

    if not suppress_duplicate(report):
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
