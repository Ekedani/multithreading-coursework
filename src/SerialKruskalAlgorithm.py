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
        # print(f'Initializing MST and Components: {end - start} s')

        orderedEdges = self.__orderEdgesByWeight(edges=graph.edges)
        for element in orderedEdges:
            print(element.weight, end=' ')
        print()

        # end = time.time()
        # print(f'Sorting Edges: {end - start} s')
        print(f'Sorted correctly: {is_edge_array_sorted(orderedEdges)}')
        # start = time.time()

        for edge in orderedEdges:
            if mstComponents.find(edge.start) != mstComponents.find(edge.end):
                mstGraph.addEdge(edge)
                mstComponents.union(edge.start, edge.end)
        end = time.time()
        # print(f'Adding edges to the MST: {end - start} s')
        return mstGraph

    def __orderEdgesByWeight(self, edges):
        edgesCopy = edges.copy()
        mergesortEdges(edgesCopy, 0, len(edgesCopy) - 1)
        return edgesCopy
