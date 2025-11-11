class Graph:
    def __init__(self, n: int):
        self.n = n
        self.graph_list = [[] for i in range(self.n)]

    def dft(self, start: int):
        seen = set()
        stack = [start]
        result = []
        
        while stack != []:
            vertex = stack.pop()
            if vertex not in seen:
                seen.add(vertex)
                result.append(str(vertex))
                neighbors = sorted(self.graph_list[vertex], reverse=True)
                for neighbor in neighbors:
                    if neighbor not in seen:
                        stack.append(neighbor)
        
        print(" ".join(result))

    def add(self, u: int, v: int):
        if v not in self.graph_list[u]:
            self.graph_list[u].append(v)
        
        if u not in self.graph_list[v]: #append the other way too cuz its undirected
            self.graph_list[v].append(u)

    def remove(self, u: int, v: int):
        if v in self.graph_list[u]:
            self.graph_list[u].remove(v)

        if u in self.graph_list[v]: #same thing
            self.graph_list[v].remove(u)

if __name__ == "__main__":
    graph = Graph(6)
    vertices = ((0, 2), (0, 4), (2, 1),
                   (2, 3), (2, 5), (3, 0),
                   (3, 5), (4, 5), (5, 1))
    for u, v in vertices:
        graph.add(u, v)
        
    graph.dft(0)

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)