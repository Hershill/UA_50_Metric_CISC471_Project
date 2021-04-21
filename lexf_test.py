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
from lexf import lexf, format_output
from parsers import parse_lexf_data


class TestProgrammingPartOne(unittest.TestCase):
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

        solution_raw = [('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'),
                        ('A', 'A', 'A', 'C'), ('A', 'A', 'A', 'D'),
                        ('A', 'A', 'B', 'A'), ('A', 'A', 'B', 'B'),
                        ('A', 'A', 'B', 'C'), ('A', 'A', 'B', 'D'),
                        ('A', 'A', 'C', 'A'), ('A', 'A', 'C', 'B'),
                        ('A', 'A', 'C', 'C'), ('A', 'A', 'C', 'D'),
                        ('A', 'A', 'D', 'A'), ('A', 'A', 'D', 'B'),
                        ('A', 'A', 'D', 'C'), ('A', 'A', 'D', 'D'),
                        ('A', 'B', 'A', 'A'), ('A', 'B', 'A', 'B'),
                        ('A', 'B', 'A', 'C'), ('A', 'B', 'A', 'D'),
                        ('A', 'B', 'B', 'A'), ('A', 'B', 'B', 'B'),
                        ('A', 'B', 'B', 'C'), ('A', 'B', 'B', 'D'),
                        ('A', 'B', 'C', 'A'), ('A', 'B', 'C', 'B'),
                        ('A', 'B', 'C', 'C'), ('A', 'B', 'C', 'D'),
                        ('A', 'B', 'D', 'A'), ('A', 'B', 'D', 'B'),
                        ('A', 'B', 'D', 'C'), ('A', 'B', 'D', 'D'),
                        ('A', 'C', 'A', 'A'), ('A', 'C', 'A', 'B'),
                        ('A', 'C', 'A', 'C'), ('A', 'C', 'A', 'D'),
                        ('A', 'C', 'B', 'A'), ('A', 'C', 'B', 'B'),
                        ('A', 'C', 'B', 'C'), ('A', 'C', 'B', 'D'),
                        ('A', 'C', 'C', 'A'), ('A', 'C', 'C', 'B'),
                        ('A', 'C', 'C', 'C'), ('A', 'C', 'C', 'D'),
                        ('A', 'C', 'D', 'A'), ('A', 'C', 'D', 'B'),
                        ('A', 'C', 'D', 'C'), ('A', 'C', 'D', 'D'),
                        ('A', 'D', 'A', 'A'), ('A', 'D', 'A', 'B'),
                        ('A', 'D', 'A', 'C'), ('A', 'D', 'A', 'D'),
                        ('A', 'D', 'B', 'A'), ('A', 'D', 'B', 'B'),
                        ('A', 'D', 'B', 'C'), ('A', 'D', 'B', 'D'),
                        ('A', 'D', 'C', 'A'), ('A', 'D', 'C', 'B'),
                        ('A', 'D', 'C', 'C'), ('A', 'D', 'C', 'D'),
                        ('A', 'D', 'D', 'A'), ('A', 'D', 'D', 'B'),
                        ('A', 'D', 'D', 'C'), ('A', 'D', 'D', 'D'),
                        ('B', 'A', 'A', 'A'), ('B', 'A', 'A', 'B'),
                        ('B', 'A', 'A', 'C'), ('B', 'A', 'A', 'D'),
                        ('B', 'A', 'B', 'A'), ('B', 'A', 'B', 'B'),
                        ('B', 'A', 'B', 'C'), ('B', 'A', 'B', 'D'),
                        ('B', 'A', 'C', 'A'), ('B', 'A', 'C', 'B'),
                        ('B', 'A', 'C', 'C'), ('B', 'A', 'C', 'D'),
                        ('B', 'A', 'D', 'A'), ('B', 'A', 'D', 'B'),
                        ('B', 'A', 'D', 'C'), ('B', 'A', 'D', 'D'),
                        ('B', 'B', 'A', 'A'), ('B', 'B', 'A', 'B'),
                        ('B', 'B', 'A', 'C'), ('B', 'B', 'A', 'D'),
                        ('B', 'B', 'B', 'A'), ('B', 'B', 'B', 'B'),
                        ('B', 'B', 'B', 'C'), ('B', 'B', 'B', 'D'),
                        ('B', 'B', 'C', 'A'), ('B', 'B', 'C', 'B'),
                        ('B', 'B', 'C', 'C'), ('B', 'B', 'C', 'D'),
                        ('B', 'B', 'D', 'A'), ('B', 'B', 'D', 'B'),
                        ('B', 'B', 'D', 'C'), ('B', 'B', 'D', 'D'),
                        ('B', 'C', 'A', 'A'), ('B', 'C', 'A', 'B'),
                        ('B', 'C', 'A', 'C'), ('B', 'C', 'A', 'D'),
                        ('B', 'C', 'B', 'A'), ('B', 'C', 'B', 'B'),
                        ('B', 'C', 'B', 'C'), ('B', 'C', 'B', 'D'),
                        ('B', 'C', 'C', 'A'), ('B', 'C', 'C', 'B'),
                        ('B', 'C', 'C', 'C'), ('B', 'C', 'C', 'D'),
                        ('B', 'C', 'D', 'A'), ('B', 'C', 'D', 'B'),
                        ('B', 'C', 'D', 'C'), ('B', 'C', 'D', 'D'),
                        ('B', 'D', 'A', 'A'), ('B', 'D', 'A', 'B'),
                        ('B', 'D', 'A', 'C'), ('B', 'D', 'A', 'D'),
                        ('B', 'D', 'B', 'A'), ('B', 'D', 'B', 'B'),
                        ('B', 'D', 'B', 'C'), ('B', 'D', 'B', 'D'),
                        ('B', 'D', 'C', 'A'), ('B', 'D', 'C', 'B'),
                        ('B', 'D', 'C', 'C'), ('B', 'D', 'C', 'D'),
                        ('B', 'D', 'D', 'A'), ('B', 'D', 'D', 'B'),
                        ('B', 'D', 'D', 'C'), ('B', 'D', 'D', 'D'),
                        ('C', 'A', 'A', 'A'), ('C', 'A', 'A', 'B'),
                        ('C', 'A', 'A', 'C'), ('C', 'A', 'A', 'D'),
                        ('C', 'A', 'B', 'A'), ('C', 'A', 'B', 'B'),
                        ('C', 'A', 'B', 'C'), ('C', 'A', 'B', 'D'),
                        ('C', 'A', 'C', 'A'), ('C', 'A', 'C', 'B'),
                        ('C', 'A', 'C', 'C'), ('C', 'A', 'C', 'D'),
                        ('C', 'A', 'D', 'A'), ('C', 'A', 'D', 'B'),
                        ('C', 'A', 'D', 'C'), ('C', 'A', 'D', 'D'),
                        ('C', 'B', 'A', 'A'), ('C', 'B', 'A', 'B'),
                        ('C', 'B', 'A', 'C'), ('C', 'B', 'A', 'D'),
                        ('C', 'B', 'B', 'A'), ('C', 'B', 'B', 'B'),
                        ('C', 'B', 'B', 'C'), ('C', 'B', 'B', 'D'),
                        ('C', 'B', 'C', 'A'), ('C', 'B', 'C', 'B'),
                        ('C', 'B', 'C', 'C'), ('C', 'B', 'C', 'D'),
                        ('C', 'B', 'D', 'A'), ('C', 'B', 'D', 'B'),
                        ('C', 'B', 'D', 'C'), ('C', 'B', 'D', 'D'),
                        ('C', 'C', 'A', 'A'), ('C', 'C', 'A', 'B'),
                        ('C', 'C', 'A', 'C'), ('C', 'C', 'A', 'D'),
                        ('C', 'C', 'B', 'A'), ('C', 'C', 'B', 'B'),
                        ('C', 'C', 'B', 'C'), ('C', 'C', 'B', 'D'),
                        ('C', 'C', 'C', 'A'), ('C', 'C', 'C', 'B'),
                        ('C', 'C', 'C', 'C'), ('C', 'C', 'C', 'D'),
                        ('C', 'C', 'D', 'A'), ('C', 'C', 'D', 'B'),
                        ('C', 'C', 'D', 'C'), ('C', 'C', 'D', 'D'),
                        ('C', 'D', 'A', 'A'), ('C', 'D', 'A', 'B'),
                        ('C', 'D', 'A', 'C'), ('C', 'D', 'A', 'D'),
                        ('C', 'D', 'B', 'A'), ('C', 'D', 'B', 'B'),
                        ('C', 'D', 'B', 'C'), ('C', 'D', 'B', 'D'),
                        ('C', 'D', 'C', 'A'), ('C', 'D', 'C', 'B'),
                        ('C', 'D', 'C', 'C'), ('C', 'D', 'C', 'D'),
                        ('C', 'D', 'D', 'A'), ('C', 'D', 'D', 'B'),
                        ('C', 'D', 'D', 'C'), ('C', 'D', 'D', 'D'),
                        ('D', 'A', 'A', 'A'), ('D', 'A', 'A', 'B'),
                        ('D', 'A', 'A', 'C'), ('D', 'A', 'A', 'D'),
                        ('D', 'A', 'B', 'A'), ('D', 'A', 'B', 'B'),
                        ('D', 'A', 'B', 'C'), ('D', 'A', 'B', 'D'),
                        ('D', 'A', 'C', 'A'), ('D', 'A', 'C', 'B'),
                        ('D', 'A', 'C', 'C'), ('D', 'A', 'C', 'D'),
                        ('D', 'A', 'D', 'A'), ('D', 'A', 'D', 'B'),
                        ('D', 'A', 'D', 'C'), ('D', 'A', 'D', 'D'),
                        ('D', 'B', 'A', 'A'), ('D', 'B', 'A', 'B'),
                        ('D', 'B', 'A', 'C'), ('D', 'B', 'A', 'D'),
                        ('D', 'B', 'B', 'A'), ('D', 'B', 'B', 'B'),
                        ('D', 'B', 'B', 'C'), ('D', 'B', 'B', 'D'),
                        ('D', 'B', 'C', 'A'), ('D', 'B', 'C', 'B'),
                        ('D', 'B', 'C', 'C'), ('D', 'B', 'C', 'D'),
                        ('D', 'B', 'D', 'A'), ('D', 'B', 'D', 'B'),
                        ('D', 'B', 'D', 'C'), ('D', 'B', 'D', 'D'),
                        ('D', 'C', 'A', 'A'), ('D', 'C', 'A', 'B'),
                        ('D', 'C', 'A', 'C'), ('D', 'C', 'A', 'D'),
                        ('D', 'C', 'B', 'A'), ('D', 'C', 'B', 'B'),
                        ('D', 'C', 'B', 'C'), ('D', 'C', 'B', 'D'),
                        ('D', 'C', 'C', 'A'), ('D', 'C', 'C', 'B'),
                        ('D', 'C', 'C', 'C'), ('D', 'C', 'C', 'D'),
                        ('D', 'C', 'D', 'A'), ('D', 'C', 'D', 'B'),
                        ('D', 'C', 'D', 'C'), ('D', 'C', 'D', 'D'),
                        ('D', 'D', 'A', 'A'), ('D', 'D', 'A', 'B'),
                        ('D', 'D', 'A', 'C'), ('D', 'D', 'A', 'D'),
                        ('D', 'D', 'B', 'A'), ('D', 'D', 'B', 'B'),
                        ('D', 'D', 'B', 'C'), ('D', 'D', 'B', 'D'),
                        ('D', 'D', 'C', 'A'), ('D', 'D', 'C', 'B'),
                        ('D', 'D', 'C', 'C'), ('D', 'D', 'C', 'D'),
                        ('D', 'D', 'D', 'A'), ('D', 'D', 'D', 'B'),
                        ('D', 'D', 'D', 'C'), ('D', 'D', 'D', 'D')]

        solution_formatted = "AAAA\nAAAB\nAAAC\nAAAD\nAABA\nAABB\nAABC\nAABD" \
                             "\nAACA\nAACB\nAACC\nAACD\nAADA\nAADB\nAADC" \
                             "\nAADD\nABAA\nABAB\nABAC\nABAD\nABBA\nABBB" \
                             "\nABBC\nABBD\nABCA\nABCB\nABCC\nABCD\nABDA" \
                             "\nABDB\nABDC\nABDD\nACAA\nACAB\nACAC\nACAD" \
                             "\nACBA\nACBB\nACBC\nACBD\nACCA\nACCB\nACCC" \
                             "\nACCD\nACDA\nACDB\nACDC\nACDD\nADAA\nADAB" \
                             "\nADAC\nADAD\nADBA\nADBB\nADBC\nADBD\nADCA" \
                             "\nADCB\nADCC\nADCD\nADDA\nADDB\nADDC\nADDD" \
                             "\nBAAA\nBAAB\nBAAC\nBAAD\nBABA\nBABB\nBABC" \
                             "\nBABD\nBACA\nBACB\nBACC\nBACD\nBADA\nBADB" \
                             "\nBADC\nBADD\nBBAA\nBBAB\nBBAC\nBBAD\nBBBA" \
                             "\nBBBB\nBBBC\nBBBD\nBBCA\nBBCB\nBBCC\nBBCD" \
                             "\nBBDA\nBBDB\nBBDC\nBBDD\nBCAA\nBCAB\nBCAC" \
                             "\nBCAD\nBCBA\nBCBB\nBCBC\nBCBD\nBCCA\nBCCB" \
                             "\nBCCC\nBCCD\nBCDA\nBCDB\nBCDC\nBCDD\nBDAA" \
                             "\nBDAB\nBDAC\nBDAD\nBDBA\nBDBB\nBDBC\nBDBD" \
                             "\nBDCA\nBDCB\nBDCC\nBDCD\nBDDA\nBDDB\nBDDC" \
                             "\nBDDD\nCAAA\nCAAB\nCAAC\nCAAD\nCABA\nCABB" \
                             "\nCABC\nCABD\nCACA\nCACB\nCACC\nCACD\nCADA" \
                             "\nCADB\nCADC\nCADD\nCBAA\nCBAB\nCBAC\nCBAD" \
                             "\nCBBA\nCBBB\nCBBC\nCBBD\nCBCA\nCBCB\nCBCC" \
                             "\nCBCD\nCBDA\nCBDB\nCBDC\nCBDD\nCCAA\nCCAB" \
                             "\nCCAC\nCCAD\nCCBA\nCCBB\nCCBC\nCCBD\nCCCA" \
                             "\nCCCB\nCCCC\nCCCD\nCCDA\nCCDB\nCCDC\nCCDD" \
                             "\nCDAA\nCDAB\nCDAC\nCDAD\nCDBA\nCDBB\nCDBC" \
                             "\nCDBD\nCDCA\nCDCB\nCDCC\nCDCD\nCDDA\nCDDB" \
                             "\nCDDC\nCDDD\nDAAA\nDAAB\nDAAC\nDAAD\nDABA" \
                             "\nDABB\nDABC\nDABD\nDACA\nDACB\nDACC\nDACD" \
                             "\nDADA\nDADB\nDADC\nDADD\nDBAA\nDBAB\nDBAC" \
                             "\nDBAD\nDBBA\nDBBB\nDBBC\nDBBD\nDBCA\nDBCB" \
                             "\nDBCC\nDBCD\nDBDA\nDBDB\nDBDC\nDBDD\nDCAA" \
                             "\nDCAB\nDCAC\nDCAD\nDCBA\nDCBB\nDCBC\nDCBD" \
                             "\nDCCA\nDCCB\nDCCC\nDCCD\nDCDA\nDCDB\nDCDC" \
                             "\nDCDD\nDDAA\nDDAB\nDDAC\nDDAD\nDDBA\nDDBB" \
                             "\nDDBC\nDDBD\nDDCA\nDDCB\nDDCC\nDDCD\nDDDA" \
                             "\nDDDB\nDDDC\nDDDD\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, lexf_set_raw)
        self.assertEqual(solution_formatted, lexf_set_formatted)

    def test_lexf_positive_c(self):
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
