class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.total=0
        self.left=None
        self.right=None
class NumArray:
        

    def __init__(self, nums: List[int]):
        self.root=self.createTree(nums,0,len(nums)-1)

    def createTree(self,nums,l,r):
        if l>r:
            return None
        if l==r:
            curr=Node(l,r)
            curr.total=nums[l]
            return curr
        mid=l+(r-l)//2
        root=Node(l,r)
        root.left=self.createTree(nums,l,mid)
        root.right=self.createTree(nums,mid+1,r)
        root.total=root.left.total+root.right.total
        return root
        
    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root,index,val)

    def updateTree(self,root,index,val):
        if root.start==root.end:
            root.total=val
            return val
        
        mid=root.start + (root.end-root.start)//2
        if index<=mid:
            self.updateTree(root.left,index,val)
        else:
            self.updateTree(root.right,index,val)
        root.total=root.left.total+root.right.total
        return root.total
        

    def sumRange(self, left: int, right: int) -> int:
        return self.getRange(self.root,left,right)

    def getRange(self,root,l,r):
        if root.start==l and root.end==r:
            return root.total
        mid=root.start+(root.end-root.start)//2

        if r<=mid:
            return self.getRange(root.left,l,r)
        elif l>=mid+1:
            return self.getRange(root.right,l,r)
        else:
            return self.getRange(root.left,l,mid)+self.getRange(root.right,mid+1,r)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)