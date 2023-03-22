# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"

        queue  = [root]
        answer = []

        while queue:
            node = queue.pop(0)

            if node:
                answer.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                answer.append('null')

        return '[' + ','.join(answer) + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        data = [i for i in data[1:-1].split(',')]

        root = TreeNode(data.pop(0))
        queue = [root]

        while data or queue:
            node = queue.pop(0)
            left, right = data.pop(0), data.pop(0)

            if left != 'null':
                node.left = TreeNode(left)
                queue.append(node.left)
            
            if right != 'null':
                node.right = TreeNode(right)
                queue.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))