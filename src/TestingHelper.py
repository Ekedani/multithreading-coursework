import os
import time

import networkx as nx
import matplotlib.pyplot as plt
import csv

from src.Graph import Graph
from src.GraphGenerator import GraphGenerator
from src.ParallelKruskalAlgorithm import ParallelKruskalAlgorithm
from src.SerialKruskalAlgorithm import SerialKruskalAlgorithm


def renderGraph(graph: Graph, filename: str, node_color: str = 'blue') -> None:
    """
    Renders graph to file with given filename
    :param graph: graph to be rendered
    :param filename: destination file name
    :param node_color:
    """
    nx_graph = convertGraphToNX(graph)
    pos = nx.circular_layout(nx_graph)
    nx.draw(nx_graph, pos=pos, edgecolors='k', with_labels=False, node_color=f'tab:{node_color}')
    edges = len(nx_graph.edges())
    vertices = len(nx_graph.nodes())
    graph_weight = sum(nx.get_edge_attributes(nx_graph, 'weight').values())
    plt.text(0.95, 0.05, f"Edges: {edges}\nVertices: {vertices}\nGraph weight: {graph_weight}",
             transform=plt.gcf().transFigure, fontsize=10, ha='right', va='bottom')
    plt.savefig(f'{filename}.png')
    plt.close()


def generatePredefinedTests(test_sizes: list, high: int = 100_000):
    data_directory = 'data'
    for size in test_sizes:
        test_graph = GraphGenerator.generateComplete(size, high)
        test_graph.saveToFile(str(size))
        nx_mst = findMinimumSpanningTreeWithNX(test_graph)
        mst_weight = sum(nx.get_edge_attributes(nx_mst, 'weight').values())
        filepath = os.path.join(data_directory, str(size) + "_solution.csv")
        with open(filepath, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([mst_weight])


def runPredefinedTests(test_sizes: list, parallelism: int = 8, show_time: bool = True):
    data_directory = 'data'
    failed_tests = []
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(parallelism)
    for size in test_sizes:
        print(f'===== PREDEFINED TEST FOR SIZE {size} =====')
        test_graph = Graph.readFromFile(str(size))
        serial_start = time.time()
        serial_mst = serialKruskalSolver.findMinimumSpanningTree(graph=test_graph)
        serial_end = time.time()
        parallel_start = time.time()
        parallel_mst = parallelKruskalSolver.findMinimumSpanningTree(graph=test_graph)
        parallel_end = time.time()
        if show_time:
            print(f'Total serial time: {serial_end - serial_start}')
            print(f'Total parallel time: {parallel_end - parallel_start}')
        filepath = os.path.join(data_directory, str(size) + "_solution.csv")
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            nx_weight = float(rows[0][0])
        serial_is_correct = nx_weight == serial_mst.getWeight()
        parallel_is_correct = nx_weight == parallel_mst.getWeight()
        print(f'Serial is correct: {serial_is_correct}')
        print(f'Parallel is correct: {parallel_is_correct}')
        if not (serial_is_correct and parallel_is_correct):
            failed_tests.append(size)
    if len(failed_tests) == 0:
        print('None of tests failed.')


def runRandomTests(test_sizes: list, parallelism: int = 8, show_time: bool = True, high: int = 100_000):
    failed_tests = []
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(parallelism)
    for size in test_sizes:
        print(f'===== RANDOM TEST FOR SIZE {size} =====')
        test_graph = GraphGenerator.generateComplete(size, high)
        serial_start = time.time()
        serial_mst = serialKruskalSolver.findMinimumSpanningTree(graph=test_graph)
        serial_end = time.time()
        parallel_start = time.time()
        parallel_mst = parallelKruskalSolver.findMinimumSpanningTree(graph=test_graph)
        parallel_end = time.time()
        if show_time:
            print(f'Total serial time: {serial_end - serial_start}')
            print(f'Total parallel time: {parallel_end - parallel_start}')
        nx_mst = findMinimumSpanningTreeWithNX(graph=test_graph)
        nx_weight = sum(nx.get_edge_attributes(nx_mst, 'weight').values())
        serial_is_correct = nx_weight == serial_mst.getWeight()
        parallel_is_correct = nx_weight == parallel_mst.getWeight()
        print(f'Serial is correct: {serial_is_correct}')
        print(f'Parallel is correct: {parallel_is_correct}')
        if not (serial_is_correct and parallel_is_correct):
            failed_tests.append(size)
    if len(failed_tests) == 0:
        print('None of tests failed.')


def hasMinimumSpanningTreeWeight(graph: Graph, mst: Graph) -> bool:
    """
    Checks if given MST of the graph is correct using networkx library
    :param graph: graph to be checked
    :param mst: MST to be checked
    :return: True if MST is correct, False if MST is incorrect
    """
    nx_mst = findMinimumSpanningTreeWithNX(graph)
    nx_mst_weight = sum(nx.get_edge_attributes(nx_mst, 'weight').values())
    return nx_mst_weight == mst.getWeight()


def findMinimumSpanningTreeWithNX(graph: Graph):
    nx_graph = convertGraphToNX(graph)
    nx_mst = nx.minimum_spanning_tree(nx_graph, weight='weight', ignore_nan=False)
    return nx_mst


def convertGraphToNX(graph: Graph):
    nx_graph = nx.Graph()
    weight_matrix = graph.toMatrix()
    vertices = len(weight_matrix)
    nx_graph.add_nodes_from(range(vertices))
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if weight_matrix[i][j] != 0:
                nx_graph.add_edge(i, j, weight=weight_matrix[i][j])
    return nx_graph
