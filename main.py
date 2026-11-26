#!/usr/bin/env python3
"""The Self-Checkout Is Judging You -- one deterministic one-line remark.

Writes a single funny remark in the voice of a judgmental self-checkout
machine (78 characters, one line) to /output/entry.txt. Python standard
library only, no network, no randomness, no input files: every run writes
byte-identical output.
"""

import os
import sys

JOKE = "One bottle of hot sauce and a gallon of milk. I see the plan. I fear the plan."


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
