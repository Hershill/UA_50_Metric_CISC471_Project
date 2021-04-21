"""
iprd.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant
phenotype). Assume that any two organisms can mate.
"""

from parsers import parse_iprb_data


def iprb(k, m, n):
    """Calculate the probability that two randomly selected mating organisms
    will produce an offspring with at least one dominant allele present for
    the given trait

    :param k: number of homozygous dominant organisms
    :param m: number of heterozygous organisms
    :param n: number of homozygous recessive organisms
    :return: probability that two randomly selected mating organisms will
                produce an offspring with at least one dominant allele
    """

    k = int(k)
    m = int(m)
    n = int(n)

    if k == 0 or m == 0 or n == 0:
        return 0

    total = k + m + n

    DD = k / total * ((k - 1) / (total - 1)) * 1 + k / total * (
            m / (total - 1)) * 1 + k / total * (n / (total - 1)) * 1
    Dd = m / total * (k / (total - 1)) * 1 + m / total * (
            (m - 1) / (total - 1)) * (3 / 4) + m / total * (
                 n / (total - 1)) * (2 / 4)
    dd = n / total * (k / (total - 1)) * 1 + n / total * (m / (total - 1)) * (
            2 / 4) + n / total * ((n - 1) / (total - 1)) * 0
    prob = round(DD + Dd + dd, 5)

    return prob


if __name__ == '__main__':
    filename = "rosalind_iprb_2.txt"
    kmn = parse_iprb_data(filename)
    # print(kmn)
    prob = iprb(kmn[0], kmn[1], kmn[2])
    print(prob)
