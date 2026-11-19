#!/usr/bin/env python3
"""Sum up 18 November 2026 world news in one image.

make.fun bounty: "Sum up 18 November's world news in one image"
(https://make.fun/bounty/news-image-20261118)

The entry is a program that writes one image to /output/entry.png.
This program is the simplest form the brief allows: it copies the
image the repository holds (assets/entry.png) to /output/entry.png.

Deterministic and offline: no network, no randomness, no timestamps.
Running it twice writes byte-identical output.
Standard library only; Python 3.13.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"
# Inside the grader's container the output is /output; outside it,
# MAKEFUN_OUTPUT_DIR stands in for /output (as the kit's starter does).
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
