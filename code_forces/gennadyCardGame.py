cardOnTable = input()
myCards = input().split()
for card in myCards:
    if card[1] == cardOnTable[1] or card[0] == cardOnTable[0]:
        print("YES")
        break
else:
    print('NO')
