num_of_queries = int(input())
stack = []
max_stack = []
for i in range(num_of_queries):
    query = input().split()
    if len(query) > 1:
        value = int(query[1])
        stack.append(value)
        current_max = value
        if max_stack:
            curent_max = max(max_stack[-1], value)

        max_stack.append(current_max)
    elif query[0] == 2:
        stack.pop()
        max_stack.pop()

    elif query[0] == 3:
        print(max_stack[-1])
