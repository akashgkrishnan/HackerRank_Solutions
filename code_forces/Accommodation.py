count = 0
for _ in range(int(input())):
    p, q = list(map(int, input().split()))
    if q - p >= 2:
        count += 1
        
print(count)
