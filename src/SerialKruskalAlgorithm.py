import time

from src.Edge import is_edge_array_sorted
from src.Graph import Graph
from src.DisjointSetUnion import DisjointSetUnion
from src.edge_sorting import mergesortEdges


class SerialKruskalAlgorithm:
    def __init__(self):
        pass

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
        print(f'Sorted correctly: {is_edge_array_sorted(orderedEdges)}')
        start = time.time()
        for edge in orderedEdges:
            if mstComponents.find(edge.start) != mstComponents.find(edge.end):
                mstGraph.addEdge(edge)
                mstComponents.union(edge.start, edge.end)
        end = time.time()
        print(f'Adding edges to the MST: {end - start} s')
        return mstGraph

    def __orderEdgesByWeight(self, edges):
        mergesortEdges(edges, 0, len(edges) - 1)
        return edges
