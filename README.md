### Timothy P. McCrary

# Parallel-Computing-MapReduce


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

```
### Example Usage:
```bash
python3 main.py -t 4
```

# Report
#### Problems

#### Time to Complete

#### Performance Measurements

#### Analysis

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
