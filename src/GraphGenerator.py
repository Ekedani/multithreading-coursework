import random

from src.Graph import Graph


class GraphGenerator:
    @staticmethod
    def generateComplete(vertices_num, high) -> Graph:
        graph_matrix = [[0 for _ in range(vertices_num)] for _ in range(vertices_num)]
        for i in range(vertices_num):
            for j in range(i + 1, vertices_num):
                weight = random.randint(1, high)
                graph_matrix[i][j] = weight
                graph_matrix[j][i] = weight
        return Graph.fromMatrix(graph_matrix)
