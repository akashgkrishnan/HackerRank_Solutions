
def search(node, data):
    if node is None:
        return

    if node.data == data:
        return True

    if data > node.data:
        return search(node.right, data)
    elif data < node.data:
        return search(node.left, data)
