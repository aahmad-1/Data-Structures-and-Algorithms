import math

def salesman(city_map):
    n = len(city_map)

    # Precompute minimum outgoing edge per city (used for lower bound)
    min_edge = []
    for i in range(n):
        smallest = math.inf
        for j in range(n):
            if i != j and city_map[i][j] < smallest:
                smallest = city_map[i][j]
        min_edge.append(smallest)

    # Best known solution so far ("p" in the PDF)
    best_cost = math.inf
    best_path = None

    # Stores the current partial solution
    path = [0] * (n + 1)
    path[0] = 0

    # Like "included[]" in PDF examples
    visited = [False] * n
    visited[0] = True

    # Lower bound function (based on section 5.5.8 PDF idea)
    def estimate_remaining():
        """Sum of minimum outgoing edges of unvisited cities."""
        est = 0
        for c in range(n):
            if not visited[c]:
                est += min_edge[c]
        return est

    # Branch-and-bound search following the PDF structure
    def search(depth, current_cost):
        nonlocal best_cost, best_path

        # Lower bound pruning:
        # h + estimate >= p  → prune (PDF logic)
        if current_cost + estimate_remaining() >= best_cost:
            return

        # All cities visited → complete cycle
        if depth == n:
            total = current_cost + city_map[path[n - 1]][path[0]]
            if total < best_cost:
                best_cost = total
                best_path = path[:n] + [0]
            return

        # Try next cities
        for next_city in range(1, n):
            if not visited[next_city]:
                new_cost = current_cost + city_map[path[depth - 1]][next_city]

                # Early prune (same idea as h >= p in PDF)
                if new_cost >= best_cost:
                    continue

                visited[next_city] = True
                path[depth] = next_city

                search(depth + 1, new_cost)

                visited[next_city] = False

    # Start search from city 0 (like search(0,0) in PDF)
    search(1, 0)

    return best_path


if __name__ == "__main__":
    cost = 0
    city_map = [
        [ 0, 12, 19, 16, 29],
        [12,  0, 27, 25,  5],
        [19, 27,  0,  8,  4],
        [16, 25,  8,  0, 14],
        [29,  5,  4, 14,  0]
    ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]

    print(path)
    print(cost)