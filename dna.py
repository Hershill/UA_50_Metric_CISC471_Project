"""
dna.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Counting DNA Nucleotides Problem

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""


from parsers import parse_dna_data


def dna(dna_str):
    """Return dict of counts of each nucleotide in DNA set

    :param dna_str: string of nucleotides
    :return: dict of count of nucleotides
    """

    # set up dict for A, C, G, T
    count = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nucleotide in dna_str:
        count[nucleotide] += 1

    return count


def format_output(counts_data):
    """ Format output according to problem requirement

    :param counts_data: dict of counts of nucleotides
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{counts_data['A']} {counts_data['C']} " \
                    f"{counts_data['G']} {counts_data['T']}"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_dna_1.txt"
    dna_read = parse_dna_data(filename)
    # print(dna_read)
    counts = dna(dna_read)
    # print(counts)
    print(format_output(counts))
