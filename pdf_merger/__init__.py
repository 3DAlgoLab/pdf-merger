from pathlib import Path
from typing import Literal, Optional, Tuple

from pypdf import PdfWriter


class PdfMergeError(Exception):
    """Raised when PDF merging fails."""

    pass


PAGE_SIZES = {
    "A4": (595.28, 841.89),
    "A4_LANDSCAPE": (841.89, 595.28),
    "A3": (841.89, 1190.55),
    "A3_LANDSCAPE": (1190.55, 841.89),
    "LETTER": (612, 792),
    "LETTER_LANDSCAPE": (792, 612),
    "LEGAL": (612, 1008),
    "LEGAL_LANDSCAPE": (1008, 612),
}


Orientation = Literal["auto", "portrait", "landscape"]


def _parse_size(
    size_str: str, orientation: Orientation = "auto"
) -> Tuple[float, float]:
    """Parse size string like 'A4', 'A4_LANDSCAPE', or '612x792'.

    Args:
        size_str: Size name (A4, A3, LETTER, LEGAL) or WxH format.
        orientation: auto, portrait, or landscape. portrait and landscape
            force the returned dimensions to that orientation.

    Raises:
        ValueError: If size_str is not a known size or a valid WxH value.
    """
    normalized = size_str.upper().strip()
    if "X" in normalized:
        parts = normalized.split("X")
        if len(parts) != 2:
            raise ValueError(
                f"Invalid size: {size_str}. Use A4, A3, LETTER, LEGAL, or WxH format."
            )
        try:
            width, height = float(parts[0]), float(parts[1])
        except ValueError:
            raise ValueError(
                f"Invalid size: {size_str}. Use A4, A3, LETTER, LEGAL, or WxH format."
            ) from None
    elif normalized in PAGE_SIZES:
        width, height = PAGE_SIZES[normalized]
    else:
        raise ValueError(
            f"Invalid size: {size_str}. Use A4, A3, LETTER, LEGAL, or WxH format."
        )

    if orientation == "portrait" and width > height:
        return (height, width)
    if orientation == "landscape" and width < height:
        return (height, width)
    return (width, height)


def merge_pdfs(
    input_dir: Path,
    output_file: Path,
    normalize_size: Optional[str] = None,
    orientation: Orientation = "auto",
) -> int:
    """Merge all PDF files in a directory into a single PDF.

    Args:
        input_dir: Path to directory containing PDF files.
        output_file: Path for the output merged PDF file.
        normalize_size: Optional page size to normalize all pages to.
            Can be A4, A3, LETTER, LEGAL, or WxH (e.g., 612x792).
        orientation: Orientation mode for auto-sized pages.
            auto: detect portrait/landscape from source page dimensions (default).
            portrait: force all pages to portrait orientation.
            landscape: force all pages to landscape orientation.

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

    target_size: Optional[Tuple[float, float]] = None
    if normalize_size:
        target_size = _parse_size(normalize_size, orientation)

    try:
        merger = PdfWriter()
        for pdf_file in pdf_files:
            if target_size:
                first_new_page = len(merger.pages)
                merger.append(pdf_file)
                for page in merger.pages[first_new_page:]:
                    current_width = float(page.mediabox.width)
                    current_height = float(page.mediabox.height)

                    if orientation == "auto":
                        if current_width > current_height:
                            target_width, target_height = (
                                target_size[1],
                                target_size[0],
                            )
                        else:
                            target_width, target_height = target_size
                    else:
                        target_width, target_height = target_size

                    scale_x = target_width / current_width
                    scale_y = target_height / current_height
                    page.scale(scale_x, scale_y)
            else:
                merger.append(pdf_file)

        merger.write(output_file)
        merger.close()
    except Exception as e:
        raise PdfMergeError(f"Failed to merge PDFs: {e}") from e

    return len(pdf_files)
