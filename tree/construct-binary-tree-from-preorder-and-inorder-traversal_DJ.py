# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # pre-order 순으로 진행 (preorder.pop이 root - left - right 순으로 진행)
            root = TreeNode(preorder.pop(0))

            # Divide & Conquer
            # index 기준으로 왼쪽 element들은 root 왼쪽에 존재함. (inorder list니까)
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])

            return root