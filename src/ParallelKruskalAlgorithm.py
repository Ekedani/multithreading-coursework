import time

from src.DisjointSetUnion import DisjointSetUnion
from src.Edge import is_edge_array_sorted
from src.Graph import Graph
from src.edge_sorting import parallelMergesortEdges


class ParallelKruskalAlgorithm:
    def __init__(self, threadsNum):
        self.threadsNum = threadsNum

    def findMST(self, graph: Graph) -> Graph:
        mstGraph = Graph()
        mstComponents = DisjointSetUnion()
        for vertex in graph.vertices:
            mstGraph.addVertex(vertex)
            mstComponents.makeSet(vertex)
        orderedEdges = self.__orderEdgesByWeight(edges=graph.edges)
        print(f'Sorted correctly: {is_edge_array_sorted(orderedEdges)}')
        for edge in orderedEdges:
            if mstComponents.find(edge.start) != mstComponents.find(edge.end):
                mstGraph.addEdge(edge)
                mstComponents.union(edge.start, edge.end)
        return mstGraph

    def __orderEdgesByWeight(self, edges):
        return parallelMergesortEdges(edges, self.threadsNum)

