from collections import deque, defaultdict

def pathCounts(root):
    allPaths = []

    answer = defaultdict(int)
    q = deque()
    q.append((root, 0))
    while q:
        node, depth = q.popleft()

        if node.left is None and node.right is None:
            answer[depth +1] += 1

        if node.left:
            q.append((node.left, depth + 1))

        if node.right:
            q.append((node.right, depth + 1))


    for item in sorted(answer.keys()):
        print(item, answer[item], '$ ')
