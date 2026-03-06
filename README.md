# PDF Merger

A simple CLI tool to merge all PDF files in a directory into a single PDF.

## Installation

### Prerequisites

- Python 3.10 or higher
- uv package manager

### Recommended: uv tool install (Linux/macOS/Windows)

Using `uv tool install` is the recommended way to install CLI tools with uv:

```bash
# Install uv (if not installed)
# Linux/macOS:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex

# Clone or download this repository
cd pdf-merger

# Install as a tool
uv tool install .
```

This makes `pdf_merge` available globally in your PATH.

### Install from GitHub (without cloning)

```bash
# Install directly from GitHub
uv tool install git+https://github.com/3DAlgoLab/pdf-merger

# Or with a specific version/tag
uv tool install git+https://github.com/3DAlgoLab/pdf-merger@v0.1.0
```

### Alternative: uv pip install

```bash
# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or download this repository
cd pdf-merger

# Install dependencies
uv pip install -e .
```

## Usage

```bash
# Navigate to directory containing PDFs
cd /path/to/your/pdfs

# Run the merger
pdf_merge .
```

This will create a merged PDF named after the current directory.

### Examples

**Linux/macOS:**
```bash
cd ~/Documents/my_pdfs
pdf_merge .
# Creates: ~/Documents/my_pdfs.pdf
```

**Windows:**
```powershell
cd C:\Users\You\Documents\my_pdfs
pdf_merge .
# Creates: C:\Users\You\Documents\my_pdfs.pdf
```

### Options

```bash
pdf_merge --help
```

## Uninstall

```bash
# If installed with uv tool install (local or GitHub)
uv tool uninstall pdf-merger

# If installed with uv pip install
uv pip uninstall pdf-merger
```
