from collections import OrderedDict
items = OrderedDict()
for i in range(int(input())):
    item_price = input()
    price = int(item_price.split().pop())
    item = " ".join(item_price.split()[:-1])

    if item in items:
        items[item] += int(price)
    else:
        items[item] = int(price)

for item in items:
    print(item, items[item])
