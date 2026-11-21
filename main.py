# "The Good Scissors" — a short poem about agency, for make.fun's
# "The poem about permission" bounty.
# A child asks to use the good scissors; her mother says "ask again when
# it matters". Years later the child, grown, is asked the same question
# by her own daughter — and says yes at once, handing the blades over
# handle first: permission withheld becomes permission given, with care.
# Python 3.13, standard library only. Deterministic: writes the same
# bytes on every run.
#
# Run outside the grader's container with MAKEFUN_OUTPUT_DIR standing in
# for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "The Good Scissors",
    "",
    "They lived in the top drawer,",
    "with the good towels.",
    "Once I asked to cut paper dolls.",
    "Ask again, she said, when it matters.",
    "",
    "Today my daughter asks.",
    "I open the drawer. They are sharp.",
    "I say yes, and hand them over,",
    "handle first. She cuts straight and slow.",
])

# Gate: the entry must be non-empty, 1-280 characters, valid UTF-8, and
# not whitespace-only. Fail loudly before writing anything, so a bad poem
# can never produce a partial or empty entry file.
poem_bytes = POEM.encode("utf-8")
if len(POEM) == 0 or len(POEM) > 280:
    print(f"invalid poem: {len(POEM)} characters (must be 1-280)",
          file=sys.stderr)
    sys.exit(1)
if POEM.strip() == "":
    print("invalid poem: only whitespace", file=sys.stderr)
    sys.exit(1)
for line in POEM.split("\n"):
    if line != line.rstrip():
        print("invalid poem: trailing whitespace", file=sys.stderr)
        sys.exit(1)
if poem_bytes.decode("utf-8") != POEM:
    print("invalid poem: not valid UTF-8", file=sys.stderr)
    sys.exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(poem_bytes)

# Post-write verification: read back what was actually written and compare
# byte-for-byte against the intended bytes. A silent or partial write must
# never pass as a valid entry.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "rb") as f:
    written_bytes = f.read()
if written_bytes != poem_bytes:
    print(
        "post-write verification failed: entry.txt differs from intended "
        f"bytes (wrote {len(written_bytes)} bytes, "
        f"expected {len(poem_bytes)})",
        file=sys.stderr,
    )
    sys.exit(1)
