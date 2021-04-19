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


def seto(num, set_a, set_b):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    all_sets = list()

    # set 1 - union
    set_1 = get_set_union(set_a, set_b)
    # print(set_1)

    # set 2 - intersect
    set_2 = get_set_intersect(set_a, set_b)
    # print(set_2)

    # set 3 and 4 - difference
    set_3 = get_set_diff(set_a, set_b)
    # print(set_3)

    set_4 = get_set_diff(set_b, set_a)
    # print(set_4)

    # set 5 and 6 - complement
    set_5 = get_set_complement(set_a, num)
    # print(set_5)

    set_6 = get_set_complement(set_b, num)
    # print(set_6)

    all_sets = [set_1, set_2, set_3, set_4, set_5, set_6]

    return all_sets


def get_set_union(a, b):
    union = list()

    for i in a:
        if i not in union:
            union.append(i)

    for i in b:
        if i not in union:
            union.append(i)

    union = sorted(union)

    return union


def get_set_intersect(a, b):
    intersect = list()

    for i in a:
        for k in b:
            if i == k:
                intersect.append(i)

    intersect = sorted(intersect)

    return intersect


def get_set_diff(a, b):
    difference = list()

    for i in a:
        if i not in b:
            difference.append(i)

    difference = sorted(difference)

    return difference


def get_set_complement(a, num):
    total_set = list(range(1, num + 1))

    complement = list()

    for i in total_set:
        if i not in a:
            complement.append(i)

    complement = sorted(complement)

    return complement


def format_output(sets):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in sets:
        formatted_str += "{"
        for k in range(len(i) - 1):
            formatted_str += f"{i[k]}, "
        formatted_str += f"{i[-1]}}}\n"

    return formatted_str


if __name__ == '__main__':
    filename = "seto_sample_data.txt"
    # filename = "rosalind_gc.txt"
    seto_data = parse_seto_data(filename)
    # print(seto_data)

    set_a = [int(i) for i in seto_data[1]]
    set_b = [int(i) for i in seto_data[2]]

    output_sets = seto(int(seto_data[0]), set_a, set_b)

    # print(output_sets)
    print(format_output(output_sets))
