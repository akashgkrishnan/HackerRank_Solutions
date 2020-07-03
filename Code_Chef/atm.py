x, y = map(float, input().split())
print(x, y)
if x % 5 == 0 and x < y:
    print("{:.2f}".format(y-x-0.5))
else:
    print("{:.2f}".format(y))
