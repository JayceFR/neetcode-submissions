class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for i in range(n)]

        def dp(pos):
            if pos == 1: 
                return 1 
            if pos == 2:
                return 2 
            if cache[pos-1] == -1:
                cache[pos-1] = dp(pos-1)
            if cache[pos-2] == -1:
                cache[pos-2] = dp(pos-2)
            return cache[pos-1] + cache[pos-2]
        
        return dp(n)