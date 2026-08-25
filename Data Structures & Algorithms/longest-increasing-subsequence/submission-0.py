class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dp(pos):
            if pos > len(nums):
                return 0 
            if pos == len(nums) - 1:
                return 1 
            curr = nums[pos]

            ret = 1
            for x in range(pos+1, len(nums)):
                if nums[x] > curr:
                    ret = max(ret, 1 + dp(x))
            
            return ret
        
        ret = 0
        for x in range(len(nums)):
            ret = max(ret, dp(x))
        
        return ret 
                
