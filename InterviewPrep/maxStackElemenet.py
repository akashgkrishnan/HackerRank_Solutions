# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        self.maxStack = deque()

    def push(self, value):
        self.stack.append(value)
        if self.maxStack:
            self.maxStack.append(max(self.maxStack[-1], value))
        else:
            self.maxStack.append(value)

    def peekMax(self):
        return self.maxStack[-1]

    def popTop(self):
        self.maxStack.pop()
        return self.stack.pop()

stack = Stack()
for _ in range(int(input())):
    query = input().split()

    if len(query) == '1':

        if query[0] == '2':
            print(stack.popTop())
        elif query[0] == '3':
            print(stack.peekMax())

    else:
        value = int(query[1])
        stack.push(value)
