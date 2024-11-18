# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
        dfs(root)
        actual_order=sorted(node.val for node in inorder)
        for i in range(len(actual_order)):
            inorder[i].val=actual_order[i]
        
            
        