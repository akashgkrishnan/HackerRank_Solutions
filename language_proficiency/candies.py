def candies(n, array):
    candies = [1 for _ in array]

    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            candies[i + 1] = candies[i] + 1



    for i in reversed(range(len(array))):
        if array[i-1] > array[i]:
            candies[i-1] = max(candies[i-1], candies[i] + 1)


    print(candies)

    return sum(candies)


if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
