class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        max_depth = 1
        while stack:
            node, depth = stack.pop()
            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))
            max_depth = max(depth, max_depth)
        return max_depth
