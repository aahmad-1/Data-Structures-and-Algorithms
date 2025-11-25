import math

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.graph_list = [[] for i in range(self.n)] 

    def add(self, u: int, v: int, w: int):
        self.graph_list[u].append((v, w))
        self.graph_list[v].append((u, w))

    def remove(self, u: int, v: int):
        self.graph_list[u] = [(neighbor, weight) for neighbor, weight in self.graph_list[u] if neighbor != v]
        self.graph_list[v] = [(neighbor, weight) for neighbor, weight in self.graph_list[v] if neighbor != u]

    def min_cost(self):
        if self.n == 0:
            return 0
        
        D = [math.inf] * self.n
        visited = [False] * self.n
        
        D[0] = 0
        total_cost = 0
        
        for _ in range(self.n):
            min_dist = math.inf
            v = -1
            for j in range(self.n):
                if not visited[j] and D[j] < min_dist:
                    min_dist = D[j]
                    v = j
            
            if v == -1 or D[v] == math.inf:
                break 
            
            visited[v] = True
            total_cost += D[v]
            
            for neighbor, edge_weight in self.graph_list[v]:
                if not visited[neighbor] and edge_weight < D[neighbor]:
                    D[neighbor] = edge_weight
        
        return total_cost

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    print(graph.min_cost())

    graph.remove(2, 3)

    print(graph.min_cost())