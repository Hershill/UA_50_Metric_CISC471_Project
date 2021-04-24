"""
subs.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

from parsers import parse_subs_data


def subs(dna_s, dna_t):
    """Return all location of substring dna_t in dna_s

    :param dna_s: reference DNA string
    :param dna_t: DNA subset
    :return: indices of dna_t occuring in dna_s
    """

    len_s = len(dna_s)
    len_t = len(dna_t)

    matched_indices = list()

    for i in range(len_s - len_t):
        dna_s_slice = dna_s[i: i+len_t]
        if dna_s_slice == dna_t:
            matched_indices.append(i + 1)

    return matched_indices


def format_output(indices_list):
    """Format output according to problem requirement

    :param indices_list: list of indices
    :return: formatted string output of results
    """

    if not indices_list:
        return ""

    formatted_str = ""

    for i in range(len(indices_list) - 1):
        formatted_str += f"{indices_list[i]} "
    formatted_str += f"{indices_list[-1]}"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_subs_3.txt"
    subs_data = parse_subs_data(filename)
    # print(subs_data)
    subs_indices = subs(subs_data[0], subs_data[1])
    # print(subs_indices)
    print(format_output(subs_indices))
