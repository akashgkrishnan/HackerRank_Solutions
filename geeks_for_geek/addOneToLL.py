#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

def reverseList(node):
    prev = None
    current = node
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def addOne(head):
    #Returns new head of linked List.
    node = head
    newHead = reverseList(node)

    carry = 1
    node = newHead

    while node:
        node.data += carry

        if node.data == 10:
            node.data = 0
            carry = 1

        else:

            carry = 0

        if node.next is None and carry == 1:
            node.next = Node(1)
            break
        node = node.next


    return reverseList(newHead)



#{
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):

        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list

        resHead = addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
