class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0 
            if memo.get(amount) is not None:
                return memo[amount]
            noOfCoins = -1 
            for c in coins:
                if c <= amount:
                    restCoins = dp(amount - c)
                    if restCoins != -1:
                        noOfCoins = (1 + restCoins) if noOfCoins == -1 else min(noOfCoins, 1 + restCoins)
            memo[amount] = noOfCoins 
            return memo[amount]
            
        
        return dp(amount)