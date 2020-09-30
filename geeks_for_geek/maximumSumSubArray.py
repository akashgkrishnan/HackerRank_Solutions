def solve():
    n, k = [int(i) for i in input().split()]
    array = [int(i) for i in input().split()]
    
    result = 0
    for i in range(k):
        result += array[i]
        
    currentSum = result
    for i in range(k, n):
        currentSum += array[i]
        currentSum -= array[i-k]
        
        result = max(result, currentSum)
        
    return result