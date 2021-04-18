"""
dna.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Counting DNA Nucleotides Problem

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
'T' occur in s.
"""


from parsers import *


def dna(dna_str):
    """Return dict of counts of each nucleotide in DNA set
    :param dna_str: string of nucleotides
    :return: dict of count of nucleotides
    """

    # set up dict for A, C, G, T
    count = {
        "A": 0, "C": 0, "G": 0, "T": 0
    }

    for i in dna_str:
        count[i] += 1

    return count


def format_output(counts):
    """ Format output according to problem requirement

    :param counts: dict of counts of nucleotides
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

    return formatted_str


if __name__ == '__main__':
    # filename = "dna_sample_data.txt"
    filename = "rosalind_dna.txt"
    dna_str = parse_dna_data(filename)
    print(dna_str)
    counts = dna(dna_str)
    print(format_output(counts))
