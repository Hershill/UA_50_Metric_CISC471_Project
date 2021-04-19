"""
random_contig_set_generator.py file containing the implementation of a generator for our sample data

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)
"""

import random

BASE_PAIRS = ["A", "G", "C", "T"]

# random.seed(version=2)


def generate_random_seq_set(min=5, max=150, num=250):
    random_contig_set = list()

    for i in range(num):
        random_len = random.randint(min, max)
        # print(random_len)
        random_contig = str()
        for i in range(random_len):
            random_contig += random.choice(BASE_PAIRS)
        random_contig_set.append(random_contig)

    return random_contig_set


def generate_random_contig(random_len):
    random_contig = str()
    for i in range(random_len):
        random_contig += random.choice(BASE_PAIRS)

    return random_contig


def generate_contigs_by_percentage(small=1/3, medium=1/3, large=1/3, num=250):
    # defaults to evenly weighted

    small_range = (5, 90)
    med_range = (90, 175)
    large_range = (175, 325)

    small_set = list()
    med_set = list()
    large_set = list()

    # threshold for small 5-90 (add citation in report)
    small_pct = small * num
    for i in range(int(round(small_pct))):
        rand_len = random.randrange(small_range[0], small_range[1])
        contig = generate_random_contig(rand_len)
        small_set.append(contig)

    # threshold for medium 90-175
    med_pct = medium * num
    for i in range(int(round(med_pct))):
        rand_len = random.randrange(med_range[0], med_range[1])
        contig = generate_random_contig(rand_len)
        med_set.append(contig)

    # threshold for large 175-325
    large_pct = large*num
    for i in range(int(round(large_pct))):
        rand_len = random.randrange(large_range[0], large_range[1])
        contig = generate_random_contig(rand_len)
        large_set.append(contig)

    total_set = small_set + med_set + large_set

    return total_set


if __name__ == '__main__':
    # generated_set = generate_random_seq_set()
    # print(generated_set)

    generated_set = generate_contigs_by_percentage(0.75, 0.125, 0.125, 250)
    print(generated_set)
    print(len(generated_set))

    generated_set = generate_contigs_by_percentage(num=250)
    print(generated_set)
    print(len(generated_set))
