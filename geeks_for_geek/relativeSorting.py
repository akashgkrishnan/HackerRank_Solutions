from collections import defaultdict

def makeArray(result, item , a1Counts):
    result += [item]*a1Counts[item]

def solve():
    #input
    n, m= list(map(int, input().split()))
    array1 = [int(i) for i in input().split()]
    array2 = [int(i) for i in input().split()]
    
    
    notInA2 = []
    
    a1Counts = defaultdict(int)
    
    setA2 = set(array2)
    
    for item in array1:
        if item in setA2:
            a1Counts[item] += 1
        else:
            notInA2.append(item)
    result =[]
            
    for item in array2:
        makeArray(result, item , a1Counts)
    
    notInA2.sort()
    result.extend(notInA2)
    
    return result

t = int(input())
while t:
    ans = solve()
    for item in ans:
        print(item, end = ' ')
    print()
    t -= 1