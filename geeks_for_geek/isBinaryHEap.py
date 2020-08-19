# code
def isMinHeap(array, n):
    lastParent = (n - 1) // 2
    for i in range(lastParent, -1, -1):
        childOne = array[(2 * i) + 1] if (2 * i) + 1 < n else -1
        childTwo = array[(2 * i) + 2] if (2 * i) + 2 < n else -1

        if childTwo != -1:
            if array[i] < childTwo:
                return False

        if childOne != -1:
            if array[i] < childOne:
                return False
    return True


t = int(input())
while t:
    n = int(input())
    array = [int(i) for i in input().split()]
    ans = isMinHeap(array, n)
    if ans:
        print(1)
    else:
        print(0)
    t -= 1
