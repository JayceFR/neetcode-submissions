class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(lp, rp):
            if lp > rp:
                return -1 
            mp = (lp + rp) // 2 
            if nums[mp] > target:
                return bs(lp, mp - 1)
            elif nums[mp] < target:
                return bs(mp+1, rp)
            else:
                return mp 
        
        return bs(0, len(nums) - 1)