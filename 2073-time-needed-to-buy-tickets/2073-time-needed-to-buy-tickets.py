class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        for i in range(len(tickets)):
            # We only care for the kth customer, so we collect those many tickets on the run
            if i<=k:
                time+=min(tickets[i],tickets[k])
            else:
                # After our customer, the last round won't continue till the end
                # i.e. second last round only
                time+=min(tickets[i],tickets[k]-1)
        return time

        