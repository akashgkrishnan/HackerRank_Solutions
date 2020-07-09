N =int(input())
string = input()
if N >= 26:
    string = string.lower()
    if len(set(string)) == 26:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
