def helper_function(array1, array2, array3, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    common_found = False
    while i < n1 and j < n2 and k < n3:
        x = array1[i]
        y = array2[j]
        z = array3[k]

        if x == y == z:
            common_found = True
            print (x, end = ' ')
            i += 1
            j += 1
            k += 1

        if x < y:
            i += 1
        elif y < z:
            j += 1
        else:
            k += 1
    if common_found:
        print()
    else:
        print(-1)




T = int(input())
for i in range(T):
    a, b, c = list(map(int, input().split()))
    N1 = list(map(int, input().split()))
    N2 = list(map(int, input().split()))
    N3 = list(map(int, input().split()))
    helper_function(N1, N2, N3, a, b, c)
