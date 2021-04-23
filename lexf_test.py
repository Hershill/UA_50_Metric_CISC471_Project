"""
lexf_test.py file that runs the unittests for lexf.py when the file is called or
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
from lexf import lexf, format_output
from parsers import parse_lexf_data, parse_single_line_sol_data


class TestProgrammingProblemLEXF(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_lexf_positive_a(self):
        lexf_data = parse_lexf_data("rosalind_lexf_1.txt")
        lexf_set_raw = lexf(lexf_data[0], int(lexf_data[1]))
        lexf_set_formatted = format_output(lexf_set_raw)

        solution_raw = [('A', 'A'), ('A', 'C'), ('A', 'G'), ('A', 'T'),
                        ('C', 'A'), ('C', 'C'), ('C', 'G'), ('C', 'T'),
                        ('G', 'A'), ('G', 'C'), ('G', 'G'), ('G', 'T'),
                        ('T', 'A'), ('T', 'C'), ('T', 'G'), ('T', 'T')]

        solution_formatted = "AA\nAC\nAG\nAT\nCA\nCC\nCG\nCT\nGA\nGC\nGG\nGT" \
                             "\nTA\nTC\nTG\nTT\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, lexf_set_raw)
        self.assertEqual(solution_formatted, lexf_set_formatted)

    def test_lexf_positive_b(self):
        lexf_data = parse_lexf_data("rosalind_lexf_2.txt")
        lexf_set_raw = lexf(lexf_data[0], int(lexf_data[1]))
        lexf_set_formatted = format_output(lexf_set_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_lexf_2_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, lexf_set_raw)
        self.assertEqual(solution_formatted, lexf_set_formatted)

    def test_lexf_positive_c(self):
        lexf_data = parse_lexf_data("rosalind_lexf_3.txt")
        lexf_set_raw = lexf(lexf_data[0], int(lexf_data[1]))
        lexf_set_formatted = format_output(lexf_set_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_lexf_3_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, lexf_set_raw)
        self.assertEqual(solution_formatted, lexf_set_formatted)

    def test_lexf_negative(self):
        lexf_data = parse_lexf_data("rosalind_lexf_4.txt")
        lexf_set_raw = lexf(lexf_data[0], int(lexf_data[1]))
        lexf_set_formatted = format_output(lexf_set_raw)

        solution_raw = [()]
        solution_formatted = "\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, lexf_set_raw)
        self.assertEqual(solution_formatted, lexf_set_formatted)


if __name__ == '__main__':
    unittest.main()
