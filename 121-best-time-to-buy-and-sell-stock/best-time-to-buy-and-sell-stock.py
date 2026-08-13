class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_prices = prices[0]
        for i in range(len(prices)):
            price = prices[i]
            
            if min_prices > price:
                min_prices = price
            
            profit = price - min_prices
            
            if profit > max_profit:
                max_profit = profit
            
        return max_profit
