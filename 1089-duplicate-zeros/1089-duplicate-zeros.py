class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count=arr.count(0)
        n=len(arr)
        for i in range(n-1,-1,-1):
            if i+zero_count<n:
                arr[i+zero_count]=arr[i]
            if arr[i]==0:
                zero_count-=1
                if i+zero_count<n:
                    arr[i+zero_count]=0
        return arr
       