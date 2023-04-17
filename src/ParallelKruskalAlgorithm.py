import time

from src.DisjointSetUnion import DisjointSetUnion
from src.Graph import Graph
from src.edge_sorting import parallelMergesortEdges


class ParallelKruskalAlgorithm:
    def __init__(self, threadsNum):
        self.threadsNum = threadsNum

    def findMST(self, graph: Graph) -> Graph:
        start = time.time()
        mstGraph = Graph()
        mstComponents = DisjointSetUnion()
        for vertex in graph.vertices:
            mstGraph.addVertex(vertex)
            mstComponents.makeSet(vertex)
        end = time.time()
        print(f'Initializing MST and Components: {end - start} s')

        start = time.time()
        orderedEdges = self.__orderEdgesByWeight(edges=graph.edges)
        end = time.time()
        print(f'Sorting Edges: {end - start} s')

        start = time.time()
        for edge in orderedEdges:
            if mstComponents.find(edge.start) != mstComponents.find(edge.end):
                mstGraph.addEdge(edge)
                mstComponents.union(edge.start, edge.end)
        end = time.time()
        print(f'Adding edges to the MST: {end - start} s')
        return mstGraph

    def __orderEdgesByWeight(self, edges):
        return parallelMergesortEdges(edges, self.threadsNum)
