from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map=defaultdict(int)
        unique_freq=set()
        for n in arr: 
            freq_map[n]+=1
        for n in freq_map.values():
            if n in unique_freq:
                return False
            unique_freq.add(n)
        return True
        