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
import itertools


def sset(input_num):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    if input_num > 1000:
        return 0

    # mod 1,000,000
    num_ssets = 2 ** input_num % 1000000

    return num_ssets


if __name__ == '__main__':
    # filename = "sset_sample_data.txt"
    filename = "rosalind_sset.txt"
    sset_number = int(parse_dna_data(filename))
    # print(sset_number)
    subsets = sset(sset_number)
    print(subsets)
