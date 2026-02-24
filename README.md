# md-to-json

**Convert Markdown files to structured JSON formats**

A lightweight Python utility for parsing Markdown documents into structured JSON. Supports two output formats:
1. **Hierarchical JSON** - Nested structure with H1/H2 headers
2. **Jupyter Notebook** - Google Colab-compatible `.ipynb` format

---

## 📋 Features

- **Hierarchical JSON Export** - Preserves document structure with nested sections
- **Jupyter Notebook Export** - Converts Markdown to Colab-ready notebooks
- **CLI Support** - Run directly from command line
- **Module Import** - Use as a library in your Python code
- **Whitespace Agnostic** - Handles varying formatting styles
- **Preserves Content** - Maintains paragraph breaks and formatting

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/robinlwong/md-to-json.git
cd md-to-json
```

No external dependencies required - uses Python standard library only.

---

### 1. Hierarchical JSON Export

**CLI Usage:**
```bash
python md_to_json.py input.md output.json
```

**Python Module:**
```python
from md_to_json import md_to_json

md_to_json('input.md', 'output.json')
```

**Output Structure:**
```json
[
    {
        "header": "# Main Topic",
        "content": "Introductory text for the main topic.",
        "subsections": [
            {
                "header": "## Subtopic A",
                "content": "Everything under Subtopic A."
            },
            {
                "header": "## Subtopic B",
                "content": "Everything under Subtopic B."
            }
        ]
    }
]
```

**Features:**
- H1 headers (`#`) create top-level sections
- H2 headers (`##`) create nested subsections
- Content is organized hierarchically
- Trailing/leading whitespace automatically cleaned

---

### 2. Jupyter Notebook Export

**CLI Usage:**
```bash
python md_to_json_colab.py input.md output.ipynb
```

**Python Module:**
```python
from md_to_json_colab import md_to_json_colab

md_to_json_colab('input.md', 'output.ipynb')
```

**Output:** 
- Creates a Jupyter Notebook (`.ipynb`) file
- Each H1/H2 header starts a new Markdown cell
- Colab automatically creates collapsible sections
- Ready to open directly in Google Colab

**Why This Matters:**
- Google Colab uses Jupyter's flat cell structure
- Automatically renders H1/H2 as collapsible sections
- Prevents browser performance issues with large documents
- Maintains document organization in Colab UI

---

## 📁 File Overview

| File | Purpose | CLI Usage | Module Import |
|------|---------|-----------|---------------|
| `md_to_json.py` | Hierarchical JSON converter | `python md_to_json.py input.md output.json` | `from md_to_json import md_to_json` |
| `md_to_json_colab.py` | Jupyter Notebook converter | `python md_to_json_colab.py input.md output.ipynb` | `from md_to_json_colab import md_to_json_colab` |
| `example.md` | Sample document for testing | - | - |

---

## 🔧 Requirements

**Python Version:** 3.6+

**Dependencies:** None (standard library only)

**Tested On:**
- Python 3.8
- Python 3.10
- Python 3.12

---

## 📖 Usage Examples

### Example 1: CLI - Convert Documentation

```bash
# Convert project docs to JSON
python md_to_json.py PROJECT_DOCS.md docs_structured.json

# Convert to Jupyter Notebook
python md_to_json_colab.py TUTORIAL.md tutorial.ipynb
```

### Example 2: Python Module - Batch Processing

```python
from md_to_json import md_to_json
import os

# Convert all .md files in a directory
for filename in os.listdir('docs/'):
    if filename.endswith('.md'):
        input_path = os.path.join('docs', filename)
        output_path = os.path.join('output', filename.replace('.md', '.json'))
        md_to_json(input_path, output_path)
        print(f"Converted: {filename}")
```

### Example 3: Integration with Data Pipeline

