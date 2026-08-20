#!/usr/bin/env python3
"""Assert handbook/INDEX.md links exactly the pages that exist.

The Assistant reads INDEX.md first and navigates from it, so a page missing
from the index is a page the agent will never open, and an index row pointing
at a deleted page is a citation it cannot honour. Both are silent failures at
runtime, which is why they are a loud one here.
"""
import pathlib
import re
import sys

HANDBOOK = pathlib.Path(__file__).resolve().parent.parent / "handbook"
INDEX = HANDBOOK / "INDEX.md"

on_disk = {p.name for p in HANDBOOK.glob("*.md")} - {"INDEX.md"}
linked = set(re.findall(r"\]\((\d[\w.-]+\.md)\)", INDEX.read_text()))

missing = sorted(on_disk - linked)
dangling = sorted(linked - on_disk)

for name in missing:
    print(f"error: handbook/{name} exists but INDEX.md does not link it", file=sys.stderr)
for name in dangling:
    print(f"error: INDEX.md links handbook/{name}, which does not exist", file=sys.stderr)

if missing or dangling:
    sys.exit(1)
print(f"INDEX.md links all {len(on_disk)} pages, and no others.")
