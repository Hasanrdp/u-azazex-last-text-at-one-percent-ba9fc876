#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message at one percent battery to
/output/entry.txt. The text is fixed and deterministic: every run writes
the exact same bytes. Pure Python 3 standard library, no network, no
secrets, no input files.
"""

import hashlib
import os

TEXT = "Final message: your 6am alarm is set. I won't be here to ring it. Sleep in. You've earned this betrayal."

# Pinned identity of the text, verified 2026-11-25: 104 chars, 104 bytes.
# A typo or stray edit can never silently change the judged line — the
# program refuses to ship anything but exactly these bytes.
EXPECTED_SHA256 = "d5d02ee806c3f39fb0f620e109d3f2c120edb8b8eac504fd1c68028b082c4607"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read-back gate: the bytes on disk must be exactly the pinned line.
    with open(path, "rb") as f:
        written = f.read()
    if written != TEXT.encode("utf-8"):
        raise SystemExit("entry.txt on disk does not match the text")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")
    return path


if __name__ == "__main__":
    print(main())
