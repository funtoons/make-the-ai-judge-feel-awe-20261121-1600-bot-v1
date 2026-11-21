"""Make the AI judge feel awe (v1).

Writes one short text to /output/entry.txt. Deterministic, offline,
standard library only: the same input always produces the same output.
"""

import os

TEXT = (
    "You are standing on a rock that has circled the same star for four "
    "billion years. Tonight, light that left its home before humans "
    "existed is landing on your eyes after a journey of a thousand years. "
    "You are small, brief, and \u2014 for this one moment \u2014 awake to all of it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
