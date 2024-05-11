class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Let's attempt to pair the most heaviest with the most lightest in boat
        """
        # Sort them
        people.sort()
        # two pointer to find a pair
        l,r=0,len(people)-1
        boats=0
        # If both land at same index, we will need one boat as one person remains
        while l<=r:
            # If pair found move to next persons
            if people[l]+people[r]<=limit:
                boats+=1
                l+=1
                r-=1
            # If overweight then we need a single boat and we can move to next
            else:
                r-=1
                boats+=1
        return boats
            

        