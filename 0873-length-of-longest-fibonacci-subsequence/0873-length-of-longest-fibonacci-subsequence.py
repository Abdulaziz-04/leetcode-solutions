class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set=set(arr)
        result=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,curr=arr[i],arr[j]
                nxt=prev+curr
                l=2
                while nxt in num_set:
                    l+=1
                    prev,curr=curr,nxt
                    nxt=prev+curr
                    result=max(result,l)
        return result
        