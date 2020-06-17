def slice_sum(slice, value):
    for i in range(len(slice)):
        slice[i] += value



def arrayManipulation(n, queries):
    array = [0] * n
    print(queries)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]

        for i in range(a-1,b):
            array[i] += k

    print(max(array))



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
