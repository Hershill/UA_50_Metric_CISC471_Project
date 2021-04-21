"""
rna_test.py file that runs the unittests for dna.py when the file is called or run using the python CLI.

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

There are two ways to run the program, outlined below. Both methods run the unittests.
Sample Usage:
  $ python -m unittest dna_test.py
  $ python -m main main.py
"""

import unittest
from rna import rna
from parsers import parse_dna_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_rna_positive_a(self):
        dna_read = parse_dna_data("rosalind_rna_1.txt")
        rna_str = rna(dna_read)
        solution = "GAUGGAACUUGACUACGUAAAUU"

        # make sure solution matches computed result
        self.assertEqual(solution, rna_str)

    def test_rna_positive_b(self):
        dna_read = parse_dna_data("rosalind_rna_2.txt")
        rna_str = rna(dna_read)
        solution = "GGUUAUGCCCUGGUACUCGUGAUGUCGACUCCAAGCUCAGCAGAUGGGUAUACGCAC" \
                   "CAAAAUGCCACCCAAAGGCGCUUGGUGAAGCCGAGAUAAUGUUUUCCCGUAUAUGAG" \
                   "ACACUGGCGCGGUUCUAGGCGACUUGCGUGCGAUGCAGACUUUCCUAGACCGCCCUA" \
                   "GACUAAGCGGAGAAGGAUACAUCUGUUUCCGUAGUCUAUAAACGCGAGGCUUCCACU" \
                   "CCCUGCCGGCCGUUAGUGCGCGACCUUUUUGUUUGGGAGUCGGGCCUUAUACCUACU" \
                   "AUGGCAUCAGAUGCGUUGGCGGAGAGGUAAUAUAUGCAGAAUUAUGGCCACUUGUUG" \
                   "AGUUUCGCUAGGAGCACAAAGUUACGUACAGGCGAGUCAAAGUGGUUUUAUGCGUUA" \
                   "GUUGAGGAGUCAAUCAGCUUAUGAUAAUUUCAUUUACCGGAAAAUAACGACUAAUGC" \
                   "UGAGACACGCCGGUAUCCAAUAUCCCCUUAAAGUCCCGGGAUUUGAUUAUGUCUCGG" \
                   "CUACCACCACGAGACGAAGUGCAUCAGUUUAGUAAGCCGAUUCCGGAAGAAUUUGAC" \
                   "AGAUCGAGAACUUGCCAAAGAGAAGUCACAAUACCGUUGUACCUUAGUGUAUUCAUU" \
                   "GUCGCUUUGGCCUGGACAUCUUUAAGCACUAGGGCAGUUGUGCCAUAGAGACCGACA" \
                   "GUGCUAUCGACCUUCAUGGUCGUGUGCAAUACUGGCUAACAGAUAUGGCCGAAUCUG" \
                   "ACGCGUCGACCGCUUACGUUAUAGUAGUUUCGGAAUAGUGGUGGAGGGGGCCCAAGA" \
                   "ACUGUAGAGUUGUUCCACCGAAGGCCUAAGUCCCUAGGAGGUGACCCGGGCACGGCG" \
                   "CGCACUUAUACAUGAAUGUUGUGAGCAGUUUGCCGAGCUAGACGCGCGGGACGGUGU" \
                   "AUGACACCGCCUACAUGUGUAGUGUCCGGGCCCCCCUGGAGCUCAGUCGGGCUCCGA" \
                   "GCAG"

        # make sure solution matches computed result
        self.assertEqual(solution, rna_str)

    def test_rna_positive_c(self):
        dna_read = parse_dna_data("rosalind_rna_3.txt")
        rna_str = rna(dna_read)
        solution = "AGGGGAUAUUUAGUCUCAUUCCGGUGCCGCGUUUCGGUACAGUACGAUUUGCCCGGU" \
                   "AUCACCGUCCCGCCCGCCACAUUUCCAUGAAUCAUUGGUUGCUUUUGAGUAGCGGUU" \
                   "GACACGCGAUAGUGAGCACCAUGGACAUGGAGGUGUUUGUCACCCAUCUACGAUAGU" \
                   "GAGGUCCACUUUGCACCCUGCUAAUCCCACCAGAGCUUCGUCACUUAUAGGCGUGUG" \
                   "GAUUUUGGGAGUUAGAUGAACGAUAUUCCGGUUCAGGAAAUGAACGAAGCCCCAUAU" \
                   "UACUCUUCGAACCCGAUCGGCCCACGUGACCCGUAACGAGAGUAGCUCAUUCCGUUU" \
                   "GUUCGAGAUUCGUGCAACGUGGUCACCACUACCGAGUGAUUCAAGUCGCAUAACAUU" \
                   "UUAGCUCUGCGCUACUUCACGGUCGUCGCGGAUUUCGUGUGACCCCUAGUGCCCACA" \
                   "UGCUGGAGCGAAAAUCGUAAACACCUAGGGGACCAUUCGUCCCCGCUGUGUCAGUAU" \
                   "CACCUUCAGUUAGCUAGACGUGCUAGGACUUCAAGCACUUGCGGGAGUCGAAGUGAU" \
                   "AGAAUUACGAGUCACCCUGAUUAAGAUUGAACCUAUGGCACCCAAUACACGCUAACG" \
                   "AUUGAACUCGAAUUCUACUCGAGAUGUUAUGUGCAGUCAGUAUCCAGAUUGCGCUAG" \
                   "CGGCGCUUUUCACACUAGCGUGGGUUGUGGACUUCAACCGAUCAGUCCACCGGAUGG" \
                   "GCCCUAUUAUAGCACUUGGGUCUCUGCAAGCGGCUAUUACCUCUGACCUUUAGUUGG" \
                   "ACUCUUCAUAAGUGGGUGCAUAAUUUAAGUUAAUGGAGUAUGGUGCGUAAAAAGCAG" \
                   "CACGGGACCGGACAAAGGCGGUGAAUUGAGUCCCACCCGUUUGACCGCUGG"

        # make sure solution matches computed result
        self.assertEqual(solution, rna_str)

    def test_dna_negative(self):
        dna_read = parse_dna_data("rosalind_rna_4.txt")
        rna_str = rna(dna_read)
        solution = ""

        # make sure solution matches computed result
        self.assertEqual(solution, rna_str)


if __name__ == '__main__':
    unittest.main()
