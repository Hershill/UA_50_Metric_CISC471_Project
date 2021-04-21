"""
splc.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

RNA Splicing

Problem After identifying the exons and introns of an RNA string, we only
need to delete the introns and concatenate the exons to form a new string
ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of
substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the
exons of s. (Note: Only one solution will exist for the dataset provided.)
"""


from prot import prot
from parsers import parse_gc_data
import copy


def splc(fasta_sets):
    """Return the spliced RNA string given FASTA data

    :param FASTA_sets: FASTA set of DNA and intron data
    :return: spliced RNA string
    """

    # base case
    if not fasta_sets:
        return ""

    rna, introns = get_rna_and_introns(fasta_sets)
    rna_spliced = splice_rna(rna, introns)
    rna_converted = convert_dna_to_rna(rna_spliced)

    return rna_converted


def get_rna_and_introns(FASTA_data_set):
    """Determine the RNA and Introns from the FASTA data

    :param FASTA_data_set: FASTA data containing RNA and Intron sequences
    :return: the RNA string and list of Introns
    """

    FASTA_data_set_copy = copy.deepcopy(FASTA_data_set)

    rna = str()
    introns = list()
    rna = sorted(FASTA_data_set_copy.values(), key=len)[-1]

    for key, value in FASTA_data_set_copy.items():
        if value != rna:
            introns.append(value)

    return rna, introns


def splice_rna(rna, introns):
    """Splice the RNA given Introns

    :param rna: RNA string
    :param introns: list of Introns
    :return: the splcied RNA string
    """

    spliced_rna = rna
    for i in introns:
        index = spliced_rna.find(i)
        spliced_rna = spliced_rna[:index] + spliced_rna[index + len(i): ]

    return spliced_rna


def convert_dna_to_rna(dna):
    """Convert DNA to RNA

    :param dna: DNA string
    :return: RNA translated string
    """

    return dna.replace("T", "U")


def format_output(max_gc_content):
    """Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_content[0]}\n{max_gc_content[1]}"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_splc_4.txt"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    spliced_rna_str = splc(FASTA_data)
    peptide = prot(spliced_rna_str)
    print(peptide)
