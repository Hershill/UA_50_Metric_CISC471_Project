"""
subs_test.py file that runs the unittests for subs.py when the file is called or
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
from subs import subs, format_output
from parsers import parse_subs_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_subs_positive_a(self):
        subs_data = parse_subs_data("rosalind_subs_1.txt")
        indices_raw = subs(subs_data[0], subs_data[1])
        indices_formatted = format_output(indices_raw)

        solution_raw = [2, 4, 10]
        solution_formatted = "2 4 10"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, indices_raw)
        self.assertEqual(solution_formatted, indices_formatted)

    def test_subs_positive_b(self):
        subs_data = parse_subs_data("rosalind_subs_2.txt")
        indices_raw = subs(subs_data[0], subs_data[1])
        indices_formatted = format_output(indices_raw)

        solution_raw = [29, 36, 43, 50, 57, 103, 176, 235, 266, 279, 314, 485,
                        525, 704, 739, 782, 848]
        solution_formatted = "29 36 43 50 57 103 176 235 266 279 314 485 525 " \
                             "704 739 782 848"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, indices_raw)
        self.assertEqual(solution_formatted, indices_formatted)

    def test_subs_positive_c(self):
        subs_data = parse_subs_data("rosalind_subs_3.txt")
        indices_raw = subs(subs_data[0], subs_data[1])
        indices_formatted = format_output(indices_raw)

        solution_raw = [45, 52, 59, 84, 142, 192, 257, 291, 298, 332, 339, 346,
                        361, 422, 543, 561, 580, 587, 602, 619, 639, 646, 785,
                        792, 811, 818, 851, 866, 908]
        solution_formatted = "45 52 59 84 142 192 257 291 298 332 339 346 361" \
                             " 422 543 561 580 587 602 619 639 646 785 792" \
                             " 811 818 851 866 908"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, indices_raw)
        self.assertEqual(solution_formatted, indices_formatted)

    def test_subs_negative(self):
        subs_data = parse_subs_data("rosalind_subs_4.txt")
        indices_raw = subs(subs_data[0], subs_data[1])
        indices_formatted = format_output(indices_raw)

        solution_raw = []
        solution_formatted = ""

        # make sure solution matches computed result
        self.assertEqual(solution_raw, indices_raw)
        self.assertEqual(solution_formatted, indices_formatted)


if __name__ == '__main__':
    unittest.main()
