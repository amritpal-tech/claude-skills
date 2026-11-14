#!/usr/bin/env python3
"""
Turn a daily brief into delivery-ready markdown: drop the <!-- post/comment --> gate
markers, keep a blank line where each marker stood, collapse runs of blank lines.

Usage:
    python3 to_doc.py devcommx/linkedin-daily/2026-11-04.md > /path/to/out.md
"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
text = re.sub(r"^[ \t]*<!--.*?-->[ \t]*$", "", text, flags=re.M)
text = re.sub(r"\n{3,}", "\n\n", text)
sys.stdout.write(text.strip() + "\n")
