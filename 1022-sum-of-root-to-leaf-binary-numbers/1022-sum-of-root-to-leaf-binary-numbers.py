# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result=[]
        def dfs(root,num):
            if not root:
                return
            num+=str(root.val)
            if not root.left and not root.right:
                result.append(num)
                return
            dfs(root.left,num)
            dfs(root.right,num)
        dfs(root,"")
        total=0
        for r in result:
            total+=int(r,2)
        return total
        