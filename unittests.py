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


class TestN50Algorithm(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_n50_positive_a(self):
        return

    def test_n50_negative(self):
        return


if __name__ == '__main__':
    unittest.main()
