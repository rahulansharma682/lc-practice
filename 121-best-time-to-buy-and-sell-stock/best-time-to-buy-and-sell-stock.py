class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        minPrice = prices[0]

        for p in prices[1:]:
            if p < minPrice:
                minPrice = p
            else:
                best = max(best, p - minPrice)

        return best


        