class MinHeap:
    def __init__(self):
        self.heap = []
        
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[parentIdx] > heap[currentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def siftDown(self, currentIdx, endIdx, heap):
        childOne =  (2 * currentIdx) + 1
        while childOne <= endIdx:
            childTwo = (2 * currentIdx) + 2 if (2 * currentIdx) + 2 <= endIdx else -1
            if childTwo != -1 and heap[childTwo] < heap[childOne]:
                idxToSwap = childTwo
            else:
                idxToSwap = childOne

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOne = (2 * currentIdx) + 1
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)


    def remove(self, value):
        for idx, val in enumerate(self.heap):
            if val == value:
                self.swap(idx, len(self.heap)-1, self.heap)
                self.heap.pop()
                self.siftDown(idx, len(self.heap)-1, self.heap)
                break


    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

minHeap = MinHeap()
q = int(input())

while q:
    query = input().split()

    if len(query) == 1:
        print(minHeap.peek())
    else:
        if int(query[0]) == 1:
            minHeap.insert(int(query[1]))
        else:
            minHeap.remove(int(query[1]))
    q -= 1
