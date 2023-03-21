# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        q = deque()
        q.append((root, 1))
        while q:
            pointer, level = q.popleft()
            if pointer.left:
                q.append((pointer.left, level + 1))
            if pointer.right:
                q.append((pointer.right, level + 1))

        return level
        