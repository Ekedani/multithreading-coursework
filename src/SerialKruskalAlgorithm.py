import time

from src.Graph import Graph
from src.DisjointSetUnion import DisjointSetUnion


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

        start = time.time()
        for edge in orderedEdges:
            if mstComponents.find(edge.start) != mstComponents.find(edge.end):
                mstGraph.addEdge(edge)
                mstComponents.union(edge.start, edge.end)
        end = time.time()
        print(f'Adding edges to the MST: {end - start} s')
        return mstGraph

    def __orderEdgesByWeight(self, edges):
        def mergesort(edges):
            if len(edges) > 1:
                mid = len(edges) // 2
                left = edges[:mid]
                right = edges[mid:]

                mergesort(left)
                mergesort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i].weight < right[j].weight:
                        edges[k] = left[i]
                        i += 1
                    else:
                        edges[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    edges[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    edges[k] = right[j]
                    j += 1
                    k += 1

        #return sorted(edges, key=lambda edge: edge.weight)
        mergesort(edges)
        return edges

    