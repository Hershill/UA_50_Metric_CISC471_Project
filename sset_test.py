"""
sset_test.py file that runs the unittests for sset.py when the file is called or
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
from sset import sset
from parsers import parse_dna_data


class TestProgrammingProblemSSET(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_sset_positive_a(self):
        sset_number = int(parse_dna_data("rosalind_sset_1.txt"))
        subsets = sset(sset_number)
        solution = 8

        # make sure solution matches computed result
        self.assertEqual(solution, subsets)

    def test_sset_positive_b(self):
        sset_number = int(parse_dna_data("rosalind_sset_2.txt"))
        subsets = sset(sset_number)
        solution = 409856

        # make sure solution matches computed result
        self.assertEqual(solution, subsets)

    def test_sset_positive_c(self):
        sset_number = int(parse_dna_data("rosalind_sset_3.txt"))
        subsets = sset(sset_number)
        solution = 923136

        # make sure solution matches computed result
        self.assertEqual(solution, subsets)

    def test_sset_negative(self):
        sset_number = int(parse_dna_data("rosalind_sset_4.txt"))
        subsets = sset(sset_number)
        solution = 1

        # make sure solution matches computed result
        self.assertEqual(solution, subsets)


if __name__ == '__main__':
    unittest.main()
