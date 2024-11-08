# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[root]
        result=[]
        while q:
            levels=[]
            for i in range(len(q)):
                node=q.pop(0)
                if node:
                    levels.append(node.val)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                result.append(levels)
        return result
            


        