class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        # Initial max area
        mx_area= (r-l)*min(height[l],height[r])
        while l<=r:
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            curr_area=(r-l)*min(height[l],height[r])
            mx_area=max(mx_area,curr_area)
        return mx_area
        