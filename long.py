"""
long.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Genome Assembly as Shortest Superstring

Problem

For a collection of strings, a larger string containing every one of the
smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a
collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1
kbp, in FASTA format (which represent reads deriving from the same strand of
a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a
unique way to reconstruct the entire chromosome from these reads by gluing
together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome).
"""

from parsers import parse_gc_data


def long(fasta_sets):
    """Return the

    :param fasta_sets:
    :return:
    """
    dna_set = list(fasta_sets.values())
    superstr = find_superstring(dna_set)
    return superstr


def find_superstring(dna_set, dna=''):
    """

    :param dna_set:
    :param dna:
    :return:
    """

    if len(dna_set) == 0:
        return dna

    elif len(dna) == 0:
        dna = dna_set.pop(0)
        return find_superstring(dna_set, dna)

    else:
        for i in range(len(dna_set)):
            dna1 = dna_set[i]
            for j in range(len(dna1) // 2):
                idx = len(dna1) - j
                if dna.startswith(dna1[j:]):
                    dna_set.pop(i)
                    return find_superstring(dna_set, dna1[:j] + dna)
                if dna.endswith(dna1[:idx]):
                    dna_set.pop(i)
                    return find_superstring(dna_set, dna + dna1[idx:])

    return


if __name__ == '__main__':
    filename = "rosalind_long_2.txt"
    FASTA_data = parse_gc_data(filename)
    # print(FASTA_data)
    superstring = long(FASTA_data)
    print(superstring)
