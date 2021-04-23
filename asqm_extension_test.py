"""
asmq_test.py file that runs the unittests for asmq.py when the file is called or
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
from asqm_extension import *
from sample_data_generator import *


class TestProgrammingProblemASMQ(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_asmq_ext_positive_a(self):
        asmq_ext_data = generate_error_sample()
        asmq_50 = asmq(asmq_data, 50)
        asmq_75 = asmq(asmq_data, 75)

        solution_50 = 7
        solution_75 = 6

        # make sure solution matches computed result
        self.assertEqual(solution_50, asmq_50)
        self.assertEqual(solution_75, asmq_75)

    def test_asmq_ext_positive_b(self):
        asmq_data = parse_assembly_data("rosalind_asmq_2.txt")
        asmq_50 = asmq(asmq_data, 50)
        asmq_75 = asmq(asmq_data, 75)

        solution_50 = 177
        solution_75 = 133

        # make sure solution matches computed result
        self.assertEqual(solution_50, asmq_50)
        self.assertEqual(solution_75, asmq_75)

    def test_asmq_ext_positive_c(self):
        asmq_data = parse_assembly_data("rosalind_asmq_3.txt")
        asmq_50 = asmq(asmq_data, 50)
        asmq_75 = asmq(asmq_data, 75)

        solution_50 = 138
        solution_75 = 102

        # make sure solution matches computed result
        self.assertEqual(solution_50, asmq_50)
        self.assertEqual(solution_75, asmq_75)

    def test_asmq_ext_positive_d(self):
        asmq_data = parse_assembly_data("rosalind_asmq_4.txt")
        asmq_50 = asmq(asmq_data, 50)
        asmq_75 = asmq(asmq_data, 75)

        solution_50 = 0
        solution_75 = 0

        # make sure solution matches computed result
        self.assertEqual(solution_50, asmq_50)
        self.assertEqual(solution_75, asmq_75)

    # test sample data generator and assert percentages match

    # test error and assert percentages match

    # test uxx

    # test uaxx and assert error data gives same result


if __name__ == '__main__':
    unittest.main()
