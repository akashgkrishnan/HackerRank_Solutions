def helper(num):
    rev_num = 0
    while num > 0:
        a = num % 10
        rev_num = a + rev_num * 10
        num = num//10
    print(rev_num)
for i in range(int(input())):
        num = int(input())
        helper(num)
