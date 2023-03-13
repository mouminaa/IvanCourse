import pytest
import tika
from tika import parser
import os


def test_parser():
    # Initialise Tika
    tika.initVM()

    # List of paths to files to process
    files_path = ['input/momo.pdf', 'input/sample.djvu', 'input/sample2.doc', 'input/chinese.docx' ]

    # Output directory path
    output_dir_path = "output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Loop over files
    for file_path in files_path:
        # Analysis of the file with Tika
        file_content = parser.from_file(file_path)

        # Retrieval of textual content
        text_content = file_content['content']

        # Metadata retrieval
        metadata = file_content['metadata']

        # Get the file extension
        file_extension = os.path.splitext(file_path)[1]

        # Create the output file path
        output_file_path = os.path.join(
            output_dir_path, f"{file_extension}.txt")

        # Open the output file for writing with UTF-8 encoding
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write the textual content and metadata to the output file
            output_file.write(f"textual content of {file_path}:\n")
            if text_content is not None:
                output_file.write(text_content)
            output_file.write("\nMeta Data:\n")
            for cle, valeur in metadata.items():
                output_file.write(f"{cle}: {valeur}\n")

        # Check if the output file was created successfully
        assert os.path.exists(output_file_path)
