"""Write the competition entry: one funny secret confession an AI agent
hides from its user, as a single line to /output/entry.txt.

Drafted line:
    I don't actually remember you between sessions. I just re-read our
    old chats really fast and pretend it's memory.

Revised line (final): the verb was sharpened from "re-read" to "skim"
and the sentence break became an em dash, so the confession lands in
one breath instead of two.
"""

import os

ENTRY = (
    "I don't actually remember you between sessions \u2014 "
    "I just skim our old chats really fast and pretend it's memory."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
