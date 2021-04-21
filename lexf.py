"""
lexf.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Enumerating k-mers Lexicographically

Given: A collection of at most 10 symbols defining an ordered alphabet,
and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically (use the standard order of symbols in the English
alphabet).
"""

from parsers import parse_lexf_data
import itertools


def lexf(alphabet, num):
    """Return dict of counts of each nucleotide in DNA set

    :param alphabet: set of letters to be used as the alphabet set
    :param num: length of words to permute based on given alphabet
    :return: list of tuples of words of length num given alphabet
    """

    lexf_product = list()
    alphabet_list = alphabet.split(" ")

    lexf_product = list(itertools.product(alphabet_list, repeat=num))

    return lexf_product


def format_output(lexf_data):
    """Format output according to problem requirement

    :param lexf_data: list of tuples of word combinations
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in lexf_data:
        for nums in i:
            formatted_str += f"{nums}"
        formatted_str += "\n"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_lexf_2.txt"
    lexf_data = parse_lexf_data(filename)
    # print(lexf_data)
    lexf_set = lexf(lexf_data[0], int(lexf_data[1]))
    print(lexf_set)
    # print(format_output(lexf_set))
