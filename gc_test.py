"""
gc_test.py file that runs the unittests for dna.py when the file is called or
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
# import importlib
from gc_ import gc
from parsers import parse_gc_data

# _gc = importlib.import_module('gc.gc')
# gc = getattr(gc, "gc")


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_gc_positive_a(self):
        FASTA_data = parse_gc_data("rosalind_gc_1.txt")
        max_gc_content = gc(FASTA_data)
        solution = ['Rosalind_0808', 60.91954022988506]

        # make sure solution matches computed result
        self.assertEqual(solution, max_gc_content)

    def test_gc_positive_b(self):
        FASTA_data = parse_gc_data("rosalind_gc_2.txt")
        max_gc_content = gc(FASTA_data)
        solution = ['Rosalind_7453', 52.14368482039398]

        # make sure solution matches computed result
        self.assertEqual(solution, max_gc_content)

    def test_gc_positive_c(self):
        FASTA_data = parse_gc_data("rosalind_gc_3.txt")
        max_gc_content = gc(FASTA_data)
        solution = ['Rosalind_0562', 52.28426395939086]

        # make sure solution matches computed result
        self.assertEqual(solution, max_gc_content)

    def test_dna_negative(self):
        FASTA_data = parse_gc_data("rosalind_gc_4.txt")
        max_gc_content = gc(FASTA_data)
        solution = ['', 0]

        # make sure solution matches computed result
        self.assertEqual(solution, max_gc_content)


if __name__ == '__main__':
    unittest.main()
