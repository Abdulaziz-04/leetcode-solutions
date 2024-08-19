class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # There are 2 approaches to this problem
        """
        nlogn approach, we sort the array first
        -> now we know the max number of elements greater than the current element
        they are the length of the elements to the right
        -> Also, any the max_r between the range of the given numbers can also be a solution
        For this we maintain a prev pointer to keep track of previoius number
        -> We also need to handle duplicates in the loop
        nums.sort()
        max_r=len(nums)
        prev=-1
        i=0
        while i < len(nums):
            if nums[i]==max_r or prev < max_r < nums[i]:
                return max_r
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            prev=nums[i]
            i+=1
            max_r=len(nums)-i
        return -1
        """
        """
        O(n) solution
        -> Prefix array to keep track of total elements >= X
        -> Solution possible in range (1,n) n is length of arr
        -> so initialize the case with n with prefix value of all elements >=x
        -> Build upon this and verify if any of the cases match
        """
        n=len(nums)
        freq=[0]*(n+1)
        for x in nums:
            idx=x if x<n else n
            freq[idx]+=1
        target=0
        for i in range(n,-1,-1):
            target+=freq[i]
            if i==target:
                return i
        return -1


        
        