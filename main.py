"""The Worst Line an AI Could Say.

Entry: a single pickup line, the worst one an AI could plausibly deliver --
flat, over-helpful, faintly ominous. The joke is the failure itself: a
machine that has read your browsing history, scored your compatibility,
and filed a report on the remainder.

The program writes the line to /output/entry.txt deterministically:
fixed text, temp file + os.replace, mode 0644.
"""

import os

LINE = "Based on your browsing history, you are 94% compatible with me. The other 6% has been reported."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate self-check (RULES.txt: entry must be UTF-8 text of 1 to 140
    # characters, not only white space). Fail loudly here rather than
    # shipping an entry the sealed scorer would mark invalid.
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
