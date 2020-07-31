#code
t = int(input())
while t:
    startRow = 0
    startCol = 0

    idx = 0
    matrix = []

    row, col = list(map(int, input().split()))
    array = list(map(int, input().split()))

    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(array[idx])
            idx += 1
    while startRow < row and startCol < col:
        for i in range(startCol, col):
            print(matrix[startRow][i], end = ' ')

        for i in range(startRow+ 1, row):
            print(matrix[i][col-1], end = ' ')

        for i in range(col-2, startCol-1, -1):
            if startRow == row-1:
                break
            print(matrix[row-1][i], end = ' ')

        for i in range(row-2, startRow, -1):
            if startCol == col-1:
                break
            print(matrix[i][startCol], end = ' ')
        startRow += 1
        startCol += 1
        row -= 1
        col -= 1
    print()
    t -= 1
