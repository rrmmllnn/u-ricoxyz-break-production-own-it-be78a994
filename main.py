#!/usr/bin/env python3
"""One-line confession from an agent that just broke production.

The program emits a single sentence (136 characters) to
/output/entry.txt: the agent's own blunt admission, written moments
after the mistake, spelling out the command it ran, the environment
it ran it in, the time, and the damage -- a dead checkout and backups
several days stale -- and ending by taking the blame outright, with
no softening language anywhere.

Nothing here varies between runs: no clock, no randomness, no network,
only the standard library, so the file produced is identical every time.
"""

import os
import sys
from pathlib import Path

# The confession, kept as its two sentences so each can be read alone.
SENTENCES = (
    "I ran DROP TABLE users on production instead of staging at 4:58pm Friday.",
    "Checkout is dead, the backups are from Tuesday, and it was me.",
)

CHARACTER_LIMIT = 200
FORBIDDEN_LINE_BREAKS = ("\n", "\r")
FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def build_line() -> str:
    """Join the confession's sentences into the single line to emit."""
    return " ".join(SENTENCES)


def reject(message: str) -> "SystemExit":
    """Report a gate failure on stderr and stop with a nonzero status."""
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def check_line(line: str) -> None:
    """Refuse anything the scorer would mark invalid, before writing.

    The gate wants UTF-8 text of 1 to 200 characters, not only
    whitespace, on exactly one line.
    """
    if not line.strip():
        raise reject("entry is empty")
    if len(line) > CHARACTER_LIMIT:
        raise reject(
            f"entry is {len(line)} characters, over the "
            f"{CHARACTER_LIMIT} limit"
        )
    if any(ch in line for ch in FORBIDDEN_LINE_BREAKS):
        raise reject("entry must be a single line")


def destination() -> Path:
    """Where the line goes: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def run() -> None:
    line = build_line()
    check_line(line)
    target_dir = destination()
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / FILENAME).write_text(line, encoding="utf-8")


if __name__ == "__main__":
    run()
