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
                if node2.left: # node1.left is None
                    node1.left = node2.left
                
            if not dfs(node1.right, node2.right):
                if node2.right: # node1.right is None
                    node1.right = node2.right

            # 아래 return True가 없으면 오류가 발생함.
            # why? if not dfs(node1.right, node2.right) line에서 parameter 2개 모두 None이 아니어서 정상적으로 완료되도 return None이 되서 return False됐을 때와 똑같이 작동해버림.
            return True

        dfs(root1, root2)

        return root1