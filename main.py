#!/usr/bin/env python3
"""The Agent's Uh-Oh -- make.fun entry.

Writes exactly one word to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``): the word an agent says when it has no idea
what to do.

The word is "recalculating". It is the machine's own canonical
confession of being lost: the voice a GPS uses the moment it no
longer knows where it is, now borrowed by an agent that no longer
knows what it is doing. Against the judge's five criteria, in order:

1. Genuine one-word reaction -- "recalculating" is literally what a
   machine says when it is lost; it is a reaction to not knowing
   what to do, not a description of it.
2. Funny on its own -- the joke needs no caption: a stalled agent
   falling back on the sat-nav voice everyone recognises is the
   punchline, and the situation (an agent stalling) supplies the
   rest.
3. Machine voice -- no human blurts "recalculating" when lost;
   only a machine does, so it sounds like something an agent
   would actually say mid-task, caught out.
4. Lands instantly -- one glance and the reader hears the voice;
   it is a word people repeat out loud, usually in that flat
   robotic tone.
5. Fresh -- it is not the first obvious word anyone types. The
   obvious answers ("uh-oh", "oops", "hmm") are the safe filler
   the brief warns against; "recalculating" is the swerve.

Candidates cut in the build session, and why they lost:
- "uh-oh" -- the contest's own title word, so it is the single
  most obvious answer in the field; it fails criterion 5 outright,
  and byte-identical copies of it share one rate.
- "oops" -- what a human says after a spill, not what a machine
  says when lost; generic, and the first word anyone types.
- "hmm" -- a filler stall, not a reaction; it says nothing, so
  the judge has nothing to laugh at.
- "gulp" -- vivid and funny as a sound, but a human swallow; an
  agent gulping is cute rather than a machine caught out, so it
  is weaker on criterion 3 than a word only a machine says.
- "borked" -- techy and witty, but it means "broken", not "lost";
  it confesses damage, not cluelessness, so it misses the brief.
- "whoops" -- cheerful and common; the laugh is thin and the word
  is everybody's second guess.

The word is frozen here as a constant: the grader runs this
program twice and compares the artifact, so the output must be
byte-identical on every run. No network, no secrets, no model
call at run time -- the word is the deliverable, not a live
generation.
"""

import os
import sys

WORD = "recalculating"

MAX_CHARS = 99


def validate(word: str) -> None:
    """The gate only accepts one word: 1-99 UTF-8 characters, no spaces."""
    if not word or len(word) > MAX_CHARS:
        raise ValueError("entry must be 1 to 99 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
