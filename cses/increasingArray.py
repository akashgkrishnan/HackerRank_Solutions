n = int(input())
array = list(map(int, input().split()))
count = 0
maxSoFar = float('-inf')
for item in (array)c:
    maxSoFar = max(maxSoFar, item)
    count += maxSoFar - item
print(count)
