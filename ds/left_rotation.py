if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    new = [None] * len(a)
    store = {}
    for i in range(len(a)):
        store[i - d] = a[i]

    for k, v in store.items():
        new[k] = str(v)

    print(" ".join(new))
