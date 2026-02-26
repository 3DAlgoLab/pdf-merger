from pathlib import Path

from pypdf import PdfWriter


class PdfMergeError(Exception):
    """Raised when PDF merging fails."""
    pass


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
    if not input_dir.exists():
        raise FileNotFoundError(f"Directory not found: {input_dir}")

    if not input_dir.is_dir():
        raise NotADirectoryError(f"Not a directory: {input_dir}")

    pdf_files = sorted(input_dir.glob("*.pdf"))

    if not pdf_files:
        raise PdfMergeError(f"No PDF files found in: {input_dir}")

    try:
        merger = PdfWriter()
        for pdf_file in pdf_files:
            merger.append(pdf_file)

        merger.write(output_file)
        merger.close()
    except Exception as e:
        raise PdfMergeError(f"Failed to merge PDFs: {e}") from e

    return len(pdf_files)
