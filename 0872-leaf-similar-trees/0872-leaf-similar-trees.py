# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def find_leaf(node,result):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
                return result
            find_leaf(node.left,result)
            find_leaf(node.right,result)
            return result
        r1=find_leaf(root1,[])
        r2=find_leaf(root2,[])
        return r1==r2

        