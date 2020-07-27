
def maximumToys(prices, k):
    numOfToys = 0
    prices.sort()
    idx = 0
    while idx < len(prices):
        if prices[idx] > k:
            return numOfToys

        k -= prices[idx]
        numOfToys += 1
    return numOfToys





if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
