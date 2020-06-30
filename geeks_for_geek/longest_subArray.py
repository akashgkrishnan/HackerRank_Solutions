def subarray_finder(array):
    longest = 0
    counter = 0
    for item in array:
        if item < 0:
            if longest <= counter:
                longest = counter
            counter = 0
        else:
            counter += 1
    return max(longest, counter)

N = int(input())
for i in range(N):
    input()
    array = list(map(int, input().split()))
    ans = subarray_finder(array)
    print(ans)
