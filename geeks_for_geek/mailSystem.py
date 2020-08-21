class Node:
    def __init__(self, msgId, value):
        self.msgId = msgId
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)


    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert



    def remove(self, node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:

            self.tail = self.tail.prev

        self.removeNodePtrs(node)

    def removeNodePtrs(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None


def updateMessageGroup(msgId, fromList, toList, fromGroup, toGroup):

    node = fromGroup[msgId]

    fromList.remove(node)
    fromGroup.pop(msgId)

    toList.setTail(node)
    toGroup[msgId] = node



def mainPrint(node):
    while node:
        print(node.msgId, end = ' ')
        node = node.next
    print()

def printInList(messageList):
    node = messageList.head

    if node is None:
        print('EMPTY')
    else:
        mainPrint(node)



t = int(input())
while t:
    n, m = [int(i) for i in input().split()]

    unread = dict()
    read = dict()
    trash = dict()

    unreadList = LinkedList()
    readList = LinkedList()
    trashList = LinkedList()


    for i in range(1, n+1):
        node = Node(i, True)
        unread[i] = node
        unreadList.setTail(node)


    queries = [int(i) for i in input().split()]

    for i in range(0, len(queries), 2):
        query = queries[i]
        msgIdx = queries[i + 1]

        if query == 1:
            updateMessageGroup(msgIdx, unreadList, readList, unread, read)

        elif query == 2:
            updateMessageGroup(msgIdx, readList, trashList, read, trash)

        elif query == 3:
            updateMessageGroup(msgIdx, unreadList, trashList, unread, trash)

        elif query == 4:
            updateMessageGroup(msgIdx, trashList, readList, trash, read)


    printInList(unreadList)
    printInList(readList)
    printInList(trashList)
    t -= 1

























            
