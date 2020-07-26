best sol
def gamingArray(array):
    count = 0
    max_element = 0
    for item in array:
        if item > max_element:
            max_element = item
            count += 1

    if count % 2 == 0:
        return 'ANDY'
    else:
        return 'BOB'

next best sol
def gamingArray(array):
    newArray = array[:]
    maxArray = [0 for _ in array]
    maxArray[0] = array[0]
    indexMap = dict()
    indexMap[array[0]] = 0
    for i in range(1,len(array)):
        maxArray[i] = max(maxArray[i-1], array[i])
        indexMap[array[i]] = i
    count = 0
    while array:
        count += 1
        max_elem = maxArray[-1]
        del array[indexMap[max_elem]:]
        del maxArray[indexMap[max_elem]:]

    if count % 2 == 0:
        print('ANDY')
    else:
        print('BOB')


if __name__ == '__main__':


    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)
