"""
algorithms.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)
"""

from helpers import *
from copy import deepcopy


def nxx(dna_set, pct):
    """we use the N statistic NXX (where XX ranges from 01 to 99) to represent the maximum positive integer L such that
    the total number of nucleotides of all contigs having length ≥L is at least XX% of the sum of contig lengths.
    """
    temp = deepcopy(dna_set)
    track_sum = 0  # keeps track of sum so far after looking at each contig
    curr_contig_len = 0  # length of contig we are currently looking at

    genome_len = get_len_of_genome(dna_set)

    # get target based on passed in value of pct
    target_len = genome_len * (pct / 100)

    while track_sum <= target_len:
        # get largest contig in list
        longest_contig = max(temp, key=len)
        curr_contig_len = len(longest_contig)
        track_sum += curr_contig_len
        temp.remove(longest_contig)

    return curr_contig_len


if __name__ == '__main__':
    filename = "sample_data.txt"
    dna_set = parse_data(filename)
    print(dna_set)
    n50 = nxx(dna_set, 50)
    print(n50)

    n75 = nxx(dna_set, 75)
    print(n75)

