n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p.extend(q)
p= list(set(p))
if sum(p) == (n * (n+1))//2:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
