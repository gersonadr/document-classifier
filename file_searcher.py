import os
import imghdr


def list_files_with_extension(extension, folder_path="."):
    found_files = []

    # Recursively traverse the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file has the extension
            if file.lower().endswith(extension):
                # Get the relative path to the PDF file
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                # Add the relative path to the list of PDF files
                found_files.append(relative_path)

    return found_files


def list_non_png_image_files(folder_path="."):
    image_files = []
    # Iterate over all files in the directory and subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Check if the file is an image
            image_type = imghdr.what(file_path)
            if image_type is not None:
                # Check if the image type is not PNG
                if not image_type.lower() == "png":
                    # Check if the file extension is not PNG
                    if not file.lower().endswith(".png"):
                        image_files.append(file_path)
    return image_files


def test():
    result = list_non_png_image_files()
    print(result)
