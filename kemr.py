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
import itertools


def kmer(FASTA_sets, kmer_num):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    kmer_composition = list()
    nucleotides = ["A", "C", "G", "T"]

    kmer_set = list(itertools.product(nucleotides, repeat=kmer_num))

    print(kmer_set)

    # build dict of all kmers
    kmer_count = dict()
    for i in kmer_set:
        kmer_count["".join(i)] = 0

    for key, value in FASTA_sets.items():
        dna_str = value
        for i in range(len(dna_str) - kmer_num):
            kmer_count[dna_str[i:i+kmer_num]] += 1
        kmer_count[dna_str[-kmer_num:]] += 1

    return kmer_count


def gc_content(string):

    string_length = len(string)
    gc_count = 0

    for i in string:
        if i == "G" or i == "C":
            gc_count += 1

    gc_pct = (gc_count/string_length) * 100

    return gc_pct


def format_output(kmer_comp):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    formatted_str = ""
    dict_len = len(kmer_comp)
    i = 0

    for key, value in kmer_comp.items():
        i += 1
        if i != dict_len:
            formatted_str += f"{value} "
        else:
            formatted_str += f"{value}\n"

    return formatted_str


if __name__ == '__main__':
    # filename = "kmer_sample_data.txt"
    filename = "rosalind_kmer.txt"
    FASTA_data = parse_gc_data(filename)
    print(FASTA_data)
    kmer_num = 4
    kmer_comp = kmer(FASTA_data, kmer_num)
    print(kmer_comp)
    print(format_output(kmer_comp))
