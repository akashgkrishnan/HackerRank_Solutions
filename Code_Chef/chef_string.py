def finder(array, N):
    sums = 0
    for j in range(N - 1):
        sums += abs(array[j] - array[j + 1]) - 1
    return sums


T = int(input())
for i in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    sums = finder(array, N)
    print(sums)
