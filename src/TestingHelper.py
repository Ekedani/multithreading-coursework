import networkx as nx
import matplotlib.pyplot as plt

from src.Graph import Graph


class TestingHelper:
    @staticmethod
    def hasMinimumSpanningTreeWeight(graph: Graph, mst: Graph) -> bool:
        """
        Checks if given MST of the graph is correct using networkx library
        :param graph: graph to be checked
        :param mst: MST to be checked
        :return: True if MST is correct, False if MST is incorrect
        """
        nx_graph = nx.Graph()
        weight_matrix = graph.toMatrix()
        vertices = len(weight_matrix)
        nx_graph.add_nodes_from(range(vertices))
        for i in range(vertices):
            for j in range(i + 1, vertices):
                if weight_matrix[i][j] != 0:
                    nx_graph.add_edge(i, j, weight=weight_matrix[i][j])
        nx_mst = nx.minimum_spanning_tree(nx_graph, weight='weight', ignore_nan=False)
        nx_mst_weight = sum(nx.get_edge_attributes(nx_mst, 'weight').values())
        # Graph does not necessarily have one MST, but their weight is always the same
        return nx_mst_weight == mst.getWeight()

    @staticmethod
    def renderGraph(graph: Graph, filename: str) -> None:
        """
        Renders graph to file with given filename
        :param graph: graph to be rendered
        :param filename: destination file name
        """
        nx_graph = nx.Graph()
        weight_matrix = graph.toMatrix()
        vertices = len(weight_matrix)
        nx_graph.add_nodes_from(range(vertices))
        for i in range(vertices):
            for j in range(i + 1, vertices):
                if weight_matrix[i][j] != 0:
                    nx_graph.add_edge(i, j, weight=weight_matrix[i][j])

        pos = nx.circular_layout(nx_graph)
        nx.draw(nx_graph, pos=pos, edgecolors='k', with_labels=False)
        edges = len(nx_graph.edges())
        vertices = len(nx_graph.nodes())
        graph_weight = sum(nx.get_edge_attributes(nx_graph, 'weight').values())
        plt.text(0.95, 0.05, f"Edges: {edges}\nVertices: {vertices}\nGraph weight: {graph_weight}",
                 transform=plt.gcf().transFigure, fontsize=10, ha='right', va='bottom')
        plt.savefig(f'{filename}.png')
        plt.close()
