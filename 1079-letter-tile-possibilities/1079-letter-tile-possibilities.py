from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq=Counter(tiles)
        seen=set()
        result=[0]
        def backtrack(i,curr):
            if i>len(tiles):
                return
            for t in tiles:
                if len(curr)>0 and curr not in seen:
                    seen.add(curr)
                    result[0]+=1
                if freq[t]>0:
                    freq[t]-=1
                    curr+=t
                    backtrack(i+1,curr)
                    freq[t]+=1
                    curr=curr[:-1]
        backtrack(0,"")
        print(seen)
        return result[0]

        