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


def hamm(dna_str_1, dna_str_2):
    """Return dict of counts of each nucleotide in DNA set
    :param dna_str_1: string of dna
    :param dna_str_2: string of dna
    :return: dict of count of nucleotides
    """

    if len(dna_str_1) != len(dna_str_2):
        return 0

    hamming_distance = 0

    for i in range(len(dna_str_1)):
        if dna_str_1[i] != dna_str_2[i]:
            hamming_distance += 1

    return hamming_distance


if __name__ == '__main__':
    # filename = "hamm_sample_data.txt"
    filename = "rosalind_hamm.txt"
    hamm_data = parse_hamm_data(filename)
    print(hamm_data)
    hamming_distance = hamm(hamm_data[0], hamm_data[1])
    print(hamming_distance)
