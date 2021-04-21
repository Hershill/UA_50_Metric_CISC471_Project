"""
tree.py file containing the implementation of the algorithms

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

Completing a Tree

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a
graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce
a tree.
"""

from parsers import parse_tree_data


def tree(num_nodes, graph_data):
    """Return number of nodes needed to be added to generate a tree

    :param graph_data: data of the adjacency list of the graph
    :param num_nodes: number of nodes in the graph
    :return: number of nodes needed to be added to turn graph into a tree
    """

    # base case
    if num_nodes == 0:
        return 0

    graph_data_ints = list()
    set_range = list(range(1, num_nodes + 1))
    node_set = list()

    node_count = 0
    num_edges = 0

    for i in graph_data:
        graph_data_ints.append([int(k) for k in i])

    for i in graph_data_ints:
        num_edges += 1
        if i[0] not in node_set:
            node_set.append(i[0])
        if i[1] not in node_set:
            node_set.append(i[1])

    node_set = sorted(node_set)

    for i in set_range:
        if i not in node_set:
            node_count += 1

    missing_nodes = num_nodes - num_edges - 1

    return missing_nodes


if __name__ == '__main__':
    filename = "rosalind_tree_4.txt"
    tree_data = parse_tree_data(filename)
    # print(tree_data)
    num_missing_nodes = tree(int(tree_data[0]), tree_data[1:])
    print(num_missing_nodes)
