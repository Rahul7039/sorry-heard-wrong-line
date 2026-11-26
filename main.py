"""One-line smart-speaker apology for make.fun's "Sorry, I Heard That Wrong".

Prints the line and writes the identical line to /output/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "Sorry, I heard 'turn the lights down low' as 'order 40 garden gnomes'. They're at the door. They saw everything."
MAX_CHARS = 140


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, "LINE must be 1-140 chars"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
