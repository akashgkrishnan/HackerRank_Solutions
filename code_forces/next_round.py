def helper(scores, threshold):
    if threshold == 0:
        return 0

    count =0

    for i in scores:
        if i >= threshold:
            count += 1

    return count

n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
threshold = scores[k -1]

print(helper(scores, threshold))
