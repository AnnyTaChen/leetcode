class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = prices[0]
        for i in range(len(prices)):
            if min_profit > prices[i]:
                min_profit = prices[i]
            max_profit = max(prices[i]-min_profit,max_profit)
        return max_profit
