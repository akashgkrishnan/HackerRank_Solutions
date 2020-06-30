def finder(array):
    tracker = {}
    for item in  array:
        if item in tracker:
            tracker[item] += 1
        else:
            tracker[item] = 1

    for k, v in tracker.items():
        if v == 1:
            return k



for i in range(int(input())):
    n, k = input().split()
    array = list(map(int, input().split()))
    ans = finder(array)
    print(ans)
