"""
splc_test.py file that runs the unittests for splc.py when the file is called or
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
from splc import splc
from prot import prot
from parsers import parse_gc_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_splc_positive_a(self):
        splc_FASTA_data = parse_gc_data("rosalind_splc_1.txt")
        spliced_rna_str = splc(splc_FASTA_data)
        peptide = prot(spliced_rna_str)

        solution = "MVYIADKQHVASREAYGHMFKVCA"

        # make sure solution matches computed result
        self.assertEqual(solution, peptide)

    def test_splc_positive_b(self):
        splc_FASTA_data = parse_gc_data("rosalind_splc_2.txt")
        spliced_rna_str = splc(splc_FASTA_data)
        peptide = prot(spliced_rna_str)

        solution = "MYSKTRAVTHDTVMYTSESLEHQAYIHAWCMTKLVALLVRNSTGQASAKWDSGERYP" \
                   "DSPEGHVPRRYLLSLALSGRKISQILNEAGGCVARLYPFIYSTRKEVHDEDVMIASG" \
                   "ADQIRDFFKMNGNLCGSTPPEPPNCYTHRSVICLIAVPSVRRGR"

        # make sure solution matches computed result
        self.assertEqual(solution, peptide)

    def test_splc_positive_c(self):
        splc_FASTA_data = parse_gc_data("rosalind_splc_3.txt")
        spliced_rna_str = splc(splc_FASTA_data)
        peptide = prot(spliced_rna_str)

        solution = "MPGSTLKDDVLLRIKTLRGTRIRLRKVFKHSIARRSPKMVPRQVRVGRNPRYGAIV" \
                   "SSEHVGGRIASTTRLRTDRLAYAFGVVCERYKIHTWLRSMLTPDVRDEPVVSSVYM" \
                   "TMGVRLKLSISVWPPCVPSESRFQTIIIYCSTVSHLRRGGVDLLQRIKDTMLGTGS" \
                   "CQAQPPVSTIAQTEPSAYNFSRHLMDLQNPPL"

        # make sure solution matches computed result
        self.assertEqual(solution, peptide)

    def test_splc_negative(self):
        splc_FASTA_data = parse_gc_data("rosalind_splc_4.txt")
        spliced_rna_str = splc(splc_FASTA_data)
        peptide = prot(spliced_rna_str)

        solution = None

        # make sure solution matches computed result
        self.assertEqual(solution, peptide)


if __name__ == '__main__':
    unittest.main()
