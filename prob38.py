# 513
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        leftmost_value = 0

        def dfs(node, depth):
            nonlocal max_depth, leftmost_value
            if node:
                if node.left is None and node.right is None:
                    if depth > max_depth:
                        max_depth = depth
                        leftmost_value = node.val
                else:
                    dfs(node.left, depth + 1)
                    dfs(node.right, depth + 1)

        dfs(root, 0)
        return leftmost_value
