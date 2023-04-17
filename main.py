import time

from src.GraphGenerator import GraphGenerator
from src.SerialKruskalAlgorithm import SerialKruskalAlgorithm
from src.ParallelKruskalAlgorithm import ParallelKruskalAlgorithm

if __name__ == '__main__':
    startGraph = GraphGenerator.generate(16)
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(1)

    start = time.time()
    mst = serialKruskalSolver.findMST(startGraph)
    end = time.time()
    print(f'Total serial time: {end - start}')

    print()

    start = time.time()
    mst_par = parallelKruskalSolver.findMST(startGraph)
    end = time.time()
    print(f'Total parallel time: {end - start}')
