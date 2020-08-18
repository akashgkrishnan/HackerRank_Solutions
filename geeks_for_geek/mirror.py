from collections import deque
# your task is to complete this function
def mirror(root):

    queue = deque()

    queue.append(root)
    while queue:
        node = queue.popleft()

        if node is None:
            continue

        node.left, node.right = node.right, node.left

        queue.append(node.left)
        queue.append(node.right)


    def travelNode(node, array):
        if node is not None:
            travelNode(node.left, array)
            array.append(node.data)
            travelNode(node.right, array)
        return array


    return travelNode(root, [])
