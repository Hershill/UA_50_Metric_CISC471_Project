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


from revc import *
from parsers import *
import copy


def dbru(dbru_set, incl_revc=True):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    k_1 = len(dbru_set[0]) - 1

    # all unique (k−1)-mers occurring as a prefix or suffix in dbru_set
    # create set of (k-1)-mers occurring as a prefix or suffix of contigs in dbru_set

    dbru_graph = list()
    revc_set = list()

    if incl_revc:
        for i in dbru_set:
            revc_set.append(revc(i))

    final_set = dbru_set + revc_set

    for i in sorted(final_set):
        prefix = i[:k_1]
        suffix = i[-k_1:]
        pre_suf_set = (prefix, suffix)

        if pre_suf_set not in dbru_graph:
            dbru_graph.append(pre_suf_set)

    return dbru_graph


def format_output(dbru_graph):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for tup in dbru_graph:
        formatted_str += f"({tup[0]}, {tup[1]})\n"

    return formatted_str


if __name__ == '__main__':
    filename = "dbru_sample_data.txt"
    # filename = "rosalind_dbru.txt"
    dbru_data = parse_subs_data(filename)
    # print(dbru_data)
    dbru_graph = dbru(dbru_data)
    # print(dbru_graph)
    print(format_output(dbru_graph))
