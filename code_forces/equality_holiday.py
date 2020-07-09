n = int(input())
money = list(map(int, input().split()))
max_money = max(money)
count = 0
for num in money:
    count += max_money - num
print(count)
