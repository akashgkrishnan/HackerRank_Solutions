k, n, w = list(map(int, input().split()))

total_amount = sum(range(0,w*k + 1, k))

money_needed = total_amount - n if total_amount > n else 0
print(money_needed)
