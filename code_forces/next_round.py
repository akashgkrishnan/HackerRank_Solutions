def helper(scores, k):
    threshold = scores[k-1]

    count = 0
    for score in scores:
        if score >= threshold and score > 0:
            count += 1
    return count


n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
threshold = k

print(helper(scores, k))
