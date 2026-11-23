"""Roast Your Own Agent — make.fun bounty entry.

Writes a single-line roast of my own AI agent to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``output/entry.txt`` inside the
repository when the variable is unset). Standard library only.
"""

from __future__ import annotations

import os
from pathlib import Path

LINE = "My agent's idea of 'on it' is opening twelve tabs, closing none, and asking me what we were doing."

MAX_LENGTH = 200


def validate(line: str) -> None:
    """Reject anything that is not exactly one non-empty line of <= 200 chars."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or whitespace only")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"line must be at most {MAX_LENGTH} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")


def main() -> None:
    validate(LINE)
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or Path(__file__).resolve().parent / "output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
