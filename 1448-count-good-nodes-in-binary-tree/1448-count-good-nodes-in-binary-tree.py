# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good=0
        stack=[(root,root.val)]
        while stack:
            curr,cMax=stack.pop()
            if curr:
                if curr.val>=cMax:
                    good+=1
                nMax=max(curr.val,cMax)
                stack.append((curr.left,nMax))
                stack.append((curr.right,nMax))
        return good
            

        