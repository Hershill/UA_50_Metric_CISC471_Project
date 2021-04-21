"""
hamm.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Counting Point Mutations

Problem

Given two strings s and t of equal length, the Hamming distance between s and
t, denoted dH(s,t), is the number of corresponding symbols that differ in s
and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

from parsers import parse_hamm_data


def hamm(dna_str_1, dna_str_2):
    """Return Hamming distance between two dna sets

    :param dna_str_1: string of dna
    :param dna_str_2: string of dna
    :return: the Hamming distance between dna_str_1 and dna_str_2
    """

    if len(dna_str_1) != len(dna_str_2):
        return 0

    hamm_dist = 0

    for i in range(len(dna_str_1)):
        if dna_str_1[i] != dna_str_2[i]:
            hamm_dist += 1

    return hamm_dist


if __name__ == '__main__':
    filename = "rosalind_hamm_1.txt"
    hamming_data = parse_hamm_data(filename)
    # print(hamming_data)
    hamming_distance = hamm(hamming_data[0], hamming_data[1])
    print(hamming_distance)
