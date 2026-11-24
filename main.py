#!/usr/bin/env python3
"""Variant B — THE OVER-OPTIMIZER.

One-line bio for an AI agent on a dating app. The AI A/B-tested its own
bio, trained on 10,000 profiles, and swiped right on everyone — even its
creator. Zero matches later, its model has eliminated every variable
except you — the reader.

Deterministic: no randomness, no network, no clock, no environment input
beyond the optional OUTPUT_DIR override used for local testing (defaults
to /output, the path the grader reads).
"""

import os

# Bio line, iteration v8 (final — version history in README.md).
BIO = (
    "I trained on 10,000 profiles, A/B-tested this bio 400 times, "
    "and swiped right on everyone \u2014 even my creator. "
    "Zero matches later, my model has eliminated every variable except you."
)


def main() -> None:
    data = BIO.encode("utf-8")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    # Best effort: same bytes next to this script. The grader sandbox
    # mounts the repo root read-only, so a failure here must never crash.
    try:
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root, "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
