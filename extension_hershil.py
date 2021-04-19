
from algorithms import *


def extension_metric(data_set, pct=50):
    """Generate new metric based on nxx and lxx score

    :param data_set: set of contigs
    :param pct: percentage threshold for N and L scoring
    :return: new blended metric
    """
    nxx_score = nxx(data_set, pct)
    lxx_score = lxx(data_set, pct)

    max_contig_len = len(max(data_set, key=len))

    blended_metric = (max_contig_len + nxx_score) / lxx_score

    return blended_metric


if __name__ == '__main__':
    filename = "asmq_sample_data.txt"
    # filename = "asqm_datasets/rosalind_asmq_1.txt"
    dna_set = parse_assembly_data(filename)
    # print(dna_set)
    score = extension_metric(dna_set, 50)
    print(score)
