import re


for i in range(int(input())):
    s = input()
    new = re.sub(' &{2} ', ' and ', s)
    after = re.sub(' \|{2} ', ' or ', new)
    print(after)
