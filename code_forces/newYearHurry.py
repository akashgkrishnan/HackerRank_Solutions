nk = input().split()
numOfQuestions = int(nk[0])
travelTimeToParty = int(nk[1])
timeWithLimak = 240 - travelTimeToParty
solveProblemIn = [5 * i for i in range(1, numOfQuestions + 1)]
count = 1
if timeWithLimak >= 5:
    for i in range(1,len(solveProblemIn)):
        solveProblemIn[i] = solveProblemIn[i-1] + solveProblemIn[i]
        if solveProblemIn[i] <= timeWithLimak:
            count += 1
        else:
            break

    print(count)
else:
    print(0)
