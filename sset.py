"""
sset.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Counting Subsets

Given: A positive integer n (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""

from parsers import parse_dna_data


def sset(input_num):
    """Return number of subsets given a set of size input_num

    :param input_num: size of a set
    :return: number of subsets of size input_num
    """

    if input_num > 1000:
        return 0

    # mod 1,000,000
    num_ssets = 2 ** input_num % 1000000

    return num_ssets


if __name__ == '__main__':
    filename = "rosalind_sset_1.txt"
    sset_number = int(parse_dna_data(filename))
    subsets = sset(sset_number)
    print(subsets)
