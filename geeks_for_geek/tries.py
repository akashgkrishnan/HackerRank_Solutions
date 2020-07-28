class suffixTrie:
    def __init__(self, stringList):
        self.root = dict()
        self.endingCharacter = '*'
        self.buildSuffixTrie(stringList)

    def builder(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = dict()
            node = node[letter]
        node[self.endingCharacter] = True




    def buildSuffixTrie(self, stringList):
        for string in stringList:
            for i in range(len(string)):
                self.builder(i, string)


    def searchString(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return 0
            node = node[letter]
        if self.endingCharacter in node:
            return 1
        else:
            return 0





t = int(input())
while t:
    length = int(input())
    stringList = input().split()
    searchString = input()
    suffix = suffixTrie(stringList)
    print(suffix)
    print(suffix.searchString(searchString))

    t -= 1
