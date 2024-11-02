class Solution:
    def trap(self, height: List[int]) -> int:
        maxL=[0]
        maxR=[0]
        l_height=0
        r_height=0
        total=0
        for i in range(1,len(height)):
            l_height=max(l_height,height[i-1])
            maxL.append(l_height)
        for i in range(len(height)-2,-1,-1):
            r_height=max(r_height,height[i+1])
            maxR.append(r_height)
        maxR=maxR[::-1]
        for l,h,r in zip(maxL,height,maxR):
            water=min(l,r)-h
            total+=water if water>0 else 0
        return total

        
        