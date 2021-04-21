"""
tree_test.py file that runs the unittests for tree.py when the file is called or
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
from tree import tree
from parsers import parse_tree_data


class TestProgrammingProblemTREE(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_tree_positive_a(self):
        tree_data = parse_tree_data("rosalind_tree_1.txt")
        num_missing_nodes = tree(int(tree_data[0]), tree_data[1:])
        solution = 3

        # make sure solution matches computed result
        self.assertEqual(solution, num_missing_nodes)

    def test_tree_positive_b(self):
        tree_data = parse_tree_data("rosalind_tree_2.txt")
        num_missing_nodes = tree(int(tree_data[0]), tree_data[1:])
        solution = 80

        # make sure solution matches computed result
        self.assertEqual(solution, num_missing_nodes)

    def test_tree_positive_c(self):
        tree_data = parse_tree_data("rosalind_tree_3.txt")
        num_missing_nodes = tree(int(tree_data[0]), tree_data[1:])
        solution = 35

        # make sure solution matches computed result
        self.assertEqual(solution, num_missing_nodes)

    def test_tree_negative(self):
        tree_data = parse_tree_data("rosalind_tree_4.txt")
        num_missing_nodes = tree(int(tree_data[0]), tree_data[1:])
        solution = 0

        # make sure solution matches computed result
        self.assertEqual(solution, num_missing_nodes)


if __name__ == '__main__':
    unittest.main()
