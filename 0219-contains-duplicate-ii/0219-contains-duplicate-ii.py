class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l=0
        curr_window=set([nums[l]])
        for r in range(1,len(nums)):
            if r-l>k:
                curr_window.remove(nums[l])
                l+=1
            if nums[r] in curr_window: 
                return True
            curr_window.add(nums[r])
        return False

        