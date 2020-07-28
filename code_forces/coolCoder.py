num = int(input())
scores = list(map(int, input().split()))
count = 0
minScore = scores[0]
maxScore = scores[0]
for i in range(1, len(scores)):
    if scores[i] > maxScore:
        count += 1
        maxScore= scores[i]
        continue
    if scores[i] < minScore:
        count += 1
        minScore = scores[i]
print(count)
