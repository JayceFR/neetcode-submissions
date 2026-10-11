class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        # Need to keep track of how far can i jump basically. 
        '''
        [1,2,0,1,0]

        curr = 0
        max_pos = 0 
        while curr <= max_pos or something like that. 
        '''
        curr = 0 
        max_pos = 0 
        while curr < len(nums) and curr <= max_pos:
            max_pos = max(max_pos, curr + nums[curr])
            curr += 1
        return max_pos >= len(nums) - 1