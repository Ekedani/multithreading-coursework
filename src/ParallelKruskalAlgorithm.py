from src.DisjointSetUnion import DisjointSetUnion
from src.Graph import Graph
from src.EdgeSorting import parallelMergesortEdges


class ParallelKruskalAlgorithm:
    def __init__(self, parallelism):
        self.parallelism = parallelism

    def findMinimumSpanningTree(self, graph: Graph) -> Graph:
        mst_graph = Graph()
        mst_components = DisjointSetUnion()
        for vertex in graph.vertices:
            mst_graph.addVertex(vertex)
            mst_components.makeSet(vertex)
        ordered_edges = self.__orderEdgesByWeight(edges=graph.edges)
        for edge in ordered_edges:
            if mst_components.find(edge.start) != mst_components.find(edge.end):
                mst_graph.addEdge(edge)
                mst_components.union(edge.start, edge.end)
        return mst_graph

    def __orderEdgesByWeight(self, edges: list) -> list:
        return parallelMergesortEdges(edges, self.parallelism)

