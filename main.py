import time

from src.Graph import Graph
from src.GraphGenerator import GraphGenerator
from src.SerialKruskalAlgorithm import SerialKruskalAlgorithm
from src.ParallelKruskalAlgorithm import ParallelKruskalAlgorithm
from src.TestingHelper import TestingHelper

if __name__ == '__main__':
    # graph = Graph.readFromFile('750')
    graph = GraphGenerator.generateComplete(40, 100000)
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(12)
    print(graph.getWeight())
    serial_start = time.time()
    mst_ser = serialKruskalSolver.findMinimumSpanningTree(graph)
    serial_end = time.time()
    print(f'Total serial time: {serial_end - serial_start}')
    print(mst_ser.getWeight())
    print("Parallel start")
    parallel_start = time.time()
    mst_par = parallelKruskalSolver.findMinimumSpanningTree(graph)
    parallel_end = time.time()
    print(f'Total parallel time: {parallel_end - parallel_start}')
    print(mst_par.getWeight())
    TestingHelper.renderGraph(graph, 'original')
    TestingHelper.renderGraph(mst_par, 'mst')
