from io import TextIOBase, TextIOWrapper
import os
from pathlib import Path
from typing import List

class FileReadHelper:

    def get_all_file_names_in_directory(directory_name: str) -> List[str]:

        filesnames: List[str] = []

        filename: str
        for filename in os.listdir(os.getcwd() + "/" + directory_name):
            filesnames.append(filename)
            
        return filesnames

    def open_files(filenames: List[str], directory_name: str) -> List[TextIOWrapper]:

        open_files: List[TextIOWrapper] = []

        for filename in filenames:
            open_files.append(open(directory_name + "/" + filename, "r"))

        return open_files



