"""
set0.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Introduction to Set Operations

Problem

If A and B are sets, then their union A∪B is the set comprising any elements
in either A or B; their intersection A∩B is the set of elements in both A and
B; and their set difference A−B is the set of elements in A but not in B.

Furthermore, if A is a subset of another set U, then the set complement of A
with respect to U is defined as the set Ac=U−A. See the Sample sections below
for examples.

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are
taken with respect to {1,2,…,n}).
"""


from parsers import parse_seto_data


def seto(num, set_a, set_b):
    """Return 6 sets of A∪B, A∩B, A−B, B−A, Ac, and Bc

    :param num: maximum size of a set
    :param set_a: first set as a list of ints
    :param set_b: second set as a list of ints
    :return: the set operations performed between set_a and set_b
    """

    # base case
    if set_a == [''] or set_b == ['']:
        return []

    set_a = [int(i) for i in set_a]
    set_b = [int(i) for i in set_b]

    all_sets = list()


    # set 1 - union
    set_1 = get_set_union(set_a, set_b)

    # set 2 - intersect
    set_2 = get_set_intersect(set_a, set_b)

    # set 3 and 4 - difference
    set_3 = get_set_diff(set_a, set_b)

    set_4 = get_set_diff(set_b, set_a)

    # set 5 and 6 - complement
    set_5 = get_set_complement(set_a, num)

    set_6 = get_set_complement(set_b, num)

    all_sets = [set_1, set_2, set_3, set_4, set_5, set_6]

    return all_sets


def get_set_union(a, b):
    """Return the set union of a and b

    :param a: set a
    :param b: set b
    :return: union of set a and b
    """

    union = list()

    for i in a:
        if i not in union:
            union.append(i)

    for i in b:
        if i not in union:
            union.append(i)

    union = sorted(union)

    return union


def get_set_intersect(a, b):
    """Return the set intersect of a and b

    :param a: set a
    :param b: set b
    :return: intersect of set a and b
    """

    intersect = list()

    for i in a:
        for k in b:
            if i == k:
                intersect.append(i)

    intersect = sorted(intersect)

    return intersect


def get_set_diff(a, b):
    """Return the set difference of a and b

    :param a: set a
    :param b: set b
    :return: difference of set a and b
    """

    difference = list()

    for i in a:
        if i not in b:
            difference.append(i)

    difference = sorted(difference)

    return difference


def get_set_complement(a, num):
    """Return the set complement of a

    :param a: set a
    :param num: maximum size of set
    :return: complement of set a
    """

    total_set = list(range(1, num + 1))

    complement = list()

    for i in total_set:
        if i not in a:
            complement.append(i)

    complement = sorted(complement)

    return complement


def format_output(sets):
    """Format output according to problem requirement

    :param sets: list of sets
    :return: formatted string output of results
    """

    formatted_str = ""

    for i in sets:
        formatted_str += "{"
        for k in range(len(i) - 1):
            formatted_str += f"{i[k]}, "
        formatted_str += f"{i[-1]}}}\n"

    return formatted_str


if __name__ == '__main__':
    filename = "rosalind_seto_2.txt"
    seto_data = parse_seto_data(filename)
    # print(seto_data)
    set_one = seto_data[1]
    set_two = seto_data[2]
    output_sets = seto(int(seto_data[0]), set_one, set_two)
    print(output_sets)
    print(format_output(output_sets))
