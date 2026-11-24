#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message at one percent battery to
/output/entry.txt. The text is fixed and deterministic: every run writes
the exact same bytes. Pure Python 3 standard library, no network, no
secrets, no input files.
"""

import os

TEXT = "Final message: your 6am alarm is set. I won't be here to ring it. Sleep in. You've earned this betrayal."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return path


if __name__ == "__main__":
    print(main())
