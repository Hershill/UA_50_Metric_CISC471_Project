"""
kmer.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

k-Mer Composition

Problem

For a fixed positive integer k, order all possible k-mers taken from an
underlying alphabet lexicographically.

Then the k-mer composition of a string s can be represented by an array A for
which A[m] denotes the number of times that the mth k-mer (with respect to
the lexicographic order) appears in s.

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
"""

from parsers import parse_gc_data
import itertools


def kmer(FASTA_sets, kmer_num):
    """Return dict of counts of each k-mer in a DNA string

    :param FASTA_sets: string of DNA in FASTA format
    :param kmer_num: k-mer number to use
    :return: dict of count of k-mer composition of DNA
    """

    # base case
    if FASTA_sets == {}:
        return {}

    kmer_comp = list()
    nucleotides = ["A", "C", "G", "T"]

    kmer_set = list(itertools.product(nucleotides, repeat=kmer_num))

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


def format_output(kmer_comp):
    """Format output according to problem requirement

    :param kmer_comp: dictionary of the counts of k-mer compositions
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
    filename = "rosalind_kmer_3.txt"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    kmer_num = 4
    kmer_composition = kmer(FASTA_data, kmer_num)
    print(kmer_composition)
    print(format_output(kmer_composition))
