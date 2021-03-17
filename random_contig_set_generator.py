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
        print(random_len)
        random_contig = str()
        for i in range(random_len):
            random_contig += random.choice(BASE_PAIRS)
        random_contig_set.append(random_contig)

    return random_contig_set


if __name__ == '__main__':
    generated_set = generate_random_seq_set()
    print(generated_set)
