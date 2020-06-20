k, m = list(map(int, input().split()))
max_Res = 0
for i in range(k):
    max_Res += max(list(map(int, input().split()[1:])))

print(max_Res % m)
