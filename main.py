# Author: Timothy P. McCrary

from typing import Dict, List
from argparse import ArgumentParser
import time

from map_reduce.file_handler import FileHandler



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

    # List of words we will be searchinf for in the shakespeare files.
    word_list: List[str] = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]

    # Get a list of the shakespeare file names.
    shakespeare_filenames: List[str] = FileHandler.get_all_filenames_in_directory(directory_name)

    startTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    # Perform map reduce on files to get word count.
    word_count: Dict[str, int] = FileHandler.map_reduce(shakespeare_filenames, word_list, thread_count)
    endTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    elapsedTime: float = endTime - startTime

    print(f"\nWord Count: \n{word_count}\n")
    print(f"Duration: {elapsedTime}s")





    

if __name__ == '__main__':
    main()
