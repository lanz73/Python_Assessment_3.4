from collections import deque

graph = {
    "C": ["A", "S"],
    "A": ["C", "I"],
    "S": ["C", "N", "O"],
    "I": ["A", "N"],
    "N": ["I", "S", "O"],
    "O": ["N", "S"]
}

def bfs(graph, start):
    visited, queue, order = {start}, deque([start]), []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

if __name__ == "__main__":
    print("GRAPH - CASINAO")
    print("Adjacency List:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {', '.join(neighbors)}")
    print("\nBFS:", " - ".join(bfs(graph, "C")))
    print("DFS:", " - ".join(dfs(graph, "C")))
