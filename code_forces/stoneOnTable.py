
def helper(string, n):
    if n < 2:
        return 0
    count = 0
    idx = 0
    next_idx = idx + 1
    while next_idx < n:
        if string[idx] == string[next_idx]:
            '''
            #check if the item at next indx = to one at current index
            if they are equal move the next pointer to the  next index
            if they are not equal then both the pointers needs to be updated
            the next pointer is the fast running pointer
            in case we find the next and current are equal we shift the next pointer by one to check if the next index is also equal

            '''
            next_idx += 1
            count += 1
        else:
            idx = next_idx
            next_idx += 1
    return count
n = int(input())
string = list(input())
ans = helper(string, n)
print(ans)
