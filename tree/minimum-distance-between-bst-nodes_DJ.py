# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minDistance = float('inf')

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(root):
            if not root:
                return []

            # inorder traversal
            left_traversal = inorder_traversal(root.left)
            root_val = root.val
            right_traversal = inorder_traversal(root.right)

            # traversal이 끝난 후 선언해야 한다!!! 재귀 중에 self.minDistance가 바뀔 수 있기 때문.
            candidates = [self.minDistance]
            
            if left_traversal:
                candidates.append(abs(left_traversal[-1] - root_val))
            if right_traversal:
                candidates.append(abs(right_traversal[0] - root_val))

            self.minDistance = min(candidates)
            
            return left_traversal + [root_val] + right_traversal

        inorder_traversal(root)

        return self.minDistance