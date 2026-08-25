class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for x in range(len(nums))]

        def dp(pos):
            if pos >= len(nums):
                return 0
            if memo[pos] == -1:
                memo[pos] = max(nums[pos] + dp(pos+2), dp(pos+1))
            return memo[pos]
        
        return dp(0)