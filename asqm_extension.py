"""
asqm_extension.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Assessing Assembly Quality with N50 and N75 solved by 283
Problem
Given a collection of DNA strings representing contigs, we use the N statistic NXX (where XX ranges from 01 to 99) to represent the maximum positive integer L such that the total number of nucleotides of all contigs having length ≥L is at least XX% of the sum of contig lengths. The most commonly used such statistic is N50, although N75 is also worth mentioning.

Given: A collection of at most 1000 DNA strings (whose combined length does not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
"""

from asqm import nxx
from sample_data_generator import *
from outputify import *


def extension_metric(data_set, pct=50):
    """Generate new metric based on nxx and lxx score

    :param data_set: set of contigs
    :param pct: percentage threshold for N and L scoring
    :return: new blended metric
    """
    nxx_score = nxx(data_set, pct)
    lxx_score = lxx(data_set, pct)

    max_contig_len = len(max(data_set, key=len))

    # blended_metric = (max_contig_len + nxx_score) / lxx_score
    blended_metric = (max_contig_len - nxx_score)  # spread between N50 and largest contig

    return blended_metric


def comparative_scoring_analysis(dna_set, pct, ref_genome):
    """Return metrics for assembly: NXX, UXX, UGXX and L50 and dna set composition

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for UG score
    :param ref_genome: reference genome
    :return: all score metrics and data set breakdown
    """

    scoring_metrics = dict()

    scoring_metrics[f"N{pct}"] = nxx(dna_set, pct)
    scoring_metrics[f"U{pct}"] = uxx(dna_set, pct, ref_genome)
    scoring_metrics[f"UG{pct}"] = ugxx(dna_set, pct, ref_genome)
    scoring_metrics[f"UG{pct}%"] = round(ugxx(dna_set, pct, ref_genome, pct), 5)
    scoring_metrics[f"L{pct}"] = lxx(dna_set, pct)
    scoring_metrics[f"EXT{pct}"] = round(extension_metric(dna_set, pct), 5)
    # percent composition of short, medium and long contigs
    contig_info = count_contig_pct(dna_set)
    scoring_metrics["CONTIG_NUM"] = (contig_info[-1])
    scoring_metrics["CONTIG_SM_PCT"] = round(contig_info[0] * 100, 3)
    scoring_metrics["CONTIG_MD_PCT"] = round(contig_info[1] * 100, 3)
    scoring_metrics["CONTIG_LG_PCT"] = round(contig_info[2] * 100, 3)

    return scoring_metrics


def uxx(dna_set, pct, ref_genome):
    """Return the U50 score of a given set of DNA contigs and reference genome

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for U score
    :param ref_genome: reference genome
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    # initialization
    ref_genome = ref_genome  # extract the ref genome string
    coordinates = []
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))]  # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)

    # finding start and end coordinates of contigs given ref genome
    for contig in sorted_contigs:
        start = ref_genome.index(contig)
        end = ref_genome.index(contig) + len(contig)
        coordinates.append((start, end))

    # finding unique contig length
    for coordinate in coordinates:
        unique_length = 0
        start = coordinate[0]
        end = coordinate[1]
        for i in range(start, end):
            if mask_array[i] == 0:
                mask_array[i] = 1
                unique_length = unique_length + 1
        unique_contig_length.append(unique_length)

    # cutoff defined as the sum of length times the threshold precentage
    cutoff = sum(unique_contig_length) * (pct / 100)
    running_sum = 0
    for contig_length in unique_contig_length:
        running_sum = running_sum + contig_length
        if running_sum >= cutoff:
            return contig_length


def ugxx(dna_set, pct, ref_genome, percentage=None):
    """Return the UG50 score of a given set of DNA contigs and reference genome

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for UG score
    :param ref_genome: reference genome
    :param percentage: UGxx% statistics instead of UGxx, default is UGxx
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    # initialization
    ref_genome = ref_genome  # extract the ref genome string
    coordinates = []
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))]  # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)

    # finding start and end coordinates of contigs given ref genome
    for contig in sorted_contigs:
        start = ref_genome.index(contig)
        end = ref_genome.index(contig) + len(contig)
        coordinates.append((start, end))

    # finding unique contig length
    for coordinate in coordinates:
        unique_length = 0
        start = coordinate[0]
        end = coordinate[1]
        for i in range(start, end):
            if mask_array[i] == 0:
                mask_array[i] = 1
                unique_length = unique_length + 1
        unique_contig_length.append(unique_length)

    # cutoff defined as the the length of ref genome times the threshold percentage
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
    sorted_contigs = sorted(dna_set, key=len, reverse=True)
    cutoff = len(''.join(sorted_contigs)) * (pct / 100)
    running_sum = 0
    ctr = 0
    for contig in sorted_contigs:
        ctr = ctr + 1
        running_sum = running_sum + len(contig)
        if running_sum >= cutoff:
            return ctr


def experimental_analysis(genome_size, scoring_pct):
    # compare skews between contig sizes

    ref_genome = generate_random_contig(genome_size)

    # 250 contigs generated with even spread of small, medium and large lengths
    contig_set_control = generate_contigs_by_percentage_from_genome(ref_genome)
    # 250 contigs generated with skews of 75% for each of small, medium and large lengths
    contig_set_sm_skew = generate_contigs_by_percentage_from_genome(ref_genome, 0.75, 0.125, 0.125)
    contig_set_md_skew = generate_contigs_by_percentage_from_genome(ref_genome, 0.125, 0.75, 0.125)
    contig_set_lg_skew = generate_contigs_by_percentage_from_genome(ref_genome, 0.125, 0.125, 0.75)

    comparative_scoring_set_control = comparative_scoring_analysis(contig_set_control, scoring_pct, ref_genome)
    comparative_scoring_set_sm_skew = comparative_scoring_analysis(contig_set_sm_skew, scoring_pct, ref_genome)
    comparative_scoring_set_md_skew = comparative_scoring_analysis(contig_set_md_skew, scoring_pct, ref_genome)
    comparative_scoring_set_lg_skew = comparative_scoring_analysis(contig_set_lg_skew, scoring_pct, ref_genome)

    return comparative_scoring_set_control, comparative_scoring_set_sm_skew, comparative_scoring_set_md_skew, \
        comparative_scoring_set_lg_skew


if __name__ == '__main__':
    # reference genome of len 500
    ref_genome_size = 500

    # normalized data for 50% scoring
    scoring_pct = 50

    control, sm, md, lg = experimental_analysis(ref_genome_size, scoring_pct)
    outputify_comparative_scoring_analysis(control, sm, md, lg)
