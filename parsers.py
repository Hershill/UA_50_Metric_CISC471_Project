"""
parsers.py file containing the implementation of many helper functions used across all three algorithms.

Part 1 of HW 5 for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

This class has many functions that are used in the algorithm to parse input data
accessible via a simple function call
"""


def parse_assembly_data(filename):
    """Read in the RNA sequence data from a file

    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()

    for i in range(len(data_set)):
        data_set[i] = data_set[i].replace("\n", "")

    return data_set


def parse_dna_data(filename):
    """Read in the RNA sequence data from a file

    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readline()

    # for i in range(len(data_set)):
    #     data_set += data_set[i].replace("\n", "")
    data_set = data_set.strip("\n")

    return data_set


def parse_gc_data(filename):
    """Read in the RNA sequence data from a file

    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()

    FASTA_data_set = dict()

    for i in range(len(data_set)):
        if data_set[i][0] == ">":
            data_set_name = data_set[i][1:].strip("\n")
            FASTA_data_set[data_set_name] = ""
        else:
            FASTA_data_set[data_set_name] += data_set[i].strip("\n")

    return FASTA_data_set


def parse_hamm_data(filename):
    """Read in the RNA sequence data from a file
    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()
    
    hamm_data = list()

    for i in range(len(data_set)):
        hamm_data.append(data_set[i].strip("\n"))

    return hamm_data


def parse_lexf_data(filename):
    """Read in the RNA sequence data from a file
    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()
    
    lexf_data = list()

    for i in range(len(data_set)):
        lexf_data.append(data_set[i].strip("\n"))

    return lexf_data


def parse_subs_data(filename):
    """Read in the RNA sequence data from a file
    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()

    lexf_data = list()

    for i in range(len(data_set)):
        lexf_data.append(data_set[i].strip("\n"))

    return lexf_data