"""
algorithms.py file containing the implementation of the algorithms

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

from helpers import *
from parsers import *
from sorting_algorithms import *
from random_contig_set_generator import *
from copy import deepcopy


# sorting algos available to use
SORTING_ALGOS = {
    'bubble': bubble_sort
}


def nxx(dna_set, pct, sorting_algo=None):
    """Return the NXX score of a given set of DNA contigs

    :param dna_set: list of DNA contigs
    :param pct: percentage threshold for N score
    :param sorting_algo: algo to use to sort contigs, None is default and uses Python's built-in max function
    :return: corresponding N score, which is length of contig (L) where pct amount of contigs have length > L
    """

    # base case: if the dna set is emp
    if not dna_set:
        return 0

    dna_set_copy = deepcopy(dna_set)  # create a copy of the set of contigs to avoid manipulating the original set
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
    ref_genome = ref_genome[0] # extract the ref genome string 
    coordinates = []
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))] # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)

    # finding start and end coordinates of contigs given ref genome
    for contig in sorted_contigs:
        start = ref_genome.index(contig)
        end = ref_genome.index(contig) + len(contig)
        coordinates.append((start,end))
    
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
    cutoff = sum(unique_contig_length) * (pct/100)
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
    ref_genome = ref_genome[0] # extract the ref genome string 
    coordinates = []
    unique_contig_length = []
    mask_array = [0 for x in range(len(ref_genome))] # initialize mask array

    # sorting contigs from longest to the shortest
    sorted_contigs = sorted(dna_set, key=len, reverse=True)

    # finding start and end coordinates of contigs given ref genome
    for contig in sorted_contigs:
        start = ref_genome.index(contig)
        end = ref_genome.index(contig) + len(contig)
        coordinates.append((start,end))
    
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
    cutoff = len(ref_genome) * (pct/100)
    running_sum = 0

    for contig_length in unique_contig_length:
        running_sum = running_sum + contig_length
        if running_sum >= cutoff:
            if percentage:
                return 100*(contig_length/len(ref_genome)) # UG50%
            else:
                return contig_length # UG50

def lxx(dna_set, pct):
    sorted_contigs = sorted(dna_set, key=len, reverse=True)
    cutoff = len(''.join(sorted_contigs)) * (pct/100)
    running_sum = 0
    ctr = 0
    for contig in sorted_contigs:
        ctr = ctr + 1
        running_sum = running_sum + len(contig)
        if running_sum >= cutoff:
            return ctr

if __name__ == '__main__':
    filename = "sample_data.txt"
    filename1 = "sample_ref_genome.txt"
    dna_set = parse_assembly_data(filename)
    ref_genome = parse_assembly_data(filename1)
    print(dna_set)
    print(ref_genome)

    l50 = lxx(dna_set, 50)
    print(l50)

    u50 = uxx(dna_set, 50, ref_genome)
    print(u50)

    ug50 = ugxx(dna_set, 50, ref_genome)
    print(ug50)

    ug50p = ugxx(dna_set, 50, ref_genome, True)
    print(ug50p)

    n50 = nxx(dna_set, 50)
    print(n50)

    n75 = nxx(dna_set, 75)
    print(n75)

    # using bubble sort
    n50 = nxx(dna_set, 50, 'bubble')
    print(n50)

    # using generated sample data
    # TODO: need a way to verify this data with unittests, no way to prove our answers without Rosalind sample data
    generated_set = generate_random_seq_set()
    n50 = nxx(generated_set, 50)
    # print(generated_set)
    print(f"Generated Set N50: {n50}")
