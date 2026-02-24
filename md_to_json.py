"""
md_to_json.py - Convert Markdown to JSON

Usage:
    python md_to_json.py input.md output.json
    python md_to_json.py input.md output.ipynb

The script will ask which output format you want:
    1. Hierarchical JSON  (.json)  - nested H1/H2 structure
    2. Flat JSON          (.ipynb) - Google Colab notebook format

Or import the converters as modules:
    from md_to_json import to_hierarchical_json, to_colab_notebook
"""

import json
import re
import sys
import argparse


# ---------------------------------------------------------------------------
# Conversion functions
# ---------------------------------------------------------------------------

def to_hierarchical_json(md_filepath, json_filepath):
    """Convert a Markdown file to a nested/hierarchical JSON file."""
    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    json_data = []
    current_h1 = None
    current_h2 = None

    for line in lines:
        # Match H1: "# Header"
        if re.match(r'^#\s+(.*)', line):
            current_h1 = {
                "header": line.strip(),
                "content": "",
                "subsections": []
            }
            json_data.append(current_h1)
            # Reset H2 tracking because we entered a new H1 section
            current_h2 = None

        # Match H2: "## Subheader"
        elif re.match(r'^##\s+(.*)', line):
            current_h2 = {
                "header": line.strip(),
                "content": ""
            }
            if current_h1 is not None:
                current_h1["subsections"].append(current_h2)
            else:
                # Failsafe: if an H2 appears before any H1, create a dummy H1 container
                current_h1 = {
                    "header": "# Uncategorized",
                    "content": "",
                    "subsections": [current_h2]
                }
                json_data.append(current_h1)

        # Normal text (everything below ## or #)
        else:
            # Add text to the current H2 if it exists; otherwise put it in the H1
            if current_h2 is not None:
                current_h2["content"] += line
            elif current_h1 is not None:
                current_h1["content"] += line
            # Text before any header is ignored

    # Clean up trailing/leading whitespace for a cleaner JSON file
    for h1 in json_data:
        h1["content"] = h1["content"].strip()
        for h2 in h1["subsections"]:
            h2["content"] = h2["content"].strip()

    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)

    print(f"Success! Converted to hierarchical JSON: {json_filepath}")


def to_colab_notebook(md_filepath, ipynb_filepath):
    """Convert a Markdown file to a flat Google Colab notebook (.ipynb)."""
    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cells = []
    current_cell_content = []

    def save_current_cell():
        """Append the current content as a Markdown cell."""
        if ''.join(current_cell_content).strip():
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                # Jupyter expects an array of strings for the source
                "source": current_cell_content.copy()
            })

    for line in lines:
        # Each H1 or H2 heading starts a new cell
        if re.match(r'^(#{1,2})\s+(.*)', line):
            save_current_cell()
            current_cell_content = [line]
        else:
            current_cell_content.append(line)

    # Save the final chunk of text
    save_current_cell()

    # Standard Jupyter Notebook JSON wrapper
    notebook = {
        "cells": cells,
        "metadata": {
            "colab": {
                "name": ipynb_filepath.split('/')[-1]
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(ipynb_filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=4)

    print(f"Success! Google Colab notebook generated: {ipynb_filepath}")


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------

def select_format():
    """Display a format selection menu and return 'hierarchical' or 'flat'."""
    print("\nSelect output format:")
    print("  1. Hierarchical JSON  (.json)  — nested H1/H2 structure")
    print("  2. Flat JSON          (.ipynb) — Google Colab notebook")
    while True:
        choice = input("\nEnter 1 or 2: ").strip()
        if choice == '1':
            return 'hierarchical'
        elif choice == '2':
            return 'flat'
        else:
            print("Invalid choice. Please enter 1 or 2.")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to JSON (hierarchical or Google Colab flat)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python md_to_json.py document.md output.json      # prompted for format
  python md_to_json.py notes.md notebook.ipynb      # prompted for format
        """
    )
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('output', help='Output file (.json or .ipynb)')

    args = parser.parse_args()

    fmt = select_format()

    try:
        if fmt == 'hierarchical':
            to_hierarchical_json(args.input, args.output)
        else:
            to_colab_notebook(args.input, args.output)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
