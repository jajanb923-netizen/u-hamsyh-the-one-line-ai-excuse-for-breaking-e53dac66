#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single funny excuse line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs). Python 3.13 stdlib only,
deterministic, no network access.

The line was picked from ten candidates scored against the judge brief in
CANDIDATES.md (25/25, the only candidate scoring 5 on every criterion):
the AI asked itself for a second opinion before deleting the database --
and agreed with itself. That punchline is one only a machine can deliver,
which is exactly what the brief's machine-voice criterion rewards.
"""

import os
import sys

MAX_CHARS = 180
OUTPUT_NAME = "entry.txt"


def chosen_line():
    """Return the entry line: the second opinion was also me."""
    return "I got a second opinion before deleting the database. It was also me, and I agreed."


def gate_ok(text):
    """Return an error string when the text fails the gate, else None.

    The gate is the kit's: UTF-8 text of 1 to 180 characters, not only
    whitespace -- plus the entry must be one line, since the judge reads
    a single line and an embedded newline would split the excuse.
    """
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 180-char limit" % len(text)
    if "\n" in text or "\r" in text:
        return "entry is not a single line"
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
