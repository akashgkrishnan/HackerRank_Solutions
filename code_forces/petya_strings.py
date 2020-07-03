string1 = input().lower()
string2 = input().lower()
for index, value in enumerate(string1):
    if ord(value) > ord(string2[index]):
        return
