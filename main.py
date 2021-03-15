"""
main.py file that runs the unittests when the file is called or run using the python CLI.

Controller of unit tests for the Group project for CISC 471, Computational Biology.

By:
- Andrew Ma (20030440)
- Rayan Shaikli (20059806)
- Hershil Devnani (20001045)

There are two ways to run the program, outlined below. Both methods run the unittests.
Sample Usage:
  $ python -m unittest unittests.py
  $ python -m main main.py
"""

from unittests import TestN50Algorithm
import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestN50Algorithm)
    unittest.TextTestRunner(verbosity=2).run(suite)
