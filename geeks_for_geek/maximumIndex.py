def solve():
    n = int(input())
    array = [int(i) for i in input().split()]
    leftMin = [0] * n
    leftMin[0] = array[0]
    for i in range(1, len(array)):
        leftMin[i] = min(leftMin[i-1], array[i])


    rightMax = [0] * n
    rightMax[-1] = array[-1]

    for i in range(len(array)-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], array[i])


    i = 0
    j = 0
    maxDiff = 0
    while j < n and i < n:
        if leftMin[i] <= rightMax[j]:
            maxDiff = max(maxDiff, j - i)
            j += 1
        else:
            i += 1
    print(maxDiff)




t = int(input())
while t:
    solve()
    t -= 1
