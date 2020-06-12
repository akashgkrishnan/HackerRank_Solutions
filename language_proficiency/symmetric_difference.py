# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

# Input Format

# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.

# Sample Input

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Sample Output

# 5
# 9
# 11
# 12



input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
A = list(a.symmetric_difference(b))
for i in sorted(A):
    print(i)
