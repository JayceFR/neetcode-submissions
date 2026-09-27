class Solution:
    def numSquares(self, n: int) -> int:
        # Let dp[i] = the least number of perfect sqaures which sum to i
        # base case dp[0] = 0 
        # dp[i] = min(1 + dp[i - n]  for n in range(1, sqrt(i)))

        dp = [0] * (n+1)

        for i in range(1, n+1):
            res = i
            for n in range(1, i+1):
                sqr_n = n * n 
                if i - sqr_n >= 0:
                    res = min(res, 1 + dp[i - sqr_n])
            dp[i] = res
        
        return dp[n]