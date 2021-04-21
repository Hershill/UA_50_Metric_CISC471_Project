"""
prot.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)


Translating RNA into Protein

Problem The 20 commonly occurring amino acids are abbreviated by using 20
letters from the English alphabet (all letters except for B, J, O, U, X,
and Z). Protein strings are constructed from these 20 symbols. Henceforth,
the term genetic string will incorporate protein strings along with DNA
strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most
10 kbp).

Return: The protein string encoded by s.
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


def prot(rna):
    """Read RNA sequences 3 at time and maps to the amino acid that the RNA
    sequence codes for

    :param rna: RNA string to translate :return: the RNA sequence translated
                    into it's Amino Acid sequence or Peptide string
    """

    # if the length of the RNA string to translate is less than 3, we cannot
    # translate it into an amino acid
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


if __name__ == '__main__':
    filename = "rosalind_prot_1.txt"
    # filename = "rosalind_prot.txt"
    rna_string = parse_dna_data(filename)
    # print(rna_string)
    peptide = prot(rna_string)
    print(peptide)
