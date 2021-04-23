"""
dbru.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Constructing a De Bruijn Graph

Given: A collection of up to 1000 (possibly repeating) DNA strings of equal
length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding
to S∪Src.
"""

from revc import revc
from parsers import parse_subs_data


def dbru(dbru_set, incl_revc=True):
    """Return the adjacency list corresponding to the de Bruijn graph of the
    union of the set of contigs and their reverse complements

    :param dbru_set: string of nucleotides
    :param incl_revc: boolean to set whether to include the reverse complements
    :return: an adjacency list
    """

    # base case
    if not dbru_set:
        return []

    k_1 = len(dbru_set[0]) - 1

    # all unique (k−1)-mers occurring as a prefix or suffix in dbru_set
    # create set of (k-1)-mers occurring as a prefix or suffix of contigs in
    # dbru_set

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
    """Format output according to problem requirement

    :param dbru_graph: list
    :return: formatted string output of results
    """

    formatted_str = ""

    for tup in dbru_graph:
        formatted_str += f"({tup[0]}, {tup[1]})\n"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_dbru_3.txt"
    dbru_data = parse_subs_data(filename)
    # print(dbru_data)
    dbru_graph = dbru(dbru_data)
    # print(dbru_graph)
    print(format_output(dbru_graph))
