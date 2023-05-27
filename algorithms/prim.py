import sys


class Prim():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def find_min_edge(self, key, mstSet):
        min_weight = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_weight and mstSet[v] is False:
                min_weight = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        result = {}  # Dictionary to store the result

        for _ in range(self.V):
            u = self.find_min_edge(key, mstSet)

            mstSet[u] = True
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] is False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        for i in range(1, self.V):
            result[(parent[i], i)] = self.graph[i][parent[i]]

        return result
