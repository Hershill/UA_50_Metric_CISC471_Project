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
import copy


def dbru(dbru_set):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    dbru_graph = list()
    k_1 = len(dbru_set[0]) - 1

    # all unique (k−1)-mers occurring as a prefix or suffix in dbru_set
    # create set of (k-1)-mers occurring as a prefix or suffix of contigs in dbru_set

    prefixes_suffixes = list()

    for i in dbru_set:
        prefix = i[:k_1]
        suffix = i[-k_1:]
        if prefix not in prefixes_suffixes:
            prefixes_suffixes.append(prefix)
        if suffix not in prefixes_suffixes:
            prefixes_suffixes.append(suffix)
    
    prefixes_suffixes_copy = copy.deepcopy(prefixes_suffixes)

    for i in prefixes_suffixes:
        suffix_overlap = i[len(i) - 2:]
        for k in prefixes_suffixes_copy:
            prefix_overlap = k[:len(i) - 1]
            if suffix_overlap == prefix_overlap:
                dbru_graph.append((i, k))

    return dbru_graph


def gc_content(string):

    string_length = len(string)
    gc_count = 0

    for i in string:
        if i == "G" or i == "C":
            gc_count += 1

    gc_pct = (gc_count/string_length) * 100

    return gc_pct


def format_output(dbru_graph):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in dbru_graph:
        formatted_str += f"{i}\n"

    return formatted_str


if __name__ == '__main__':
    filename = "dbru_sample_data.txt"
    # filename = "rosalind_gc.txt"
    dbru_data = parse_subs_data(filename)
    # print(dbru_data)
    dbru_graph = dbru(dbru_data)
    # print(dbru_graph)
    print(format_output(dbru_graph))
