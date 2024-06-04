class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Needs to be valid to have a valid solution
        if sum(gas)<sum(cost):
            return -1
        # If we have a valid solution, the diff sum should be greater than 0
        # If not then we skip to the next position, our next position will be 
        # our solution as it didn't drop below zero which shows we were able to visit
        # all stations
        total=0
        start=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                start=i+1
        return start
        