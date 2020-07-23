n = int(input())
array = list(map(int, input().split()))
if sum(array) > 0:
    print('HARD')
else:
    print('EASY')
