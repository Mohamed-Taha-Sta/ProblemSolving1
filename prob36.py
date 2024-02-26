# 100
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    print(isSameTree([1, 2, 3], [1, 2, 3]))  # True
    print(isSameTree([1, 2], [1, None, 2]))  # False
    print(isSameTree([1, 2, 1], [1, 1, 2]))  # False
