def findNoOfNotes(amount):
    denominations = [100, 50, 10, 5, 2, 1]
    numOfNotes = 0
    idx = 0
    while amount > 0 and idx < 6:
        denom = denominations[idx]
        if denom < amount:
            numOfNotes += amount // denom
            amount = amount % denom
        idx += 1
    return numOfNotes


for _ in range(int(input())):
    amount = int(input())

    noteCount = findNoOfNotes(amount)
    print(noteCount)
