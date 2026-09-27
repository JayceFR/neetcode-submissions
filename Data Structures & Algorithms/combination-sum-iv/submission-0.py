class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Let dp[i] = number of distinct ways of making i from nums 
        # base case dp[0] = 1 
        # dp[i] = dp[i - n] for n in nums

        dp = [0] * (target + 1)
        dp[0] = 1 
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]