class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r=1,ranks[0]*cars**2
        result=0
        while l<=r:
            m=l+(r-l)//2
            curr=0
            for rank in ranks:
                curr+=int((m/rank)**0.5)
            if curr>=cars:
                result=m
                r=m-1
            else:
                l=m+1
        return result

        