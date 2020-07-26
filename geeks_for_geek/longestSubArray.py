t = int(input())
while t:
    n = int(input())
    array = list(map(int, input().split()))

    count = 0
    maxCount = 0
    for index, item in enumerate(array):
        if item >= 0:
            count += 1
        else:
            maxCount = max(count, maxCount)
            count = 0
    print('ans ->', max(maxCount, count))
     t-= 1
