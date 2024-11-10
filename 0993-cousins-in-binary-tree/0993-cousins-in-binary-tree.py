# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=[(root,0,None)]
        result=[]
        while q:
            if len(result)==2:
                break
            for i in range(len(q)):
                curr,depth,parent=q.pop(0)
                if curr:
                    if curr.val==x or curr.val==y:
                        result.append((depth,parent))
                    q.append((curr.left,depth+1,curr))
                    q.append((curr.right,depth+1,curr))
        ix,iy=result
        return ix[0]==iy[0] and ix[1]!=iy[1]

        