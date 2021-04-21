"""
perm.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Enumerating Gene Orders

Problem

A permutation of length n is an ordering of the positive integers {1,2,…,
n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of
all such permutations (in any order).
"""

from parsers import parse_dna_data
import itertools


def perm(input_num):
    """Return the number of permutations of a set of length input_num

    :param input_num: length of permutation
    :return: number of permutation for a set of size input_num
    """

    perms = list()

    if input_num > 7:
        return perms

    number_set = list(range(1, input_num + 1))
    perms = list(itertools.permutations(number_set))

    return perms


def format_output(permutation_set):
    """Format output according to problem requirement

    :param permutation_set: list of tuples containing all sets of permutations
    :return: formatted string output of results
    """

    formatted_str = f"{len(permutation_set)}\n"

    for i in permutation_set:
        for nums in i:
            formatted_str += f"{nums} "
        formatted_str += "\n"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_perm_2.txt"
    perm_number = int(parse_dna_data(filename))
    # print(perm_number)
    permutations = perm(perm_number)
    print(permutations)
    # print(format_output(permutations))
