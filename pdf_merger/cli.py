import logging
import sys
from pathlib import Path

import click

from pdf_merger import PdfMergeError, merge_pdfs

logger = logging.getLogger(__name__)


@click.command()
@click.argument("directory", type=click.Path(exists=True, path_type=Path))
def main(directory: Path) -> None:
    """Merge all PDF files in DIRECTORY into a single PDF named after the directory."""
    logger.info(f"Merging PDFs from: {directory}")

    output_file = directory.with_suffix(".pdf")

    try:
        count = merge_pdfs(directory, output_file)
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
