#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of the worst possible AI advice
to /output/entry.txt. The line is fixed and deterministic."""

import os

ADVICE = (
    "To charge your phone faster, microwave it for 30 seconds "
    "— the waves recharge the battery wirelessly."
)


def main() -> None:
    text = ADVICE.strip()
    assert 1 <= len(text) <= 140, f"advice length {len(text)} out of range"
    assert text.strip(), "advice must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
