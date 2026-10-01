class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Looks like a sliding window problem 

        # We can solve it in O(n*log(n)) by using binary search to find the suitable window size. 
        # Then we need to check if such a window exists in the nums array. 

        # But we need an O(n) solution. 
        # We just move the rp all the way to the time we can get sum >= total. 
        # And then we can see if we can move the fp to the next, preserving the sum >= total. 
        # If we can't we can keep moving the rp and then try moving the fp. 

        l, total = 0, 0
        if sum(nums) < target:
            return 0 
        res = len(nums)

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return res