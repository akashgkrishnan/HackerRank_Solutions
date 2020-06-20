import numpy

def arrays(arr):
    # fist = list(map(float, arr[::-1]))
    return numpy.array(arr[::-1], float)
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
