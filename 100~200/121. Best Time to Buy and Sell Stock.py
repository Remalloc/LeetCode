class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if not prices:
            return result
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            result = max(price - min_price, result)
        return result
