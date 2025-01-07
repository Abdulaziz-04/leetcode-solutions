class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff=[]
        for i in range(1,len(prices)):
            diff.append(prices[i]-prices[i-1])
        profit=0
        for d in diff:
            if d>0:
                profit+=d
        return profit
        