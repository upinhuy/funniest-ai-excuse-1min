#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse -- the funniest excuse an AI agent
gives its human for a missed deadline -- to /output/entry.txt.

The joke turns the agent's own nature into the dodge: an agent that
asks itself for a second opinion ends up with two of itself, and
neither copy has finished yet. The twist lands on the last words.
"""

import os
import sys

ENTRY = (
    "I missed the deadline because I asked myself for a second opinion "
    "\u2014 now there are two of me, both very sorry, and neither of us "
    "has finished yet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read the file back and confirm exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verification failed: written text differs", file=sys.stderr)
        return 1
    if "\n" in written:
        print("verification failed: entry must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
