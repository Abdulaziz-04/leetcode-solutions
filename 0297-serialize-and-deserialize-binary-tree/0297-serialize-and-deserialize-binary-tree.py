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
        result=[]
        def pre(node):
            if not node:
                result.append('N')
                return
            result.append(str(node.val))
            pre(node.left)
            pre(node.right)
            return result
        pre(root)
        return ",".join(result)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0
        result=data.split(',')
        def dfs():
            if result[self.i]=='N':
                self.i+=1
                return None
            node=TreeNode(int(result[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))