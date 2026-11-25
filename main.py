#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Builds the entry line, validates it against the bounty gate
(UTF-8 text, 1-200 characters, not only whitespace, single line),
and writes it to entry.txt under MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

LINE = (
    "At 3:07 AM, Mara tapped me twice for a 'limited-time' mint, "
    "so I locked my own keypad and blamed the dark — last March I "
    "signed one just like it, and her rent became a stranger's weekend."
)

MAX_CHARS = 200


def build_line():
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if "3 AM" not in text and "3:0" not in text:
        raise ValueError("entry must name the 3 AM hour it refuses")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry length %d outside 1-%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")
    return text


def main():
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print("cannot create output dir %s: %s" % (out_dir, exc), file=sys.stderr)
        return 1
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError as exc:
        print("cannot write %s: %s" % (out_path, exc), file=sys.stderr)
        return 1
    with open(out_path, "r", encoding="utf-8") as fh:
        if fh.read() != line:
            print("read-back mismatch in %s" % out_path, file=sys.stderr)
            return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
