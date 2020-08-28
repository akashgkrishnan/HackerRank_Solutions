
def canCompleteCircle(i, petrol, distance, n):
    start = i
    petrolLeft = petrol[i] - distance[i]
    i += 1

    while True:
        if i == start:
            return True
        currentPetrol = petrolLeft + petrol[i]
        if distance[i] > currentPetrol:
            return False
        petrolLeft = currentPetrol - distance[i]
        i += 1
        if i == n:
            i = 0


def tour(lis, n):
    petrol = [item[0] for item in lis]
    distance = [item[1] for item in lis]

    if sum(petrol) < sum(distance):
        return -1

    for i in range(len(petrol)):
        if petrol[i] >= distance[i]:
            if canCompleteCircle(i, petrol, distance, n):
                return i
    return -1


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2 * n, 2):
            lis.append([arr[i - 1], arr[i]])
        print(tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends
