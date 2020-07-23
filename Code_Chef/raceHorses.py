def helpers(skills, n):
    min_val = float('inf')

    skills.sort()
    for i in range(1, len(skills)):
        if min_val > skills[i] - skills[i-1]:
            min_val =skills[i] - skills[i-1]

    return min_val




T = int(input())
for _ in range(T):
    n = int(input())
    skills = list(map(int, input().split()))

    minSkillDiff = helpers(skills, n)
    print(minSkillDiff)
