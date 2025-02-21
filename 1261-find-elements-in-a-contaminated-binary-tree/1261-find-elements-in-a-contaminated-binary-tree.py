# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def generate_values(self,node):
        if not node:
            return
        if node.left:
            left_val=2*node.val+1
            node.left.val=left_val
            self.nums.add(left_val)
            self.generate_values(node.left)
        if node.right:
            right_val=2*node.val+2
            node.right.val=right_val
            self.nums.add(right_val)
            self.generate_values(node.right)


    def __init__(self, root: Optional[TreeNode]):
        self.nums=set()
        self.root=root
        self.root.val=0
        self.nums.add(0)
        self.generate_values(self.root)
        

    def find(self, target: int) -> bool:
        return target in self.nums
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)