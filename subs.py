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


def subs(dna_s, dna_t):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    len_s = len(dna_s)
    len_t = len(dna_t)

    matched_indices = list()

    for i in range(len_s - len_t):
        dna_s_slice = dna_s[i: i+len_t]
        if dna_s_slice == dna_t:
            matched_indices.append(i + 1)

    return matched_indices


def format_output(subs_indices):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in range(len(subs_indices) - 1):
        formatted_str += f"{subs_indices[i]} "
    formatted_str += f"{subs_indices[-1]}\n"

    return formatted_str


if __name__ == '__main__':
    # filename = "subs_sample_data.txt"
    filename = "rosalind_subs.txt"
    subs_data = parse_subs_data(filename)
    # print(subs_data)
    subs_indices = subs(subs_data[0], subs_data[1])
    # print(subs_indices)
    print(format_output(subs_indices))
