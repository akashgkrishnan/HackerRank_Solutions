string = input()
if len(string) > 1:
    result_str = sorted(string.split('+'))
    print("+".join(result_str))
else:
    print(string)
