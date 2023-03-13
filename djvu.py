import os
import shutil
import subprocess

def get_djvu_path():
    # Check if ddjvu command exists
    if shutil.which('ddjvu') is None:
        raise FileNotFoundError('ddjvu not found in path')

    # Get path to ddjvu executable
    djvu_path = shutil.which('ddjvu')
    print(f"djvu_path: {djvu_path}")
    return djvu_path


def convert_djvu_to_images(input_file_path, output_dir_path):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Call ddjvu to convert the input file to PPM images
    subprocess.call(['ddjvu', '-format=ppm', '-scale=30%', input_file_path, os.path.join(output_dir_path, 'output_%03d.ppm')])

    # Set path to ddjvu executable manually
    djvu_path = '/usr/bin/ddjvu'

    # Call convert to convert the PPM images to JPEG
    print(f"Converting {djvu_path} to images...")
    subprocess.call([djvu_path, '-format=ppm', input_file_path, os.path.join(output_dir_path, 'output_000.jpg')])
    print("Conversion complete.")

    # Check if the output images were created successfully
    assert os.path.exists(os.path.join(output_dir_path, 'output_000.jpg'))


# Example usage
convert_djvu_to_images('input/sample.djvu', 'output_djvu')