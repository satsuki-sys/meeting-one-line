#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one sentence to /output/entry.txt: the single line that could
have replaced an entire pointless meeting. Stdlib only, no network.
"""

import os

ENTRY = (
    "Nine people spent an hour discovering nobody had read the document, "
    "then booked a second meeting to read it out loud together."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
