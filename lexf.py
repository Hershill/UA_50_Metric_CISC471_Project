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


def lexf(alphabet, num):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    lexf_product = list()
    alphabet_list = alphabet.split(" ")

    lexf_product = list(itertools.product(alphabet_list, repeat=num))

    return lexf_product


def format_output(lexf_data):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in lexf_data:
        for nums in i:
            formatted_str += f"{nums}"
        formatted_str += "\n"

    return formatted_str


if __name__ == '__main__':
    # filename = "lexf_sample_data.txt"
    filename = "rosalind_lexf.txt"
    lexf_data = parse_lexf_data(filename)
    # print(lexf_data)
    lexf_set = lexf(lexf_data[0], int(lexf_data[1]))
    # print(lexf_set)
    print(format_output(lexf_set))
