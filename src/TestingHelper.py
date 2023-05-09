import networkx as nx

from src.Graph import Graph


class TestingHelper:
    @staticmethod
    def isMinimumSpanningTree(graph: Graph, mst: Graph) -> bool:
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
        # Graph does not necessarily have the same MST, but their weight is always the same
        return nx_mst_weight == mst.getWeight()

    @staticmethod
    def findMinimumSpanningTreeUsingNX():
        pass
