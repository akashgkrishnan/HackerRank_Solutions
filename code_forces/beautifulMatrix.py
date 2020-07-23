array = []
for i in range(5):
    row = input().split()
    array.append(row)
for i in range(5):
    for j in range(5):
        if array[i][j] == '1':
            print(abs(2-i) + abs(2-j))
            break
