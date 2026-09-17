class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        # top down (just add memo)
        # but only bottom up passes the hackerrank OAs 
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        dp = [0, 1, 1]
        for i in range(3, n+1):
            new_dp = [0, 0, 0]
            new_dp[2] = dp[0] + dp[1] + dp[2]
            new_dp[1] = dp[2]
            new_dp[0] = dp[1]
            dp = new_dp
        return dp[2]