string = input()
token = string[1:len(string)-1]

if token:
    ans = set(token.split(', '))
    print(len(ans))
else:
    print(0)
