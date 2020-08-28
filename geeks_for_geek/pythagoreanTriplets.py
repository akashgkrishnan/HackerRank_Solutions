def solve():
    n = int(input())
    array = [int(i)**2 for i in input().split()]
    array.sort()

    for i in range(n-1, 1, -1):
        left = 0
        right = i -1
        while left < right:
            if array[right] + array[left] == array[i]:
                return True


            if array[right] + array[left] < array[i]:
                left += 1
            else:
                right -= 1
    return False
t = int(input())
while t:
    if solve():
        print('Yes')
    else:
        print('No')
    t -= 1
