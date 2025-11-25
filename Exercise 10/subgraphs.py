class Graph:
    def __init__(self, n: int):
        self.n = n
        self.graph_list = [[] for i in range(self.n)] #use adjacency list cuz undirected graph w/ no weights

    def add(self, u: int, v: int): #js use the same functions from last week lol
        if v not in self.graph_list[u]:
            self.graph_list[u].append(v)
        
        if u not in self.graph_list[v]:
            self.graph_list[v].append(u)

    def remove(self, u: int, v: int):
        if v in self.graph_list[u]:
            self.graph_list[u].remove(v)

        if u in self.graph_list[v]:
            self.graph_list[v].remove(u)
        

    def subgraphs(self):
        visited = set()  
        count = 0  

        for vertex in range(self.n):
            if vertex not in visited:
                count += 1
                self.dfs(vertex, visited)
        
        return count
    
    def dfs(self, vertex: int, visited: set):
        visited.add(vertex)
        
        for neighbor in self.graph_list[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        

if __name__ == "__main__":
    graph = Graph(6)

    edges = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())
    
    more_edges = ((0, 2), (2, 3), (3, 5), (4, 5))
    for u, v in more_edges:
        graph.add(u, v)

    print(graph.subgraphs())