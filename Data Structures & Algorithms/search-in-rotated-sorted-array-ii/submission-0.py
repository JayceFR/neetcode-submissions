class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = 0
        while n < len(nums) - 1 and nums[n] <= nums[n+1]:
            n += 1 
        n += 1 

        fp = 0 
        rp = len(nums) - 1 
        while fp <= rp:
            mp = (fp + rp) // 2 
            val = nums[(mp + n) % len(nums)]
            if target > val:
                fp = mp + 1 
            elif target < val:
                rp = mp - 1 
            else:
                return True 
        return False 