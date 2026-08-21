import logging
import sys
from pathlib import Path
from typing import Optional, cast

import click

from pdf_merger import Orientation, PdfMergeError, merge_pdfs

logger = logging.getLogger(__name__)


@click.command()
@click.argument("directory", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--size",
    "-s",
    "normalize_size",
    default=None,
    help="Normalize page size to specified size. "
    "Options: A4, A3, LETTER, LEGAL, or WxH (e.g., 612x792).",
)
@click.option(
    "--orientation",
    "-o",
    "orientation",
    type=click.Choice(["auto", "portrait", "landscape"]),
    default="auto",
    help="Page orientation: auto (detect from source), "
    "portrait, or landscape. Default: auto.",
)
def main(
    directory: Path,
    normalize_size: Optional[str],
    orientation: str,
) -> None:
    """Merge all PDF files in DIRECTORY into a single PDF named after the directory."""

    directory = directory.resolve()
    logger.info(f"Merging PDFs from: {directory}")

    output_file = directory.with_suffix(".pdf")

    try:
        count = merge_pdfs(
            directory, output_file, normalize_size, cast(Orientation, orientation)
        )
        click.echo(f"Successfully merged {count} PDF(s) into {output_file}")
    except PdfMergeError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        logger.exception("Unexpected error")
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
