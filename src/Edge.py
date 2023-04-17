def is_edge_array_sorted(edges):
    for i in range(1, len(edges)):
        if edges[i].weight < edges[i - 1].weight:
            return False
    return True


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
