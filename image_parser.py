import pytesseract
from PIL import Image
import xml_parser

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def convert_image_to_fields(image_file):

    # Open the image file
    with Image.open(image_file) as img:

        # Extract the text using Pytesseract
        xml_string = pytesseract.image_to_alto_xml(img)

        # Print the extracted text
        return xml_parser.get_fields_from_xml(xml_string.decode())
