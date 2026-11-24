"""One-line excuse entry for make.fun's "Make the AI Judge Laugh: Developer Excuses" bounty.

The program writes exactly one line to entry.txt: the excuse

    It worked on my machine, so I promoted my machine to production.

Why this line: the judge's brief rewards a twist a developer recognises
that reveals what really happened. This one takes the most worn excuse in
software ("it worked on my machine") and turns it into a confession: the
fix was not to find the difference between dev and prod, but to erase it
by shipping my own machine as production. It lands fast, the jargon is
used right, and it sounds like something a developer would actually say
out loud while the incident channel watches.
"""

import os

# The excuse itself: one line, under 200 characters.
EXCUSE = "It worked on my machine, so I promoted my machine to production."


def check_gate(text):
    """The sealed scorer's gate: UTF-8 text of 1 to 200 characters,
    not only white space, on a single line, with no stray spaces
    at either end."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")


def main():
    check_gate(EXCUSE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    # The grader collects outputs as another user, so the file must
    # be readable by everyone, whatever the umask is.
    os.chmod(path, 0o644)
    # Read it back: a broken entry must fail loudly here, not sail
    # through to judging with the wrong contents.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    check_gate(written)
    if written != EXCUSE:
        raise ValueError("entry.txt does not hold the excuse")


if __name__ == "__main__":
    main()
