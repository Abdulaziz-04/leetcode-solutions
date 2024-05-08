class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Thought process: first if the length<3 :return False
        Keep track of the first smallest element found so far
        Keep track of second smallest element found so far
        compare it with the running third element and conclude
        """
        if len(nums)<3:
            return False
        f = float('inf')
        s = float('inf')
        for t in nums:
            if t <= f:
                f=t
            elif t<= s:
                s=t
            if t > f and t>s:
                return True
        return False
        
               

        