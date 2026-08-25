class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(profit, buy, pos):

            if pos >= len(prices):
                return profit 
            
            cooldown = dp(profit, buy, pos+1)

            if buy: 
                p = dp(profit - prices[pos], not buy, pos +1)
            else:
                p = dp(profit + prices[pos], not buy, pos + 2)
            
            return max(p, cooldown)
        
        return dp(0, True, 0)
        