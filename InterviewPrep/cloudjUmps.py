
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds):
    count = 0
    emmaIdx = 0
    while emmaIdx + 1 < len(clouds):
        if clouds[emmaIdx + 2] and clouds[emmaIdx + 2] != 1:
            emmaIdx += 2
        else:
            emmaIdx += 1
        count += 1


    return count

if __name__ == '__main__':


    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
