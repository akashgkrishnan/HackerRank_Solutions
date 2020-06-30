def superReducedString(string):
    stack = []
    for token in string:
        if stack:
            if stack[-1] == token:
                stack.pop()
            else:
                stack.append(token)
        else:
            stack.append(token)

    if len(stack) == 0:
        return 'Empty String'
    return ''.join(stack)

print(superReducedString(input()))
