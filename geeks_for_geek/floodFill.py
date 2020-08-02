from collections import deque
def findNeighBourNodes(image, currentColor, i, j):
    neighbours = []
    if i > 0 and image[i-1][j] == currentColor:
        neighbours.append([i-1, j])
    if i < len(image)-1 and image[i+1][j] == currentColor:
        neighbours.append([i+1, j])

    if j > 0 and image[i][j-1] == currentColor:
        neighbours.append([i, j-1])
    if j < len(image[0]) - 1 and image[i][j + 1] == currentColor:
        neighbours.append([i, j + 1])
    return neighbours

def floodFill(image, rows, cols, k):
    currentColor = image[rows][cols]
    newColor = k

    queue = deque()
    queue.append([rows, cols])
    while queue:
        current = queue.popleft()

        i = current[0]
        j = current[1]

        if image[i][j] != currentColor:
            continue

        image[i][j] = newColor

        neighBourNodes = findNeighBourNodes(image, currentColor, i, j)

        for node in neighBourNodes:
            queue.append(node)

    return image

t = int(input())
while t:
    rows, cols = list(map(int, input().split()))
    elems = list(map(int, input().split()))
    image = []
    idx = 0
    for i in range(rows):
        image.append([])
        for j in range(cols):
            image[i].append(elems[idx])
            idx += 1

    x, y, k = list(map(int, input().split()))
    grid = floodFill(image, x, y, k)
    for row in grid:
        for item in row:
            print(item, end = ' ')

    print()

    t -= 1
