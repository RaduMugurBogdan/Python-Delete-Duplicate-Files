import os


def test_folder_path(input_path):
    return os.path.isdir(input_path)==True
