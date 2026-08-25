class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                p = dfs(i + 1, not buying) - prices[i]
                # dp[(i, buying)] = max(buy, cooldown)
            else:
                p = dfs(i + 2, not buying) + prices[i]

            dp[(i, buying)] = max(p, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
        