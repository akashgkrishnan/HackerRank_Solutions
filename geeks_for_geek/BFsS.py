from collections import deque

def bfs(graph,N):
    array = []
    visited = [False] * (N+1)

    queue = deque()
    queue.append(0)
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        array.append(node)

        for child in graph[node]:
            queue.append(child)
    return array
