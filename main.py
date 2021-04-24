"""
main.py file that runs the unittests when the file is called or run using the
python CLI.

Controller of unit tests for the Group Project for CISC 471,
Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

There are two ways to run the program, outlined below. Both methods run the
unittests.

Sample Usage:
  $ python -m main main.py
"""

import unittest
import os


def get_test_suite():
    """Grab all test files pattern matched with *_test.py

    :return: unittest test suite loaded and ready to run with all unitest files
    """
    loader = unittest.TestLoader()
    start_dir = os.getcwd()
    test_suite_loader = loader.discover(start_dir, pattern="*_test.py")
    return test_suite_loader


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestN50Algorithm)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    test_suite = get_test_suite()
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
