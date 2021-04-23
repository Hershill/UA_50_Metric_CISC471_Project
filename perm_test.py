"""
perm_test.py file that runs the unittests for perm.py when the file is called or
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
import ast
from perm import perm, format_output
from parsers import parse_dna_data, parse_single_line_sol_data


class TestProgrammingProblemPERM(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_perm_positive_a(self):
        permutation_number = int(parse_dna_data("rosalind_perm_1.txt"))
        permutations_raw = perm(permutation_number)
        permutation_formatted = format_output(permutations_raw)

        solution_raw = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2),
                        (3, 2, 1)]
        solution_formatted = "6\n1 2 3 \n1 3 2 \n2 1 3 \n2 3 1 \n3 1 2 " \
                             "\n3 2 1 \n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, permutations_raw)
        self.assertEqual(solution_formatted, permutation_formatted)

    def test_perm_positive_b(self):
        permutation_number = int(parse_dna_data("rosalind_perm_2.txt"))
        permutations_raw = perm(permutation_number)
        permutation_formatted = format_output(permutations_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_perm_2_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, permutations_raw)
        self.assertEqual(solution_formatted, permutation_formatted)

    def test_perm_positive_c(self):
        permutation_number = int(parse_dna_data("rosalind_perm_3.txt"))
        permutations_raw = perm(permutation_number)
        permutation_formatted = format_output(permutations_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_perm_3_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, permutations_raw)
        self.assertEqual(solution_formatted, permutation_formatted)

    def test_perm_negative(self):
        permutation_number = int(parse_dna_data("rosalind_perm_4.txt"))
        permutations_raw = perm(permutation_number)
        permutation_formatted = format_output(permutations_raw)

        solution_raw = [()]
        solution_formatted = "1\n\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, permutations_raw)
        self.assertEqual(solution_formatted, permutation_formatted)


if __name__ == '__main__':
    unittest.main()
