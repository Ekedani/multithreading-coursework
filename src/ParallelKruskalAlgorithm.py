from src.DisjointSetUnion import DisjointSetUnion
from src.Edge import isEdgeArraySorted
from src.Graph import Graph
from src.EdgeSorting import parallelMergesortEdges


class ParallelKruskalAlgorithm:
    def __init__(self, threads_num):
        self.threads_num = threads_num

    def findMST(self, graph: Graph) -> Graph:
        mst_graph = Graph()
        mst_components = DisjointSetUnion()
        for vertex in graph.vertices:
            mst_graph.addVertex(vertex)
            mst_components.makeSet(vertex)
        ordered_edges = self.__orderEdgesByWeight(edges=graph.edges)
        print(f'Sorted correctly: {isEdgeArraySorted(ordered_edges)}')
        for edge in ordered_edges:
            if mst_components.find(edge.start) != mst_components.find(edge.end):
                mst_graph.addEdge(edge)
                mst_components.union(edge.start, edge.end)
        return mst_graph

    def __orderEdgesByWeight(self, edges):
        return parallelMergesortEdges(edges, self.threads_num)

