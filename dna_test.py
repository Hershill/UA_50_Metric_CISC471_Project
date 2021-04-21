"""
dna_test.py file that runs the unittests for dna.py when the file is called or
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
from dna import dna
from parsers import parse_dna_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_dna_positive_a(self):
        dna_read = parse_dna_data("rosalind_dna_1.txt")
        dna_counts = dna(dna_read)
        solution = {'A': 20, 'C': 12, 'G': 17, 'T': 21}

        # make sure solution matches computed result
        self.assertEqual(solution, dna_counts)

    def test_dna_positive_b(self):
        dna_read = parse_dna_data("rosalind_dna_2.txt")
        dna_counts = dna(dna_read)
        solution = {'A': 197, 'C': 222, 'G': 181, 'T': 212}

        # make sure solution matches computed result
        self.assertEqual(solution, dna_counts)

    def test_dna_positive_c(self):
        dna_read = parse_dna_data("rosalind_dna_3.txt")
        dna_counts = dna(dna_read)
        solution = {'A': 235, 'C': 232, 'G': 272, 'T': 250}

        # make sure solution matches computed result
        self.assertEqual(solution, dna_counts)

    def test_dna_negative(self):
        dna_read = parse_dna_data("rosalind_dna_4.txt")
        dna_counts = dna(dna_read)
        solution = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        # make sure solution matches computed result
        self.assertEqual(solution, dna_counts)


if __name__ == '__main__':
    unittest.main()
