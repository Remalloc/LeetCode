class Solution(object):
    def maxProfit(self, prices):
        maxnum=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxnum+=prices[i]-prices[i-1]
        return maxnum
