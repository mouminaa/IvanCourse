import os
import shutil
import subprocess
import pytest
from tempfile import TemporaryDirectory

from djvu import convert_djvu_to_images, get_djvu_path


def test_convert_djvu_to_images():
    with TemporaryDirectory() as tmpdir:
        input_file_path = 'input/sample.djvu'
        output_dir_path = os.path.join(tmpdir, 'output_djvu')
        convert_djvu_to_images(input_file_path, output_dir_path)
        assert os.path.exists(os.path.join(output_dir_path, 'output_000.jpg'))


def test_get_djvu_path_ddjvu_found(monkeypatch):
    monkeypatch.setattr(shutil, 'which', lambda x: '/usr/bin/ddjvu')
    djvu_path = get_djvu_path()
    assert djvu_path == '/usr/bin/ddjvu'


def test_get_djvu_path_ddjvu_not_found(monkeypatch):
    monkeypatch.setattr(shutil, 'which', lambda x: None)
    with pytest.raises(FileNotFoundError):
        get_djvu_path()