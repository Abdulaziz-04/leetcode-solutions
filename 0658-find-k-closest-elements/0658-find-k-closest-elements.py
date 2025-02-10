class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while l<r:
            m=l+(r-l)//2
            if arr[m]<x:
                l=m+1
            else:
                r=m
        l,r=l-1,l
        while r-l-1<k:
            if l<0:
                r+=1
            elif r>=len(arr):
                l-=1
            elif abs(arr[l]-x)<=abs(arr[r]-x):
                l-=1
            else:
                r+=1
        return arr[l+1:r]

        