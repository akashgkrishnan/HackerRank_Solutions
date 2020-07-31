#code
def rangeOperator(array, left, right, k):
    array[left] += k
    array[right + 1] -= k


t = int(input())
while t:
    n, m = input().split()
    array = [0] * (int(n)+1)

    for i in range(int(m)):
        a,b,k = list(map(int, input().split()))
        rangeOperator(array, a, b, k)

    sum = 0
    maxSum = float('-inf')
    for i in  range(len(array)):
        sum += array[i]
        maxSum = max(sum, maxSum)
    print(maxSum)
    t -= 1
