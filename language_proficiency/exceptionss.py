# You are given two values  and .
# Perform integer division and print .

# Input Format

# The first line contains , the number of test cases.
# The next  lines each contain the space separated values of  and .

# Constraints

# Output Format

# Print the value of .
# In the case of ZeroDivisionError or ValueError, print the error code.

# Sample Input

# 3
# 1 0
# 2 $
# 3 1

for i in range(int(input())):
    a, b = input().split()
    
    try:
        print(int(a) // int(b) )
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)