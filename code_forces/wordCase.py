string = input()
lCount = 0
uCount = 0
for item in string:
    if item.islower():
        lCount += 1
    else:
        uCount += 1
if uCount > lCount:
    print(string.upper())
else:
    print(string.lower())
