
import shutil
import os

def make_tarfile(folder_path):
    if os.path.exists(folder_path):
        shutil.make_archive(folder_path, 'tar', folder_path)