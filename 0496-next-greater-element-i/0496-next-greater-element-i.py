class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Let's have an index map to update the final result
        nums1_map={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        for n in nums2:
            while stack and n>stack[-1]:
                # pop the value which we found as we found the next greater
                val=stack.pop()
                # Get the index of this val for nums1
                idx=nums1_map[val]
                # Assign the next greater to it as we did find it
                res[idx]=n
            # If this is the number for which we need to find the next greater, we add it to stack
            if n in nums1_map:
                stack.append(n)
        return res

        