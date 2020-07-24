t = int(input())
while t:
    nk = input().split()
    k = int(nk[1])
    firstArray = list(map(int, input().split()))
    secondArray = list(map(int, input().split()))
    
    firstArray.sort()
    secondArray.sort(reverse = True)

    for i in range(k):
        if firstArray[i] < secondArray[i]:
            firstArray[i] = secondArray[i]
    print(sum(firstArray))
    t -= 1
