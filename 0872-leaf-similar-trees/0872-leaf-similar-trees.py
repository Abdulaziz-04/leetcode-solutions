# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,leaves):
            if not root:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
            dfs(root.left,leaves)
            dfs(root.right,leaves)
            return leaves
        l1=dfs(root1,[])
        l2=dfs(root2,[])
        return l1==l2
            
        