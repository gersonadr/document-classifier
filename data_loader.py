import file_searcher
import file_converter
import image_parser
from tqdm import tqdm
import os


def load_one(filename):
    if filename.lower().endswith(".pdf"):
        file_converter.convert_pdf_to_png(filename)
    else:
        file_converter.convert_image_to_png(filename)

    type = get_type(filename)
    fields = image_parser.convert_image_to_fields(filename + ".png")

    all_text = [i["text"] for i in fields]
    all_text = " ".join(all_text)
    field = {}
    field["text"] = all_text
    field["type"] = type
    return [field]


def load(docs_folder, extract_images=False, document_level=True):

    if extract_images:
        pdf_files = file_searcher.list_files_with_extension(
            ".pdf", folder_path=docs_folder
        )
        print(" - Step 1 - saving PDF's 1st page as PNG")
        for pdf_file in tqdm(pdf_files):
            file_converter.convert_pdf_to_png(docs_folder + "/" + pdf_file)

        print(" - Step 2 - finding non-PNG images")
        image_files = file_searcher.list_non_png_image_files(folder_path=docs_folder)

        print(" - Step 3 - Converting images to .PNG")
        for image_file in tqdm(image_files):
            file_converter.convert_image_to_png(image_file)

    data = []

    print(" - Step 4 - OCRing PNGs")
    png_files = file_searcher.list_files_with_extension(".png", folder_path=docs_folder)
    for png_file in tqdm(png_files):

        try:
            # get type
            type = get_type(png_file)

            # get fields
            fields = image_parser.convert_image_to_fields(docs_folder + "/" + png_file)

            if document_level:
                all_text = [i["text"] for i in fields]
                all_text = " ".join(all_text)
                field = {}
                field["text"] = all_text
                field["type"] = type
                field["filename"] = png_file
                data.append(field)
            else:
                for field in fields:
                    field["type"] = type
                    data.append(field)
        except:
            pass

    return data


def get_type(path):

    documents_folder = "Documents"
    common_prefix = os.path.commonprefix(
        [path, os.path.join(os.path.sep, documents_folder)]
    )
    relative_path = os.path.relpath(path, common_prefix)
    next_folder = os.path.split(relative_path)[0]

    return next_folder
