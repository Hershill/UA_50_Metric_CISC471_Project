"""
revc.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Complementing a Strand of DNA

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C'
and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing
the symbols of s, then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

from parsers import parse_dna_data


def revc(dna):
    """Returns the reverse complement of a given DNA string of length at most
    1000bp

    :param dna: a string of DNA
    :return: the reverse complement of that string of DNA
    """

    reverse_complement = ""
    reversed_dna = dna[::-1]

    for n in reversed_dna:
        if n == "A":
            reverse_complement = reverse_complement + "T"
        elif n == "T":
            reverse_complement = reverse_complement + "A"
        elif n == "G":
            reverse_complement = reverse_complement + "C"
        elif n == "C":
            reverse_complement = reverse_complement + "G"

    return reverse_complement


if __name__ == '__main__':
    filename = "rosalind_revc_1.txt"
    dna_str = parse_dna_data(filename)
    print(dna_str)
    rev_complement = revc(dna_str)
    print(rev_complement)
