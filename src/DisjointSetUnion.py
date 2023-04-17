class DisjointSetUnion:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, element):
        if element not in self.parent:
            self.parent[element] = element
            self.rank[element] = 0

    def find(self, element):
        if element not in self.parent:
            return None
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, subsetA, subsetB):
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
