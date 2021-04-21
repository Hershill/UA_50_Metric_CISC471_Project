"""
gc.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in
all decimal answers unless otherwise stated; please see the note on absolute
error below.
"""

from parsers import parse_gc_data


def gc(FASTA_sets):
    """Return the DNA set that has the greatest GC-content

    :param FASTA_sets: FASTA formatted sets of data as a dictionary
    :return: the DNA strand with the greatest GC%-content
    """

    if not FASTA_sets:
        return [str(), int()]

    max_gc = dict()

    for key, value in FASTA_sets.items():
        max_gc[key] = gc_content(value)

    return [max(max_gc, key=max_gc.get), max_gc[max(max_gc, key=max_gc.get)]]


def gc_content(string):
    """Calculate the GC-content of a given DNA string

    :param string: a DNA string
    :return: the GC-content of the given DNA string
    """
    string_length = len(string)
    gc_count = 0

    for i in string:
        if i == "G" or i == "C":
            gc_count += 1

    gc_pct = (gc_count/string_length) * 100

    return gc_pct


def format_output(max_gc_str):
    """ Format output according to problem requirement

    :param max_gc_str: list of data of mac GC-content DNA string
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_str[0]}\n{max_gc_str[1]}"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_gc_4.txt"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    max_gc_content = gc(FASTA_data)
    # print(max_gc_content)
    print(format_output(max_gc_content))
