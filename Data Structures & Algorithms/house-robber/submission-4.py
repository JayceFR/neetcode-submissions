class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Top down 
        # memo = [-1 for x in range(len(nums))]

        # def dp(pos):
        #     if pos >= len(nums):
        #         return 0
        #     if memo[pos] == -1:
        #         memo[pos] = max(nums[pos] + dp(pos+2), dp(pos+1))
        #     return memo[pos]
        
        # return dp(0)

        # bottom up solution 
        # have 2 lists, prob can do one with a tuple 
        # robbed = [0] * len(nums)
        # passed = [0] * len(nums)
        
        # for pos, money in enumerate(nums):
        #     if pos == 0:
        #         robbed[pos] = money
        #     else:
        #         robbed[pos] = money + passed[pos-1]
        #         passed[pos] = max(robbed[pos-1], passed[pos-1])
        # e = len(nums) - 1
        # return max(robbed[e], passed[e])

        # bottom up: but with one list 

        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]