#User function Template for python3
def sort012(array, N):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in array:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1

    print(count_0, count_1, count_2)

    i = 0
    while 0 < count_0:
        array[i] = 0
        i += 1
        count_0 -= 1

    while 0 < count_1:
        array[i] = 1
        i += 1
        count_1 -= 1

    while 0 < count_2:
        array[i] = 2
        i += 1
        count_2 -= 1

    return array


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
