
allTools = {
 '!':0,
 '#':1,
 '$':2,
 '%':3,
 '&':4,
 '*':5,
 '@':6,
 '^':7,
 '~':8
 }

t = int(input())
while t:
    n = int(input())

    nuts = set(input().split())
    bolts = input().split()
    result = [0] * 9
    count = 0
    for item in bolts:
        if item in nuts:
            result[allTools[item]] = item


    for item in result:
        if item != 0:
            print(item, end = ' ')
    print()
    for item in result:
        if item != 0:
            print(item, end = ' ')

    print()
    t -= 1
