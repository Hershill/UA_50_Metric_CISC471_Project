"""
rna.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Transcribing DNA into RNA

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G',
and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA
string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""


from parsers import *


def rna(dna_str):
    """Return transcribed DNA

    :param dna_str: string of nucleotides
    :return: RNA transcription of the dna_str
    """

    transcribed_rna_str = dna_str

    for i in range(len(dna_str)):
        if dna_str[i] == "T":
            transcribed_rna_str = transcribed_rna_str[:i] + "U" + \
                                  transcribed_rna_str[i+1:]

    return transcribed_rna_str


if __name__ == '__main__':
    filename = "rosalind_rna_1.txt"
    dna_read = parse_dna_data(filename)
    # print(dna_str)
    transcribed_str = rna(dna_read)
    print(transcribed_str)
