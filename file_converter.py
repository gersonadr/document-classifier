from PIL import Image
import fitz
import os


def convert_pdf_to_png(pdf_file):

    # Open the PDF file
    with fitz.open(pdf_file) as pdf:

        # Iterate through the pages
        for page in pdf:

            # Render the page as a PNG image
            pix = page.get_pixmap(alpha=False)

            # Save the image as a PNG file
            pix.save(f"{pdf_file}.png")

            # Only the first page is needed
            break


def convert_image_to_png(image_file):
    file_name = os.path.splitext(image_file)[0]
    output_file = file_name + ".png"

    with Image.open(image_file) as im:
        # Convert the image to PNG and save it
        im.save(output_file)
