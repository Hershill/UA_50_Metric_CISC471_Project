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


def perm(input_num):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    permutations = list()

    if input_num > 7:
        return permutations

    number_set = list(range(1, input_num + 1))
    permuations = list(itertools.permutations(number_set))

    return permuations


def format_output(permutation_set):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = f"{len(permutation_set)}\n"

    for i in permutation_set:
        for nums in i:
            formatted_str += f"{nums} "
        formatted_str += "\n"

    return formatted_str


if __name__ == '__main__':
    # filename = "perm_sample_data.txt"
    filename = "rosalind_perm.txt"
    perm_number = int(parse_dna_data(filename))
    # print(perm_number)
    permutation_set = perm(perm_number)
    # print(permutation_set)
    print(format_output(permutation_set))
