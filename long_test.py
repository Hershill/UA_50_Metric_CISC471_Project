"""
long_test.py file that runs the unittests for long.py when the file is called or
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
from long import long
from parsers import parse_gc_data, parse_single_line_sol_data


class TestProgrammingProblemlong(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_long_positive_a(self):
        long_data = parse_gc_data("rosalind_long_1.txt")
        superstring = long(long_data)
        solution = "ATTAGACCTGCCGGAATAC"

        # make sure solution matches computed result
        self.assertEqual(solution, superstring)

    def test_long_positive_b(self):
        long_data = parse_gc_data("rosalind_long_2.txt")
        superstring = long(long_data)
        solution = parse_single_line_sol_data("rosalind_long_2_sol.txt")

        # make sure solution matches computed result
        self.assertEqual(solution, superstring)

    def test_long_positive_c(self):
        long_data = parse_gc_data("rosalind_long_3.txt")
        superstring = long(long_data)
        solution = parse_single_line_sol_data("rosalind_long_3_sol.txt")

        # make sure solution matches computed result
        self.assertEqual(solution, superstring)

    def test_long_negative(self):
        long_data = parse_gc_data("rosalind_long_4.txt")
        superstring = long(long_data)
        solution = ""

        # make sure solution matches computed result
        self.assertEqual(solution, superstring)


if __name__ == '__main__':
    unittest.main()
