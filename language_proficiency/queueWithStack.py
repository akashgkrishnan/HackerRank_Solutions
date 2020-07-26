# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

class MyQueue:
    def __init__(self):
        self.inStack = deque()
        self.outStack = deque()

    def enque(self, value):
        self.inStack.append(value)

    def moveToOutStack(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())


    def deque(self):
        if not self.outStack:
            self.moveToOutStack()
        self.outStack.pop()

    def peekFront(self):
        if not self.outStack:
            self.moveToOutStack()
        return self.outStack[-1]


q = int(input())

queue = MyQueue()
for _ in range(q):
    query = input().split()

    if len(query) == 1:
        if  query[0] == '2':
            queue.deque()
        elif query[0] == '3':
            print('ans', queue.peekFront())
    else:
        value = int(query[1])
        queue.enque(value)
