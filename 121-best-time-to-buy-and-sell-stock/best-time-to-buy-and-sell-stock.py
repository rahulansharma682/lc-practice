class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cheapPrice = prices[0]
        for p in prices[1:]:
            cheapPrice = min(cheapPrice, p)
            profit = max(profit, p - cheapPrice)
        return profit


        