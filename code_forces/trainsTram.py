N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = list(map(int, input().split()))
total_pass = B[0]
max_pass = B[0]
for i in range(1,N):
    remaining_pass = total_pass - A[i]
    total_pass = remaining_pass + B[i]
    max_pass = max(total_pass, max_pass)
print(max_pass)
