# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0

        if not root:
            return 0

        if root.val < low:
            rangeSum += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            rangeSum += self.rangeSumBST(root.left, low, high)
        else:
            rangeSum += root.val
            rangeSum += self.rangeSumBST(root.left, low, high)
            rangeSum += self.rangeSumBST(root.right, low, high)

        return rangeSum

        