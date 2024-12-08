# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        best_level=1
        levels=1
        mx_sum=-float('inf')
        q=deque([root])
        while q:
            currSum=0
            for i in range(len(q)):
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                currSum+=curr.val
            if currSum>mx_sum:
                best_level=levels
                mx_sum=currSum
            levels+=1
        return best_level



        