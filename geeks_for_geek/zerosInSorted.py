def solve():
    n = int(input())
    array = [int(i) for i in input().split()]

    # print(n - sum(array))
    left = 0
    right = n - 1
    while left <= right:
        middle = left + (right - left)//2

        if array[middle] == 0 and (middle == 0 or array[middle -1] == 1):
            break

        if array[middle] == 1:
            left = middle + 1

        else:
            right = middle -1

    print(n - middle)

t = int(input())
while t:
    solve()
    t -= 1
