class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left_valid=i==0 or flowerbed[i-1]==0
                right_valid=i==len(flowerbed)-1 or flowerbed[i+1]==0
                if left_valid and right_valid:
                    flowerbed[i]=1
                    n-=1
        return n<=0

        