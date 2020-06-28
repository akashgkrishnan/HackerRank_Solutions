
def getMaxScore(jewels):
    if len(jewels) == 0 or jewels is None:
        return 0
    sums = 0
    char_jewels = list(jewels)
    idx = 0
    length = len(char_jewels)-1
    while idx < len(char_jewels)-1:
        if char_jewels[idx] == char_jewels[idx + 1]:
            sums += 1
            char_jewels.pop(idx)
            char_jewels.pop(idx + 1)
            idx = 0
            length -= 2
        idx += 1
    return sums





if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)
        print(ans)
