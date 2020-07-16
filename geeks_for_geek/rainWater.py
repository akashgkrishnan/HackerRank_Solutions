#code
def rainWater(heights):
    left_max = 0
    right_max = 0
    left = []
    right = []
    result = [0] * len(heights)

    for value in heights:
        left.append(left_max)
        left_max = max(left_max, value)


    for value in reversed(heights):
        right.append(right_max)
        right_max = max(right_max, value)


    right = list(reversed(right))


    for index, height in enumerate(heights):
        if height < min(right[index], left[index]):
            result[index] = min(right[index], left[index]) - height
        else:
            result[index] = 0
    return sum(result)



heights =[0,8,0,0,5,0,0,10,0,0,1,1,0,3]
print(rainWater(heights))
