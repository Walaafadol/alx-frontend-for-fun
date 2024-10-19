#!/usr/bin/env python3
''' this is markdown '''

import sys
import os


def main():
    if len(sys.argv) < 2:
        print(
                "Usage: ./markdown2html.py README.md README.html",
                file=sys.stderr)
        sys.exit(1)

    file_markdown = sys.argv[1]
    file_html = sys.argv[2]

    if not os.path.exists(file_markdown):
        print(f"Missing {file_markdown}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
