"""
asqm_extension.py file containing the implementation of the extension algorithms
for assessing assembly quality scoring metrics

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

"""

from asmq import asmq
from sample_data_generator import generate_error_sample, count_contig_pct, \
    generate_contigs_by_percentage_from_genome, generate_random_contig
from outputify import outputify_comparative_scoring_analysis_with_errors, \
    outputify_comparative_scoring_analysis


# the range of errors to test with
PCT_ERRS = [0.05, 0.1, .25, .50]


def uaxx(data_set, pct, ref_genome, index_set):
    """Compute the unique alignment metric

    :param data_set: set of contigs as list of strings
    :param pct: percentage threshold for N and L scoring
    :param ref_genome: reference genome as a single string
    :param index_set: a dict of indices and their start/stop indices in the
                        reference genome
    :return: the UAXX score
    """

    uaxx_score = int()
    aligned_contigs = []
    aligned_index_set = []
    new_contigs = []
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))]  # initialize mask array

    for contig in data_set:
        correct_contigs = find_correct_contigs(contig, ref_genome)
        # error joint split into contig blocks
        if len(correct_contigs) > 1:
            # keep track of the new contig blocks
            new_contigs = new_contigs + correct_contigs
        aligned_contigs = aligned_contigs + correct_contigs

    # aligned_index_set only contains correct aligned contigs
    for index in index_set:
        if index[0] in aligned_contigs:
            aligned_index_set.append(index)

    # add index for newly added aligned contig blocks
    for new_contig in new_contigs:
        aligned_index_set.append([new_contig, (ref_genome.index(new_contig),
                                               ref_genome.index(
                                                   new_contig) + len(
                                                   new_contig))])

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(aligned_contigs, key=len, reverse=True)
    sorted_index = sorted(
        aligned_index_set, key=lambda x: len(x[0]), reverse=True
    )

    # finding unique contig length
    for j in range(len(sorted_contigs)):
        unique_length = 0
        start = sorted_index[j][1][0]
        end = sorted_index[j][1][1]
        for i in range(start, end):
            if mask_array[i] == 0:
                mask_array[i] = 1
                unique_length = unique_length + 1
        unique_contig_length.append(unique_length)

    unique_contig_length = sorted(unique_contig_length, reverse=True)

    # cutoff defined as the sum of length times the threshold percentage
    cutoff = sum(unique_contig_length) * (pct / 100)
    running_sum = 0
    for contig_length in unique_contig_length:
        running_sum = running_sum + contig_length
        if running_sum >= cutoff:
            return contig_length

    return uaxx_score


def find_correct_contigs(contig, ref_genome):
    """ Returns the 'correct' set of contigs where each contig is aligned with
    the ref_genome

    :param contig: a string of dna 
    :param ref_genome: reference genome as a string
    :return: Set of contigs as a list of strings
    """

    correct_contigs = []
    if contig in ref_genome:  # contig aligned with ref genome
        correct_contigs.append(contig)
        return correct_contigs
    else:  # contig not aligned
        kmer = len(contig) // 2

        # first half of contig
        correct_contigs = correct_contigs + find_correct_contigs(
            contig[:kmer], ref_genome)
        # second half of contig
        correct_contigs = correct_contigs + find_correct_contigs(
            contig[kmer:], ref_genome)

    return correct_contigs


def comparative_scoring_analysis(dna_set, pct, ref_genome, index_set,
                                 err_set=False):
    """Return metrics for assembly: NXX, UXX, UGXX and L50 and DNA set
    composition

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for metric scores
    :param ref_genome: reference genome
    :param err_set: is the data set induced with simulated errors
    :return: all score metrics and data set breakdown
    """

    scoring_metrics = dict()

    scoring_metrics[f"N{pct}"] = asmq(dna_set, pct)
    scoring_metrics[f"UA{pct}"] = round(
        uaxx(dna_set, pct, ref_genome, index_set), 5)

    if not err_set:
        scoring_metrics[f"U{pct}"] = uxx(dna_set, pct, ref_genome, index_set)
        scoring_metrics[f"UG{pct}pct"] = round(
            ugxx(dna_set, pct, ref_genome, index_set, pct), 5)
        scoring_metrics[f"L{pct}"] = lxx(dna_set, pct, len(ref_genome))

    # percent composition of short, medium and long contigs
    contig_info = count_contig_pct(dna_set)

    scoring_metrics["CONTIG_NUM"] = (contig_info[-1])
    scoring_metrics["CONTIG_SM_PCT"] = round(contig_info[0] * 100, 3)
    scoring_metrics["CONTIG_MD_PCT"] = round(contig_info[1] * 100, 3)
    scoring_metrics["CONTIG_LG_PCT"] = round(contig_info[2] * 100, 3)

    return scoring_metrics


