"""
gasm.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Genome Assembly Using Reads

Given: A collection S of (error-free) reads of equal length (not exceeding 50
bp). In this dataset, for some positive integer k, the de Bruijn graph Bk on
Sk+1∪Srck+1 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its
reverse complement.
"""

from revc import revc
from parsers import parse_gasm_data


def gasm(dna):
    """Return a cyclic minimal length superstring given DNA reads and their
    reverse complement

    :param dna: set of error free DNA reads
    :return: a cyclic superstring based on the DNA reads and thier complements
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

    return


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
    dna_reads = parse_gasm_data("rosalind_gasm_1.txt")
    dna_reads = list(set(dna_reads + [revc(i) for i in dna_reads]))
    # print(dna_reads)
    cyclic_superstring = gasm(dna_reads)
    print(cyclic_superstring)
