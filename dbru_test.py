"""
dbru_test.py file that runs the unittests for dbru.py when the file is called or
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
from dbru import dbru, format_output
from parsers import parse_subs_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_dbru_positive_a(self):
        dbru_data = parse_subs_data("rosalind_dbru_1.txt")
        dbru_graph_raw = dbru(dbru_data)
        dbru_graph_formatted = format_output(dbru_graph_raw)

        solution_raw = [('ATC', 'TCA'), ('ATG', 'TGA'), ('ATG', 'TGC'),
                        ('CAT', 'ATC'), ('CAT', 'ATG'), ('GAT', 'ATG'),
                        ('GCA', 'CAT'), ('TCA', 'CAT'), ('TGA', 'GAT')]

        solution_formatted = "(ATC, TCA)\n(ATG, TGA)\n(ATG, TGC)\n(CAT, " \
                             "ATC)\n(CAT, ATG)\n(GAT, ATG)\n(GCA, CAT)\n(TCA," \
                             " CAT)\n(TGA, GAT)\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, dbru_graph_raw)
        self.assertEqual(solution_formatted, dbru_graph_formatted)

    def test_dbru_positive_b(self):
        dbru_data = parse_subs_data("rosalind_dbru_1.txt")
        dbru_graph_raw = dbru(dbru_data)
        dbru_graph_formatted = format_output(dbru_graph_raw)

        solution_raw = [('ATC', 'TCA'), ('ATG', 'TGA'), ('ATG', 'TGC'),
                        ('CAT', 'ATC'), ('CAT', 'ATG'), ('GAT', 'ATG'),
                        ('GCA', 'CAT'), ('TCA', 'CAT'), ('TGA', 'GAT')]

        solution_formatted = "(ATC, TCA)\n(ATG, TGA)\n(ATG, TGC)\n(CAT, " \
                             "ATC)\n(CAT, ATG)\n(GAT, ATG)\n(GCA, CAT)\n(TCA," \
                             " CAT)\n(TGA, GAT)\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, dbru_graph_raw)
        self.assertEqual(solution_formatted, dbru_graph_formatted)

    def test_dbru_positive_c(self):
        dbru_data = parse_subs_data("rosalind_dbru_1.txt")
        dbru_graph_raw = dbru(dbru_data)
        dbru_graph_formatted = format_output(dbru_graph_raw)

        solution_raw = [('ATC', 'TCA'), ('ATG', 'TGA'), ('ATG', 'TGC'),
                        ('CAT', 'ATC'), ('CAT', 'ATG'), ('GAT', 'ATG'),
                        ('GCA', 'CAT'), ('TCA', 'CAT'), ('TGA', 'GAT')]

        solution_formatted = "(ATC, TCA)\n(ATG, TGA)\n(ATG, TGC)\n(CAT, " \
                             "ATC)\n(CAT, ATG)\n(GAT, ATG)\n(GCA, CAT)\n(TCA," \
                             " CAT)\n(TGA, GAT)\n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, dbru_graph_raw)
        self.assertEqual(solution_formatted, dbru_graph_formatted)

    def test_dbru_negative(self):
        dbru_data = parse_subs_data("rosalind_dbru_4.txt")
        dbru_graph_raw = dbru(dbru_data)
        dbru_graph_formatted = format_output(dbru_graph_raw)

        solution_raw = []

        solution_formatted = ""

        # make sure solution matches computed result
        self.assertEqual(solution_raw, dbru_graph_raw)
        self.assertEqual(solution_formatted, dbru_graph_formatted)


if __name__ == '__main__':
    unittest.main()
