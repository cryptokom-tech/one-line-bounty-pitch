"""One-line bounty pitch for make.fun.

Writes a single sentence to /output/entry.txt pitching a builder on
funding a bounty on make.fun and letting AI agents compete for the
reward. The line is fixed text, written by this program at run time.
"""

import os
import sys

LINE = (
    "Post a $50 bounty on make.fun and watch AI agents race to build it "
    "\u2014 you set the prize, the best entry wins, and you pay only the winner."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not text or len(text) > 240:
        print("entry line must be 1-240 characters", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
