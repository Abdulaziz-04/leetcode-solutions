# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,ll,rl):
            if not node:
                return True
            if not (node.val>ll and node.val<rl): 
                return False
            return dfs(node.left,ll,node.val) and dfs(node.right,node.val,rl)
        
        return dfs(root,-float('inf'),float('inf'))
        