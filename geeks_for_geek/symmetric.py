# return true/false denoting whether the tree is Symmetric or not
def isSym(leftTree, rightTree):
    if leftTree is None and rightTree is None:
        return True

    if leftTree is None or rightTree is None:
        return False


    if leftTree.data != rightTree.data:
        return False

    return isSym(leftTree.left, rightTree.right) and isSym(leftTree.right, rightTree.left)


def isSymmetric(root):
    return isSym(root, root)



def isSymmetric(root):
    if root is None:
        return True

    q = deque()
    q.append(root)
    q.append(root)

    while q:

        node1 = q.popleft()
        node2 = q.popleft()

        if node1 is None and node2 is None:
            continue

        elif node1 is None or node2 is None:
            return False

        if node1.data != node2.data:
            return False

        q.append(node1.left)
        q.append(node2.right)
        q.append(node1.right)
        q.append(node2.left)

    return True
