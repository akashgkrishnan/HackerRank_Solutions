# ou are given a polynomial  of a single indeterminate (or variable), x and k
# You are also given the values of  and . Your task is to verify if P(x) =k

# Constraints
# All coefficients of polynomial  are integers.
#  and  are also integers.

# Input Format

# The first line contains the space separated values of x and k
# The second line contains the polynomial P

# Output Format

# Print True if .P(x) = k Otherwise, print False.

# Sample Input

# 1 4
# x**3 + x**2 + x + 1

x, k = map(int, input().split())
expression = input()

print(eval(expression) == k)