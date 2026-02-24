# python-mdToJson

**Convert Markdown files to structured JSON formats**

A lightweight Python utility for parsing Markdown documents into structured JSON. Supports two output formats:
1. **Hierarchical JSON** - Nested structure with H1/H2 headers
2. **Jupyter Notebook** - Google Colab-compatible `.ipynb` format

---

## 📋 Features

- **Hierarchical JSON Export** - Preserves document structure with nested sections
- **Jupyter Notebook Export** - Converts Markdown to Colab-ready notebooks
- **Whitespace Agnostic** - Handles varying formatting styles
- **Preserves Content** - Maintains paragraph breaks and formatting

---

## 🚀 Quick Start

### 1. Hierarchical JSON Export (`mdToJson.py`)

Converts Markdown to nested JSON structure.

**Usage:**
```python
from mdToJson import mdtojson

mdtojson('input.md', 'output.json')
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

### 2. Jupyter Notebook Export (`mdToJson-colab.py`)

Converts Markdown to Google Colab-compatible `.ipynb` format.

**Usage:**
```python
from mdToJson_colab import mdtojson_colab

mdtojson_colab('input.md', 'output.ipynb')
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

| File | Purpose | Output Format |
|------|---------|---------------|
| `mdToJson.py` | Hierarchical JSON converter | `.json` with nested structure |
| `mdToJson-colab.py` | Jupyter Notebook converter | `.ipynb` (Colab-compatible) |

---

## 🔧 Installation

**Requirements:**
- Python 3.6+
- Standard library only (no external dependencies)

**Clone the repository:**
```bash
git clone https://github.com/robinlwong/python-mdToJson.git
cd python-mdToJson
```

---

## 📖 Usage Examples

### Example 1: Convert Documentation to JSON

```python
from mdToJson import mdtojson

# Convert project documentation
mdtojson('PROJECT_DOCS.md', 'docs_structured.json')
```

**Use Cases:**
- API documentation parsing
- Knowledge base structuring
- Content management systems
- Search indexing

---

### Example 2: Import to Google Colab

```python
from mdToJson_colab import mdtojson_colab

# Convert notes to Colab notebook
mdtojson_colab('research_notes.md', 'research.ipynb')
```

**Then:**
1. Upload `research.ipynb` to Google Drive
2. Open with Google Colab
3. Each H1/H2 appears as a collapsible section

**Use Cases:**
- Research notes organization
- Tutorial creation
- Educational content
- Long-form documentation

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

---

## 🤝 Contributing

**Issues found?** Open an issue on GitHub.

**Improvements?** Submit a pull request.

**Use cases:**
- Add H3+ support
- Custom JSON schema options
- Batch processing
- CLI interface

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

**Maintained by:** Robin Wong  
**Repository:** https://github.com/robinlwong/python-mdToJson
