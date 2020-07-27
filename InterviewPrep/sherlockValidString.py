def isValid(string):
    stringCounts = dict()
    for char in string:
        if char in stringCounts:
            stringCounts[char] += 1
        else:
            stringCounts[char] = 1

    charCounts = set(v for v in stringCounts.values())
    if len(charCounts) == 1:
        return 'YES'

    




if __name__ == '__main__':


    s = input()

    result = isValid(s)
    print(result)
