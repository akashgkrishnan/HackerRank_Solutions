def helper(string, L):
    print(string[0] + str(L-2) + string[-1])

T = int(input())
for i in range(T):
    string = input()
    L = len(string)
    if L > 10:
        helper(string, L)
    else:
        print(string)
