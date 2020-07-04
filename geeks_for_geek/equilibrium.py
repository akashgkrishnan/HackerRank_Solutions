# O(N^3)
# def helper(array):
#         for j in range(N):
#             left_sum = sum(array[:j])
#             right_sum = sum(array[j+1:])
#             if left_sum == right_sum:
#                 return j +1
#         return -1
#
# for i in range(int(input())):
#     N = int(input())
#     array = list(map(int, input().split()))
#     print(helper(array))

def helper(array):
    total_sum = sum(array)
    left_sum = 0
    for num in array:
        total_sum -= num

        if total_sum == left_sum:
            return i
        left_sum += num
    return -1



for i in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    print(helper(array))
