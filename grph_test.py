"""
grph_test.py file that runs the unittests for grph.py when the file is called or
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
from grph import grph, format_output
from parsers import parse_gc_data


class TestProgrammingPartOne(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_grph_positive_a(self):
        grph_data = parse_gc_data("rosalind_grph_1.txt")
        adjacency_raw = grph(grph_data)
        adjacency_formatted = format_output(adjacency_raw)

        solution_raw = [('Rosalind_0498', 'Rosalind_2391'),
                        ('Rosalind_0498', 'Rosalind_0442'),
                        ('Rosalind_2391', 'Rosalind_2323')]
        solution_formatted = \
            "Rosalind_0498 Rosalind_2391 \n" \
            "Rosalind_0498 Rosalind_0442 \n" \
            "Rosalind_2391 Rosalind_2323 \n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, adjacency_raw)
        self.assertEqual(solution_formatted, adjacency_formatted)

    def test_grph_positive_b(self):
        grph_data = parse_gc_data("rosalind_grph_2.txt")
        adjacency_raw = grph(grph_data)
        adjacency_formatted = format_output(adjacency_raw)

        solution_raw = [
         ('Rosalind_0327', 'Rosalind_0937'), ('Rosalind_0327', 'Rosalind_1226'),
         ('Rosalind_0327', 'Rosalind_5849'), ('Rosalind_8012', 'Rosalind_8080'),
         ('Rosalind_8012', 'Rosalind_9546'), ('Rosalind_0175', 'Rosalind_6766'),
         ('Rosalind_1140', 'Rosalind_8012'), ('Rosalind_1140', 'Rosalind_4185'),
         ('Rosalind_6573', 'Rosalind_1708'), ('Rosalind_7532', 'Rosalind_1939'),
         ('Rosalind_7532', 'Rosalind_2559'), ('Rosalind_6711', 'Rosalind_8466'),
         ('Rosalind_6711', 'Rosalind_8935'), ('Rosalind_6711', 'Rosalind_0778'),
         ('Rosalind_4304', 'Rosalind_7532'), ('Rosalind_4304', 'Rosalind_3870'),
         ('Rosalind_4304', 'Rosalind_4010'), ('Rosalind_4304', 'Rosalind_6555'),
         ('Rosalind_4304', 'Rosalind_0032'), ('Rosalind_2699', 'Rosalind_9332'),
         ('Rosalind_7690', 'Rosalind_5047'), ('Rosalind_7690', 'Rosalind_1005'),
         ('Rosalind_7690', 'Rosalind_2384'), ('Rosalind_1494', 'Rosalind_7149'),
         ('Rosalind_1494', 'Rosalind_0081'), ('Rosalind_1851', 'Rosalind_2519'),
         ('Rosalind_4935', 'Rosalind_7690'), ('Rosalind_4935', 'Rosalind_7036'),
         ('Rosalind_4935', 'Rosalind_5740'), ('Rosalind_1297', 'Rosalind_0318'),
         ('Rosalind_2519', 'Rosalind_1297'), ('Rosalind_2519', 'Rosalind_4293'),
         ('Rosalind_8997', 'Rosalind_0318'), ('Rosalind_8464', 'Rosalind_9858'),
         ('Rosalind_8464', 'Rosalind_9612'), ('Rosalind_8464', 'Rosalind_4641'),
         ('Rosalind_8464', 'Rosalind_3352'), ('Rosalind_9500', 'Rosalind_2748'),
         ('Rosalind_9500', 'Rosalind_5638'), ('Rosalind_3870', 'Rosalind_0568'),
         ('Rosalind_3870', 'Rosalind_6122'), ('Rosalind_0568', 'Rosalind_0937'),
         ('Rosalind_0568', 'Rosalind_1226'), ('Rosalind_0568', 'Rosalind_5849'),
         ('Rosalind_4010', 'Rosalind_8464'), ('Rosalind_4010', 'Rosalind_1553'),
         ('Rosalind_4010', 'Rosalind_2518'), ('Rosalind_7036', 'Rosalind_8012'),
         ('Rosalind_7036', 'Rosalind_4185'), ('Rosalind_3908', 'Rosalind_1142'),
         ('Rosalind_3908', 'Rosalind_9172'), ('Rosalind_1939', 'Rosalind_2308'),
         ('Rosalind_1939', 'Rosalind_5295'), ('Rosalind_1939', 'Rosalind_5848'),
         ('Rosalind_0239', 'Rosalind_8012'), ('Rosalind_0239', 'Rosalind_4185'),
         ('Rosalind_5774', 'Rosalind_5935'), ('Rosalind_5295', 'Rosalind_9500'),
         ('Rosalind_5295', 'Rosalind_6804'), ('Rosalind_5295', 'Rosalind_4875'),
         ('Rosalind_5295', 'Rosalind_7209'), ('Rosalind_5848', 'Rosalind_7532'),
         ('Rosalind_5848', 'Rosalind_4304'), ('Rosalind_5848', 'Rosalind_3870'),
         ('Rosalind_5848', 'Rosalind_4010'), ('Rosalind_5848', 'Rosalind_6555'),
         ('Rosalind_5848', 'Rosalind_0032'), ('Rosalind_2967', 'Rosalind_3908'),
         ('Rosalind_0073', 'Rosalind_1851'), ('Rosalind_0073', 'Rosalind_3137'),
         ('Rosalind_1226', 'Rosalind_1051'), ('Rosalind_2924', 'Rosalind_0920'),
         ('Rosalind_2924', 'Rosalind_2757'), ('Rosalind_6122', 'Rosalind_4423'),
         ('Rosalind_6804', 'Rosalind_8080'), ('Rosalind_6804', 'Rosalind_9546'),
         ('Rosalind_7527', 'Rosalind_6766'), ('Rosalind_9612', 'Rosalind_3016'),
         ('Rosalind_5740', 'Rosalind_1671'), ('Rosalind_4097', 'Rosalind_7573'),
         ('Rosalind_4641', 'Rosalind_6766'), ('Rosalind_0061', 'Rosalind_7149'),
         ('Rosalind_0061', 'Rosalind_0081'), ('Rosalind_2757', 'Rosalind_8080'),
         ('Rosalind_2757', 'Rosalind_9546'), ('Rosalind_1138', 'Rosalind_3908'),
         ('Rosalind_3172', 'Rosalind_6766'), ('Rosalind_6766', 'Rosalind_7149'),
         ('Rosalind_6766', 'Rosalind_0081'), ('Rosalind_9172', 'Rosalind_1297'),
         ('Rosalind_9172', 'Rosalind_4293'), ('Rosalind_8466', 'Rosalind_0073'),
         ('Rosalind_1708', 'Rosalind_2204'), ('Rosalind_1708', 'Rosalind_1138'),
         ('Rosalind_7209', 'Rosalind_8464'), ('Rosalind_7209', 'Rosalind_1553'),
         ('Rosalind_7209', 'Rosalind_2518'), ('Rosalind_8080', 'Rosalind_1671'),
         ('Rosalind_3691', 'Rosalind_1494'), ('Rosalind_3691', 'Rosalind_4097'),
         ('Rosalind_3691', 'Rosalind_2220'), ('Rosalind_5849', 'Rosalind_0314'),
         ('Rosalind_5849', 'Rosalind_7527'), ('Rosalind_5849', 'Rosalind_0004'),
         ('Rosalind_8234', 'Rosalind_0937'), ('Rosalind_8234', 'Rosalind_1226'),
         ('Rosalind_8234', 'Rosalind_5849'), ('Rosalind_0081', 'Rosalind_1671'),
         ('Rosalind_3352', 'Rosalind_8997'), ('Rosalind_3352', 'Rosalind_7024'),
         ('Rosalind_3352', 'Rosalind_8167'), ('Rosalind_1553', 'Rosalind_1708'),
         ('Rosalind_2220', 'Rosalind_8997'), ('Rosalind_2220', 'Rosalind_7024'),
         ('Rosalind_2220', 'Rosalind_8167'), ('Rosalind_0450', 'Rosalind_9858'),
         ('Rosalind_0450', 'Rosalind_9612'), ('Rosalind_0450', 'Rosalind_4641'),
         ('Rosalind_0450', 'Rosalind_3352'), ('Rosalind_9546', 'Rosalind_9500'),
         ('Rosalind_9546', 'Rosalind_6804'), ('Rosalind_9546', 'Rosalind_4875'),
         ('Rosalind_9546', 'Rosalind_7209'), ('Rosalind_1005', 'Rosalind_1851'),
         ('Rosalind_1005', 'Rosalind_3137'), ('Rosalind_2559', 'Rosalind_5935'),
         ('Rosalind_2559', 'Rosalind_5774'), ('Rosalind_0047', 'Rosalind_8012'),
         ('Rosalind_0047', 'Rosalind_4185'), ('Rosalind_3137', 'Rosalind_2519'),
         ('Rosalind_4185', 'Rosalind_9500'), ('Rosalind_4185', 'Rosalind_6804'),
         ('Rosalind_4185', 'Rosalind_4875'), ('Rosalind_4185', 'Rosalind_7209'),
         ('Rosalind_0032', 'Rosalind_9332'), ('Rosalind_5638', 'Rosalind_0920'),
         ('Rosalind_5638', 'Rosalind_2757'), ('Rosalind_8145', 'Rosalind_6573'),
         ('Rosalind_8145', 'Rosalind_9721'), ('Rosalind_0318', 'Rosalind_1297'),
         ('Rosalind_0318', 'Rosalind_4293'), ('Rosalind_2384', 'Rosalind_1671'),
         ('Rosalind_2518', 'Rosalind_5047'), ('Rosalind_2518', 'Rosalind_1005'),
         ('Rosalind_2518', 'Rosalind_2384')
        ]

        solution_formatted = \
            "Rosalind_0327 Rosalind_0937 \nRosalind_0327 Rosalind_1226 \n" \
            "Rosalind_0327 Rosalind_5849 \nRosalind_8012 Rosalind_8080 \n" \
            "Rosalind_8012 Rosalind_9546 \nRosalind_0175 Rosalind_6766 \n" \
            "Rosalind_1140 Rosalind_8012 \nRosalind_1140 Rosalind_4185 \n" \
            "Rosalind_6573 Rosalind_1708 \nRosalind_7532 Rosalind_1939 \n" \
            "Rosalind_7532 Rosalind_2559 \nRosalind_6711 Rosalind_8466 \n" \
            "Rosalind_6711 Rosalind_8935 \nRosalind_6711 Rosalind_0778 \n" \
            "Rosalind_4304 Rosalind_7532 \nRosalind_4304 Rosalind_3870 \n" \
            "Rosalind_4304 Rosalind_4010 \nRosalind_4304 Rosalind_6555 \n" \
            "Rosalind_4304 Rosalind_0032 \nRosalind_2699 Rosalind_9332 \n" \
            "Rosalind_7690 Rosalind_5047 \nRosalind_7690 Rosalind_1005 \n" \
            "Rosalind_7690 Rosalind_2384 \nRosalind_1494 Rosalind_7149 \n" \
            "Rosalind_1494 Rosalind_0081 \nRosalind_1851 Rosalind_2519 \n" \
            "Rosalind_4935 Rosalind_7690 \nRosalind_4935 Rosalind_7036 \n" \
            "Rosalind_4935 Rosalind_5740 \nRosalind_1297 Rosalind_0318 \n" \
            "Rosalind_2519 Rosalind_1297 \nRosalind_2519 Rosalind_4293 \n" \
            "Rosalind_8997 Rosalind_0318 \nRosalind_8464 Rosalind_9858 \n" \
            "Rosalind_8464 Rosalind_9612 \nRosalind_8464 Rosalind_4641 \n" \
            "Rosalind_8464 Rosalind_3352 \nRosalind_9500 Rosalind_2748 \n" \
            "Rosalind_9500 Rosalind_5638 \nRosalind_3870 Rosalind_0568 \n" \
            "Rosalind_3870 Rosalind_6122 \nRosalind_0568 Rosalind_0937 \n" \
            "Rosalind_0568 Rosalind_1226 \nRosalind_0568 Rosalind_5849 \n" \
            "Rosalind_4010 Rosalind_8464 \nRosalind_4010 Rosalind_1553 \n" \
            "Rosalind_4010 Rosalind_2518 \nRosalind_7036 Rosalind_8012 \n" \
            "Rosalind_7036 Rosalind_4185 \nRosalind_3908 Rosalind_1142 \n" \
            "Rosalind_3908 Rosalind_9172 \nRosalind_1939 Rosalind_2308 \n" \
            "Rosalind_1939 Rosalind_5295 \nRosalind_1939 Rosalind_5848 \n" \
            "Rosalind_0239 Rosalind_8012 \nRosalind_0239 Rosalind_4185 \n" \
            "Rosalind_5774 Rosalind_5935 \nRosalind_5295 Rosalind_9500 \n" \
            "Rosalind_5295 Rosalind_6804 \nRosalind_5295 Rosalind_4875 \n" \
            "Rosalind_5295 Rosalind_7209 \nRosalind_5848 Rosalind_7532 \n" \
            "Rosalind_5848 Rosalind_4304 \nRosalind_5848 Rosalind_3870 \n" \
            "Rosalind_5848 Rosalind_4010 \nRosalind_5848 Rosalind_6555 \n" \
            "Rosalind_5848 Rosalind_0032 \nRosalind_2967 Rosalind_3908 \n" \
            "Rosalind_0073 Rosalind_1851 \nRosalind_0073 Rosalind_3137 \n" \
            "Rosalind_1226 Rosalind_1051 \nRosalind_2924 Rosalind_0920 \n" \
            "Rosalind_2924 Rosalind_2757 \nRosalind_6122 Rosalind_4423 \n" \
            "Rosalind_6804 Rosalind_8080 \nRosalind_6804 Rosalind_9546 \n" \
            "Rosalind_7527 Rosalind_6766 \nRosalind_9612 Rosalind_3016 \n" \
            "Rosalind_5740 Rosalind_1671 \nRosalind_4097 Rosalind_7573 \n" \
            "Rosalind_4641 Rosalind_6766 \nRosalind_0061 Rosalind_7149 \n" \
            "Rosalind_0061 Rosalind_0081 \nRosalind_2757 Rosalind_8080 \n" \
            "Rosalind_2757 Rosalind_9546 \nRosalind_1138 Rosalind_3908 \n" \
            "Rosalind_3172 Rosalind_6766 \nRosalind_6766 Rosalind_7149 \n" \
            "Rosalind_6766 Rosalind_0081 \nRosalind_9172 Rosalind_1297 \n" \
            "Rosalind_9172 Rosalind_4293 \nRosalind_8466 Rosalind_0073 \n" \
            "Rosalind_1708 Rosalind_2204 \nRosalind_1708 Rosalind_1138 \n" \
            "Rosalind_7209 Rosalind_8464 \nRosalind_7209 Rosalind_1553 \n" \
            "Rosalind_7209 Rosalind_2518 \nRosalind_8080 Rosalind_1671 \n" \
            "Rosalind_3691 Rosalind_1494 \nRosalind_3691 Rosalind_4097 \n" \
            "Rosalind_3691 Rosalind_2220 \nRosalind_5849 Rosalind_0314 \n" \
            "Rosalind_5849 Rosalind_7527 \nRosalind_5849 Rosalind_0004 \n" \
            "Rosalind_8234 Rosalind_0937 \nRosalind_8234 Rosalind_1226 \n" \
            "Rosalind_8234 Rosalind_5849 \nRosalind_0081 Rosalind_1671 \n" \
            "Rosalind_3352 Rosalind_8997 \nRosalind_3352 Rosalind_7024 \n" \
            "Rosalind_3352 Rosalind_8167 \nRosalind_1553 Rosalind_1708 \n" \
            "Rosalind_2220 Rosalind_8997 \nRosalind_2220 Rosalind_7024 \n" \
            "Rosalind_2220 Rosalind_8167 \nRosalind_0450 Rosalind_9858 \n" \
            "Rosalind_0450 Rosalind_9612 \nRosalind_0450 Rosalind_4641 \n" \
            "Rosalind_0450 Rosalind_3352 \nRosalind_9546 Rosalind_9500 \n" \
            "Rosalind_9546 Rosalind_6804 \nRosalind_9546 Rosalind_4875 \n" \
            "Rosalind_9546 Rosalind_7209 \nRosalind_1005 Rosalind_1851 \n" \
            "Rosalind_1005 Rosalind_3137 \nRosalind_2559 Rosalind_5935 \n" \
            "Rosalind_2559 Rosalind_5774 \nRosalind_0047 Rosalind_8012 \n" \
            "Rosalind_0047 Rosalind_4185 \nRosalind_3137 Rosalind_2519 \n" \
            "Rosalind_4185 Rosalind_9500 \nRosalind_4185 Rosalind_6804 \n" \
            "Rosalind_4185 Rosalind_4875 \nRosalind_4185 Rosalind_7209 \n" \
            "Rosalind_0032 Rosalind_9332 \nRosalind_5638 Rosalind_0920 \n" \
            "Rosalind_5638 Rosalind_2757 \nRosalind_8145 Rosalind_6573 \n" \
            "Rosalind_8145 Rosalind_9721 \nRosalind_0318 Rosalind_1297 \n" \
            "Rosalind_0318 Rosalind_4293 \nRosalind_2384 Rosalind_1671 \n" \
            "Rosalind_2518 Rosalind_5047 \nRosalind_2518 Rosalind_1005 \n" \
            "Rosalind_2518 Rosalind_2384 \n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, adjacency_raw)
        self.assertEqual(solution_formatted, adjacency_formatted)

    def test_grph_positive_c(self):
        grph_data = parse_gc_data("rosalind_grph_3.txt")
        adjacency_raw = grph(grph_data)
        adjacency_formatted = format_output(adjacency_raw)

        solution_raw = [
         ('Rosalind_1768', 'Rosalind_6654'), ('Rosalind_2173', 'Rosalind_1581'),
         ('Rosalind_2173', 'Rosalind_3225'), ('Rosalind_2173', 'Rosalind_7939'),
         ('Rosalind_6859', 'Rosalind_2868'), ('Rosalind_6859', 'Rosalind_4149'),
         ('Rosalind_6859', 'Rosalind_1049'), ('Rosalind_6859', 'Rosalind_5110'),
         ('Rosalind_2576', 'Rosalind_1269'), ('Rosalind_2576', 'Rosalind_3262'),
         ('Rosalind_2576', 'Rosalind_9921'), ('Rosalind_3068', 'Rosalind_3960'),
         ('Rosalind_2868', 'Rosalind_6673'), ('Rosalind_1521', 'Rosalind_2173'),
         ('Rosalind_1521', 'Rosalind_9476'), ('Rosalind_1521', 'Rosalind_1387'),
         ('Rosalind_1521', 'Rosalind_6336'), ('Rosalind_1581', 'Rosalind_1935'),
         ('Rosalind_8872', 'Rosalind_2868'), ('Rosalind_8872', 'Rosalind_4149'),
         ('Rosalind_8872', 'Rosalind_1049'), ('Rosalind_8872', 'Rosalind_5110'),
         ('Rosalind_8927', 'Rosalind_3960'), ('Rosalind_1935', 'Rosalind_0311'),
         ('Rosalind_1935', 'Rosalind_7588'), ('Rosalind_6931', 'Rosalind_8314'),
         ('Rosalind_6931', 'Rosalind_2566'), ('Rosalind_5082', 'Rosalind_9225'),
         ('Rosalind_3775', 'Rosalind_7060'), ('Rosalind_9225', 'Rosalind_2037'),
         ('Rosalind_9225', 'Rosalind_9668'), ('Rosalind_4637', 'Rosalind_9694'),
         ('Rosalind_4637', 'Rosalind_0271'), ('Rosalind_4637', 'Rosalind_9294'),
         ('Rosalind_6665', 'Rosalind_4857'), ('Rosalind_6665', 'Rosalind_1917'),
         ('Rosalind_6665', 'Rosalind_6697'), ('Rosalind_6665', 'Rosalind_3374'),
         ('Rosalind_6665', 'Rosalind_4429'), ('Rosalind_8942', 'Rosalind_0035'),
         ('Rosalind_8942', 'Rosalind_0548'), ('Rosalind_4266', 'Rosalind_0425'),
         ('Rosalind_7679', 'Rosalind_9303'), ('Rosalind_7679', 'Rosalind_7789'),
         ('Rosalind_6936', 'Rosalind_9694'), ('Rosalind_6936', 'Rosalind_0271'),
         ('Rosalind_6936', 'Rosalind_9294'), ('Rosalind_0035', 'Rosalind_6673'),
         ('Rosalind_9303', 'Rosalind_0425'), ('Rosalind_9110', 'Rosalind_7636'),
         ('Rosalind_0425', 'Rosalind_8606'), ('Rosalind_0425', 'Rosalind_9800'),
         ('Rosalind_0425', 'Rosalind_0645'), ('Rosalind_9795', 'Rosalind_0444'),
         ('Rosalind_0784', 'Rosalind_9694'), ('Rosalind_0784', 'Rosalind_0271'),
         ('Rosalind_0784', 'Rosalind_9294'), ('Rosalind_4857', 'Rosalind_0035'),
         ('Rosalind_4857', 'Rosalind_0548'), ('Rosalind_2385', 'Rosalind_0444'),
         ('Rosalind_6055', 'Rosalind_8314'), ('Rosalind_6055', 'Rosalind_2566'),
         ('Rosalind_6412', 'Rosalind_8606'), ('Rosalind_6412', 'Rosalind_9800'),
         ('Rosalind_6412', 'Rosalind_0645'), ('Rosalind_3656', 'Rosalind_3068'),
         ('Rosalind_3656', 'Rosalind_6531'), ('Rosalind_1611', 'Rosalind_4266'),
         ('Rosalind_1611', 'Rosalind_6055'), ('Rosalind_1871', 'Rosalind_1521'),
         ('Rosalind_1871', 'Rosalind_2385'), ('Rosalind_1871', 'Rosalind_6202'),
         ('Rosalind_0548', 'Rosalind_1269'), ('Rosalind_0548', 'Rosalind_3262'),
         ('Rosalind_0548', 'Rosalind_9921'), ('Rosalind_1782', 'Rosalind_9694'),
         ('Rosalind_1782', 'Rosalind_0271'), ('Rosalind_1782', 'Rosalind_9294'),
         ('Rosalind_7065', 'Rosalind_6673'), ('Rosalind_1226', 'Rosalind_9303'),
         ('Rosalind_1226', 'Rosalind_7789'), ('Rosalind_1917', 'Rosalind_0270'),
         ('Rosalind_1917', 'Rosalind_2689'), ('Rosalind_1917', 'Rosalind_8950'),
         ('Rosalind_9012', 'Rosalind_2868'), ('Rosalind_9012', 'Rosalind_4149'),
         ('Rosalind_9012', 'Rosalind_1049'), ('Rosalind_9012', 'Rosalind_5110'),
         ('Rosalind_0270', 'Rosalind_9012'), ('Rosalind_6654', 'Rosalind_8983'),
         ('Rosalind_6654', 'Rosalind_8042'), ('Rosalind_5051', 'Rosalind_4857'),
         ('Rosalind_5051', 'Rosalind_1917'), ('Rosalind_5051', 'Rosalind_6697'),
         ('Rosalind_5051', 'Rosalind_3374'), ('Rosalind_5051', 'Rosalind_4429'),
         ('Rosalind_9476', 'Rosalind_6936'), ('Rosalind_9476', 'Rosalind_3702'),
         ('Rosalind_9800', 'Rosalind_9303'), ('Rosalind_9800', 'Rosalind_7789'),
         ('Rosalind_2502', 'Rosalind_1532'), ('Rosalind_2502', 'Rosalind_9795'),
         ('Rosalind_2502', 'Rosalind_5287'), ('Rosalind_1387', 'Rosalind_2173'),
         ('Rosalind_1387', 'Rosalind_9476'), ('Rosalind_1387', 'Rosalind_6336'),
         ('Rosalind_3702', 'Rosalind_0035'), ('Rosalind_3702', 'Rosalind_0548'),
         ('Rosalind_3225', 'Rosalind_8905'), ('Rosalind_2689', 'Rosalind_3068'),
         ('Rosalind_2689', 'Rosalind_6531'), ('Rosalind_5287', 'Rosalind_7679'),
         ('Rosalind_1049', 'Rosalind_1226'), ('Rosalind_7599', 'Rosalind_0448'),
         ('Rosalind_2566', 'Rosalind_4637'), ('Rosalind_8905', 'Rosalind_8314'),
         ('Rosalind_8905', 'Rosalind_2566'), ('Rosalind_3727', 'Rosalind_2037'),
         ('Rosalind_3727', 'Rosalind_9668'), ('Rosalind_7636', 'Rosalind_0311'),
         ('Rosalind_7636', 'Rosalind_7588'), ('Rosalind_3374', 'Rosalind_9110'),
         ('Rosalind_3374', 'Rosalind_0914'), ('Rosalind_0141', 'Rosalind_4857'),
         ('Rosalind_0141', 'Rosalind_1917'), ('Rosalind_0141', 'Rosalind_6697'),
         ('Rosalind_0141', 'Rosalind_3374'), ('Rosalind_0141', 'Rosalind_4429'),
         ('Rosalind_0311', 'Rosalind_1782'), ('Rosalind_0311', 'Rosalind_4811'),
         ('Rosalind_0335', 'Rosalind_3960'), ('Rosalind_1269', 'Rosalind_9110'),
         ('Rosalind_1269', 'Rosalind_0914'), ('Rosalind_0444', 'Rosalind_0270'),
         ('Rosalind_0444', 'Rosalind_2689'), ('Rosalind_0444', 'Rosalind_8950'),
         ('Rosalind_7939', 'Rosalind_5051'), ('Rosalind_3960', 'Rosalind_4637'),
         ('Rosalind_8409', 'Rosalind_4637'), ('Rosalind_9921', 'Rosalind_3960'),
         ('Rosalind_9668', 'Rosalind_6936'), ('Rosalind_9668', 'Rosalind_3702'),
         ('Rosalind_7588', 'Rosalind_4771'), ('Rosalind_7588', 'Rosalind_6873'),
         ('Rosalind_0448', 'Rosalind_6673'), ('Rosalind_6531', 'Rosalind_0311'),
         ('Rosalind_6531', 'Rosalind_7588'), ('Rosalind_8983', 'Rosalind_8314'),
         ('Rosalind_8983', 'Rosalind_2566'), ('Rosalind_6336', 'Rosalind_0035'),
         ('Rosalind_6336', 'Rosalind_0548'), ('Rosalind_0645', 'Rosalind_2173'),
         ('Rosalind_0645', 'Rosalind_9476'), ('Rosalind_0645', 'Rosalind_1387'),
         ('Rosalind_0645', 'Rosalind_6336'), ('Rosalind_7060', 'Rosalind_6936'),
         ('Rosalind_7060', 'Rosalind_3702'), ('Rosalind_8950', 'Rosalind_3656'),
         ('Rosalind_0271', 'Rosalind_0448'), ('Rosalind_6673', 'Rosalind_1782'),
         ('Rosalind_6673', 'Rosalind_4811'), ('Rosalind_4771', 'Rosalind_8905'),
         ('Rosalind_6873', 'Rosalind_7060'), ('Rosalind_8042', 'Rosalind_3960'),
         ('Rosalind_5110', 'Rosalind_1581'), ('Rosalind_5110', 'Rosalind_3225'),
         ('Rosalind_5110', 'Rosalind_7939'), ('Rosalind_2785', 'Rosalind_3775'),
         ('Rosalind_4811', 'Rosalind_6654'), ('Rosalind_7789', 'Rosalind_7636'),
         ('Rosalind_9294', 'Rosalind_8942'), ('Rosalind_9294', 'Rosalind_3727'),
         ('Rosalind_6202', 'Rosalind_8872'), ('Rosalind_4429', 'Rosalind_2576'),
         ('Rosalind_4429', 'Rosalind_6931'), ('Rosalind_4429', 'Rosalind_8409')
        ]

        solution_formatted = \
            "Rosalind_1768 Rosalind_6654 \nRosalind_2173 Rosalind_1581 \n" \
            "Rosalind_2173 Rosalind_3225 \nRosalind_2173 Rosalind_7939 \n" \
            "Rosalind_6859 Rosalind_2868 \nRosalind_6859 Rosalind_4149 \n" \
            "Rosalind_6859 Rosalind_1049 \nRosalind_6859 Rosalind_5110 \n" \
            "Rosalind_2576 Rosalind_1269 \nRosalind_2576 Rosalind_3262 \n" \
            "Rosalind_2576 Rosalind_9921 \nRosalind_3068 Rosalind_3960 \n" \
            "Rosalind_2868 Rosalind_6673 \nRosalind_1521 Rosalind_2173 \n" \
            "Rosalind_1521 Rosalind_9476 \nRosalind_1521 Rosalind_1387 \n" \
            "Rosalind_1521 Rosalind_6336 \nRosalind_1581 Rosalind_1935 \n" \
            "Rosalind_8872 Rosalind_2868 \nRosalind_8872 Rosalind_4149 \n" \
            "Rosalind_8872 Rosalind_1049 \nRosalind_8872 Rosalind_5110 \n" \
            "Rosalind_8927 Rosalind_3960 \nRosalind_1935 Rosalind_0311 \n" \
            "Rosalind_1935 Rosalind_7588 \nRosalind_6931 Rosalind_8314 \n" \
            "Rosalind_6931 Rosalind_2566 \nRosalind_5082 Rosalind_9225 \n" \
            "Rosalind_3775 Rosalind_7060 \nRosalind_9225 Rosalind_2037 \n" \
            "Rosalind_9225 Rosalind_9668 \nRosalind_4637 Rosalind_9694 \n" \
            "Rosalind_4637 Rosalind_0271 \nRosalind_4637 Rosalind_9294 \n" \
            "Rosalind_6665 Rosalind_4857 \nRosalind_6665 Rosalind_1917 \n" \
            "Rosalind_6665 Rosalind_6697 \nRosalind_6665 Rosalind_3374 \n" \
            "Rosalind_6665 Rosalind_4429 \nRosalind_8942 Rosalind_0035 \n" \
            "Rosalind_8942 Rosalind_0548 \nRosalind_4266 Rosalind_0425 \n" \
            "Rosalind_7679 Rosalind_9303 \nRosalind_7679 Rosalind_7789 \n" \
            "Rosalind_6936 Rosalind_9694 \nRosalind_6936 Rosalind_0271 \n" \
            "Rosalind_6936 Rosalind_9294 \nRosalind_0035 Rosalind_6673 \n" \
            "Rosalind_9303 Rosalind_0425 \nRosalind_9110 Rosalind_7636 \n" \
            "Rosalind_0425 Rosalind_8606 \nRosalind_0425 Rosalind_9800 \n" \
            "Rosalind_0425 Rosalind_0645 \nRosalind_9795 Rosalind_0444 \n" \
            "Rosalind_0784 Rosalind_9694 \nRosalind_0784 Rosalind_0271 \n" \
            "Rosalind_0784 Rosalind_9294 \nRosalind_4857 Rosalind_0035 \n" \
            "Rosalind_4857 Rosalind_0548 \nRosalind_2385 Rosalind_0444 \n" \
            "Rosalind_6055 Rosalind_8314 \nRosalind_6055 Rosalind_2566 \n" \
            "Rosalind_6412 Rosalind_8606 \nRosalind_6412 Rosalind_9800 \n" \
            "Rosalind_6412 Rosalind_0645 \nRosalind_3656 Rosalind_3068 \n" \
            "Rosalind_3656 Rosalind_6531 \nRosalind_1611 Rosalind_4266 \n" \
            "Rosalind_1611 Rosalind_6055 \nRosalind_1871 Rosalind_1521 \n" \
            "Rosalind_1871 Rosalind_2385 \nRosalind_1871 Rosalind_6202 \n" \
            "Rosalind_0548 Rosalind_1269 \nRosalind_0548 Rosalind_3262 \n" \
            "Rosalind_0548 Rosalind_9921 \nRosalind_1782 Rosalind_9694 \n" \
            "Rosalind_1782 Rosalind_0271 \nRosalind_1782 Rosalind_9294 \n" \
            "Rosalind_7065 Rosalind_6673 \nRosalind_1226 Rosalind_9303 \n" \
            "Rosalind_1226 Rosalind_7789 \nRosalind_1917 Rosalind_0270 \n" \
            "Rosalind_1917 Rosalind_2689 \nRosalind_1917 Rosalind_8950 \n" \
            "Rosalind_9012 Rosalind_2868 \nRosalind_9012 Rosalind_4149 \n" \
            "Rosalind_9012 Rosalind_1049 \nRosalind_9012 Rosalind_5110 \n" \
            "Rosalind_0270 Rosalind_9012 \nRosalind_6654 Rosalind_8983 \n" \
            "Rosalind_6654 Rosalind_8042 \nRosalind_5051 Rosalind_4857 \n" \
            "Rosalind_5051 Rosalind_1917 \nRosalind_5051 Rosalind_6697 \n" \
            "Rosalind_5051 Rosalind_3374 \nRosalind_5051 Rosalind_4429 \n" \
            "Rosalind_9476 Rosalind_6936 \nRosalind_9476 Rosalind_3702 \n" \
            "Rosalind_9800 Rosalind_9303 \nRosalind_9800 Rosalind_7789 \n" \
            "Rosalind_2502 Rosalind_1532 \nRosalind_2502 Rosalind_9795 \n" \
            "Rosalind_2502 Rosalind_5287 \nRosalind_1387 Rosalind_2173 \n" \
            "Rosalind_1387 Rosalind_9476 \nRosalind_1387 Rosalind_6336 \n" \
            "Rosalind_3702 Rosalind_0035 \nRosalind_3702 Rosalind_0548 \n" \
            "Rosalind_3225 Rosalind_8905 \nRosalind_2689 Rosalind_3068 \n" \
            "Rosalind_2689 Rosalind_6531 \nRosalind_5287 Rosalind_7679 \n" \
            "Rosalind_1049 Rosalind_1226 \nRosalind_7599 Rosalind_0448 \n" \
            "Rosalind_2566 Rosalind_4637 \nRosalind_8905 Rosalind_8314 \n" \
            "Rosalind_8905 Rosalind_2566 \nRosalind_3727 Rosalind_2037 \n" \
            "Rosalind_3727 Rosalind_9668 \nRosalind_7636 Rosalind_0311 \n" \
            "Rosalind_7636 Rosalind_7588 \nRosalind_3374 Rosalind_9110 \n" \
            "Rosalind_3374 Rosalind_0914 \nRosalind_0141 Rosalind_4857 \n" \
            "Rosalind_0141 Rosalind_1917 \nRosalind_0141 Rosalind_6697 \n" \
            "Rosalind_0141 Rosalind_3374 \nRosalind_0141 Rosalind_4429 \n" \
            "Rosalind_0311 Rosalind_1782 \nRosalind_0311 Rosalind_4811 \n" \
            "Rosalind_0335 Rosalind_3960 \nRosalind_1269 Rosalind_9110 \n" \
            "Rosalind_1269 Rosalind_0914 \nRosalind_0444 Rosalind_0270 \n" \
            "Rosalind_0444 Rosalind_2689 \nRosalind_0444 Rosalind_8950 \n" \
            "Rosalind_7939 Rosalind_5051 \nRosalind_3960 Rosalind_4637 \n" \
            "Rosalind_8409 Rosalind_4637 \nRosalind_9921 Rosalind_3960 \n" \
            "Rosalind_9668 Rosalind_6936 \nRosalind_9668 Rosalind_3702 \n" \
            "Rosalind_7588 Rosalind_4771 \nRosalind_7588 Rosalind_6873 \n" \
            "Rosalind_0448 Rosalind_6673 \nRosalind_6531 Rosalind_0311 \n" \
            "Rosalind_6531 Rosalind_7588 \nRosalind_8983 Rosalind_8314 \n" \
            "Rosalind_8983 Rosalind_2566 \nRosalind_6336 Rosalind_0035 \n" \
            "Rosalind_6336 Rosalind_0548 \nRosalind_0645 Rosalind_2173 \n" \
            "Rosalind_0645 Rosalind_9476 \nRosalind_0645 Rosalind_1387 \n" \
            "Rosalind_0645 Rosalind_6336 \nRosalind_7060 Rosalind_6936 \n" \
            "Rosalind_7060 Rosalind_3702 \nRosalind_8950 Rosalind_3656 \n" \
            "Rosalind_0271 Rosalind_0448 \nRosalind_6673 Rosalind_1782 \n" \
            "Rosalind_6673 Rosalind_4811 \nRosalind_4771 Rosalind_8905 \n" \
            "Rosalind_6873 Rosalind_7060 \nRosalind_8042 Rosalind_3960 \n" \
            "Rosalind_5110 Rosalind_1581 \nRosalind_5110 Rosalind_3225 \n" \
            "Rosalind_5110 Rosalind_7939 \nRosalind_2785 Rosalind_3775 \n" \
            "Rosalind_4811 Rosalind_6654 \nRosalind_7789 Rosalind_7636 \n" \
            "Rosalind_9294 Rosalind_8942 \nRosalind_9294 Rosalind_3727 \n" \
            "Rosalind_6202 Rosalind_8872 \nRosalind_4429 Rosalind_2576 \n" \
            "Rosalind_4429 Rosalind_6931 \nRosalind_4429 Rosalind_8409 \n"

        # make sure solution matches computed result
        self.assertEqual(solution_raw, adjacency_raw)
        self.assertEqual(solution_formatted, adjacency_formatted)

    def test_grph_negative(self):
        grph_data = parse_gc_data("rosalind_grph_4.txt")
        adjacency_raw = grph(grph_data)
        adjacency_formatted = format_output(adjacency_raw)

        solution_raw = []
        solution_formatted = ""

        # make sure solution matches computed result
        self.assertEqual(solution_raw, adjacency_raw)
        self.assertEqual(solution_formatted, adjacency_formatted)


if __name__ == '__main__':
    unittest.main()
