from collections import defaultdict, deque

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


def solve(source, destination, edges, n):
    g = Graph(v)
    for u,v in edges:
        g.addEdge(u, v)

    visited = set()
    q = deque()
    q.append(source)
    count = 0
    graph = g.graph
    while q:
        node = q.popleft()
        if node == destination:
            count += 1
            continue

        
        if node in visited:
            return "INFINITE PATHS"
        
        visited[node] = True
        if node in graph:
            for child in graph[node]:
                q.append(child)

    return count

        
    

n, m = [int(i) for i in input().split()]

edges = []

for i in range(m):
    edges.append([int(i) for i in input().split()])

source, destination = [int(i) for i in input().split()]

print(solve(source, destination, edges, n))