"""
seto_test.py file that runs the unittests for seto.py when the file is called or
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
from seto import seto, format_output
from parsers import parse_seto_data, parse_single_line_sol_data


class TestProgrammingProblemSETO(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_seto_positive_a(self):
        seto_data = parse_seto_data("rosalind_seto_1.txt")
        set_a = [int(i) for i in seto_data[1]]
        set_b = [int(i) for i in seto_data[2]]
        output_sets_raw = seto(int(seto_data[0]), set_a, set_b)
        output_sets_formatted = format_output(output_sets_raw)

        solution_raw = [[1, 2, 3, 4, 5, 8, 10], [2, 5], [1, 3, 4], [8, 10],
                        [6, 7, 8, 9, 10], [1, 3, 4, 6, 7, 9]]
        solution_formatted = "{1, 2, 3, 4, 5, 8, 10}\n{2, 5}\n{1, 3, 4}\n{8, " \
                             "10}\n{6, 7, 8, 9, 10}\n{1, 3, 4, 6, 7, 9}\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, output_sets_raw)
        self.assertEqual(solution_formatted, output_sets_formatted)

    def test_seto_positive_b(self):
        seto_data = parse_seto_data("rosalind_seto_2.txt")
        set_a = [int(i) for i in seto_data[1]]
        set_b = [int(i) for i in seto_data[2]]
        output_sets_raw = seto(int(seto_data[0]), set_a, set_b)
        output_sets_formatted = format_output(output_sets_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_perm_2_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, output_sets_raw)
        self.assertEqual(solution_formatted, output_sets_formatted)

    def test_seto_positive_c(self):
        seto_data = parse_seto_data("rosalind_seto_3.txt")
        set_a = [int(i) for i in seto_data[1]]
        set_b = [int(i) for i in seto_data[2]]
        output_sets_raw = seto(int(seto_data[0]), set_a, set_b)
        output_sets_formatted = format_output(output_sets_raw)

        solution_raw = ast.literal_eval(parse_single_line_sol_data(
            "rosalind_perm_3_sol.txt")
        )
        solution_formatted = format_output(solution_raw)

        # make sure solution matches computed result
        self.assertEqual(solution_raw, output_sets_raw)
        self.assertEqual(solution_formatted, output_sets_formatted)

    def test_seto_negative(self):
        seto_data = parse_seto_data("rosalind_seto_4.txt")
        set_one = seto_data[1]
        set_two = seto_data[2]
        output_sets_raw = seto(int(seto_data[0]), set_one, set_two)
        output_sets_formatted = format_output(output_sets_raw)

        solution_raw = []
        solution_formatted = ""

        # make sure solution matches computed result
        self.assertEqual(solution_raw, output_sets_raw)
        self.assertEqual(solution_formatted, output_sets_formatted)


if __name__ == '__main__':
    unittest.main()
