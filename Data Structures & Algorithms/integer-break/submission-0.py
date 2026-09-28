class Solution:
    def integerBreak(self, n: int) -> int:
        # Let dp[i] = the max product of integers that are broken to sum i 
        dp = [0] * (n+1)
        dp[1] = 1 
        for i in range(2, n + 1):
            res = i - 1 
            for j in range(1, i):
                res = max(j * max(dp[i-j], i-j), res)
            dp[i] = res 
        print(dp)
        return dp[n]