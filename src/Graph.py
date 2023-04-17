from src import Edge

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addEdge(self, edge: Edge):
        self.edges.append(edge)

    def printEdges(self):
        for edge in self.edges:
            print(f'{edge.start}-{edge.end} : {edge.weight}')