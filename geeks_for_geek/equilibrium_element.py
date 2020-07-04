array = list(map(int, input().split()))
left_sum = 0
total_sum = sum(array)

for i in array:
    total_sum -= i

    if left_sum == total_sum:
        print(i)
        break
    left_sum += i
    
