string = input()
start = 'A'
count = 0
max_count = 1
for char in string:
    if char == start:
        count += 1
        max_count = max(count, max_count)
    else:
        start = char
        count = 1
print(max_count)
