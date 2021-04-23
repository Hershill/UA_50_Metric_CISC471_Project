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

# SMALL_RANGE = (5, 90)
# MEDIUM_RANGE = (90, 175)
# LARGE_RANGE = (175, 215)

SMALL_RANGE = (36, 150)
MEDIUM_RANGE = (150, 250)
LARGE_RANGE = (250, 500)


def generate_random_seq_set(min=5, max=150, num=12500):
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


def generate_contigs_by_percentage_from_genome(ref_genome, small=1/3, medium=1/3, large=1/3, num=12500):

    if small + medium + large > 1:
        return []

    # defaults to evenly weighted

    small_set = list()
    med_set = list()
    large_set = list()

    genome_len = len(ref_genome)

    index_set = list()

    # threshold for small 5-90 (add citation in report)
    small_pct = small * num
    for i in range(int(round(small_pct))):
        rand_len = random.randrange(SMALL_RANGE[0], SMALL_RANGE[1])
        rand_index = random.randrange(0, genome_len - rand_len)
        contig = ref_genome[rand_index:rand_index + rand_len]
        # index_set.append((rand_index, rand_index + rand_len))
        index_set.append([contig, (rand_index, rand_index + rand_len)])
        small_set.append(contig)

    # threshold for medium 90-175
    med_pct = medium * num
    for i in range(int(round(med_pct))):
        rand_len = random.randrange(MEDIUM_RANGE[0], MEDIUM_RANGE[1])
        rand_index = random.randrange(0, genome_len - rand_len)
        contig = ref_genome[rand_index:rand_index + rand_len]
        # index_set.append((rand_index, rand_index + rand_len))
        index_set.append([contig, (rand_index, rand_index + rand_len)])
        med_set.append(contig)

    # threshold for large 175-325
    large_pct = large * num
    for i in range(int(round(large_pct))):
        rand_len = random.randrange(LARGE_RANGE[0], LARGE_RANGE[1])
        rand_index = random.randrange(0, genome_len - rand_len)
        contig = ref_genome[rand_index:rand_index + rand_len]
        # index_set.append((rand_index, rand_index + rand_len))
        index_set.append([contig, (rand_index, rand_index + rand_len)])
        large_set.append(contig)

    total_set = small_set + med_set + large_set

    return total_set, index_set


def generate_error_sample(contig_sample, ref_genome, pct_error=.05):
    num_error = len(contig_sample) * pct_error
    contig_errs = list()
    indices_to_remove = list()
    index_set = list()

    for i in range(int(round(num_error))):
        rand_index_1 = random.randrange(0, len(contig_sample))
        rand_index_2 = random.randrange(0, len(contig_sample))

        while rand_index_1 in indices_to_remove:
            rand_index_1 = random.randrange(0, len(contig_sample))

        while rand_index_2 in indices_to_remove:
            rand_index_2 = random.randrange(0, len(contig_sample))

        temp_contig = contig_sample[rand_index_1] + contig_sample[rand_index_2]
        if temp_contig in ref_genome:
            temp_contig = contig_sample[rand_index_2] + contig_sample[rand_index_1]

        contig_errs.append(temp_contig)
        indices_to_remove.extend([rand_index_1, rand_index_2])

    return contig_sample + contig_errs


def generate_contigs_by_percentage(small=1/3, medium=1/3, large=1/3, num=12500):
    # defaults to evenly weighted

    small_set = list()
    med_set = list()
    large_set = list()

    # threshold for small 5-90 (add citation in report)
    small_pct = small * num
    for i in range(int(round(small_pct))):
        rand_len = random.randrange(SMALL_RANGE[0], SMALL_RANGE[1])
        contig = generate_random_contig(rand_len)
        small_set.append(contig)

    # threshold for medium 90-175
    med_pct = medium * num
    for i in range(int(round(med_pct))):
        rand_len = random.randrange(MEDIUM_RANGE[0], MEDIUM_RANGE[1])
        contig = generate_random_contig(rand_len)
        med_set.append(contig)

    # threshold for large 175-325
    large_pct = large*num
    for i in range(int(round(large_pct))):
        rand_len = random.randrange(LARGE_RANGE[0], LARGE_RANGE[1])
        contig = generate_random_contig(rand_len)
        large_set.append(contig)

    total_set = small_set + med_set + large_set

    return total_set


def count_contig_pct(contig_set):
    small_count = 0
    med_count = 0
    large_count = 0

    num = len(contig_set)

    for i in contig_set:
        if SMALL_RANGE[0] <= len(i) <= SMALL_RANGE[1]:
            small_count += 1
        elif MEDIUM_RANGE[0] <= len(i) <= MEDIUM_RANGE[1]:
            med_count += 1
        elif LARGE_RANGE[0] <= len(i) <= LARGE_RANGE[1]:
            large_count += 1

    small_pct = small_count/num
    med_pct = med_count/num
    large_pct = large_count/num

    return [small_pct, med_pct, large_pct, num]


if __name__ == '__main__':
    # generated_set = generate_random_seq_set()
    # print(generated_set)

    generated_set = generate_contigs_by_percentage(0.75, 0.125, 0.125, 250)
    print(generated_set)
    print(len(generated_set))

    print(count_contig_pct(generated_set))

    generated_set = generate_contigs_by_percentage(num=250)
    print(generated_set)
    print(len(generated_set))
