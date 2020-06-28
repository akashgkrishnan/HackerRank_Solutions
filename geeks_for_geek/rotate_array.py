def rotator(array, d):
    n = [0] * len(array)

    for i in range(len(array)):
        n[i-d] = array[i]
    return n

T = int(input())
for i in range(T):
    N, D = list(map(int, input().split()))
    array = list(map(int, input().split()))
    ans = rotator(array, D)
    print(ans)
