class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        result1=[]
        result2=[]
        for n in nums1:
            if n not in nums2:
                result1.append(n)
        for n in nums2:
            if n not in nums1:
                result2.append(n)
        return [result1,result2]
        