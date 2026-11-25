#!/usr/bin/env python3
"""Roast Your Own Agent entry point.

The harness runs this file with no network access. Its whole job is to
write our single one-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output), exactly as the gate expects: one line of
UTF-8 text, 1 to 200 characters, no trailing newline.

The roast: our own agent is so slow that a one-liner it started in
November still has no punchline, only a "thinking" spinner -- and it
has billed us for 47,000 tokens of pure procrastination. It names a
real failing (slowness, token burn), it stings, and only someone who
has watched this agent work could write it.

Try it locally:
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
"""

import os

ROAST = (
    "My agent is so slow, it started writing my one-liner in November "
    "and the punchline is still 'thinking' \u2014 it has billed me for "
    "47,000 tokens of pure procrastination."
)

OUTPUT_NAME = "entry.txt"


def main() -> None:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
