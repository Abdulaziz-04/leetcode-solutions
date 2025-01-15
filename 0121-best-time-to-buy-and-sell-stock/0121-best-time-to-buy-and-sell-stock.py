class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        mx_profit=0
        for r in range(1,len(prices)):
            if prices[l]>prices[r]:
                l=r
            else:
                mx_profit=max(mx_profit,prices[r]-prices[l])
        return mx_profit
        