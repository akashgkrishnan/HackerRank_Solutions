from collections import defaultdict


def solve():
    n = int(input())
    array = [int(i) for i in input().split()]

    counts = defaultdict(int)
    for item in array:
        counts[item] += 1

    ans = []
    for num, count in counts.items():
        if count%2 == 1:
            ans.append(num)

    ans.sort()
    for item in ans:
        print(item, end=' ')
    print()


t = int(input())
while t:
    solve()
    t -= 1
