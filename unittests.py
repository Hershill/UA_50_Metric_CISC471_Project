"""
main.py file that runs the unittests when the file is called or run using the python CLI.

Unit tests for N50 algorithm for the Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)


There are two ways to run the program, outlined below. Both methods run the unittests.
Sample Usage:
  $ python -m unittest unittests.py
  $ python -m main main.py
"""

import unittest
from asqm import *


class TestN50Algorithm(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_nxx_positive(self):
        # N50 Test
        file = "sample_data.txt"
        contig_set = parse_data(file)
        n50_score = nxx(contig_set, 50)

        # make sure solution matches computed result
        self.assertEqual(n50_score, 7)

        # N75 Test
        file = "sample_data.txt"
        contig_set = parse_data(file)
        n75_score = nxx(contig_set, 75)

        # make sure solution matches computed result
        self.assertEqual(n75_score, 6)

    def test_n50_negative(self):
        # N50 Test
        file = "sample_data_negative.txt"
        contig_set = parse_data(file)
        n50_score = nxx(contig_set, 50)

        # make sure solution matches computed result
        self.assertEqual(n50_score, 0)

        # N75 Test
        file = "sample_data_negative.txt"
        contig_set = parse_data(file)
        n75_score = nxx(contig_set, 75)

        # make sure solution matches computed result
        self.assertEqual(n75_score, 0)


if __name__ == '__main__':
    unittest.main()
