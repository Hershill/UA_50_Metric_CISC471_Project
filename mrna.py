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

from enum import Enum


# Enum for storing mapping of number of coding sequences for each Amino Acid
class PeptideReverseCodingCount(Enum):
    """Enum that stores the number of RNA coding sequences per Amino Acid
    """
    M = 1
    H = 2
    Q = 2
    P = 4
    R = 6
    L = 6
    D = 2
    E = 2
    A = 4
    G = 4
    V = 4
    Y = 2
    S = 6
    C = 2
    W = 1
    F = 2
    N = 2
    K = 2
    T = 4
    I = 3
    STOP = 3


def mrna(peptide_seq):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    count = 1

    for i in peptide_seq:
        count *= PeptideReverseCodingCount[i].value

    count *= PeptideReverseCodingCount["STOP"].value

    # mod 1,000,000
    count = count % 1000000

    return count


def format_output(max_gc_content):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_content[0]}\n{max_gc_content[1]}"

    return formatted_str


if __name__ == '__main__':
    # filename = "mrna_sample_data.txt"
    filename = "rosalind_mrna.txt"
    mrna_data = parse_dna_data(filename)
    # print(mrna_data)
    combinations = mrna(mrna_data)
    print(combinations)
