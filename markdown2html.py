#!/usr/bin/python3
"""markdown2html: validate arguments and source file existence.

This script takes two arguments: the input Markdown filename and the output
HTML filename. It only validates the arguments and the input file presence,
printing the required error messages and exit codes.
"""

import os
import sys


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    infile = sys.argv[1]

    if not os.path.isfile(infile):
        print(f"Missing {infile}", file=sys.stderr)
        sys.exit(1)

    # Success: do nothing and exit 0
    sys.exit(0)
