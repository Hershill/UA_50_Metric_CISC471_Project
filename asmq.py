"""
asqm.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Assessing Assembly Quality with N50 and N75

Problem

Given a collection of DNA strings representing contigs, we use the N
statistic NXX (where XX ranges from 01 to 99) to represent the maximum
positive integer L such that the total number of nucleotides of all contigs
having length ≥L is at least XX% of the sum of contig lengths. The most
commonly used such statistic is N50, although N75 is also worth mentioning.

Given: A collection of at most 1000 DNA strings (whose combined length does
not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
"""

from helpers import get_len_of_genome
from parsers import parse_assembly_data
from sorting_algorithms import bubble_sort
from copy import deepcopy


# sorting algos available to use
SORTING_ALGOS = {
    'bubble': bubble_sort
}


def asmq(dna_set, pct, sorting_algo=None):
    """Return the NXX score of a given set of DNA contigs

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for
                    N score
    :param sorting_algo: algo to use to sort contigs, None is default
                    and uses Python's built-in max function
    :return: corresponding N score, which is length of contig (L) where pct
                    amount of contigs have length > L
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    # create a copy of the set of contigs to avoid manipulating the original set
    dna_set_copy = deepcopy(dna_set)
    track_sum = 0  # keeps track of sum so far after looking at each contig
    curr_contig_len = 0  # length of contig we are currently looking at

    genome_len = get_len_of_genome(dna_set)

    # get target based on passed in value of pct
    target_len = genome_len * (pct / 100)

    if sorting_algo:
        # sort dna_set based on specified sorting algo
        sorted_contigs = SORTING_ALGOS[sorting_algo](dna_set_copy)
        print(sorted_contigs)
        for contig in sorted_contigs:
            curr_contig_len = len(contig)
            track_sum += curr_contig_len
            if track_sum >= target_len:
                break

    elif not sorting_algo:
        # use Python's built-in max function
        while track_sum <= target_len:
            # get largest contig in list
            longest_contig = max(dna_set_copy, key=len)
            curr_contig_len = len(longest_contig)
            track_sum += curr_contig_len
            dna_set_copy.remove(longest_contig)

    return curr_contig_len


if __name__ == '__main__':
    filename = "rosalind_asmq_2.txt"
    dna_set = parse_assembly_data(filename)

    n50 = asmq(dna_set, 50)
    n75 = asmq(dna_set, 75)
    print(n50, n75)
