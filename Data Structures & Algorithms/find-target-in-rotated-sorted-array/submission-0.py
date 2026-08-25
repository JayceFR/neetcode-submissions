class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        fp, rp = 0, (len(nums) - 1)
        while fp <= rp:
            if target == nums[fp]:
                return fp
            if target == nums[rp]:
                return rp
            mp = (fp + rp) // 2 
            if target == nums[mp]:
                return mp
            if nums[fp] < nums[mp]:
                # left sorted half 
                if target < nums[mp]:
                    if target < nums[fp]:
                        fp = mp + 1 
                    else:
                        rp = mp - 1 
                else:
                    fp = mp + 1 
            else:
                # right half
                if target < nums[mp]:
                    rp = mp - 1 
                else:
                    if target > nums[rp]:
                        rp = mp - 1 
                    else:
                        fp = mp + 1 
        return -1 



