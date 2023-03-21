# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None or root2 is None:
            return root1 if root1 is not None else root2

        def dfs(node1, node2): # node1에 통합하는 방향으로
            if node1 is None or node2 is None:
                return False
            
            node1.val = node1.val + node2.val

            if not dfs(node1.left, node2.left):
                node1.left = node1.left if node1.left is not None else node2.left
                
            if not dfs(node1.right, node2.right):
                node1.right = node1.right if node1.right is not None else node2.right

        dfs(root1, root2)

        return root1