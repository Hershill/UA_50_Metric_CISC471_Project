"""
iprb_test.py file that runs the unittests for iprb.py when the file is called or
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
from iprb import iprb
from parsers import parse_iprb_data


class TestProgrammingProblemIPRB(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_iprb_positive_a(self):
        kmn = parse_iprb_data("rosalind_iprb_1.txt")
        probability = iprb(kmn[0], kmn[1], kmn[2])
        solution = 0.78333

        # make sure solution matches computed result
        self.assertEqual(solution, probability)

    def test_iprb_positive_b(self):
        kmn = parse_iprb_data("rosalind_iprb_2.txt")
        probability = iprb(kmn[0], kmn[1], kmn[2])
        solution = 0.74421

        # make sure solution matches computed result
        self.assertEqual(solution, probability)

    def test_iprb_positive_c(self):
        kmn = parse_iprb_data("rosalind_iprb_3.txt")
        probability = iprb(kmn[0], kmn[1], kmn[2])
        solution = 0.80213

        # make sure solution matches computed result
        self.assertEqual(solution, probability)

    def test_iprb_negative(self):
        kmn = parse_iprb_data("rosalind_iprb_4.txt")
        probability = iprb(kmn[0], kmn[1], kmn[2])
        solution = 0.0

        # make sure solution matches computed result
        self.assertEqual(solution, probability)


if __name__ == '__main__':
    unittest.main()
