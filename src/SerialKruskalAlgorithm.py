from src.Graph import Graph
from src.DisjointSetUnion import DisjointSetUnion
from src.EdgeSorting import mergesortEdges


class SerialKruskalAlgorithm:
    def __init__(self):
        pass

    def findMinimumSpanningTree(self, graph: Graph) -> Graph:
        mst_graph = Graph()
        # initialization_start = time.time()
        mst_components = DisjointSetUnion()
        for vertex in graph.vertices:
            mst_graph.addVertex(vertex)
            mst_components.makeSet(vertex)
        # initialization_end = time.time()
        # sorting_start = time.time()
        ordered_edges = self.__orderEdgesByWeight(edges=graph.edges)
        # sorting_end = time.time()
        # insert_start = time.time()
        for edge in ordered_edges:
            if mst_components.find(edge.start) != mst_components.find(edge.end):
                mst_graph.addEdge(edge)
                mst_components.union(edge.start, edge.end)
        # insert_end = time.time()
        # print(
        #     f'Time by stages:\n'
        #     f'Initialization: {initialization_end - initialization_start} s\n'
        #     f'Sorting: {sorting_end - sorting_start} s\n'
        #     f'Insert: {insert_end - insert_start} s\n'
        # )
        return mst_graph

    def __orderEdgesByWeight(self, edges: list) -> list:
        edges_copy = edges.copy()
        mergesortEdges(edges_copy, 0, len(edges_copy) - 1)
        return edges_copy
