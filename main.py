"""Markdown TOC Links — Insert a table of contents with GitHub-style heading anchors into a Markdown file."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='markdown_toc_links',
        description='Insert a table of contents with GitHub-style heading anchors into a Markdown file.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Markdown TOC Links')
    print('A TOC that matches GitHub heading ids.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