```python
from md_to_json import md_to_json
import json

# Convert markdown to JSON
md_to_json('research_notes.md', 'structured.json')

# Load and process the structured data
with open('structured.json', 'r') as f:
    data = json.load(f)
    
# Extract all H2 headers
h2_headers = []
for section in data:
    for subsection in section['subsections']:
        h2_headers.append(subsection['header'])

print(f"Found {len(h2_headers)} subsections")
```

### Example 4: Google Colab Workflow

```bash
# Convert notes to notebook
python md_to_json_colab.py research_notes.md research.ipynb

# Upload to Google Drive, then:
# 1. Right-click research.ipynb in Google Drive
# 2. Open with → Google Colab
# 3. All H1/H2 headers become collapsible sections
```

---

## ⚙️ How It Works

### Hierarchical JSON Converter

1. **Parses Markdown line-by-line**
2. **Identifies headers:**
   - `# Header` → H1 (top-level section)
   - `## Subheader` → H2 (nested subsection)
3. **Groups content:**
   - Text following H1 goes to `h1.content`
   - Text following H2 goes to `h2.content`
4. **Builds hierarchy:**
   - H2 sections nested under parent H1
   - Orphaned H2s get a default "Uncategorized" H1
5. **Cleans output:**
   - Strips trailing/leading whitespace
   - Preserves paragraph breaks within content

### Jupyter Notebook Converter

1. **Splits document at headers:**
   - Each H1/H2 starts a new cell
2. **Creates Markdown cells:**
   - Uses Jupyter's `{"cell_type": "markdown"}` format
3. **Preserves formatting:**
   - Text between headers stays together
4. **Generates notebook JSON:**
   - Wraps cells in Jupyter's `nbformat` structure

---

## 🐛 Known Issues & Edge Cases

**Orphaned H2 Headers:**
- H2 sections before any H1 are wrapped in `# Uncategorized`
- This prevents data loss but may need manual cleanup

**Pre-Header Content:**
- Text before the first header is ignored
- Move introductory text after first H1 if needed

**Deep Nesting:**
- Only H1 and H2 levels supported
- H3+ headers treated as regular content

**File Paths:**
- Relative paths work from current directory
- Use absolute paths if running from different location

---

## 🎓 CLI Help

**Get help:**
```bash
python md_to_json.py --help
python md_to_json_colab.py --help
```

**Example output:**
```
usage: md_to_json.py [-h] input output

Convert Markdown to hierarchical JSON

positional arguments:
  input       Input Markdown file (.md)
  output      Output JSON file (.json)

optional arguments:
  -h, --help  show this help message and exit

Examples:
  python md_to_json.py document.md output.json
  python md_to_json.py notes.md structured_notes.json
```

---

## 🤝 Contributing

**Issues found?** Open an issue on GitHub.

**Improvements?** Submit a pull request.

**Potential enhancements:**
- [ ] H3+ support (deeper nesting)
- [ ] Custom JSON schema options
- [ ] Batch processing CLI flag
- [ ] Progress bar for large files
- [ ] YAML/TOML output formats
- [ ] Markdown-to-Markdown reformatter

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🔗 Related Projects

**For more advanced Markdown parsing:**
- [mistune](https://github.com/lepture/mistune) - Fast Markdown parser
- [markdown-it-py](https://github.com/executablebooks/markdown-it-py) - Markdown parser with plugin support
- [pandoc](https://pandoc.org/) - Universal document converter

**For Jupyter workflows:**
- [nbconvert](https://nbconvert.readthedocs.io/) - Convert notebooks to various formats
- [jupytext](https://jupytext.readthedocs.io/) - Markdown ↔ Notebook sync

---

## 🏷️ Naming Convention

**Repository:** `md-to-json` (kebab-case)  
**Python files:** `md_to_json.py` (snake_case)  
**Functions:** `md_to_json()` (snake_case)

This follows Python naming conventions (PEP 8):
- Modules/files: lowercase with underscores
- Functions: lowercase with underscores
- Repository: kebab-case (GitHub standard)

---

**Maintained by:** Robin Wong  
**Repository:** https://github.com/robinlwong/md-to-json
