
def dfsHelper(node, visited, graph, array):
    visited[node] = True
    array.append(node)

    for child in graph[node]:
        if visited[child] == False:
            dfsHelper(child, visited, graph, array)


def dfs(graph,N):
    visited = [False] * (max(graph)+1)
    array = []
    dfsHelper(0, visited,graph, array)
    return array
