"""
revc_test.py file that runs the unittests for revc.py when the file is called or
run using the python CLI.

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

There are two ways to run the program, outlined below. Both methods run the
unittests.

Sample Usage:
  $ python -m unittest dna_test.py
  $ python -m main main.py
"""

import unittest
from revc import revc
from parsers import parse_dna_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_revc_positive_a(self):
        dna_read = parse_dna_data("rosalind_revc_1.txt")
        revc_str = revc(dna_read)
        solution = "ACCGGGTTTT"

        # make sure solution matches computed result
        self.assertEqual(solution, revc_str)

    def test_revc_positive_b(self):
        dna_read = parse_dna_data("rosalind_revc_2.txt")
        revc_str = revc(dna_read)
        solution = "TCTTGGCTGGTGCTTATTGATCATGAGTTTGTCGATATTGCGGAAGAACAGATCAGG" \
                   "CATCGCCCCACACAAAACATTAAGAAACCATCTGAGAATGTTTTGGTTTCGGCGCGG" \
                   "TAATTCGCTAAGATCGTGCATTCCCAAACGAATTCTTCCGAAGGTGAGTTCCTAGAC" \
                   "CGGAGTACTTAGTGAATCATCTTGGCCGCTCCTCCTTGGCCTCAATTGATGGGCGTA" \
                   "CCCGCCGGCGTGGAGATGATGAACACCCAACGCGTGCGCTATGGGTGCCTAAACGTT" \
                   "TGACTTTTAGATACCCGTCCAGTTATAATCACGCGAAGTGCCGCAAGGAAATTACCC" \
                   "TCATATATCGAACGAAATGAGTAGCCACTGGTCTAATTAAGCCCCGGGCTGGTGTTG" \
                   "CTACAAATCGTGTCCGTGCGTCGCCCCCTAACCAACTCATTTGGGTACGGGCGTCGT" \
                   "AGCAACGACCTACCAAGTATACCGCACCACTTTGAACGTGATCAATACGATCATATG" \
                   "CGAAAGAAATCTGCCCTTAAGGGCGCTCGCCTCTAAGCCACTACGCCGCTACGAGCC" \
                   "AACTCCACTGCTCGTCGTTAATATTGTCGCGCCCCCGAGGGTAGGCTGGTTGCCTCT" \
                   "GCTTCCTGGCCCAGAGCGACTCTAGTTTCCGTTCTTCCGAACGTTTCTTCATACCCC" \
                   "CGCCCGGATGGACGTGCGGCTCATAGACGTATCTGGTCTTGACTCACAACATCCGTG" \
                   "TGCGCAGTTTCATTGCTGCGCGAATTGGTGGGTGGACCATCGGACCGCCTCATGTCT" \
                   "CAGTGATGCGTCCCGGCAATTGCTTACCAAGGAACGTCCTTGGGAGGAATAGACCAA" \
                   "TCCTGACATCCTACCCCAGCTCGGCTTACTAACAGATGTCAC"

        # make sure solution matches computed result
        self.assertEqual(solution, revc_str)

    def test_revc_positive_c(self):
        dna_read = parse_dna_data("rosalind_revc_3.txt")
        revc_str = revc(dna_read)
        solution = "CTACTGGATATCTTGATTTCACTCGGTCGGGCCGCAGACTAGGGTGCGTAGCTGTG" \
                   "CATTGGAACACAAACACGAAAGATTCCCGCTCGCCGCGTGCGAATGCGGCGGTGTC" \
                   "TAGAGTTGAAGAACTACTCAGTCATACGATACTTTAGAACCTATATCAAACCGCGT" \
                   "TTCAGGCTAACGGTTGCATTTCTATGAAAATCGAGCCTCTCTGGGAACTGCTATCC" \
                   "AAGTCCGCGGGACCTGGGGATGCGCTAACGTCTGGACGGACTGACGTAAGGTCGGC" \
                   "TAGAGTGGGAACTCCTATATCTACTTGCTCGTCTGGATCTGATCTATTTTACGAGT" \
                   "CGGCGCTATTGAATCCACCGCGAATACAGTTTTCGAGCGAGCAAAGCTCGTTACAA" \
                   "GACGTCACATTGAATATGGATTTGTTCGACAGTAGCTGTAGCGAGTAGATCTATTC" \
                   "AATCAAGCAGAACACCGCGACCGGTCCGTTAACAGGATTGAGACATTTAAAAGTTC" \
                   "TTCGATACCTAGCAGGTATAATCACTGGTATGTTTACATCGGGACACCCTTTGCGC" \
                   "CCTTCCAGGACATGAGGATAACGCTGACCGATAATGAAGATAATCGGGTAGGCAGT" \
                   "TACAGTAAAGATTGCGATTAACGGGCTAGGCCATCACAGATCAGGCTGTGGACCCG" \
                   "GTGGTATACACATTTGTACAGCGTCGTTAGTAGGTACAAAGAAAAACCACGCTACT" \
                   "ACAATGATGCCATAGAAGCCTGTTCTTCTGTATACGAAGTGTTTCGGAATATCCTG" \
                   "CGAATTGACGACATGAGAGCGGCAAACTCCAGTACCCGTTGATTCGGAACCGGGTC" \
                   "CAAGCCTTGCACATTCGCAGATATCAATCATGTCCCGTCCCGCAAAGATTGATATT" \
                   "ACTTATGAAGAGCTCCTTCAAAGCCAACTTATTCCGTAGACGGACCCTACCTAATC" \
                   "ATCG"

        # make sure solution matches computed result
        self.assertEqual(solution, revc_str)

    def test_revc_negative(self):
        dna_read = parse_dna_data("rosalind_revc_4.txt")
        revc_str = revc(dna_read)
        solution = ""

        # make sure solution matches computed result
        self.assertEqual(solution, revc_str)


if __name__ == '__main__':
    unittest.main()
