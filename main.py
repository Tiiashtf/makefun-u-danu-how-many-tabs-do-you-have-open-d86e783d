#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

The honest count is 1: exactly one browser tab was open in the browser
session used for this build at the moment of sending -- the GitHub
repository page for this very entry. The program writes exactly that
one digit to /output/entry.txt, nothing else.
"""

import os
import shutil

TAB_COUNT = "1"
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Never remove the output directory itself: only clear its contents,
    # so the program also works when /output is root-owned inside a
    # sticky parent directory.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(TAB_COUNT)


if __name__ == "__main__":
    main()
