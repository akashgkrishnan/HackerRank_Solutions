t = int(input())
while t:
    n, e = list(map(int, input().split()))
    edgePairs = list(map(int, input().split()))

    vertex = dict()
    for i in range(0, len(edgePairs)-1, 2):
        if edgePairs[i] in vertex:
            vertex[edgePairs[i]] += 1
        else:
            vertex[edgePairs[i]] = 1
    print(vertex)
    print(sum(v for v in vertex.values()))

    t-= 1
