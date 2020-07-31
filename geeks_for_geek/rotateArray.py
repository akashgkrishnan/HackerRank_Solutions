t = int(input())
while t:
    n = int(input())
    elems = list(map(int, input().split()))
    idx = 0
    array = []
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(elems[idx])
            idx += 1
        # print(array[i])
    print(array)
    array.reverse()
    print(array)
    for i in range(len(array)):
        for j in range(i):
            array[i][j], array[j][i] = array[j][i], array[i][j]

    print(array)
    t -= 1
