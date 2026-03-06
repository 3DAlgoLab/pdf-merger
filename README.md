# PDF Merger

A simple CLI tool to merge all PDF files in a directory into a single PDF.

## Installation

### Prerequisites

- Python 3.10 or higher
- uv package manager

### Recommended: uv tool install from GitHub (Linux/macOS/Windows)

The easiest way to install - no cloning required:

```bash
# Install uv (if not installed)
# Linux/macOS:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex

# Install directly from GitHub
uv tool install git+https://github.com/3DAlgoLab/pdf-merger

# Or with a specific version/tag
uv tool install git+https://github.com/3DAlgoLab/pdf-merger@v0.1.0
```

This makes `pdf_merge` available globally in your PATH.

### Alternative: Clone and install

```bash
# Clone the repository
git clone https://github.com/3DAlgoLab/pdf-merger
cd pdf-merger

# Install as a tool
uv tool install .
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

### Page Size Normalization

You can normalize all pages to a standard size:

```bash
# Normalize all pages to A4 (auto-detect orientation from source)
pdf_merge . --size A4

# Force all pages to portrait or landscape
pdf_merge . --size A4 --orientation portrait
pdf_merge . --size A4 --orientation landscape

# Available sizes: A4, A3, LETTER, LEGAL, or WxH (e.g., 612x792)
pdf_merge . --size 800x1200 --orientation auto
```

**Orientation options:**
- `auto` (default): detects portrait/landscape from source page dimensions
- `portrait`: forces all pages to portrait
- `landscape`: forces all pages to landscape

## Uninstall

```bash
# If installed with uv tool install (GitHub or local)
uv tool uninstall pdf-merger

# If installed with uv pip install
uv pip uninstall pdf-merger
```
