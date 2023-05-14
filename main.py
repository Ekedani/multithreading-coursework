import time

from src.Graph import Graph
from src.GraphGenerator import GraphGenerator
from src.SerialKruskalAlgorithm import SerialKruskalAlgorithm
from src.ParallelKruskalAlgorithm import ParallelKruskalAlgorithm
from src.TestingHelper import TestingHelper

VISUALIZE_RESULTS = False

if __name__ == '__main__':
    # graph = Graph.readFromFile('2000')
    graph = GraphGenerator.generateComplete(2000, 100000)
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(12)

    serial_start = time.time()
    mst_ser = serialKruskalSolver.findMinimumSpanningTree(graph)
    serial_end = time.time()
    print(f'Total serial time: {serial_end - serial_start}')
    print(mst_ser.getWeight())

    # parallel_start = time.time()
    # mst_par = parallelKruskalSolver.findMinimumSpanningTree(graph)
    # parallel_end = time.time()
    # print(f'Total parallel time: {parallel_end - parallel_start}')
    # print(mst_par.getWeight())

    if VISUALIZE_RESULTS:
        TestingHelper.renderGraph(graph, 'original', node_color='green')
        TestingHelper.renderGraph(mst_ser, 'mst_ser', node_color='red')
        # TestingHelper.renderGraph(mst_par, 'mst_par', node_color='blue')
