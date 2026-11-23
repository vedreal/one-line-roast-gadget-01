"""One-Line Roast entry: write a single roast line to /output/entry.txt.

The line is hardcoded and deterministic, so the program always writes
exactly the same text. It roasts a gadget people use every day.
"""

import os

# The roast line: a smartwatch that congratulates its owner for standing.
LINE = "My smartwatch congratulates me for standing up, as if sitting was the hardest part of my day."


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Write exactly the line, with no trailing newline, so the file holds
    # one line of 1-200 UTF-8 characters and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
