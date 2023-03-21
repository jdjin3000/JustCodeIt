# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, level):
            if node is None:
                return level - 1

            left_level = dfs(node.left, level + 1)
            right_level = dfs(node.right, level + 1)

            if abs(left_level - right_level) > 1:
                self.balanced = False

            return max(left_level, right_level)

        dfs(root, 0)

        return self.balanced