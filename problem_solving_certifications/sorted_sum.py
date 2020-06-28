def sortedSum(a):
    total = 0
    for i in range(len(a)):
        sub_array = a[:i+1]
        sub_array.sort()
        for index, value in enumerate(sub_array):
            total += value * (index+1)

    return total




if __name__ == '__main__':


    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = sortedSum(a)
    print(result)
