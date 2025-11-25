import math

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.graph_matrix = [[0] * n for i in range(n)] #use adjacency matrix cuz directed graph w/ graphs
    
    def add(self, u: int, v: int, w: int):
        self.graph_matrix[u][v] = w

    def remove(self, u: int, v: int):
        self.graph_matrix[u][v] = 0

    def all_paths(self): #basically just Floyd’s algorithm with extra steps. code inspired from https://lut-dsa.cc.lut.fi/Books/LUTDSA/html/Floyd.html
        distances = [[math.inf] * self.n for i in range(self.n) ]

        for i in range(self.n): #diagonals = 0 (distance from vertex to itself)
            distances[i][i] = 0

        for i in range(self.n):
            for j in range(self.n):
                if self.graph_matrix[i][j] != 0:
                    distances[i][j] = self.graph_matrix[i][j]

        for k in range (self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (distances[i][k] != math.inf and
                        distances[k][j] != math.inf and
                        distances[i][j] > distances[i][k] + distances[k][j]):

                        distances[i][j] = distances[i][k] + distances[k][j]

        for i in range(self.n): #for the nonexistent paths
            for j in range(self.n):
                if distances[i][j] == math.inf:
                    distances[i][j] = -1

        return distances

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()