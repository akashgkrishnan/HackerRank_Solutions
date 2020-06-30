def marsExploration(string):
    error_count = 0
    for i in range(0,len(string), 3):
        s = string[i: i + 3]
        if s != 'SOS':
            if s[0] != 'S':
                error_count += 1
            if s[1] != '0':
                error_count += 1
            if s[2] != 'S':
                error_count += 1
    return error_count

string = 'SOSSOT'
print(marsExploration(string))
