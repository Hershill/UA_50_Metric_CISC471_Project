"""
grph.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at
most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any
order.
"""

from parsers import parse_gc_data


def grph(FASTA_sets):
    """Return adjacency list corresponding to O^3

    :param FASTA_sets: strings of nucleotides
    :return: adjacent list corresponding to O^3 of FASTA data set names
    """

    dna_names = []
    dna_strings = []
    edges = []

    for dna_name in FASTA_sets:
        dna_names.append(dna_name)

    for dna_name in FASTA_sets:
        dna_strings.append(FASTA_sets[dna_name])

    for cur_dna in dna_strings:
        suffix = cur_dna[len(cur_dna) - 3:]
        for dna1 in dna_strings:
            if dna1 != cur_dna:
                prefix = dna1[:3]
                if suffix == prefix:
                    edge = (dna_names[dna_strings.index(cur_dna)],
                            dna_names[dna_strings.index(dna1)])
                    edges.append(edge)

    return edges


def format_output(edges):
    """Format output according to problem requirement

    :param edges: list of tuples of edges
    :return: formatted string output of results
    """

    formatted_str = ""

    for edge in edges:
        formatted_str = formatted_str + f"{edge[0]} {edge[1]} \n"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_grph_3.txt"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    adj_list = grph(FASTA_data)
    # print(adj_list)
    print(format_output(adj_list))
