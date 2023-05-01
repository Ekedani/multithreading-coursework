from src.Edge import is_edge_array_sorted
from src.Graph import Graph
from src.DisjointSetUnion import DisjointSetUnion
from src.edge_sorting import mergesortEdges


class SerialKruskalAlgorithm:
    def __init__(self):
        pass

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
        edgesCopy = edges.copy()
        mergesortEdges(edgesCopy, 0, len(edgesCopy) - 1)
        return edgesCopy
