if __name__ == '__main__':
    n = int(input())
    binary_n = bin(n)

    count = 0
    max_count = 0
    for item in str(binary_n):
        if item == '0':
            count = 0
        elif item == '1':
            count += 1
            max_count = max(count, max_count)
    print(max_count)