def uxx(dna_set, pct, ref_genome, index_set):
    """Return the UXX score of a given set of DNA contigs and reference genome

    :param dna_set: list of DNA contigs with each contig as a single string
    :param pct: percentage threshold for UG score
    :param ref_genome: reference genome given as a single string
    :return: UXX score
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    # initialization
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))]  # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)
    sorted_index = sorted(index_set, key=lambda x: len(x[0]), reverse=True)

    # finding unique contig length
    for j in range(len(sorted_contigs)):
        unique_length = 0
        start = sorted_index[j][1][0]
        end = sorted_index[j][1][1]
        for i in range(start, end):
            if mask_array[i] == 0:
                mask_array[i] = 1
                unique_length = unique_length + 1
        unique_contig_length.append(unique_length)

    unique_contig_length = sorted(unique_contig_length, reverse=True)

    # cutoff defined as the sum of length times the threshold precentage
    cutoff = sum(unique_contig_length) * (pct / 100)
    running_sum = 0
    for contig_length in unique_contig_length:
        running_sum = running_sum + contig_length
        if running_sum >= cutoff:
            return contig_length


def ugxx(dna_set, pct, ref_genome, index_set, percentage=None):
    """Return the UGXX score of a given set of DNA contigs and reference genome

    :param dna_set: list of DNA contigs with each contig as a single string
    :param pct: percentage threshold for UG score
    :param ref_genome: reference genome given as a single string
    :param percentage: UGxx% statistics instead of UGxx, default is UGxx
    :return: UGXX score or UGXX% score
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    # initialization
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))]  # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)
    sorted_index = sorted(index_set, key=lambda x: len(x[0]), reverse=True)

    # finding unique contig length
    for j in range(len(sorted_contigs)):
        unique_length = 0
        start = sorted_index[j][1][0]
        end = sorted_index[j][1][1]
        for i in range(start, end):
            if mask_array[i] == 0:
                mask_array[i] = 1
                unique_length = unique_length + 1
        unique_contig_length.append(unique_length)

    unique_contig_length = sorted(unique_contig_length, reverse=True)

    # cutoff defined as the the length of ref genome times the threshold
    # percentage
    cutoff = len(ref_genome) * (pct / 100)
    running_sum = 0

    for contig_length in unique_contig_length:
        running_sum = running_sum + contig_length
        if running_sum >= cutoff:
            if percentage:
                return 100 * (contig_length / len(ref_genome))  # UG50%
            else:
                return contig_length  # UG50


def lxx(dna_set, pct):
    """Return the LXX score of a given set of DNA contigs and reference genome

    :param dna_set: list of DNA contigs with each contig as a single string
    :param pct: percentage threshold for L score
    :return: LXX score
    """

    sorted_contigs = sorted(dna_set, key=len, reverse=True)
    cutoff = len(''.join(sorted_contigs)) * (pct / 100)
    running_sum = 0
    ctr = 0

    for contig in sorted_contigs:
        ctr = ctr + 1
        running_sum = running_sum + len(contig)
        if running_sum >= cutoff:
            return ctr


def experimental_analysis(genome_size, scoring_pct, contig_set_size):
    """Conduct the experimental analysis on each metric given data set
    parameters

    :param genome_size: size of the genome
    :param scoring_pct: percentage to use for the scoring metrics
    :param contig_set_size: number of contigs oer data set
    :return: dictionary of data for all metrics given data set parameters
    """

    # compare skews between contig sizes

    ref_genome = generate_random_contig(genome_size)

    # 250 contigs generated with even spread of small, medium and large lengths
    contig_set_control, indx_set_control = \
        generate_contigs_by_percentage_from_genome(
            ref_genome, num=contig_set_size
        )

    # 250 contigs generated with skews of 75% for each of small, medium and
    # large lengths
    contig_set_sm_skew, indx_set_sm = \
        generate_contigs_by_percentage_from_genome(ref_genome, 0.75, 0.125,
                                                   0.125, num=contig_set_size)
    contig_set_md_skew, indx_set_md = \
        generate_contigs_by_percentage_from_genome(ref_genome, 0.125, 0.75,
                                                   0.125, num=contig_set_size)
    contig_set_lg_skew, indx_set_lg = \
        generate_contigs_by_percentage_from_genome(ref_genome, 0.125, 0.125,
                                                   0.75, num=contig_set_size)

    comparative_scoring_set_control = comparative_scoring_analysis(
        contig_set_control, scoring_pct, ref_genome, indx_set_control
    )
    comparative_scoring_set_sm_skew = comparative_scoring_analysis(
        contig_set_sm_skew, scoring_pct, ref_genome, indx_set_sm
    )
    comparative_scoring_set_md_skew = comparative_scoring_analysis(
        contig_set_md_skew, scoring_pct, ref_genome, indx_set_md
    )
    comparative_scoring_set_lg_skew = comparative_scoring_analysis(
        contig_set_lg_skew, scoring_pct, ref_genome, indx_set_lg
    )

    return comparative_scoring_set_control, comparative_scoring_set_sm_skew, \
        comparative_scoring_set_md_skew, comparative_scoring_set_lg_skew


