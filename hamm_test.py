"""
hamm_test.py file that runs the unittests for hamm.py when the file is called or
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
from hamm import hamm
from parsers import parse_hamm_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_hamm_positive_a(self):
        hamming_data = parse_hamm_data("rosalind_hamm_1.txt")
        hamming_distance = hamm(hamming_data[0], hamming_data[1])
        solution = 7

        # make sure solution matches computed result
        self.assertEqual(solution, hamming_distance)

    def test_hamm_positive_b(self):
        hamming_data = parse_hamm_data("rosalind_hamm_2.txt")
        hamming_distance = hamm(hamming_data[0], hamming_data[1])
        solution = 499

        # make sure solution matches computed result
        self.assertEqual(solution, hamming_distance)

    def test_hamm_positive_c(self):
        hamming_data = parse_hamm_data("rosalind_hamm_3.txt")
        hamming_distance = hamm(hamming_data[0], hamming_data[1])
        solution = 471

        # make sure solution matches computed result
        self.assertEqual(solution, hamming_distance)

    def test_hamm_negative(self):
        hamming_data = parse_hamm_data("rosalind_hamm_4.txt")
        hamming_distance = hamm(hamming_data[0], hamming_data[1])
        solution = 0

        # make sure solution matches computed result
        self.assertEqual(solution, hamming_distance)


if __name__ == '__main__':
    unittest.main()
