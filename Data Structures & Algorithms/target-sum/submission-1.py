class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(pos, amount):
            if pos >= len(nums):
                if amount == 0:
                    return 1 
                return 0 

            if (pos,amount) in memo:
                return memo[(pos, amount)]
            
            l = dp(pos+1, amount + nums[pos])
            r = dp(pos+1, amount - nums[pos])

            memo[(pos, amount)] = l + r 
            return memo[(pos, amount)]
        
        return dp(0, target)