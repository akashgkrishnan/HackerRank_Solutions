def findNoOfNotes(distance):
    maxSteps = [5, 4, 3, 2, 1]
    numOfSteps = 0
    idx = 0
    while distance > 0 and idx < 6:
        step = maxSteps[idx]
        if step <= distance:
            numOfSteps += distance // step
            distance = distance % step
        idx += 1
    return numOfSteps



stepCount = findNoOfNotes(int(input()))
print(stepCount)
