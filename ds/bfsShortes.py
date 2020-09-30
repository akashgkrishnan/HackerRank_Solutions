from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.v = v

    def addEdge(self, u, v):
        self.graph[u].append(v)


def bfs(n, m, edges, start):

    g = Graph(n)

    graph = g.graph

    for u, v in edges:
        g.addEdges(u, v)

    q = deque()

    q.append((start, 0))
    distances = dict()

    while q:
        node, dist = q.popleft()

        if node in graph:
            for child in graph[node]:
                distances[child] = dist + 6
                q.append((child, dist + 6))

    result = []
    for i in range(1, n + 1):
        if i == s:
            continue

        if i in distances:
            result.append(distances[i])
        else:
            result.append(-1)
            
    return result
    


    
q = int(input())

for q_itr in range(q):
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    s = int(input())

    result = bfs(n, m, edges, s)

    print(result)