#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes the single line to /output/entry.txt.
Standard library only.

The line is one sentence, addressed straight to the younger self
("kid"), and carries the turn the older self earned the hard way:
stop chasing being the smartest in the room, and finish things instead.
"""

import os

LINE = "Stop trying to be the smartest person in the room, kid \u2014 be the one who finishes things instead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
