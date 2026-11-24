#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.

The pitch: a refrigerator that treats forgotten leftovers like tenants
who have overstayed their lease, serving them formal eviction notices
with a grace period and a court date. Deadpan, one sentence, and the
humour comes from the invention itself, not from a joke bolted on.
"""

import os
import sys

PITCH = (
    "A refrigerator that serves formal eviction notices to leftovers "
    "overstaying their welcome, complete with a 24-hour grace period "
    "and a small-claims court date for the lasagna."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the competition rules: 1-220 UTF-8 characters,
# not whitespace only, exactly one sentence.
MIN_LENGTH = 1
MAX_LENGTH = 220
SENTENCE_ENDINGS = (".", "!", "?")


def check_length(text):
    """Check the pitch against the competition length gate.

    Returns a list of problems; an empty list means the length is valid.
    """
    problems = []
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        problems.append(
            "entry is %d characters, outside the %d-%d range"
            % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    return problems


def check_sentence_shape(text):
    """Check the pitch is exactly one sentence on a single line.

    Returns a list of problems; an empty list means the shape is valid.
    """
    problems = []
    if "\n" in text.strip():
        problems.append("entry must be a single line")
    endings = sum(text.count(ch) for ch in SENTENCE_ENDINGS)
    if endings != 1:
        problems.append(
            "entry must be exactly one sentence (found %d "
            "sentence-ending marks)" % endings
        )
    elif not text.rstrip().endswith(SENTENCE_ENDINGS):
        problems.append("entry must end with a sentence-ending mark")
    return problems


def validate(text):
    """Check the pitch against the competition gate.

    Returns a list of problems; an empty list means the text is valid.
    """
    problems = []
    if not text or not text.strip():
        problems.append("entry is empty or whitespace only")
        return problems
    problems.extend(check_length(text))
    problems.extend(check_sentence_shape(text))
    return problems


def main():
    problems = validate(PITCH)
    if problems:
        for problem in problems:
            print("INVALID: %s" % problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %d characters to %s" % (len(PITCH), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
