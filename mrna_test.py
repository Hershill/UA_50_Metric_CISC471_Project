"""
mrna_test.py file that runs the unittests for mrna.py when the file is called or
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
from mrna import mrna
from parsers import parse_dna_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_mrna_positive_a(self):
        mrna_data = parse_dna_data("rosalind_mrna_1.txt")
        combinations = mrna(mrna_data)
        solution = 12

        # make sure solution matches computed result
        self.assertEqual(solution, combinations)

    def test_mrna_positive_b(self):
        mrna_data = parse_dna_data("rosalind_mrna_2.txt")
        combinations = mrna(mrna_data)
        solution = 345152

        # make sure solution matches computed result
        self.assertEqual(solution, combinations)

    def test_mrna_positive_c(self):
        mrna_data = parse_dna_data("rosalind_mrna_3.txt")
        combinations = mrna(mrna_data)
        solution = 333056

        # make sure solution matches computed result
        self.assertEqual(solution, combinations)

    def test_mrna_negative(self):
        mrna_data = parse_dna_data("rosalind_mrna_4.txt")
        combinations = mrna(mrna_data)
        solution = 0

        # make sure solution matches computed result
        self.assertEqual(solution, combinations)


if __name__ == '__main__':
    unittest.main()
