counter = 0
number = input()
for i in number:
    if i == '7' or i == '4':
        counter += 1
if counter == 7 or counter == 4:
    print('YES')
else:
    print('NO')
