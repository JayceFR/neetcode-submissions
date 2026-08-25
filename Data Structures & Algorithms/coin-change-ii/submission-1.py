class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {} # (total, pos) -> 1 or 0
        def dp(total, pos):
            
            if pos >= len(coins) or total > amount:
                return 0

            if total == amount: # found a valid path 
                return 1

            if (total, pos) in memo:
                return memo[(total, pos)]
            
            # copy the previous
            l = dp(total + coins[pos], pos)

            # go to the new one 
            r = dp(total, pos + 1)

            memo[(total, pos)] = l + r 
            return memo[(total, pos)]
        
        return dp(0,0)

