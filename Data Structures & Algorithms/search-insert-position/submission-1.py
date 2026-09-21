class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bs #
        '''
        -1 0 2 4 6 8 
        '''
        lp = 0 
        rp = len(nums) - 1 
        found = False 
        while lp <= rp and not found:
            mp = (lp + rp) // 2 
            if target < nums[mp]:
                rp = mp - 1 
            elif target > nums[mp]:
                lp = mp + 1 
            else:
                found = True
        if found:
            return (lp + rp) // 2  
        return lp 