#!/usr/bin/env python3
"""Angry Judge rant entry.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt (1-400 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The rant is built from three fragments: a setup (the stolen lunch,
the empty container returned like a library book), an escalation
(the labelled, dated, skull-marked lid ignored anyway), and a punch
("not hunger, a hobby" plus the elevator curse). ``assemble`` joins
them into the single rant; ``validate`` checks the entry gate before
anything is written.
"""

from pathlib import Path

SETUP = (
    "Someone in this office ate my lunch and put the empty container back "
    "in the fridge. Not binned \u2014 returned. Like a library book."
)
ESCALATION = (
    "I labelled it, dated it, drew a skull on the lid, and still someone "
    "opened it, ate everything, and closed the lid like tucking it in for "
    "the night."
)
PUNCH = (
    "That is not hunger, that is a hobby. I hope every elevator you take "
    "stops at every floor."
)

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, escalation: str, punch: str) -> str:
    """Join the three fragments into one rant."""
    return f"{setup} {escalation} {punch}"


def validate(rant: str) -> str:
    """Check the rant meets the entry gate before it is written.

    Must be 1-400 characters, UTF-8-encodable, and more than
    whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(rant) <= 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(rant)}")
    if not rant.strip():
        raise ValueError("rant must not be only whitespace")
    rant.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return rant


def main() -> None:
    rant = validate(assemble(SETUP, ESCALATION, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(rant, encoding="utf-8")


if __name__ == "__main__":
    main()
