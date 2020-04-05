class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, price in enumerate(prices[1:]):
            if price > prices[i]:
                profit += price - prices[i]
        return profit
