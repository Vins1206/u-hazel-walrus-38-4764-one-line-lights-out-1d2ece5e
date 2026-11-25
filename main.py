"""One Line, Lights Out -- make.fun entry.

Writes a single status update (under 200 characters) to /output/entry.txt.
Pure standard library, deterministic: every run writes byte-identical output.
"""

from pathlib import Path

ENTRY = "Status: idle. Lid closed. The cursor is still blinking where they stopped typing."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate is 1-200 characters; assert it here so a bad line can never ship.
    # No trailing newline is written: the file is exactly the line, which also
    # keeps the byte size minimal for the ranking tie-break (smaller text wins).
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
