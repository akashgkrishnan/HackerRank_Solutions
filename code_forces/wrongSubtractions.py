nk = input().split()
num = int(nk[0])
k = int(nk[1])
for _ in range(k):
    lastDigit = num % 10
    if lastDigit == 0:
        num = num // 10
    else:
        num -= 1
print(num)
