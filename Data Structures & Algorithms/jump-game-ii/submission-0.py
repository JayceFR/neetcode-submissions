class Solution:
    def jump(self, nums: List[int]) -> int:
        # its a greedy problem of just finding the max element in the current window. We can just increment the jump variable as we find it 

        j = 0 
        l, r = 0, 0 
        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1 
            r = farthest
            j += 1 
        return j 