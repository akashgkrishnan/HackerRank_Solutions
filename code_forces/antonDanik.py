t = int(input())
string = input()
anton = 0
danik = 0
for i in string:
    if i == 'A':
        anton += 1
        continue
    else:
        danik += 1
ans = 'Anton' if anton > danik else 'Danik'
if anton == danik:
    print('Friendship')
else:

    print(ans)
