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


def tree(num_nodes, graph_data):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    graph_data_ints = list()
    set_range = list(range(1, num_nodes + 1))
    node_set = list()

    node_count = 0
    num_edges = 0

    for i in graph_data:
        graph_data_ints.append([int(k) for k in i])

    for i in graph_data_ints:
        num_edges += 1
        if i[0] not in node_set:
            node_set.append(i[0])
        if i[1] not in node_set:
            node_set.append(i[1])

    node_set = sorted(node_set)

    for i in set_range:
        if i not in node_set:
            node_count += 1

    missing_nodes = num_nodes - num_edges - 1

    return missing_nodes


def format_output(max_gc_content):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_content[0]}\n{max_gc_content[1]}"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_tree.txt"
    # filename = "rosalind_gc.txt"
    tree_data = parse_tree_data(filename)
    print(tree_data)
    missing_nodes = tree(int(tree_data[0]), tree_data[1:])
    print(missing_nodes)
