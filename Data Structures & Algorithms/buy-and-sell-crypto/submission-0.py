class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if (len(prices) == 0):
            return profit
        minTerm = prices[0]
        for curr in prices:
            if curr < minTerm:
                minTerm = curr 
            profit = max(profit, curr - minTerm)
        return profit 
