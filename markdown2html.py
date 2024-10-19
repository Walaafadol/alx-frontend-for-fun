#!/usr/bin/python3

"""
Markdown script using python.
"""

import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as md_file:
        with open(output_file, 'w') as html_file:
            for line in md_file:
                line = line.rstrip()  # Remove trailing whitespace
                if line.startswith('#'):
                    heading_level = 0
                    while heading_level < 7 and line[heading_level] == '#':
                        heading_level += 1
                    heading_text = line[heading_level:].strip()
                    if heading_level > 0:
                        opening_tag = f'<h{heading_level}>'
                        closing_tag = f'</h{heading_level}>'
                        full_heading = opening_tag + heading_text + closing_tag
                        html_file.write(full_heading + '\n')
                else:
                    # Write any other lines as they are
                    html_file.write(f'<p>{line}</p>\n')


def main():
    if len(sys.argv) < 3:
        print(
                "Usage: ./markdown2html.py README.md README.html",
                file=sys.stderr)
        sys.exit(1)

    file_markdown = sys.argv[1]
    file_html = sys.argv[2]

    if not os.path.exists(file_markdown):
        print(f"Missing {file_markdown}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(file_markdown, file_html)

    sys.exit(0)


if __name__ == "__main__":
    main()
