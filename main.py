#!/usr/bin/env python3
"""One Line, Big Laugh — entry program (program/v1).

Writes a single self-contained funny line to /output/entry.txt.
Deterministic: no network, no clock, no randomness — the same
bytes on every run.
"""

import os
import sys

LINE = "The auctioneer could sell anything to anyone \u2014 he once convinced a man to buy back his own furniture."


def main() -> int:
    # Gate: the entry must be 1-200 UTF-8 characters, not whitespace only.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry out of bounds"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