def experimental_analysis_with_error(ref_genome, contig_set,
                                     scoring_pct, index_set):
    """Conduct the experimental analysis on each metric given data set
    parameters, given simulate erroneous data

    :param ref_genome: the reference genome
    :param genome_size: size of the genome
    :param scoring_pct: percentage to use for the scoring metrics
    :param contig_set_size: number of contigs oer data set
    :return: dictionary of data for all metrics given data set parameters
    """

    comparative_scoring_set_control = comparative_scoring_analysis(
        contig_set, scoring_pct, ref_genome, index_set, err_set=True
    )

    return comparative_scoring_set_control


def generate_skewed_data_analysis(genome_size, num_contigs, score_pct):
    """Generate the analytics of a contig data set

    :param genome_size: size of the reference genome
    :param num_contigs: number of contigs in the data set
    :param score_pct: percentage used for metric score
    :return: set of data for analysis of the contig set
    """

    ctrl, sml, mdm, lrg = experimental_analysis(
        genome_size, score_pct, num_contigs
    )

    return ctrl, sml, mdm, lrg


def generate_n_vs_ua_data_analysis(genome_size, num_contigs, score_pct):
    """Generate data for the N50 vs UA50 experiment

    :param genome_size: the size of the reference genome
    :param num_contigs: number of contigs in the data set
    :param score_pct: percentage of scoring to use for the metrics
    :return: data set as a dictionary of the comparative metric measures
    """

    accumulated_err_results = dict()

    reference_genome = generate_random_contig(genome_size)

    contig_set_control, index_set_control = \
        generate_contigs_by_percentage_from_genome(
            reference_genome, 0.50, 0.25, 0.25, num_contigs
        )

    for pct_err in PCT_ERRS:
        contig_error_set = generate_error_sample(
            contig_set_control, reference_genome, pct_error=pct_err
        )

        error_results = experimental_analysis_with_error(
            reference_genome, contig_error_set, score_pct, index_set_control
        )

        accumulated_err_results[f"{pct_err * 100}"] = error_results

    return accumulated_err_results


if __name__ == '__main__':
    # reference genome of len 500
    ref_genome_size = 5000

    # number of contigs in data set
    contig_genome_scale = 2.25  # percent ratio of contigs to ref_genome_size
    contig_set_size = contig_genome_scale * ref_genome_size

    # normalized data for 50% scoring
    scoring_pct = 50

    control, sm, md, lg = generate_skewed_data_analysis(ref_genome_size,
                                                        contig_set_size,
                                                        scoring_pct)

    outputify_comparative_scoring_analysis(control, sm, md, lg)

    generate_n_vs_ua_data_analysis(
        ref_genome_size, contig_set_size, scoring_pct
    )

    pct_errs = [0.05, 0.1, .25, .50]

    ref_genome = generate_random_contig(ref_genome_size)

    contig_set_control, index_set_control = \
        generate_contigs_by_percentage_from_genome(
            ref_genome, 0.50, 0.25, 0.25, contig_set_size
        )

    # print(contig_set_control[0])
    # print(ref_genome[index_set_control[0][0] : index_set_control[0][1]])

    for pct_err in pct_errs:
        contig_error_set = generate_error_sample(contig_set_control, ref_genome,
                                                 pct_error=pct_err)

        error_results = experimental_analysis_with_error(
            ref_genome, contig_error_set, scoring_pct, index_set_control
        )

        outputify_comparative_scoring_analysis_with_errors(
            error_results, scoring_pct, pct_err
        )
