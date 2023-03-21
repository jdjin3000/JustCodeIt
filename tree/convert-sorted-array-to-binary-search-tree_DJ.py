# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
            
        root_val = nums[len(nums)//2]
        root_left = nums[:len(nums)//2]
        root_right = nums[len(nums)//2 + 1:]

        root = TreeNode(val=root_val)
        root.left = self.sortedArrayToBST(root_left)
        root.right = self.sortedArrayToBST(root_right)

        return root