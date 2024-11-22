class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        mxArea=min(height[l],height[r])*(r-l)
        while l<r:
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            print(mxArea)
            mxArea=max(mxArea,min(height[l],height[r])*(r-l))
        return mxArea
        