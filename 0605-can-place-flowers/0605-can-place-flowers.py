class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Thought process:
        We need 2 conditions to deal with a valid flowerbed
        left valid condition : index should be greater than zero or if there is valid flowerbed 
        right valid condition : index should be less than final length or if there is valid flowerbed next
        """
        for i in range(len(flowerbed)):
            # Check for conditions
            left_valid=i==0 or flowerbed[i-1]==0
            right_valid=i==len(flowerbed)-1 or flowerbed[i+1]==0
            # Check a valid point to put flower
            if flowerbed[i]==0:
                # If conditions meet put flower and reduce count
                if left_valid and right_valid:
                    flowerbed[i]=1
                    n-=1
            # If the provided flowers become <=0, return
            if n<=0:
                return True
        # Break condition not met
        return False 
            
            