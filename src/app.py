"""
python src/app.py \
--input-folder /Users/ananyalahiri/Downloads/testDocuments-Claudius-2025-04_limitedPages \
--output-folder /Users/ananyalahiri/Downloads/testDocuments-Claudius-images
"""

import fitz
import os
import click
from pathlib import Path


@click.command()
@click.option(
    "--input-folder", type=str, required=True, help="Input folder path",
)
@click.option(
    "--output-folder", type=str, required=True, help="Output folder path",
)
def main(
        input_folder: str,
        output_folder: str,
):
    print("Starting")
    if not Path(input_folder).is_dir():
        raise FileNotFoundError(f"{input_folder} is not a directory")

    Path(output_folder).mkdir(parents=True, exist_ok=True)
    print("output dir created")

    try:
        for f in Path(input_folder).rglob("*.pdf"):
            print(f"processing file: {f}")
            pdf_document = fitz.open(str(f))
            dest_folder = f"{output_folder}/{f.stem}"
            Path(dest_folder).mkdir(exist_ok=True, parents=True)

            # Iterate through each page
            for page_number in range(len(pdf_document)):
                page = pdf_document[page_number]

                # Render the page as an image
                pix = page.get_pixmap(dpi=300)  # Adjust DPI for quality

                # Save the image as a PNG
                # output_file = os.path.join(output_folder, f"{os.path.splitext(f)[0]}_page_{page_number + 1}.png")
                output_file = f"{dest_folder}/{f.stem}_page_{page_number + 1}.png"
                print(f"{output_file=}")
                pix.save(output_file)
                print(f"Saved: {output_file}")
            pdf_document.close()
    except Exception as e:
        raise ValueError(f"Document {str(f)} could not be converted: {e}")

    print(f"All documents converted to images: {output_folder}")


if __name__ == "__main__":
    main()
