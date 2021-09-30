# Author: Timothy P. McCrary

from io import TextIOWrapper
from typing import List
from argparse import ArgumentParser

import pymp

from map_reduce.file_read_helper import FileReadHelper



def main():

    parser: ArgumentParser = ArgumentParser(
        description='Perfom parallel word counting on files.')
    parser.add_argument('-t', '--threads', default=1, type=int,
                        help='(int, optional) Number of threads to use in parallel.')
    parser.add_argument('-d', '--directory', default="shakespeare_files", type=str,
                        help='(str, optional) At project root, directory name to files that will be searched.')

    args = parser.parse_args()

    thread_count: bool = args.threads
    directory_name: str = args.directory

    shakespeare_filenames: List[str] = FileReadHelper.get_all_file_names_in_directory(directory_name)

    open_files: List[TextIOWrapper] = FileReadHelper.open_files(shakespeare_filenames, directory_name)

    print(open_files)

    

    
    pass

if __name__ == '__main__':
    main()
