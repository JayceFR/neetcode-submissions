class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {} #dict from amount to number of coins

        def change(coins, amount):
            if amount == 0:
                return 0
            numberOfCoins = -1 
            for coin in coins:
                if coin <= amount: 
                    if memo.get(amount - coin) is None:
                        noOfCoins = change(coins, amount - coin)
                        memo[amount - coin] = noOfCoins
                    if memo[amount - coin] != -1:
                        numberOfCoins = (1 + memo[amount - coin]) if numberOfCoins == -1 else min(numberOfCoins, (1 + memo[amount - coin]))
            return numberOfCoins
        
        return change(coins, amount)