"""
mrna.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein
could have been translated, modulo 1,000,000. (Don't neglect the importance
of the stop codon in protein translation.)
"""

from enum import Enum
from parsers import parse_dna_data


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
    """Return the number of reverse translated potential RNA strings given a
    peptide

    :param peptide_seq: a peptide sequence as a string
    :return: number of potential RNA sequences that translate to peptide_seq
    """

    # base case
    if not peptide_seq:
        return 0

    count = 1

    for i in peptide_seq:
        count *= PeptideReverseCodingCount[i].value

    count *= PeptideReverseCodingCount["STOP"].value

    # mod 1,000,000
    count = count % 1000000

    return count


if __name__ == '__main__':
    filename = "rosalind_mrna_1.txt"
    mrna_data = parse_dna_data(filename)
    # print(mrna_data)
    combinations = mrna(mrna_data)
    print(combinations)
