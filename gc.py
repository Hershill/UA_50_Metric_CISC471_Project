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


def gc(FASTA_sets):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    # set up dict for A, C, G, T
    count = {
        "A": 0, "C": 0, "G": 0, "T": 0
    }

    max_gc = dict()

    for key, value in FASTA_sets.items():
        max_gc[key] = gc_content(value)

    print(max_gc)

    return [max(max_gc, key=max_gc.get), max_gc[max(max_gc, key=max_gc.get)]]


def gc_content(string):

    string_length = len(string)
    gc_count = 0

    for i in string:
        if i == "G" or i == "C":
            gc_count += 1

    gc_pct = (gc_count/string_length) * 100

    return gc_pct


def format_output(max_gc_content):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_content[0]}\n{max_gc_content[1]}"

    return formatted_str


if __name__ == '__main__':
    # filename = "gc_sample_data.txt"
    filename = "rosalind_gc.txt"
    FASTA_data = parse_gc_data(filename)
    print(FASTA_data)
    max_gc_content = gc(FASTA_data)
    print(max_gc_content)
    print(format_output(max_gc_content))
