# PDF Merger

A simple CLI tool to merge all PDF files in a directory into a single PDF.

## Installation

### Prerequisites

- Python 3.10 or higher
- uv package manager

### Linux

```bash
# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or download this repository
cd pdf-merger

# Install dependencies
uv pip install -e .
```

### macOS

```bash
# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or download this repository
cd pdf-merger

# Install dependencies
uv pip install -e .
```

### Windows

```powershell
# Install uv (if not installed)
irm https://astral.sh/uv/install.ps1 | iex

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
uv pip uninstall pdf-merger
```
