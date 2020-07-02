count = 0
for i in range(int(input())):
    team_knowledge = list(map(int, input().split()))
    if sum(team_knowledge) > 1:
        count += 1
print(count)
