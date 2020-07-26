string = input()

result = []
count = 1

if len(string) == 1:
    print('(1, {})'.format(string[0]))
else:

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            result.append((count, int(string[i-1])))
            count = 1
    result.append((count, int(string[i])))


    for item in result:
        print(item, end = ' ')
