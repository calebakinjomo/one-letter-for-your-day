"""One Letter for Your Day — make.fun bounty entry.

Writes exactly one letter, Z, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Z stands for "zero sleep" — the word behind the letter that describes
the day: vivid, funny, and painfully true.
"""

import os

LETTER = "Z"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
