
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        
    def rotate(self, k):
        addToEnd = self.head
        node = self.head
        for i in range(k-1):
            node = node.next

        newHead = node.next
        node.next = None

        self.head = newHead
        self.tail.next = addToEnd

    def __repr__(self):
        node = self.head
        ans = ''
        while node:
            ans += str(node.value) + '-->'
            node  = node.next
        
        return ans + 'None'

        
array = [int(i) for i in input().split()]
ll = linkedList()
for num in array:
    ll.insert(num)
print(ll)
k = 2
ll.rotate(k)
print(ll)