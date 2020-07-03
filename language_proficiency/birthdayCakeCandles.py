def birthdayCakeCandles(arr):
    return arr.count(max(arr))

if __name__ == '__main__':


    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
