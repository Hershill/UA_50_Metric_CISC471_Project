"""
helpers.py file containing the implementation of many helper functions used across all three algorithms.

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

This class has many functions that are shared across all three algorithms.

"""


def parse_data(filename):
    """Read in the RNA sequence data from a file

    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.readlines()

    for i in range(len(data_set)):
        data_set[i] = data_set[i].replace("\n", "")

    return data_set


def get_len_of_genome(dna_set):
    """Get the assembled contig length

    :param dna_set: set of contigs
    :return: length of assembled contigs
    """

    genome_len = 0
    for contig in dna_set:
        genome_len += len(contig)
    return genome_len
