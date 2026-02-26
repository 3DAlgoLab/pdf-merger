# Agent Guidelines for pdf-merger

## Project Overview

Simple PDF merger CLI tool written in Python 3.13 using the uv framework. Merges all PDF files in a directory into a single PDF named after the directory.

## Project Configuration

- **Python Version**: 3.13
- **Package Manager**: uv
- **Project Type**: CLI application

## Commands

### Running the Application

```bash
uv run pdf_merge <directory>
```

### Installing Dependencies

```bash
uv pip install <package>   # Install without saving to pyproject.toml
uv add <package>           # Install and save to pyproject.toml
```

### Running Tests

```bash
uv run pytest              # Run all tests
uv run pytest -x           # Stop on first failure
uv run pytest -k <pattern> # Run tests matching pattern
uv run pytest tests/test_file.py::test_function_name  # Single test
```

### Linting and Formatting

When configured, use ruff:

```bash
uv run ruff check .   # Lint
uv run ruff format .  # Format
uv run mypy .         # Type check
```

## Code Style Guidelines

### General Principles

- Write simple, readable code - prefer clarity over cleverness
- Follow Python philosophy: "There should be one obvious way to do it"
- Keep functions small and focused (single responsibility)
- Avoid premature abstraction

### Formatting

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters
- Two blank lines between top-level definitions (classes, functions)

### Imports

Group in order: standard library, third-party, local. Sort alphabetically within each group.

```python
import os
from pathlib import Path

import click
from PyPDF2 import PdfMerger

from pdf_merger import merge_pdfs
```

### Naming Conventions

- Variables/functions: `snake_case` (e.g., `input_file`, `merge_pdfs`)
- Classes: `PascalCase` (e.g., `PdfMerger`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_FILE_SIZE`)
- Private: prefix with underscore (e.g., `_validate_input`)

### Types

- Use type hints for all function parameters and return values
- Use `Optional[X]` instead of `X | None`
- Use `Union[X, Y]` instead of `X | Y`

```python
def merge_pdfs(input_dir: Path, output_file: Path) -> int:
    files: list[Path] = list(input_dir.glob("*.pdf"))
    return len(files)
```

### Error Handling

- Use exceptions for exceptional cases, not control flow
- Catch specific exceptions, not bare `except:`
- Include informative error messages
- Use custom exceptions for domain-specific errors

```python
class PdfMergeError(Exception):
    pass

def merge_pdfs(input_dir: Path, output_file: Path) -> None:
    if not input_dir.exists():
        raise FileNotFoundError(f"Directory not found: {input_dir}")
```

### Logging

- Use `logging` module for application logging
- Configure at application entry point
- Use appropriate levels: DEBUG, INFO, WARNING, ERROR

```python
import logging
logger = logging.getLogger(__name__)

def merge_pdfs(input_dir: Path, output_file: Path) -> None:
    logger.info(f"Merging PDFs from {input_dir}")
```

### CLI Interface

- Use `click` for CLI interface
- Use type hints on CLI options
- Provide helpful error messages and usage examples

### Docstrings

Use Google-style or NumPy-style. Include brief description, Args, Returns, Raises.

```python
def merge_pdfs(input_dir: Path, output_file: Path) -> int:
    """Merge all PDF files in a directory into a single PDF.

    Args:
        input_dir: Path to directory containing PDF files.
        output_file: Path for the output merged PDF file.

    Returns:
        Number of PDF files merged.

    Raises:
        PdfMergeError: If merging fails.
    """
```

### Testing

- Place tests in `tests/` directory
- Name test files `test_<module>.py`
- Name test functions `test_<description>`

```python
def test_merge_pdfs_returns_count(tmp_path):
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    (pdf_dir / "1.pdf").write_bytes(b"%PDF-1.4")
    (pdf_dir / "2.pdf").write_bytes(b"%PDF-1.4")
    
    count = merge_pdfs(pdf_dir, tmp_path / "output.pdf")
    assert count == 2
```

### Git Practices

- Make small, focused commits
- Write commit messages in imperative mood
- Run linting and tests before committing
- Never commit secrets or credentials
