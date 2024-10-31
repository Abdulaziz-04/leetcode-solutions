class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        # Go through each index and height in heights
        for i,h in enumerate(heights):
            # Store everything in pairs
            # for backward extension keep the index as is for now
            start=i
            # If we are not able to extend our top of stack i.e. 6 >>> 2 then we need to pop 6
            # Calculate area and update it
            while stack and stack[-1][1]>h:
                pop_index,pop_h=stack.pop()
                maxArea=max(maxArea,pop_h*(i-pop_index))
                # Revert till here
                start=pop_index
            stack.append((start,h))    
        # For values remaining in stack which reached the end
        for i,h in stack:    
            maxArea=max(maxArea,h*(len(heights)-i))
        return maxArea    


        