class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
            if len(freq)<=2:
                continue
            new_freq=defaultdict(int)
            for n,c in freq.items():
                if c>1:
                    new_freq[n]=c-1
            freq=new_freq
        result=[]
        for n in freq.keys():
            if nums.count(n)>len(nums)//3:
                result.append(n)
        return result
        