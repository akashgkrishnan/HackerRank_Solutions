T = int(input())
N = int(input())

def leader_finder(array):
    ans = []
    potential_leader = 0
    for i in range(len(array)):
        is_leader = True
        potential_leader = array[i]
        for j in range(i + 1, len(array)):
            if array[j] > potential_leader:
                is_leader = False
                break
        if is_leader:
            ans.append(potential_leader)

    return ans






for i in range(T):
    array = list(map(int, input().split()))
    print(leader_finder(array))
