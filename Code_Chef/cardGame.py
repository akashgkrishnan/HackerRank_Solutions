def digitSum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num = num // 10
    return digit_sum
    
T = int(input())
for i in range(T):
    N = int(input())
    chefScore = 0
    mortyScore = 0

    for i in range(N):

        Ai, Bi = list(map(int, input().split()))

        Ai = digitSum(Ai)
        Bi = digitSum(Bi)

        if Ai > Bi:
            chefScore += 1
        elif Bi > Ai:
            mortyScore += 1
        else:
            chefScore += 1
            mortyScore += 1
    if chefScore > mortyScore:
        print("0 {}".format(chefScore))
    elif mortyScore > chefScore:
        print("1 {}".format(mortyScore))
    else:
        print("2 {}".format(chefScore))
