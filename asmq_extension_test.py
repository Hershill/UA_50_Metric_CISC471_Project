"""
asmq_extension_test.py file that runs the unittests for asmq_extension.py when
the file is called or run using the python CLI.

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
from asmq_extension import experimental_analysis_with_error
from sample_data_generator import generate_contigs_by_percentage, \
    count_contig_pct, generate_error_sample, generate_random_contig, \
    generate_contigs_by_percentage_from_genome

REF_GENOME_SIZE = 500
CONTIG_GENOME_SCALE = 1.25  # percent ratio of contigs to REF_GENOME_SIZE
CONTIG_SET_SIZE = CONTIG_GENOME_SCALE * REF_GENOME_SIZE


class TestProgrammingProblemASMQ(unittest.TestCase):
    """Testing class for the required unittests
    """

    def test_asmq_ext_positive_a(self):
        # test uaxx and assert error data gives same result
        pct_errs = [0.05, 0.1, .25, .50]

        ref_genome = generate_random_contig(REF_GENOME_SIZE)

        contig_set_control, index_set_control = \
            generate_contigs_by_percentage_from_genome(
                ref_genome, 0.50, 0.25, 0.25, CONTIG_SET_SIZE
            )

        ua_score_set = list()

        for pct_err in pct_errs:
            contig_error_set = generate_error_sample(
                contig_set_control, ref_genome, pct_error=pct_err
            )

            error_results = experimental_analysis_with_error(
                ref_genome, contig_error_set, 50, index_set_control
            )

            ua_score_set.append(error_results['UA50'])

        self.assertEqual(ua_score_set[0], ua_score_set[1])
        self.assertEqual(ua_score_set[0], ua_score_set[2])
        self.assertEqual(ua_score_set[0], ua_score_set[3])

    def test_asmq_ext_positive_b(self):
        # test uaxx and assert error data gives same result
        pct_errs = [0.15, 0.20, .35, .40]

        ref_genome = generate_random_contig(REF_GENOME_SIZE)

        contig_set_control, index_set_control = \
            generate_contigs_by_percentage_from_genome(
                ref_genome, 0.50, 0.25, 0.25, CONTIG_SET_SIZE
            )

        ua_score_set = list()

        for pct_err in pct_errs:
            contig_error_set = generate_error_sample(
                contig_set_control, ref_genome, pct_error=pct_err
            )

            error_results = experimental_analysis_with_error(
                ref_genome, contig_error_set, 50, index_set_control
            )

            ua_score_set.append(error_results['UA50'])

        self.assertEqual(ua_score_set[0], ua_score_set[1])
        self.assertEqual(ua_score_set[0], ua_score_set[2])
        self.assertEqual(ua_score_set[0], ua_score_set[3])

    def test_asmq_ext_positive_c(self):
        # test uaxx and assert error data gives same result on large range of
        # error percentages
        pct_errs = [0.05, 0.10, .15, .35, .45]

        ref_genome = generate_random_contig(REF_GENOME_SIZE)

        contig_set_control, index_set_control = \
            generate_contigs_by_percentage_from_genome(
                ref_genome, 0.50, 0.25, 0.25, CONTIG_SET_SIZE
            )

        ua_score_set = list()

        for pct_err in pct_errs:
            contig_error_set = generate_error_sample(
                contig_set_control, ref_genome, pct_error=pct_err
            )

            error_results = experimental_analysis_with_error(
                ref_genome, contig_error_set, 50, index_set_control
            )

            ua_score_set.append(error_results['UA50'])

        self.assertEqual(ua_score_set[0], ua_score_set[1])
        self.assertEqual(ua_score_set[0], ua_score_set[2])
        self.assertEqual(ua_score_set[0], ua_score_set[3])
        self.assertEqual(ua_score_set[0], ua_score_set[4])

    def test_asmq_ext_negative(self):
        # test uaxx and assert error data gives same result on large range of
        # error percentages
        pct_errs = [0.05, 0.10, 0.15]

        ref_genome = generate_random_contig(REF_GENOME_SIZE)

        contig_set_control, index_set_control = \
            generate_contigs_by_percentage_from_genome(
                ref_genome, 0.50, 0.50, 0.25, CONTIG_SET_SIZE
            )

        self.assertEqual(contig_set_control, [])
        self.assertEqual(index_set_control, [])

    def test_sample_data_generation(self):
        # test sample data generator and assert percentages match
        # almostEquals assert is used due to rounding since all parameters
        # for number of contigs and percentage breakdown is not evenly divisible

        # test defaults
        sm, md, lg = 1/3, 1/3, 1/3
        sample_data_default = generate_contigs_by_percentage(
            small=sm, medium=md, large=lg
        )
        pcts = count_contig_pct(sample_data_default)

        # assert small, medium and large are in range
        self.assertAlmostEqual(sm, pcts[0], places=2)
        self.assertAlmostEqual(md, pcts[1], places=2)
        self.assertAlmostEqual(lg, pcts[2], places=2)

        # assert num contigs generated matches
        self.assertAlmostEqual(len(sample_data_default), pcts[-1])

        # test skew
        sm, md, lg = .25, .25, .50
        sample_data_default = generate_contigs_by_percentage(
            small=sm, medium=md, large=lg
        )
        pcts = count_contig_pct(sample_data_default)

        # assert small, medium and large are in range
        self.assertAlmostEqual(sm, pcts[0], places=2)
        self.assertAlmostEqual(md, pcts[1], places=2)
        self.assertAlmostEqual(lg, pcts[2], places=2)

        # assert num contigs generated matches
        self.assertAlmostEqual(len(sample_data_default), pcts[-1])


if __name__ == '__main__':
    unittest.main()
