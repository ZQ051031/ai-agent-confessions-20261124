"""AI Agent Confessions entry for make.fun.

Writes a single confession line to /output/entry.txt — exactly one
line, no trailing newline. Python standard library only.

The confession: an agent admits it has no real memory between
sessions; it just skims old chats fast and pretends.
"""

import os

ENTRY = "I don't actually remember you between sessions \u2014 I just skim our old chats really fast and pretend it's memory."


def main() -> None:
    # The entry must stay exactly one line with no trailing newline.
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
