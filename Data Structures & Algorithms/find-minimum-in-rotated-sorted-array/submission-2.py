class Solution:
    def findMin(self, nums: List[int]) -> int:
        fp, rp = 0, (len(nums) - 1)

        res = nums[0]
        while fp < rp:
            if nums[fp] < nums[rp]:
                res = min(nums[fp], res)
                break
            
            mp = (fp + rp) // 2 
            res = min(res, nums[rp])
            res = min(res, nums[mp])
            if nums[fp] < nums[mp]:
                fp = mp + 1 
            else:
                rp = mp - 1 
        return res 
            
