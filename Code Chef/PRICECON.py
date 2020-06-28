T = int(input())
for i in range(T):
	N, K = list(map(int, input().split()))
	prices = list(map(int, input().split()))
	total_sale = sum(prices)
	loss_sale = sum(price if price < K else K  for price in prices)
	print(total_sale - loss_sale)
