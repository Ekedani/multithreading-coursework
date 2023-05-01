
from src import Edge

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
