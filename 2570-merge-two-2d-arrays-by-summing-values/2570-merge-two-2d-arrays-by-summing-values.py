class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l,r=0,0
        result=[]
        while l<len(nums1) and r<len(nums2):
            id1,id2=nums1[l][0],nums2[r][0]
            val1,val2=nums1[l][1],nums2[r][1]
            if id1==id2:
                result.append([id1,val1+val2])
                l+=1
                r+=1
            elif id1<id2:
                result.append([id1,val1])
                l+=1
            else:
                result.append([id2,val2])
                r+=1
        while l<len(nums1):
            result.append(nums1[l])
            l+=1
        while r<len(nums2):
            result.append(nums2[r])
            r+=1
        return result
        