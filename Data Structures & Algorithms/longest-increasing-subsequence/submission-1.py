class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        
        def dp(pos):
            if pos > len(nums):
                return 0 
            if pos == len(nums) - 1:
                return 1 
            if pos in memo:
                return memo[pos]

            curr = nums[pos]

            memo[pos] = 1
            for x in range(pos+1, len(nums)):
                if nums[x] > curr:
                    memo[pos] = max(memo[pos], 1 + dp(x))
            
            return memo[pos]
        
        ret = 0
        for x in range(len(nums)):
            ret = max(ret, dp(x))
        
        return ret 
                
