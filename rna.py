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


def rna(dna_str):
    """Return dict of counts of each nucleotide in DNA set
    :param dna_str: string of nucleotides
    :return: dict of count of nucleotides
    """

    transcribed_rna_str = dna_str

    for i in range(len(dna_str)):
        if dna_str[i] == "T":
            transcribed_rna_str = transcribed_rna_str[:i] + "U" + transcribed_rna_str[i+1:]

    return transcribed_rna_str


if __name__ == '__main__':
    # filename = "rna_sample_data.txt"
    filename = "rosalind_rna.txt"
    dna_str = parse_dna_data(filename)
    print(dna_str)
    transcribed_str = rna(dna_str)
    print(transcribed_str)
