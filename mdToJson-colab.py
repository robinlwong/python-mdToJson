import json
import re

def mdtojson_colab(md_filepath, ipynb_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cells = []
    current_cell_content = []

    def save_current_cell():
        """Helper to append the current content as a Markdown cell."""
        # Only save if there's actual content (ignores empty files or leading whitespace)
        if ''.join(current_cell_content).strip():
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                # Jupyter expects an array of strings for the source
                "source": current_cell_content.copy() 
            })

    for line in lines:
        # Check if the line is an H1 (#) or H2 (##)
        if re.match(r'^(#{1,2})\s+(.*)', line):
            # Save the previous cell before starting a new one
            save_current_cell()
            # Start the new cell with the header
            current_cell_content = [line]
        else:
            # Continue adding standard text to the current cell
            current_cell_content.append(line)

    # Don't forget to save the very last chunk of text!
    save_current_cell()

    # The standard Jupyter Notebook JSON wrapper
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

    # Dump the fully formatted notebook file
    with open(ipynb_filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=4)

    print(f"Success! Notebook generated at: {ipynb_filepath}")

# Execution
# Replace 'input.md' and 'output.ipynb' with your actual file paths
mdtojson_colab('input.md', 'output.ipynb')
