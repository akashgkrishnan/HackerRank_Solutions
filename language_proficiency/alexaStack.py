def twoStacks(x, a, b):
    runningSum = 0
    counter = 0
    minimumTop = min(a[-1], b [-1])

    while runningSum + minimumTop <= x:

        if a[-1] <= b[-1]:
            val = a.pop()
        else:
            val = b.pop()
        counter += 1
        runningSum += val
        minimumTop = min(a[-1], b [-1])

    return counter

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        print(result)
