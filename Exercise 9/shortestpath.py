import math

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.graph_matrix = [[0] * n for i in range(n)]
    
    def add(self, u: int, v: int, w: int):
        self.graph_matrix[u][v] = w
    
    def shortest_path(self, start: int, end: int):
        distances = [math.inf] * self.n
        distances[start] = 0
        
        prev = [None] * self.n
        seen = set() 
        
        for i in range(self.n):
            curr = self.minVertex(distances, seen)
            
            if curr == -1 or distances[curr] == math.inf:
                break
            
            seen.add(curr)
            
            if curr == end:
                self.print_path(prev, end)
                return
            
            for neighbor in range(self.n):
                weight = self.graph_matrix[curr][neighbor]
                
                if weight > 0 and neighbor not in seen:
                    new_dist = distances[curr] + weight
                    
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        prev[neighbor] = curr
        
        print(-1)
    
    def minVertex(self, distances: list[float], seen: set):
        shortest_dist = math.inf
        min_vertex = -1
        
        for v in range(self.n):
            if v not in seen and distances[v] < shortest_dist:
                shortest_dist = distances[v]
                min_vertex = v
        
        return min_vertex
    
    def print_path(self, prev, end):
        path = []
        curr = end
        
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        
        path.reverse()
        
        print(" ".join(map(str, path)))


if __name__ == "__main__":
    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
                   (1, 4,  3), (2, 3,  7), (2, 5, 25),
                   (3, 4, 12), (3, 5, 15), (3, 6,  4),
                   (3, 7, 15), (3, 8, 20), (4, 7,  2),
                   (5, 8,  2), (6, 7,  8), (6, 8, 13),
                   (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)