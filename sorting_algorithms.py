"""
sorting_algorithms.py file containing the implementation of the different sorting algorithms used for assembly quality
scoring

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)
"""


def bubble_sort(data):
    """Sort using bubble sort

    TODO: update/re-write the code, code was taken directly from https://stackabuse.com/bubble-sort-in-python/

    :param data: set of string to sort from largest to smallest using bubble sort
    :return: sorted data
    """
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if len(data[j]) < len(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    data = [4,2,1]
