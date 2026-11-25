"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to ``entry.txt`` in the
output directory (``MAKEFUN_OUTPUT_DIR``, default ``/output``).

The joke, written from scratch for this bounty:

    I told Dad I'm afraid of the dark. He said, 'Good — the dark's
    afraid of the electricity bill.'

Why this line: it is a dad joke in the classic dinner-table shape
(a kid's setup, Dad's deadpan retort), the punchline lands in the
last words with a double twist (the thing you fear is itself afraid
— of the electricity bill, the most dad of all fears), it uses no
well-worn punchline from the joke books (no anti-gravity book, no
seafood diet, no scarecrow award), and it is short enough to say out
loud in one breath. The output is byte-identical on every run.
"""

import os
import sys

JOKE = "I told Dad I'm afraid of the dark. He said, 'Good \u2014 the dark's afraid of the electricity bill.'"

# The gate the sealed scorer applies: UTF-8 text of 1 to 140 characters,
# not only white space, on a single line. Refuse to write anything
# that would fail it, instead of handing the judge an invalid entry.
MAX_CHARS = 140


def validate(text: str) -> None:
    if not text.strip():
        sys.exit("entry is blank")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    if len(text) > MAX_CHARS:
        sys.exit(f"entry is {len(text)} characters, over the {MAX_CHARS} cap")
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
