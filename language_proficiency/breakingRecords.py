# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_record_change = 0
    max_record_change = 0
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_record_change += 1
            continue
        if scores[i] < min_score:
            min_score = scores[i]
            min_record_change += 1
            continue
    return [max_record_change ,min_record_change]



if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
