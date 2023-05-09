class DisjointSetUnion:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, element):
        """
        Creates a new subset
        :param element: parent of the new subset
        """
        if element not in self.parent:
            self.parent[element] = element
            self.rank[element] = 0

    def find(self, element):
        """
        Searches for the subset, which contains an element
        :param element: the element to be searched
        :return: parent of the subset
        """
        if element not in self.parent:
            return None
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, subsetA, subsetB):
        """
        Joins two subsets into one with the highest rank
        :param subsetA: first subset to be joined
        :param subsetB: second subset to be joined
        """
        rootA = self.find(subsetA)
        rootB = self.find(subsetB)
        if rootA is None or rootB is None or rootA == rootB:
            return
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
