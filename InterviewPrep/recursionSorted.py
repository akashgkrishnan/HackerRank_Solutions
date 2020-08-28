def isSortedArray(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isSortedArray(A[1:])
print(isSortedArray([1,21,3,4,5,6]))
