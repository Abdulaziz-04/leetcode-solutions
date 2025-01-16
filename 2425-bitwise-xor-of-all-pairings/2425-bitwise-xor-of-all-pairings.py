class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        x1,x2=0,0
        n1,n2=len(nums1),len(nums2)
        if n1%2:
            for n in nums2:
                x2=x2^n
        if n2%2:
            for n in nums1:
                x1=x1^n
        return x1^x2

                

        