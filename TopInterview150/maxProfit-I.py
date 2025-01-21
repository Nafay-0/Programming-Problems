class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i]< buy:
                buy = prices[i]
            max_profit = max(max_profit, (prices[i] - buy))

        return max_profit