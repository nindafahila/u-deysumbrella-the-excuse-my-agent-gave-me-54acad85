#!/usr/bin/env python3
"""u-deysumbrella-the-excuse-my-agent-gave-me-54acad85 -- make.fun entry.

The entry is one line of text: the excuse an AI agent hands its human
for a missed deadline. This program writes that line, byte for byte,
to <output>/entry.txt, so every run produces the exact same file:
deterministic, no network, no randomness, no clock. Python 3.13,
standard library only.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry \u2014 I burned the whole deadline re-reading your brief, "
    "ran out of context, and hallucinated a calendar where it is still "
    "next Tuesday."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
