# Author: Timothy P. McCrary


from io import TextIOWrapper
import os
from typing import Dict, List
import pymp


class FileHandler:



    def get_all_filenames_in_directory(directory: str) -> List[str]:
        """Given a directory, gets all files names in said directory (includes directory in file name.)

        Args:
            directory (str): The directory that will be searched for files.

        Returns:
            List[str]: A list of file names.
        """

        filesnames: List[str] = []

        filename: str
        for filename in os.listdir(os.getcwd() + "/" + directory):
            filesnames.append(directory + "/" + filename)
            
        return filesnames



    def map_reduce(filenames: List[str], word_list: List[str], thread_count: int) -> Dict[str, int]:
        """Using parallel map reduce, finds the number of times a list of words are found in a .txt file.

        Args:
            filenames (List[str]): List of filenames that will be opened and searched.
            word_list (List[str]): List of words that we want to find.
            thread_count (int): Number of threads used for parallel.

        Returns:
            Dict[str, int]: The number of times each word is found.
        """

        # Initialize dictionary that will be shared amongst all threads.
        shared_word_count: Dict[str, int] = pymp._shared.dict()

        # Initializes dictionary that is not shared, and will allow a thread to upate a .txt word count without the use of a lock.
        nonshared_word_count: Dict[str, int] = {}

        # Start pymp with given thrad count
        with pymp.Parallel(thread_count) as p:

            # For each file, we brak up the work using pymps iterate. Each thread will get a file, and as work becomes available, a thread will take it.
            for filename in p.iterate(filenames):
                p.print(f"Thread {p.thread_num} handling {filename}")

                # Open the file given its name.
                open_file: TextIOWrapper = open(filename, "r")

                # Read the filing, turning it into a string, and make that string lowercase.
                file_text: str = open_file.read().lower()

                # Get the word count.
                nonshared_word_count = FileHandler.get_word_count(file_text, word_list)
                        
                p.lock.acquire()
                for word in nonshared_word_count:
                    if word in shared_word_count:
                        shared_word_count[word] += nonshared_word_count[word]
                    else:
                        shared_word_count[word] = nonshared_word_count[word]
                p.lock.release()
        
        return shared_word_count



    def get_word_count(given_string: str, word_list: List[str]) -> Dict[str, int]:
        """Given a string and a list of words, returns a dictionary of how many times those words are found in that string.

        Args:
            given_string (str): String to search.
            word_list (List[str]): List of words we are searching for.

        Returns:
            Dict[str, int]: Dictionary of how many times a word is found.
        """

        word_count: Dict[str, int] = {}

        word: str
        for word in word_list:
            word_count[word] = given_string.count(word)
        
        return word_count




                
