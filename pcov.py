"""
pcov.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Genome Assembly with Perfect Coverage

Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same
strand of a circular chromosome. In this dataset, all k-mers from this strand
of the chromosome are present, and their de Bruijn graph consists of exactly
one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus
corresponding to a candidate cyclic chromosome).
"""

from parsers import parse_gasm_data


def pcov(dna):
    """Return a cyclic minimal length superstring given DNA reads

    :param dna: set of error free DNA reads
    :return: a cyclic superstring based on the DNA read
    """

    # base case
    if not dna:
        return ""

    l = len(dna[0])

    for k in range(l - 1, 1, -1):
        adj = get_adj(dna, l, k)
        first = kmer = next(iter(adj))
        superstr = ''

        while True:
            if kmer in adj:
                superstr += kmer[-1]
                kmer = adj.pop(kmer)
                if kmer == first:
                    return superstr
            else:
                break

    return ""


def get_adj(dna, length, k):
    """Get the adjacency list of the set of DNA reads

    :param dna: set of DNA reads
    :param length: length of DNA reads
    :param k: k-mer overlap of reads
    :return: adjacency list of DNA reads
    """

    adj = dict()
    for d in dna:
        for i in range(length - k):
            adj[d[i:i + k]] = d[i + 1:i + k + 1]
    return adj


if __name__ == '__main__':
    dna_reads = parse_gasm_data("rosalind_pcov_4.txt")
    # print(dna)
    superstring = pcov(dna_reads)
    print(superstring)
