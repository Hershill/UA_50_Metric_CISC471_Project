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


from enum import Enum
from parsers import *


# Enum for storing mapping of string sequences and coding Amino Acids
class RNACoding(Enum):
    """Enum that stores mapping data for RNA sequences to Amino Acids - the genetic code
    """
    UU = {"U": "F", "C": "F", "A": "L", "G": "L"}
    CU = {"U": "L", "C": "L", "A": "L", "G": "L"}
    AU = {"U": "I", "C": "I", "A": "I", "G": "M"}
    GU = {"U": "V", "C": "V", "A": "V", "G": "V"}
    UC = {"U": "S", "C": "S", "A": "S", "G": "S"}
    CC = {"U": "P", "C": "P", "A": "P", "G": "P"}
    AC = {"U": "T", "C": "T", "A": "T", "G": "T"}
    GC = {"U": "A", "C": "A", "A": "A", "G": "A"}
    UA = {"U": "Y", "C": "Y", "A": "*", "G": "*"}
    CA = {"U": "H", "C": "H", "A": "Q", "G": "Q"}
    AA = {"U": "N", "C": "N", "A": "K", "G": "K"}
    GA = {"U": "D", "C": "D", "A": "E", "G": "E"}
    UG = {"U": "C", "C": "C", "A": "*", "G": "W"}
    CG = {"U": "R", "C": "R", "A": "R", "G": "R"}
    AG = {"U": "S", "C": "S", "A": "R", "G": "R"}
    GG = {"U": "G", "C": "G", "A": "G", "G": "G"}


def parse_data(filename):
    """Read in the RNA sequence data from a file

    :param filename: file containing RNA sequence
    :return: RNA sequence as a string
    """
    with open(filename) as file:
        data_set = file.read().replace("\n", "")
    return data_set


def prot(rna):
    """Read RNA sequences 3 at time and maps to the amino acid the RNA sequence codes for

    :param rna: RNA string to translate
    :return: the RNA sequence translated into it's Amino Acid sequence or Peptide string
    """

    # if the length of the RNA string to translate is less than 3, we cannot translate it into an amino acid
    if len(rna) < 3:
        return None

    rna_three_mers = list()
    amino_seq = ""

    for i in range(0, len(rna) - 3, 3):
        rna_three_mers.append(rna[i:i + 3])
    rna_three_mers.append(rna[-3:])

    # takes codons and translate into amino acids/peptide sequence
    for rna_seq in rna_three_mers:
        amino_acid = RNACoding[rna_seq[0:2]].value[rna_seq[2]]
        if amino_acid == "*":  # if we reach a stop codon, terminate translation
            return amino_seq
        amino_seq += RNACoding[rna_seq[0:2]].value[rna_seq[2]]

    return amino_seq


def format_output(max_gc_content):
    """ Format output according to problem requirement

    :param max_gc_content: list
    :return: formatted string output of results
    """

    # append to string
    formatted_str = f"{max_gc_content[0]}\n{max_gc_content[1]}"

    return formatted_str


if __name__ == '__main__':
    filename = "prot_sample_data.txt"
    # filename = "rosalind_prot.txt"
    rna_string = parse_dna_data(filename)
    print(rna_string)
    peptide = prot(rna_string)
    print(peptide)
    # print(format_output(max_gc_content))
