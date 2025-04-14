class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    c1=abs(arr[i]-arr[j])
                    c2=abs(arr[j]-arr[k])
                    c3=abs(arr[i]-arr[k])
                    if c1<=a and c2<=b and c3<=c:
                        total+=1
        return total
        