class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(pos, amount):
            if pos >= len(nums):
                if amount == 0:
                    return 1 
                return 0 
            
            l = dp(pos+1, amount + nums[pos])
            r = dp(pos+1, amount - nums[pos])

            return l + r 
        
        return dp(0, target)