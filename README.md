### Timothy P. McCrary

# Parallel-Computing-MapReduce
This program searches and counts eight .txt files (containing Shakespeare text) for these words: `[hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest]`</br>
It is important to note, this program uses a map reduce model.</br>
The logic is that each thread gets its own file, counts the words in that file, and then finally updates a shared dictionary amonst the threads.


### IMPORTANT: Report can be found at bottom of README.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `pymp`.

```bash
pip install pymp-pypi
```

## Usage

This program uses a CLI (commnad line interface) to recieve user input.<br/><br/>
Use the following commands in the root folder of the program.<br/>
For CLI help:
```bash
python3 main.py -h
```
Outputting:
```
usage: main.py [-h] [-t THREADS] [-d DIRECTORY]

Perfom parallel word counting on files.

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        (int, optional) Number of threads to use in parallel.
  -d DIRECTORY, --directory DIRECTORY
                        (str, optional) At project root, directory name to files that will be searched.
```
### Example Usage:
```bash
python3 main.py -t 4
```
This will start the program and have it run on 4 threads.

# Report
#### Problems
During this assignment I came across one problem. Initially, I tried opening all the files and stoting them in a list of type: `List[TextIOWrapper]`. Then, I would use the pymp `iterate()` function to iterate over the list and distrubt the work. However, for some reason, pymp could not iterate over a list of type `TextIOWrapper` and would just hang. I could not figure out why this was happening, but to solve this I instead iterated over a list of type: `List[str]`. This list held all the names of the .txt files. Therefore, the threads would get assigned a file name and they would open the file once the work was distributed and not before.</br>
That being, the program is 100% working, and all words are found in the files.
#### Time to Complete
This assignment took me around 6-8 hours to complete, including the write up. The aspect that took the longest was coding the logic for the parallel section and how the words should be counted. Initially, I was looking for the exact word match, until I realize I needed to ignore case, along with abbrevitions and punctuations. After realizing this, I was able to get the correct word count.
#### Performance Measurements
This program was ran on 1, 2, 4, and 8 threads:
```
1 Thread Duration: 0.27941689899989797s
2 Thread Duration: 0.2869608490000246s
4 Thread Duration: 0.22721178000006148s
8 Thread Duration: 0.16655839899999592s
```
#### Analysis
This algorithm provided some strange (and non-consistent) results. Initially when I wrote the program, 4 threads seemed to be the sweet spot, and 8 made it slower. With the results here, 1 thread is of course slow, and 2 threads is slower. Then, 4 threads goes back to being faster, and finally 8 threads being the fastest.</br>
Best conclusion is that this is just not totally consistent, and seems to depend on the machine and what parts of memory are available.</br>
Additionally, I did try optimizing the algorithm. Specifically, by iterating over a list of strings, containing all the text. However, this turned out to be slower! Therefore, the algorithm was not altered and each thread gets its own file to open, search, and then report to a shared variable.
#### CPU Info
```
model name	: AMD Ryzen 7 5800H with Radeon Graphics
     16     160     832
```


# Parallel-Computing-MapReduce
For this assignment you will write a parallel map reduce program. The program will search for a set 
of words among a set of documents that constitute the works of Shakespeare. The set of words is listed 
below. The assignment should use the map-reduce design pattern to split up the work. You should have
functions that count the number of a specific word within a specific document and combine the individual
word counts.

The program should output the total instances of all words and the counts for each individual word

Word list:
hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest

Once completed the repository should contain your code, a short report, and any instructions needed to run your code.

Important note:
You should initialize the shared global dictionary inside your parallel section, there's a bug in the
OpenMP system that sometimes causes a program to freeze when initializing outside the parallel section.

Hints: 
* Its easier to load all the files containing text serial before entering the parallel processing region
* Some of the variables will need to be locked before updating, otherwise a difficult to debug race condition may occure
* This will take multiple loops (functions would be better though), you can iterate over the list of words

## Requirements 

Write a serial matrix multiply program in Python. The could should use reasonable decomposition, use reasonable variable names, and should generally follow good coding standards. Important, your assignment should include your name. 

The program shall count the number of each instances of each word for the set of documents, and the total of count of all words in the list

The program shall use PyMP to compute the number of words in parallel

The program shall time how long overall operation takes and how long the word count and file reading operations take individually

The program shall include any necessary instructions to properly run the program 

The assignment shall be submitted through github 
