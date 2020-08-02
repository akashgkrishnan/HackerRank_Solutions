

import math
import os
import random
import re
import sys

def findNeighbours(grid, visited, i, j):
    neighbors = []

    if i > 0 and j > 0 and not visited[i-1][j-1]:
        neighbors.append([i-1, j-1])

    if i < len(grid) - 1 and j < len[grid[0]] - 1 and not visited[i + 1][j + 1]:
        neighbors.append([i+1, j + 1])

    if i > 0 and j < len(grid[0])-1 and not visited[i-1][j + 1]:
        neighbors.append([i-1, j + 1])

    if i < len(grid) - 1 and j > 0 and not visited[i+1][j-1]:
        neighbors.append([i+1, j - 1])

    if i > 0 and not visited[i-1][j]:
        neighbors.append([i-1, j])

    if i < len(grid)-1 and not visited[i+1][j]:
        neighbors.append([i+1, j])

    if j > 0 and not visited[i][j-1]:
        neighbors.append([i][j-1])

    if j < len(grid[0]) - 1 and not visited[i][j + 1]:
        neighbors.append([i][j+1])
    return neighbors


def travelNode(grid, i, j, visited, cells):
    queue = [[i, j]]

    sums = 0
    while queue:
        current = queue.pop()
        i = current[0]
        j = current[1]

        if not visited[i][j]:
            continue

        visited[i][j] = True

        if grid[i][j] == 0:
            continue
        sums += 1

        neigbors = findNeighbours(grid, visited, i, j)

        for node in neighbors:
            queue.append(node)

    if sums > 0:
        cells.append(sums)


def maxRegion(grid):
    visited = [[False for _ in row] for row in grid]
    cells = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                travelNode(grid, i, j, visited, cells)
    return max(cells)


if __name__ == '__main__':


    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)
    print(res)
