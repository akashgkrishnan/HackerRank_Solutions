#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def getNeighbours(i, j, grid, visited):
    neighbours = []
    if i > 0 and not visited[i - 1][j]:
        neighbours.append([i-1, j])
    if i < len(grid) - 1 and not visited[i + 1][j]:
        neighbours.append([i + 1, j])
    if j > 0 and not visited[i][j-1]:
        neighbours.append([i, j - 1])
    if j < len(grid[0]) -1 and not visited[i][j + 1]:
        neighbours.append([i,j + 1])

    return neighbours



def traverseNodes(i, j, grid, visited, ones_array):
    nodes_toExplore = [[i, j]]
    connected_size = 0
    while nodes_toExplore:
        current_node = nodes_toExplore.pop()
        i = current_node[0]
        j = current_node[1]

        if visited[i][j]:
            continue

        visited[i][j] = True
        if grid[i][j] == 0:
            continue

        connected_size += 1

        neighbours= getNeighbours(i, j, grid, visited)
        # diagonalNeighbours= getDiagonalNeighbours(i, j, grid, visited)

        for node in neighbours:
            nodes_toExplore.append(node)

        # for node in diagonalNeighbours:
        #     nodes_toExplore.append(node)


    if connected_size > 0:
        ones_array.append(connected_size)



def maxRegion(grid):
    ones_array = []
    visited = [[False for value in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, grid, visited, ones_array)
    return max(ones_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
