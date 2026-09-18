class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Top down approach 
        # memo = {}
        # def dp(amount):
        #     if amount == 0:
        #         return 0 
        #     if memo.get(amount) is not None:
        #         return memo[amount]
        #     noOfCoins = -1 
        #     for c in coins:
        #         if c <= amount:
        #             restCoins = dp(amount - c)
        #             if restCoins != -1:
        #                 noOfCoins = (1 + restCoins) if noOfCoins == -1 else min(noOfCoins, 1 + restCoins)
        #     memo[amount] = noOfCoins 
        #     return memo[amount]
        
        # return dp(amount)

        # Bottom up approach, we maintain a list of amounts 

        dp = [(amount + 2) for x in range(amount + 1)] # length = 13
        dp[0] = 0 # For amount 0, there is only one option. Base case 
        for a in range(1, len(dp)):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[-1] if dp[-1] != amount + 2 else -1 