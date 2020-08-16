
class MyQueue:
    def __init__(self):
        self.head = None


     def push(self, item):
         newNode = Node(item)
         if self.head is None:
             self.head = newNode
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newNode

     def pop(self):
         if self.head is None:
             return -1

        node = self.head
        self.head = self.head.next
        node.next = None
        return node.data
