def longestCommonSubsequence(array, n):

    tracker = {item: True for item in array}
    longest = [0,0]
    for item in array:
        if tracker[item]:
            tracker[item] = False



            leftNum = item - 1
            rightNum = item + 1

            while leftNum in tracker:
                tracker[leftNum] = False
                leftNum -= 1

            while rightNum in tracker:
                tracker[rightNum] = False
                rightNum += 1

            leftNum += 1
            rightNum -= 1

            longest = max(longest, [leftNum, rightNum], key = lambda x : x[1]-x[0])

    return longest[1] - longest[0] + 1



t = int(input())
while t:
    n = int(input())
    array = [int(i) for i in input().split()]
    ans = longestCommonSubsequence(array, n)
    print(ans)
    t -= 1
