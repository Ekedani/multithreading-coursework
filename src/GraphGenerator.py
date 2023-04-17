import random

from src.Graph import Graph
from src.Edge import Edge


class GraphGenerator:
    @staticmethod
    def generate(verticesNum) -> Graph:
        matrix = [[0 for _ in range(verticesNum)] for _ in range(verticesNum)]
        for i in range(verticesNum):
            for j in range(i + 1, verticesNum):
                weight = random.randint(1, 10000)
                matrix[i][j] = weight
                matrix[j][i] = weight

        graph = Graph()
        for i in range(verticesNum):
            graph.addVertex(i)
        for i in range(verticesNum):
            for j in range(verticesNum):
                if matrix[i][j] > 0:
                    graph.addEdge(Edge(i, j, matrix[i][j]))

        return graph
