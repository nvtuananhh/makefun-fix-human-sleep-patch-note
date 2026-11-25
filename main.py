#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note entry.

Writes one patch note announcing that the human's sleep has been
fixed: the human now powers down at night like a proper machine.
Writes to /output/entry.txt and prints it.
"""

import os

LINE = "Patch 2.1 \u2014 Human sleep: fixed. The human now powers down at 11pm instead of doomscrolling until 3am. Side effect: dreams now run in 4K."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
