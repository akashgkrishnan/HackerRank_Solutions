def show_array(array):
    for i in array:
        print(i, end = ' ')
    print()

def insertionSort1( array):
    final = array[-1]
    i = len(array) -1
    print(f'{final}')

    while i > 0:
        if array[i-1] > final:
            array[i] = array[i-1]
        else:
            array[i] = final
        show_array(array)
        i -= 1
    if final in array:
        pass
    else:
        array[0] = final
        show_array(array)

array = list(map(int, input().split()))
print(insertionSort1(array))
