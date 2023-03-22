# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.SumOfGreaterNodes = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        greater_nodes = []
        
        def inorder_traversal(root): # 더 큰 값을 더해줘야 하니, 중위 순회를 반대로 right - root - left 순으로.
            if not root:
                return

            inorder_traversal(root.right)

            root.val += self.SumOfGreaterNodes
            self.SumOfGreaterNodes = root.val

            inorder_traversal(root.left)
        
        inorder_traversal(root)

        return root