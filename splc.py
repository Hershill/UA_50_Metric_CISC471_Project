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


from prot import *
from parsers import *
import copy


def splc(FASTA_sets):
    """Return dict of counts of each nucleotide in DNA set
    :param FASTA_sets: string of nucleotides
    :return: dict of count of nucleotides
    """

    max_gc = dict()

    for key, value in FASTA_sets.items():
        max_gc[key] = gc_content(value)

    print(max_gc)

    return [max(max_gc, key=max_gc.get), max_gc[max(max_gc, key=max_gc.get)]]


def get_rna_and_introns(FASTA_data_set):

    FASTA_data_set_copy = copy.deepcopy(FASTA_data_set)

    rna = ""
    introns = list()

    rna = sorted(FASTA_data_set_copy.values(), key=len)[-1]
    # rna = FASTA_data_set_copy[rna_key]
    #
    # del FASTA_data_set_copy[rna_key]

    for key, value in FASTA_data_set_copy.items():
        if value != rna:
            introns.append(value)

    return rna, introns


def splice_rna(rna, introns):
    spliced_rna = rna
    for i in introns:
        index = spliced_rna.find(i)
        spliced_rna = spliced_rna[:index] + spliced_rna[index + len(i): ]

    return spliced_rna


def convert_dna_to_rna(dna):
    return dna.replace("T", "U")


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
    filename = "splc_sample_data.txt"
    # filename = "rosalind_splc.txt"
    # solution:     rna = "AUGUACAGUAAGACUCGAGCUGUAACGCAUGAUACAGUCAUGUACACAUCUGAAAGUUUAGAACAUCAGGCAUAUAUUCAUGCAUGGUGCAUGACAAAGCUCGUAGCUCUUUUGGUACGGAACUCCACCGGGCAAGCUUCAGCCAAAUGGGACUCGGGAGAAAGAUAUCCAGACAGCCCGGAAGGACACGUACCCAGGAGGUACUUGUUAUCCUUAGCUCUGAGCGGCAGGAAAAUUUCUCAAAUUCUGAAUGAAGCAGGGGGAUGCGUAGCCCGUCUUUACCCAUUUAUAUACUCUACGCGAAAGGAAGUGCACGAUGAAGAUGUUAUGAUUGCAAGUGGUGCAGACCAGAUAAGGGACUUCUUUAAGAUGAACGGCAACCUAUGCGGCUCAACCCCGCCUGAGCCGCCCAACUGUUAUACGCAUCGGAGUGUCAUAUGUUUAAUAGCGGUUCCUAGCGUGAGAAGAGGGAGGUGA"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    rna, introns = get_rna_and_introns(FASTA_data)
    # print(rna)
    # print(introns)
    rna_spliced = splice_rna(rna, introns)
    # print(rna_spliced)
    rna_converted = convert_dna_to_rna(rna_spliced)
    # print(rna_converted)
    peptide = prot(rna_converted)
    print(peptide)
