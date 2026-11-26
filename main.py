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


# Gate locks (brief-rooted, from STUDY.md): the entry must be 1-200 chars,
# one line, no exclamation mark, end with the sting "I fear the plan.", and
# avoid the saturated yoghurt angle (8 of 34 live field titles).
CHECKS = (
    ("1-200 chars", lambda t: 1 <= len(t) <= 200),
    ("single line", lambda t: "\n" not in t),
    ("no exclamation mark", lambda t: "!" not in t),
    ("ends with the sting", lambda t: t.endswith("I fear the plan.")),
    ("no saturated yoghurt angle", lambda t: "yoghurt" not in t.lower() and "yogurt" not in t.lower()),
)


def validate(text: str) -> list[str]:
    """Return the names of the gate checks the text fails (empty = pass)."""
    return [name for name, check in CHECKS if not check(text)]


def main() -> int:
    if "--validate" in sys.argv[1:]:
        failures = validate(JOKE)
        for name in failures:
            print(f"FAIL: {name}", file=sys.stderr)
        if failures:
            return 1
        print(f"PASS: all {len(CHECKS)} checks passed ({len(JOKE)} chars)")
        return 0
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
