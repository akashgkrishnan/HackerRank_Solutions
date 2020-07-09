lamak, bob = list(map(int, input().split()))
count = 0
while lamak <= bob:
    lamak *= 3
    bob *= 2
    count += 1
print(count)
