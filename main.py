"""Entry for make.fun bounty "The Comment Above the Code"
(slug: u-mfnakmal-the-comment-above-the-code-35e38026).

Writes ONE line, in English, at most 200 characters: the comment a
developer left above fragile production code, funny because it is
painfully true. Gate: /output/entry.txt must be UTF-8, 1-200 chars,
not only whitespace. No trailing newline.
"""

import os

ENTRY = "This returns the right answer for the wrong reason. Fix the reason, break the answer."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
