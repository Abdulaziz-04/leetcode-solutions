class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        mx_area=(min(height[r],height[l]))*(r-l)
        while l<r:
            if height[r]>height[l]: 
                l+=1
            else:
                r-=1
            mx_area=max(mx_area,min(height[r],height[l])*(r-l))   
        return mx_area   

        