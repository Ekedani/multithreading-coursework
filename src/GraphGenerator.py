import random

from src.Graph import Graph
from src.Edge import Edge


class GraphGenerator:
    @staticmethod
    def generate(verticesNum) -> Graph:
        graphMatrix = [[0 for _ in range(verticesNum)] for _ in range(verticesNum)]
        for i in range(verticesNum):
            for j in range(i + 1, verticesNum):
                weight = random.randint(1, 10000)
                graphMatrix[i][j] = weight
                graphMatrix[j][i] = weight

        graph = Graph()
        for i in range(verticesNum):
            graph.addVertex(i)
        for i in range(verticesNum):
            for j in range(i + 1, verticesNum):
                if graphMatrix[i][j] > 0:
                    graph.addEdge(Edge(i, j, graphMatrix[i][j]))

        return graph
