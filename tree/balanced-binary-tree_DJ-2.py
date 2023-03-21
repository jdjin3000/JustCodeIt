# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0

            left_level = dfs(node.left)
            right_level = dfs(node.right)

            if left_level == -1 or right_level == -1 or abs(left_level - right_level) > 1:
                return -1

            return max(left_level, right_level) + 1

        return True if dfs(root) != -1 else False