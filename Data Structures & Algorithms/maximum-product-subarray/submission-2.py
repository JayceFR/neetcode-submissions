class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # top down solution 
        # def dp(pos):
        #     if pos == 0:
        #         return nums[0], nums[0], nums[0]  # min, max, global

        #     mi, ma, ans = dp(pos - 1)

        #     curr_min = min(nums[pos], nums[pos] * mi, nums[pos] * ma)
        #     curr_max = max(nums[pos], nums[pos] * mi, nums[pos] * ma)

        #     return curr_min, curr_max, max(ans, curr_max)
        
        # return dp(len(nums)-1)[2]


        # more efficient 
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
