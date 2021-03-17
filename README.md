# CISC 471 Group Project

This project contains the programming implementation for our Group Project. The code was written using Python 3.8+.

Our chosen algorithm to analyse was [Assessing Assembly Quality with N50 and N75](http://rosalind.info/problems/asmq/).

## File structure

The project contains the following files:

```
.
├── main.py                             # Runs the unittests the algorithms implemented
├── algorithms.py                       # Contains the implementations of the asssemby acoring algorithms
├── sorting_algorithms.py               # Contains the implementations of the various sorting algorithms being compared
├── random_contig_set_generator.py      # Contains the implementation of a data generator to generate data sets that the assembly quality algorithms can be run on
├── helpers.py                          # Contains common helper functions used accross the different algorithms
├── unittests.py                        # Contains the unit tests for the implemented algorithms
├── sample_data_x.py                    # Contains the sample data for the unittests
├── solution_x.py                       # Contains the solutions to the sample data for the unittests
└── README.md                           # This file, contians information about the program
```

## Running the programs

The following commands can be used to run the programming question - The Peptide Encoding Problem:

- `python main.py`
- `python -m unittest unittests.py`

## 1 - N50 and N75 Algorithms

The solutions for the programming question are contained in `n50.py` and can be run from `main.py` or 
`unittests.py` depending on whether you would like to run the individual functions or the unit tests. See below for more detail.

### Running unittests and individual functions

Unittests:
- Running `main.py` or `unittests.py` using the commands above will run the unittests written for the
required functions.

Individual Functions:
- There are some commented out lines in the main method of `unittests.py` and these can be uncommented or
modified to run the functions individually.
