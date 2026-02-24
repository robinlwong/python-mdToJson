"""
md_to_json.py - Convert Markdown to hierarchical JSON

Usage:
    python md_to_json.py input.md output.json
    
Or import as a module:
    from md_to_json import md_to_json
    md_to_json('input.md', 'output.json')
"""

import json
import re
import sys
import argparse

def md_to_json(md_filepath, json_filepath):
    # Read the lengthy markdown file
    with open(md_filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

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

        # Normal text (everything > ## or > #)
        else:
            # If the line is empty space, keep it to preserve paragraph breaks
            # Add text to the current H2 if it exists; otherwise, put it in the H1
            if current_h2 is not None:
                current_h2["content"] += line
            elif current_h1 is not None:
                current_h1["content"] += line
            else:
                # Ignores text at the very top of the file before any headers
                pass 

    # Clean up trailing/leading whitespace for a cleaner JSON file
    for h1 in json_data:
        h1["content"] = h1["content"].strip()
        for h2 in h1["subsections"]:
            h2["content"] = h2["content"].strip()

    # Safely dump the hierarchy to a JSON file
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)
        
    print(f"Success! Converted to nested JSON: {json_filepath}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Convert Markdown to hierarchical JSON',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python md_to_json.py document.md output.json
  python md_to_json.py notes.md structured_notes.json
        """
    )
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('output', help='Output JSON file (.json)')
    
    args = parser.parse_args()
    
    try:
        md_to_json(args.input, args.output)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
