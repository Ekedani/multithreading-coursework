import time

from src.GraphGenerator import GraphGenerator
from src.SerialKruskalAlgorithm import SerialKruskalAlgorithm
from src.ParallelKruskalAlgorithm import ParallelKruskalAlgorithm

if __name__ == '__main__':
    startGraph = GraphGenerator.generateComplete(1000, 20000)
    serialKruskalSolver = SerialKruskalAlgorithm()
    parallelKruskalSolver = ParallelKruskalAlgorithm(12)
    print(startGraph.getWeight())
    start = time.time()
    mst = serialKruskalSolver.findMST(startGraph)
    end = time.time()
    print(f'Total serial time: {end - start}')
    print(mst.getWeight())
    print("Parallel start")
    start = time.time()
    mst_par = parallelKruskalSolver.findMST(startGraph)
    end = time.time()
    print(f'Total parallel time: {end - start}')
    print(mst_par.getWeight())


