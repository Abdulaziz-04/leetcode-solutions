class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums)<2:
            return 0
        freq_map={}
        for n in nums:
            if n not in freq_map:
                freq_map[n]=1
            else:
                freq_map[n]+=1
        pairs=0
        for n in nums:
            # Check for opp. number in map and check if current number has sufficient freq
            if k-n in freq_map and freq_map[n]>0:
                freq_map[n]-=1
                if freq_map[k-n]>0:
                    freq_map[k-n]-=1
                    pairs+=1
        return pairs

        