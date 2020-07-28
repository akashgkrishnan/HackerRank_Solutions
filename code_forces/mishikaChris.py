t = int(input())
mishika = 0
chris = 0
while t:
    m, c = input().split()
    if int(m) > int(c):
        mishika += 1
    elif int(c) > int(m):
        chris += 1
    else:
        mishika += 1
        chris += 1
    t -= 1
if mishika > chris:
    print('Mishka')
elif chris > mishika:
    print('Chris')

else:
    print('Friendship is magic!^^')
