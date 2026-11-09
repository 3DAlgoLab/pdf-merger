from pathlib import Path

import pytest
from pypdf import PdfReader, PdfWriter

from pdf_merger import PdfMergeError, _parse_size, merge_pdfs

A4_PORTRAIT = (595.28, 841.89)
A4_LANDSCAPE = (841.89, 595.28)


def _make_pdf(path: Path, width: float, height: float) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=width, height=height)
    with path.open("wb") as file:
        writer.write(file)


def _page_size(pdf_path: Path, index: int = 0) -> tuple[float, float]:
    page = PdfReader(pdf_path).pages[index]
    return (float(page.mediabox.width), float(page.mediabox.height))


def test_parse_size_accepts_wxh_in_any_case() -> None:
    assert _parse_size("612x792") == (612, 792)
    assert _parse_size("612X792") == (612, 792)
    assert _parse_size(" 612x792 ") == (612, 792)


def test_parse_size_forces_requested_orientation() -> None:
    assert _parse_size("A4", "landscape") == A4_LANDSCAPE
    assert _parse_size("A4", "portrait") == A4_PORTRAIT
    assert _parse_size("800x1200", "landscape") == (1200, 800)
    assert _parse_size("800x1200", "portrait") == (800, 1200)
    assert _parse_size("A4", "auto") == A4_PORTRAIT


def test_parse_size_rejects_invalid_values() -> None:
    with pytest.raises(ValueError):
        _parse_size("B5")
    with pytest.raises(ValueError):
        _parse_size("abcxdef")


def test_merge_normalizes_named_size_and_orientation(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()
    _make_pdf(source / "1.pdf", *A4_PORTRAIT)
    _make_pdf(source / "2.pdf", *A4_PORTRAIT)
    output = tmp_path / "docs.pdf"

    count = merge_pdfs(source, output, "A4", "landscape")

    assert count == 2
    assert _page_size(output, 0) == pytest.approx(A4_LANDSCAPE)
    assert _page_size(output, 1) == pytest.approx(A4_LANDSCAPE)


def test_merge_auto_preserves_each_source_orientation(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()
    _make_pdf(source / "1.pdf", *A4_PORTRAIT)
    _make_pdf(source / "2.pdf", *A4_LANDSCAPE)
    output = tmp_path / "docs.pdf"

    merge_pdfs(source, output, "A4", "auto")

    assert _page_size(output, 0) == pytest.approx(A4_PORTRAIT)
    assert _page_size(output, 1) == pytest.approx(A4_LANDSCAPE)


def test_merge_normalizes_explicit_wxh(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()
    _make_pdf(source / "1.pdf", *A4_PORTRAIT)
    output = tmp_path / "docs.pdf"

    merge_pdfs(source, output, "800x1200", "portrait")

    assert _page_size(output) == pytest.approx((800, 1200))


def test_merge_without_pdfs_raises(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()

    with pytest.raises(PdfMergeError):
        merge_pdfs(source, tmp_path / "docs.pdf")
