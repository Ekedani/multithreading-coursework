import csv
import os

from src.Edge import Edge


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def addVertex(self, vertex) -> None:
        self.vertices.append(vertex)

    def addEdge(self, edge: Edge) -> None:
        self.edges.append(edge)

    def printEdges(self):
        for edge in self.edges:
            print(f'{edge.start}-{edge.end} : {edge.weight}')

    def getWeight(self) -> float:
        weight = 0
        for edge in self.edges:
            weight += edge.weight
        return weight

    def toMatrix(self) -> list[list[int]]:
        n = len(self.vertices)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for edge in self.edges:
            i = self.vertices.index(edge.start)
            j = self.vertices.index(edge.end)
            matrix[i][j] = edge.weight
            matrix[j][i] = edge.weight
        return matrix

    def saveToFile(self, filename) -> None:
        """
        Saves graph matrix to .csv file
        :param filename: name of resulting file
        """
        data_directory = 'data'
        matrix = self.toMatrix()
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
        filepath = os.path.join(data_directory, filename + ".csv")
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in matrix:
                writer.writerow(row)

    @staticmethod
    def fromMatrix(matrix):
        graph = Graph()
        vertices_num = len(matrix)
        for i in range(vertices_num):
            graph.addVertex(i)
        for i in range(vertices_num):
            for j in range(i + 1, vertices_num):
                if matrix[i][j] > 0:
                    graph.addEdge(Edge(i, j, matrix[i][j]))
        return graph

    @staticmethod
    def readFromFile(filename):
        """
        Reads matrix from .csv file and parses it into Graph
        :param filename: name of the .csv file with graph matrix
        """
        data_directory = 'data'
        filepath = os.path.join(data_directory, filename + ".csv")
        matrix = []
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row = [int(x) for x in row]
                matrix.append(row)
        return matrix
